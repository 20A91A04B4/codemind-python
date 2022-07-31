n=int(input())
j=[]
for i in range(1,n):
    if n%i==0 and i not in j:
        j.append(i)
    i+=1
x=sum(j)
if x>n:
    print('True')
else:
    print('False')
    
    