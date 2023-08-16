# CLI Based Encryption and Decryption Tool

This command-line tool allows you to encrypt and decrypt data using RSA encryption.

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Prerequisites

Before using this tool, ensure you have the following:

- Python (3.6 or higher)
- The `pycryptodome` library (install with ```pip install pycryptodome```)

## Install Dependencies

```bash
pip install -r requirements.txt
```
## Features

- Generate RSA key pairs (public and private keys).
- Encrypt data with the public key.
- Decrypt data with the private key.

## Getting Started

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Generate RSA key pairs (public and private keys) using the `generate_key_pair.py` script.

   ```bash
   python generate_key_pair.py

## Usage

1. **Generate key pairs:**

   To generate the RSA key pairs, run the following commands:

   ```bash
   python cli.py generate-keys > private_key.pem
   python cli.py generate-keys --public > public_key.pem
   ```
   This will create private_key.pem and public_key.pem files in the project directory.

## Encryption:

To encrypt data, follow these steps:
1. Make sure you have the public key file (public_key.pem) generated in the previous step.
2. Open a terminal and navigate to the project directory.
3. Use the CLI tool as follows to encrypt data:

```bash
python main.py encrypt --data "Your secret message here" --public-key public_key.pem
```
4. The tool will display the encrypted data.

# Decryption:

To decrypt data, follow these steps:
1. Make sure you have the private key file (private_key.pem) generated in the initial step.
2. Open a terminal and navigate to the project directory.
3. Use the CLI tool as follows to decrypt data:
   
```bash
python main.py decrypt --data "Encrypted data here" --private-key private_key.pem
```
4. The tool will display the decrypted data.

## Example

Encrypting and Decrypting Example:

Encrypt data:

```bash
python main.py encrypt --data "Hello, this is a test!" --public-key public_key.pem
```
Output:

```Encrypted Data: ...```

Decrypt data:

```bash
python main.py decrypt --data "Encrypted data here" --private-key private_key.pem
```
Output:

```Decrypted Data: Hello, this is a test!```

## Troubleshooting

1. If you encounter any errors related to missing libraries, make sure you have the pycryptodome library installed. You can install it using the following command:

```bash
pip install pycryptodome
```
2. Double-check that you're providing the correct paths to the public and private key files.
3. If you encounter any issues, feel free to create an issue in this repository.

## Security Considerations

1. Keep your private key (private_key.pem) safe and never share it with others.
2. Encryption is a powerful tool, but ensure you understand its limitations and best practices for secure communication.
   
# License
This project is licensed under the GNU License.
