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
    
    def getNormCpos(self):
        nCPosX = (variables.selected_object.cpos[0] - variables.window_width/2)/variables.pixelgap
        nCPosY = (variables.window_height/2 - variables.selected_object.cpos[1])/variables.pixelgap
        return [nCPosX, nCPosY]
    
    def setRealCenter(self):
        num_vertices = len(self.coords)
        normVertex = getNormPos(self.coords)
        total_x = sum(vertex[0] for vertex in normVertex)
        total_y = sum(vertex[1] for vertex in normVertex)
        center_x = total_x / num_vertices
        center_y = total_y / num_vertices
        oriCenter = getBackPos([[center_x, center_y]])[0]
        self.cpos = oriCenter
    
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
        newPos = transformation(coords=self.coords, trans=transMatrix, ptr=self)
        self.coords = newPos
        
        if not static:
            self.cpos = (transformation(coords=[self.cpos], trans=transMatrix, ptr=self))[0]
        
        self.refresh()
    
    def refresh(self):
        self.launcher()
        
    def destroy(self):
        variables.obj_shapes = [obj for obj in variables.obj_shapes if obj.name != self.name]
        variables.selected_object = None
        self.refresh()
        del self

def create_triangle(base, height, name, color, outline, launcher):
    # Calculate the coordinates of the triangle
    x1 = variables.origin_x - base/2 * variables.pixelgap
    y1 = variables.origin_y + height/2 * variables.pixelgap
    x2 = variables.origin_x
    y2 = variables.origin_y - height/2 * variables.pixelgap
    x3 = variables.origin_x + base/2 * variables.pixelgap
    y3 = variables.origin_y + height/2 * variables.pixelgap
    
    # Draw the triangle and add it to the obj_shapes list
    newTriangle = Shapes(name=name, color=color, outline=outline, coords=[[x1, y1], [x2, y2], [x3, y3]], launcher=launcher)
    translate = getTranslateMatrix(transX=variables.customCenter[0], transY=variables.customCenter[1])
    newTriangle.transform(transMatrix=translate)
    
    variables.obj_shapes.append(newTriangle)

def create_rect(width, height, name, color, outline, launcher):
    # Calculate the coordinates of the square
    x1 = variables.origin_x - width/2 * variables.pixelgap
    y1 = variables.origin_y - height/2 * variables.pixelgap
    x2 = variables.origin_x + width/2 * variables.pixelgap
    y2 = variables.origin_y + height/2 * variables.pixelgap
    
    # Draw the square and add it to the obj_shapes list
    newRect = Shapes(name=name, color=color, outline=outline, coords=[[x1, y1], [x1, y2], [x2, y2], [x2, y1]], launcher=launcher)
    translate = getTranslateMatrix(transX=variables.customCenter[0], transY=variables.customCenter[1])
    newRect.transform(transMatrix=translate)
    
    variables.obj_shapes.append(newRect)

def create_pentagon(side_length, name, color, outline, launcher):
    # Calculate the coordinates of the pentagon
    angle = 360 / 5  # Angle between each vertex of the pentagon
    pentagon_coords = []
    for i in range(5):
        x = (variables.origin_x / variables.pixelgap + side_length * math.cos(math.radians(i * angle))) * variables.pixelgap
        y = (variables.origin_y / variables.pixelgap + side_length * math.sin(math.radians(i * angle))) * variables.pixelgap
        pentagon_coords.append([x, y])
    
    # Draw the pentagon and add it to the obj_shapes list
    newPentagon = Shapes(name=name, color=color, outline=outline, coords=pentagon_coords, launcher=launcher)
    translate = np.array(getTranslateMatrix(transX=variables.customCenter[0], transY=variables.customCenter[1]))
    rot = np.array(getRotMatrix(deg=-18))
    transform = (np.dot(rot, translate)).tolist()
    
    newPentagon.transform(transMatrix=transform)
    
    variables.obj_shapes.append(newPentagon)

def create_hexagon(side_length, name, color, outline, launcher):
    # Calculate the coordinates of the hexagon
    angle = 360 / 6  # Angle between each vertex of the hexagon
    hexagon_coords = []
    for i in range(6):
        x = (variables.origin_x / variables.pixelgap + side_length * math.cos(math.radians(i * angle))) * variables.pixelgap
        y = (variables.origin_y / variables.pixelgap + side_length * math.sin(math.radians(i * angle))) * variables.pixelgap
        hexagon_coords.append([x, y])
    
    # Draw the hexagon and add it to the obj_shapes list
    newHexagon = Shapes(name=name, color=color, outline=outline, coords=hexagon_coords, launcher=launcher)
    translate = getTranslateMatrix(transX=variables.customCenter[0], transY=variables.customCenter[1])
    newHexagon.transform(transMatrix=translate)
    
    variables.obj_shapes.append(newHexagon)

def create_circle(radius, name, color, outline, launcher):
    # Calculate the coordinates of the circle
    vertices = []
    num_vertices = 360
    angle_step = 360 / num_vertices 
    for i in range(num_vertices):
        angle = math.radians(i * angle_step)
        x = (variables.origin_x/variables.pixelgap + radius * math.cos(angle))*variables.pixelgap
        y = (variables.origin_y/variables.pixelgap + radius * math.sin(angle))*variables.pixelgap
        vertices.append([x, y])
    
    # Draw the circle and add it to the obj_shapes list
    newCircle = Shapes(name=name, color=color, outline=outline, coords=vertices, launcher=launcher)
    # translate = getTranslateMatrix(transX=variables.customCenter[0], transY=variables.customCenter[1])
    # newCircle.transform(transMatrix=translate)
    
    variables.obj_shapes.append(newCircle)

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

def transformation(coords, trans, ptr=None):
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
    
    # Special Condition: on self center
    toCenterMtx, toOriginMtx = [], []
    if variables.selfCenter:
        nCPosX, nCPosY = ptr.getNormCpos()
        toCenterMtx = getTranslateMatrix(transX=-nCPosX, transY=-nCPosY)
        toOriginMtx = getTranslateMatrix(transX= nCPosX, transY= nCPosY)
        
        matrixTrans = np.dot(toCenterMtx, matrixTrans)
        matrixTrans = np.dot(matrixTrans, toOriginMtx)
    
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