from numpy.random import randint
import random
import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import networkx
import sys

number_of_iterations = 4000

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

    def load_best_chromosome(self):
        self.best_chromosome = np.loadtxt("best_chromosome.txt").astype(int)

    def load_best_chromosome_from_cmd(self, i):
        self.best_chromosome = np.loadtxt(i).astype(int)

    def visualize_connections(self, subplot_id, plot_text):
        # first translate points into two arrays

        ax = self.fig.add_subplot(2, 4, subplot_id)
        x_point = []
        y_point = []
        for i in range(self.chromosome_length):
            x_point.append(self.node_list[i][1][0])
            y_point.append(self.node_list[i][1][1])
        # second get connections
        x_connection = []
        y_connection = []
        for i in range(self.chromosome_length):
            x_connection.append(self.node_list[self.best_chromosome[i]][1][0])
            y_connection.append(self.node_list[self.best_chromosome[i]][1][1])
        ax.scatter(x_point,y_point)
        ax.plot(x_connection,y_connection)
        ax.title.set_text(plot_text)

# testing
# create class instance
TSP_instance = travelling_salesman_problem_algorithm(population_size=5)
TSP_instance.best_chromosome = TSP_instance.population[np.argmin(min(TSP_instance.population_evaluation))]
TSP_instance.best_score = min(TSP_instance.population_evaluation)
TSP_instance.visualize_connections((1,2), "Randomly initialized")
TSP_instance.load_best_chromosome_from_cmd("results/xqg237_50k_5p_1956.txt")
TSP_instance.visualize_connections((3,4), "5 chromosome population")
TSP_instance.load_best_chromosome_from_cmd("results/xqg237_50k_20p_1616.txt")
TSP_instance.visualize_connections((5,6), "20 chromosome population")
TSP_instance.load_best_chromosome_from_cmd("results/xqg237_50k_50p_1463.txt")
TSP_instance.visualize_connections((7,8), "50 chromosome population")
TSP_instance.ax.get_xaxis().set_visible(False)
TSP_instance.ax.get_yaxis().set_visible(False)
plt.show()
