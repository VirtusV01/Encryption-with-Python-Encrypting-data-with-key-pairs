from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_data(public_key, data):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()

def decrypt_data(private_key, encrypted_data):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data.encode())).decode()
    return decrypted_data

# Example usage:
private_key, public_key = generate_key_pair()
print("Private Key:", private_key)
print("Public Key:", public_key)

original_data = "Hello, this is a test!"
encrypted_data = encrypt_data(public_key, original_data)
print("Encrypted Data:", encrypted_data)

decrypted_data = decrypt_data(private_key, encrypted_data)
print("Decrypted Data:", decrypted_data)
