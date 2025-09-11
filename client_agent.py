from fastmcp import Client
import asyncio
import os

async def main():
    # To connect to the local server running via stdio, you need a configuration
    # that specifies the command to execute your server script.
    config = {
        "mcpServers": {
            "weather": {
                "command": "python",
                "args": ["weather_mcp.py"],
            }
        }
    }
    
    # Create a client with the defined configuration.
    client = Client(config)

    # Use a context manager to ensure the client is properly started and closed.
    async with client:
        print("Connecting to MCP server...")

        # Call the get_weather tool on the 'weather' server.
        city_to_check = "London"
        print(f"Requesting weather for {city_to_check}...")
        try:
            forecast = await client.call_tool(
                "weather_get_weather", 
                {"city": city_to_check}
            )
            print(f"Received from server: {forecast}")
        except Exception as e:
            print(f"An error occurred: {e}")

        city_to_check = "Gurugram"
        print(f"\nRequesting weather for {city_to_check}...")
        try:
            forecast = await client.call_tool(
                "weather_get_weather", 
                {"city": city_to_check}
            )
            print(f"Received from server: {forecast}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
