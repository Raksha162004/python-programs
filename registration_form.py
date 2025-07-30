import tkinter
def register():
    try:
        name = name_val.get()
        email = email_val.get()
        password = pass_val.get()
        gender = gender_val.get()
        if not name or not email or not password or not gender:
            raise ValueError("Empty field")
        with open("registrations.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}, Password: {password}, Gender: {gender}\n")
        message = f"Registered Successfully!"
    except:
        message = "Please fill in all the fields correctly."
    message_label = tkinter.Label(root, text=message, font=("Arial", 12), bg="light yellow")
    message_label.pack(pady=10)
root = tkinter.Tk()
root.geometry("600x600")
root.title("Registration Form")
root.configure(bg="light blue")
head = tkinter.Label(root, text="User Registration", font="Arial 20 bold", fg="Black", bg="white")
head.pack(pady=30)
fr = tkinter.LabelFrame(root, text="Registration Form", font=("Arial", 14, "bold"), bg="light blue", bd=3, relief="groove", padx=20, pady=20)
fr.pack(pady=20)
name_label = tkinter.Label(fr, text="Name:", font=("Arial", 15), bg="light blue")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_val = tkinter.Entry(fr)
name_val.grid(row=0, column=1, padx=10, pady=10)
email_label = tkinter.Label(fr, text="Email:", font=("Arial", 15), bg="light blue")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_val = tkinter.Entry(fr)
email_val.grid(row=1, column=1, padx=10, pady=10)
pass_label = tkinter.Label(fr, text="Password:", font=("Arial", 15), bg="light blue")
pass_label.grid(row=2, column=0, padx=10, pady=10)
pass_val = tkinter.Entry(fr, show="*")
pass_val.grid(row=2, column=1, padx=10, pady=10)
gender_label = tkinter.Label(fr, text="Gender:", font=("Arial", 15), bg="light blue")
gender_label.grid(row=3, column=0, padx=10, pady=10)
gender_val = tkinter.Entry(fr)
gender_val.grid(row=3, column=1, padx=10, pady=10)
btn = tkinter.Button(fr, text="REGISTER", font=("Arial", 16, "bold"), fg="green", command=register)
btn.grid(row=4, column=0, columnspan=2, pady=20)
root.mainloop()