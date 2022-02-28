from bisect import bisect_left
ssn=[]
while True:
    try:
        lines=[]
        lines=list(map(int,input().split(" ")))
        ssn.append(lines)
    except:break


def LIS(arr):
    l=[]
    for num in arr:
        insertion_pos = bisect_left(l, num)
        #binary sort
        #返回插入num的位置，如果插入在最后，就加入队列l中    
        if insertion_pos == len(l):
        #index是自然数-1，如果l没有东西，刚好是插入num的index（即是0）
            l.append(num)
        else:
            l[insertion_pos] = num
        #被替换了,这个方法是没有办法返回具体的sequence的
        #如果不替换，对于[9,10,1,2,3,4,5]这种是没法算的
    return len(l)

l_result=LIS(ssn[1])
print(l_result)


nums= [10, 22, 9, 33, 21, 50, 41, 60, 80]
l=[10,22,33,50]
bisect_left(l,41)