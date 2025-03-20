from tkinter import Canvas
from window import Window

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2
        )

class Cell:
    def __init__(self,
                 has_left_wall: bool,
                 has_right_wall: bool,
                 has_top_wall: bool,
                 has_bottom_wall: bool,
                 x1: int, x2: int, y1: int, y2: int, win: Window) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.has_left_wall:
            p1, p2 = Point(self.x1, self.y1), Point(self.x1, self.y2)
            line = Line(p1, p2)
            self.win.draw_line(line)

        if self.has_right_wall:
            p1, p2 = Point(self.x2, self.y1), Point(self.x2, self.y2)
            line = Line(p1, p2)
            self.win.draw_line(line)

        if self.has_top_wall:
            p1, p2 = Point(self.x1, self.y1), Point(self.x2, self.y1)
            line = Line(p1, p2)
            self.win.draw_line(line)

        if self.has_bottom_wall:
            p1, p2 = Point(self.x1, self.y2), Point(self.x2, self.y2)
            line = Line(p1, p2)
            self.win.draw_line(line)
