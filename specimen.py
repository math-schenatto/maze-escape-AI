from genetic import Genetic
import random
from walls import walls
from movement import move_value

class Specimen:

    def __init__(self):
        self.genetic_code = self.random_cromossomo()
        self.current_position = 91 # Default start location
        self.route = self.get_route()
        self.fitness = self.fitness_function()


    def random_cromossomo(self):
        directions = ['00', '01', '10', '11']
        genetic_code=''.join(random.choice(directions) for i in range(23))

        #gerar aptidao
        return genetic_code

    def create_specimen(self, gene):
        self.genetic_code = gene

        if random.uniform(0,1<= Genetic.mutation):
            random_pos = random.randrange(0,23,1)
            self.genetic_code[random_pos] = random.choice(['0','1'])


        #gera aptidão


    def get_fitness(self):
        return self.fitness

    def get_genetic_code(self):
        return self.genetic_code

    def fitness_function(self):
        fitness = self.score_route()
        print('meu fitness', fitness)
        fitness_duplicate = self.score_duplicate()
        print(fitness)
        total_fitness = fitness+fitness_duplicate
        print(f"FITNESS : {total_fitness}")
        return total_fitness

    def get_route(self):
        start = 0
        end = 2
        route = []
        for i in range(23):
            direction = self.genetic_code[start:end]
            next_position = self.current_position + move_value[direction]
            route.append(next_position)
            start += 2
            end += 2
        return route

    def score_duplicate(self):
        duplicates = set(self.route)
        fitness = 0
        if duplicates:
            print("Caminhos repetidos + 50")
            print(duplicates)
            fitness += (50 * len(duplicates))
        return fitness


    def score_route(self):
        print("----------")
        fitness = 0
        for index, position in enumerate(self.route):
            if index == len(self.route) - 1:
                break
            next_position = self.route[index+1]
            if next_position < 0 or next_position > 100:
                result = 'Fora do mapa + 100'
                fitness += 100
            elif position % 10 == 0 and next_position % 10 == 1:
                result = 'Fora do mapa + 100'
                fitness += 100
            elif position % 10 == 1 and next_position % 10 == 0:
                result = 'Fora do mapa + 100'
                fitness += 100
            elif walls.get(position) and next_position in walls.get(position):
                result = 'Parede + 25'
                fitness += 25
            else:
                result = 'OK + 1'
                fitness += 1
            #print(f"{position} -> {next_position} : {result}")
            print(fitness)
        return fitness