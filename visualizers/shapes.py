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
    
    def getPos(self):
        matrixCoor = []
        for coor in self.coords:
            xPos = (coor[0] - variables.window_width/2)/variables.pixelgap+variables.x_gap
            yPos = -((coor[1] - variables.window_height/2)/variables.pixelgap+variables.y_gap)
            matrixCoor.append([xPos, yPos])
        return matrixCoor
    
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
    
    def scale(self, scaleX=None, scaleY=None):
        dScaleX, dScaleY = 1, 1
        if scaleX != None:
            dScaleX = scaleX
            variables.scale_x=scaleX
        if scaleY != None:
            dScaleY = scaleY
            variables.scale_y=scaleY
        
        self.updatePos(scaleX=dScaleX, scaleY=dScaleY)
        
    def reflect(self, axis="x"):
        if axis == "x":
            self.updatePos(scaleX=-1)
        elif axis == "y":
            self.updatePos(scaleY=-1)
        
    def updatePos(self, posX=0, posY=0, scaleX=1, scaleY=1, rot=0):
        for coord in self.coords:
            coord[0] += posX * variables.pixelgap * (variables.zoomX / abs(variables.zoomX))
            coord[1] -= posY * variables.pixelgap * (variables.zoomY / abs(variables.zoomY))
            
            coord[0] += variables.x_gap*variables.pixelgap
            coord[0] -= variables.window_width/2
            coord[0] *= scaleX
            coord[0] += variables.window_width/2
            coord[0] -= variables.x_gap*variables.pixelgap
            
            coord[1] -= variables.y_gap*variables.pixelgap
            coord[1] -= variables.window_height/2
            coord[1] *= scaleY
            coord[1] += variables.window_height/2
            coord[1] += variables.y_gap*variables.pixelgap
            
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