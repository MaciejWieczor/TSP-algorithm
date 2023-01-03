# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import sys
  
x5 = np.loadtxt("results_eval_v2/xqf131_100k_50p_615_x.txt").astype(int)[:3500]
y5 = np.loadtxt("results_eval_v2/xqf131_100k_50p_615_y.txt").astype(int)[:3500]

plt.plot(x5, y5, label = "With inversion")

x20 = np.loadtxt("results_eval/xqf131_100k_50p_606_x.txt").astype(int)[:3500]
y20 = np.loadtxt("results_eval/xqf131_100k_50p_606_y.txt").astype(int)[:3500]

plt.plot(x20, y20, label = "Without inversion")
  
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
