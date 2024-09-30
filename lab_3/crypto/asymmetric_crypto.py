import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding


class Asymmetric:
    """
    Class for RSA key management and asymmetric encryption/decryption

    Attributes:
        _private_key: The RSA private key.
        _public_key: The RSA public key.
    """

    def __init__(self):
        self._private_key = None
        self._public_key = None

    def create_key_pair(self, key_size: int = 2048) -> None:
        """
        Generate RSA key pair (private and public keys).

        Args:
            key_size (int): Length of RSA key (default is 2048 bits).
        """
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        self._public_key = self._private_key.public_key()

    def save_public_key(self, filepath: str) -> None:
        """
        Save the public key to a PEM file.

        Args:
            filepath (str): File path to save the public key.
        """
        try:
            with open(filepath, 'wb') as pub_file:
                pub_file.write(self._public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            print(f"Public key saved to '{filepath}'")
        except OSError as e:
            print(f"Error saving public key: {e}")

    def save_private_key(self, filepath: str) -> None:
        """
        Save the private key to a PEM file.

        Args:
            filepath (str): File path to save the private key.
        """
        try:
            with open(filepath, 'wb') as priv_file:
                priv_file.write(self._private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))
            print(f"Private key saved to '{filepath}'")
        except OSError as e:
            print(f"Error saving private key: {e}")

    def load_public_key(self, filepath: str) -> None:
        """
        Load a public key from a PEM file.

        Args:
            filepath (str): File path of the public key.
        """
        try:
            with open(filepath, 'rb') as pub_file:
                key_data = pub_file.read()
                self._public_key = load_pem_public_key(key_data)
            print(f"Public key loaded from '{filepath}'")
        except OSError as e:
            print(f"Error loading public key: {e}")

    def load_private_key(self, filepath: str) -> None:
        """
        Load a private key from a PEM file.

        Args:
            filepath (str): File path of the private key.
        """
        try:
            with open(filepath, 'rb') as priv_file:
                key_data = priv_file.read()
                self._private_key = load_pem_private_key(key_data, password=None)
            print(f"Private key loaded from '{filepath}'")
        except OSError as e:
            print(f"Error loading private key: {e}")

    def encrypt_data(self, data: bytes) -> bytes:
        """
        Encrypts data using RSA algorithm.

        Args:
            data (bytes): Data to encrypt.

        Returns:
            bytes: Encrypted data.
        """
        try:
            return self._public_key.encrypt(
                data,
                rsa_padding.OAEP(
                    mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            print(f"Error encrypting data: {e}")
            return b''

    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        """
        Decrypts data using RSA algorithm.

        Args:
            encrypted_data (bytes): Data to decrypt.

        Returns:
            bytes: Decrypted data.
        """
        try:
            return self._private_key.decrypt(
                encrypted_data,
                rsa_padding.OAEP(
                    mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            print(f"Error decrypting data: {e}")
            return b''
