def subset(set,n,sum):
    if sum ==0 : # base cond when the given sum is 0
        return True
    if n == 0: # base cond when the number of element is zero
        return False

    if set[n-1] > sum: # if element is more than sum 
        return subset(set,n-1,sum)
    
    return subset(set,n-1,sum) or subset(set,n-1,sum-set[n-1])
    ----------------------------------------------------------------------------
set=[3,34,4,12,5,2]
sum=9
n=len(set)
subset(set,n,sum)
