n = int(input())
x=0
seq=[None] * n
x=0
maio=0
men=500
resp=0
while(n > x):
    seq[x]= int(input())
    x+=1
x=0
for x in range(n):
    if seq[x]>maio:
        maio=seq[x]
    if seq[x]<men:
        men=seq[x]
for x in range(n):
    if seq[x]==maio:
        resp+=1
        if seq[x-1]==seq[x] and n!=1:
            resp-=1
    elif seq[x]==men:
        resp+=1
        if seq[x-1]==seq[x] and n!=1:
            resp-=1
print(resp)