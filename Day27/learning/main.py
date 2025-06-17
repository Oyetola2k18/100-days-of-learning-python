import tkinter

window = tkinter.Tk()
window.title("MY first GUI Program")
window.minsize(width=500,height=300)



#label
#the line below will not display unless the you call the pack function in line 12
my_label = tkinter.Label(text="I am a label", font= ("Arial", 24))
my_label.pack(side="bottom")
window.mainloop()



#Hmm ,learnt about functions with default values e.g

# def add(a = 1, b = 2):
#     print(a + b)

# # add() #i can call the function like this and it will work perfectly fine
# # add(2,3) #and i can also do this and it will overwrite the default values in the functions
# # #thank you

# add()
# add(2,3)