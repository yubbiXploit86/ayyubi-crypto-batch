import os
import sys
import base64
import hashlib
import crypto_core

# PASSCODE yang kamu mau
PASSPHRASE = "212121"

# Bentuk Fernet key valid dari passphrase (tanpa ubah crypto_core)
digest = hashlib.sha256(PASSPHRASE.encode()).digest()
fernet_key = base64.urlsafe_b64encode(digest)

# Set key ke crypto_core
crypto_core.encryption_key = fernet_key

if len(sys.argv) != 2:
    print("Usage:")
    print("  python main.py encrypt")
    print("  python main.py decrypt")
    sys.exit(1)

mode = sys.argv[1]

for root, dirs, files in os.walk("."):
    for file in files:
        if file in ["main.py", "crypto_core.py", "README.md"]:
            continue
        path = os.path.join(root, file)
        try:
            if mode == "encrypt":
                crypto_core.encrypt_file(path)
                print("[ENCRYPTED]", path)
            elif mode == "decrypt":
                crypto_core.decrypt_file(path)
                print("[DECRYPTED]", path)
        except:
            print("[SKIPPED]", path)
