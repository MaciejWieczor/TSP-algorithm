# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import sys
  
x5 = np.loadtxt("results_eval/xqg237_100k_5p_1744_x.txt").astype(int)
y5 = np.loadtxt("results_eval/xqg237_100k_5p_1744_y.txt").astype(int)

plt.plot(x5, y5, label = "5 chromosomes")

x20 = np.loadtxt("results_eval/xqg237_100k_20p_1428_x.txt").astype(int)
y20 = np.loadtxt("results_eval/xqg237_100k_20p_1428_y.txt").astype(int)

plt.plot(x20, y20, label = "20 chromosomes")

x50 = np.loadtxt("results_eval/xqg237_100k_50p_1344_x.txt").astype(int)
y50 = np.loadtxt("results_eval/xqg237_100k_50p_1344_y.txt").astype(int)

plt.plot(x50, y50, label = "50 chromosomes")
  
# naming the x axis
plt.xlabel("Iterations")
# naming the y axis
plt.ylabel("Evaluation score")
  
# giving a title to my graph
plt.title("Evaluation score in relation to iterations")

# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()
