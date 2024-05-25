import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit}°F", fg="blue")
    except ValueError:
        result_label.config(text="Invalid input!", fg="red")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius}°C", fg="blue")
    except ValueError:
        result_label.config(text="Invalid input!", fg="red")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Styling
root.configure(bg="#f0f0f0")

# Celsius input
celsius_label = tk.Label(root, text="Celsius:", bg="#f0f0f0")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(root)
celsius_entry.grid(row=0, column=1)

celsius_button = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit, bg="#00aaff", fg="white")
celsius_button.grid(row=0, column=2)

# Fahrenheit input
fahrenheit_label = tk.Label(root, text="Fahrenheit:", bg="#f0f0f0")
fahrenheit_label.grid(row=1, column=0)

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=1)

fahrenheit_button = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius, bg="#00aaff", fg="white")
fahrenheit_button.grid(row=1, column=2)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.grid(row=2, columnspan=3)

# Run the main event loop
root.mainloop()
