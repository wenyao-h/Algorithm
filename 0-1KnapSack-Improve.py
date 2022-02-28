w=[]
v=[]
lines_1=list(map(int,input().split(" ")))
W=lines_1[1]

while True:
    try:
        lines=[]
        lines=list(map(int,input().split(" ")))
        w.append(lines[0])
        v.append(lines[1])
    except:break

def KnapSack(W,weight,value):

    dp=[0 for i in range(W+1)]
    for i in range(len(weight)):
        for j in range(W,weight[i]-1,-1): 
        #从容量W开始往下递减
        #逆序才能保证推dp[j]时dp[j-weight[i]]保存的是状态dp[i-1][j-weight[i]]的值
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
 
    return dp[W]


# w=[13, 18, 89, 96, 32, 62, 22, 18, 99, 69]
# v=[660, 586, 939, 501, 100, 577, 337, 975, 127, 753]
# W=0

VAL=KnapSack(W,w,v)
print(VAL)


