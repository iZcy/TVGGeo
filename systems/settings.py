import tkinter as tk
from systems.events import *
from visualizers.shapes import *
from globals import variables

def launch_window():
    # Create the main window
    variables.root = tk.Tk()
    
    # Disable resizing
    variables.root.resizable(width=False, height=False)

    # Set the window title
    variables.root.title("Geometry Transformation | 22/499769/TK/54763")
    
    # Set the window icon
    # variables.root.iconbitmap("./globals/icons.ico")
    
    # Create a canvas
    variables.canvas = tk.Canvas(variables.root, width=variables.window_width, height=variables.window_height-130)
    variables.canvas.pack()
    
    # Create a frame
    variables.frame = tk.Frame(variables.root, width=variables.window_width, height=variables.window_height)
    variables.frame.pack(padx=10, pady=10)
    
    bindings()
    inits()
    
    # Center the window
    center_window()

def center_window():
    # Get the screen width and height
    screen_width = variables.root.winfo_screenwidth()
    screen_height = variables.root.winfo_screenheight()

    # Calculate the x and y positions for the window to be centered
    x = (screen_width - variables.window_width) // 2
    y = (screen_height - variables.window_height) // 2

    # Set the window's position
    variables.root.geometry(f"{variables.window_width}x{variables.window_height}+{x}+{y}")
    
def bindings():
    # variables.canvas.bind("<Button-1>", lambda event : on_screen_click(event))
    variables.canvas.bind("<ButtonPress-1>", start_action)
    variables.canvas.bind("<ButtonRelease-1>", stop_action)

def inits():
    launch_dash(on_button_click, reset=True)
    create_rect(width=1, height=1, name="Rect Red", color="red", outline="red", launcher=lambda: launch_dash(on_button_click))