import random

#q1
def q1():
    num = 100
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    min = 10
    for x in my_list:
        if x < min:
            min = x

    print('Min is ', min )

def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)

class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    def display(self):
        print(self.__model, ' ', self.__year, ' ', self.__color)

def run():
    q1()
    print(fact(5))
    PinkCar = Car('Barbie', 2023, 'pink')
    PinkCar.display()