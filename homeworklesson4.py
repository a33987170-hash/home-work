users_result_test = int(input("введіть свій результат тесту "))

if users_result_test > 90:
    print("ваш результат А ")

elif users_result_test > 80:
    print("твій результат B ")

elif users_result_test > 70:
    print("твій результат  C ")

elif users_result_test > 60:
    print("твій результат D ")

elif users_result_test > 0 < 50:
    print("твій результат  F")    

else:
    print("Invalid")    
