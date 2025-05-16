

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(Words,shifts):
    encrypted=""
    for x in range(0,len(Words)):
        position = int(alphabet.index(Words[x]))
        new_position = position + shifts
        if new_position >= alphabet.index('z'):
            encrypted+= alphabet[new_position%26]
        else:
            encrypted+=alphabet[new_position]
    print(f"The encrypted password is:{encrypted}")

def decrypt(Words,shifts):
    decrypted = ""
    for x in range(0,len(Words)):
        position = int(alphabet.index(Words[x]))
        new_position = position - shifts

        decrypted+=alphabet[new_position]
    print(f"THe decryted Text is: {decrypted}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(Words=text,shifts=shift)
elif direction == "decode":
    decrypt(Words=text,shifts=shift)