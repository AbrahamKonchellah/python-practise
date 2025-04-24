#Define a function that takes a number from a user
def check_number():
  num=int(input("Enter a number:"))
#Check whether the number is odd or even using a conditional if statement
  if num%2!=0:
       print("The number is odd")
  else:
        print("The number is even")


check_number()