import tkinter as tk

def center_window(window, window_width, window_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y positions for the window to be centered
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window's position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def main():
    # Create the main window
    root = tk.Tk()

    # Set the window size (width x height)
    window_width = 500
    window_height = 500

    # Center the window
    center_window(root, window_width, window_height)

    # Set the window title
    root.title("Prompt Window with Defined Size")
    
    # Set the window icon
    root.iconbitmap("icons.ico")

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
