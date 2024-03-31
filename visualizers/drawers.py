from globals import variables

def draw_cartesian(color):
    origin_x = (variables.origin_x - variables.x_gap*variables.pixelgap)*variables.zoomX
    origin_y = (variables.origin_y + variables.y_gap*variables.pixelgap)*variables.zoomY

    zoomX=variables.zoomX
    zoomY=variables.zoomY
    
    # Draw x-axis
    variables.canvas.create_line(0, origin_y, variables.window_width, origin_y, fill=color, width=2)

    # Draw y-axis
    variables.canvas.create_line(origin_x, 0, origin_x, variables.window_height, fill=color, width=2)

    # Draw x-axis tick marks and labels
    for i in range(-variables.window_width, variables.window_width):
        x = origin_x + i * (variables.window_width*zoomX/20)
        variables.canvas.create_line(x, origin_y-5, x, origin_y+5, fill=color, width=2)
        variables.canvas.create_text(x, origin_y+10, text=str(i), anchor="n")

    # Draw y-axis tick marks and labels
    for i in range(-variables.window_height, variables.window_height):
        y = origin_y - i * (variables.window_height*zoomY/20)
        variables.canvas.create_line(origin_x-5, y, origin_x+5, y, fill=color, width=2)
        variables.canvas.create_text(origin_x-15, y, text=str(i), anchor="e")
    

def draw_shapes():
    if len(variables.obj_shapes) != 0:
        for obj in variables.obj_shapes:
            vert_list = sum(obj.coords, [])
            variables.canvas.create_polygon(vert_list, fill=obj.color, outline=obj.outline, width=2)

def draw_objects():
    variables.canvas.delete("all")
    
    # Draw Shapes existing
    draw_shapes()
    
    # Draw Cartesian coordinate system
    draw_cartesian(color="black")