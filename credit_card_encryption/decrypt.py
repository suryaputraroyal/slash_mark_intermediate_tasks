# decrypt.py
from cryptography.fernet import Fernet
import boto3
import os

def load_key():
    return open("keys/key.key", "rb").read()

def decrypt_credit_card(encrypted_card):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_card).decode()
    return decrypted

def download_from_s3(bucket, file_name, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    try:
        s3_client.download_file(bucket, object_name, file_name)
        print(f"Downloaded {file_name} from {bucket}/{object_name}")
    except Exception as e:
        print(f"Error downloading {file_name}: {e}")

if __name__ == "__main__":
    bucket_name = "your-s3-bucket-name"
    file_name = "encrypted_card.txt"
    download_from_s3(bucket_name, file_name)

    with open(file_name, "rb") as file:
        encrypted_card = file.read()

    decrypted_card = decrypt_credit_card(encrypted_card)
    print(f"Decrypted credit card number: {decrypted_card}")
