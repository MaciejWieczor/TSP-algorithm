# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import sys
  
x5 = np.loadtxt("results_eval_v2/xqf131_100k_50p_615_x.txt").astype(int)
y5 = np.loadtxt("results_eval_v2/xqf131_100k_50p_615_y.txt").astype(int)

plt.plot(x5, y5, label = "50 chromosomes")

x20 = np.loadtxt("results_eval_v2/xqf131_100k_75p_588_x.txt").astype(int)
y20 = np.loadtxt("results_eval_v2/xqf131_100k_75p_588_y.txt").astype(int)

plt.plot(x20, y20, label = "75 chromosomes")

x50 = np.loadtxt("results_eval_v2/xqf131_100k_100p_614_x.txt").astype(int)
y50 = np.loadtxt("results_eval_v2/xqf131_100k_100p_614_y.txt").astype(int)

plt.plot(x50, y50, label = "100 chromosomes")
  
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
