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
        


class Bank(Client):
    def __init__(self):
        self.client_bank = {}
    
    def add_client(self, client: Client):
        self.client_bank = client
    
    # def transfer(self):
        
    # def get_balance(self):


d = Bank()
print(d.add_client(Client('alina', 500)))
        
    
        
    
        

#Задача 5: Менеджер плагинов

#Задача 6: Расписание и преподаватели

#Задача 7: Конструктор UI-интерфейсов

