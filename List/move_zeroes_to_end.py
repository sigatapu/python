a=[]

for i in range(0,5):
    b = int(input())
    a.append(b)
count = 0    

l=len(a)
b=[]
i=0 
count = 0
while i<l:
    if a[i]!=0:
        b.append(a[i])
    if a[i]==0:
        count = count+1
    i=i+1

for i in range(0,count):
    b.append(0)    

print(b)







