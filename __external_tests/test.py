import tkinter as tk

def track_cursor(event):
    x, y = event.x, event.y
    print("Cursor position: x={}, y={}".format(x, y))

def main():
    root = tk.Tk()
    root.geometry("400x400")

    frame = tk.Frame(root, width=200, height=200, bg="lightgray")
    frame.pack(padx=50, pady=50)

    frame.bind("<Motion>", track_cursor)

    root.mainloop()

if __name__ == "__main__":
    main()
