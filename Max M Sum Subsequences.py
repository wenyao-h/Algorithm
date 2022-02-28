while True:
    try:
        setting=list(map(int,input().split(" ")))
        m=setting[1]
        n=setting[0]

        lines=list(map(int,input().split(" ")))
        lines.insert(0,0)
        #在列表左边添加一个0，从0开摆

        inf = 1e+6
        dp1 = [0]*100000
        dp2 = [0]*100000
        res = 0

        def hdu(arr,m,n):

            for i in range(1, m + 1):
                res = -inf
                for j in range(1, n + 1):
                    dp1[j] = max(dp1[j - 1] + arr[j], dp2[j - 1] + arr[j])
                    dp2[j - 1] = res
                    res = max(res, dp1[j])

            return res


        s=hdu(lines,m,n)
        print(s)
        
    except:break






# arr_active=[0,1 ,2 ,-3, 4, 5, -6 ,7]
# m,n=2,7
