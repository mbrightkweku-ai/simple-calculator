while True:
    while True:
        try:
            num = int(input("Enter a number : "))
            break
        except ValueError:
            print("invalid number!! Try again")
        
    print(f"\n Multiplication table for {num}")
    for i in range(1, 13):
        print(f"{i} x {num} = {i*num} ")
        
    again =input("do you want to generate another times table (yes / no)").strip().lower()
    if again != "yes":
        print("Goodbye")
        break
