#Зад.1. Реализовать функцию, принимающую два числа (позиционные аргументы)
#и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
#обработку ситуации деления на ноль.



def my_func(x, y):

    try:
        k = x / y
        return k
    except ZeroDivisionError:
        return "y не может быть 0"
    except ValueError:
        return "введите число"

print(my_func((int(input("Введите x "))), (int(input("Введите y ")))))


