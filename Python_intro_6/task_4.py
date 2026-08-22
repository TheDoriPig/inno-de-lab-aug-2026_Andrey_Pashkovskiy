number = int(input("Введите целое число: "))
remainder = number % 2
if remainder == 0:
    print(f"Число {number} - чётное.")
else:
    print(f"Число {number} - нечетное.")
