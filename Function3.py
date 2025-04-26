#Get input, a number , from a user
num=int(input("Enter a number:"))
#Set factorial to 1 since the factorial of 0 is 1
factorial=1
#Use a for loop to iterate through the sequence of numbers that precede the number
for i in range(1,num+1):
    factorial*=i
print("The factorial of ", num, "is", factorial)