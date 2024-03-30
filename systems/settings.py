import tkinter as tk
from systems.events import *
from visualizers.shapes import *

def launch_window(window_width, window_height, origin_x, origin_y, obj_shapes):
    # Create the main window
    root = tk.Tk()
    
    # Disable resizing
    root.resizable(width=False, height=False)

    # Set the window title
    root.title("Geometry Transformation")
    
    # Set the window icon
    root.iconbitmap("./globals/icons.ico")
    
    # Create a canvas
    canvas = tk.Canvas(root, width=window_width, height=window_height-100)
    canvas.pack()
    
    # Create a frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    
    bindings(canvas, frame)
    inits(canvas, frame, origin_x, origin_y, obj_shapes)
    
    # Center the window
    center_window(root, window_width, window_height)
    
    return root, canvas

def center_window(window, window_width, window_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y positions for the window to be centered
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window's position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
def bindings(canvas, frame):
    canvas.bind("<Button-1>", lambda event, canvas=canvas, frame=frame : launchDash(event, canvas, frame))

def inits(canvas, frame, origin_x, origin_y, obj_shapes):
    launchDash(None, canvas, frame)
    create_rect(canvas, "red", "red", 1, 1, origin_x, origin_y, obj_shapes)