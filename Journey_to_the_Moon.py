
import math
import os
import random
import re
import sys
from collections import defaultdict

def journeyToMoon(n, astronaut):
    # Build adjacency list representation of the graph
    adj = defaultdict(list)
    for u, v in astronaut:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * n
    country_sizes = []
    
    # Run DFS iteratively to find the size of each connected component (country)
    for i in range(n):
        if not visited[i]:
            size = 0
            stack = [i]
            visited[i] = True
            
            while stack:
                curr = stack.pop()
                size += 1
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        
            country_sizes.append(size)
    
    # Calculate valid pairs: Total Pairs - Same Country Pairs
    total_pairs = n * (n - 1) // 2
    same_country_pairs = sum(c * (c - 1) // 2 for c in country_sizes)
    
    return total_pairs - same_country_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
