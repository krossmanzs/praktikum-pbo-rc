import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

class System:
    def __init__(self, program_name):
        self.__program_name = program_name
        self.__user_data = dict()
        self.__total_data = -1
        self.__load_data()
    
    def get_program_name(self):
        return self.__program_name
    
    def __load_data(self):
        try:
            with open('file.csv', 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    self.__user_data[row[0]] = row[1]
                    self.__total_data += 1

        except (FileNotFoundError):
            with open('file.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['username', 'password'])
                totalData = 0
                self.__total_data = 0

    def login(self, username, password):
        # Return Code
        # -1 = Error, wrong username or password
        # 1  = Success
        # 0  = Empty username or password
        if username == "" or password == "":
            return 0
        elif username in self.__user_data and self.__user_data[username] == password:
            return 1
        else:
            return -1

    def register(self, username, password):
        # Return Code
        # -1 = Duplicate username
        # 1  = Success
        # 0  = Empty username or password
        if username == "" or password == "":
            return 0
        if username in self.__user_data:
            return -1
        else:
            self.__write_data(username,password)
            return 1

    def __write_data(self, username, password):
        with open('file.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow([username, password])
            self.__total_data += 1
        
        self.__user_data[username] = password

def on_login_selected(username_input, password_input):
    login_status = login_system.login(username_input, password_input)

    if login_status == 1: # success
        messagebox.showinfo("Login Successfull", f"Welcome, {username_input}!")
    elif login_status == -1: # wrong username or password
        messagebox.showerror("Login Error", "Wrong username or password")
    elif login_status == 0: #
        messagebox.showwarning("Empty Input", "Empty username or password")

def on_register_seleted(username_input, password_input, register_window):
    login_status = login_system.register(username_input, password_input)

    if login_status == 1: # success
        messagebox.showinfo("Register Successfull", f"You can login with the new username")
    elif login_status == -1: # wrong username or password
        messagebox.showerror("Register Error", "Username already exist!")
    elif login_status == 0: #
        messagebox.showwarning("Empty Input", "Empty username or password")
    
    register_window.destroy()

    

def on_register_menu_selected():
    register_window = tk.Toplevel(window)

    register_window.title("Register Menu")
    register_window.minsize(350,150)

    frame = ttk.Frame(register_window)
    frame.pack(pady=10)

    username_frame = ttk.Frame(register_window)
    username_frame.pack(side='top')

    username_label = ttk.Label(username_frame,text="Username")
    username_label.pack(side='left', padx=10)
    username_register_entry = ttk.Entry(username_frame, )
    username_register_entry.pack(side='left')

    password_frame = ttk.Frame(register_window)
    password_frame.pack(side='top', pady=10)

    password_label = ttk.Label(password_frame,text="Password")
    password_label.pack(side='left', padx=10)
    password_register_entry = ttk.Entry(password_frame, )
    password_register_entry.pack(side='left')

    register_button = ttk.Button(
        register_window, 
        text="Register",
        width=30, 
        command=lambda: on_register_seleted(
            username_input=username_register_entry.get(),
            password_input=password_register_entry.get(),
            register_window=register_window
        )
    )
    register_button.pack(pady=5)

    register_window.mainloop()

def on_spinbox_select():
    selected_value = ttk.Spinbox.get()
    messagebox.showinfo("Selected SpinBox Value", f"You selected: {selected_value}")

login_system = System("Login System by Leenoogs")

window = tk.Tk()

window.title(login_system.get_program_name())
window.minsize(350,150)

frame = ttk.Frame(window)
frame.pack(pady=10)

username_frame = ttk.Frame(window)
username_frame.pack(side='top')

username_label = ttk.Label(username_frame,text="Username")
username_label.pack(side='left', padx=10)
username_entry = ttk.Entry(username_frame, )
username_entry.pack(side='left')

password_frame = ttk.Frame(window)
password_frame.pack(side='top', pady=10)

password_label = ttk.Label(password_frame,text="Password")
password_label.pack(side='left', padx=10)
password_entry = ttk.Entry(password_frame, )
password_entry.pack(side='left')

login_button = ttk.Button(
    window, 
    text="Login", 
    width=30, 
    command= lambda: on_login_selected(
        username_input=username_entry.get(),
        password_input=password_entry.get()
    )
)
register_button = ttk.Button(
    window, 
    text="Register", 
    width=30, 
    command=on_register_menu_selected
)
login_button.pack(pady=10)
register_button.pack(pady=5)

window.mainloop()