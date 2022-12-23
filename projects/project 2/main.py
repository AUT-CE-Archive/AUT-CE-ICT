# Standard imports
import pyaes
import os, base64, binascii, secrets
from pbkdf2 import PBKDF2
from dotenv import load_dotenv

load_dotenv()


def get_encryption_key() -> str:
    """ Returns the encryption key from the .env file """
    return os.getenv("ENCRYPTION_KEY")


def generate_salt() -> str:
    """ Returns a random salt """
    salt = os.urandom(16)   # 128-bit salt
    return base64.b64encode(salt).decode()


def enforce_encryption_key(key: str, salt: str) -> str:
    """ Enforces the encryption key by adding the salt to it, extend to 256 bits and hexlify it """
    return PBKDF2(key, salt).read(32) # 256-bit key


def get_vi() -> bytes:
    """ Returns a random initialization vector """
    return secrets.randbits(128)   # 128-bit IV


def read_plaintext() -> str:
    """ Reads the plaintext from the .env file """
    with open("plaintext.txt", "r") as f:
        return f.read()


def encrypt_plaintext(pbp: str, vi: int, plaintext: str) -> bytes:
    """ Encrypts the plaintext using AES-256-CBC """
    return pyaes.AESModeOfOperationCTR(pbp, pyaes.Counter(vi)).encrypt(plaintext)


def write_ciphertext_to_file(ciphertext: bytes, path: str = "ciphertext.txt") -> str:
    """ Saves the ciphertext to a file as binary """
    with open(path, "wb") as f:
        f.write(ciphertext)
    return path


def decrypt_ciphertext(pbp: str, vi: int, ciphertext: bytes) -> str:
    """ Decrypts the ciphertext using AES-CTR """
    return pyaes.AESModeOfOperationCTR(pbp, pyaes.Counter(vi)).decrypt(ciphertext).decode()


def read_ciphertext_from_file(path: str = "ciphertext.txt") -> bytes:
    """ Reads the ciphertext from a file as binary """
    with open(path, "rb") as f:
        return f.read()


if __name__ == '__main__':

    # Read and vet the encryption key
    key = get_encryption_key()
    print('Encryption key:', key)

    # Read and vet the salt
    salt = generate_salt()
    print('Salt:', salt)

    # Enforce the encryption key
    pbp = enforce_encryption_key(key, salt)
    print('Enforced encryption key:', binascii.hexlify(pbp).decode())
    print('Length of enforced encryption key:', len(pbp))

    # Generate a random IV
    vi = get_vi()
    print('Initialization vector:', vi)

    # Read the raw text for encryption
    plaintext = read_plaintext()
    print('Raw text:', plaintext)

    # Encrypt the plaintext
    ciphertext = encrypt_plaintext(pbp, vi, plaintext)

    # Write the ciphertext
    path = write_ciphertext_to_file(ciphertext)
    print("Ciphertext written to:", path)

    # Read the ciphertext
    ciphertext = read_ciphertext_from_file(path)
    print(f'Ciphertext read from "{path}":', ciphertext)

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt_ciphertext(pbp, vi, ciphertext)
    print('Decrypted text:', decrypted_plaintext)