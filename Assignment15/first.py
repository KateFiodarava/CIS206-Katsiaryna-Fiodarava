# This is a BMI Calculator using pounds and inches
# Made with tkinter for a GUI

import tkinter as tk
from tkinter import messagebox

# Function that runs when we click the button
def calculate_bmi():
    try:
        # Get name, weight and height from the text boxes
        name = name_entry.get()
        weight = float(weight_entry.get())  # user's weight in pounds
        height = float(height_entry.get())  # user's height in inches

        # BMI formula for inches and pounds
        bmi = (weight / (height * height)) * 703
        bmi = round(bmi, 2)  # round it to 2 decimal places

        # Show the result in the label
        result_label.config(text=name + ", your BMI is: " + str(bmi))
    except:
        # If the user types something that's not a number, show error
        messagebox.showerror("Oops!", "Please enter numbers only for weight and height.")

# Make the main window
window = tk.Tk()
window.title("BMI Calculator (Inches & Pounds)")

# Name input
tk.Label(window, text="Enter your name:").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

# Weight input
tk.Label(window, text="Weight (lbs):").grid(row=1, column=0)
weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1)

# Height input
tk.Label(window, text="Height (inches):").grid(row=2, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1)

# Button to do the BMI math
calc_btn = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calc_btn.grid(row=3, column=0, columnspan=2)

# Label to show result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Run the app
window.mainloop()
