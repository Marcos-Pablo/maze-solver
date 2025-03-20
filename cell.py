from graphics import Line, Point
from window import Window

class Cell:
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

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
