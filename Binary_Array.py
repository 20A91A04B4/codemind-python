n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    a=l.count(0)
    b=l.count(1)
if n==a+b:
    print('True')
else:
    print('False')
       