n=input()
v='aeiouAEIOU'
j=[]
for i in n:
    if i in n and i in v:
        if i not in j:
            j.append(i)
print(*j)