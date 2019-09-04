import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # pixels
MAZE_H = 10  # grid height
MAZE_W = 10  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('Algoritmo Genético')
        self.geometry('{0}x{1}'.format(MAZE_H * 80, MAZE_H * 40))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='blue',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        self.canvas_2 = tk.Canvas(self, bg='orange',
                           height=50 * UNIT,
                           width=50 * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_W * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        #Linhas externas
        self.line1 = self.canvas.create_line(3,396,396,396, width=5)
        self.line2 = self.canvas.create_line(3, 3, 550, 3, width=5)
        self.line3 = self.canvas.create_line(3, 3, 3, 360, width=5)
        self.line3 = self.canvas.create_line(398, 40, 398, 398, width=5)
        self.line4 = self.canvas.create_line(20, 300, 40, 340, width=5)

        # create origin
        origin = np.array([20, 380])


        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 10, origin[1] - 10,
            origin[0] + 10, origin[1] + 10,
            fill='red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.30)
        self.canvas.delete(self.rect)
        origin = np.array([20, 380])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 10, origin[1] - 10,
            origin[0] + 10, origin[1] + 10,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 2:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 3:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 4:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent


    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            env.step(a)


if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()