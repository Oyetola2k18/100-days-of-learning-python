#mile to kilometers converter
import tkinter

FONT = ("Arial", 10, "bold")
#window
windows = tkinter.Tk()
windows.title("MilE to Km converter")
windows.minsize(width=250,height=100)
windows.config(padx=10,pady=10)
#user_input
input = tkinter.Entry(width=10)
input.grid(column=1,row=0)

#miles label
mile_label = tkinter.Label()
mile_label.config(text="MIles", font=FONT)
mile_label.grid(row=0,column=2)

#is equal to  label
is_equal_to = tkinter.Label()
is_equal_to.config(text="is equal to", font=FONT)
is_equal_to.grid(row=1,column=0)

#Score  label
Score = tkinter.Label()
Score.config(text=0, font=FONT)
Score.grid(row=1,column=1)

#Km  label
Km = tkinter.Label()
Km.config(text="Km", font=FONT)
Km.grid(row=1,column=2)

#function to perform conversion
def calculate():
    miles = float(input.get())
    the_km = miles * 1.60934
    Score.config(text=f"{round(the_km)}")

#submit button
calculate_button = tkinter.Button(width=10, command=calculate, text="Calculate")
calculate_button.grid(row=2,column=1)
windows.mainloop()