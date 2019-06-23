import re

from faculty.constants import Gender


class Student:
    def __init__(self, index: str, first_name: str, last_name: str,
                 gender: Gender, age: int):
        if not len(index) == 6:
            raise ValueError('Student index must be exactly 6 characters long')
        if not re.match(r'^[0-9]{6}$', index):
            raise ValueError('Student index must contain only digits')
        if not re.match(r'^[a-zA-Z]+$', first_name):
            raise ValueError('Student first name must not be empty and contain only letters')
        if not re.match(r'^[a-zA-Z]+$', last_name):
            raise ValueError('Student last name must not be empty and contain only letters')
        if not (0 < age < 130):
            raise ValueError('Student age must be between 0 and 130')
        self.index = index
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
