n=int(input())
l=list(map(int,input().split()))
j=[]
for i in range(n):
    if l[i]%2==0:
        j.append(l[i])
    else:
        break
print(sum(j))