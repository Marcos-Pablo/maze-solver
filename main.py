from drawable_elements import Line, Point
from window import Window

def main():
    point1 = Point(100, 100)
    point2 = Point(500, 100)
    line = Line(point1, point2)
    win = Window(800, 600)
    win.draw_line(line)
    win.wait_for_close()

main()
