import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import available_functions

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

user_prompt = next(arg for arg in sys.argv[1:] if not arg.startswith("--"))
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
model='gemini-2.0-flash-001', 
contents= messages,
config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
)
if response.function_calls:
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    print(response.text)



if "--verbose" in sys.argv:
    Prompt_tokens = response.usage_metadata.prompt_token_count
    Response_tokens = response.usage_metadata.candidates_token_count
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {Prompt_tokens}")
    print(f"Response tokens: {Response_tokens}")


