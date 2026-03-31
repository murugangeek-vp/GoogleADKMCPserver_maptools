import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import  McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

load_dotenv()

MAPS_API_KEY = os.getenv("MAPS_API_KEY")

MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp" # Google-hosted Maps MCP endpc

maps_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=MAPS_MCP_URL,
        headers={
            "X-Goog-Api-Key": MAPS_API_KEY,
        },
    )
)

root_agent = LlmAgent(
    name="maps_mcp_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant that can answer questions about Google Maps."
    "use the mcp provided maps tools to answer the questions"
    "when direction are requested, include the travel mode in the response and google maps link in the final answer",
    description="Root agent for the Google Maps MCP server",
    tools=[maps_toolset],
)
