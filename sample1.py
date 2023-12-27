"""
Module with a function that adds numbers
"""
def add(number1, number2):
    '''
    This functions adds two numbers and returns the value
    '''
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f'The sum of {NUM1} and {NUM2} is {TOTAL}')
