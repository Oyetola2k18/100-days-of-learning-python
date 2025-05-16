

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(Words,shifts,direction):
    Final_Message = ""
    if direction == "encode":
        for x in range(0,len(Words)):
            position = int(alphabet.index(Words[x]))
            new_position = position + shifts
            if new_position >= alphabet.index('z'):
                Final_Message+= alphabet[new_position%26]
            else:
                Final_Message+=alphabet[new_position]
        print(f"The encrypted message is: {Final_Message}")
    elif direction == "decode":
        for x in range(0,len(Words)):
            position = int(alphabet.index(Words[x]))
            new_position = position - shifts

            Final_Message+=alphabet[new_position]
        print(f"The decrypted message is: {Final_Message}")
    
import art
print(art.logo)

end_of_game  = False
while end_of_game == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction=direction,Words=text,shifts=shift)
    run = input("Type 'yes'if you wanna go again , otherwise type 'NO' ")).lower()
    if run == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser(direction=direction,Words=text,shifts=shift)
    elif run == "no":
        print("Alright bye")
        end_of_game = True