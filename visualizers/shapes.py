from globals import variables
from visualizers.drawers import *
from systems.events import *
import numpy as np
import math

class Shapes:
    def __init__(self, name, color="black", outline="black", coords=[[0,0]], cpos = [0,0], launcher=None):
        self.name = name
        self.coords = coords
        self.cpos = [cpos[0]+variables.window_width/2, cpos[1]+variables.window_height/2]
        self.color = color
        self.outline = outline
        self.launcher = launcher
        
    def onSelect(self, selected=False):
        if selected:
            self.outline="black"
        else:
            self.outline=self.color
        
        self.refresh()
    
    def move(self, posX=None, posY=None, static=False):
        dposX, dposY = 0, 0
        if posX != None:
            dposX = posX
            if not static:
                variables.trans_x=posX
        if posY != None:
            dposY = posY
            if not static:
                variables.trans_y=posY
        
        translateMtx = getTranslateMatrix(transX=dposX, transY=dposY)
        self.transform(transMatrix=translateMtx, static=static)
    
    def scale(self, scaleX=None, scaleY=None, static=False):
        dScaleX, dScaleY = 1, 1
        if scaleX != None:
            dScaleX = scaleX
            if not static:
                variables.scale_x=scaleX
        if scaleY != None:
            dScaleY = scaleY
            if not static:
                variables.scale_y=scaleY
        
        scaleTransMtx = getScaleMatrix(scaleX=dScaleX, scaleY=dScaleY)
        self.transform(transMatrix=scaleTransMtx, static=static)
        
    def reflect(self, axis="x", static=False):
        refTransMtx = []
        if axis == "x":
            refTransMtx = getScaleMatrix(scaleX=-1)
        elif axis == "y":
            refTransMtx = getScaleMatrix(scaleY=-1)
        self.transform(transMatrix=refTransMtx, static=static)
    
    def rotate(self, deg=0, static=False):
        if not static:
            variables.rot = deg
        rotDegMtx = getRotMatrix(deg)
        self.transform(transMatrix=rotDegMtx, static=static)
        
    def transform(self, transMatrix, static=False):
        newPos = transformation(coords=self.coords, trans=transMatrix)
        self.coords = newPos
        
        if not static:
            self.cpos = (transformation(coords=[self.cpos], trans=transMatrix))[0]
        
        self.refresh()
    
    def refresh(self):
        self.launcher()
        
    def destroy(self):
        variables.obj_shapes = [obj for obj in variables.obj_shapes if obj.name != self.name]
        variables.selected_object = None
        self.refresh()
        del self

def create_rect(width, height, name, color, outline, launcher):
    # Calculate the coordinates of the square
    x1 = variables.origin_x - width/2 * variables.pixelgap
    y1 = variables.origin_y - height/2 * variables.pixelgap
    x2 = variables.origin_x + width/2 * variables.pixelgap
    y2 = variables.origin_y + height/2 * variables.pixelgap
    
    # Draw the square and add it to the obj_shapes list
    newRect = Shapes(name=name, color=color, outline=outline, coords=[[x1, y1], [x1, y2], [x2, y2], [x2, y1]], launcher=launcher)
    
    variables.obj_shapes.append(newRect)

def getNormPos(coords):
    matrixCoor = []
    for coor in coords:
        xPos = (coor[0] + variables.x_gap*variables.pixelgap - variables.window_width/2)/variables.pixelgap
        yPos = -(coor[1] - variables.y_gap*variables.pixelgap - variables.window_height/2)/variables.pixelgap
        matrixCoor.append([xPos, yPos])
    return matrixCoor

def getBackPos(coords):
    matrixPos = []
    for coor in coords:
        xPos = (coor[0]*variables.pixelgap + variables.window_width/2 - variables.x_gap*variables.pixelgap)
        yPos = (-coor[1]*variables.pixelgap + variables.window_height/2 + variables.y_gap*variables.pixelgap)
        matrixPos.append([xPos, yPos])
    return matrixPos

def transformation(coords, trans):
    # Normalize Coordinate
    normPos = getNormPos(coords=coords)
    
    # Expand to 3D
    for norm in normPos:
        norm.append(1)
    # Change to Matrix
    normMtx = np.array(normPos)
    
    # Get Transformation Matrix
    matrixOrdTrans = trans
    matrixTrans = np.array(matrixOrdTrans)
    
    # Execute Transformation
    matrixRes = np.dot(normMtx, matrixTrans)
    
    # Back to Arrays
    matrixBack = matrixRes.tolist()
    
    # Cut Last Row
    matrixBack = [row[:-1] for row in matrixBack]
    
    # Convert to Ordinary Coordinate
    matrixBack = getBackPos(matrixBack)
    
    return matrixBack

def getRotMatrix(deg):
    transMatrix=[[math.cos(math.radians(deg)),-math.sin(math.radians(deg)),0],[math.sin(math.radians(deg)),math.cos(math.radians(deg)),0],[0,0,1]]
    return transMatrix

def getScaleMatrix(scaleX=1, scaleY=1):
    transMatrix=[[scaleX, 0, 0], [0, scaleY, 0], [0, 0, 1]]
    return transMatrix

def getTranslateMatrix(transX=0, transY=0):
    transMatrix=[[1, 0, 0], [0, 1, 0], [transX*variables.zoomX, transY*variables.zoomY, 1]]
    return transMatrix