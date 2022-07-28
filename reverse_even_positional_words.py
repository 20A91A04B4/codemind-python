n=input().split()
for i in range(len(n)):
    if i%2==0:
        n[i]=n[i][::-1]
print(" ".join(n))