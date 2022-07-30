m=int(input())
n=int(input())
j=[]
k=[]
for i in range(1,(m//2)+1):
    if m%int(i)==0:
        j.append(int(i))
        i+=1
for t in range(1,(n//2)+1):
    if n%int(t)==0:
        k.append(int(t))
        t+=1
h=sum(j)
r=sum(k)
if h==n:
    print('Amicable')
else:
    print('Not Amicable')
        