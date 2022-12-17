from numpy.random import randint
import tsplib95
import networkx
import sys

# takes name of tsp file from the first command line argument
class travelling_salesman_problem_algorithm:
    def __init__(self, population_size=5):
        # set population size
        self.population_size = population_size

        # load the tsplib problem
        self.problem = tsplib95.load('./' + sys.argv[1])

        # convert into a networkx.Graph
        self.graph = self.problem.get_graph()

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

    def initialize_random_chromosome(self):
        # randomize array of cities indexes
        array = randint(1, self.chromosome_length, self.chromosome_length-1)
        array[0] = 0
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
            

# testing
# create class instance
TSP_instance = travelling_salesman_problem_algorithm(population_size=10)
# evaluate first population iteration
TSP_instance.evaluate_chromosomes()
# loop over each member of the population
for i in range(TSP_instance.population_size): 
    # print each member score
    print(f"Chromosome nr {i} score : {TSP_instance.population_evaluation[i]}")
    # print each member city visit order
    print(TSP_instance.population[i])
