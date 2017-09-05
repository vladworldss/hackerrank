# coding: utf-8
# Resolve of task "Zipped!"
from statistics import mean


if __name__ == '__main__':
    N, X = map(int, input().split())
    if (0<N<=100) and (0<X<=100):
        studs = [[float(x) for x in input().split()] for i in range(X)]
        results = zip(*studs)
        for x in results:
        	print(mean(x))
        
# INPUT
"""
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
"""

# OUTPUT
"""
90.0 
91.0 
82.0 
90.0 
85.5
"""