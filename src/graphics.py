from tkinter import Tk, BOTH, Canvas
from .colors import WALL_COLOR

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        
        # Ensure the window closes properly
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        self.__root.destroy()
    
    def draw_line(self, line:Line, fill_color=WALL_COLOR):
        line.draw(self.__canvas, fill_color)

