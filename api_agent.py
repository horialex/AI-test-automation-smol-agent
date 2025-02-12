from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
host = os.getenv("API_HOST")

model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"

api_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(model_id = model_id,token=access_token),
    additional_authorized_imports=['requests', 'bs4', 'pytest', 'json'] 
)

expected_status_code = 200

# Define the test input prompt to include the request, response, and CSV writing
test_input = f"""
Write a pytest for a GET endpoint at {host}/products.
Check if the status is {expected_status_code}. 
Create an assertion for this and return the request URL, response content, and test status (passed or failed) in a properly formatted JSON object.
Ensure that:
- The JSON is correctly formatted with double quotes around keys and string values.
Return the following:
- request_url: The URL of the GET request
- actual response code
- expected response code
- test_status: 'Passed' if the status code is {expected_status_code}, otherwise 'Failed'

The output should be valid JSON, which can be parsed directly without any further modifications.
"""

response = api_agent.run(test_input)
print(response)
