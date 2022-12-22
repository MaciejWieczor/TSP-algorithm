from numpy.random import randint
import random
import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import networkx
import sys

number_of_iterations = 20000

# takes name of tsp file from the first command line argument
class travelling_salesman_problem_algorithm:
    def __init__(self, population_size=5):
        # set population size
        self.population_size = population_size

        # load the tsplib problem
        self.problem = tsplib95.load('./' + sys.argv[1])

        # convert into a networkx.Graph
        self.graph = self.problem.get_graph()

        # get nodes into a list for easier plotting
        self.node_list = list(self.graph.nodes(data='coord'))

        # convert into a numpy distance matrix
        self.distance_matrix = networkx.to_numpy_matrix(self.graph)

        # get chromosome length
        self.chromosome_length = self.distance_matrix[0].shape[1]

        # initialize population
        self.population = []
        for i in range(self.population_size):
            self.population.append(self.initialize_random_chromosome())

        # initialize evaluation value for each population member to max
        self.population_evaluation = [sys.maxsize] * self.population_size

        # visual part 
        self.fig, self.ax = plt.subplots()

        # best chromosome
        self.best_chromosome = None
        self.best_score = None

    def initialize_random_chromosome(self):
        # randomize array of cities indexes
        # array = randint(1, self.chromosome_length, self.chromosome_length-1)
        # array = np.random.choice(range(1, self.chromosome_length),\
                                 # self.chromosome_length-1, replace=False)
        array = np.array(list(range(1, self.chromosome_length)))
        random.shuffle(array)
        array = np.insert(array, 0, 0)
        return(array)

    def return_distance_matrix(self, x, y):
        # print the distance between nodes 4 and 2:
        return(self.distance_matrix[x, y])

    def evaluate_chromosome(self, chromosome_array):
        sum = 0
        for i in range(0, chromosome_array.shape[0]-1):
            sum += self.return_distance_matrix(chromosome_array[i], chromosome_array[i + 1])
        return sum

    def evaluate_chromosomes(self):
        for i in range(self.population_size):
            self.population_evaluation[i] = self.evaluate_chromosome(self.population[i])

    def crossing_function(self, i, second_parent_index):
        # implement OX crossover here

        # create children
        first_crossover_point = randint(1, self.chromosome_length/2)
        second_crossover_point = randint(self.chromosome_length/2, self.chromosome_length)

        new_child_one = [0] * self.chromosome_length
        new_child_two = [0] * self.chromosome_length

        new_child_one[first_crossover_point:second_crossover_point] = \
            self.population[i][first_crossover_point:second_crossover_point]
        new_child_two[first_crossover_point:second_crossover_point] = \
            self.population[second_parent_index][first_crossover_point:second_crossover_point]

        # print("CHROMOSOME")
        # print("POPULATION @ i")
        # print(self.population[i])
        # print("SECOND PARENT POPULATION")
        # print(self.population[second_parent_index])
        # print("NEW CHILD INIT @ i")
        # print(new_child_one)
        # print(len(new_child_one))

        new_child_one_tmptmp = list(self.population[i][second_crossover_point:]) + \
                               list(self.population[i][1:first_crossover_point]) + \
                               list(self.population[i][first_crossover_point:second_crossover_point])
        new_child_two_tmptmp = list(self.population[second_parent_index][second_crossover_point:]) + \
                               list(self.population[second_parent_index][1:first_crossover_point]) + \
                               list(self.population[second_parent_index][first_crossover_point:second_crossover_point])

        new_child_one_tmp = [i for i in new_child_one_tmptmp if i not in new_child_two]
        new_child_two_tmp = [i for i in new_child_two_tmptmp if i not in new_child_one]

        # print("NEW CHILD MERGED CUT @ i")
        # print(new_child_two_tmptmp)
        # print(len(new_child_two_tmptmp))
        # print("NEW CHILD MERGED CUT REMOVED COPIES @ i")
        # print(new_child_two_tmp)
        # print(len(new_child_two_tmp))
        # print(f"LEN TMP {len(new_child_one_tmp)}, LEN MIDDLE PART {second_crossover_point - first_crossover_point}")
        # print(f"LEN SUM {len(new_child_one_tmp) + second_crossover_point - first_crossover_point}")

        new_child_one = \
            np.array([0] + \
            list(new_child_two_tmp[first_crossover_point:]) + \
            list(self.population[i][first_crossover_point:second_crossover_point]) + \
            list(new_child_two_tmp[:first_crossover_point]))


        # print("NEW CHILD AFTER CROSSING @ i")
        # print(new_child_one)
        # print(len(new_child_one))

        new_child_two = \
            np.array([0] + \
            list(new_child_one_tmp[first_crossover_point:]) + \
            list(self.population[second_parent_index][first_crossover_point:second_crossover_point]) + \
            list(new_child_one_tmp[:first_crossover_point]))

        # evaluate children scores 

        child_one_evaluation = self.evaluate_chromosome(new_child_one)
        child_two_evaluation = self.evaluate_chromosome(new_child_two)

        # if better than their parents replace the parents
        # return 0 if both parents are replaced
        # return 1 if first parent is replaced
        # return 2 if second parent is replaced
        # return 3 if no parents are replaced

        return_value = 3

        if child_one_evaluation < self.population_evaluation[i]:
            self.population[i] = new_child_one
            self.population_evaluation[i] = child_one_evaluation
            return_value = 1


        if child_two_evaluation < self.population_evaluation[second_parent_index]:
            self.population[second_parent_index] = new_child_two
            self.population_evaluation[second_parent_index] = child_two_evaluation
            if(return_value == 3):
                return_value = 2

        # print("------------------------------------------------------------------------")
        return return_value

    def mutating_function(self, i):

        test = randint(0, 1000)
        if test < 10:

            # swap two elements of the "i" chromosome
            first_mutation_index = randint(11, self.chromosome_length-10)
            second_mutation_index = randint(first_mutation_index-10, first_mutation_index+10)
            while first_mutation_index == second_mutation_index:
                second_mutation_index = randint(first_mutation_index-10, first_mutation_index+10)

            new_mutated_chromosome = self.population[i]

            # do the swap
            tmp = new_mutated_chromosome[second_mutation_index]

            new_mutated_chromosome[second_mutation_index] = \
                new_mutated_chromosome[first_mutation_index]

            new_mutated_chromosome[first_mutation_index] = tmp


            # test evaluation 
            mutated_evaluation = self.evaluate_chromosome(new_mutated_chromosome)
            # if mutated_evaluation < self.population_evaluation[i]:
            self.population[i] = new_mutated_chromosome 
            self.population_evaluation[i] = mutated_evaluation

    def update_population(self):
        # loop through all chromosomes 
        best_score = max(self.population_evaluation)
        for i in range(0, self.population_size):
            # do probability test based on current outcome against best evaluation 
            # (best should have max probability) 
            # here we get <0, 1> float and we multiply it by 1000
            probability_treshold = (1000 * self.population_evaluation[i]) / best_score
            probability_test = randint(0, 1001)
            # if test passed then do crossing and check agains last evaluation 
            # if better than last evaluation update member - else go to mutations
            if(probability_test < probability_treshold):

                # find second parent
                second_parent_index = randint(0, self.population_size)
                while second_parent_index == i:
                    second_parent_index = randint(0, self.population_size)

                do_mutation = self.crossing_function(i, second_parent_index)
                # mutate member if he didn't do crossing
                if do_mutation == 3:
                    self.mutating_function(i)

    def visualize_connections(self):
        # first translate points into two arrays
        x_point = []
        y_point = []
        for i in range(self.chromosome_length):
            x_point.append(self.node_list[i][1][0])
            y_point.append(self.node_list[i][1][1])
        # second get connections
        x_connection = []
        y_connection = []
        min_index = np.argmin(self.population_evaluation)
        for i in range(self.chromosome_length):
            x_connection.append(self.node_list[self.best_chromosome[i]][1][0])
            y_connection.append(self.node_list[self.best_chromosome[i]][1][1])
        self.ax.scatter(x_point,y_point)
        self.ax.plot(x_connection,y_connection)
        plt.show()

# testing
# create class instance
TSP_instance = travelling_salesman_problem_algorithm(population_size=5)
TSP_instance.best_chromosome = TSP_instance.population[np.argmin(min(TSP_instance.population_evaluation))]
TSP_instance.best_score = min(TSP_instance.population_evaluation)

for k in range(number_of_iterations):
    # get chromosome scores
    TSP_instance.evaluate_chromosomes()

    # get new population based on probability
    TSP_instance.update_population()

    if(k % 1000 == 0):
        print(f"ITERATION {k}")
        print(min(TSP_instance.population_evaluation))
    if(min(TSP_instance.population_evaluation) < TSP_instance.best_score):
        TSP_instance.best_chromosome = TSP_instance.population[np.argmin(min(TSP_instance.population_evaluation))]
        TSP_instance.best_score = min(TSP_instance.population_evaluation)

TSP_instance.visualize_connections()
