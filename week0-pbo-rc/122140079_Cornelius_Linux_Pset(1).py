height = int(input("Input Height: "))

much_spaces = height-1
much_stars = 1

for i in range(height):
    print(f"{' ' * much_spaces}{'*' * much_stars}")
    much_spaces -= 1
    much_stars += 2