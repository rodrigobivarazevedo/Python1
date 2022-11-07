def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()


def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()



def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()

#Notice that we have an outer loop addresses each row in the square. 
# Then, we have an inner loop that prints a brick in each row. 
# Finally, we have a print statement that prints a blank line.

# We can further abstract away our code:

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
            