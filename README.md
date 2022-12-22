# Overwiev

The project aims to implement TSP algorithm without the use of and available python libraries

# The implementation

One chromosome is the path that the travelling salesman is taking (the nodes)

The population of such chromosomes is getting randomly initialized and evaluated 
with a function summing their path lengths. The lower the value, the better the score. 

Then in the loop population members get crossovered with each other with some 
probability (OX crossover mechanism) and reevaluated. If their new score is better 
than the last they are getting replaced with the new chromosome. Parents are picked 
randomly with probability reflecting their score. Parents with better scores are 
more likely to get picked.

If newly created chromosome from two parents has a worse score than the parent,
it is mutated (again it is randomly selected if the mutation occurs) and 
replaces the parent. This allows for better scores but needs some parameter 
optimization to achieve the best score.

The best chromosome with its score gets saved separately to be displayed at the end 
with matplotlib.

# Installation 

```python
pip install tsplib95
```

# Usage

```python 
python tsp.py <file.tsp>
```
