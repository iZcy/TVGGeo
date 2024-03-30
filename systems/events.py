import tkinter as tk
from visualizers.drawers import *
from visualizers.validators import *
from globals.variables import *

def launchDash(event, canvas, frame):
    global obj_shapes
    
    # Destroy or remove all widgets contained within the frame
    for widget in frame.winfo_children():
        widget.destroy()
        
    selected_object = check_points(event, obj_shapes)
    
    not_selected = selected_object == None
    
    # Create a Text widget with state="disabled" to make it read-only
    text_widget = tk.Label(frame, text=f"Selecting : {"Default Display" if not_selected else selected_object.name}", height=1)
    text_widget.grid(row=0, column=0, columnspan=4)
    
    # Create a Translate X
    entryTX = tk.Entry(frame, width=10)
    entryTX.grid(row=1, column=0, padx=5)
    entryTX.insert(0, 0)
    
    buttonTX = tk.Button(frame, text="Swipe X", command=((lambda: on_button_click(canvas, entry=entryTX, type="x"))) if not_selected else (lambda: selected_object.move(posX=float(entryTX.get()))))
    buttonTX.grid(row=1, column=1, padx=(0, 10))
    
    # Create a Translate Y
    entryTY = tk.Entry(frame, width=10)
    entryTY.grid(row=1, column=2, padx=5)
    entryTY.insert(0, 0)
    
    buttonTY = tk.Button(frame, text="Swipe Y", command=((lambda: on_button_click(canvas, entry=entryTY, type="y"))) if not_selected else (lambda: selected_object.move(posY=float(entryTY.get()))))
    buttonTY.grid(row=1, column=3, padx=(0, 10))
    
    # Create a Scale X
    entrySx = tk.Entry(frame, width=10)
    entrySx.grid(row=2, column=0, padx=5)
    entrySx.insert(0, 1)
    
    buttonSx = tk.Button(frame, text="Zoom X", command=lambda: on_button_click(canvas, entry=entrySx, type="sx"))
    buttonSx.grid(row=2, column=1, padx=(0, 10))
    
    # Create a Scale Y
    entrySy = tk.Entry(frame, width=10)
    entrySy.grid(row=2, column=2, padx=5)
    entrySy.insert(0, 1)
    
    buttonSy = tk.Button(frame, text="Zoom Y", command=lambda: on_button_click(canvas, entry=entrySy, type="sy"))
    buttonSy.grid(row=2, column=3, padx=(0, 10))

def on_button_click(canvas, entry, type):
    global x_gap, y_gap, zoomX, zoomY, window_width, window_height, origin_x, origin_y, obj_shapes, obj_shapes
    
    text = entry.get()

    resp = float(text)

    if (type == "x"):
        x_gap += float(text)
    elif (type == "y"):
        y_gap += float(text)
    elif (type == "sx" and resp != 0):
        zoomX *= float(text)
    elif (type == "sy" and resp != 0):
        zoomY *= float(text)
    
    draw_objects(canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY, obj_shapes)