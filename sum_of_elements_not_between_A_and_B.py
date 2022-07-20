n=int(input())
l=list(map(int,input().split()))
m,k=map(int,input().split())
j=[]
for i in range(n):
    if not(m<=l[i]<=k):
        j.append(l[i])
print(sum(j))

        