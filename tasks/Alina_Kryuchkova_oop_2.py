# -*- coding: cp1251 -*-

# Задача 1: Класс ShoppingCart

class ShoppingCart():
    def __init__(self):
        self.products = []

    def add_item(self, name: str, price: float):
        self.products.append([name, price])

    def total(self):
        result = 0
        for item in self.products:  
           result += item[1]       
        return result  
        
    
c = ShoppingCart()
c.add_item('melon', 300)
c.add_item('lemon', 100)
print(c.products)
print(c.total())


#Задача 2: Архив сообщений
class MessageArchive():
    def __init__(self):
        self.message = []

    def add_message(self, text: str):
        self.message.append(text)
        
    @property
    def last_message(self):
        return self.message[-1]
    
    def len_message(self):
        return len(self.message)
    
    
f = MessageArchive()
f.add_message('hello')
f.add_message("it's me")
print(f.message)
print(f.len_message())
print(f.last_message)
            
#Задача 3: Менеджер задач    

class Task():
    def __init__(self, title: str, done: False):
        self.title = title
        self.done = done
        

class TaskManager(Task):
    def __init__(self):
        self.__tasks = []
    
    @property
    def tasks(self):
        return self.__tasks
    
    def add_task(self, *task: Task):
        self.__tasks.extend(task)
    
    def tasks_result(self):
        for task in self.tasks:
            if task.done:
                print(f'Задача "{task.title}" выполнена')


tm = TaskManager()
tm.add_task(
    Task("Задача 1", False),
    Task("Задача 2", False),
    Task("Задача 3", False)
)
tm.tasks_result()

tm1 = TaskManager()
tm1.add_task(
    Task("Задача 1", False),
    Task("Задача 2", True),
    Task("Задача 3", False)
)
tm1.tasks_result()

    
#Задача 4: Банк и клиенты

class Client():
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

class Bank():
    def __init__(self):
        self.clients = {}
    
    def add_client(self, name: str, balance: int):
        self.clients[name] = Client(name, balance)
    
    def transfer(self, from_name: str, to_name: str, amount: int):
            from_client = self.clients[from_name]
            to_client = self.clients[to_name]
            from_client.balance -= amount
            to_client.balance += amount
        
    def get_balance(self, name: str):
        return self.clients[name].balance
        

b = Bank()
b.add_client("Ivan", 1000)
b.add_client("Anna", 500)
b.transfer("Ivan", "Anna", 300)
print(b.get_balance("Anna"))
print(b.get_balance("Ivan"))    
        

#Задача 5: Менеджер плагинов

from abc import ABC, abstractmethod

class Plugin(ABC):
    
    @abstractmethod
    def execute(self):
        pass
    
class PrintPlugin(Plugin):
    def __init__(self, message: str):
        self.message = message
    
    def execute(self):
        return self.message
    
class SumPlugin(Plugin):
    def __init__(self, numbers: int):
        self.numbers = numbers
    
    def execute(self):
        return sum(self.numbers)
               

class ReversePlugin(Plugin):
    def __init__(self, text: str):
        self.text = text
    
    def execute(self):
        return self.text[::-1]
    
class PluginManager():
    def __init__(self):
        self.plugins = []
    
    def register(self, plugin: Plugin):
        self.plugins.append(plugin)
        print(plugin.execute())
    
    def runAll(self,):
        for plugin in self.plugins:
            print(plugin.execute())
    

pm = PluginManager()
pm.register(ReversePlugin('pirog'))
pm.register(SumPlugin([3, 3, 3]))
pm.register(PrintPlugin('attack'))
pm.runAll()

#Задача 6: Расписание и преподаватели

class Teacher():
    def __init__(self, teacher: str, subject: list):
        self.teacher = teacher
        self.subject = subject
        
class Schedule():
    def __init__(self):
        self.lesson = []
    
    def add_lesson(self, day: str, subject: str, teacher: Teacher):
        self.lesson.append((day, subject, teacher))
    
    def get_day_schedule(self, day: str):
        one_day = []
        for lesson in self.lesson:  
            if lesson[0] == day:
              one_day.append(f"Предмет: {lesson[1]}, Преподаватель: {lesson[2].teacher}")
        return ", ".join(one_day)
            
   
t = Teacher("Ivanov", ["History"])
t1 = Teacher("Petrov", ["Math"])
t2 = Teacher("Minin", ["English"])
s = Schedule()
s.add_lesson("Monday", "History", t)
s.add_lesson("Monday", "Math", t1)
s.add_lesson("Friday", "English", t2)
print(s.get_day_schedule("Monday"))



