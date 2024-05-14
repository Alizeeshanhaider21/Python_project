from tkinter import *
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
repeater=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_counter():
    global repeater
    window.after_cancel(timer)
    canvas.itemconfig(counter_text,text='00:00')
    timer_label.config(text='Timer')
    mark_label.config(text="")
    repeater=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global repeater,timer
    repeater+=1
    long_break=LONG_BREAK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    work_secs=WORK_MIN*60
    if repeater%8==0:
        countdown(long_break)
        timer_label.config(text='Long Break',font=('Arial',35,'bold'),fg=RED,bg=YELLOW)
    elif repeater%2==0:
        countdown(short_break)
        timer_label.config(text='Break',font=('Arial',35,'bold'),fg=RED,bg=YELLOW)
    else:
     countdown(work_secs)
    
    
    # countdown(5*2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    if count>=0:
        count_mints=math.floor(count/60)
        count_secs=count%60
        if count_secs<10:
            count_secs=f'0{count_secs}'
        canvas.itemconfig(counter_text,text=f'{count_mints}:{count_secs}')
        timer=window.after(1000,countdown,count-1)
    
    else:
        start_countdown()
        global repeater
        marks=''
        work_sessions=math.floor(repeater%2)
        for _ in range(work_sessions):
            marks+='✔'
        mark_label.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

timer_label=Label()
timer_label.config(text='Timer',font=('Arial',35,'bold'),fg=GREEN,bg=YELLOW,highlightthickness=0)
timer_label.grid(column=1,row=0)

mark_label=Label()
mark_label.config(font=('Arial',16,'bold'),fg=GREEN,bg=YELLOW,highlightthickness=0)
mark_label.grid(column=1,row=2)

canvas=Canvas()
canvas.config(width=200,height=224,bg=YELLOW,highlightthickness=0)
potato_image=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=potato_image)
counter_text=canvas.create_text(100,130,text='00:00',font=('Arial',25,'bold'))
canvas.grid(column=1,row=1)

start_btn=Button()
start_btn.config(text='Start',command=start_countdown)
start_btn.grid(column=0,row=2)

reset_btn=Button()
reset_btn.config(text='Reset',command=reset_counter)
reset_btn.grid(column=2,row=2)
# countdown(5)

window.mainloop()


# mark='✔'