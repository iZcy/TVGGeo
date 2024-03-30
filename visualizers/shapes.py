from globals.variables import *
from visualizers.drawers import *

class Shapes:
    def __init__(self, name, canvas, color="black", outline="black", coords=[[0,0]], dpos = [0,0]):
        self.name = name
        self.coords = coords
        self.dpos = dpos
        self.color = color
        self.outline = outline
        self.canvas = canvas
        
    def move(self, posX=0, posY=0):
        self.dpos = (self.dpos[0] + posX*pixelgap, self.dpos[1] - posY*pixelgap)
        draw_objects(self.canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY, obj_shapes)
        
def create_rect(canvas, color, outline, width, height, origin_x, origin_y, obj_shapes):
    # Calculate the coordinates of the square
    x1 = origin_x - width * pixelgap
    y1 = origin_y - height * pixelgap
    x2 = origin_x + width * pixelgap
    y2 = origin_y + height * pixelgap
    
    # Draw the square and add it to the obj_shapes list
    newRect = Shapes(canvas=canvas, name="RectA", color=color, outline=outline, coords=[[x1, y1], [x1, y2], [x2, y2], [x2, y1]])
    obj_shapes.append(newRect)