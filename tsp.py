from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import networkx
import sys

number_of_iterations = 5000

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


    def initialize_random_chromosome(self):
        # randomize array of cities indexes
        # array = randint(1, self.chromosome_length, self.chromosome_length-1)
        array = np.random.choice(range(1, self.chromosome_length),\
                                 self.chromosome_length-1, replace=False)
        array = np.insert(array, 0, 0)
        print(array)
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

    def sort_by_evaluation(self):
        self.population = [x for _, x in sorted(zip(self.population_evaluation,\
                                                    self.population))]
        self.population_evaluation.sort()

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
        print(self.node_list[self.population[0][0]])
        print(list(self.population[0]))
        for i in range(self.chromosome_length):
            x_connection.append(self.node_list[self.population[0][i]][1][0])
            y_connection.append(self.node_list[self.population[0][i]][1][1])
        self.ax.scatter(x_point,y_point)
        self.ax.plot(x_connection,y_connection)
        plt.show()

    def population_crossing(self):
        pass

    def population_mutating(self):
        pass

    def get_new_population(self):
        self.population_crossing()
        self.population_mutating()

# testing
# create class instance
TSP_instance = travelling_salesman_problem_algorithm(population_size=20)

for k in range(number_of_iterations):
    # evaluate first population iteration
    TSP_instance.evaluate_chromosomes()

    # sort population by evaluation
    TSP_instance.sort_by_evaluation()

    # loop over each member of the population
    # for i in range(TSP_instance.population_size): 
    #     # print each member score
    #     print(f"Chromosome nr {i} score : {TSP_instance.population_evaluation[i]}")

        # # print each member city visit order
        # print(TSP_instance.population[i])

    print(f"Best chromosome score : {TSP_instance.population_evaluation[0]} \
            at iteration number {k}")

    # mutate best chromosome
    TSP_instance.get_new_population()

TSP_instance.visualize_connections()
