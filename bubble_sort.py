def bubble_sort(ar):
    n= len(ar)
    for i in range(n):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1] :
                ar[j],ar[j+1] = ar[j+1],ar[j]

arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
  
print("Sorted array is:")
for i in range(len(arr)):
      print(arr[i], end=" ")


