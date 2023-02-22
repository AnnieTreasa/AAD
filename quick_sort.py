
def partition(a,s,e):
    i=s-1
    p=a[e]

    for j in range(s,e):
        if(a[j]<=p):
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[e]=a[e],a[i+1]
    return (i+1)

def quick(a,s,e):
    if(s<e):
        p=partition(a,s,e)
        quick(a,s,p-1)
        quick(a,p+1,e)  
    return a              

a=[6,4,3,7,5]
print(quick(a,0,len(a)-1))    