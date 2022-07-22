n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    if i%2==0 and i not in j:
        j.append(i)
print(len(j))