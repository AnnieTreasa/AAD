# method 1
def missing_no (a):
    n=len(a)
    s=(n+1)*(n+2)/2
    s1=0
    for i in range(n):
        s1+=a[i]
    x=s-s1
    return x

a=[1,2,3,5,6]
print(missing_no(a))        

# method 2
def missing_no2(a,p):
    n=len(a)
    f=[]
    ans=[]
    for i in range(0,n+p):
        f.append(0)
    for i in range(0,n):
        v=a[i]
        f.insert(v,1)
    for i in range(1,n+p):
        if f[i] == 0 :
            ans.append(i)
    return ans

b=[1,2,3,4,7]    
p=missing_no2(b,2)   
print(p)