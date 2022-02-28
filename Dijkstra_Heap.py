import sys
import heapq

line = list(map(int, sys.stdin.readline().split()))
N,M,s,t=line[0],line[1],line[2],line[3]

neighbors = [[] for j in range(N)]
edge = []
for i in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    edge.append(line)
    neighbors[edge[i][0]-1].append((edge[i][1]-1, edge[i][2]))
    #python的index从0计数，有调整


def startwith(start, neighbors):
    passed = []
    dis = [float('inf') for _ in range(N)]#先将距离都设定为inf
    dis[start] = 0#start到start距离为0
    Q = []
    for i in range(N):
        heapq.heappush(Q, (dis[i], i))#将各点加入堆中
    while Q:
        #弹出距离最小的vertice，如果已经松驰过，则跳过
        flag = heapq.heappop(Q)[1]
        if flag in passed: continue

        #没有松弛过，加入passed
        passed.append(flag)
        
        #relaxing
        for V in neighbors[flag]:
            if not V[0] in passed:
                if V[1] + dis[flag] < dis[V[0]]:
                    dis[V[0]] = V[1] + dis[flag]
                    heapq.heappush(Q, (dis[V[0]], V[0]))

    return dis


dist = startwith(s-1, neighbors)

print(dist[t-1] if (not dist[t-1] == float('inf')) else -1)