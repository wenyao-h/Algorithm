def hanoi(n,a,b,c):#上文中的状态0，表示把a上的n个盘子移动到c上，其中可以用到b
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)#把A上的n-1个移动到B，操作结束为状态1；看函数定义，此时c是工具人，b是目标
        print(a,'-->',c)#把A上的大盘子移动到C
        hanoi(n-1,b,a,c)#把B上的n-1移动到C，操作结束位状态2，和状态1相比只是规模变小

hanoi(3,"a","b","c")
