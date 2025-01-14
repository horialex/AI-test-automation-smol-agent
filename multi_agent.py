from tools.tools import visit_webpage
import os
from dotenv import load_dotenv

from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)


load_dotenv()
access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
host = os.getenv("API_HOST")
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"

web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=HfApiModel(token=access_token),
    max_steps=10,
)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)

manager_agent = CodeAgent(
    tools=[],
    model=HfApiModel(token=access_token, model_id=model_id,),
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas", "requets"],
)

answer = manager_agent.run("If the Romania's GDP increases by this rate, on 2030 on what place would Romania be world wide and on what place is now and tell me the latest year that you have data on?")

print(answer)