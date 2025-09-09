from mcp import Tool
from mcp.server.fastmcp import FastMCP
import random

# The @tool() decorator is now imported directly and used correctly.
@Tool(name="get_weather")
def get_weather(city: str) -> str:
    """
    Returns the current weather for a given city.
    
    Args:
        city: The name of the city (e.g., "Hyderabad").

    Returns:
        A string describing the weather.
    """
    mock_responses = [
        "It's sunny and 30°C.",
        "It's cloudy with light rain, 27°C.",
        "There is a thunderstorm, 25°C."
    ]
    return f"According to the weather API, {random.choice(mock_responses)}"

# Run the MCP server to start listening for tool requests.
if __name__ == "__main__":
    # The function is also imported directly.
    mcp.run()