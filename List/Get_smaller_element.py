a = [2 , 1 ,3 ,4 , 5 ,7 ,9 ,8]

result = a[0]

for i in range (1,len(a)-1):
    if result >a[i]:
        result = a[i]

print(result)

# code using predefined function 

# a.sort()
# print(a[0])