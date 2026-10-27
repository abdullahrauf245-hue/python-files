# TASK 2: RSA Encryption (uses PUBLIC key from Task 1)
import json
import base64

def encrypt(message, public_key):
    e, n = public_key
    m = int.from_bytes(message.encode("utf-8"), "big")   # string -> integer
    if m >= n:
        raise ValueError("Message too long for this key size")
    c = pow(m, e, n)                                     # C = m^e mod n
    c_bytes = c.to_bytes((n.bit_length() + 7) // 8, "big")
    return c_bytes.hex(), base64.b64encode(c_bytes).decode()

if __name__ == "__main__":
    print("=== TASK 2: RSA Encryption ===")
    with open("keys.json") as f:
        k = json.load(f)
    public_key = (k["e"], k["n"])

    message = input("Enter plaintext message: ")
    c_hex, c_b64 = encrypt(message, public_key)

    print("Ciphertext (hex)   :", c_hex)
    print("Ciphertext (base64):", c_b64)

    # Saved so Task 3 can decrypt it and verify against the original
    with open("cipher.json", "w") as f:
        json.dump({"cipher_hex": c_hex, "original": message}, f)
    print("Ciphertext saved to cipher.json")