from window import Window
from drawable_elements import Cell, Line, Point

def main():
    p1, p2 = Point(100, 100), Point(500, 500)
    line = Line(p1, p2)
    win = Window(800, 600)
    win.draw_line(line)
    cell = Cell(True, True, True, True, 100, 500, 100, 500, win)
    cell.draw()
    cell = Cell(False, True, True, True, 100, 200, 100, 200, win)
    cell.draw()
    win.wait_for_close()

main()
