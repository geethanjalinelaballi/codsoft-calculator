def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

want_to_end = False
while not want_to_end:
    select = get_valid_integer("Select operation from 1, 2, 3, 4: ")
    
    if select not in [1, 2, 3, 4]:
        print("Invalid selection. Please choose a valid operation.")
        continue
    
    number_1 = get_valid_integer("Enter first number: ")
    number_2 = get_valid_integer("Enter second number: ")

    if select == 1:
        print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
    elif select == 2:
        print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
    elif select == 3:
        print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
    elif select == 4:
        result = divide(number_1, number_2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{number_1} / {number_2} = {result}")

    proceed = input("Type 'yes' to continue, 'no' to exit: ").strip().lower()
    if proceed == 'no':
        want_to_end = True
