#try:
    #a = 5
    #b = 2 
    #print(a/b)
#except  ZeroDivisionError:
    #print("на нуль ділити не можна")   

try:
    a = int(input("введіть перше число "))
    b = int(input("введіть перше число "))
    option = str(input("виберіть дію "))
    if option == "*":
        print(a*b)
    elif option == "/":
        print(a/b)   
    elif option == "-":
        print(a-b)
    elif option == "+":
        print(a+b)

except  ZeroDivisionError:
    print("на нуль ділити не можна")  
except ValueError:
    print("введіть цифри")   
finally:
    print("Я відпрацював")

