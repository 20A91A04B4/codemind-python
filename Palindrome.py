n=int(input())
s=0
k=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if s==k:
    print('True')
else:
    print('False')