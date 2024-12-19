# simple formula for finding lcm is :
        
#                                  "LCM(a, b) = (a × b) / GCF(a, b)"

first_number = int(input())
second_number = int(input())

if first_number < second_number :
    loop = first_number
else:
    loop = second_number


gcf = 0 

i = 1 
while i<=loop :
    if(first_number%i==0) and (second_number%i==0):
        gcf = i 
    i = i+1 

# print(gcf)        \

lcm = (first_number * second_number)/gcf 

print(int(lcm))