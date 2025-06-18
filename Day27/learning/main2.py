#working with other widgets

import tkinter

window = tkinter.Tk()
window.title("TK")
window.minsize(width=500, height=500)

#entry
entry = tkinter.Entry(width=30)

entry.insert(tkinter.END, string="Some text to begin with")
entry.focus() 
print(entry.get())
entry.pack()

#text - textbox area

text = tkinter.Text(height=5,width=30)
text.focus()#the focus puts cursor in textbox
text.insert(tkinter.END, "FLEX FLEX STEP")
print(text.get("1.0", tkinter.END))
#Get current value from textbox at line 1(first line), character 0 to the END
text.pack()


#spin box
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0,to=10, width=20, command=spinbox_used)
#create a spin box that its range is 0 to 10, size 20, if we change the value of the spinbox, 
# that commamd is called and it prints its current value
spinbox.pack()


#scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100,command=scale_used)
scale.pack()


#checkbutton
def check_button_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=check_button_used)
checked_state.get()
checkbutton.pack()


#radio button
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", command=radio_used,value=2, variable=radio_state)

radiobutton1.pack()
radiobutton2.pack()


#list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruit = ["Apple","Pear", "Orange", "Banana"]
for item in fruit:
    listbox.insert(fruit.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()