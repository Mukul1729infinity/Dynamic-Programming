def rod(price,length,N,n):
    t=[[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == 0 or j ==0:
                t[i][j]=0
            elif length[i-1] <= j:
                t[i][j]=max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])        
            else:
                t[i][j]=t[i-1][j]
    return t[N][N]
                    
testcase=int(input())
for _ in range(testcase):
    N=int(input())
    price=list(map(int,input().split()))
    n=len(price)
    length=[int(i) for i in range(1,n+1)]
    print(rod(price,length,N,n))
