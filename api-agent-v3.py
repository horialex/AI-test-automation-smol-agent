from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
host = os.getenv("API_HOST")

# Initialize the agent with the Hugging Face token
api_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(token=access_token),
    additional_authorized_imports=['requests', 'bs4', 'pytest']
)


# Run the agent and let it dynamically generate the test based on the input
test_input = f"Write a pytest for a GET endpoint at {host}/products/1 and check if the status is 200. Create an assertion for this and return me a message indicating if the test passed or not."

# Let the agent create the test based on the description
api_agent.run(test_input)
