# -*- coding: cp1251 -*-
# Задача 1: Счётчик
class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def get_counter(self):
        return self.__count
    

c = Counter()
c.increment()
c.increment()
c.increment()
print(c.get_counter())  # 3


#Задача 2: Животные

class Animal:

    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):

    def speak(self):
        print("Гав-гав!")

class Cat(Animal):

    def speak(self):
        print("Мяу-мяу!")

animals = [Dog(), Cat()]
for a in animals:
    a.speak() 

#Задача 3: Прямоугольник

class Rectangle:
    def __init__(self, width, height):
        self.width = width  
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        if new_width > 0:
            self.width = new_width
        else:
            print("ValueError")
        
    def get_height(self):
        return self.height

    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
            print("ValueError")

    @property
    def area(self):
        return self.width * self.height
        

newArea = Rectangle(3, 4)
print(newArea.area)
newArea.width = -5
newArea.height = -6


#Задача 4: Платёжные системы

class PaymentMethod:

    def pay(amount):
        pass

class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Оплата по кредитной карте: {amount} руб.")

class PayPalPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} руб.")


def make_payment(method: PaymentMethod, amount: float):
    method.pay(amount)

credit = CreditCardPayment()
paypal = PayPalPayment()
make_payment(credit, 1000)
make_payment(paypal, 500.50)


#Задача 5: Транспорт

from abc import ABC, abstractmethod
class Transport(ABC):
     
     @abstractmethod
     def start(self):
         pass
     
     
     @abstractmethod
     def stop(self):
         pass
     


class Car(Transport):
    def __init__(self, max_speed):
        self._max_speed = None
        self.max_speed = max_speed
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self, value):
        if(value < 0):
            print("Скорость не может быть отрицательной")
        elif(value > 300):
            print("Скорость не может быть выше 300")
        else:
            self._max_speed = value
    
    def start(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановлена")

c = Car(250)  
print(c.max_speed)
c = Car(350)  
print(c.max_speed)