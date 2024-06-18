import tkinter as tk
from tkinter import ttk
from appearance import get_font, set_theme

class PressureAdvanceCalculator:
    def __init__(self, frame, log_callback):
        # Initialize the frame and log callback
        self.frame = frame
        self.log_callback = log_callback
        self.setup_ui() # Setup the UI components

    def setup_ui(self):
        # Create and position the title label
        title = ttk.Label(self.frame, text="Pressure Advance", font=get_font('title'))
        title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.frame.update_idletasks()
        self.frame.grid_columnconfigure(0, weight=10)
        self.frame.grid_columnconfigure(1, weight=2)

        # Create and position the start value label and entry field
        self.start_value_label = ttk.Label(self.frame, text="Start Value:", font=get_font('label'))
        self.start_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.start_value_entry = ttk.Entry(self.frame, font=get_font('entry'), width=5)
        self.start_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Create and position the step value label and entry field
        self.step_value_label = ttk.Label(self.frame, text="Step Value:", font=get_font('label'))
        self.step_value_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.step_value_entry = ttk.Entry(self.frame, font=get_font('entry'), width=5)
        self.step_value_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Create and position the measured height label and entry field
        self.measured_height_label = ttk.Label(self.frame, text="Measured Height:", font=get_font('label'))
        self.measured_height_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.measured_height_entry = ttk.Entry(self.frame, font=get_font('entry'), width=5)
        self.measured_height_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Create and position the calculate button
        calculate_btn = ttk.Button(self.frame, text="Calculate", command=self.calculate_pressure_advance, style="Custom.TButton")
        calculate_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Create and position the result label and value display
        self.result_label = ttk.Label(self.frame, text="Pressure Advance Value:", font=get_font('label'))
        self.result_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.result_value = ttk.Label(self.frame, text="", font=get_font('result'))
        self.result_value.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    def calculate_pressure_advance(self):
        try:
            # Convert input values to floats
            start_value = float(self.start_value_entry.get())
            step_value = float(self.step_value_entry.get())
            measured_height = float(self.measured_height_entry.get())

            # Calculate new PA value
            new_pa_value = start_value + (step_value * measured_height)

            # Update the result label with the new PA value
            self.result_value.config(text=f"{new_pa_value:.5f}")

            # Log the calculation details
            self.log_callback(f"Pressure Advance Calibration: Start Value: {start_value}, Step Value: {step_value}, Measured Height: {measured_height}, New PA Value: {new_pa_value:.5f}")
        except ValueError:
            # Handle invalid input errors
            self.result_value.config(text="Invalid input")
            self.log_callback("Pressure Advance Calculation Error: Invalid input")