from path import (
    original_decrypt_file, 
    original_encrypt_file, 
    frequency_file, 
    result_decrypt_file, 
    result_encrypt_file,
    key_decrypt_file, 
    key_encrypt_file)

from encoder import encode
from decoder import decode, frequency


def main() -> None:
    """
    Main function to perform encryption, frequency analysis, and decryption.
    """
    encode(original_encrypt_file, result_encrypt_file, key_encrypt_file, 3)
    print(f"Encryption complete. Check: {result_encrypt_file}")
    
    frequency(original_decrypt_file, frequency_file)
    print(f"Frequency analysis complete. Check: {frequency_file}")
    
    decode(original_decrypt_file, result_decrypt_file, key_decrypt_file)
    print(f"Decryption complete. Check: {result_decrypt_file}")
    
   
if __name__ == "__main__":
    main()
