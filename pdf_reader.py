import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()


# Configure the Gemini API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    """
    Extracts all text content from a PDF file uploaded to Streamlit.

    Args:
        pdf_file: The file-like object uploaded via Streamlit.

    Returns:
        str: A single string containing all the text from the PDF.
    """
    # Create PdfReader directly from the file-like object
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_pdf_with_llm(pdf_text, question):
    # This part of the code remains the same
    llm_prompt = f"Based on the following document content, answer this question: {question}\n\nDocument content:\n{pdf_text}"
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(llm_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# --- Streamlit App Interface ---
st.set_page_config(page_title="PDF Q&A with Gemini")
st.title("📄 PDF Q&A with Google Gemini")
st.markdown("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.markdown(f"**Filename:** {uploaded_file.name}")
    
    with st.spinner("Extracting text from PDF..."):
        # Pass the uploaded file object directly to the function
        pdf_content = extract_text_from_pdf(uploaded_file)
    st.success("Text extraction complete!")
    
    user_question = st.text_area("Ask a question about the document:")
    
    if st.button("Get Answer"):
        if user_question:
            st.info("Thinking...")
            with st.spinner("Analyzing document with LLM..."):
                llm_response = analyze_pdf_with_llm(pdf_content, user_question)
            
            st.markdown("---")
            st.subheader("LLM Answer:")
            st.write(llm_response)
        else:
            st.warning("Please enter a question.")

