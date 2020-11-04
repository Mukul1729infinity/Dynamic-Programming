def findpart(arr,n):
    sum1=sum(arr)
    if sum1 % 2 !=0:
        return False
    t=[[True for i in range(sum1//2+1)] for j in range(n+1)]
    
    for i in range(n+1):
        t[i][0]=True
    
    for i in range(1,sum1//2+1):
        t[0][i]=False
        
    for i in range(1,n+1):
        for j in range(1,sum1//2+1):
            t[i][j]=t[i-1][j]
            if j >= arr[i-1]:
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
    return t[n][sum1//2]
            
