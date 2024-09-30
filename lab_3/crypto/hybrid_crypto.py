from crypto.symmetric_crypto import Symmetric
from crypto.asymmetric_crypto import Asymmetric
from functions import write_byte_file, read_byte_file


def generation(symmetric: Symmetric, asymmetric: Asymmetric,
                      path_public: str, path_private: str, path_symmetric: str) -> None:
    """Generates asymmetric and symmetric keys, saving them to specified files.
    
    Args:
        symmetric (Symmetric): An instance of the Symmetric class.
        asymmetric (Asymmetric): An instance of the Asymmetric class.
        path_public (str): Path to save the public key.
        path_private (str): Path to save the private key.
        path_symmetric (str): Path to save the symmetric key.
    """
    asymmetric.create_key_pair()
    asymmetric.save_public_key(path_public)
    asymmetric.save_private_key(path_private)
    symmetric.create_key()
    symmetric.save_key(path_symmetric)


def encryption(symmetric: Symmetric, path_symmetric: str, 
                      path_original: str, path_encrypted: str) -> None:
    """Encrypts a file using the symmetric key.
    
    Args:
        symmetric (Symmetric): An instance of the Symmetric class.
        path_symmetric (str): Path to the symmetric key file.
        path_original (str): Path to the original file to encrypt.
        path_encrypted (str): Path to save the encrypted file.
    """
    symmetric.load_key(path_symmetric)
    symmetric.encrypt_data(path_original, path_encrypted)


def decryption(symmetric: Symmetric, path_symmetric: str, 
                      path_encrypted: str, path_decrypted: str) -> None:
    """Decrypts an encrypted file using the symmetric key.
    
    Args:
        symmetric (Symmetric): An instance of the Symmetric class.
        path_symmetric (str): Path to the symmetric key file.
        path_encrypted (str): Path to the encrypted file.
        path_decrypted (str): Path to save the decrypted file.
    """
    symmetric.load_key(path_symmetric)
    symmetric.decrypt_data(path_encrypted, path_decrypted)


def encryption_sym(symmetric: Symmetric, asymmetric: Asymmetric,
                             path_symmetric: str, path_public: str, 
                             path_enc_sym_key: str) -> None:
    """Encrypts the symmetric key using the public key.
    
    Args:
        symmetric (Symmetric): An instance of the Symmetric class.
        asymmetric (Asymmetric): An instance of the Asymmetric class.
        path_symmetric (str): Path to the symmetric key file.
        path_public (str): Path to the public key file.
        path_enc_sym_key (str): Path to save the encrypted symmetric key.
    """
    symmetric.load_key(path_symmetric)
    asymmetric.load_public_key(path_public)
    symmetric_key = symmetric._key
    encrypted_symmetric_key = asymmetric.encrypt_data(symmetric_key)
    write_byte_file(path_enc_sym_key, encrypted_symmetric_key)


def decryption_sym(symmetric: Symmetric, asymmetric: Asymmetric,
                             path_symmetric: str, path_private: str, 
                             path_enc_sym_key: str, path_dec_sym_key: str) -> bytes:
    """
    Decrypts the symmetric key using the private key.
    
    Args:
        symmetric (Symmetric): An instance of the Symmetric class.
        asymmetric (Asymmetric): An instance of the Asymmetric class.
        path_symmetric (str): Path to the symmetric key file.
        path_private (str): Path to the private key file.
        path_enc_sym_key (str): Path to the encrypted symmetric key file.
        path_dec_sym_key (str): Path to save the decrypted symmetric key.
    
    Returns:
        bytes: Decrypted symmetric key.
    """
    symmetric.load_key(path_symmetric)
    asymmetric.load_private_key(path_private)
    encrypted_symmetric_key = read_byte_file(path_enc_sym_key)
    decrypted_symmetric_key = asymmetric.decrypt_data(encrypted_symmetric_key)
    symmetric.save_key(path_dec_sym_key)
    return decrypted_symmetric_key

