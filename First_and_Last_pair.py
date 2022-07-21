n=int(input())
l=list(map(int,input().split()))
j=[]
i=0
while i!=n//2:
    j.append(l[i])
    j.append(l[(n-1)-i])
    i+=1
if len(l)%2:
    j.append(l[i])
    j.append(0)
print(*j)

