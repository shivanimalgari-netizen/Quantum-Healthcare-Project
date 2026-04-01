from Crypto.Cipher import AES
import hashlib
import base64

# Generate key
def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

# Encrypt function
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(cipher.nonce + ciphertext).decode()
# Decrypt function


def decrypt_data(encrypted_data, key):
    import base64
    from Crypto.Cipher import AES

    data = base64.b64decode(encrypted_data.encode())

    nonce = data[:16]
    ciphertext = data[16:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt(ciphertext)

    return decrypted.decode()