number = int(input("enter the digit to count : "))

count = 0 

temp = number


if number > 0:
    while temp > 0:
        count = count + 1

        temp = temp // 10
      #should use double slash(//) for division in python 

    print(count)

else:
    print(1)