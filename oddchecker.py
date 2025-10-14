#Even and odd number checker Beginner
def check():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print(f"The number {number} is Even ")
            else:
                print(f"The number {number} is Odd")

            again = input(
                "Do you want to check another number? (y/n): ").lower()
            if again != "y":
                print("Goodbye")
                break

        except ValueError:
            print(" Invalid input! Please enter a number.\n")


check()