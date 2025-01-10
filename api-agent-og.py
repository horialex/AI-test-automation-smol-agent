from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv
import os



# Load environment variables from .env
load_dotenv()

# Access the token
access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


api_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4', 'pytest'])
print(access_token)
api_agent.run("write pytest for GET endpoint https://httpbin.org/get and check status is 200")
# api_agent.run("write pytest for GET endpoint https://httpbin.org/get and check status is not 300, 500, 302")

