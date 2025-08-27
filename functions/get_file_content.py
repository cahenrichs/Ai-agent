import os
from google.genai import types
from prompts import system_prompt

def get_file_content(working_directory, file_path):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            MAX_CHARS = 10000
            with open(target_path, "r") as f:
                file_content_string = f.read(MAX_CHARS + 1)
            if MAX_CHARS < len(file_content_string):
                return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content_string
    except Exception as e:
        return f"Error: '{e}'"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a file in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
available_functions = types.Tool(
    function_declarations=[
        schema_get_file_content,
    ]
)

config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)