n=int(input())
l=list(map(int,input().split()))
j=[]
c=0
for i in l:
    if len(str(abs(i)))>0:
        k=len(str(abs(i)))
        j.append(k)
m=max(j)
for t in l:
    if len(str(abs(t)))==m:
        print(t,end=' ')