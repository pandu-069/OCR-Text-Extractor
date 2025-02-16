from flask import Flask, render_template, request, url_for# type: ignore
import os
import cv2 # type: ignore
import pytesseract #type: ignore
import openai #type: ignore

# Configuration Class
class Config:
    UPLOAD_FOLDER = 'static/uploads'
    TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update path based on installation
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

# Image Processing Class
class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path

    def preprocess_image(self):
        """ Convert image to grayscale and apply thresholding for better OCR. """
        image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return gray

    def extract_text(self):
        """ Run Tesseract OCR on the processed image. """
        pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD
        processed_image = self.preprocess_image()
        extracted_text = pytesseract.image_to_string(processed_image)
        return extracted_text.strip()

# Text Enhancement Class
class TextEnhancer:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        """ Use OpenAI GPT to correct and enhance the extracted text. """
        client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        prompt = f"The following text is extracted from handwritten notes, which may include doctor prescriptions, shop bills, product names, or general notes. Your task is to analyze each word carefully, correct spelling and grammar, and improve readability while keeping the meaning unchanged. Predict unclear words based on common patterns in handwriting but do not add new information. Output only the corrected text without labeling or categorization:\n\n{self.text}"

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """ Render the main page. """
    return render_template('index.html', image_url=None, extracted_text="")

@app.route('/upload', methods=['POST'])
def upload_image():
    """ Handle image upload, extract text, enhance it, and return results. """
    if 'image' not in request.files:
        return render_template('index.html', error="No image uploaded!", image_url=None, extracted_text="")

    image = request.files['image']
    if image.filename == '':
        return render_template('index.html', error="No selected file!", image_url=None, extracted_text="")

    # Save the uploaded image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filepath)

    # Extract text using Tesseract
    processor = ImageProcessor(filepath)
    raw_text = processor.extract_text()

    # Enhance text using GPT
    enhancer = TextEnhancer(raw_text)
    cleaned_text = enhancer.clean_text()

    # Pass data to the front end
    image_url = url_for('static', filename=f'uploads/{image.filename}')
    return render_template('index.html', image_url=image_url, extracted_text=cleaned_text)

if __name__ == '__main__':
    app.run(debug=True)