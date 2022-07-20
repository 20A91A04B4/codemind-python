t,s,b=map(int,input().split())
cap=2*t*b*s*512
ckb=cap//1024
print(ckb,end='KB')