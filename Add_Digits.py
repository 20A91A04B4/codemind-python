n=int(input())
s=0
while n!=0:
    s=s+(n%10)
    n=n//10
    if s>9:
        if n==0:
            n=s
            s=0
print(s)