
import math
import os
import random
import re
import sys

def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
            return 0
        
        # Mark cell as visited by setting it to 0
        grid[r][c] = 0
        region_size = 1
        
        # Explore all 8 adjacent directions (horizontally, vertically, diagonally)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                region_size += dfs(r + dr, c + dc)
                
        return region_size

    max_size = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                max_size = max(max_size, dfs(r, c))
                
    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
