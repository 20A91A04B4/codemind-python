n,k=map(int,input().split())
l=list(map(int,input().split()))
j=[]
c=0
for t in l:
    if len(str(abs(t)))==k:
        c+=1
print(c)
