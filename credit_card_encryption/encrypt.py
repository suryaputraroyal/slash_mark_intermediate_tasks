# prakash,s credit card encrypt.py
from cryptography.fernet import Fernet
import boto3
import os

def load_key():
    return open("keys/key.key", "rb").read()

def encrypt_credit_card(card_number):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(card_number.encode())
    return encrypted

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded {file_name} to {bucket}/{object_name}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

if __name__ == "__main__":
    card_number = "1234-5678-9876-5432"
    encrypted_card = encrypt_credit_card(card_number)

    with open("encrypted_card.txt", "wb") as file:
        file.write(encrypted_card)

    bucket_name = "your-s3-bucket-name"
    upload_to_s3("encrypted_card.txt", bucket_name)
