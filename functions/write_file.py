import os
from google.genai import types
from prompts import system_prompt

def write_file(working_directory, file_path, content):
    try:
        target = os.path.abspath(os.path.join(working_directory, file_path))
        if not target.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file in the working directory with optional args.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Optional command-line arguments to pass to the script.",
            ),
        },
        required=["file_path", "content"],
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_run_python_file,
    ]
)

config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)