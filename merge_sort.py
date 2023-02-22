# Merge Sort
def merge_sort(a):
    if len(a)>1:
        mid =len(a)//2
        l=a[:mid]
        r=a[mid:]

        merge_sort(l)
        merge_sort(r)

        i=j=k=0

        while i<len(l) and j<len(r):
            if l[i] <= r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j +=1
            k+=1 

        while i<len(l):
            a[k] = l[i]
            i+=1
            k+=1

        while j<len(r):
            a[k] = r[j]
            j+=1
            k+=1            
    return a

a=[8,6,10,5,3]    
print(merge_sort(a))