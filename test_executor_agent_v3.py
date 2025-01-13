from smolagents import CodeAgent, HfApiModel
from tools.tools import read_testcase_file, save_code_to_file, execute_api_test
from dotenv import load_dotenv
import os


# Load environment variables from .env
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
host = os.getenv("API_HOST")

model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"


test_executor_agent = CodeAgent(
    tools=[read_testcase_file, save_code_to_file, execute_api_test],
    model=HfApiModel(model_id=model_id, token=access_token), 
    additional_authorized_imports=['requests', 'bs4', 'pytest-bdd', 'pytest-html', 'json']
)


"""
write test code
"""
test_executor_agent.run(
   """
   can you write and save pytest code for test case file using request module
   additional_args={"filename":'api_test.feature', "codefilename": "api_test.py", "code":"code_response"}
   """
)

"""
Execute test
"""
test_executor_agent.run(
   """
   can you execute api test from saved file
   additional_args={"codefilename": "api_test.py"}
   """
)