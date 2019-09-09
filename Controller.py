from maze_env import  Maze
from labirinth import Labyrinth

class Controller:
    def __init__(self):
        self.labirinth = Labyrinth(self)
        self.env = Maze(self)

    def move_view_truck(self, action):
        self.env.render()
        self.env.step(action)

    def start_code(self, pop=0, cross=0, mut=0):
        self.env.after(100)
        self.env.mainloop()

    def main_show_maze(self, pop, cross, mut):
        self.env.reset()
        self.env.after(100, self.labirinth.show_path_on_maze())

if __name__ == "__main__":
    Controller().start_code()
