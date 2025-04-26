# recursive function to add the digits of a number using recursion
def add(n):
    if n == 0:
        return 0 #Base case
    else:
     return (n % 10) + add(n // 10) #Recursive case

n=int(input("Enter a long number(e.g 12345:"))
print(add(n))
