# W = capacity of the bag
def knapsack(W,wt,val,n):
    
    #base cond
    # if donot have any element 
    if n==0 or W==0:
        return 0
    
    # if wt of item is > capacity of bag
    if wt[n-1] > W:
        return knapsack(W,wt,val,n-1)
    else:
        return max(val[n-1] + knapsack(W-wt[n-1],wt,val,n-1),knapsack(W,wt,val,n-1))
 ----------------------------------------------------------------------------------------
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
print(knapsack(W,wt,val,n))
