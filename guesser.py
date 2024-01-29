import tkinter as tk
from tkinter import ttk, messagebox
from itertools import permutations

def generate_passwords():
    name = name_entry.get()
    dob = dob_entry.get()
    pet_name = pet_name_entry.get()
    favorite_color = favorite_color_entry.get()
    lucky_number = lucky_number_entry.get()
    hometown = hometown_entry.get()

    if not name or not dob or not pet_name or not favorite_color or not lucky_number or not hometown:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Get the minimum length of the password
    try:
        min_length = int(min_length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid minimum length.")
        return

    # Get the number of passwords to generate
    try:
        num_passwords = int(num_passwords_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of passwords.")
        return

    data = [name, dob, pet_name, favorite_color, lucky_number, hometown]

    # Generate permutations of data
    all_passwords = set()
    for r in range(min_length, len(data) + 1):
        for combination in permutations(data, r):
            password = ''.join(combination)
            all_passwords.add(password)
            # Add variations like uppercase/lowercase combinations
            all_passwords.add(password.lower())
            all_passwords.add(password.upper())

    # Convert to list and get the specified number of passwords
    all_passwords = list(all_passwords)[:num_passwords]

    # Save the passwords to a file
    with open("generated_passwords.txt", "w") as file:
        for password in all_passwords:
            file.write(password + "\n")

    messagebox.showinfo("Success", f"Generated {len(all_passwords)} passwords saved to 'generated_passwords.txt'.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Set the theme for ttk widgets
style = ttk.Style(root)
style.theme_use("clam")  # You can experiment with other available themes

# Styling
root.geometry("400x350")
root.resizable(False, False)

# Create a frame for styling
frame = ttk.Frame(root, padding=(10, 10, 10, 10))
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and Entry widgets
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Date of Birth:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
dob_entry = ttk.Entry(frame)
dob_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Pet Name:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
pet_name_entry = ttk.Entry(frame)
pet_name_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame, text="Favorite Color:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
favorite_color_entry = ttk.Entry(frame)
favorite_color_entry.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(frame, text="Lucky Number:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
lucky_number_entry = ttk.Entry(frame)
lucky_number_entry.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(frame, text="Hometown:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
hometown_entry = ttk.Entry(frame)
hometown_entry.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(frame, text="Minimum Password Length:").grid(row=6, column=0, sticky="e", padx=10, pady=5)
min_length_entry = ttk.Entry(frame)
min_length_entry.grid(row=6, column=1, padx=10, pady=5)

ttk.Label(frame, text="Number of Passwords:").grid(row=7, column=0, sticky="e", padx=10, pady=5)
num_passwords_entry = ttk.Entry(frame)
num_passwords_entry.grid(row=7, column=1, padx=10, pady=5)

# Button to generate passwords
generate_button = ttk.Button(frame, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()

