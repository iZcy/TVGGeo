import tkinter as tk
# import random

canvas = None
frame = None

# Set the window size (width x height)
window_width = 600
window_height = 600

# Set the origin coordinates
origin_x = window_width // 2
origin_y = window_height // 2

# Gap Config
pixelgap = 30
x_gap = 0
y_gap = 0

# Scale Config
zoomX = 1
zoomY = 1

# Timer
# time = 0.1

#Object
obj_shapes = []
selected_object = None

def launchDash(event):
    global selected_object, frame, canvas, x_gap, y_gap, zoomX, zoomY, window_width, window_height, origin_x, origin_y, obj_shapes
    
    # Destroy or remove all widgets contained within the frame
    for widget in frame.winfo_children():
        widget.destroy()
        
    check_points(event)
    
    if selected_object == None:
        # Create a Translate X
        entryTX = tk.Entry(frame, width=10)
        entryTX.grid(row=0, column=0, padx=5)
        entryTX.insert(0, 0)
        
        buttonTX = tk.Button(frame, text="Swipe X", command=lambda: on_button_click(canvas, entry=entryTX, type="x"))
        buttonTX.grid(row=0, column=1, padx=(0, 10))
        
        # Create a Translate Y
        entryTY = tk.Entry(frame, width=10)
        entryTY.grid(row=0, column=2, padx=5)
        entryTY.insert(0, 0)
        
        buttonTY = tk.Button(frame, text="Swipe Y", command=lambda: on_button_click(canvas, entry=entryTY, type="y"))
        buttonTY.grid(row=0, column=3, padx=(0, 10))
        
        # Create a Scale X
        entrySx = tk.Entry(frame, width=10)
        entrySx.grid(row=1, column=0, padx=5)
        entrySx.insert(0, 1)
        
        buttonSx = tk.Button(frame, text="Zoom X", command=lambda: on_button_click(canvas, entry=entrySx, type="sx"))
        buttonSx.grid(row=1, column=1, padx=(0, 10))
        
        # Create a Scale Y
        entrySy = tk.Entry(frame, width=10)
        entrySy.grid(row=1, column=2, padx=5)
        entrySy.insert(0, 1)
        
        buttonSy = tk.Button(frame, text="Zoom Y", command=lambda: on_button_click(canvas, entry=entrySy, type="sy"))
        buttonSy.grid(row=1, column=3, padx=(0, 10))
    else:
        entryTX = tk.Entry(frame, width=10)
        entryTX.grid(row=0, column=0, padx=5)
        entryTX.insert(0, 0)
        
        buttonTX = tk.Button(frame, text="Swipe X", command=lambda: selected_object.move(posX=float(entryTX.get())))
        buttonTX.grid(row=0, column=1, padx=(0, 10))
        
        # Create a Translate Y
        entryTY = tk.Entry(frame, width=10)
        entryTY.grid(row=0, column=2, padx=5)
        entryTY.insert(0, 0)
        
        buttonTY = tk.Button(frame, text="Swipe Y", command=lambda: selected_object.move(posY=float(entryTY.get())))
        buttonTY.grid(row=0, column=3, padx=(0, 10))
        
        # Create a Scale X
        entrySx = tk.Entry(frame, width=10)
        entrySx.grid(row=1, column=0, padx=5)
        entrySx.insert(0, 1)
        
        buttonSx = tk.Button(frame, text="Zoom X", command=lambda: None)
        buttonSx.grid(row=1, column=1, padx=(0, 10))
        
        # Create a Scale Y
        entrySy = tk.Entry(frame, width=10)
        entrySy.grid(row=1, column=2, padx=5)
        entrySy.insert(0, 1)
        
        buttonSy = tk.Button(frame, text="Zoom Y", command=lambda: None)
        buttonSy.grid(row=1, column=3, padx=(0, 10))

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
    global selected_object
    selected_object = None
    for obj in obj_shapes:
        cond = point_inside_polygon(event.x, event.y, obj.coords)
        if (cond):
            selected_object = obj
            return

class Shapes:
    def __init__(self, name, canvas, color="black", outline="black", coords=[[0,0]], dpos = [0,0]):
        self.name = name
        self.coords = coords
        self.dpos = dpos
        self.color = color
        self.outline = outline
        self.canvas = canvas
        
    def move(self, posX=0, posY=0):
        print(posX, posY)
        self.dpos = (self.dpos[0] + posX*pixelgap, self.dpos[1] + posY*pixelgap)
        print(self.dpos)
        loop_draw(self.canvas)

def center_window(window, window_width, window_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y positions for the window to be centered
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window's position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def draw_cartesian(canvas, width, height, origin_x, origin_y, color):
    # Draw x-axis
    canvas.create_line(0, origin_y, width, origin_y, fill=color, width=2)

    # Draw y-axis
    canvas.create_line(origin_x, 0, origin_x, height, fill=color, width=2)

    # Draw x-axis tick marks and labels
    for i in range(-window_width, window_width):
        x = origin_x + i * (width*zoomX/20)
        canvas.create_line(x, origin_y-5, x, origin_y+5, fill=color, width=2)
        canvas.create_text(x, origin_y+10, text=str(i), anchor="n")

    # Draw y-axis tick marks and labels
    for i in range(-window_height, window_height):
        y = origin_y - i * (height*zoomY/20)
        canvas.create_line(origin_x-5, y, origin_x+5, y, fill=color, width=2)
        canvas.create_text(origin_x-15, y, text=str(i), anchor="e")
    

def draw_objects(canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY):
    global obj_shapes, pixelgap
    
    if len(obj_shapes) != 0:
        for obj in obj_shapes:
            deltapos = [x + y for x, y in zip(obj.dpos, [-x_gap*pixelgap, y_gap*pixelgap])]
            result = [[x + y for x, y in zip(sublist, deltapos)] for sublist in obj.coords]
            vert_list = sum(result, [])
            canvas.create_polygon(vert_list, fill=obj.color, outline=obj.outline, width=2)
    
    # Draw Cartesian coordinate system
    draw_cartesian(canvas, window_width, window_height, origin_x = (origin_x - x_gap*pixelgap)*zoomX, origin_y = (origin_y + y_gap*pixelgap)*zoomY, color="black")

def on_button_click(canvas, entry, type):
    global x_gap, y_gap, zoomX, zoomY, window_width, window_height, origin_x, origin_y, obj_shapes
    
    text = entry.get()

    resp = float(text)

    if (type == "x"):
        x_gap += float(text)
    elif (type == "y"):
        y_gap += float(text)
    elif (type == "sx" and resp != 0):
        zoomX *= float(text)
    elif (type == "sy" and resp != 0):
        zoomY *= float(text)
    
    loop_draw(canvas)
        
def loop_draw(canvas):
    canvas.delete("all")
    draw_objects(canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY)

def create_rect(canvas, color, outline, width, height):
    global obj_shapes
    
    # Calculate the coordinates of the square
    x1 = origin_x - width * pixelgap
    y1 = origin_y - height * pixelgap
    x2 = origin_x + width * pixelgap
    y2 = origin_y + height * pixelgap
    
    # Draw the square and add it to the obj_shapes list
    newRect = Shapes(canvas=canvas, name="RectA", color=color, outline=outline, coords=[[x1, y1], [x1, y2], [x2, y2], [x2, y1]])
    obj_shapes.append(newRect)

def main():
    global x_gap, y_gap, zoomX, zoomY, window_width, window_height, origin_x, origin_y, canvas, frame
    
    # Create the main window
    root = tk.Tk()
    
    # Disable resizing
    root.resizable(width=False, height=False)

    # Set the window title
    root.title("Geometry Transformation")
    
    # Set the window icon
    root.iconbitmap("icons.ico")


    # Center the window
    center_window(root, window_width, window_height)
    
    # Create a canvas
    canvas = tk.Canvas(root, width=window_width, height=window_height-100)
    canvas.pack()
    
    # Create a frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    
    launchDash(None)
    canvas.bind("<Button-1>", launchDash)

    create_rect(canvas, "red", "red", 1, 1)

    loop_draw(canvas)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
