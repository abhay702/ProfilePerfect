from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to process the PDF and extract the first page as an image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert the first page to base64
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(),
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to interact with the Gemini model
def get_gemini_response(input_prompt, pdf_content, job_description):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model name
    response = model.generate_content([input_prompt, pdf_content[0], job_description])
    return response.text

# Updated UI with a modern layout
st.set_page_config(page_title="ProfilePerfect 🚀", page_icon="📄", layout="centered")

# Header Section
st.title("📄 ProfilePerfect: ATS Resume Analyzer 🚀")
st.subheader("Optimize Your Resume to Match Your Dream Job")

# Job Description Input and Resume Upload
st.write("**🔎 Step 1: Paste the Job Description Below:**")
job_description = st.text_area("💼 Job Description", key="job_desc", height=150)

st.write("**📤 Step 2: Upload Your Resume (PDF Format):**")
uploaded_file = st.file_uploader("Upload your resume...", type=["pdf"])

# Display a success message when a file is uploaded
if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

# Buttons for different functionalities
col1, col2 = st.columns(2)
with col1:
    analyze_button = st.button("🧑‍💼 Review Resume")
with col2:
    match_button = st.button("📊 Match Percentage")

# Prompts for the AI model
review_prompt = """
You are a seasoned Human Resource Manager with years of experience in technical recruitment. 
Please review the uploaded resume against the provided job description and share your insights:
- Evaluate the candidate's profile alignment with the role.
- Highlight strengths, weaknesses, and areas for improvement.
- Provide a professional summary of your evaluation.
"""

match_prompt = """
You are an advanced ATS (Applicant Tracking System) with expertise in data analysis and recruitment technology.
Evaluate the uploaded resume against the provided job description and provide:
1. The **match percentage** (accuracy of alignment).
2. List of **missing keywords** or skills.
3. Final thoughts on how the candidate can enhance their resume to improve alignment.
"""

# Functionalities
if analyze_button:
    if uploaded_file and job_description:
        st.info("🔍 Analyzing the resume...")
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(review_prompt, pdf_content, job_description)
        st.subheader("🧑‍💼 Resume Review")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume and provide a job description.")

elif match_button:
    if uploaded_file and job_description:
        st.info("📊 Evaluating the resume for match percentage...")
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(match_prompt, pdf_content, job_description)
        st.subheader("📊 Resume Match Analysis")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume and provide a job description.")

# Footer
st.markdown(
    """
    ---
    **ProfilePerfect** helps you optimize your resume to align with job requirements using AI-powered analysis.  
    🛠 Developed with ❤️ by Abhay Rathore using Streamlit and Google Gemini.
    """
)


