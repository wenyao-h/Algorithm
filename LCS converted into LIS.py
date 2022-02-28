from bisect import bisect_left
ssn=[]
while True:
    try:
        lines=[]
        lines=list(map(str,input().split(" ")))
        ssn.append(lines)
    except:break

a=ssn[0]
b=ssn[1]   

#转化为LIS
def longestCommonSubsequence(text1, text2):
    arr=[]
        #先找出text2在text1中相同的元素的下标
    for i in range(len(text2)):
        for j in range(len(text1)):
            if text1[i]==text2[j]:
                arr.append(j)
                continue
    #LIS
    l=[]
    for num in arr:
        insertion_pos = bisect_left(l, num)
            
        if insertion_pos == len(l):
            l.append(num)
        else:
            l[insertion_pos] = num
    return len(l)



a=[6,10,1,4,3,8,5,7,2,9]
b=[7,9,2,10,4,6,3,1,8,5]

#7 9 8 1  3 0 4 2 5 6
#5 3  7 4 6 8 9 0 2 1

# 2 1 1 1 1 1
# 1 2 1 4 5 6
# 1 0 



s=longestCommonSubsequence(a,b)
print(s)