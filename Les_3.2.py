#Реализовать функцию, принимающую несколько параметров,
#описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать параметры
#как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_data(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_data(name='Kate', surname='Glu', year='1989', city='Moscow', email='kkvfk@mail.ru',
              telephone='8759648324'))