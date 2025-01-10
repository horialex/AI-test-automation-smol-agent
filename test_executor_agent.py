from smolagents import CodeAgent, HfApiModel
from tools.tools import report, read_testcase_file
from dotenv import load_dotenv
import os
import pytest_bdd

# Load environment variables from .env
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
host = os.getenv("API_HOST")

model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"


test_executor_agent = CodeAgent(
    tools=[read_testcase_file,report],
    model=HfApiModel(model_id=model_id,token=access_token), 
    additional_authorized_imports=['requests', 'bs4', 'pytest-bdd', 'pytest', 'json']
)

"""
Execute BDD style test cases from feature file
"""
test_executor_agent.run(
   """
   execute BDD api test case using only pytest-bdd using task "read_file" return test execution report in json format using task "report" and save.
   Do not hallucinate.
   additional_args={"filename":'api_test.feature'}
   """
)