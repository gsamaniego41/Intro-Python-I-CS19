"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %1.2f, z is "%s"' % (x, y, z))
# https://pyformat.info/
# https://www.programiz.com/python-programming/string

# Use the 'format' string method to print the same thing
print('x is {0}, y is {1:.3g}, z is "{2}"'.format(x, y, z))
# https://stackoverflow.com/questions/2389846/python-decimals-format

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y: .2f}, z is "{z}"')
# https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings/45310389
# https://realpython.com/python-f-strings/
