#Temperature converter
def celsius2fehrenheit(c):
    return (c * (9 / 5)) + 32


def fehrenheit2celsius(f):
    return (f - 32) * 5 / 9


def celsius2kelvin(c):
    return (c + 273.15)


def kelvin2celsius(k):
    return (k - 273.15)


def fehrenheit2kelvin(f):
    return (f - 32) * (5 / 9) + 273.15


def kelvin2fehrenheit(k):
    return (k - 273.15) * (9 / 5) + 32


def main():
    print("Temperature converter\n")
    print(""" pls choose the conversion type

    1.  Celsius  To  Fehrenheit

    2.  Fehrenheit  To Celsius

    3.  Celsius To Kelvin

    4.  Kelvin To Celsius

    5.  Fehrenheit To Kelvin

    6.  Kelvin To Fehrenheit

    """)

    try:
        choice = int(input("Choose from one to six: "))
        temp = float(input("Enter the temperatue: "))

        if choice == 1:
            print(f"{temp}°C = {celsius2fehrenheit(temp):.2f}°F")
        elif choice == 2:
            print(f"{temp}°F = {fehrenheit2celsius(temp):.2f}°C")
        elif choice == 3:
            print(f"{temp}°C = {celsius2kelvin(temp):.2f}K")
        elif choice == 4:
            print(f"{temp}K = {kelvin2celsius(temp):.2f}°C")
        elif choice == 5:
            print(f"{temp}°F = {fehrenheit2kelvin(temp):.2f}K")
        elif choice == 6:
            print(f"{temp}K = {kelvin2fehrenheit(temp):.2f}°F")
        else:
            print(" Invalid choice! Please select a number from 1 to 6.")

    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print(f"Unexcepted error has occured {e}")


if __name__ == "__main__":
    main()