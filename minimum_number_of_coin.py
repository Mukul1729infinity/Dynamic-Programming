import sys
def minCoin(coin,n,S):
    t=[0 for i in range(S+1)]
    t[0]=0
    for i in range(1,S+1):
        t[i]=sys.maxsize
    
    for i in range(1,S+1):
        for j in range(n):
            if coin[j] <= i:
                sub_res=t[i-coin[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < t[i]):
                    
                    t[i]=sub_res + 1
    return t[S]
