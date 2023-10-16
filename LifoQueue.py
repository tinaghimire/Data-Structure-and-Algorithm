import queue

my_stack = queue.LifoQueue(maxsize=0)
my_stack.put("Mt. Everest")  # Push operation
my_stack.put("Nepal")

print("The size is: ", my_stack.qsize())

print(my_stack.get())  # Pop operation
print(my_stack.get())

print("Empty stack: ", my_stack.empty())  # True
my_stack.put("Mt. Everest")
print("Empty stack: ", my_stack.empty())  # False


