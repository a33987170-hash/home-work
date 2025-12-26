
arr3 =[]
arr2 = []
arr = [1,2,3,4,-11,5,-7,-123,10,-15]
count_1_arr2 = 0
count_0_arr2 = 0
sum_count = 0
negative = 0
positif = 0

for x in arr:
    if x > 0:
        arr2.append(1)
    else:
        arr2.append(0)
    
for x in arr:
    sum_count += x

for x in arr:
    if x  > 0:
        positif += 1
    else:
        negative +=1

for x in arr2:
    if x >= 1:
        count_0_arr2 += 1
    else:
        count_1_arr2 += 1    

for x in arr2:
    if x > 0:
        arr3.append(0)
    else:
        arr3.append(1)

print(f""arr3)       
print(negative)        
print(positif)
print(sum_count)   
print(arr2)    
print(count_1_arr2)    
print(count_0_arr2)