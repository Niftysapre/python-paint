import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.pen_color = 'black'
        self.pen_size = 5
        self.drawing = False
        self.eraser_mode = False
        self.start_x, self.start_y = None, None

        self.create_widgets()

    def create_widgets(self):
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        self.color_button = tk.Button(self.root, text="Select Color", command=self.choose_color)
        self.color_button.pack()

        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack()

        self.pen_size_slider = tk.Scale(self.root, from_=1, to=20, orient="horizontal", label="Pen Size", command=self.change_pen_size)
        self.pen_size_slider.pack()

    def start_draw(self, event):
        self.drawing = True
        self.start_x, self.start_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)

    def draw(self, event):
        if self.drawing:
            x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            if self.eraser_mode:
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill='white', width=self.pen_size)
            else:
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill=self.pen_color, width=self.pen_size)
            self.start_x, self.start_y = x, y

    def stop_draw(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color[0]:
            self.pen_color = color[1]

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode

    def change_pen_size(self, value):
        self.pen_size = int(value)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Paint App")
    app = PaintApp(root)
    root.mainloop()
