n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    for s in str(abs(i)):
        e=len(str(abs(i)))
        j.append(e)
        break
print(*j)
    