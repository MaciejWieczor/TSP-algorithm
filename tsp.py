from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import networkx
import sys

number_of_iterations = 1000

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

    def crossing_function(self, i):
        # implement OX crossover here
        # find second parent
        # create children
        # evaluate children scores 
        # if better than their parents replace the parents - return 0
        # else - return 1
        pass

    def mutating_function(self, i):
        pass

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
                do_mutation = self.crossing_function(i)
                # mutate member if he didn't do crossing
                if(do_mutation):
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
        for i in range(self.chromosome_length):
            x_connection.append(self.node_list[self.population[0][i]][1][0])
            y_connection.append(self.node_list[self.population[0][i]][1][1])
        self.ax.scatter(x_point,y_point)
        self.ax.plot(x_connection,y_connection)
        plt.show()

# testing
# create class instance
TSP_instance = travelling_salesman_problem_algorithm(population_size=20)

for k in range(number_of_iterations):
    # get chromosome scores
    TSP_instance.evaluate_chromosomes()

    # get new population based on probability
    TSP_instance.update_population()

    print(TSP_instance.population_evaluation)

TSP_instance.visualize_connections()
