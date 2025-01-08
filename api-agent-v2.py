from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access the token
access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

# Initialize the agent with the Hugging Face token
api_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(token=access_token),
    additional_authorized_imports=['requests', 'bs4', 'pytest']
)

print(access_token)

server = "http://172.21.128.1:3000"

api_agent.run(f"write pytest for GET endpoint ${server}/products/1 and check status is 201 and create an assertion for this and return me message that tells if test passed or not")
#api_agent.run("write pytest for GET endpoint http://172.21.128.1:3000/products and check status is 200")