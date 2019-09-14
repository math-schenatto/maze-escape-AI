import random
from walls import walls
from movement import move_value
from collections import Counter

class Specimen:

    def random_cromossomo(self):
        directions = ['00', '01', '10', '11']
        genetic_code=''.join(random.choice(directions) for i in range(23))
        return genetic_code

    def __init__(self, genetic_code = None):
        self.genetic_code = genetic_code or self.random_cromossomo()
        self.current_position = 91 # Default start location
        self.route = self.get_route()
        self.fitness = self.fitness_function()

    def create_specimen(self, gene):
        self.genetic_code = gene

        # if random.uniform(0,1<= GeneticAlgorithm.mutation):
        #     random_pos = random.randrange(0,23,1)
        #     self.genetic_code[random_pos] = random.choice(['0','1'])


        #gera aptidão


    def get_fitness(self):
        return self.fitness

    def get_genetic_code(self):
        return self.genetic_code

    def fitness_function(self):
        fitness = self.score_route()
        fitness_duplicates = self.score_duplicates()
        total_fitness = fitness + fitness_duplicates
        return total_fitness

    def get_route(self):
        current_position = self.current_position
        start = 0
        end = 2
        route = []
        for i in range(23):
            direction = self.genetic_code[start:end]
            next_position = current_position + move_value[direction]
            route.append(next_position)
            start += 2
            end += 2
            current_position = next_position
        return route

    # +50 para cada vez que passa por um lugar que já passou
    def score_duplicates(self):
        counter = Counter(self.route)
        fitness = 0
        for position in counter:
            if counter[position] > 1:
                fitness += (20 * counter[position])
        return fitness

    def score_route(self):
        # +100 para cada vez que sai do mapa
        # +25 para cada parede que atravessa
        fitness = 0
        for index, position in enumerate(self.route):
            if index == len(self.route) - 1:
                break
            next_position = self.route[index+1]
            if next_position < 0 or next_position > 100:
                fitness += 100
            elif position % 10 == 0 and next_position % 10 == 1:
                fitness += 100
            elif position % 10 == 1 and next_position % 10 == 0:
                fitness += 100
            elif walls.get(position) and next_position in walls.get(position):
                fitness += 25
            else:
                fitness += 1
        return fitness
