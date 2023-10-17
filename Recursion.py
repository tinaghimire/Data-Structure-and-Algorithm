# Without recursion
def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result

print(factorial(5))

# With recursion
def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursion(n-1)

print(factorial_recursion(5))

# Fibonacci series
def fibonacci(n):
  # Define the base case
  if n <= 1:
    return n
  else:
    # Call recursively to fibonacci
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

cache = [None]*(100)
def fibonacci(n): 
    if n <= 1:
        return n
    
    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]
print(fibonacci(6)) 
    
# Tower of hanoi
def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks <= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)