"""Minimal Project Task Management."""

from .constants import (
    Gender
)
from .course import Course
from .exceptions import (
    StudentNotFoundInCourse,
    StudentAlreadyInCourse
)
from .student import Student

__version__ = '0.1.0'
