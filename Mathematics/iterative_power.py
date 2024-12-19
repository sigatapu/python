# finding power by iterating the loop 

a = int(input("enter number"))
b = int(input("enter power"))

result = a

power = b - 1

i =1 

while i<b :
     result=result*a 
     i=i+1 

print(result)
