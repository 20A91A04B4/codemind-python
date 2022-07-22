n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
for i in range(n):
    if a<=l[i]<=b:
        p.append(l[i])
m=sum(p)
print(m)