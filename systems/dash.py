import tkinter as tk
from globals import variables
from visualizers.drawers import *
from visualizers.shapes import *
import random

def launch_dash(on_button_click, reset=False):
    not_selected=variables.selected_object == None
    
    if reset:
        variables.trans_x = 0
        variables.trans_y = 0
        variables.scale_x = 1
        variables.scale_y = 1
        variables.rot = 0
    
    for widget in variables.frame.winfo_children():
        widget.destroy()
    
    if variables.creatingObject:
        launch_dash_object(on_button_click)
        return
    
    if variables.creatingCustomObject:
        launch_dash_custom_object(on_button_click)
        draw_objects()
        return
    
    launch_title(not_selected)
    
    if variables.insertingMatrix:
        launch_dash_matrix(on_button_click)
        draw_objects()
        return
    
    launch_dash_normal(on_button_click, not_selected)
    
    if not not_selected:
        launch_dash_selected(on_button_click)    

    draw_objects()

def launch_title(not_selected):
    # Create a Text widget with state="disabled" to make it read-only
    pos_string = ""
    if not not_selected:
        cpos = variables.selected_object.getNormCpos()
        pos_string = f"({f"{variables.x_gap}, {variables.y_gap}" if not_selected else f"{"{:.{}f}".format(cpos[0], 3)}, {"{:.{}f}".format(cpos[1], 3)}"})"

    text_widget = tk.Label(variables.frame, height=1)
    text_widget.grid(row=0, column=0, columnspan=5 + (0 if not_selected else 2) + (0 if not variables.insertingMatrix else -1))
    text_widget.config(text=f"Selecting : {(f"Default Display ({"{:.{}f}".format(variables.x_gap, 3)}, {"{:.{}f}".format(variables.y_gap, 3)}) (Please click an existing Shape)") if not_selected else (variables.selected_object.name)} {pos_string}")

def launch_dash_normal(on_button_click, not_selected):
    entryNull = tk.Entry(variables.frame)
    entryNull.insert(0, 0)
    
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
    
    if not_selected:
        # Create an Object Creator
        buttonCreate = tk.Button(variables.frame, text="Create Object", command=(lambda on_button_click=on_button_click : toggleSelectCreate(on_button_click)))
        buttonCreate.grid(row=3, column=0, columnspan=5, padx=(0, 10))

def launch_dash_selected(on_button_click):
    # Create a Rotation Matrix
    entryRot = tk.Entry(variables.frame, width=10)
    entryRot.grid(row=1, column=5, padx=5)
    entryRot.insert(0, float(variables.rot))
    
    buttonRot = tk.Button(variables.frame, text="Rotate", command=lambda: variables.selected_object.rotate(deg=float(entryRot.get())))
    buttonRot.grid(row=2, column=5, padx=(0, 10))
    
    # Custom Matrix
    buttonMtx = tk.Button(variables.frame, text="Custom Matrix", command=lambda: toggleMatrix(on_button_click))
    buttonMtx.grid(row=1, column=6, padx=(0, 10))
    
    # Delete Object
    buttonDel = tk.Button(variables.frame, text="Delete", command=variables.selected_object.destroy)
    buttonDel.grid(row=2, column=6, padx=(0, 10))
    
    # Checkbox on self center
    checkbox_var = tk.BooleanVar(value=variables.selfCenter)
    checkbox = tk.Checkbutton(variables.frame, text="Self-Center Transformation", variable=checkbox_var, command=(lambda: toggleSelfCenter(checkbox_var.get())))
    checkbox.grid(row=3, column=0, columnspan=7)

def launch_dash_matrix(on_button_click):
    matrix = variables.matrixCache
    
    # Create Entry widgets
    entries = [[tk.Entry(variables.frame, width=5) for _ in range(3)] for _ in range(3)]
    
    get_float = lambda entry: float(entry.get())
    
    for i, row in enumerate(entries):
        for j, entry in enumerate(row):
            entry.grid(row=j+1, column=i, padx=5)
            entry.insert(0, matrix[i][j])
    
    construct_matrix = lambda: [[get_float(entry) for entry in row] for row in entries]
    
    buttonMtx = tk.Button(variables.frame, text="Back", command=(lambda: toggleMatrix(on_button_click)))
    buttonMtx.grid(row=1, column=3, padx=(0, 10))
    
    buttonExec = tk.Button(variables.frame, text="Transform", command=(lambda: inputMatrixChanges(construct_matrix())))
    buttonExec.grid(row=2, column=3, padx=(0, 10))
    
    # Checkbox on self center
    checkbox_var = tk.BooleanVar(value=variables.selfCenter)
    checkbox = tk.Checkbutton(variables.frame, text="Self-Center", variable=checkbox_var, command=(lambda: toggleSelfCenter(checkbox_var.get())))
    checkbox.grid(row=3, column=3)

def launch_dash_object(on_button_click):
    shapes = ["Triangle", "Rectangle", "Pentagon", "Hexagon", "Circle", "Custom"]
    obj_string = "Please choose what object would you like to make (click screen to go back)."
    obj_widget = tk.Label(variables.frame, height=1, text=obj_string)
    obj_widget.grid(row=1, column=0, columnspan=len(shapes))
    
    entries = [tk.Entry(variables.frame, width=10) for _ in range(2)]
    for i, entry in enumerate(entries):
        entry.grid(row=3, column=[2, 3][i])
        entry.insert(0, 0)
        
    get_value = lambda entry: float(entry.get())
    get_entries = lambda: [get_value(entry) for entry in entries]
        
    coor_string = "Custom Center: "
    coor_widget = tk.Label(variables.frame, height=1, text=coor_string)
    coor_widget.grid(row=3, column=0, columnspan=2)
    
    buttons = [tk.Button(variables.frame, text=shapes[i], command=(lambda on_button_click = on_button_click, i=i, center=lambda: get_entries() : toggleSelectCreate(on_button_click, i, center))) for i in range(len(shapes))]
    for i, button in enumerate(buttons):
        button.grid(row=2, column=i)
        
    # Checkbox on self center
    checkbox_var = tk.BooleanVar(value=variables.useDefaultCenter)
    checkbox = tk.Checkbutton(variables.frame, text="Use Default Center (ignore custom center)", variable=checkbox_var, command=(lambda: toggleUseDefCenter(checkbox_var.get())))
    checkbox.grid(row=4, column=0, columnspan=len(shapes))

def launch_dash_custom_object(on_button_click):
    obj_string = "Create your object. Please pick the points on the screen."
    obj_widget = tk.Label(variables.frame, height=1, text=obj_string)
    obj_widget.grid(row=1, column=0, columnspan=5)
    
    buttonMtx = tk.Button(variables.frame, text="Complete", command=(lambda: toggleCreate(on_button_click)))
    buttonMtx.grid(row=2, column=0, columnspan=5, padx=(0, 10))
    
    polyColor = randomColor()
    newPoly = Shapes(name=f"Object {variables.numObj}", color=polyColor, outline=polyColor, coords=[], launcher=lambda: launch_dash(on_button_click))
    variables.numObj += 1
    
    variables.obj_shapes.append(newPoly)
    variables.editingObject = newPoly

def toggleMatrix(on_button_click):
    variables.insertingMatrix = not variables.insertingMatrix
    if not variables.insertingMatrix:
        variables.matrixCache = variables.matrixDefault
    
    launch_dash(on_button_click)
    
def inputMatrixChanges(matrix):
    variables.matrixCache = matrix
    variables.selected_object.transform(matrix)

def toggleSelectCreate(on_button_click, idx=0, center=lambda: [0, 0]):
    if variables.creatingObject:
        variables.customCenter = center()
        color = randomColor()
        height = 2
        width = 2
        name = f"Object {variables.numObj}"
        variables.numObj += 1
        launcher = lambda: launch_dash(on_button_click)
        
        if idx == 0:
            create_triangle(name=name, base=width, height=height, color=color, outline=color, launcher=launcher)
        elif idx == 1:
            create_rect(name=name, width=width, height=height, color=color, outline=color, launcher=launcher)
        elif idx == 2:
            create_pentagon(side_length=width, name=name, color=color, outline=color, launcher=launcher)
        elif idx == 3:
            create_hexagon(side_length=width, name=name, color=color, outline=color, launcher=launcher)
        elif idx == 4:
            create_circle(radius=width, name=name, color=color, outline=color, launcher=launcher)
        elif idx == 5:
            variables.creatingCustomObject = True
            
        if idx != 5:
            draw_objects()
            variables.useDefaultCenter = True
    
    variables.creatingObject = not variables.creatingObject
    launch_dash(on_button_click)

def toggleCreate(on_button_click):
    if variables.creatingCustomObject:
        variables.creatingCustomObject = False
        
        if len(variables.editingObject.coords) != 0:
            variables.editingObject.setRealCenter()
            
            if not variables.useDefaultCenter:
                getCenter = getNormPos([variables.editingObject.cpos])[0]
                transX, transY = [(variables.customCenter[i] - curr) for i, curr in enumerate(getCenter)]
                translate = getTranslateMatrix(transX=transX, transY=transY)
                variables.editingObject.transform(transMatrix=translate)
        else:
            variables.editingObject.destroy()
        
        variables.editingObject = None
        variables.customCenter = [0, 0]
        
    variables.creatingCustomObject = False
    variables.creatingObject = False
    variables.useDefaultCenter = True
    
    launch_dash(on_button_click)
    
def toggleSelfCenter(value):
    variables.selfCenter = value

def toggleUseDefCenter(value):
    variables.useDefaultCenter = value

def randomColor():
    return rgb_to_hex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def rgb_to_hex(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)