from tkinter import *
import pyperclip
import random
import string

# Function to generate password
def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +
                                             string.punctuation)
    pass_str.set(password)

# Function to copy password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())

# Create tkinter window
root = Tk()
root.title('Password generator')
root.geometry('400x400')

# Set background color to pink
root.configure(bg='pink')

# Program name label
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold')
heading.pack()

# Label for password length
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

# Entry for password length
pass_len = IntVar()
#controls the min as well as max length of the password
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=15)
length.pack()

# StringVar to store generated password
pass_str = StringVar()

# Button to generate password
generate_button = Button(root, text="GENERATE PASSWORD", command=Generator, bg="blue", fg="white")
generate_button.pack(pady=5)

# Entry to display generated password
Entry(root, textvariable=pass_str).pack()

# Button to copy password to clipboard
copy_button = Button(root, text='COPY TO CLIPBOARD', command=Copy_password, bg="blue", fg="white")
copy_button.pack(pady=5)

root.mainloop()

