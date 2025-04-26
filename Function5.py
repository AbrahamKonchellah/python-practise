#Create a function reverse_string that takes in a text parameter
def reverse_string(text):
    reversed_text = ""  #Create an empty string reversed_string to store the reversed text
    for i in range(len(text)-1, -1, -1): #use a for loop that counts backwards through the string
        # starting from the last character until before the first character and counting down by 1
        reversed_text += text[i]
    return reversed_text

eg= "hello"
result = reverse_string(eg)
print(result)