try:
    num1 = int(input("Enter a uumber"))
    num2 = int(input("enetr a umber"))
    esult = num1/num2
    print("resut is : ", result)
    print("resut is : ", result1)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("please enter numerical value")
except NameError as ex :
    print("the exception is" ,ex)

except:
    print("some error occured")
finally:
    print("i will execute no matter what happens")


    