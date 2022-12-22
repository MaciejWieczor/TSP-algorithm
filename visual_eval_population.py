# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import sys
  
x5 = np.loadtxt(sys.argv[1]).astype(int)
y5 = np.loadtxt(sys.argv[2]).astype(int)

plt.plot(x5, y5, label = "5 chromosomes")

x20 = np.loadtxt(sys.argv[3]).astype(int)
y20 = np.loadtxt(sys.argv[4]).astype(int)

plt.plot(x20, y20, label = "20 chromosomes")

x50 = np.loadtxt(sys.argv[5]).astype(int)
y50 = np.loadtxt(sys.argv[6]).astype(int)

plt.plot(x50, y50, label = "50 chromosomes")
  
# naming the x axis
plt.xlabel("Iterations")
# naming the y axis
plt.ylabel("Evaluation score")
  
# giving a title to my graph
plt.title(sys.argv[7])

# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()
