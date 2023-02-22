def heapify(arr,n,i):
    lg=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]<arr[l]:
        lg=l
    if r<n and arr[i]<arr[r]:
        lg=r

    if lg !=i :
        arr[i],arr[lg]=arr[lg],arr[i]
        heapify(arr,n,lg)

def heapsort(arr):
    n=len(arr)
    for  i in range (n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range (n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr    


a=[12,5,1,6,11]
print(heapsort(a))