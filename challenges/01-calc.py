# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    calc = input('What calculation would you like to do? (add, sub, mult, div)\n')
    num1 = input('What is number 1\n')
    num2 = input('What is number 2\n')
    if calc == 'add' :
        result = int(num1) + int(num2)
    elif calc == 'sub' :
        result = int(num1) - int(num2)
    elif calc == 'mult' :
        result = int(num1) * int(num2)
    elif calc == 'div' :
        result = int(num1) / int(num2)
    return result
print(calculator())