# Encryption with Python: Encrypting data with key pairs

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This project demonstrates how to perform encryption and decryption of data using RSA key pairs in Python. It provides a Command-Line Interface (CLI) tool to encrypt and decrypt data.

## Requirements

- Python 3.x installed.
- PyCryptodome library. Install it using
  ```bash
  pip install pycryptodome
  ```

## Features

- Generate RSA key pairs (public and private keys).
- Encrypt data with the public key.
- Decrypt data with the private key.

## Usage

1. **Generate key pairs:**

   To generate the RSA key pairs, run the following commands:

   ```bash
   python cli.py generate-keys > private_key.pem
   python cli.py generate-keys --public > public_key.pem
   ```

# Encrypt data:

To encrypt data using the public key, use the following command:

```bash
python cli.py encrypt --data "Hello, this is a secret message." --public-key public_key.pem
```

Replace public_key.pem with the path to your public key file, and the output will be the encrypted data.

# Decrypt data:

To decrypt the encrypted data using the private key, run the following command:

```bash
python cli.py decrypt --data "ENCRYPTED_DATA_HERE" --private-key private_key.pem
```

Replace ENCRYPTED_DATA_HERE with the encrypted data obtained from the encryption step, and private_key.pem with the path to your private key file.

# License
This project is licensed under the GNU License.
