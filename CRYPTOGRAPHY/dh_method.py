import random


# Fungsi untuk menghitung eksponensial modular: (base^exponent) % modulus
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)


# 1. Parameter publik (bisa diketahui semua pihak)
p = 23  # Bilangan prima
g = 5  # Generator
print(f"Parameter publik:\n  Bilangan prima (p): {p}\n  Generator (g): {g}\n")

# 2. Kunci privat (dipilih secara rahasia oleh masing-masing pihak)
a = random.randint(1, p - 1)  # Kunci privat Alice
b = random.randint(1, p - 1)  # Kunci privat Bob
print(f"Kunci privat:\n  Alice (a): {a}\n  Bob (b): {b}\n")

# 3. Kunci publik (dihitung dan dikirim ke pihak lain)
A = mod_exp(g, a, p)  # Kunci publik Alice
B = mod_exp(g, b, p)  # Kunci publik Bob
print(f"Kunci publik:\n  Alice (A): {A}\n  Bob (B): {B}\n")

# 4. Menghitung kunci rahasia bersama
# Alice menghitung (B^a) % p
secret_key_alice = mod_exp(B, a, p)
# Bob menghitung (A^b) % p
secret_key_bob = mod_exp(A, b, p)

print(f"Kunci rahasia bersama (harus sama):\n  Alice: {secret_key_alice}\n  Bob: {secret_key_bob}\n")

# Verifikasi
if secret_key_alice == secret_key_bob:
    print("Kunci rahasia berhasil dibangun bersama!")
else:
    print("Terjadi kesalahan dalam perhitungan kunci rahasia.")
