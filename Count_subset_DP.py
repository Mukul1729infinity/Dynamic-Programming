def count_of_subset(arr,n,sum1):
    t=[[False for i in range(sum1+1)] for j in range(n+1)]
    
    for i in range(n+1):
        t[i][0]=True
    
    for i in range(1,sum1+1):
        t[0][i]=False
    
    for i in range(1,n+1):
        for j in range(1,sum1+1):
            if arr[i-1] > j:
                t[i][j]=t[i-1][j]
            elif j>= arr[i-1]:
                t[i][j]=t[i-1][j] + t[i-1][j-arr[i-1]]
    return t[n][sum1]
