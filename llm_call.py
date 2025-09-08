import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Access the API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))



def get_gemini_response(prompt_text):
    """
    Makes a simple API call to the Gemini model and returns the response text.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Define a general prompt
my_prompt = "What is the capital of France?"

# Get the response from the LLM
llm_response = get_gemini_response(my_prompt)

# Print the response
print(f"Prompt: {my_prompt}")
print(f"LLM Response: {llm_response}")


