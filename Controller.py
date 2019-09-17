from movement import maze_value
from specimen import Specimen
from maze_env import  Maze

from genetic_algorithm import GeneticAlgorithm
from population import Population

class Controller:
    def __init__(self):
        pass
        self.env = Maze(self)
        self.env.mainloop()

    def move_view_truck(self, action):
        self.env.render()
        self.env.step(action)

    def main_show_maze(self, pop, cross, mut, max_generation, elitismo):
        # vars
        solution = False
        generation = 0
        mut = float(mut)
        cross = float(cross)
        elitismo = True if str(elitismo) == '1' else False
        # Cria a população
        ##########################################3
        population = Population(tamPop=int(pop))
        population.create_random_population()

        # Cria o algoritmo genetico
        algoritmo = GeneticAlgorithm(crossover=cross, mutation=mut, elitismo=elitismo)

        while solution == False and generation<=int(max_generation):
            generation += 1

            population = algoritmo.create_new_generation(current_population=population)
            best_specimen = population.getSpeciemen(0)
            # Reseta a tela e mostra o caminho do melhor cromossomo
            ######################################################################
            if generation % 10 == 0:
                self.env.reset()
                self.env.after(100, self.show_path_on_maze(best_specimen=best_specimen))

            solution = algoritmo.get_solution(best_specimen.genetic_code)
            conteudo = '\nCódigo={} \nFitness={} \nGeração={}\nRota=[{}]'.format(best_specimen.genetic_code, best_specimen.fitness, generation,best_specimen.route)

            self.env.delete()
            self.env.escreve(conteudo)
            print(best_specimen.genetic_code, best_specimen.fitness, best_specimen.route, generation)



    def show_path_on_maze(self, best_specimen):
        specimen = best_specimen
        start = 0
        end = 2
        for i in range(26):
            direction = specimen.genetic_code[start:end]
            start += 2
            end += 2
            action = maze_value[direction]
            self.move_view_truck(action)

if __name__ == "__main__":

    algorithm = GeneticAlgorithm(0.7, 0.2, 1)
    population = Population(2000)
    population.create_random_population()
    generations_limit = 120

    controler = Controller()
    #controler.main_show_maze(5000, 8.6, 0.5, 1000, 1)