first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

while True:
    choice = input("Выберите оператор (+, -, *, /): ")

    if choice == "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
        break

    elif choice == "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
        break

    elif choice == "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
        break

    elif choice == "/":
        if second_number == 0:
            print("Деление на ноль невозможно!")
            break

        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result:.2f}")
            break

    else:
        print("Пожалуйста, выберите оператор из предложенного списка")
        continue
