# the result of both gcd and hcf are same.
# so this single code is enough for both of them

first_number = int(input())
second_number = int(input())



gcd_and_hcf = 0 

if first_number < second_number :
    loop = first_number
else:
    loop = second_number

# print(loop)

i =1 

while i<=loop:
    if (first_number%i == 0) and (second_number%i==0):
        gcd_and_hcf = i 
    i=i+1 

print(gcd_and_hcf)        