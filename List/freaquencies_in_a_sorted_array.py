# freaquencies in a array means how many times each number is there in the list 
a = [1,1,2,2,2,3]
b= list(set(a))
# print(b)

lb = len(b)
la = len(a)

i=0 

while i<lb:
    count = 0 
    j=0 
    while j<la:
        if b[i]==a[j]:
            count = count + 1
        j=j+1 
    print(str(b[i]) +" occured "+str(count)+" times")
    i=i+1        