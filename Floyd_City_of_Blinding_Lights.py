import sys

def main():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    iterator = iter(data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    
    # Initialize distance matrix with infinity
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # Distance from a node to itself is 0
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    # Read edges
    # Note: If multiple edges exist between the same pair, 
    # the problem states the last one (most recent) overrides previous ones.
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        dist[u][v] = w

    # Floyd-Warshall Algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Process queries
    q = int(next(iterator))
    output = []
    for _ in range(q):
        x = int(next(iterator))
        y = int(next(iterator))
        
        ans = dist[x][y]
        if ans == INF:
            output.append("-1")
        else:
            output.append(str(ans))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
