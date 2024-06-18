from tkinter import ttk

# Retrieve the font settings for a specific UI element
def get_font(element):
    common_font = ('Lato')
    fonts = {
        'title': ('Lato', 16),
        'label': (common_font, 10),
        'entry': (common_font, 10),
        'result': (common_font, 10),
        'button': (common_font, 10)
    }
    return fonts[element]

# Get the style configuration for a specific button style
def get_button_style(style):
    styles = {
        'Custom.TButton': {
            'font': ('button', 10),
            'padding': [2, 2],
            'width': 8  # Set the width to allow for 5 characters
        }
    }
    return styles[style]

# Define the width for all input fields
def get_entry_width():
    return 5 # Set the width of all input fields to 5 characters

# Configure the styles for the application
def configure_styles():
    style = ttk.Style()
    style.theme_use('clam')
    button_style = get_button_style('Custom.TButton')
    style.configure('Custom.TButton', font=button_style['font'], padding=button_style['padding'], width=button_style['width'])

# Set the color theme for the application window
def set_theme(window):
    window.tk_setPalette(
        background='#3d4445',  # Dark Slate Gray RGB(61, 68, 69)
        foreground='#d3d3d3',  # Light Gray RGB(211, 211, 211)
        activeBackground='#419487',  # Aquamarine RGB(65, 148, 135)
        activeForeground='#d3d3d3'  # Light Gray RGB(211, 211, 211)
    )