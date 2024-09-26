import os
import sys
import json

from collections import Counter
from func import read_text, write_text


def frequency(original_file: str, frequency_file: str) -> None:
    """
    Count frequency for each letter in input file.

    Args:
        original_file: Path to the source .txt file.
        frequency_file: Path to save the frequency analysis. .txt file.
    """
    cipher = read_text(original_file)
    frequency_counter = Counter(cipher)
    total_length = len(cipher)

    result = ""
    for char, count in frequency_counter.most_common():
        result += f"{char}: {round(count / total_length, 5)}\n"

    write_text(frequency_file, result)


def read_key_json(key_json_file: str) -> dict:
    """
    Read key from a JSON file.
    
    Args:
        key_json_file: Path to read the encryption key as .json file.
    """
    with open(key_json_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def decode(original_file: str, result_file: str, key_json_file: str) -> None:
    """
    Decoding text from input file with given key.
    
    Args:
        original_file: Path to the source .txt file.
        result_file: Path to save the encrypted .txt file.
        key_json_file: Path to store the encryption key as .json file.
    """
    cipher = read_text(original_file)
    key = read_key_json(key_json_file)

    result: str = ""
    try:
        for i in cipher:
            result += key.get(i, i)
    except Exception as error:
        print("An error occurred during decryption:", error)

    write_text(result_file, result)