import math
def isprime(n):
    sqrt=int(math.sqrt(n))+1
    for i in range(3,sqrt,2):
        if n % i ==0:
            return False
    return True


t=int(input())
prime_list=[]
prime_list.append(2)
for i in range(3,1000000,2):
    if isprime(i):
        prime_list.append(i)


while t != 0:
    x,y,m=list(map(int,input().split(' ')))
    floor=math.gcd(x,y)
    x_factor=int(x/floor)
    y_factor=int(y/floor)
    time=0
    for i in range(0,m):
        pn=prime_list[i]
        if pn >= m:
            break
        
        while (x_factor % pn == 0):
            x_factor=int(x_factor/pn)
            time+=1
            
        while (y_factor % pn ==0):
            y_factor=int(y_factor/pn)
            time+=1
        
        if x_factor ==1 and y_factor==1:
            break
    if x_factor ==1 and y_factor ==1:
        print(str(time),floor)
    else:
        print(-1)
    t-=1
