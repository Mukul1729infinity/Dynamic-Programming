# gobal arr having all element -1
t=[[-1 for i in range(W+1)] for j in range(n+1)]
def M_knapsack(wt,val,W,n):
    # base class
    if n==0 or W==0:
        return 0
    
    if t[n][W] != -1:
        return t[n][W]
    
    # choice diagram
    if wt[n-1] <= W:
        t[n][W]= max(val[n-1]+M_knapsack(wt,val,W-wt[n-1],n-1),M_knapsack(wt,val,W,n-1))
        return t[n][W]
    
    # if wt of element > then the capacity then it cannot contaon any element
    elif wt[n-1] > W:
        t[n][W]=M_knapsack(wt,val,W,n-1)
        return t[n][W]
    ----------------------------------------------------------------------------------------
val=[10,20,15,25]
wt=[10,5,8,15]
W=20
n=len(val)
print(M_knapsack(wt,val,W,n))
