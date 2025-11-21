#server_pasword = "1234567g"
#server_username = "Python123"




#user_pasword = str(input("введіть пароль "))
#user_username = str(input("введіть логін " ))
#if user_username == server_username and user_pasword == server_pasword:
    #print("ви ввійшли в систему")
#else:
    #print("введіть знову")




#gost_name = str(input("введіть свое ім'я "))

#if gost_name == "Іван":
    #print("вас немае в списку гостей")
#elif gost_name == "Марія":    
    #print("вас немае в списку гостей")
#else:
    #print("ви е в списку  гостей проходьте")


number1 = int(input("введіть перше число "))   
option = str(input("вибиріть дію "))
number2 = int(input("введіть друге число "))
if option == "+" :
    print(number1 + number2)

elif option == "-":
    print(number1 - number2)

elif option == "*":
    print(number1 * number2)

elif option == "/":   
    print(number1 / number2)

else:
    print("такого знака не має")
