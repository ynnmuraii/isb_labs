import os
import logging
import json


logging.basicConfig(level=logging.DEBUG)

def read_file(path: str) -> bytes:
    """
    Load a file in binary mode.

    Args:
        path (str): Path to the file.

    Returns:
        bytes: The binary data read from the file.
    """
    if not os.path.exists(path):
        logging.warning(f"File not found: {path}")
        return b''

    try:
        with open(path, 'rb') as f:
            content = f.read()
            logging.debug(f"Successfully loaded {len(content)} bytes from '{path}'")
            return content
    except OSError as err:
        logging.error(f"Failed to load file '{path}': {err}")
        return b''


def write_file(path: str, content: bytes) -> None:
    """
    Save binary data to a file.

    Args:
        path (str): Path to the file.
        content (bytes): Data to be written to the file.

    Returns:
        None
    """
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
        logging.info(f"Directory created: {dir_name}")

    try:
        with open(path, 'wb') as f:
            f.write(content)
            logging.debug(f"Written {len(content)} bytes to file '{path}'")
    except OSError as err:
        logging.error(f"Error while writing to file '{path}': {err}")
        

def read_json(path: str) -> dict:
    """
    Read data from a JSON file and return it as a dictionary.
    
    Args:
        path (str): Path to the JSON file.
    
    Returns:
        dict: Data from the JSON file.
    """
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            logging.debug(f"Successfully read JSON file '{path}'")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON file: {path}")
    except Exception as e:
        logging.error(f"Unexpected error occurred while reading the file '{path}': {e}")
        

def write_file(filepath: str, content: str) -> None:
    """
    Save the provided data to a file.

    Args:
        filepath (str): The path to the file where the data will be saved.
        content (str): The data to be written to the file.
    """
    try:
        with open(filepath, "w", encoding='UTF-8') as f:
            f.write(content)
        logging.debug(f"Data successfully saved to '{filepath}'.")
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
    except OSError as e:
        logging.error(f"Failed to write to file '{filepath}': {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
