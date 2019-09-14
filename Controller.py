from movement import maze_value
from specimen import Specimen
from maze_env import  Maze

from genetic_algorithm import GeneticAlgorithm
from population import Population

class Controller:
    def __init__(self):
        self.env = Maze(self)
        self.env.mainloop()

    def move_view_truck(self, action):
        self.env.render()
        self.env.step(action)

    def main_show_maze(self, pop, cross, mut, max_generation):
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

    algorithm = GeneticAlgorithm('1', 0.6, 0.3, True)
    population_size = 200
    generations_limit = 200
    population = Population(population_size)
    population.create_random_population()
    solution_found = False
    generation = 0
    population.order_population()
    print(f"INICIAL - fitness: {population.specimens[0].fitness}")
    while generation < generations_limit:
        generation += 1
        population = algorithm.create_new_generation(population)
        print(f"Geração {generation} | Melhor fitness {population.specimens[0].fitness}")

    Controller()
