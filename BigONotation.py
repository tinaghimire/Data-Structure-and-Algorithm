# Mathematical expressions: O(1), O(n), ....

colors = ['green', 'yellow', 'blue', 'pink']

# O(1)
def constant(colors):
    print(colors[2])   # O(1)

constant(colors)  # Prints only the third element

# O(n)
def linear(colors):
    for color in colors:
        print(color)  # O(n) 

linear(colors)  # For n elements, n operations are performed

# O(n2)
def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first, second)

quadratic(colors)

# O(n3)
def cubic(colors):
    for first in colors:
        for second in colors:
            for third in colors:
                print(first, second, third)

cubic(colors)