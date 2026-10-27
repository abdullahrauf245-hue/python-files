# TASK 3: RSA Decryption (uses PRIVATE key from Task 1)
import json

def decrypt(c, private_key):
    d, n = private_key
    m = pow(c, d, n)                                     # m = C^d mod n
    return m.to_bytes((m.bit_length() + 7) // 8, "big").decode("utf-8")

if __name__ == "__main__":
    print("=== TASK 3: RSA Decryption ===")
    with open("keys.json") as f:
        k = json.load(f)
    private_key = (k["d"], k["n"])

    with open("cipher.json") as f:
        data = json.load(f)
    c = int.from_bytes(bytes.fromhex(data["cipher_hex"]), "big")

    decrypted = decrypt(c, private_key)
    print("Decrypted message :", decrypted)
    print("Original message  :", data["original"])
    print("Match?            :", decrypted == data["original"])