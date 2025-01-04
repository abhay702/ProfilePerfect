

# ProfilePerfect: AI-Powered Resume Analyzer

**ProfilePerfect** is an advanced ATS (Applicant Tracking System) resume optimization tool. It analyzes resumes against job descriptions, providing professional feedback, match percentages, and keyword insights to help job seekers enhance their resumes for better alignment.

---

## Tech Stack

| Technology | Purpose |
|---------------------------|--------------------------------------|
| **Python 3.10** | Programming Language |
| **Streamlit** | Web Application Framework |
| **Google Generative AI** | AI-powered Resume Analysis |
| **pdf2image & Pillow** | PDF Content Extraction |
| **dotenv** | Secure API Key Management |

---

## Installation Guide

Follow these steps to set up and run **ProfilePerfect** on your local machine.

### 1. Clone the Repository

Clone the repository from GitHub and navigate to the project folder:

```bash
git clone https://github.com/abhay702/ProfilePerfect.git
cd ProfilePerfect
```

### 2. Set Up a Virtual Environment

To isolate dependencies, create and activate a virtual environment:

**On Windows:**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Project Dependencies

Use the `requirements.txt` file to install all required libraries:

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

1. Create a `.env` file in the **root directory** of the project.
2. Add your Google Generative AI API key:

```
GOOGLE_API_KEY=your-google-api-key
```

Replace `your-google-api-key` with your valid API key from Google.

### 5. Run the Application

Launch the Streamlit app using the following command:

```bash
streamlit run app.py
```

The application will start, and you can access it in your browser at:

```
http://localhost:8501
```

## How to Use ProfilePerfect

### 1. Upload Your Resume
- Upload your resume in **PDF format** using the file uploader in the app.

### 2. Enter Job Description
- Paste the job description into the text area provided.

### 3. Analyze Your Resume
- **Review Resume**: Get HR-style professional feedback on strengths, weaknesses, and alignment.
- **Percentage Match**: Analyze alignment percentage, identify missing keywords, and receive actionable recommendations.

### 4. Review Results
- Review the generated insights to identify strengths, weaknesses, and areas for improvement.


## Screenshots

![image](https://github.com/user-attachments/assets/71823305-07a9-4dd5-a4ca-7aa6340acb6e)

![image](https://github.com/user-attachments/assets/decf90a2-3fb1-400c-b641-2ba3d622d664)

![image](https://github.com/user-attachments/assets/c258cf06-9d68-4073-a77f-a82cfdc23097)


![image](https://github.com/user-attachments/assets/0df42660-e983-40be-996c-c306972e02cc)

![image](https://github.com/user-attachments/assets/e5b57391-8ec1-4c13-900c-8aab92aa9c79)
