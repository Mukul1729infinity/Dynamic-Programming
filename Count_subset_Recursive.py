def count_subset(arr,n,sum1):
    if sum1 == 0:
        return 1
    if n==0 :
        return 0
    if arr[n-1] > sum1:
        return count_subset(arr,n-1,sum1)
    return count_subset(arr,n-1,sum1)+count_subset(arr,n-1,sum1-arr[n-1])
arr = [ 3, 3, 3, 3 ];  
n = len(arr)
sum1 = 6
print(count_subset(arr,n,sum1))
