import random
import string
from walls import walls
import IPython as ipy
from maze_env import Maze
from movement import maze_value, move_value

class Specimen:
    def __init__(self, genetic_code):
        self.fitness = None
        self.genetic_code = genetic_code
        self.current_position = 91
        self.route = []

    def fitness_function(self):
        fitness = 8


def crossOver():
    pass

def mutacao():
    pass

def elitismo():
    pass

def randomCromossomo(stringLength=23):
    directions = ['00', '01', '10', '11']
    return ''.join(random.choice(directions) for i in range(stringLength))

def move_truck(current,direction):
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


def show_track(cromossomo):
    start = 0
    end = 2
    env.reset()
    for i in range(23):
        direction = specimen.genetic_code[start:end]
        specimen.current_position = move_truck(specimen.current_position,direction)
        action = maze_value[direction]
        env.render()
        env.step(action)
        start += 2
        end += 2


if __name__ == "__main__":
    specimen = Specimen(genetic_code=randomCromossomo())
    env = Maze()
    env.after(100, show_track(specimen))
    env.mainloop()
