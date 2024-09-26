import os
import sys

from constants import ALPHABET
from func import read_text, write_text, read_json, save_json

project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

def encode(original_file: str, result_file: str, key_json_file: str, shift_value: int) -> None:
    """
    Encrypt the text using Caesar cipher.

    Args:
        original_file: Path to the source .txt file.
        result_file: Path to save the encrypted .txt file.
        key_json_file: Path to store the encryption key as .json file.
    """
    alphabet = ALPHABET
    shift_value = 3
    encrypted_text = ""

    raw_text = read_text(original_file)
    if raw_text is None:
        raise FileNotFoundError(f"Could not read the original file: {original_file}")

    raw_text = raw_text.upper()
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    cipher_map = {}

    for original_char, shifted_char in zip(alphabet, shifted_alphabet):
        cipher_map[original_char] = shifted_char

    for char in raw_text:
        encrypted_text += cipher_map.get(char, char)

    encrypted_text = f'"{encrypted_text}"'
    
    save_json(key_json_file, cipher_map)
    write_text(result_file, encrypted_text)
    
    
    