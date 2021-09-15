import string
import random
from tkinter import*


def generate():

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.punctuation
    s4 = string.digits

    password_data = []
    password_data.extend(list(s1))
    password_data.extend(list(s2))
    password_data.extend(list(s3))
    password_data.extend(list(s4))

    random.shuffle(password_data)
    a = len_pass.get()
    passgen = ("".join(password_data[0:a]))
    random.shuffle(password_data)

    passleb = Label(window, text = "Password:").grid(row = 7, column = 0)

    pass_disply = Entry(window, text = passgen)
    pass_disply.insert(0, passgen)
    pass_disply.grid(row = 8, column = 0)

    passle = Label(window, text = passgen).grid(row = 9, column = 0)


window = Tk()
window.title("Password Generation")
window .geometry("400x400")
window.resizable(width = False, height = False)

head_label = Label(window, text = "Welcome").grid(row = 1, column = 0)

content_label = Label(window, text = "This application is used to generate password").grid(row = 2, column = 0)

password_length = Label(window, text = "Enter Lenght of Password").grid(row = 3, column = 0)

len_pass = IntVar()
pass_len_user = Entry(window, textvariable = len_pass).grid(row = 4, column = 0)

generate_button = Button(window, text = "Generate", command = generate, width = 20).grid(row = 5, column = 1)

close_button = Button(window, text = "Close", command = quit, width = 20).grid(row = 6, column = 1)



window.mainloop()