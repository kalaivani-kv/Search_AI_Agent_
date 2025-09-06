from dotenv import load_dotenv
import os

from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool
from groq import Groq

# loading enironment variables 
load_dotenv()
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

agent = Agent(
    'groq:llama-3.1-8b-instant',
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt='Search Tavily for the given query and return the results.'
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output
