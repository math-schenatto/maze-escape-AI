import random
import string
from walls import walls
import IPython as ipy
from maze_env import Maze
import time

class Individuo:
    def __init__(self):
        self.aptidao = None
        self.cromosssomo = None


def crossOver():
    pass

def mutacao():
    pass

def elitismo():
    pass

def randomCromossomo(stringLength=23):
    directions = ['00', '01', '10', '11']
    return ''.join(random.choice(directions) for i in range(stringLength))

#for i in range(100):
#    print(randomString())




move_value = {
    '00': +1,   # '00': leste,
    '01': -10,  # '01': norte,
    '10': -1,   # '10': oeste,
    '11': +10   # '11': sul
}

maze_value ={
    '00': 3,   # '00': leste,
    '01': 2,  # '01': norte,
    '10': 4,   # '10': oeste,
    '11': 1   # '11': sul
}

def fitness_function():
    fitness =

def move_truck(current,direction):
    new = current + move_value[direction]
    #ipy.embed()
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
    current = 91
    start = 0
    end = 2
    env.reset()
    for i in range(23):
        direction = cromossomo[start:end]
        current = move_truck(current,direction)
        action = maze_value[direction]
        env.render()
        env.step(action)
        start += 2
        end += 2


if __name__ == "__main__":
    #cromossomo = "0101010000011010010000000000000000000101010100"
    cromossomo = randomCromossomo()
    env = Maze()
    env.after(100, show_track(cromossomo))
    env.mainloop()
