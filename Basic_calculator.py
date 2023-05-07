def add(a, b):
    answer = a+b
    print(answer)


def sub(a, b):
    answer = a-b
    print(answer)


def mul(a, b):
    answer = a*b
    print(answer)


def div(a, b):
    answer = a/b
    print(answer)


number = 0
while number != 5:
    print("Press:")
    print("1.Addition    2.Subtraction")
    print("3.Division    4.Multiplication")
    print("          5. EXIT              ")
    try:
        number = int(input())
    except ValueError:
        print("Enter valid text")
    if number == 1:
        try:
            a = int(input("Enter number A: "))
            b = int(input("Enter number B: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        add(a, b)
    elif number == 2:
        try:
            a = int(input("Enter number A: "))
            b = int(input("Enter number B: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        sub(a, b)
    elif number == 4:
        try:
            a = int(input("Enter number A: "))
            b = int(input("Enter number B: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        mul(a, b)
    elif number == 3:
        try:
            a = int(input("Enter number A: "))
            b = int(input("Enter number B: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        div(a, b)
    elif number == 5:
        break
    else:
        print("Enter valid input")
