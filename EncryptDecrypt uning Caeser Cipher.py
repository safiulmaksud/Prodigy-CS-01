def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                ascii_offset = ord('a')
            else:
                ascii_offset = ord('A')
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift (positive for encryption, negative for decryption): "))
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()

    if mode == 'encrypt':
        encrypted_text = caesar_cipher(text, shift, mode)
        print("Encrypted text:", encrypted_text)
    elif mode == 'decrypt':
        decrypted_text = caesar_cipher(text, shift, mode)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
