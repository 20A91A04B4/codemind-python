n=int(input())
k=0
while n!=1:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    else:
        k=1
        break
if k==1:
    print('Not Ugly Number')
else:
    print('Ugly Number')
    
        
                    
        