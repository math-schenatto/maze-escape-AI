from movement import maze_value
from specimen import Specimen

class Labyrinth:
    def __init__(self, controller):
        self.control = controller
        self.specimen = Specimen()

    def show_path_on_maze(self):
        specimen = self.specimen
        start = 0
        end = 2
        for i in range(23):
            direction = specimen.genetic_code[start:end]
            start += 2
            end += 2
            action = maze_value[direction]
            self.control.move_view_truck(action)
