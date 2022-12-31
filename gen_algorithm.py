from itertools import permutations
import pygad
# import Simulation as sim
import characteristics_of_soldiers
import armors
from random import randint
import numpy as np
import pickle


charact_soldiers = characteristics_of_soldiers.all_characteristics
_armors = armors.armors
min_price = armors.min_price


class GeneticALgorithm:
    def __init__(self, charact_soldiers, armors, min_price, start_price, fitness_fun=None) -> None:
        self.ch_soldiers = charact_soldiers
        self.armors = armors
        self.min_price = min_price
        self.start_price = start_price
        self.fitness_fun = fitness_fun

    def create_weapon_buyer(self, armors, start_price):
        copy_armors = armors.copy()
        sp = start_price
        result = []
        arms = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        while sp > 0:
            r = randint(0, len(copy_armors) - 1)
            if copy_armors[r].price <= sp:
                arms[r] += 1
                sp -= copy_armors[r].price
            else:
                break
        for key in arms.keys():
            result.append((key, arms[key]))
        return result

    def population(self):
        population = []
        charact = []
        for x in permutations(range(5), 3):
            charact.append(list(x))
        weapons = []
        for x in range(len(charact)):
            weapons.append(self.create_weapon_buyer(
                self.armors,  self.start_price))
        for x, y in zip(charact, weapons):
            population.append(x + y)
        return population

    def get_fitness_scores(self, population):
        scores = []
        pop = population
        for gen in pop:
            sold_alive = self.fitness_fun(20, 20, 40, 40, 100, gen)
            for sol in sold_alive:
                if sol.army == 'B':
                    scores.append(0)
                    break
            else:
                scores.append(len(sold_alive))
        return scores

    def ranking_scores(self, scores: list[int], generation):
        if generation == 1:
            result = np.argsort(scores)
            return result[:20]
        if generation == 2:
            result = np.argsort(scores)
            return result[:10]
        if generation == 3:
            result = np.argsort(scores)
            return result[:4]

    def crossover(self, parent1, parent2, crossover_type):

        # Check crossover type
        if crossover_type not in ['one_point']:
            raise ValueError(
                'crossover_type should be one of uniform and one_point ')

        if crossover_type == 'one_point':
            index = np.random.choice(range(len(parent1)))
            children = [parent2[:index] + parent1[index:],
                        parent1[:index] + parent2[index:]]
        # elif crossover_type == 'uniform':
        #     parents = list(zip(*[parent1, parent2]))
        #     children1 = tuple([np.random.choice(element)
        #                       for element in parents])
        #     children2 = tuple([np.random.choice(element)
        #                       for element in parents])
        #     children = [children1, children2]
        else:
            pass
        return children

    def optimize(self):
        population = self.population()
        generation = 1
        new_population = population
        while generation <= 3:
            scores = self.get_fitness_scores(new_population)
            ranking_scores = self.ranking_scores(scores, generation)
            new_population = []
            for index in ranking_scores:
                new_population.append(population[index])
            # crossover
            children = []
            for i in range(len(new_population) - 1):
                children.append(self.crossover(
                    new_population[i], new_population[i+1], 'one_point'))
            generation += 1
        return children[0]


# ga = GeneticALgorithm(charact_soldiers, _armors, min_price,
#                       1000, sim.start_simulation)
# population = ga.population()
# # scores = ga.get_fitness_scores(population)
# # sc = scores
# # with open('dic_indx_tfidf.txt', 'wb') as fh:
# #     pickle.dump(sc, fh)
# #     fh.close()

# pickle_1 = open(
#     'C:/Users/acer/Downloads/Telegram Desktop/Simulacion/Proyecto simulacion/Battlefield/dic_indx_tfidf.txt', 'rb')
# po = pickle.load(pickle_1)
# # print(po)
# ga.optimize(po, population)
