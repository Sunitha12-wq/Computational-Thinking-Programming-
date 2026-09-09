
from dataclasses import dataclass


# Traditional Class
class Student:
    def __init__(self, name: str, age: int, marks: float) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def __repr__(self) -> str:
        return f"Student({self.name}, {self.age}, {self.marks})"


# Dataclass
@dataclass
class Employee:
    name: str
    age: int
    salary: float


# Creating Objects
student = Student("Sunitha", 20, 88.5)
employee = Employee("Ajitha", 31, 42000.0)

print("Traditional Class:", student)
print("Dataclass:", employee)

