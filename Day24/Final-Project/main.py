#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
friends = []
with open("Day24/Final-Project/Input/Names/invited_names.txt", mode="r") as n_file:
    name_list = n_file.readlines()
    for name in name_list:
        name=name.strip("\n")
        friends.append(name)

with open("Day24/Final-Project/Input/Letters/starting_letter.docx", mode="r") as sl_file:
    line = sl_file.readlines()
    for friend in friends:
        line[0]=line[0].replace("[name]",friend)
        with open(f"Day24/Final-Project/Output/ReadyToSend/letter_for_{friend}.docx", mode="w") as output:
            output.writelines(line)
        
        with open("Day24/Final-Project/Input/Letters/starting_letter.docx", mode="r") as sl_file:
            starting_file_line = sl_file.readline()
        line[0] = starting_file_line #resetting the first index
    