# Leaders in the array

a = [1, 2, 3, 4, 5, 2]

result = []

temp = 0
l=len(a)
i=0 

while i<l-1:
    con = True
    j=i+1 
    while j<l:
        if a[i]<a[j]:
            con = False 
        j=j+1 
    if con == True :
        result.append(a[i])
    i=i+1 


result.append(a[l-1])    
print(result)            

