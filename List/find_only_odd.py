a=[]
for i in range(1,11):
    a.append(i)
# print(a)    
b = [i for i in a if i%2 != 0]
print(b)