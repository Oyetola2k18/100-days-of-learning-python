import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas =tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
#add image to canvas
#the create image function takes in 3 values, the x and y coord to know where the image would be placed
#and the image we want to use, we cant just pass in the image  path in there , we need to make use of a class
#called photoimage that we will use to read that image from its path(if that makes sense)
tomato_image = tkinter.PhotoImage(file="Day28/pomodoro-project/tomato.png")
canvas.create_image(100,112,image=tomato_image)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,28,"bold"))
canvas.pack()













window.mainloop()