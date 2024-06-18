import tkinter as tk
import webbrowser
from tkinter import ttk
from flow_rate_calculator import FlowRateCalculator
from pressure_advance_calculator import PressureAdvanceCalculator
from volumetric_speed_calculator import VolumetricSpeedCalculator
from appearance import set_theme

# Function to save messages to a log file.
def save_to_log(message):
    with open("calibration_log.txt", "a") as log_file:
        log_file.write(message + "\n")  # Append message to the log file with a newline.

# Initialize main application window.
window = tk.Tk()
window.title("OrCal")  # Set window title.
window.geometry("340x550")  # Set window dimensions.
window.resizable(False, False)  # Disable resizing of the window.
set_theme(window)  # Apply the selected theme to the window.

# Create a notebook for tabbed interface.
notebook = ttk.Notebook(window)
notebook.pack(expand=1, fill='both')  # Expand to fill both directions.

# Create frames for each tab in the notebook.
flow_rate_frame = ttk.Frame(notebook)
pressure_advance_frame = ttk.Frame(notebook)
volumetric_speed_frame = ttk.Frame(notebook)

# Add frames to notebook tabs.
notebook.add(flow_rate_frame, text='Flow Rate')
notebook.add(pressure_advance_frame, text='Pressure Advance')
notebook.add(volumetric_speed_frame, text='Max Volumetric Speed')

# Initialize calculator objects with corresponding frames and log function.
FlowRateCalculator(flow_rate_frame, save_to_log)
PressureAdvanceCalculator(pressure_advance_frame, save_to_log)
VolumetricSpeedCalculator(volumetric_speed_frame, save_to_log)

# Create disclaimer label at the bottom of the window.
disclaimer_text = """Disclaimer\n\nThis tool was developed by wFirbolg and he is not affiliated with, endorsed by, or supported by SoftFever, the creators of Orca Slicer. Orca Slicer is a trademark of SoftFever. Use of this trademark is solely for reference purposes and does not imply any endorsement or partnership.\n\nThis tool is used for the calibration of 3D printers using the Orca Slicer. Always ensure to follow the safety guidelines and procedures while working with your 3D printer."""
disclaimer = tk.Label(window, text=disclaimer_text, bg='#3d4445', fg='#d3d3d3', wraplength=300, justify='left')
disclaimer.pack(side='bottom', pady=10)  # Place the disclaimer at the bottom with padding.

# Add link to GitHub profile at the bottom.
github_link = tk.Label(window, text='wFirbolg', fg='#d3d3d3', cursor='hand2')
github_link.pack(side='bottom', pady=7)
github_link.bind("<Button-1>", lambda e: webbrowser.open_new('https://github.com/wFirbolg'))

# Start the main loop. 
window.mainloop() # Start the Tkinter event loop.