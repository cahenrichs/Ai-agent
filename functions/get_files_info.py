import os

def get_files_info(working_directory, directory="."):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, directory))
        ab = os.path.abspath(working_directory)
        if not target_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        lines = []
        if os.path.isdir(target_path):
            for item in os.listdir(target_path):
                item_path = os.path.join(target_path, item)
                item_size = os.path.getsize(item_path)
                item_is_dir = os.path.isdir(item_path)
                # Format a string for this item...
                line = f'- {item}: file_size={item_size} bytes, is_dir={item_is_dir}'
                lines.append(line)
            return "\n".join(lines) 
    except Exception as e:
        return f'Error: {e}'
