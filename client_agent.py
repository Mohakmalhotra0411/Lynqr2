from fastmcp import Client
import asyncio
import os

async def main():
    config = {
        "mcpServers": {
            # Use the name defined in the server, e.g., "GeminiMCP".
            "gemini": { 
                "command": "python",
                "args": ["weather_mcp.py"],
            }
        }
    }
    
    client = Client(config)

    async with client:
        print("Connecting to MCP server...")
        
        # Call the existing weather tool
        city_to_check = input("Enter the city you want to check ")
        print(f"\nRequesting weather for {city_to_check}...")
        try:
            forecast = await client.call_tool(
                "gemini_get_weather", 
                {"city": city_to_check}
            )
            print(f"Received from server: {forecast}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Ensure your API key is set before running.
    # For example: os.environ['GEMINI_API_KEY'] = 'YOUR_API_KEY'
    asyncio.run(main())
