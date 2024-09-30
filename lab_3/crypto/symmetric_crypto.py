import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from functions import read_byte_file, write_byte_file, write_file


class Symmetric:
    """
    Class for SM4 key management and symmetric encryption/decryption.
    
    Attributes:
        _key: The SM4 encryption key.
    """

    def __init__(self):
        self._key = None

    def create_key(self) -> None:
        """
        Generate a random 16-byte SM4 key for encryption.
        """
        self._key = os.urandom(16)

    def load_key(self, filepath: str) -> None:
        """
        Load the symmetric key from a file.
        
        Args:
            filepath (str): Path to the file containing the key.
        """
        try:
            with open(filepath, "rb") as key_file:
                self._key = key_file.read()
            print(f"Key loaded from '{filepath}'")
        except OSError as e:
            print(f"Error loading key: {e}")

    def save_key(self, filepath: str) -> None:
        """
        Save the symmetric key to a file.
        
        Args:
            filepath (str): File path to save the key.
        """
        try:
            with open(filepath, 'wb') as key_file:
                key_file.write(self._key)
            print(f"Key saved to '{filepath}'")
        except OSError as e:
            print(f"Error saving key: {e}")

    def encrypt_data(self, input_filepath: str, output_filepath: str) -> None:
        """
        Encrypt the content of a file using the SM4 algorithm in CFB mode.
        
        Args:
            input_filepath (str): Path to the file with the data to be encrypted.
            output_filepath (str): Path to save the encrypted data.
        """
        try:
            data = read_byte_file(input_filepath)
            iv = os.urandom(16)
            cipher = Cipher(algorithms.SM4(self._key), modes.CFB(iv))
            encryptor = cipher.encryptor()

            padder = padding.ANSIX923(32).padder()
            padded_data = padder.update(data) + padder.finalize()

            encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()
            write_byte_file(output_filepath, encrypted_data)
            print(f"Data encrypted and saved to '{output_filepath}'")
        except OSError as e:
            print(f"Error during encryption: {e}")

    def decrypt_data(self, input_filepath: str, output_filepath: str) -> None:
        """
        Decrypt the content of a file using the SM4 algorithm in CFB mode.
        
        Args:
            input_filepath (str): Path to the file with the encrypted data.
            output_filepath (str): Path to save the decrypted data.
        """
        try:
            encrypted_data = read_byte_file(input_filepath)
            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]

            cipher = Cipher(algorithms.SM4(self._key), modes.CFB(iv))
            decryptor = cipher.decryptor()

            decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

            unpadder = padding.ANSIX923(128).unpadder()
            unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

            decoded_data = unpadded_data.decode('UTF-8')
            write_file(output_filepath, decoded_data)
            print(f"Data decrypted and saved to '{output_filepath}'")
        except OSError as e:
            print(f"Error during decryption: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print(f"Encrypted data size: {len(encrypted_data)} bytes")
