from population import Population
from specimen import Specimen
import random
class GeneticAlgorithm:
    def __init__(self, crossover, mutation, elitismo):
        self.solution = '010101000001010001101010010000000000010100000000'
        self.solution1 = '0101010000010100011010100100000000000101000000110001'
        self.crossover_rate = crossover
        self.mutation = mutation
        self.elitismo = elitismo
        self.current_population = None

    def crossover(self, pais):
        #genes dos filhos
        filhos = []

        #pontos de corte
        cutoff_1 = random.randint(0,(len(pais[0].genetic_code)/2)-2) + 1
        cutoff_2 = (random.randint(0,(len(pais[0].genetic_code)/2)-2) + len(pais[0].genetic_code)//2)

        #genes dos pais
        gene_pai1 = pais[0].genetic_code
        gene_pai2 = pais[1].genetic_code

        #corte do gene
        gene_filho1 = gene_pai1[0:cutoff_1]
        gene_filho1 = gene_filho1 + gene_pai2[cutoff_1:cutoff_2]
        gene_filho1  = gene_filho1 + gene_pai1[cutoff_2:]

        gene_filho2 = gene_pai2[0:cutoff_1]
        gene_filho2 = gene_filho2 + gene_pai1[cutoff_1:cutoff_2]
        gene_filho2 = gene_filho2 + gene_pai2[cutoff_2:]

        f1 = Specimen()
        f1.create_specimen(gene_filho1, self.mutation)

        f2 = Specimen()
        f2.create_specimen(gene_filho2, self.mutation)

        filhos.append(f1)
        filhos.append(f2)

        return filhos

    def create_new_generation(self, current_population):
        self.current_population = current_population
        filhos = []

        new_population = Population(current_population.getTamPop())

        if self.elitismo == True:
            new_population.specimens.append(current_population.getSpeciemen(pos=0))


        while len(new_population.specimens) < len(current_population.specimens):
            pais = self.torneio()

            if random.uniform(0,1) <= self.crossover_rate:
                filhos = self.crossover(pais)
            else:
                filhos = pais

            new_population.specimens.append(filhos[0])
            new_population.specimens.append(filhos[1])

        new_population.order_population()

        return new_population



    def torneio(self):
        pop_itermediaria = Population(tamPop=3)
        pop_itermediaria.specimens.append(random.choice(self.current_population.specimens))
        pop_itermediaria.specimens.append(random.choice(self.current_population.specimens))
        pop_itermediaria.specimens.append(random.choice(self.current_population.specimens))


        pop_itermediaria.order_population()

        pais = []
        pais.append(pop_itermediaria.getSpeciemen(0))
        pais.append(pop_itermediaria.getSpeciemen(1))

        return pais

    def get_solution(self, gen):
        if gen == self.solution1:
            print('Achou o perfeito==', gen)
            return True
        else:
            return False


# Testing

# GeneticAlgorithm(solution, crossover, mutation, elitismo)
