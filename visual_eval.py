# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import sys
  
x = np.loadtxt(sys.argv[1]).astype(int)
y = np.loadtxt(sys.argv[2]).astype(int)
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel("Iterations")
# naming the y axis
plt.ylabel("Evaluation score")
  
# giving a title to my graph
plt.title(sys.argv[3] + "chromosomes")
  
# function to show the plot
plt.show()
