from specimen import Specimen

class Population:
    def __init__(self, tamPop):
        self.specimens = []
        self.tamPop = tamPop


    # cria população com indivíduos aleatórios
    def create_random_population(self):
        for spci in range(0,self.tamPop):
            specimen = Specimen()
            specimen.random_cromossomo()
            self.specimens.append(specimen)

    # cria população vazia
    def create_none_population(self):
        for spci in range(0, self.tamPop):
            self.specimens.append(Specimen())

    def order_population(self):
        ordered_specimens = sorted(self.specimens, key=Specimen.get_fitness)
        self.specimens = ordered_specimens

    #retorna tamanho da lista de indivíduos
    def getNumSpecimens(self):
        return len(self.specimens)

    #Retorna o tamanho da população
    def getTamPop(self):
        return self.tamPop

    #Retorna um individuo especifico
    def getSpeciemen(self, pos):
        return self.specimens[pos]


if __name__ == '__main__':
    pop = Population(tamPop=200)
    pop.create_random_population()
    pop.order_population()

    for ind in pop.specimens:
        print(ind.genetic_code, ind.fitness)
