from movement import maze_value
from specimen import Specimen
from maze_env import  Maze

class Controller:
    def __init__(self):
        self.env = Maze(self)
        self.env.mainloop()

    def move_view_truck(self, action):
        self.env.render()
        self.env.step(action)

    def main_show_maze(self, pop, cross, mut):
        self.specimen = Specimen()
        self.env.reset()
        self.specimen.fitness_function()
        self.env.after(100, self.show_path_on_maze())

    def show_path_on_maze(self):
        specimen = self.specimen
        start = 0
        end = 2
        for i in range(23):
            direction = specimen.genetic_code[start:end]
            start += 2
            end += 2
            action = maze_value[direction]
            self.move_view_truck(action)

if __name__ == "__main__":
    Controller()
