from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title('French Word Guessing')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

try:
    data=pd.read_csv('data/data_to_learn.csv')
except FileNotFoundError:
    origional_data=pd.read_csv('data/french_words.csv')
    listed_data=origional_data.to_dict(orient='records')
else:
    listed_data=data.to_dict(orient='records')


current_data={}
def move_card():
    global current_data,window_timer
    window.after_cancel(window_timer)
    current_data=random.choice(listed_data)
    canvas.itemconfig(canvas_face,image=card_front)
    canvas.itemconfig(card_title,text='French',fill='black')
    canvas.itemconfig(card_word,text=current_data['French'],fill='black')
    window_timer=window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(canvas_face,image=card_back)
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=current_data['English'],fill='white')

def known_word():
    listed_data.remove(current_data)
    to_learn=pd.DataFrame(listed_data)
    to_learn.to_csv('data/data_to_learn.csv',index=None)
    move_card()

canvas=Canvas()
canvas.config(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file='images/card_front.png')
card_back=PhotoImage(file='images/card_back.png')
canvas_face=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,153,text='Title here',font=('Arial',25,'italic'))
card_word=canvas.create_text(400,253,text='Word Here',font=('Arial',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)

right_img=PhotoImage(file='images/right.png')
btn_known=Button(image=right_img,command=known_word)
btn_known.grid(column=1,row=1)

wrong_img=PhotoImage(file='images/wrong.png')
btn_unknown=Button(image=wrong_img,command=move_card)
btn_unknown.grid(column=0,row=1)

window_timer=window.after(3000,flip_card)
move_card()


window.mainloop()