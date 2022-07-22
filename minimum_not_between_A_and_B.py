n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
j=[]
for i in range(n):
    if a<=l[i]<=b:
        p.append(l[i])
    else:
        j.append(l[i])
if len(j)!=0:
    e=min(j)
    print(e)
else:
    print('-1')
