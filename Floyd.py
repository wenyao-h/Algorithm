# arr=[]
# while True:
#     try:
#         lines=[]
#         lines=list(map(int,input().split(" ")))
#         arr.append(lines)
#     except:break
#====================================================
import sys
arr=[]
for line in sys.stdin:
    temp=list(map(int,line.split(" ")))
    arr.append(temp)

#准备Distance图

N=arr[0][0]
M=arr[0][1]
starting_point=arr[0][2]
ending_point=arr[0][3]

inf=float('inf')
graph=[[inf]*N for i in range(N)]

for i in range(N):
    graph[i][i]=0

for i in range(M):
    a=arr[i+1][0]
    b=arr[i+1][1]
    w=arr[i+1][2]
    graph[a-1][b-1]=w
#===================================================

# inf = float('inf')
# matrix_distance = [[0,3,2,5],
#                    [inf,0,4,inf],
#                    [inf,inf,0,1],
#                    [inf,inf,inf,0]]

def Floyd(dis,s,e):
    #min (Dis(i,j) , Dis(i,k) + Dis(k,j) )
    nums_vertex = len(dis[0])
    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis[s-1][e-1]

length=Floyd(graph,1,4)
print(length)
