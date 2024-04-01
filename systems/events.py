from visualizers.drawers import *
from visualizers.validators import *
from globals import variables
from systems.dash import launch_dash

def on_screen_click(event):
    if variables.insertingMatrix or variables.creatingCustomObject:
        return
    
    variables.creatingObject = False
    
    prevName = None
    if variables.selected_object != None:
        prevName = variables.selected_object.name
    
    variables.selected_object = check_points(event)
    
    sameName = False
    if variables.selected_object != None and prevName != None:
        nowName = variables.selected_object.name
        sameName = prevName == nowName
    
    launch_dash(on_button_click, reset=(variables.selected_object != None) and not sameName)

def on_button_click(entry, type):
    text = entry.get()
    resp = float(text)

    # Move the plane
    if (type == "rx"):
        variables.zoomY *= -1
    elif (type == "ry"):
        variables.zoomX *= -1
    
    if (resp == 0):
        None
    elif (type == "x"):
        variables.x_gap += resp*variables.zoomX
        variables.trans_x = resp
    elif (type == "y"):
        variables.y_gap += resp*variables.zoomY
        variables.trans_y = resp
    elif (type == "sx"):
        variables.zoomX *= resp
        variables.scale_x = resp
    elif (type == "sy"):
        variables.zoomY *= resp
        variables.scale_y = resp
        
    # Move the objects relative to the plane
    for obj in variables.obj_shapes:
        if (type == "rx"):
            obj.scale(scaleY=-1, static=True)
        elif (type == "ry"):
            obj.scale(scaleX=-1, static=True)
        
        if (resp == 0):
            break
        elif (type == "x"):
            obj.move(posX=-resp, static=True)
        elif (type == "y"):
            obj.move(posY=-resp, static=True)
        elif (type == "sx"):
            obj.scale(scaleX=resp, static=True)
        elif (type == "sy"):
            obj.scale(scaleY=resp, static=True)
        elif (type == "rx"):
            obj.reflect(axis="x", static=False)
        elif (type == "ry"):
            obj.reflect(axis="y", static=False)
    
    draw_objects()
    launch_dash(on_button_click)
    
def start_action(event):
    if variables.creatingCustomObject:
        # Bind motion event to continuously update coordinates
        variables.canvas.bind("<Motion>", lambda event : on_vertex_pick(event))
    else:
        on_screen_click(event)

def stop_action(event=None):
    if variables.creatingCustomObject:
        # Unbind motion event when the mouse button is released
        variables.canvas.unbind("<Motion>")
    
def on_vertex_pick(event):
    variables.editingObject.coords.append([event.x, event.y])
    draw_objects()