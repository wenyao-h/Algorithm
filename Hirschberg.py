def score(x,y,penalty):
    if x==y: return 2
    else: return penalty
    #not x and not y 的情况可能，但是已经被basis解决了

def GA(s,t,penalty):#用s去匹配t
    #Basis
    v=[[0]*(len(t)+1) for _ in range(len(s)+1)] 
    for i in range(len(s)+1):
        v[i][0]=i*penalty
    for j in range(len(t)+1):
        v[0][j]=j*penalty
    
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):            
            v[i][j]=max(v[i-1][j-1], v[i-1][j], v[i][j-1])+penalty
            if s[i-1]==t[j-1]:
                v[i][j]=v[i-1][j-1]+2
                print('HRER')
            print("i: ",i, 'j: ',j,'[',s[i-1],t[j-1],']', "v[i][j]: ", v[i][j])
    print(v)
    return v[-1][-1]

def forward(s,t,penalty):
    v=[[0]*(len(t)+1) for _ in range(len(s)+1)] 
    for i in range(len(s)+1):
        v[i][0]=i*penalty
    for j in range(len(t)+1):
        v[0][j]=j*penalty
    
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            
            v[i][j]=max(v[i-1][j-1]+score(s[i-1],t[j-1],penalty), v[i-1][j]+penalty, v[i][j-1]+penalty)
        #Clear Memory
        v[i-1]=[]
    return v[len(s)]



def backward(s,t,penalty):
    v=[[0]*(len(t)+1) for _ in range(len(s)+1)] 
    for i in range(len(s)+1):
        v[i][0]=i*penalty
    for j in range(len(t)+1):
        v[0][j]=j*penalty
    
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            
            v[i][j]=max(v[i-1][j-1]+score(s[len(s)-i],t[len(t)-j],penalty), v[i-1][j]+penalty, v[i][j-1]+penalty)
        #Clear Memory
        v[i-1]=[]
    return v[len(s)]


def DP(s,t,penalty):
    #print("s: ",s, "t: ",t)
    if len(s)<=1 or len(t)<=1:
        #print('len(s): ',len(s),'len(t): ',len(t))
        return GA(s,t,penalty)
    else:
        mid=len(s)//2
        #print("mid: ",mid)

        S1=forward(s[:mid],t,penalty) #返回最后一行数
        S2=backward(s[mid:],t,penalty)  #返回reverse的最后一行数

        SCORE_DP=[]
        for j in range(len(t)+1):
            SCORE_DP.append(S1[j]+S2[len(t)-j])
        
        midpoint=SCORE_DP.index(max(SCORE_DP))
    return DP(s[:mid],t[:midpoint],penalty)+DP(s[mid:],t[midpoint:],penalty)

A=list("teacher")
B=list("botcher")

A=list('ACAATCC')
B=list('AGCATGC')

# A=list("horse")
# B=list('ros')

#forward(A,B,-1)
GA(A,B,-1)

RES=DP(A,B,0)-DP(A,B,-1)
RES