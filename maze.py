from typing import List, Optional
from cell import Cell
from window import Window
import time
import random

class Maze:
    def __init__(
            self,
            x: int,
            y: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: float,
            cell_size_y: float,
            win: Optional[Window] = None,
            seed = None
        ) -> None:
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = []
        self._moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if seed:
            random.seed(seed)
        self._create_cells()
        self._d_break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        
        for m1, m2 in self._moves:
            new_row, new_col = i + m1, j + m2
            if (new_row < 0 or new_row >= self._num_rows or new_col < 0 or new_col >= self._num_cols or
                self._cells[new_row][new_col].visited):
                continue

            can_move = False
            if (new_row == i - 1 and new_col == j and 
                not self._cells[i][j].has_left_wall and
                not self._cells[new_row][new_col].has_right_wall):
                can_move = True
            elif (new_row == i and new_col == j + 1 and 
                  not self._cells[i][j].has_bottom_wall and
                  not self._cells[new_row][new_col].has_top_wall):
                can_move = True
            elif (new_row == i + 1 and new_col == j and
                  not self._cells[i][j].has_right_wall and
                  not self._cells[new_row][new_col].has_left_wall):
                can_move = True
            elif (new_row == i and new_col == j - 1 and
                  not self._cells[i][j].has_top_wall and
                  not self._cells[new_row][new_col].has_bottom_wall):
                can_move = True

            if not can_move:
                continue

            self._cells[i][j].draw_move(self._cells[new_row][new_col])
            if self.solve(new_row, new_col):
                return True
            self._cells[i][j].draw_move(self._cells[new_row][new_col], True)

        return False

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            paths = []
            for m1, m2 in self._moves:
                new_row, new_col = i + m1, j + m2
                if 0 <= new_row < self._num_rows and 0 <= new_col < self._num_cols and not self._cells[new_row][new_col].visited:
                    paths.append((new_row, new_col))

            if not paths:
                self._draw_cell(i, j)
                return

            new_row, new_col = random.choice(paths)

            if new_row == i - 1 and new_col == j:
                self._cells[i][j].has_left_wall = False
                self._cells[new_row][new_col].has_right_wall = False
            elif new_row == i and new_col == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_row][new_col].has_top_wall = False
            elif new_row == i + 1 and new_col == j:
                self._cells[i][j].has_right_wall = False
                self._cells[new_row][new_col].has_left_wall = False
            elif new_row == i and new_col == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[new_row][new_col].has_bottom_wall = False
            self._break_walls_r(new_row, new_col)

    def _d_break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit = self._cells[-1][-1]
        exit.has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _create_cells(self):
        for i in range(self._num_rows):
            self._cells.append([])
            for _ in range(self._num_cols):
                self._cells[i].append(Cell(self._win))

        if not self._win:
            return

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell: Cell = self._cells[i][j]
        x1 = self._x + (i * self._cell_size_x)
        y1 = self._y + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)
