import hashlib
import rsa

def generate_keys():
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def sign_transaction(private_key, transaction):
    return rsa.sign(transaction.encode(), private_key, 'SHA-256')

def verify_signature(public_key, transaction, signature):
    try:
        rsa.verify(transaction.encode(), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
