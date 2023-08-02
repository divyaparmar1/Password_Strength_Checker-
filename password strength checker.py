import tkinter as tk

def check_password_strength():
    password = password_entry.get()
    strength = 0

    # Check for length and complexity
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1 
    if any(char.isdigit() for char in password):
        strength += 1  
    if any(not char.isalnum() for char in password):
        strength += 1
    
    # Evaluate password strength
    if strength == 0:
        result = "Very Weak"
        color = "red"
    elif strength == 1:
        result = "Weak"
        color = "orange"
    elif strength == 2:
        result = "Moderate"
        color = "yellow"
    elif strength == 3:
        result = "Moderate"
        color = "yellow"
    elif strength == 4:
        result = "Strong"
        color = "green"
    else:
        result = "Very Strong"
        color = "darkgreen"
    
    label_hash_result.config(text=f"Password strength: {result}", fg=color)

# Create the main application window
app = tk.Tk()
app.title("Password Strength Checker")

# Create widgets (labels, entries, buttons)
password_label = tk.Label(app, text="Enter Your Password :")
password_label.pack()

password_entry = tk.Entry(app, show="*")
password_entry.pack()

check_button = tk.Button(app, text="Check", command=check_password_strength)
check_button.pack()

label_hash_result = tk.Label(app, text="", fg="black")
label_hash_result.pack()

# Start the main event loop
app.mainloop()
