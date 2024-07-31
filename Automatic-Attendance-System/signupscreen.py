from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

from loginscreen import LoginScreen


class SignupScreen:
    def __init__(self, master, open_login):
        self.master = master
        self.open_login = open_login
        self.master.geometry("800x600")
        self.master.title("Sign Up")
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_email = StringVar()

        # Title "Register Here"
        self.title_label = Label(self.master, text="Register Here", font=("Poppins", 24, "bold"), bg="white")
        self.title_label.pack(pady=20)

        # First Name
        self.first_name_label = Label(self.master, text="First Name:", bg="white")
        self.first_name_label.pack()

        self.first_name_entry = Entry(self.master, textvariable=self.var_fname, width=30, font=("Poppins", 12))
        self.first_name_entry.pack(pady=5)

        # Last Name
        self.last_name_label = Label(self.master, text="Last Name:", bg="white")
        self.last_name_label.pack()

        self.last_name_entry = Entry(self.master, textvariable=self.var_lname, width=30, font=("Poppins", 12))
        self.last_name_entry.pack(pady=5)

        # Phone Number
        self.phone_label = Label(self.master, text="Phone Number:", bg="white")
        self.phone_label.pack()

        self.phone_entry = Entry(self.master, textvariable=self.var_contact, width=30, font=("Poppins", 12))
        self.phone_entry.pack(pady=5)

        # Email
        self.email_label = Label(self.master, text="Email:", bg="white")
        self.email_label.pack()

        self.email_entry = Entry(self.master, textvariable=self.var_email, width=30, font=("Poppins", 12))
        self.email_entry.pack(pady=5)

        # Password
        self.password_label = Label(self.master, text="Password:", bg="white")
        self.password_label.pack()

        self.password_entry = Entry(self.master, textvariable=self.var_pass, show="*", width=30, font=("Poppins", 12))
        self.password_entry.pack(pady=5)

        # Show Password Checkbutton
        self.show_password_var = IntVar()
        self.show_password_checkbox = Checkbutton(self.master, text="Show Password", variable=self.show_password_var, command=self.toggle_password)
        self.show_password_checkbox.pack()

        # Confirm Password
        self.confirm_password_label = Label(self.master, text="Confirm Password:", bg="white")
        self.confirm_password_label.pack()

        self.confirm_password_entry = Entry(self.master, textvariable=self.var_confpass, show="*", width=30, font=("Poppins", 12))
        self.confirm_password_entry.pack(pady=5)

        # Register Button
        self.register_button_img = Image.open("register.jpeg")
        self.register_button_img = self.register_button_img.resize((100, 100))
        self.register_button_img = ImageTk.PhotoImage(self.register_button_img)

        self.register_button = Button(self.master, image=self.register_button_img, borderwidth=0, command=self.register_and_back)
        self.register_button.pack(pady=10)

        # Label to move back to login screen
        self.back_to_login_label = Label(self.master, text="Back to Login", font=("Poppins", 12), fg="blue", cursor="hand2", bg="white")
        self.back_to_login_label.pack(pady=10)
        self.back_to_login_label.bind("<Button-1>", self.back_to_login)

    def toggle_password(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
            self.confirm_password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            self.confirm_password_entry.config(show="*")

    def back_to_login(self, event=None):
        self.master.withdraw()  # Hide the signup window
        self.open_login()  # Show the login window

    def register_and_back(self):
        # Handle signup functionality here...
        if self.var_fname.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        else:
            conn = mysql.connector.connect(host="", user="", password="", database="")
            cursor = conn.cursor()

            # Check if email already exists
            query = "SELECT * FROM register WHERE email = %s"
            cursor.execute(query, (self.var_email.get(),))
            row = cursor.fetchone()

            if row:
                messagebox.showerror("Error", "User already exists. Please try another email.")
            else:
                # Insert new user into the database
                insert_query = "INSERT INTO register (first_name, last_name, phone_number, password, email) VALUES (%s, %s, %s, %s, %s)"
                insert_values = (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_pass.get(),
                    self.var_email.get()
                )
                cursor.execute(insert_query, insert_values)
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Registered Successfully!")
                self.back_to_login


def open_login_screen():
    login_root = Tk()
    login_root.title("Login")
    login_root.geometry("600x400")
    login_screen = LoginScreen(login_root)
    login_root.mainloop()
def main():
    root = Tk()
    signup_screen = SignupScreen(root, open_login_screen)
    root.mainloop()

if __name__ == "__main__":
    main()

