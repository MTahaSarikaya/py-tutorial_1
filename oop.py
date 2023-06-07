'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)

s1 = Student("Taha", 18, 100)
s2 = Student("Ahmet", 18, 75)
s3 = Student("Mehmet", 18, 90)

course = Course("Maths", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

'''

# yukaridaki kod bir sinif olusturup, siniftaki kisilerin ortalama notunu hesaplayan bir kod.


# Inheritance 
# ( üst bir sinif olusturup, diger siniflarda da kullanmak icin kullanilir.)

'''
class Pet:
    def __init_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

d = Dog("Doggy", 5)
d.speak()
'''

# Class 
'''
class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init_ (self, name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

pl = Person("tim")
p2 = Person("jill")
print(Person.number_of_people)
'''

# Static Method
'''
class Math:

    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10

print(Math.add10(5))
'''