from window import Window
from graphics import Line, Point
from cell import Cell

def main():
    p1, p2 = Point(100, 100), Point(500, 500)
    line = Line(p1, p2)
    win = Window(800, 600)
    win.draw_line(line)
    cell = Cell(win)
    cell.draw(100, 100, 500, 500)
    win.wait_for_close()

main()
