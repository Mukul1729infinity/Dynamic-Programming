def Dp_knapsack(W,wt,val,n):
    t=[[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            
            # base cond
            if i==0 or j==0:
                t[i][j]=0
            # choice diagram item weight < capacity    
            elif wt[i-1] < W:
                t[i][j]=max(val[i-1] + t[i-1][j - wt[i-1]] , t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W]
    ----------------------------------------------------------------------
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(Dp_knapsack(W, wt, val, n)) 
