import json


def read_json(path_to_file: str) -> dict:
    """
    Read JSON content from a file.

    Args:
        path_to_file (str): Location of the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    try:
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError as file_error:
        raise FileNotFoundError(f"File {path_to_file} was not found.") from file_error
    except Exception as error:
        raise error


def save_json(path_to_file: str, data: dict) -> None:
    """
    Save a dictionary as JSON to a file.

    Args:
        path_to_file (str): Location to save the JSON file.
        data (dict): Data to be saved as JSON.

    Returns:
        None
    """
    try:
        with open(path_to_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except Exception as error:
        raise error
    
    
def read_text(path_to_file: str) -> str:
    """_summary_

    Args:
        path_to_file (str): _description_

    Returns:
        str: _description_
    """
    content = None
    
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Unable to locate file: {path_to_file}")
    except Exception as error:
        print(f"Unexpected error: {error}")
    return content


def write_text(path_to_file: str, content: str) -> bool:
    """
    Write given text content to a specified file.

    Args:
        path_to_file (str): Location of the .txt file to write.
        content (str): Text to be saved.

    Returns:
        bool: True if save was successful, False otherwise.
    """
    is_saved = True
    try:
        with open(path_to_file, 'w', encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Saving failed: file {path_to_file} not found.")
        is_saved = False
    except Exception as error:
        print(f"Unexpected error: {error}")
        is_saved = False
    return is_saved