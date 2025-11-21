# VityarthiProject
VITyarthi - Build Your Own Project

---

# Automated Resume Evaluator

This project is a simple web-based tool that evaluates resumes by extracting text, identifying skills, estimating experience, and generating a final score along with suggestions. It uses a lightweight frontend (HTML, CSS, JavaScript) and a Python Flask backend.

---

## 📌 Features
- Upload resumes in **PDF**, **DOC**, or **DOCX** format  
- Extracts and cleans resume text  
- Detects technical and soft skills  
- Estimates experience from date ranges  
- Generates a resume score and suggestions  
- Simple and beginner-friendly interface  

---

## 🛠 Technology Stack

### Frontend
- HTML  
- CSS  
- JavaScript (Fetch API)

### Backend
- Python (Flask)  
- PyPDF2  
- python-docx  

---

## 🚀 How to Run the Project

###   Install the Project File

#### 1.	Software Requirements
- **Backend**: Python 3.8 or above installed
- **Frontend**: A modern web browser (Chrome, Edge, Firefox, etc.)

  Install required python libraries for the backend

  Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux), then type:

  ```
  pip install flask PyPDF2 python-docx
  ```

#### 2.	Start the Backend Server
- Open the project folder.
- Go to the backend directory and open the file `app.py`.

  The backend will start at: http://127.0.0.1:5000
  
❗Keep this window open while using the project.

#### 3.	Open the Frontend
-	Go to the frontend directory.
-	Open the file `index.html`.
-	The website will open in the default browser immediately.

#### 4.	How to Use the System
-	Click “Upload Resume” on the webpage.
-	Choose a file (PDF, DOC, or DOCX).
-	Click Submit.
-	Wait a moment while the backend processes the file.
-	The results will appear on the page
  
    💠Skills detected

    💠Resume score

    💠Experience estimate

    💠Suggestions for improvement

---

## ⚙️ Instructions for Testing

#### 1. Test File Upload
Open the website, click Upload Resume, choose a PDF/DOC/DOCX file, and click Submit.
The file should upload without errors.

#### 2. Check Resume Processing
After submitting, wait a few seconds.
You should see skills, score, experience, and suggestions on the screen.

#### 3. Try Different File Types
Upload different resume formats (PDF, DOC, DOCX).
The system should work for all supported formats.

#### 4. Test Error Handling
Try uploading an unsupported file or click Submit without selecting a file.
An error message should appear.

#### 5. Test Full Workflow
Start the backend (python app.py), open index.html, upload a resume, and view the results.
Everything should work smoothly from upload to output.

---

## 📸 Screenshot

<img width="1536" height="1024" alt="Screenshot" src="https://github.com/user-attachments/assets/b079175b-65db-49e8-828a-daee0a23d963" />




