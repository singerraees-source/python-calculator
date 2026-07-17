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
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")

    # User se choice lena
    choice = input("Choice likho: ")

    # Agar Exit choose kiya
    if choice == "5":
        print("Calculator band ho gaya.")
        break

    # Agar galat choice di
    if choice not in ["1", "2", "3", "4"]:
        print("Galat choice!")
        continue

    # Do number lena
    num1 = int(input("Pehla number: "))
    num2 = int(input("Dusra number: "))

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
            print("0 se divide nahi kar sakte.")
        else:
            print("Answer =", div(num1, num2))