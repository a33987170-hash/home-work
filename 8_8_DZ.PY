#def sum_list(lst):
    #total = 0
    #for x in lst:
        #total += x
    #return total

#def unique_element(nums):
    #unique = []
    #for x in nums:
        #if x not in unique:
            #unique.append(x)
    #return unique

#def combine_lists(a, b):
    #return a + b


#def max_number(a,b):
    #if a > b:
        #return "a > b"
    #else:
        #return "a < b"
#print(max_number(7,9))

#def even_or_odd(a):
    #if a % 2 == 0:
        #return "even"
    #else:
        #return "odd"
#print(even_or_odd(7))












#def factorial(n):
    #if n < 1:
        #return n
    #return n * factorial(n-1)
#print(factorial(5))



#def fibonacci(n):
    #if n <= 1:
        #return n
    #return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(900))

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))  # 10
