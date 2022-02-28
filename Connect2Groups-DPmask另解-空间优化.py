def DP(cost):
    m = len(cost)
    n = len(cost[0])
    s = m + n
    t = s + 1
    _s = t + 1
    _t = _s + 1

    #dp[i][s]=min cost to cover first i points in group1 and a set of points s in group2.
    dp = [[0] * (_t + 1) for _ in range(_t + 1)] #m+n+3
    v = [[0] * (_t + 1) for _ in range(_t + 1)] 

    for i in range(m):
        dp[s][i] = n - 1
        dp[_s][i] = 1

    for j in range(m, m + n):
        dp[j][t] = m - 1
        dp[j][_t] = 1

    dp[t][_s] = n
    dp[s][_t] = m - n
    dp[_t][s] = n
    dp[t][s] = m * n - n
    dp[s][t] = n

    for i in range(m):
        for j in range(n):
            dp[i][j + m] = 1
            v[i][j + m] = cost[i][j]
            v[j + m][i] = -cost[i][j]
    res = 0
    while True:
        dis = [None] * (_t + 1)
        prev = [None] * (_t + 1)
        used = {_s}
        dis[_s] = 0
        now = _s
        while _t not in used:
            min_dis = None
            next = None
            for index in range(_t + 1):
                if dp[now][index] > 0 and (dis[index] is None or dis[index] > dis[now] + v[now][index]):
                    dis[index] = dis[now] + v[now][index]
                    prev[index] = now
                    if index in used:
                        used.remove(index)
                if index not in used and dis[index] is not None and (min_dis is None or min_dis > dis[index]):
                    next = index
                    min_dis = dis[index]

            if min_dis is None:
                return res

            used.add(next)
            now = next

        res += dis[_t]
        now = _t
        while now != _s:
            dp[now][prev[now]] += 1
            dp[prev[now]][now] -= 1
            now = prev[now]
    
    return res

N, M = map(int, input().split())
point = []
for i in range(N):
    a = [int(i) for i in input().split()]
    point.append(a)
