#tar=input().split()
#pat=input().split()

def compute_next(p):
    m=len(p)
    next=[0 for i in range(m)]

    i=0
    j=1
    #list_i=[0]
    #list_j=[1]
    while j<=(m-1):
        if p[i]==p[j]:
            next[j]=i+1
            i+=1
            j+=1
            #list_i.append(i)
            #print('MATCH ','i: ', i,'j: ', j)
            
        else:
            if i==0:
                #next[j]=0
                j+=1
            else:
                i=next[i-1]
                
            #list_i.append(i)
            
            #print('UNMATCH ','i: ', i,'j: ', j)
            #因为initial时让next先全部为零了，
            #这里next[j]相当于为0了
        
        #list_j.append(j)
    
    #return list_i,list_j,next
    return next

#compute_next(list('abababca'))
#compute_next(list('ababbabbabbababbabb'))

def KMP(t,p):
    
    #print(next)
    next=compute_next(p)
    q=0 #number of characters matched so far
    pos=0 #position marker in T

    while pos<=len(t):
        #loop until a match is found
        #or the matched is 0
        while q>0 and p[q]!=t[pos]:
            q=next[q-1]
            #print('UNMATCH ','pos: ', pos,'q: ', q)
        #q=0时啥也没办法干，只能退出这个loop，加上pos
        #print('HERE ','pos: ', pos,'q: ', q, 'p[q]: ',p[q], 't[pos]: ',t[pos])
        if p[q]==t[pos]:
            q+=1
            #print('MATCH ','pos: ', pos,'q: ', q)
        #上面q=0但是仍不相等也可以退出循环，因此这里必须要加条件
        
        if q==len(p):
            return pos-len(p)+1
        
        pos+=1
        if pos==len(t):
            return -1

    


tar=list('abcdefg')
pat=list('hijk')
KMP(tar,pat)
        


tar=list('abcabcabdabba')
pat=list('abcabd')
KMP(tar,pat)

next=compute_next(pat)
pos=0
q=0
while pat[q]!=tar[pos]:
    if q>0:
        q=next[q-1]
    else:q=0


            
print(KMP(tar,pat))


class Solution:
    def strStr(self, haystack, needle):
        a, b = len(needle), len(haystack)
        if a == 0: return 0
        # 1、求next数组
        nxt = self.getnext(needle)
        # 2、模式匹配
        p = -1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = nxt[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1
    # 求next数组
    def getnext(self, needle):
        nxt = [-1] * len(needle)
        j = -1
        for i in range(1, len(needle)):
            while (j >= 0 and needle[j+1] != needle[i]):
                j = nxt[j]
            if needle[j+1] == needle[i]:
                j += 1
            nxt[i] = j
        return nxt
