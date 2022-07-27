n=int(input())
l=list(map(int,input().split()))
j=[]
c=0
for i in l:
    if len(str(abs(i)))>0:
        s=len(str(abs(i)))
        j.append(s)
m=max(j)
for t in l:
    if len(str(abs(t)))==m:
        c+=1
print(c)