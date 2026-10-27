# TASK 1: RSA Key Generation
import secrets
import json

def is_prime(n, rounds=40):
    """Miller-Rabin primality test."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        c = secrets.randbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(c):
            return c

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(e, phi):
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % phi

def generate_keypair(bits=1024):
    e = 65537
    while True:
        p = generate_prime(bits)
        q = generate_prime(bits)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if egcd(e, phi)[0] == 1:
            break
    n = p * q
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

if __name__ == "__main__":
    print("=== TASK 1: RSA Key Generation ===")
    public_key, private_key = generate_keypair(1024)
    e, n = public_key
    d, _ = private_key

    print("Public exponent e :", e)
    print("Modulus n length  :", n.bit_length(), "bits")
    print("Key pair generated successfully.")
    with open("keys.json", "w") as f:
        json.dump({"e": e, "d": d, "n": n}, f)
    print("Keys saved to keys.json")