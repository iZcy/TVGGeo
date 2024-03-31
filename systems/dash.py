import tkinter as tk
from globals import variables

def launch_dash(on_button_click, reset=False):
    entryNull = tk.Entry(variables.frame)
    entryNull.insert(0, 0)
    
    not_selected=variables.selected_object == None
    
    if reset:
        variables.trans_x = 0
        variables.trans_y = 0
        variables.scale_x = 1
        variables.scale_y = 1
    
    # Create a Text widget with state="disabled" to make it read-only
    pos_string = f"({f"{variables.x_gap}, {variables.y_gap}" if not_selected else f"{variables.selected_object.dpos[0]}, {variables.selected_object.dpos[1]}"})"
    
    text_widget = tk.Label(variables.frame, text=f"Selecting : {"Default Display" if not_selected else variables.selected_object.name} {pos_string}", height=1)
    text_widget.grid(row=0, column=0, columnspan=5)
    
    # Create a Translate X
    entryTX = tk.Entry(variables.frame, width=10)
    entryTX.grid(row=1, column=0, padx=5)
    entryTX.insert(0, float(variables.trans_x))
    
    buttonTX = tk.Button(variables.frame, text="Translate X", command=(lambda: on_button_click(entry=entryTX, type="x")) if not_selected else (lambda: variables.selected_object.move(posX=float(entryTX.get()))))
    buttonTX.grid(row=1, column=1, padx=(0, 10))
    
    # Create a Translate Y
    entryTY = tk.Entry(variables.frame, width=10)
    entryTY.grid(row=2, column=0, padx=5)
    entryTY.insert(0, float(variables.trans_y))
    
    buttonTY = tk.Button(variables.frame, text="Translate Y", command=(lambda: on_button_click(entry=entryTY, type="y")) if not_selected else (lambda: variables.selected_object.move(posY=float(entryTY.get()))))
    buttonTY.grid(row=2, column=1, padx=(0, 10))
    
    # Create a Scale X
    entrySx = tk.Entry(variables.frame, width=10)
    entrySx.grid(row=1, column=2, padx=5)
    entrySx.insert(0, float(variables.scale_x))
    
    buttonSx = tk.Button(variables.frame, text="Scale X", command=(lambda: on_button_click(entry=entrySx, type="sx")) if not_selected else (lambda: variables.selected_object.scale(scaleX=float(entrySx.get()))))
    buttonSx.grid(row=1, column=3, padx=(0, 10))
    
    # Create a Scale Y
    entrySy = tk.Entry(variables.frame, width=10)
    entrySy.grid(row=2, column=2, padx=5)
    entrySy.insert(0, float(variables.scale_y))
    
    buttonSy = tk.Button(variables.frame, text="Scale Y", command=(lambda: on_button_click(entry=entrySy, type="sy")) if not_selected else (lambda: variables.selected_object.scale(scaleY=float(entrySy.get()))))
    buttonSy.grid(row=2, column=3, padx=(0, 10))
    
    # Create a Reflect X
    buttonRx = tk.Button(variables.frame, text="Reflect X", command=(lambda: on_button_click(entry=entryNull, type="rx")) if not_selected else (lambda: variables.selected_object.reflect(axis="x")))
    buttonRx.grid(row=1, column=4, padx=(0, 10))
    
    # Create a Reflect Y
    buttonRy = tk.Button(variables.frame, text="Reflect Y", command=(lambda: on_button_click(entry=entryNull, type="ry")) if not_selected else (lambda: variables.selected_object.reflect(axis="y")))
    buttonRy.grid(row=2, column=4, padx=(0, 10))