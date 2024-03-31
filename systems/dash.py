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
        variables.rot = 0
    
    for widget in variables.frame.winfo_children():
        widget.destroy()
            
    # Create a Text widget with state="disabled" to make it read-only
    pos_string = f"({f"{variables.x_gap}, {variables.y_gap}" if not_selected else f"{variables.selected_object.cpos[0]}, {variables.selected_object.cpos[1]}"})"
    
    text_widget = tk.Label(variables.frame, height=1)
    text_widget.grid(row=0, column=0, columnspan=5 + (0 if not_selected else 2) + (0 if not variables.insertingMatrix else -1))
    text_widget.config(text=f"Selecting : {("Default Display") if not_selected else (variables.selected_object.name)} {pos_string}")
    
    if variables.insertingMatrix:
        width=5
        entry11 = tk.Entry(variables.frame, width=width)
        entry11.grid(row=1, column=0, padx=5)
        entry11.insert(0, 1)
        
        entry12 = tk.Entry(variables.frame, width=width)
        entry12.grid(row=2, column=0, padx=5)
        entry12.insert(0, 0)
        
        entry13 = tk.Entry(variables.frame, width=width)
        entry13.grid(row=3, column=0, padx=5)
        entry13.insert(0, 0)
        
        entry21 = tk.Entry(variables.frame, width=width)
        entry21.grid(row=1, column=1, padx=5)
        entry21.insert(0, 0)
        
        entry22 = tk.Entry(variables.frame, width=width)
        entry22.grid(row=2, column=1, padx=5)
        entry22.insert(0, 1)
        
        entry23 = tk.Entry(variables.frame, width=width)
        entry23.grid(row=3, column=1, padx=5)
        entry23.insert(0, 0)
        
        entry31 = tk.Entry(variables.frame, width=width)
        entry31.grid(row=1, column=2, padx=5)
        entry31.insert(0, 0)
        
        entry32 = tk.Entry(variables.frame, width=width)
        entry32.grid(row=2, column=2, padx=5)
        entry32.insert(0, 0)
        
        entry33 = tk.Entry(variables.frame, width=width)
        entry33.grid(row=3, column=2, padx=5)
        entry33.insert(0, 1)
        
        buttonMtx = tk.Button(variables.frame, text="Back", command=(lambda: toggleMatrix(on_button_click)))
        buttonMtx.grid(row=1, column=3, padx=(0, 10))
        
        buttonExec = tk.Button(variables.frame, text="Transform", command=(lambda: matrixResult([[float(entry11.get()), float(entry12.get()), float(entry13.get())], [float(entry21.get()), float(entry22.get()), float(entry23.get())], [float(entry31.get()), float(entry32.get()), float(entry33.get())]])))
        buttonExec.grid(row=2, column=3, padx=(0, 10))
        
        return
    
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
    
    if not not_selected:
        launch_dash_not_selected(on_button_click)    
        
def launch_dash_not_selected(on_button_click):
    # Create a Rotation Matrix
    entryRot = tk.Entry(variables.frame, width=10)
    entryRot.grid(row=1, column=5, padx=5)
    entryRot.insert(0, float(variables.rot))
    
    buttonRot = tk.Button(variables.frame, text="Rotate", command=lambda: variables.selected_object.rotate(deg=float(entryRot.get())))
    buttonRot.grid(row=2, column=5, padx=(0, 10))
    
    buttonMtx = tk.Button(variables.frame, text="Custom Matrix", command=lambda: toggleMatrix(on_button_click))
    buttonMtx.grid(row=1, column=6, padx=(0, 10))
    
    buttonDel = tk.Button(variables.frame, text="Delete", command=variables.selected_object.destroy)
    buttonDel.grid(row=2, column=6, padx=(0, 10))
        
def launch_dash_matrix():
    None        

def toggleMatrix(on_button_click):
    variables.insertingMatrix = not variables.insertingMatrix
    launch_dash(on_button_click)
    
def matrixResult(transMatrix):
    variables.selected_object.transform(transMatrix)