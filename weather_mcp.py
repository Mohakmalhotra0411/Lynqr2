from fastmcp import FastMCP
import asyncio

# Instantiate a FastMCP server.
mcp = FastMCP("WeatherMCP")

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

if __name__ == "__main__":
    # The stdio transport is suitable for connecting with local clients.
    mcp.run(transport="stdio")
