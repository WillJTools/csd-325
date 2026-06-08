# William Judd
# CSD-325 Advanced Python
# Module 1.3 Assignment
# Assignment: On the Wall 
# 6-8-2026
# This program asks the user how many bottles of beer are on the wall.



def countdown_bottles(bottles):
    """Print the bottle countdown lyrics from the user's number down to 1."""
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around,")
        bottles -= 1

        if bottles == 1:
            print("1 bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around,")
    print("No more bottles of beer on the wall.\n")


def get_bottle_count():
    """Ask the user for a positive whole number and return it as an integer."""
    while True:
        user_input = input("How many bottles of beer are on the wall? ")

        try:
            bottles = int(user_input)

            if bottles < 1:
                print("Please enter a number greater than zero.\n")
            else:
                return bottles

        except ValueError:
            print("Please enter a valid whole number.\n")


def main():
    """Run the main program."""
    bottles = get_bottle_count()
    countdown_bottles(bottles)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
