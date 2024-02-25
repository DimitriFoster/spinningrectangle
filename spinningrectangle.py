import tkinter as tk

class SpinningCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create a rectangle to spin
        self.rectangle = self.create_rectangle(0, 0, 100, 100, fill="red")

        # Start the spinning animation
        self.after(10, self.spin)

    def spin(self):
        # Rotate the rectangle by 10 degrees
        self.itemconfig(self.rectangle, angle=10)

        # Schedule the next animation frame
        self.after(10, self.spin)

# Create the main window
root = tk.Tk()

# Create a spinning canvas
canvas = SpinningCanvas(root)

# Pack the canvas
canvas.pack()

# Start the mainloop
root.mainloop()
