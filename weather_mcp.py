from fastmcp import FastMCP
import google.generativeai as genai
import os

# Get the API key from an environment variable for security
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Instantiate a FastMCP server.
mcp = FastMCP("GeminiMCP")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Returns mock weather information for a given city.
    Args:
        city: The name of the city.
    """
    mock_weather = {
        "london": "Sunny, 30°C",
        "new york": "Cloudy, 25°C",
        "tokyo": "Rainy, 22°C",
        "gurugram": "Hot and Humid, 35°C",
    }
    return mock_weather.get(city.lower(), "Weather information not available.")

@mcp.tool()
def generate_response(prompt: str) -> str:
    """
    Generates a response using the Gemini API based on a text prompt.
    Args:
        prompt: The text prompt to send to the Gemini model.
    """
    if not genai.configure.api_key:
        return "Error: Gemini API key is not configured."
        
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API error: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")

