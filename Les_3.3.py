#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    sequence = [x, y, z]
    min = min(sequence)
    sequence.remove(min)
    return (sum(sequence))

print(my_func(1, 2, 3))


