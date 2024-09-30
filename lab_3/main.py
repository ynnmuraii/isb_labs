import argparse

from crypto.symmetric_crypto import Symmetric
from crypto.asymmetric_crypto import Asymmetric
from crypto.hybrid_crypto import generation, encryption, decryption, encryption_sym, decryption_sym
from functions import read_settings


def menu():
    """
    Displays the command line menu for the application.
    
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation')
    group.add_argument('-enc', '--encryption')
    group.add_argument('-dec', '--decryption')
    group.add_argument('-enc_sym', '--encryption_symmetric')
    group.add_argument('-dec_sym', '--decryption_symmetric')
    parser.add_argument("setting", type=str)

    args = parser.parse_args()
    setting = read_settings(args.setting)
    symmetric = Symmetric()
    asymmetric = Asymmetric()
    match args:
        case args if args.generation:
            generation(symmetric, asymmetric, setting["public_key"], setting["private_key"], setting["sym_key"])
        case args if args.encryption:
            encryption(symmetric, setting["sym_key"], setting["original_file"], setting["encrypted_file"])
        case args if args.decryption:
            decryption(symmetric, setting["sym_key"], setting["encrypted_file"], setting["decrypted_file"])
        case args if args.encryption_symmetric:
            encryption_sym(symmetric, asymmetric, setting["sym_key"], setting["public_key"], setting["encrypted_sym_key"])
        case args if args.decryption_symmetric:
            decryption_sym(symmetric, asymmetric, setting["sym_key"], setting["private_key"], setting["encrypted_sym_key"], 
                                     setting["decrypted_sym_key"])
        case _:
            print("The wrong action was selected")


if __name__ == "__main__":
    menu()
