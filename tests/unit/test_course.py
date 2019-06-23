import re

import pytest
from faculty.constants import Gender
from faculty.course import Course
from faculty.exceptions import StudentAlreadyInCourse, StudentNotFoundInCourse
from faculty.student import Student


@pytest.fixture()
def student_fixture():
    students = list()
    filip = Student('161528', 'Filip', 'Markoski', Gender.MALE, 21)
    mila = Student('171246', 'Mila', 'Vasileska', Gender.FEMALE, 19)
    students.append(filip)
    students.append(mila)
    return students


@pytest.fixture()
def course_fixture():
    courses = list()
    course = Course(code='CSES631', name='Software Testing')
    courses.append(course)
    return courses


@pytest.fixture()
def faculty_fixture(course_fixture, student_fixture):
    for course in course_fixture:
        for student in student_fixture:
            course.add_student(student)
    return course_fixture


student_constructor_fields = 'index, first_name, last_name, gender, age'
student_constructor_input = [
    ('161528', '', 'markoski', Gender.MALE, 21),
    ('161528', 'markoski', '', Gender.MALE, 21),
    ('61528', 'Filip', 'Markoski', Gender.MALE, 21),
    ('16l5281', 'Filip', 'Markoski', Gender.MALE, 21),
    ('161528', 'Fi48ip', 'Markoski', Gender.MALE, 21),
    ('161528', 'Filip', 'M@rk0sk1', Gender.MALE, 21),
    ('161528', 'Filip', 'Markoski', Gender.MALE, 0)]


class TestStudent():

    @pytest.mark.regex
    def test_good_student_index_regex_exceptions(self):
        expected = True
        received = bool(re.match(r'^[0-9]{6}$', '161528'))
        assert expected == received

    @pytest.mark.regex
    def test_bad_student_index_regex_exceptions(self):
        expected = False
        received = bool(re.match(r'^[0-9]{6}$', '16a528'))
        assert expected == received

    @pytest.mark.parametrize(student_constructor_fields, student_constructor_input)
    def test_create_student(self, index: str, first_name: str, last_name: str,
                            gender: Gender, age: int):
        with pytest.raises(ValueError):
            student = Student(index, first_name, last_name, gender, age)


@pytest.mark.course
@pytest.mark.usefixtures('faculty_fixture')
class TestCourse():

    @pytest.mark.regex
    def test_good_course_code_regex_exceptions(self):
        expected = True
        received = bool(re.match(r'^[A-Z]{4}[0-9]{3}$', 'CSEW506'))
        assert expected == received

    @pytest.mark.regex
    def test_bad_course_code_regex_exceptions(self):
        expected = False
        received = bool(re.match(r'^[A-Z]{4}[0-9]{3}$', 'CSE1506'))
        assert expected == received

    def test_contains_student(self, faculty_fixture):
        course: Course = faculty_fixture[0]
        filip: Student = Student('161528', 'Filip', 'Markoski', Gender.MALE, 21)
        expected = True
        received = course.contains_student(filip)
        assert expected == received

    def test_add_student_to_course(self, faculty_fixture):
        course: Course = faculty_fixture[0]
        filip: Student = Student('161528', 'Filip', 'Markoski', Gender.MALE, 21)
        with pytest.raises(StudentAlreadyInCourse):
            course.add_student(filip)

    def test_remove_student_from_course(self, faculty_fixture):
        course: Course = faculty_fixture[0]
        filip: Student = Student('161528', 'Filip', 'Markoski', Gender.MALE, 21)
        with pytest.raises(StudentNotFoundInCourse):
            course.remove_student(filip)

    def test_count_students_by_gender(self, faculty_fixture):
        course: Course = faculty_fixture[0]
        expected = 1
        received = course.count_students_by_gender(Gender.MALE)
        assert expected == received

    def test_count_students_greater_than_age(self, faculty_fixture):
        course: Course = faculty_fixture[0]
        expected = 1
        received = course.count_students_greater_than_age(20)
        assert expected == received
