#define a list 'x' with numbers
x=[2, 5,16,7,89,15,30,24]
#Create a recursive function to add the elements in the list
def recursive_add(x):
   if len(x)==0:
      return 0
   else:
      return x[0]+ recursive_add(x[1:])
total=recursive_add(x)
print(total)
""" 
 Alternatively; 
    a)Add the elements in the list using the sum() function
   sum(x)

   b)Iterate through the list using a for loop
   total=0
   for i in x:
       total+=i
       print(total)
"""