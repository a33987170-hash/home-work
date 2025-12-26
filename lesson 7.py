#def count(a,b):
    #return a+b
#print(count(1,3))


#def even_or_odd(a):
    #if a % 2 == 0:
        #return "even"
    #else:
        #return "odd"
#print(even_or_odd(7))

#def max_number(a,b):
    #if a > b:
        #return "a > b"
    #else:
        #return "a < b"
#print(max_number(5,9))



def arr_sum(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result 

mass = [1,2,3,4,-8]
print(arr_sum(mass))
        




