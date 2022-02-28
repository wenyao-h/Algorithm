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

def KnapSack(W,weights,values):
    
    B=[[0]*len(weights) for i in range(W+1)]

    #B[i,w] 所以是W*n的矩阵
    #物品总价值，起始值都先设为0

    for i in range(len(weights)):
        for w in range(W+1):
            if weights[i]<=w:
            #中途会需要用到较小的背包容量，所以将所有组合都放进来了
            #循环一遍后，w会改变，所以是从一个新的背包容量开始
                if values[i]+B[w-weights[i]][i-1]>=B[w][i-1]:
                    B[w][i]=values[i]+B[w-weights[i]][i-1]

                else:
                    B[w][i]=B[w][i-1]
            else:
                B[w][i]=B[w][i-1]
    return B[W][len(weights)-1]


#w=[13, 18, 89, 96, 32, 62, 22, 18, 99, 69]
#v=[660, 586, 939, 501, 100, 577, 337, 975, 127, 753]
#W=0

VAL=KnapSack(W,w,v)
print(VAL)


