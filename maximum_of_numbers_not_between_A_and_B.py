n=int(input())
l=list(map(int,input().split()))
m,k=map(int,input().split())
j=[]
for i in range(n):
    if not(m<=l[i]<=k):
        j.append(l[i])
if len(j)!=0:
    print(max(j))
else:
    print('-1')