#  palindrome of a number
number = int(input("enter the number to check  : "))
temp = number 

result = 0 

if number < 10 and number >0 :
    print("given number is palindrome")
elif number == 0 :
    print("enter a valid number")
else :
    while temp>0 :
        last_digit = temp % 10
        result = (result * 10) + last_digit
        temp = temp // 10 

    if result == number :
        print("given number is palindrome")
    else :
        print("given number is not a palindrome")