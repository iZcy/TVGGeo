# IMPORT packages
# import random
from globals.variables import *
from systems.settings import *

def main():
    # Create a window
    root, canvas = launch_window(window_width, window_height, origin_x, origin_y, obj_shapes)
    draw_objects(canvas, window_width, window_height, origin_x, origin_y, x_gap, y_gap, zoomX, zoomY, obj_shapes)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
