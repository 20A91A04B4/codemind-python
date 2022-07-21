n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    if i not in j:
        j.append(i)
k=sum(j)
print(k)