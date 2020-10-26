def mintrip(weight,n):
    trip=0
    left_index=0
    weight.sort()
    for i in range(n-1,-1,-1):
        if weight[i] > 1.99:
            trip+=1
        elif weight[i] <= 1.99:
            if weight[i]+weight[left_index] <=3.0:
                left_index+=1
            trip+=1
        if left_index >= i:
            break
            
    return trip
    
