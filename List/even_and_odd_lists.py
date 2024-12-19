a= []

for i in range(1,21):
    
    a= a+[i]

print(a)
even = []
odd = []

for i in a :
    if i%2 ==0 :
        even = even +[i]  # or even.append(i)
    else:
        odd = odd + [i]    # or odd.append(i)

print(even)
print(odd)

