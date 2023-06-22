import tkinter as tk
from tkinter import messagebox
import random
import math

def generate_duck_positions(n, radius):
    positions = []
    for _ in range(n):
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, radius)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        positions.append((x, y))
    return positions

def calculate_probability(n, sector_degree, num_simulations):
    count_same_half = 0  # Number of cases where all ducks are in the same half
    success_count = 0  # Number of successes
    trial_count = 0  # Number of trials

    for _ in range(num_simulations):
        positions = generate_duck_positions(n, radius)
        trial_count += 1

        # Calculate the angle of each duck from the x-axis
        angles = [math.atan2(y, x) for x, y in positions]

        # Check if all ducks are in the same half-sector
        if all(abs(angle - angles[0]) <= math.radians(sector_degree) for angle in angles):
            count_same_half += 1
            success_count += 1

        # Clear previous ducks
        canvas.delete("duck")

        # Draw new ducks
        for x, y in positions:
            canvas_x = center_x + x
            canvas_y = center_y - y
            canvas.create_oval(canvas_x - 3, canvas_y - 3, canvas_x + 3, canvas_y + 3, fill="blue", tags="duck")

        # Update the canvas
        canvas.update()

        # Update success, trial, and relative frequency labels
        success_label.config(text=f"Successes: {success_count}")
        trial_label.config(text=f"Trials: {trial_count}")
        frequency = success_count / trial_count if trial_count > 0 else 0
        frequency_label.config(text=f"Relative Frequency: {frequency:.4f}")

    probability = count_same_half / num_simulations
    return probability

def calculate_button_click():
    try:
        n = int(ducks_entry.get())
        sector_degree = int(sector_entry.get())
        num_simulations = int(simulations_entry.get())

        if n >= 2 and sector_degree > 0 and num_simulations > 0:
            probability = calculate_probability(n, sector_degree, num_simulations)
            messagebox.showinfo("Result", f"The probability is: {probability:.4f}")
        else:
            messagebox.showerror("Error", "Please enter valid values.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

# Create GUI window
window = tk.Tk()
window.title("Duck Probability Calculator")

# Create GUI elements
ducks_label = tk.Label(window, text="Enter the number of ducks:")
ducks_label.pack()

ducks_entry = tk.Entry(window)
ducks_entry.pack()

sector_label = tk.Label(window, text="Enter the degree of the sector (M-degree sector):")
sector_label.pack()

sector_entry = tk.Entry(window)
sector_entry.pack()

simulations_label = tk.Label(window, text="Enter the number of simulated runs:")
simulations_label.pack()

simulations_entry = tk.Entry(window)
simulations_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_button_click)
calculate_button.pack()

# Draw circle and ducks using canvas
canvas_width = 400
canvas_height = 400
radius = min(canvas_width, canvas_height) / 2 - 10
center_x = canvas_width / 2
center_y = canvas_height / 2

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

circle = canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black")

# Labels for success, trial, and relative frequency
success_label = tk.Label(window, text="Successes: 0")
success_label.pack()

trial_label = tk.Label(window, text="Trials: 0")
trial_label.pack()

frequency_label = tk.Label(window, text="Relative Frequency: 0.0000")
frequency_label.pack()

# Run the GUI event loop
window.mainloop()
