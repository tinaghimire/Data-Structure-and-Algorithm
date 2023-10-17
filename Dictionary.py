# Empty dictionary
my_empty_dictionary = {}

# Dictionary with items
my_food_menu = {
    'Momo' : 200,
    'Pizza' : 450,
    'Sausage' : 50, 
}

# print items
print(my_food_menu['Momo'])
print(my_food_menu['Sausage'])

# Get displays None if the key doesnot exist
print(my_food_menu.get('Momo'))

# Get all items -- Show complete dictionary
print(my_food_menu.items())

# Get keys only
print(my_food_menu.keys())

# Get values only
print(my_food_menu.values())

# Insert elements
my_food_menu['Burger'] = 220
print(my_food_menu.items())

# Modify elements
my_food_menu['Burger'] = 400
print(my_food_menu.items())

# Iterate within dictionary elements
for key, value in my_food_menu.items():
    print(f"\nKey : {key}")
    print(f"Value : {value}")

# Iterate only key 
for item in my_food_menu:
    print(item)

# Iterate only values
for price in my_food_menu.values():
    print(price)
    
# Delete a key-value pair
del my_food_menu['Pizza']

# Empties a dictionary
my_food_menu.clear()

# Delete whole dictionary 
del my_food_menu

