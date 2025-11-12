try:
    a, value, b = int(input()), input(), int(input())
    match value:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            try:
                print(round((a / b), 2))
            except ZeroDivisionError:
                print("Делить на ноль нельзя")
        case _:
            print("Ошибка.\nКалькулятор может использовать только +, -, *, /")
except (TypeError, ValueError):
    print('Произошла ошибка. Проверьте ввод данных.\n'
          '1) Сначала вводим число\n'
          '2) Затем вводим один знак (+, -, * или /)\n'
          '3) Снова вводим число')
