n=int(input())
l=list(map(int,input().split()))
s=0
k=[]
for i in l:
    if i%2 and i not in k:
        k.append(i)
        s=s+i
print(s)
