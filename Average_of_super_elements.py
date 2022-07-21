n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if l.count(i)==i and i not in k:
        k.append(i)
if len(k)==0:
    print('-1')
else:
    s=sum(k)
    avg=s/len(k)
    print("%0.2f"%avg)
        
