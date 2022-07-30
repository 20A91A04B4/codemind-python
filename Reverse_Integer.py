n=int(input())
s=0
k=n
if n<0:
    n=n*(-1)
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if k<0:
    print(s*(-1))
else:
    print(s)

    
       
