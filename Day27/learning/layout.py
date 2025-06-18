#TKinter has A lot of layout managers(that are inchargeof how widgets are placed), but we will be working with 3
#we have
#GRID- working with ROWS and COLUMNS(start from Row -0, COlumn - 0)
#PACK- packs each of the widget next together and has options like, right, left , center,top,bottom
#PLACE-X and Y coord adjustment

#note wd cant use GRID Aand PACK in the same place
import tkinter

window = tkinter.Tk()
window.title("MY first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=250,pady=150)

#we can change padding
#with padx and pady(space around your program) in the config function

#label
my_label = tkinter.Label(text="Free Candy(Label)", font= ("Arial", 24))
my_label.config(text="New text 2")
my_label.grid(column=0,row=0)
# my_label.pack()
# my_label["text"]= "New Text"
# #or



#button
button = tkinter.Button(text="CLick Me",font=("Arial", 24, "bold"))
# button.pack()
# button.place(x=100,y=200)
button.grid(row=1,column=1)

#new button
button2 = tkinter.Button(text="2nd BUtton", font=("Arial", 24, "bold"))
button2.grid(row=0,column=2)


#ENtry(input)
input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2,column=3)
# input.pack()




window.mainloop()