from globals import variables
from visualizers.drawers import *
from systems.events import *
from systems.dash import *

class Shapes:
    def __init__(self, name, color="black", outline="black", coords=[[0,0]], dpos = [0,0]):
        self.name = name
        self.coords = coords
        self.dpos = dpos
        self.color = color
        self.outline = outline
        
    def move(self, posX=None, posY=None):
        dPosX, dPosY = 0, 0
        if posX != None:
            dPosX = posX
            variables.trans_x=posX
        if posY != None:
            dPosY = posY
            variables.trans_y=posY
        
        self.dpos = [self.dpos[0] + dPosX, self.dpos[1] + dPosY]
        self.updatePos(posX=dPosX, posY=dPosY)
    
    def scale(self, scaleX=1, scaleY=1):
        variables.scale_x=scaleX
        variables.scale_y=scaleY
        
        self.dscale = [self.dscale[0] * scaleX, self.dscale[1] * scaleY]
        self.updatePos(self, scaleX=scaleX, scaleY=scaleY)
        
    def updatePos(self, posX=0, posY=0, scaleX=1, scaleY=1, rot=0):
        for coord in self.coords:
            coord[0] += posX * variables.pixelgap
            coord[0] *= scaleX
            coord[1] -= posY * variables.pixelgap
            coord[1] *= scaleY
            
        launch_dash(on_button_click)
        draw_objects()
        
def create_rect(width, height, name, color, outline):
    # Calculate the coordinates of the square
    x1 = variables.origin_x - width * variables.pixelgap
    y1 = variables.origin_y - height * variables.pixelgap
    x2 = variables.origin_x + width * variables.pixelgap
    y2 = variables.origin_y + height * variables.pixelgap
    
    # Draw the square and add it to the obj_shapes list
    newRect = Shapes(name=name, color=color, outline=outline, coords=[[x1, y1], [x1, y2], [x2, y2], [x2, y1]])
    variables.obj_shapes.append(newRect)