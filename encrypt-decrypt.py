import os

base_dir = os.path.dirname(os.path.abspath(__file__))


def encrypt_char(ch, shift1, shift2):

    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        shift = shift1 * shift2
        return chr((pos + shift) % 26 + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        shift = shift1 + shift2
        return chr((pos + shift) % 26 + ord('A'))

    return ch

def decrypt_char(ch, shift1, shift2):
    
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        shift = shift1 * shift2
        return chr((pos - shift) % 26 + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        shift = shift1 + shift2
        return chr((pos - shift) % 26 + ord('A'))

    return ch


def encrypt_file(shift1, shift2):

    raw_file = os.path.join(base_dir, "raw_text.txt")
    enc_file = os.path.join(base_dir, "encrypted_text.txt")

    with open(raw_file, "r") as infile, open(enc_file, "w") as outfile:
        for line in infile:
            encrypted_line = ""
            for ch in line:
                encrypted_line += encrypt_char(ch, shift1, shift2)
            outfile.write(encrypted_line)


def decrypt_file(shift1, shift2):
    
    enc_file = os.path.join(base_dir, "encrypted_text.txt")
    dec_file = os.path.join(base_dir, "decrypted_text.txt")

    with open(enc_file, "r") as infile, open(dec_file, "w") as outfile:
        for line in infile:
            decrypted_line = ""
            for ch in line:
                decrypted_line += decrypt_char(ch, shift1, shift2)
            outfile.write(decrypted_line)

def verify_decryption():
    raw_file = os.path.join(base_dir, "raw_text.txt")
    dec_file = os.path.join(base_dir, "decrypted_text.txt")

    with open(raw_file, "r") as f1, open(dec_file, "r") as f2:
        if f1.read() == f2.read():
            print("Decryption successful: Files match.")
        else:
            print("Decryption failed: Files do not match.")

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypt_file(shift1, shift2)
decrypt_file(shift1, shift2)
verify_decryption()
