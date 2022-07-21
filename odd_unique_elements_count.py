n=int(input())
l=list(map(int,input().split()))
j=[]
c=0
for i in l:
    if i not in j:
        if i%2:
            j.append(i)
            c+=1
print(c)