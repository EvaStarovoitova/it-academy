# Создайте базовый класс Vehicle (транспортное средство) с защищённым (_protected) атрибутом max_speed и приватным (__private) атрибутом mileage.
#  - Добавьте публичный метод display_info(), который выводит эти атрибуты.
#  - Создайте дочерний класс Bus, который наследует Vehicle и добавляет атрибут passenger_capacity.
#  - Переопределите метод display_info() в Bus, чтобы он показывал также вместимость пассажиров.

class Vechical:
  
    def __init__(self, _max_speed, __mileage):
        self._max_speed=_max_speed
        self.__mileage=__mileage


    def display_info(self):
        print(f"{self._max_speed}, {self.__mileage}")


class Bus(Vechical):

    def __init__(self,_max_speed, __mileage, passenger_capacity):
        self._max_speed=_max_speed
        self.__mileage=__mileage
        self.passenger_capacity=passenger_capacity


    def display_info(self):
        print(f" Max speed: {self._max_speed}, max mileage: {self.__mileage}, passenger: {self.passenger_capacity}")


bus = Bus(180, 10000, 50)
bus.display_info()

# Создайте класс Temperature с приватным атрибутом __celsius.
#  - Реализуйте геттер и сеттер для celsius, 
# где сеттер проверяет, что температура не может быть ниже -273.15°C (абсолютный ноль).
#  - Добавьте свойство fahrenheit (геттер), которое возвращает температуру в Фаренгейтах (формула: °F = °C * 9/5 + 32).

class Temperature:

    def __init__(self, celsius):   
        self.celsius = celsius  

    @property
    def celsius(self):
        return  self.__celsius 
    
    @celsius.setter
    def celsius(self, value):
        assert value >= -273.15 ,"температура не может быть ниже -273.15°C "
        self.__celsius=value

    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32
    
temp = Temperature(-25)
print(temp.fahrenheit) 
temp.celsius = -300    



# Реализуйте класс BankAccount:
#  - Приватные атрибуты: __balance, __account_number.
#  - Геттеры для баланса и номера счёта. Сеттер только для баланса (с проверкой, что баланс не может быть отрицательным).
#  - Статический метод generate_account_number(), который возвращает случайный 10-значный номер счёта.
#  - Метод класса create_account(cls, initial_balance), который создаёт аккаунт с сгенерированным номером.

# account = BankAccount.create_account(1000)
# print(account.balance)          # 1000
# account.balance = -500          # ValueError

import random

class BankAccount:

    def __init__(self, balance, account_number):
        self.balance = balance
        self.__account_number = account_number
    
    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть меньше нуля")
        self.__balance = value

    @property
    def account_number(self):
        return self.__account_number
    
    @staticmethod
    def generate_account_number():
        return ''.join(random.choices('0123456789', k=10))

    @classmethod
    def create_account(cls, initial_balance):
        account_number = cls.generate_account_number()
        return cls(initial_balance, account_number)


account = BankAccount.create_account(1000)
print(account.balance)  # 1000
account.balance = -500  # ValueError


# 4*)Создайте базовый класс Employee с атрибутами name, salary (защищённый) и методом display_info().
# От него унаследуйте Manager (добавляет атрибут department) и Developer (добавляет programming_language).
# Сделайте так, чтобы salary нельзя было изменить напрямую, 
# но можно было через метод set_salary(), который проверяет, что зарплата не меньше 0.

# dev = Developer("Alice", 5000, "Python")
# dev.set_salary(-1000)  # Должно вызвать ошибку

class Employee:

    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary

    @property
    def salary(self):
        return self.__salary
    
    def display_info(self):
        print(f"Name {self.name}, salary: {self.__salary}")

    def set_salary(self, value):
        if value <0: raise ValueError("Зарплата не должна быть меньше нуля")
        self.__salary=value

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department=department
    
    def display_info(self):
        print(f"Name {self.name}, salary: {self.salary}, department: {self.department}")


class Developer(Employee):

     def __init__(self, name, salary, programming_language ):
        super().__init__(name, salary)
        self.programming_language=programming_language

     def display_info(self):
        print(f"Name {self.name}, salary: {self.salary}, programming language : {self.programming_language }")



dev = Developer("Alice", 5000, "Python")
dev.display_info()
dev.set_salary(-1000)  # Должно вызвать ошибку

       