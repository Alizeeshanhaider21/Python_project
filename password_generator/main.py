from tkinter import *
from tkinter import messagebox
import random,json,pyperclip as pc 

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

password_list=[]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    password_char=[random.choice(letters) for char in  range(2,8)]
    password_num=[random.choice(numbers) for char in  range(2,5)]
    password_symbol=[random.choice(symbols) for char in  range(1,4)]
    password_list=password_char+password_num+password_symbol
    random.shuffle(password_list)
    password="".join(password_list)
    password_input.insert(0,password)
    pc.copy(password)
    print(password)
# -------------------  --------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name=website_input.get()
    email=email_input.get()
    password=password_input.get()
    data_dict={
        website_name:{
            'email':email,
            'password':password
        }
    }
    if len(website_name)>0 and len(email)>0 and len(password)>0:
        is_ok=messagebox.askokcancel(title='Conformation',message=f'Please Review the Details Below\n Website: {website_name}\n Email/Username: {email}\n Password: {password}\n Are you Sure to Save details ? ')
        if  is_ok:
            with open('Password_records.json' , 'r') as get_file:
                past_content=json.load(get_file)
                past_content.update(data_dict)
            with open('Password_records.json' , 'w' ) as pass_file:
                json.dump(past_content,pass_file,indent=4)
                website_input.delete(0,END)
                password_input.delete(0,END)
    else:
        messagebox.showinfo(message='Please make sure provide all details..')
    
def search():
    website_name=website_input.get()
    with open('Password_records.json' , 'r') as get_file:
            past_content=json.load(get_file)
            if website_name in past_content:
                messagebox.showinfo(message=f'Email: {past_content[website_name]['email']}\nPassword: {past_content[website_name]['password']}')
            else:
               
               messagebox.showinfo(message='No Record Found')
          
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Generator')
window.config(padx=50,pady=50)


canvas=Canvas()
canvas.config(width=200,height=200)
img_logo=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img_logo)
canvas.grid(column=1,row=0)

label_website=Label(text='Website :')
label_website.grid(column=0,row=1,pady=5)
label_email=Label(text='Email/Username :')
label_email.grid(column=0,row=2,pady=5)
label_password=Label(text='Password :')
label_password.grid(column=0,row=3,pady=5)


website_input=Entry(width=33)
website_input.grid(column=1,row=1,padx=10)
website_input.focus()
email_input=Entry(width=53)
email_input.grid(column=1,row=2,columnspan=2,padx=10)
email_input.insert(0,'example@abc.com')
password_input=Entry(width=33)
# password_input.insert(0,'Hello')
password_input.grid(row=3,column=1)


search_btn=Button(text='Search',width=15,command=search)
search_btn.grid(column=2,row=1,)
pass_gen_btn=Button(text='Generate Password',command=generate_pass)
pass_gen_btn.grid(column=2,row=3)

add_pass_btn=Button(text='Add',width=45,command=save_password)
add_pass_btn.grid(column=1,row=4,columnspan=2)

window.mainloop()