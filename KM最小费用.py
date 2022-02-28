import numpy as np
import math

from numpy.matrixlib.defmatrix import matrix
INF=math.inf


N,M = map(int, input().strip().split())

# np array with dimension N*N, if M<N, 用虚拟的点补上，权重为INF
adj_matrix=[[[INF]*N for i in range(N)]]
for i in range(N):
    adj_matrix[i][:len(M)]=list(map(int, input().split()))


label_left=np.max(adj_matrix, axis=1)  # init label for the left set
label_right=np.zeros(N)  # init label for the right set

#match result
match_right = np.empty(N) * np.nan

#dfs辅助变量
visit_left = np.empty(N) * False
visit_right = np.empty(N) * False
slack_right = np.empty(N) * 0

#增广路，dfs
def find_path(i):
    print(f'begin to find path for {i} in group 1')
    visit_left[i] = True
    for j, match_weight in enumerate(adj_matrix[i]):
        
        if visit_right[j]:
            print(f"{visit_right[j]} HAS BEEN VISITED")
            continue  #if visited then next one
        
        gap = match_weight-label_left[i]-label_right[j]
        print(f"gap between left {label_left[i]} and right {label_left[j]} is {gap}")
        if gap == 0:
            #找到可行匹配
            print(f"FIND A MATCH BETWEEN {label_left[i]} on the left and {label_left[j]} on the right")
            visit_right[j] = True
            if np.isnan(match_right[j]) or find_path(match_right[j]):  
                #j未被匹配，或虽然j已被匹配，但是j的已匹配对象有其他可选备胎
                match_right[j]=i
                return True
        else:
            #计算变为可行匹配需要的顶标改变量
            #c-1, C到c只能增加，weight>C+c, gap>0
            if slack_right[j] > -gap: 
                slack_right[j] = -gap
                return False

# KM主函数
def KM():
    for i in range(N):#按照group1的元素循环
        #重置辅助变量
        slack_right = np.empty(N) * 0
        while True:
            #重置辅助变量
            visit_left = np.empty(N) * False
            visit_right = np.empty(N) * False
        
            #能找到可行匹配
            if find_path(i): break

            #不能找到可行匹配，修改顶标
            #(1)将所有在增广路中的X方点的label全部减去一个常数d 
            #(2)将所有在增广路中的Y方点的label全部加上一个常数d
            d = np.inf
            for j, slack in enumerate(slack_right):
                if not visit_right[j] and slack < d:
                    d = slack
                for k in range(N):
                    if visit_left[k]: label_left[k] -= d
                for n in range(N):
                    if visit_right[n]: label_right[n] += d
    res = 0
    for j in range(N):
        if match_right[j] >=0 and match_right[j] < N:
            res += adj_matrix[match[j]][j]
            return res