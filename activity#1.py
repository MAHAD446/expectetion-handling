# using a try and expect
try:
    number = int(input("enter a number:"))
    print("the number entered is", number)
#using value error"
except ValueError as ex:

   print("Exception:",ex)