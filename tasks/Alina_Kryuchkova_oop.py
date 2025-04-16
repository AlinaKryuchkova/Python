# -*- coding: utf-8 -*-
# Р—Р°РґР°С‡Р° 1: РЎС‡С‘С‚С‡РёРє
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
print(c.get_counter())


#Р—Р°РґР°С‡Р° 2: Р–РёРІРѕС‚РЅС‹Рµ

class Animal:

    def speak(self):
        print("Р–РёРІРѕС‚РЅРѕРµ РёР·РґР°С‘С‚ Р·РІСѓРє")

class Dog(Animal):

    def speak(self):
        print("Р“Р°РІ-РіР°РІ!")

class Cat(Animal):

    def speak(self):
        print("РњСЏСѓ-РјСЏСѓ!")

animals = [Dog(), Cat()]
for a in animals:
    a.speak() 

#Р—Р°РґР°С‡Р° 3: РџСЂСЏРјРѕСѓРіРѕР»СЊРЅРёРє

class Rectangle:
    def __init__(self, width, height):
        self.width = width  
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("РЁРёСЂРёРЅР° РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅРѕР№ РёР»Рё СЂР°РІРЅРѕР№ РЅСѓР»СЋ")

    @property  
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Р’С‹СЃРѕС‚Р° РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅРѕР№ РёР»Рё СЂР°РІРЅРѕР№ РЅСѓР»СЋ")

    @property
    def area(self):
        return self.width * self.height

newArea = Rectangle(3, 4)
print(newArea.area)
newArea = Rectangle(-3, 4)
newArea = Rectangle(3, -4)


#Р—Р°РґР°С‡Р° 4: РџР»Р°С‚С‘Р¶РЅС‹Рµ СЃРёСЃС‚РµРјС‹

class PaymentMethod:

    def pay(amount):
        pass

class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"РћРїР»Р°С‚Р° РїРѕ РєСЂРµРґРёС‚РЅРѕР№ РєР°СЂС‚Рµ: {amount} СЂСѓР±.")

class PayPalPayment(PaymentMethod):

    def pay(self, amount):
        print(f"РћРїР»Р°С‚Р° С‡РµСЂРµР· PayPal: {amount} СЂСѓР±.")


def make_payment(method: PaymentMethod, amount: float):
    method.pay(amount)

credit = CreditCardPayment()
paypal = PayPalPayment()
make_payment(credit, 1000)
make_payment(paypal, 500.50)


#Р—Р°РґР°С‡Р° 5: РўСЂР°РЅСЃРїРѕСЂС‚
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
        self.max_speed = max_speed
    
    @property # РґРµРєРѕСЂР°С‚РѕСЂ, РїРѕР·РІРѕР»СЏРµС‚ РѕР±СЂР°С‰Р°С‚СЊСЃСЏ Рє С„СѓРЅРєС†РёРё РєР°Рє Рє РїРµСЂРµРјРµРЅРЅРѕР№
    def max_speed(self):
        return self.__max_speed
    
    @max_speed.setter # РґРµРєРѕСЂР°С‚РѕСЂ СЃРµС‚С‚РµСЂР°, РІ РЅР°Р·РІР°РЅРёРё РЅСѓР¶РЅРѕ РїРµСЂРµРґРѕРІР°С‚СЊ РЅР°Р·РІР°РЅРёРµ РіРµС‚С‚РµСЂР° + РјРµС‚РѕРґ setter
    def max_speed(self, value):
        if(value < 0):
            print(f"РЎРєРѕСЂРѕСЃС‚СЊ РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅРѕР№, РІР°С€Р° СЃРєРѕСЂРѕСЃС‚СЊ {value}")
        elif(value > 300):
            print(f"РЎРєРѕСЂРѕСЃС‚СЊ РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РІС‹С€Рµ 300, РІР°С€Р° СЃРєРѕСЂРѕСЃС‚СЊ {value}")
        elif(value == 0):
            print("РЎРєРѕСЂРѕСЃС‚СЊ СЂР°РІРЅРѕ 0, РјР°С€РёРЅР° СЃС‚РѕРёС‚")
        else:
            self.__max_speed = value
    
    def start(self):
        print("РњР°С€РёРЅР° РµРґРµС‚")

    def stop(self):
        print("РњР°С€РёРЅР° РѕСЃС‚Р°РЅРѕРІР»РµРЅР°")

c = Car(250)  
print(c.max_speed)
c = Car(350)
c = Car(-20)
c = Car(0)