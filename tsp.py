from numpy.random import randint
import tsplib95
import networkx
import sys

# takes name of tsp file from the first command line argument
class travelling_salesman_problem_algorithm:
    def __init__(self):
        # load the tsplib problem
        self.problem = tsplib95.load('./' + sys.argv[1])

        # convert into a networkx.Graph
        self.graph = self.problem.get_graph()

        # convert into a numpy distance matrix
        self.distance_matrix = networkx.to_numpy_matrix(self.graph)

        # get chromosome length
        self.chromosome_length = self.distance_matrix[0].shape[1]

    def initialize_random_chromosome(self):
        # randomize array of cities indexes
        return(randint(0, self.chromosome_length, self.chromosome_length))

    def return_distance_matrix(self, x, y):
        # print the distance between nodes 4 and 2:
        return(self.distance_matrix[x, y])

    def evaluate_chromosome(self, chromosome_array):
        sum = 0
        for i in range(0, chromosome_array.shape[0]-1):
            sum += self.return_distance_matrix(chromosome_array[i], chromosome_array[i + 1])
        return sum

# testing
TSP_instance = travelling_salesman_problem_algorithm()
for i in range(0, 10): 
    chromosome_1 = TSP_instance.initialize_random_chromosome()
    print(f"Chromosome nr {i} score : {TSP_instance.evaluate_chromosome(chromosome_1)}")
