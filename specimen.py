import random
from walls import walls
from movement import move_value

class Specimen:
    def random_cromossomo():
        directions = ['00', '01', '10', '11']
        genetic_code=''.join(random.choice(directions) for i in range(23))
        return genetic_code

    def __init__(self):
        self.genetic_code = Specimen.random_cromossomo()
        self.current_position = 91 # Default start location
        self.fitness = 0
        self.route = []
        self.get_route()

    def fitness_function(self):
        self.score_route()
        self.score_duplicate()
        print(f"FITNESS : {self.fitness}")

    def get_route(self):
        start = 0
        end = 2
        for i in range(23):
            direction = self.genetic_code[start:end]
            next_position = self.current_position + move_value[direction]
            self.route.append(next_position)
            start += 2
            end += 2

    def score_duplicate(self):
        duplicates = set(self.route)
        if duplicates:
            print("Caminhos repetidos + 50")
            print(duplicates)
            self.fitness += (50 * len(duplicates))


    def score_route(self):
        print("----------")
        for index, position in enumerate(self.route):
            if index == len(self.route) - 1:
                return
            next_position = self.route[index+1]
            if next_position < 0 or next_position > 100:
                result = 'Fora do mapa + 100'
                self.fitness += 100
            elif position % 10 == 0 and next_position % 10 == 1:
                result = 'Fora do mapa + 100'
                self.fitness += 100
            elif position % 10 == 1 and next_position % 10 == 0:
                result = 'Fora do mapa + 100'
                self.fitness += 100
            elif walls.get(position) and next_position in walls.get(position):
                result = 'Parede + 25'
                self.fitness += 25
            else:
                result = 'OK + 1'
                self.fitness += 1
            print(f"{position} -> {next_position} : {result}")
