import tkinter as tk
from tkinter import ttk
from appearance import get_entry_width, get_font, set_theme

class FlowRateCalculator:
    def __init__(self, frame, log_callback):
        self.frame = frame
        self.log_callback = log_callback
        self.pass_one_complete = False
        self.old_ratio = 0
        self.new_ratio = 0
        self.setup_ui()

    def setup_ui(self):
        # Set up the title of the calculator
        title = ttk.Label(self.frame, text="Flow Rate", font=get_font('title'))
        title.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Center the UI elements with a fixed window width of 420 px
        self.frame.update_idletasks()
        window_width = 420
        frame_width = self.frame.winfo_width()
        pad_x = (window_width - frame_width) // 2

        # Input field for the old flow ratio
        self.old_ratio_label = ttk.Label(self.frame, text="Current Flow Ratio:", font=get_font('label'))
        self.old_ratio_label.grid(row=1, column=0, padx=(pad_x, 10), pady=5)
        self.old_ratio_entry = ttk.Entry(self.frame, font=get_font('entry'), 
width=get_entry_width())
        self.old_ratio_entry.grid(row=1, column=1, padx=10, pady=5)
        # Label for selecting the modifier values
        self.modifier_label = ttk.Label(self.frame, text="Select Modifier (Pass 1):", font=get_font('label'))
        self.modifier_label.grid(row=2, column=0, columnspan=2, padx=(pad_x, 10), pady=5)

        # Frame to hold the modifier buttons
        self.modifier_buttons_frame = ttk.Frame(self.frame)
        self.modifier_buttons_frame.grid(row=3, column=0, columnspan=5, padx=(pad_x, 10), pady=5)

        # Create and display buttons for Pass 1 modifiers
        self.create_modifier_buttons_pass_one()

        # Label to display the results
        self.result_label = ttk.Label(self.frame, text="New Flow Ratio:", font=get_font('label'))
        self.result_label.grid(row=4, column=0, padx=(pad_x, 10), pady=5)
        self.result_value = ttk.Label(self.frame, text="", font=get_font('result'))
        self.result_value.grid(row=4, column=1, padx=10, pady=5)

        # Add reset button
        reset_button = ttk.Button(self.frame, text="Reset", style="Custom.TButton", command=self.reset_calculator)
        reset_button.grid(row=5, column=1, columnspan=10, pady=10)

    def create_modifier_buttons_pass_one(self):
        # List of modifier values and their grid positions for Pass 1
        modifiers = [20, 15, 10, 5, 0, -5, -10, -15, -20]
        position = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for i, modifier in enumerate(modifiers):
            row, col = position[i]
            btn = ttk.Button(self.modifier_buttons_frame, text=f"{modifier}", style="Custom.TButton", command=lambda m=modifier: self.calculate_flow_rate(m))
            btn.grid(row=row, column=col, padx=2, pady=2)

    def create_modifier_buttons_pass_two(self):
        # List of modifier values and their grid positions for Pass 2
        modifiers = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        position = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
        # Destroy any existing widgets in the modifier_buttons_frame
        for widget in self.modifier_buttons_frame.winfo_children():
            widget.destroy()
        for i, modifier in enumerate(modifiers):
            row, col = position[i]
            btn = ttk.Button(self.modifier_buttons_frame, text=f"{modifier}", style="Custom.TButton", command=lambda m=modifier: self.calculate_flow_rate(m))
            btn.grid(row=row, column=col, padx=2, pady=2)

    def calculate_flow_rate(self, modifier):
        # Check if Pass 1 is complete
        if not self.pass_one_complete:
            self.old_ratio = float(self.old_ratio_entry.get())
            self.new_ratio = self.old_ratio * (100 + modifier) / 100
            self.result_value.config(text=f"{self.new_ratio:.5f}")
            self.log_callback(f"Flow Rate Calibration Pass 1: Old Ratio: {self.old_ratio}, Modifier: {modifier}, New Ratio: {self.new_ratio:.5f}")
            self.pass_one_complete = True
            self.modifier_label.config(text="Select Modifier (Pass 2):")
            self.create_modifier_buttons_pass_two()
        else:
            final_ratio = self.new_ratio * (100 + modifier) / 100
            self.result_value.config(text=f"{final_ratio:.5f}")
            self.log_callback(f"Flow Rate Calibration Pass 2: Pass 1 New Ratio: {self.new_ratio}, Modifier: {modifier}, Final New Ratio: {final_ratio:.5f}")
            for widget in self.modifier_buttons_frame.winfo_children():
                widget.config(state=tk.DISABLED)

    def reset_calculator(self):
        # Reset all input and output fields
        self.old_ratio_entry.delete(0, tk.END)
        self.result_value.config(text="")
        self.pass_one_complete = False
        self.modifier_label.config(text="Select Modifier (Pass 1):")
        # Destroy existing widgets and re-create Pass 1 buttons
        for widget in self.modifier_buttons_frame.winfo_children():
            widget.destroy()
        self.create_modifier_buttons_pass_one()