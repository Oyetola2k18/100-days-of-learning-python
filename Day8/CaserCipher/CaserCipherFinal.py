
#one thing about the modulus function, if your number you are divviding by is less than the denominator, it will return the numerator

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(Words,shifts,direction):
    Final_Message = ""
    if direction == "encode":
        for x in range(0,len(Words)):
            if(Words[x] not in alphabet):
                Final_Message+=Words[x]
                continue
            position = int(alphabet.index(Words[x]))
            new_position = position + shifts
            if new_position >= alphabet.index('z'):
                Final_Message+= alphabet[new_position%26]
            else:
                Final_Message+=alphabet[new_position]
        print(f"The encrypted message is: {Final_Message}")
    elif direction == "decode":
        for x in range(0,len(Words)):
            if(Words[x] not in alphabet):
                Final_Message+=Words[x]
                continue
            position = int(alphabet.index(Words[x]))
            new_position = position - shifts

            Final_Message+=alphabet[new_position%26]
        print(f"The decrypted message is: {Final_Message}")
    
import art
print(art.logo)

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction=direction,Words=text,shifts=shift)
    
    run = input("Type 'yes'if you wanna go again , otherwise type 'NO' ").lower()
    if run == "no":
        print("Aiit bye")
        should_continue=False