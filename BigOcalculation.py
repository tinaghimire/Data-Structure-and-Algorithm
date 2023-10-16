colors = ['green', 'blue', 'pink', 'black', 'white']  # O(1), n=5
other_colors = ['orange','brown', 'purple'] # O(1), m=3

def complex_algorithm(colors):
    color_count = 0                 # O(1)

    for color in colors:
        print(color)                # O(n) == O(5)
        color_count += 1            # O(n) == O(5)

    for other_color in other_colors:
        print(other_color)          # O(m) == O(3)
        color_count += 1            # O(m) == O(3)

    print(color_count)              # O(1)

    complex_algorithm(colors)       # O(4 + 2n + 2m) ===> O(n + m) ===> O(n)

