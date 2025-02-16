# **Ctrl Alt Elite - OCR Text Extractor**

## 📌 **Overview**
Ctrl+Alt+Elite - OCR Text Extractor is a **Flask-based web application** that extracts text from images using **Tesseract OCR**, enhances the text using **OpenAI's GPT-3.5**, and displays the cleaned-up output.

## 🚀 **Features**
- Upload images containing handwritten or printed text
- Extract text using **Tesseract OCR**
- Enhance text clarity using **GPT-3.5**
- Simple and user-friendly web interface
- Supports noisy or unclear handwriting (e.g., doctor prescriptions, notes)

---

## 📂 **Project Structure**
```
/OCR-Text-Extractor
│── /static
│   ├── uploads/  (Stores uploaded images)
│── /templates
│   ├── index.html (Frontend UI)
│── app.py (Main Flask application)
│── config.py (Configuration settings)
│── requirements.txt (Dependencies)
│── README.md (Project Documentation)
│── test_images/ (Sample images for testing)
```

---

## 🛠️ **Installation Steps**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/pandu-069/OCR-Text-Extractor.git
cd OCR-Text-Extractor
```

### **2️⃣ Create a Virtual Environment**
```sh
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up OpenAI API Key**
Create an `.env` file in the root directory and add your OpenAI API key:
```sh
OPENAI_API_KEY="your-api-key-here"
```
Alternatively, set it manually in your terminal:
```sh
# Windows (Command Prompt)
set OPENAI_API_KEY="your-api-key-here"

# macOS/Linux
export OPENAI_API_KEY="your-api-key-here"
```

---

## 🚀 **Running the Application**
```sh
python app.py
```
The app will be available at:  
🔗 `http://127.0.0.1:5000/`

---

## 📷 **Testing the OCR**
1. Open the web app.
2. Upload an image containing handwritten or printed text.
3. Click **"Upload & Extract"** to process the image.
4. View the extracted and enhanced text.

---

## 🛠️ **Troubleshooting**
### **1️⃣ OpenCV Image Read Error (`cv2.error`)**
- Ensure the image path is correct.
- Try replacing `cv2.imread(image_path)` with:
  ```python
  image = cv2.imdecode(np.fromfile(image_path, np.uint8), cv2.IMREAD_COLOR)
  ```
  
### **2️⃣ OpenAI API Errors**
- Double-check your API key.
- Ensure you have enough OpenAI API credits.
- Use `temperature=0.3` to reduce randomness in text enhancement.

### **3️⃣ Flask Debugging**
If the app doesn't start, try:
```sh
flask run --debug
```

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 🤝 **Contributors**
- **Your Team Name (Ctrl+Alt+Elite)**
- **Team Members: [B VAMSI KRISHNA, B SAKETH, M PRAVEEN KUMAR, B SREEDHAR, S PUNEETH REDDY]**

