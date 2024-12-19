a= []

for i in range(1,11):
    a.append(i)

b = [i for i in a  ]
# print(b)

even = [i for i in a if i%2==0]

odd = [i for i in a if i%2 != 0]

print(even)
print(odd)

two = [i+1 for i in a]
print(two)