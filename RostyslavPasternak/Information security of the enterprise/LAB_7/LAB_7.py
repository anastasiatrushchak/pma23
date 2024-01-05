from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import argparse
import os

def generate_key_pair(private_key_path, public_key_path):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    with open(private_key_path, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    public_key = private_key.public_key()
    with open(public_key_path, 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def encrypt_file(public_key_path, input_file_path, output_file_path):
    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    with open(input_file_path, 'rb') as f:
        data = f.read()

    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(private_key_path, input_file_path, output_file_path):
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    with open(input_file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description='RSA File Encryption/Decryption')
    parser.add_argument('--generate-keys', action='store_true', help='Генерація ключової пари RSA')
    parser.add_argument('--public-key', help='Шлях до файлу публічного ключа')
    parser.add_argument('--private-key', help='Шлях до файлу приватного ключа')
    parser.add_argument('--encrypt', help='Шлях до файлу для шифрування')
    parser.add_argument('--decrypt', help='Шлях до файлу для дешифрування')
    parser.add_argument('--output', help='Шлях до вихідного файлу')

    args = parser.parse_args()

    if args.generate_keys:
        if not args.public_key or not args.private_key:
            print("Будь ласка, вкажіть шлях до обох файлів: публічного та приватного ключів.")
            return
        generate_key_pair(args.private_key, args.public_key)
        print("Ключова пара RSA успішно згенерована.")
    elif args.encrypt:
        if not args.public_key or not args.output:
            print("Будь ласка, вкажіть шляхи до файлу публічного ключа та вихідного файлу.")
            return
        encrypt_file(args.public_key, args.encrypt, args.output)
        print("Файл успішно зашифровано.")
    elif args.decrypt:
        if not args.private_key or not args.output:
            print("Будь ласка, вкажіть шляхи до файлу приватного ключа та вихідного файлу.")
            return
        decrypt_file(args.private_key, args.decrypt, args.output)
        print("Файл успішно дешифровано.")
    else:
        print("Будь ласка, вкажіть вірну операцію: --generate-keys, --encrypt або --decrypt.")

if __name__ == "__main__":
    main()
