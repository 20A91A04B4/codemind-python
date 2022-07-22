n=int(input())
l=list(map(int,input().split()))
k=[]
s=0
for i in l:
    if i%2==0 and i not in k:
        k.append(i)
        s=s+i
print(s)