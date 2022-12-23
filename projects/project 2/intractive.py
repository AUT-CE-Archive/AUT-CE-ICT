from main import *


if __name__ == '__main__':

    print("** AES-256-CTR Encryption and Decryption Program, developed by Keivan Ipchi Hagh **")

    # Read and vet the encryption key
    key = get_encryption_key()
    print('- Loaded Encryption key from ".env":', key, sep = '\t')

    # Read and vet the salt
    salt = generate_salt()
    print('- Generated 128-bit Random Salt:', salt, sep = '\t')

    # Enforce the encryption key
    pbp = enforce_encryption_key(key, salt)
    print(f'- Enforced encryption key:', f'{binascii.hexlify(pbp).decode()} (length: {len(pbp)})', sep = '\t\t')

    # Generate a random IV
    vi = get_vi()
    print('- Generated 128-bit (VI):', vi, sep = '\t\t')


    while True:

        choice = input('\n1. Encrypt a plaintext\n2. Decrypt a ciphertext\n3. Exit\nEnter your choice: ')
        if choice == '1':
            plaintext = input('Enter the plaintext: ')
            ciphertext = encrypt_plaintext(pbp, vi, plaintext)
            print('Ciphertext:', ciphertext)
            path = write_ciphertext_to_file(ciphertext)
            print('Ciphertext saved to', path)
        elif choice == '2':
            path = input('Enter the path to the ciphertext file (leave blank for default): ')
            ciphertext = read_ciphertext_from_file(path) if path != '' else read_ciphertext_from_file()
            plaintext = decrypt_ciphertext(pbp, vi, ciphertext)
            print('Decrypted text:', plaintext)
        elif choice == '3':
            break