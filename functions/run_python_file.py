import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        target = os.path.abspath(os.path.join(working_directory, file_path))
        if not target.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: File "{file_path}" not found.'
        if not target.endswith(".py"):
            return f'Error: File "{file_path}" is not a Python file.'
        import subprocess

        result = subprocess.run(
            ["python", target, *args],
            cwd= working_directory,
            timeout=30,
            capture_output=True,
            text=True
            )
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
    except Exception as e:
        return f"Error: executing Python file: {e}"