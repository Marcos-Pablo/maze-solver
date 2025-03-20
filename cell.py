from graphics import Line, Point
from window import Window

class Cell:
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw_move(self, to_cell, undo=False):
        if not self._win or self._x1 == None or self._y1 == None or self._x2 == None or self._y2 == None:
            return

        fill_color = "gray" if undo else "red"
        p1 = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        p2 = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        print("p1 -> ", p1.x, p1.y)
        print("p2 -> ", p2.x, p2.y)
        line = Line(p1, p2)
        self._win.draw_line(line, fill_color)

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            p1, p2 = Point(self._x1, self._y1), Point(self._x1, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_right_wall:
            p1, p2 = Point(self._x2, self._y1), Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_top_wall:
            p1, p2 = Point(self._x1, self._y1), Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_bottom_wall:
            p1, p2 = Point(self._x1, self._y2), Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)
