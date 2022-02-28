def DP(cost):
    num = len(cost)
    m = len(cost[0])
    dp = [[100000] * (1 << m) for i in range(num + m)]
    #dp = min cost to cover first i points in group1 and a set of points s in group2.
    #s is presented as a bit mask
    #初始dp的任何数都大于1e5

    for i in range(num):
        if i == 0:
            pre_status = 0
            for j in range(m):
                status = pre_status | (1 << j)
                
                
                print(f'from group 2: {j} -> pre_status:{pre_status} status: {status}')
                #状态压缩，status=2**j，
                #现在确定num>m，因此第一组至少每个都有一条边，状态只需要维护第二组的链接状态就行
                #Eg. abc|ab.|a.c|.bc|a..|.b.|..c|... 2**3种状态，相当于一个ele from group 2的状态一个bit
                # => 00111|00110|00101|.....
                #j=0 -> a.. | j=1 -> ab. | j=2 -> abc
                dp[i][status] = min(dp[i][status], cost[i][j])
                #对于A，看谁靓，想连谁就连谁咯

                print(f'dp[i]: {dp[i]}')
        else:
            print(f'========== i={i} =============')
            for pre_status in range(1 << m):
                if dp[i - 1][pre_status] >= 100000:
                    #如果第二组有某个点没连接，需要选一个最小的cost做连接，后面体现
                    continue
                for j in range(m):
                    #先pre_status再j的循环是因为B要看A的脸色
                    #先根据当A连上所有第二组的各点的情况，分别讨论B连上各点的情况
                    #Aa时，B点连接group2，总体cost：[x, 2+3, 2+4,       x, 2+7,x , x, x])
                    #Ab时，B点连接group3，总体cost：[x, 2+3, 2+4(不变), x, 2+7,x , x, x]
                    status = pre_status | (1 << j)
                    dp[i][status] = min(dp[i][status], dp[i - 1][pre_status] + cost[i][j])
                    #如果A点有连接，B点要在冲突（右边一点出现多边）与换点之间选择
                    print(f'dp[{i}][{status}]：{dp[i][status]}, dp[{i - 1}][{pre_status}] + cost[{i}][{j}] = {dp[i - 1][pre_status]} + { cost[i][j]} ')
                    
        print(f'i:{i}, dp[i]: {dp[i]}')
    print(f'####################\ndp:{dp}')

    min_cost = []
    for j in range(m):
        mcost = 100000 #threshhold
        for i in range(num):
            mcost = min(cost[i][j], mcost)
        min_cost.append(mcost)
    for j in range(m):
        for pre_status in range(1 << m):
            if dp[num + j - 1][pre_status] >= 100000:
                continue
            if pre_status & (1 << j) != 0:
                dp[num + j][pre_status] = min(dp[num + j][pre_status], dp[num + j - 1][pre_status])
            else:
                status = pre_status | (1 << j)
                dp[num + j][status] = min(dp[num + j][status], dp[num + j - 1][pre_status] + min_cost[j])
        print(j, dp[m + j])
    return dp[-1][-1]

point = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
DP(point)
