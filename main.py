# caesar_cipher.py
# Caesar Cipher Encryption and Decryption Program

def caesar_shift_char(ch: str, shift: int) -> str:
    """Shift a single character preserving case."""
    if ch.isalpha():  # only shift alphabets
        base = ord('A') if ch.isupper() else ord('a')
        new_ord = (ord(ch) - base + shift) % 26 + base
        return chr(new_ord)
    else:
        return ch  # leave spaces, numbers, punctuation unchanged

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    return ''.join(caesar_shift_char(ch, shift) for ch in text)

def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar cipher."""
    return ''.join(caesar_shift_char(ch, -shift) for ch in text)

def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    mode = input("Type 'e' for encryption or 'd' for decryption: ").lower()

    if mode == 'e':
        result = caesar_encrypt(message, shift)
        print("\nEncrypted message:", result)
    elif mode == 'd':
        result = caesar_decrypt(message, shift)
        print("\nDecrypted message:", result)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()