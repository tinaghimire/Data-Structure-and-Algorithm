# Example of Nested Dictionary

my_friends = {
    'Lonika' : {
        'Age' : 21,
        'Study' : 'Lawyer',
    },
    'Molina' : {
        'Age' : 22,
        'Study' : "MBBS",
    },
}

print(my_friends['Lonika'])
print(my_friends['Lonika']['Age'])

for friend, detail in my_friends.items():
    print(f"The details of {friend.title()} are \nAge: {detail['Age']} and \nStudy: {detail['Study']} \n")
