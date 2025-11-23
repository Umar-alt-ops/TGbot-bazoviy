'№1'
'''Наследование в ООП - это когда один класс может использовать свойства и методы другого класса. Она нужна для того,чтобы 
избежать дублирования кода и упростить его поддержку.'''
'№2'
'''Разница между полиморфизмом и инкапсуляцией в том, что полиморфизм позволяет объектам разных классов использовать один и тот же метод,
в то время как инкапсуляция скрывает внутренние детали реализации объекта и предоставляет только необходимый метод для взаимодействия с ним.'''
'Примеры'
'Инкапсуляция:'
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
'Полиморфизм:'
class Dog:
    def sound(self):
        return "Гав-гав"
    def sound(self):
        return "Мяу-мяу"
        
'№3'
'''модуль и пакет в Python - это способы организации кода. Модуль - это отдельный файл с кодом, который можно 
импортировать в другие файлы. Пакет - это файл, который содержит __init__.py и внутри него никакого кода не должно бытью'''
'№4'
'1 - git init - инициализация и создание репозитория'
'2 - git add . - добавление всех изменений в индекс'
'3 - git commit -m "сообщение" - создание коммита с сообщением'
'4 - git push origin main - отправка изменений на удаленный репозиторий'
'№5'
'''Виртуальная среда в Python - это среда, которая изолирует зависимости проекта от глобальных установок Python. 
Она нужна для того, чтобы избежать конфликтов между разными проектами и управлять зависимостями более эффективно. Внешний
пакет устанавливается с помощью команды pip install имя_пакета внутри активированной виртуальной среды.'''
'№6'
'Основные CRUD операции с базой данных:'
'1 - Create (Создание) - добавление новых записей в базу данных'
'2 - Read (Чтение) - получение данных из базы данных'
'3 - Update (Обновление) - изменение существующих записей в базе данных'
'4 - Delete (Удаление) - удаление записей из базы данных'
'5 - SELECT - выборка данных из таблицы'
'6 - UPDATE - обновление данных в таблице'
'№7'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f'Name: {self.name}, Age: {self.age}'
    
class Student(Person):
    def __init__(self, name, age, grade):
         self.name = name
         self.age = age
         self.grade = grade
    def study(self):
        return f'{self.name} is stidying'

s = Student('Alice', 20, 'A')
print(s.info())
print(s.study())
'№8'
class Student:
    _all_grades = []

    def __init__(self, average_grade):
        self.__average_grade = average_grade
        Student._all_grades.append(average_grade)

    def get_average(self):
        return self.__average_grade

    @classmethod
    def get_group_average(cls):
        return sum(cls._all_grades) / len(cls._all_grades)

s  = Student(5)
s2 = Student(4)
s3 = Student(3)
s4 = Student(2)
for student in (s, s2, s3, s4):
    print("Оценка:", student.get_average())
print("Средний балл группы:", Student.get_group_average())
'№9'
class Student:
    def __init__(self, average_grade):
        self._average_grade = average_grade  # защищённый атрибут

    @property
    def average(self):
        """Геттер — возвращает среднюю оценку"""
        return self._average_grade

    @average.setter
    def average(self, value):
        """Сеттер — проверяет диапазон 0–5 и задаёт новое значение"""
        if 0 <= value <= 5:
            self._average_grade = value
        else:
            raise ValueError("Средняя оценка должна быть в диапазоне 0–5")

s = Student(5)
s.average = 4.2     
print(s.average)     
'№10'
class Student:
    def __init__(self, name, average):
        self.name = name
        self.average = average

class Team:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if not (s.name == name)]

    def team_average(self):
        if not self.students:
            return 0
        total = sum(s.average for s in self.students)
        return total / len(self.students)

team = Team()

team.add_student(Student("Umar", 5))
team.add_student(Student("Ali", 3))
team.add_student(Student("Sara", 4))

print("Средний балл команды:", team.team_average())
'№11'
import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
grade TEXT,
average REAL
)
''')
conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("Umar", "10th", 4.5))
# conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("Ali", "11th", 3.8))
# conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("Sara", "10th", 4.2))
# conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("Mira", "12th", 4.9))
# conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("John", "11th", 3.5))
# conn.commit()
# cursor.execute("INSERT INTO students (name, grade, average) VALUES (?, ?, ?)", ("Lina", "10th", 4.7))
# conn.commit()
print("Студенты с средним баллом выше 4.0:")
cursor.execute("SELECT * FROM students WHERE average > 4.0")
rows = cursor.fetchall()
for row in rows:
    print(row)
'№12'
print("Топ 3 лучших студента по среднему баллу:")  
cursor.execute("SELECT average FROM students ORDER BY average DESC LIMIT 3")
rows = cursor.fetchall()
for row in rows:
    print(row[0])
# cursor.execute("UPDATE students SET average = 5 WHERE name = ?", ("Umar",))
# conn.commit()
print("Обновленный средний балл Умара:")
cursor.execute("SELECT average FROM students WHERE name = ?", ("Umar",))
row = cursor.fetchone()
print(row[0])
# cursor.execute("DELETE FROM students WHERE name = ?", ("Sara",))
# conn.commit()