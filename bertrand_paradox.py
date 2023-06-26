import tkinter as tk
import random
import math

class BertrandParadoxSimulator(tk.Tk):
    def __init__(self):

        #setting up the window for the GUI 
        tk.Tk.__init__(self)
        self.title("Bertrand's Paradox Simulator")
        self.canvas_width = 500
        self.canvas_height = 500
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()
        self.label_success = tk.Label(self, text="Successes: ")
        self.label_success.pack()
        self.label_trials = tk.Label(self, text="Trials: ")
        self.label_trials.pack()
        self.label_frequency = tk.Label(self, text="Relative Frequency: ")
        self.label_frequency.pack()
        self.strategy = tk.StringVar()
        self.strategy.set("Random Endpoints")
        self.simulations = tk.StringVar()
        self.simulations.set("100")
        self.create_widgets()

    def create_widgets(self):
        strategy_label = tk.Label(self, text="Strategy:")
        strategy_label.pack()
        strategy_options = tk.OptionMenu(self, self.strategy, "Random Endpoints", "Random Radius", "Random Midpoint", "My Strategy")
        strategy_options.pack()

        simulations_label = tk.Label(self, text="Simulations:")
        simulations_label.pack()
        simulations_entry = tk.Entry(self, textvariable=self.simulations)
        simulations_entry.pack()

        start_button = tk.Button(self, text="Start Simulation", command=self.start_simulation)
        start_button.pack()

    #The main simulation loop for all of the strategies
    def start_simulation(self):
        self.canvas.delete("all")
        self.label_success.configure(text="Successes: ")
        self.label_trials.configure(text="Trials: ")
        self.label_frequency.configure(text="Relative Frequency: ")
        strategy = self.strategy.get()
        num_simulations = int(self.simulations.get())

        if strategy == "Random Endpoints":
            self.random_endpoints_simulation(num_simulations)
        elif strategy == "Random Radius":
            self.random_radius_simulation(num_simulations)
        elif strategy == "Random Midpoint":
            self.random_midpoint_simulation(num_simulations)
        elif strategy == "My Strategy":
            self.my_strategy_simulation(num_simulations)

    #Random endpoint strategy 
    def random_endpoints_simulation(self, num_simulations):
        successes = 0
        count = 0
        radius = min(self.canvas_width, self.canvas_height) / 2 - 10
        center_x = self.canvas_width / 2
        center_y = self.canvas_height / 2
        self.draw_circle(center_x, center_y, radius)

        for i in range(num_simulations):
            theta1 = random.uniform(0, 2 * math.pi)
            theta2 = random.uniform(0, 2 * math.pi)
            x1, y1 = center_x + radius * math.cos(theta1), center_y + radius * math.sin(theta1)
            x2, y2 = center_x + radius * math.cos(theta2), center_y + radius * math.sin(theta2)

            if self.is_chord_intersecting_circle(x1, y1, x2, y2, center_x, center_y, radius):
                successes += 1
            else:
                self.canvas.create_line(x1, y1, x2, y2, fill='red')

            count += 1
            relative_frequency = successes / count
            self.label_success.configure(text="Successes: {}".format(successes))
            self.label_trials.configure(text="Trials: {}".format(count))
            self.label_frequency.configure(text="Relative Frequency: {:.4f}".format(relative_frequency))
            self.update()

    # Random radius strategy
    def random_radius_simulation(self, num_simulations):
        success = 0
        radius = min(self.canvas_width, self.canvas_height) / 2 - 10
        center_x = self.canvas_width / 2
        center_y = self.canvas_height / 2
        self.draw_circle(center_x, center_y, radius)


        for _ in range (num_simulations):
            theta1 = random.uniform(0, 2 * math.pi)
            theta2 = random.uniform(0, 2 * math.pi)
            x1, y1 = center_x + radius * math.cos(theta1), center_y + radius * math.sin(theta1)
            x2, y2 = center_x + radius * math.cos(theta2), center_y + radius * math.sin(theta2)



            radius_point = random.uniform(0,1.0)
            
            intersect_distance = 1 / 2
            if radius_point < intersect_distance: 
                success += 1 
                if not self.is_chord_intersecting_circle(x1, y1, x2, y2, center_x, center_y, radius):
                    self.canvas.create_line(x1, y1, x2, y2, fill='red')
                
            
            relative_frequency = success / num_simulations
            self.label_success.configure(text="Successes: {}".format(success))
            self.label_trials.configure(text="Trials: {}".format(num_simulations))
            self.label_frequency.configure(text="Relative Frequency: {:.4f}".format(relative_frequency))
            self.update()

    # The random midpoint strategy 
    def random_midpoint_simulation(self, num_simulations):
        successes = 0
        count = 0
        radius = min(self.canvas_width, self.canvas_height) / 2 - 10
        center_x = self.canvas_width / 2
        center_y = self.canvas_height / 2
        self.draw_circle(center_x, center_y, radius)

        for i in range(num_simulations):
            r = random.uniform(0, radius)
            theta1 = random.uniform(0, 2 * math.pi)
            theta2 = random.uniform(0, 2 * math.pi)
            x1, y1 = center_x + radius * math.cos(theta1), center_y + radius * math.sin(theta1)
            x2, y2 = center_x + radius * math.cos(theta2), center_y + radius * math.sin(theta2)

            distance_squared = ((x2 - x1)) ** 2 + (y2 - y1) ** 2
            if distance_squared > (math.sqrt(3.4) * radius) ** 2:
                successes += 1
            else:
                self.canvas.create_line(x1, y1, x2, y2, fill='red')
            count += 1
            relative_frequency = successes / count
            self.label_success.configure(text="Successes: {}".format(successes))
            self.label_trials.configure(text="Trials: {}".format(count))
            self.label_frequency.configure(text="Relative Frequency: {:.4f}".format(relative_frequency))
            self.update()

    # My own strategy 
    def my_strategy_simulation(self, num_simulations): 
        successes = 0
        count = 0
        radius = min(self.canvas_width, self.canvas_height) / 2 - 10
        center_x = self.canvas_width / 2
        center_y = self.canvas_height / 2
        self.draw_circle(center_x, center_y, radius)

        for i in range(num_simulations):
            x1 = random.uniform(-1, 1)
            y1 = random.uniform(-1, 1)
            x2 = random.uniform(-1, 1)
            y2 = random.uniform(-1, 1)
            chord_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


            if chord_length > math.sqrt(3):
                successes += 1
            else:
                theta1 = random.uniform(0, 2 * math.pi)
                theta2 = random.uniform(0, 2 * math.pi)
                x1, y1 = center_x + radius * math.cos(theta1), center_y + radius * math.sin(theta1)
                x2, y2 = center_x + radius * math.cos(theta2), center_y + radius * math.sin(theta2)
                self.canvas.create_line(x1, y1, x2, y2, fill='red')

            count += 1
            relative_frequency = successes / count
            self.label_success.configure(text="Successes: {}".format(successes))
            self.label_trials.configure(text="Trials: {}".format(count))
            self.label_frequency.configure(text="Relative Frequency: {:.4f}".format(relative_frequency))
            self.update()

    #draws the circle
    def draw_circle(self, center_x, center_y, radius):
        self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='black')

    # Determines if the chord is intersecting and the points
    def is_chord_intersecting_circle(self, x1, y1, x2, y2, center_x, center_y, radius):
        distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
        return distance_squared > (math.sqrt(3) * radius) ** 2

if __name__ == "__main__":
    app = BertrandParadoxSimulator()
    app.mainloop()

