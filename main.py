import os
import sys
import base64
import hashlib
import crypto_core

# ===============================
# ASCII BANNER
# ===============================
BANNER = r"""
   ___    __   __  __  ____  _    _ _ _ _ _ 
  / _ \   \ \ / / |  \/  | |  | | | | | | |
 | | | |   \ V /  | |\/| | |  | | | | | | |
 | |_| |    | |   | |  | | |__| | | | | | |
  \___/     |_|   |_|  |_|\____/|_|_|_|_|_|
                                            
       by AYYUBI - Crypto Batch
"""

# ===============================
# PERMANENT KEY SETUP
# ===============================
PASSPHRASE = "212121"
digest = hashlib.sha256(PASSPHRASE.encode()).digest()
fernet_key = base64.urlsafe_b64encode(digest)
crypto_core.encryption_key = fernet_key

# ===============================
# HELP / USAGE
# ===============================
if len(sys.argv) != 2 or sys.argv[1] in ["-h", "--help"]:
    print(BANNER)
    print("Usage:")
    print("  python main.py encrypt    # Encrypt all files")
    print("  python main.py decrypt    # Decrypt all files")
    sys.exit(0)

mode = sys.argv[1]
extension = ".ayyubii"  # Custom extension

print(BANNER)
print(f"[INFO] Mode: {mode.upper()}")

# ===============================
# LOOP ENCRYPT/DECRYPT
# ===============================
for root, dirs, files in os.walk("."):
    for file in files:
        if file in ["main.py", "crypto_core.py", "README.md"]:
            continue
        path = os.path.join(root, file)
        try:
            if mode == "encrypt":
                crypto_core.encrypt_file(path)
                os.rename(path, path + extension)
                print("[ENCRYPTED]", path)
            elif mode == "decrypt":
                if file.endswith(extension):
                    crypto_core.decrypt_file(path)
                    original = os.path.splitext(path)[0]
                    os.rename(path, original)
                    print("[DECRYPTED]", path)
        except Exception as e:
            print("[SKIPPED]", path, "| Reason:", str(e))
