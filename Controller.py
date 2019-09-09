from maze_env import  Maze
from main_empilhadeira import Labyrinth

class Controller:
    def __init__(self):
        self.model = Labyrinth(self)
        self.env = Maze(self)


    def move_view_truck(self, action):
        self.env.render()
        self.env.step(action)

    def start_code(self, pop, cross, mut):
        self.env.after(100)
        #self.env.after(100, self.model.show_track())
        self.env.mainloop()

    #def main_show_maze(self):
    #    self.env.mainloop()

    def main_show_maze(self, pop, cross, mut):
        print(pop, cross, mut)
        self.env.reset()
        self.env.after(100, self.model.show_track())



if __name__ == "__main__":
    #specimen = Specimen(genetic_code=randomCromossomo())
    controller = Controller()
    controller.start_code(1,2,3)

