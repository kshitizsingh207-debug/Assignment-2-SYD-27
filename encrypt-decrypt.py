import os

base_dir = os.path.dirname(os.path.abspath(__file__))


def encrypt_char(ch, shift1, shift2):
    """
    Encrypt a single character using a reversible cipher.
    Lowercase letters and uppercase letters use different shifts.
    """
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        shift = shift1 * shift2
        return chr((pos + shift) % 26 + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        shift = shift1 + shift2
        return chr((pos + shift) % 26 + ord('A'))

    return ch
def encrypt_file(shift1, shift2):
    """
    Encrypt the contents of raw_text.txt and save to encrypted_text.txt
    """
    raw_file = os.path.join(base_dir, "raw_text.txt")
    enc_file = os.path.join(base_dir, "encrypted_text.txt")

    with open(raw_file, "r") as infile, open(enc_file, "w") as outfile:
        for line in infile:
            encrypted_line = ""
            for ch in line:
                encrypted_line += encrypt_char(ch, shift1, shift2)
            outfile.write(encrypted_line)

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))
encrypt_file(shift1, shift2)
