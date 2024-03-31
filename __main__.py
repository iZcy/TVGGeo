# IMPORT packages
# import random
from globals import variables
from systems.settings import *

def main():
    # Create a window
    launch_window()
    draw_objects()

    # Run the Tkinter event loop
    variables.root.mainloop()

if __name__ == "__main__":
    main()
