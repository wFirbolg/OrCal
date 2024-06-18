import tkinter as tk
from tkinter import ttk
from appearance import get_font, set_theme

class VolumetricSpeedCalculator:
    def __init__(self, frame, log_callback):
        self.frame = frame
        self.log_callback = log_callback
        self.setup_ui()

    def setup_ui(self):
        # Setup title label
        title = ttk.Label(self.frame, text="Max Volumetric Speed", font=get_font('title'))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Center the UI elements properly
        self.frame.update_idletasks()
        self.frame.grid_columnconfigure(0, weight=10)
        self.frame.grid_columnconfigure(1, weight=2)

        # Setup start speed input fields
        self.start_speed_label = ttk.Label(self.frame, text="Start Vol. Speed (mm³/s):", font=get_font('label'))
        self.start_speed_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.start_speed_entry = ttk.Entry(self.frame, font=get_font('entry'), width=10)
        self.start_speed_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Setup end speed input fields
        self.end_speed_label = ttk.Label(self.frame, text="End Vol. Speed (mm³/s):", font=get_font('label'))
        self.end_speed_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.end_speed_entry = ttk.Entry(self.frame, font=get_font('entry'), width=10)
        self.end_speed_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # Setup step input fields
        self.step_label = ttk.Label(self.frame, text="Step (mm³/s):", font=get_font('label'))
        self.step_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.step_entry = ttk.Entry(self.frame, font=get_font('entry'), width=10)
        self.step_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # Setup measured height input fields
        self.measured_height_label = ttk.Label(self.frame, text="Measured Height:", font=get_font('label'))
        self.measured_height_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.measured_height_entry = ttk.Entry(self.frame, font=get_font('entry'), width=10)
        self.measured_height_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        # Setup calculate button
        # Setup calculate button
        # Re-add the calculate button that was removed
        self.calculate_btn = ttk.Button(self.frame, text="Calculate", command=self.calculate_vmax, style="Custom.TButton")
        self.calculate_btn.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        # Setup result display fields
        self.result_label = ttk.Label(self.frame, text="Max Volumetric Speed:", font=get_font('label'))
        self.result_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.result_value = ttk.Label(self.frame, text="", font=get_font('result'))
        self.result_value.grid(row=6, column=1, padx=5, pady=5, sticky='w')

    def calculate_vmax(self):
        # Retrieve and convert input values
        start_speed = float(self.start_speed_entry.get())
        step = float(self.step_entry.get())
        measured_height = float(self.measured_height_entry.get())

        # Calculate max volumetric speed
        max_v_speed = start_speed + (measured_height * step)

        # Update result in the UI
        self.result_value.config(text=f"{max_v_speed:.5f} mm³/s")

        # Log the values used and the result
        self.log_callback(f"Volumetric Speed Calibration: Start Speed: {start_speed}, Step: {step}, Measured Height: {measured_height}, Max Volumetric Speed: {max_v_speed:.5f} mm³/s")