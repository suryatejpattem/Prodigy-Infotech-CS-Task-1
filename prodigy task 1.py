def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_start + shift) % 26 + shift_start)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_start - shift) % 26 + shift_start)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
choice = input("Type 'e' to encrypt or 'd' to decrypt: ")

if choice == 'E':
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
elif choice == 'D':
    decrypted_message = decrypt(message, shift)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice! Please choose 'E' or 'D'.")
