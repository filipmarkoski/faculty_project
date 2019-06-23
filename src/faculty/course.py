import re

from faculty.constants import Gender
from faculty.exceptions import StudentAlreadyInCourse, StudentNotFoundInCourse
from faculty.student import Student


class Course:
    def __init__(self, code: str, name: str):
        if not re.match(r'^[A-Z]{4}[0-9]{3}$', code):
            raise ValueError('Course code must have AAAA000 format')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise ValueError('Course name must not be empty and contain only letters')
        self.code = code
        self.name = name
        self.students = list()

    def add_student(self, student: Student) -> None:
        if self.contains_student(student):
            raise StudentAlreadyInCourse()
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        if self.contains_student(student):
            raise StudentNotFoundInCourse()
        self.students.remove(student)

    def contains_student(self, student: Student) -> bool:
        return bool(student.index in [student.index for student in self.students])

    def count_students_by_gender(self, gender: Gender) -> int:
        if gender not in Gender:
            raise AttributeError()

        count: int = 0
        for student in self.students:
            if student.gender == gender:
                count += 1
        return count

    def count_students_greater_than_age(self, age: int) -> int:
        if not (0 < age < 130):
            raise ValueError('Age must be between 0 and 130')

        count: int = 0
        for student in self.students:
            if student.age > age:
                count += 1
        return count
