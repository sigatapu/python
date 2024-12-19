a = []

for i in range (1,21):
    a.append(i)
  
b = tuple(a)
c = set(a)


print(a[1:4])
print(b[4:7])
# print(c[5:10]) in python cannot slice a set if we want to slice it we need to convert it into list or tuple



# d= dict(a)

# print("this is list ")
# print(a)  

# print("this is tuple")
# print(b)
 
# print("this is set") 
# print(c)

# print("this is dictionary")
# print(d)