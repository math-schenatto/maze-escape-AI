import random
from walls import walls
from movement import maze_value, move_value


class Specimen:
    def __init__(self, genetic_code):
        self.fitness = None
        self.genetic_code = genetic_code
        self.current_position = 91
        self.route = []

    def fitness_function(self):
        fitness = 8

class Labyrinth:

    def __init__(self, controller):
        self.control = controller
        self.specimen = self.randomCromossomo()

    def crossOver(self):
        pass

    def mutacao(self):
        pass

    def elitismo(self):
        pass

    def randomCromossomo(self, stringLength=23):
        specimens =[]
        directions = ['00', '01', '10', '11']
        specimens.append(Specimen(genetic_code=''.join(random.choice(directions) for i in range(stringLength))))
        return specimens[0]
    def move_truck(self, current,direction):
        new = current + move_value[direction]

        if new < 0 or new > 100:
            result = 'Fora do mapa'
        elif current % 10 == 0 and direction == '00':
            result = 'Fora do mapa'
        elif current % 10 == 1 and direction == '10':
            result = 'Fora do mapa'
        elif new in walls[current]:
            result = 'Parede'
        else:
            result = 'OK'
        print(f"{current} -> {new} : {result}")

        return new

# cada pos fora do mapa = 100
# cada pos val = 1
# parede penalizacao = 25
# penalizacao se passar por uma mesma pos = 50 percurso[lista]


    def show_track(self):
        start = 0
        end = 2
        for i in range(23):
            direction = self.specimen.genetic_code[start:end]
            self.specimen.current_position = self.move_truck(self.specimen.current_position,direction)
            action = maze_value[direction]
            self.control.move_view_truck(action)
            start += 2
            end += 2


