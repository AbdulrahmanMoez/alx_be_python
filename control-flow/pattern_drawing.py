square_size = 1

while square_size >= 1:
    square_size = int(input("Enter the size of the pattern: "))
    for num in range(square_size):
        print( "****", end="")
        print()
