# sieve of eratosthenes means nothing but printing all the prime numbers in the range of given number

number = int(input())

i =2 


while i<=number:
    j=1 
    count =0 
    while j<=i:
        if i%j == 0:
            count = count+1 
        j = j + 1

    if count == 2:
        print(str(i),end=" ")        



    i=i+1