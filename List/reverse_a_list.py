a=[1,2,3,4,5,6,7,8,9,10]

# print(a[::-1])  #we can write like this without using loops or anythng extra

l=len(a)-1
b=[]

i=l
while i>=0:
    b.append(a[i])
    i=i-1


print(b)    
