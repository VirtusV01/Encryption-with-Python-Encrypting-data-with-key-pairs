import argparse
import encrypt_decrypt

def main():
    parser = argparse.ArgumentParser(description="CLI Encryption and Decryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: encrypt or decrypt")
    parser.add_argument("--data", required=True, help="Data to encrypt or decrypt")
    parser.add_argument("--public-key", help="Path to public key (for encryption)")
    parser.add_argument("--private-key", help="Path to private key (for decryption)")

    args = parser.parse_args()

    if args.action == "encrypt":
        if not args.public_key:
            print("Please provide the path to the public key using --public-key.")
            return
        with open(args.public_key, "rb") as f:
            public_key = f.read()
        encrypted_data = encrypt_decrypt.encrypt_data(public_key, args.data)
        print("Encrypted Data:", encrypted_data)

    elif args.action == "decrypt":
        if not args.private_key:
            print("Please provide the path to the private key using --private-key.")
            return
        with open(args.private_key, "rb") as f:
            private_key = f.read()
        decrypted_data = encrypt_decrypt.decrypt_data(private_key, args.data)
        print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
