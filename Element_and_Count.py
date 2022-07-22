n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    if i not in j:
        j.append(i)
for k in j:
    print(k,l.count(k),end=' ')