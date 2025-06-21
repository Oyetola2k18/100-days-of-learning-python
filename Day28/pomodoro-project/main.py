import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #work - 1,3,5,7 th rep
    #long break - 8th rep
    #short break - 2 , 4 , 6th rep
    if reps in [1,3,5,7] or reps == 0:
        countdown(work_sec)
    elif reps in [2,4]:
        countdown(short_break_sec)
    else:
        countdown(long_break_sec)
    reps+=1

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # print(count)
    #changing text that is on a canvas is different from the ways we have been doing it with other widgets
    #here we tap into the canvas we want to tweak and we use the .itemconfig function
    count_min = math.floor(count / 60)
    count_sec = count%60
    #or just check if its less than 10 lol
    if len(str(count_sec))==1 and len(str(count_min))==1:
        final_time = f"0{count_min}:0{count_sec}"
    elif len(str(count_min))==1:
        final_time = f"0{count_min}:{count_sec}"
    elif len(str(count_sec))==1:
        final_time = f"{count_min}:0{count_sec}"
    else:
        final_time = f"{count_min}:{count_sec}"

    canvas.itemconfig(timer_text,text=final_time)
    if count > 0:
        window.after(1, countdown, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(thing, a ,b , c):
#     print(thing)
#     print(a)
#     print(b)
#     print(c)

#the after function is used to do a particular task after some time (always in ms(milliseconds))
#it takes in the time in ms, the function and the parameters 
# window.after(1000,say_something,"moses",1,2,3)


canvas =tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
#add image to canvas
#the create image function takes in 3 values, the x and y coord to know where the image would be placed
#and the image we want to use, we cant just pass in the image  path in there , we need to make use of a class
#called photoimage that we will use to read that image from its path(if that makes sense)
tomato_image = tkinter.PhotoImage(file="Day28/pomodoro-project/tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,28,"bold"))

canvas.grid(row=1,column=1)

#we will not use bg to change the color of a label text, we use fg which stands for

#Heading TImer label
timer_heading = tkinter.Label(text="Timer")
timer_heading.config(font=(FONT_NAME,45,"bold"), fg=GREEN, bg=YELLOW)
timer_heading.grid(row=0,column=1)


#start button
start = tkinter.Button(text="Start",highlightthickness=0, command=start_timer)
start.grid(row=2,column=0)
# start.config(padx=0,pady=0)


#Reset button
reset = tkinter.Button(text="Reset", highlightthickness=0)
reset.grid(row=2,column=2)
# reset.config(padx=0,pady=0)

#checkbox to count how many pomodoro's you've done
check = tkinter.Label(text="✔️")
check.grid(row=3,column=1)
check.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME,18,"bold"))
window.mainloop()