n=int(input())
l=list(map(int,input().split()))
j=[]
c=0
d=0
for i in range(n-2):
    if l[i]<l[i+1]>l[i+2]:
        c+=1
    elif l[i]>l[i+1]<l[i+2]:
        c+=1
    else:
        d=1
if d==1:
    print('no')
else:
    print('yes')
    
        
        
        