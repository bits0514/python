def firstrepeatingno(arr):
    n=len(arr)
    for i in range(n):
        j=i+1
        while j<n:
            if arr[i]==arr[j]:
                break
            j=i+1
        if j==n:
            return arr[i]
    return 0
    
arr=[1,2,4,1,6,2,6,2,1]
print(firstrepeatingno(arr))
