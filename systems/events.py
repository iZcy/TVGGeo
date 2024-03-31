from visualizers.drawers import *
from visualizers.validators import *
from globals import variables
from systems.dash import launch_dash

def on_screen_click(event):
    # Destroy or remove all widgets contained within the frame
    for widget in variables.frame.winfo_children():
        widget.destroy()
    
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
    if (resp == 0):
        None
    elif (type == "x"):
        variables.x_gap += resp
        variables.trans_x = resp
    elif (type == "y"):
        variables.y_gap += resp
        variables.trans_y = resp
    elif (type == "sx"):
        variables.zoomX *= resp
        variables.scale_x = resp
    elif (type == "sy"):
        variables.zoomY *= resp
        variables.scale_y = resp
        
    # Move the objects relative to the plane
    for obj in variables.obj_shapes:
        for axis in obj.coords:
            if (resp == 0):
                break
            elif (type == "x"):
                axis[0] -= variables.pixelgap*resp*variables.zoomX
            elif (type == "y"):
                axis[1] += variables.pixelgap*resp*variables.zoomY
            elif (type == "sx"):
                axis[0] *= resp
            elif (type == "sy"):
                axis[1] *= resp
    
    draw_objects()
    launch_dash(on_button_click)