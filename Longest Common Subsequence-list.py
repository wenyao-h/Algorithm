ssn=[]
while True:
    try:
        lines=[]
        lines=list(map(str,input().split(" ")))
        ssn.append(lines)
    except:break

a=ssn[0]
b=ssn[1]   

class Solution(object):
    def longestCommonSubsequence(self, list1, list2):

        m=len(list1)
        n=len(list2)
        c=[[0]*(n+1) for i in range(m+1)]
        lcs=[]
        #生成(m+1)*(n+1)矩阵，要考虑0到n / 0到m；
        #c[i,0],c[0,j]自动为零，无需讨论

        for i in range(1,m+1):
            for j in range(1,n+1):
                if list1[i-1]==list2[j-1]:
                    c[i][j]=c[i-1][j-1]+1
                    
                else:
                    c[i][j]=max(c[i-1][j],c[i][j-1])
        return c[m][n]


lcsc=Solution()
s=lcsc.longestCommonSubsequence(a,b)
print(s)