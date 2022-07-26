n=int(input())
l=list(map(int,input().split()))
e=[]
c=0
for i in range(len(l)):
    h=l[i]
    s=0
    
    while h>0:
        r=h%10
        s=s*10+r
        h=h//10
    e.append(s)
    if e[i]==l[i]:
     c+=1
print(c)
