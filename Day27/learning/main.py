import tkinter

window = tkinter.Tk()
window.title("MY first GUI Program")
window.minsize(width=500,height=300)



#label
#the line below will not display unless the you call the pack function in line 12
my_label = tkinter.Label(text="Free Candy(Label)", font= ("Arial", 24))
my_label.pack()

# my_label["text"]= "New Text"
# #or
# my_label.config(text="New text 2")


#button
# def button_click():
#     # my_label["text"] = "I got clicked"
#     my_label.config(text="i got clicked")

# button = tkinter.Button(text="CLick Me", command=button_click)
#the text is like the name on the button
#the command is basically like if the button is clicked , what should happen, it takes in a function as its arguement

# button.pack()


#ENtry(input)

#creating an input field
input = tkinter.Entry()
input.config(width=10)
input.pack()
#we want to get the entry from that input, we use


def get_user_input():
    user_input = input.get()
    my_label.config(text=user_input)


button = tkinter.Button(text="Submit", command=get_user_input)
button.pack()












window.mainloop()
#Hmm ,learnt about functions with default values e.g

# def add(a = 1, b = 2):
#     print(a + b)

# # add() #i can call the function like this and it will work perfectly fine
# # add(2,3) #and i can also do this and it will overwrite the default values in the functions
# # #thank you

# add()
# add(2,3)
