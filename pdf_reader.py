import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

             
# Configure the Gemini API key
genai.configure(api_key='AIzaSyDLRB_JuPItiHQDL-f5oUqqh5XUPJo5-jE')

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_pdf_with_llm(pdf_path, question):
    """
    Extracts text from a PDF and uses an LLM to answer a question about it.
    """
    pdf_text = extract_text_from_pdf(pdf_path)

    # Construct the prompt for the LLM.
    # We include both the PDF content and the user's question.
    llm_prompt = f"Based on the following document content, answer this question: {question}\n\nDocument content:\n{pdf_text}"
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(llm_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
    

# --- Streamlit App Interface ---
st.set_page_config(page_title="PDF Q&A with Gemini")
st.title("📄 PDF Q&A with Google Gemini")
st.markdown("Upload a PDF and ask questions about its content.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Display the name of the uploaded file
    st.write("File uploaded successfully!")
    st.markdown(f"**Filename:** {uploaded_file.name}")
    
    # Extract text from the uploaded PDF
    with st.spinner("Extracting text from PDF..."):
        pdf_content = extract_text_from_pdf(uploaded_file)
    st.success("Text extraction complete!")
    
    # Input box for the user's question
    user_question = st.text_area("Ask a question about the document:")
    
    if st.button("Get Answer"):
        if user_question:
            st.info("Thinking...")
            # Get the LLM's answer
            with st.spinner("Analyzing document with LLM..."):
                llm_response = analyze_pdf_with_llm(pdf_content, user_question)
            
            st.markdown("---")
            st.subheader("LLM Answer:")
            st.write(llm_response)
        else:
            st.warning("Please enter a question.")
