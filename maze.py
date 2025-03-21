from typing import List, Optional
from cell import Cell
from window import Window
import time

class Maze:
    def __init__(
            self,
            x: int,
            y: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: float,
            cell_size_y: float,
            win: Optional[Window],
        ) -> None:
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = []
        self._create_cells()

    def _create_cells(self):
        if not self._win:
            return
        for i in range(self._num_rows):
            self._cells.append([])
            for _ in range(self._num_cols):
                self._cells[i].append(Cell(self._win))

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        cell: Cell = self._cells[i][j]
        x1 = self._x + (i * self._cell_size_x)
        y1 = self._y + (j * self._cell_size_y)

        x2 = self._x + ((i + 1) * self._cell_size_x)
        y2 = self._y + ((j + 1) * self._cell_size_y)
        cell.draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)
