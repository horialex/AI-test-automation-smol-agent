from smolagents import tool
from huggingface_hub import list_models
import subprocess
from markdownify import markdownify
from requests.exceptions import RequestException
import requests
import re
import json
from typing import Dict

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = ['model1', 'model2']
    return most_downloaded_model[0]


@tool
def write_testcase_file(filename: str, task: str) -> str:
    """
    Save a task description into a test case file and return the saved file name.

    This tool saves the provided task description into a file in the `test_cases` directory.
    If the directory does not exist, it will be created.

    Args:
        filename: The name of the test case file to be created. 
                    This should include the file extension (e.g., "test_case_1.txt").
        task: The task description or content to be saved in the file.

    Returns:
        str: A confirmation message with the name of the saved file.

    Raises:
        IOError: If the file cannot be created or written.
    """
    try:
        # Write the task to the specified file
        with open(f"features/{filename}", 'w') as file:
            file.write(task)

        print(f"File created successfully")
        return f"Saved file name is: {filename}"
    except IOError as e:
        return f"An error occurred while saving the file: {e}"

@tool
def read_testcase_file(filename: str, task: str) -> str:
    """
    Read the contents of a test case file and return its content.

    This tool reads the content of a specified test case file from the `test_cases` directory.
    If the file does not exist or cannot be read, an appropriate error message is returned.

    Args:
        filename: The name of the test case file to be read. 
                        This should include the file extension (e.g., "test_case_1.txt").
        task: The task to read file from filename.

    Returns: The content of the test case file if it is successfully read, 
             or an error message if the file cannot be found or read.
    """
    try:
        with open(f"features/{filename}", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except IOError as e:
        return f"Error: An I/O error occurred: {e}"

    print(f"File created successfully")
    return str(content)


@tool
def save_code_to_file(code: str, codefilename: str) -> str:
    """
    Save LLM-generated code into a specified file.

    Args:
        code: The code to be saved into the file. This should be a valid string containing Python or any other language code.
        codefilename: The name of the file to save the code in. Defaults to "generated_code.py". 
                        The file will be created in the 'generated_code' directory.

    Returns:
        str: A confirmation message if the code is successfully saved, or an error message if something goes wrong.
    """
    
    try:
        with open(f"src/{codefilename}", "w") as file:
            file.write(code)
        return f"Code successfully saved to {codefilename}"
    except Exception as e:
        return f"Failed to save code: {e}"

@tool
def execute_api_test(codefilename: str) -> str:
    """
    Execute API test using pytest and return the result.
    
    Args:
        codefilename: Name of the test code file.
    """
    result = subprocess.run(
        ['pytest', f'./src/{codefilename}', '--html=report/report.html', '--self-contained-html'],
        capture_output=True, 
        text=True
    )    
    
    print("***** EXECUTING API TEST *****")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    if result.returncode != 0:
        return f"Test execution failed. Check the report and logs.\nError:\n{result.stderr}"
    
    return f"Test executed successfully. Saved file name is: {codefilename}"

@tool

def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    
@tool
def write_api_test_report(filename: str, report_data: Dict[str, str]) -> str:
    """
    Writes an API test report to a JSON file.

    Args:
        filename: The name of the file to save the report (e.g., "api_test_report.json").
        report_data: A dictionary containing test report details such as:
                     - Host
                     - Request Type (GET, PUT, POST, etc.)
                     - Request Route
                     - Expected Status
                     - Actual Status
                     - Test Status (Passed or Failed)

    Returns:
        str: Confirmation message if the report is saved successfully, 
             or an error message if saving fails.
    """
    try:
        # Save the report as a JSON file
        with open(f"reports/{filename}", 'w') as file:
            json.dump(report_data, file, indent=4)

        return f"API test report saved to: {filename}"
    except IOError as e:
        return f"Error saving API test report: {e}"    