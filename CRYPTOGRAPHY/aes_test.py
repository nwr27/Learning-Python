from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
print(f"Key: {key}")

iv = os.urandom(16)
print(f"IV: {iv}")

plaintext = b"This is a secret message"
print(f"Plaintext: {plaintext}")

padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
chipertext = encryptor.update(padded_plaintext) + encryptor.finalize()
print(f"Chipertext: {chipertext}")

decryptor = cipher.decryptor()
decrypted_padded_plaintext = decryptor.update(chipertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()
print(f"Decrypted plaintext: {decrypted_plaintext}")
