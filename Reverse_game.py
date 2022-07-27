n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    h=i
    s=0
    while h!=0:
        r=h%10
        s=s*10+r
        h=h//10
    j.append(s)
print(*j)
        
    