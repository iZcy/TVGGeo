from globals.variables import pixelgap

def draw_cartesian(canvas, width, height, origin_x, origin_y, color, zoomX, zoomY):
    # Draw x-axis
    canvas.create_line(0, origin_y, width, origin_y, fill=color, width=2)

    # Draw y-axis
    canvas.create_line(origin_x, 0, origin_x, height, fill=color, width=2)

    # Draw x-axis tick marks and labels
    for i in range(-width, width):
        x = origin_x + i * (width*zoomX/20)
        canvas.create_line(x, origin_y-5, x, origin_y+5, fill=color, width=2)
        canvas.create_text(x, origin_y+10, text=str(i), anchor="n")

    # Draw y-axis tick marks and labels
    for i in range(-height, height):
        y = origin_y - i * (height*zoomY/20)
        canvas.create_line(origin_x-5, y, origin_x+5, y, fill=color, width=2)
        canvas.create_text(origin_x-15, y, text=str(i), anchor="e")
    

def draw_objects(canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY, obj_shapes):
    canvas.delete("all")
    
    if len(obj_shapes) != 0:
        for obj in obj_shapes:
            deltapos = [x + y for x, y in zip(obj.dpos, [-x_gap*pixelgap, y_gap*pixelgap])]
            result = [[x + y for x, y in zip(sublist, deltapos)] for sublist in obj.coords]
            vert_list = sum(result, [])
            canvas.create_polygon(vert_list, fill=obj.color, outline=obj.outline, width=2)
    
    # Draw Cartesian coordinate system
    draw_cartesian(canvas, window_width, window_height, origin_x = (origin_x - x_gap*pixelgap)*zoomX, origin_y = (origin_y + y_gap*pixelgap)*zoomY, color="black", zoomX=zoomX, zoomY=zoomY)