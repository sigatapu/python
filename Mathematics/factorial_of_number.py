number = int(input("enter the number for factorial : "))

result = 1
i=1 

if number ==0 :
    print(1)
else :
    while i<=number :
        result = result*i 
        i=i+1 

    print(result)    