# Prime factors of a given number
number = int(input())

i = 2

while i <= number:
    if number % i == 0:
        j = 1
        count = 0
        while j <= i:
            if i % j == 0:
                count = count + 1
            j = j + 1
        if count == 2:
            print(i)
    i = i + 1
