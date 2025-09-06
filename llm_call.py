import os
import google.generativeai as genai

# Configure the API key from an environment variable.
# It is highly recommended to set this in your system environment.
# For example, on Linux/macOS: export GOOGLE_API_KEY='your_api_key_here'
# Or for a quick test, you can uncomment the line below and paste your key.
genai.configure(api_key='AIzaSyDLRB_JuPItiHQDL-f5oUqqh5XUPJo5-jE')

# The API key is automatically picked up from the environment variable GOOGLE_API_KEY
# If you didn't set it in your environment, the 'genai.configure' line above is necessary.

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

