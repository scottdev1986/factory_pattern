from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.occupation = "Student"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Teacher(Person):
    def __init__(self, name, age, class_teaching):
        self.name = name
        self.age = age
        self.occupation = "Teacher"
        self.class_teaching = class_teaching

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_class(self):
        return self.class_teaching


class PersonFactory(ABC):
    @abstractmethod
    def get_person(self) -> Person:
        pass


class StudentFactory(PersonFactory):
    def get_person(self) -> Person:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        return Student(name, age)


class TeacherFactory(PersonFactory):
    def get_person(self) -> Person:
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        class_teaching = input("Subject teaching: ")
        return Teacher(name, age, class_teaching)


def create_entry():
    types = {
        "student": StudentFactory(),
        "teacher": TeacherFactory()
    }

    while True:
        entry_type = input("Enter entry type (student/teacher): ")
        if entry_type in types:
            return types[entry_type]
        else:
            print("Invalid entry type")


def main():
    entry = create_entry()
    person = entry.get_person()
    print("Name:", person.get_name())
    print("Age:", person.get_age())
    print("Occupation:", person.occupation)


if __name__ == "__main__":
    main()
