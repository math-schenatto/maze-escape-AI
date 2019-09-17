import random
from walls import walls
from movement import move_value
from collections import Counter

class Specimen:

    def __init__(self, genetic_code = None):
        self.genetic_code = None
        self.current_position = 91 # Default start location
        self.route = None
        self.fitness = None


    def random_cromossomo(self):
        directions = ['00', '01', '10', '11']
        genetic_code=''.join(random.choice(directions) for i in range(26))

        self.genetic_code = genetic_code
        self.route = self.get_route()
        self.fitness = self.fitness_function()


    def create_specimen(self, gene, mut):
        self.genetic_code = gene

        if random.uniform(0,1)<= mut:
            random_pos = random.randrange(0,26,1)
            index = 0
            new_string = ''

            while index < len(self.genetic_code):
                if index == random_pos:
                    mutex = random.choice(['0', '1'])
                    new_string += mutex
                else:
                    new_string += self.genetic_code[index]
                index = index + 1

            self.genetic_code = new_string



        self.route = self.get_route()
        self.fitness = self.fitness_function()


    def get_fitness(self):
        return self.fitness

    def get_genetic_code(self):
        return self.genetic_code

    def fitness_function(self):
        fitness = self.score_route()
        fitness_duplicates = self.score_duplicates()
        #fitness_final_position = self.penalize_final_position()
        reward = self.reward_cookies()
        total_fitness = fitness + fitness_duplicates + reward
        return total_fitness

    def get_route(self):
        current_position = self.current_position
        start = 0
        end = 2
        route = []
        route.append(current_position)
        for i in range(26):
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
                fitness += (25 * counter[position])
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
                fitness += 50
            elif position % 10 == 0 and next_position % 10 == 1:
                fitness += 50
            elif position % 10 == 1 and next_position % 10 == 0:
                fitness += 50
            elif walls.get(position) and next_position in walls.get(position):
                fitness += 50
            else:
                fitness += 0
        return fitness

    def penalize_final_position(self):
        final_position = self.route[-1]
        penalty = 0
        # Penaliza mais quanto mais pra baixo termina
        if final_position > 20:
            penalty += 30
        if final_position > 40:
            penalty += 30
        if final_position > 70:
            penalty += 30
        # Penaliza mais quanto mais pra esquerda termina
        if final_position % 10 <= 3:
            penalty += 30
        if final_position % 10 <= 6:
            penalty += 30
        if final_position % 10 <= 8:
            penalty += 30
        if final_position < 10:
            penalty+=500
        if final_position > 10:
            penalty+=500
        if final_position == 10:
            penalty-=1000
        return penalty

    def reward_cookies(self):
        reward = 0
        if self.route[1] == 71:
            reward -= 100
        if self.route[7] == 44:
            reward -= 100
        if self.route[9] == 33:
            reward -= 100
        if self.route[12] == 21:
            reward -= 100
        if self.route[17] == 26:
            reward -= 100
        if self.route[-1] == 10:
            reward -= 100
        return reward