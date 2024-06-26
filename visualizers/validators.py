from globals import variables

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def check_points(event):
    # Reset selected values
    variables.insertingMatrix = False
    variables.selfCenter = False
    
    if variables.selected_object != None:
        variables.selected_object.onSelect(selected=False)
    
    # Check for new Value
    if len(variables.obj_shapes) == 0:
        return None
    
    reversedlist = variables.obj_shapes[::-1]
    
    for obj in reversedlist:
        cond = point_inside_polygon(event.x, event.y, obj.coords)
        
        if (cond):
            obj.onSelect(selected=True)
            return obj
        
    return None