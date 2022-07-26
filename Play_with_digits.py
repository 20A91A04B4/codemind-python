n=int(input())
l=list(map(int,input().split()))
num='0123456789'
j=[]
for i in l:
    s=0
    for k in str(i):
        s+=int(k)
    j.append(s)
print(sum(j))
    
        
        
    