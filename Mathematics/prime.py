# Number which is divisible by one and itself is called prime number

number = int(input())

i = 1 
count = 0 

if number == 0 or number == 1 :
    print("enter a valid number")
else:
    while i <= number:
        if number%i ==0 :
            count = count+1 
        i = i+1 

    if count == 2 :
        print("given number is prime")        
    else:
        print("given number is not prime")    
    