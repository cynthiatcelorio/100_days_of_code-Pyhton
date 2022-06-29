alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

def encrypt(shift, msg):
    cipher_text = ""
    for i in msg:
        letter = alphabet[alphabet.index(i) + shift]
        cipher_text += letter
    print(f"The encoded text is: {cipher_text}")
    return cipher_text     


def decrypt(shift, msg):
    decode_text = ""
    for i in msg:
        letter = alphabet[alphabet.index(i) - shift]
        decode_text += letter
    print(f"The decoded text is: {decode_text}")
    return decode_text


action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
msg = input("Type your message: ")
shift = int(input("Type your shift number: "))

if action == "encode":
    encrypt(shift, msg)

elif action == "decode":
    decrypt(shift, msg)


