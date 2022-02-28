def UK(W,weights,values):
    
    B=[0 for i in range(W+1)]
    #物品总价值，起始值都先设为0
    #如果不提前设定好array的形状，会报错，说list index out of range
    ITEMS=[[] for i in range(W+1)]    
       
    for w in range(W+1):
        
        #中途会需要用到较小的背包容量，所以将所有组合都放进来了
        #循环一遍后，w会改变，所以是从一个新的背包容量开始
        for i in range(len(weights)):
            #n必然小于len(weights)，因为实在weights的物品中做循环
            if (weights[i]<=w):
                B[w]=max(B[w-weights[i]]+values[i],B[w])
                if B[w-weights[i]]+values[i]>=B[w]:
                    ITEMS[w]=ITEMS[w-weights[i]]+[weights[i]]
                    #用list.append()或者([],[])都不好使
                    
    return B[W],ITEMS[W]

weights=[2,3,5,7,8,11]
values=[2,4,6,9,11,15]
W=30

UK(W,weights,values)


weights=[1,2,3]
values=[1,4,6]
W=3

UK(W,weights,values)