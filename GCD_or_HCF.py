m,n=map(int,input().split())
k=max(m,n)
while True:
    if m%k==0 and n%k==0:
        print(k)
        break
    k-=1
    