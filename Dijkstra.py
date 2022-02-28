arr=[]
while True:
    try:
        lines=[]
        lines=list(map(int,input().split(" ")))
        arr.append(lines)
    except:break

#准备Distance图

N=arr[0][0]
M=arr[0][1]
source=arr[0][2]
ending=arr[0][3]

inf = float("inf")
graph=[[inf]*N for i in range(N)]

for i in range(N):
    graph[i][i]=0

for i in range(M):
    a=arr[i+1][0]
    b=arr[i+1][1]
    w=arr[i+1][2]
    graph[a-1][b-1]=w

# mgraph = [[0, 1, 12, inf, inf, inf],
#              [inf, 0, 9, 3, inf, inf],
#             [inf, inf, 0, inf, 5, inf],
#              [inf, inf, 4, 0, 13, 15],
#              [inf, inf, inf ,inf, 0, 4],
#             [inf, inf, inf, inf ,inf, 0]]
def startwith(start, graph):
    passed = [start]
    nopass = [x for x in range(len(graph)) if x != start]
    dis = graph[start]
    
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)#Q
        passed.append(idx)#S

        #relaxing
        #ONLY FOR DIRECTED GRAPH
        for i in nopass:
            if dis[idx] + graph[idx][i] < dis[i]: 
                dis[i] = dis[idx] + graph[idx][i]

            #dis[idx]就是graph[start][idx]
            #dis[i]就是graph[start][i]
            
    return dis

dis = startwith(source-1, graph)

if dis[ending-1]==inf:
    print(-1)
else: print(dis[ending-1])