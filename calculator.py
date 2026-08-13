
# Add function
def add(a, b):
    return a + b


# Subtract function
def sub(a, b):
    return a - b


# Multiply function
def mul(a, b):
    return a * b


# Divide function
def div(a, b):
    return a / b


# Calculator tab tak chalega jab tak user Exit nahi karega
while True:

    # Menu dikhana
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # User se choice lena
    choice = input("Choice likho: ")

    # Agar Exit choose kiya
    if choice == "5":
        print("Calculator band ho gaya.")
        break

    # Agar galat choice di
    if choice not in ["1", "2", "3", "4"]:
        print("Galat choice! 1 se 5 tak choice select karo.")
        continue

    # Number input lene ki koshish
    try:
        num1 = int(input("Pehla number: "))
        num2 = int(input("Dusra number: "))

    # Agar user number ki jagah text likhe
    except ValueError:
        print("Error! Kripya valid number enter karo.")
        continue

    # Choice ke hisaab se function chalana
    if choice == "1":
        print("Answer =", add(num1, num2))

    elif choice == "2":
        print("Answer =", sub(num1, num2))

    elif choice == "3":
        print("Answer =", mul(num1, num2))

    elif choice == "4":
        # Divide by zero check
        if num2 == 0:
            print("Error! 0 se divide nahi kar sakte.")
        else:
            print("Answer =", div(num1, num2))

print("Git clone practice")
print("Git pull practice")
