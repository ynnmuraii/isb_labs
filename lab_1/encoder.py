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
        shift_value: Number of positions to shift the alphabet.
    """
    alphabet = ALPHABET
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

    write_text(result_file, encrypted_text)
    save_json(key_json_file, cipher_map)


def main() -> None:
    """
    Example function to call encoder with hardcoded parameters. Or just main.
    """
    original_file = "lab_1/task1/original.txt"    
    result_file = "lab_1/task1/result.txt"   
    key_json_file = "lab_1/task1/key.json"      
    shift_value = 3                          

    encode(original_file, result_file, key_json_file, shift_value)

if __name__ == "__main__":
    main()

