#Get a number from a user
num=int(input("Enter the number:"))
#define a factorial() function that use conditional if to calculate it's factorial
def factorial(num):
    if num==0 or num==1: #Base case
        return 1
    else:
        return num*factorial(num-1)  # Recursive case where the function calls itself
result=factorial(num) # Call the factorial function
print("The factorial of", num, "is", result) # Print out the factorial function