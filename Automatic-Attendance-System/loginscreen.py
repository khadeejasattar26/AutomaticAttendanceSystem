from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import re

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("600x400")

        # Background image
        self.background_image = Image.open("WhatsApp Image 2024-05-08 at 20.37.51_c8ab751f.jpg")
        self.background_image = self.background_image.resize((600, 400))
        self.img = ImageTk.PhotoImage(self.background_image)
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        self.title_label = Label(master, text="Automatic Attendance System", font=("times new roman", 20, "bold"), fg="black")
        self.title_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        # Email label and entry
        self.email_label = Label(master, text="Email:", font=("Times New Roman", 14), bg="light blue", fg="black")
        self.email_label.place(relx=0.2, rely=0.4, anchor=CENTER)
        self.email_entry = Entry(master, width=25, font=("Times New Roman", 12), bg="white", fg="black", highlightthickness=0)
        self.email_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Password label and entry
        self.password_label = Label(master, text="Password:", font=("Times New Roman", 14), bg="light blue", fg="black")
        self.password_label.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.password_entry = Entry(master, show="*", width=25, font=("Times New Roman", 12), bg="white", fg="black", highlightthickness=0)
        self.password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Show password checkbox
        self.show_password_var = IntVar()
        self.show_password_checkbox = Checkbutton(master, text="Show Password", variable=self.show_password_var, command=self.toggle_password)
        self.show_password_checkbox.place(relx=0.5, rely=0.6, anchor=CENTER)

        # Login button
        self.login_button = Button(master, text="Login", command=self.login, font=("Times New Roman", 14), bg="light blue", fg="black")
        self.login_button.place(relx=0.4, rely=0.7, anchor=CENTER)

        # Signup button
        self.signup_button = Button(master, text="Signup", command=self.open_signup, font=("Times New Roman", 14), bg="light blue", fg="black")
        self.signup_button.place(relx=0.6, rely=0.7, anchor=CENTER)

    def login(self):
        # Get the entered email and password
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Database connection details
        host = "your_host"
        user = "your_username"
        password_db = "your_password"
        database = "your_database"

        # Establish database connection and execute query
        conn = mysql.connector.connect(host=host, user=user, password=password_db, database=database)
        cursor = conn.cursor()
        query = "SELECT * FROM register WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        # Fetch the row
        row = cursor.fetchone()

        if row:
            # Successful login
            messagebox.showinfo("Login", "Login Successful!")
            # Perform actions for successful login, e.g., opening main window
            self.open_main_window()
        else:
            # Unsuccessful login
            messagebox.showerror("Error", "Invalid email or password")

        # Close the database connection
        cursor.close()
        conn.close()

    def open_signup(self):
        # Hide the login window
        self.master.withdraw()
    
        # Open the signup window
        import signupscreen
        signup_screen = Toplevel(self.master)
        signup_screen.title("Signup")
        signup_screen.geometry("400x300")
        signup_window = signupscreen.SignupScreen(signup_screen, self.open_login)

    def open_login(self):
        # Placeholder for opening the login window
        pass

    def open_main_window(self):
        # Placeholder for opening the main window upon successful login
        pass

    def toggle_password(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

def main():
    win = Tk()
    app = LoginScreen(win)
    win.mainloop()

if __name__ == "__main__":
    main()
