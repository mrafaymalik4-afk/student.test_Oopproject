from abc import ABC, abstractmethod
from typing import Dict

class Student(ABC):
    """Abstract base class representing a generic student."""
    
    # Centralized rules that subclasses can override if necessary
    MIN_ATTENDANCE = 78
    MIN_GPA = 2.5
    MIN_SUBJECT_MARK = 80

    def __init__(self, name: str, age: int, roll_no: int, attendance: float, gpa: float, marks: Dict[str, int]):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.attendance = attendance
        self.gpa = gpa
        self.marks = marks  # Expecting a dictionary, e.g., {"Math": 85, "Physics": 90}

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, roll_no={self.roll_no}, "
            f"attendance={self.attendance}%, gpa={self.gpa})"
        )

    def check_attendance(self) -> bool:
        return self.attendance >= self.MIN_ATTENDANCE

    def check_gpa(self) -> bool:
        return self.gpa >= self.MIN_GPA

    def check_marks(self) -> bool:
        # Ensures EVERY subject meets the minimum criteria
        if not self.marks:
            return False
        return all(mark >= self.MIN_SUBJECT_MARK for mark in self.marks.values())

    def is_eligible(self) -> dict:
        """Returns a comprehensive evaluation of the student's eligibility."""
        return {
            "attendance_ok": self.check_attendance(),
            "gpa_ok": self.check_gpa(),
            "marks_ok": self.check_marks(),
            "fully_eligible": self.check_attendance() and self.check_gpa() and self.check_marks()
        }


class RegularStudent(Student):
    """Inherits standard rules from the base Student class."""
    pass


class ScholarshipStudent(Student):
    """A stricter student category requiring higher benchmarks."""
    MIN_ATTENDANCE = 80
    MIN_GPA = 4.5
    # Inherits the standard MIN_SUBJECT_MARK (80) automatically


if __name__ == "__main__":
    # Marks represented as a dictionary for realistic tracking
    rahul_marks = {"Math": 77, "English": 85}
    saleem_marks = {"Math": 80, "English": 90}
    arbaaz_marks = {"Math": 85, "English": 88}

    student1 = RegularStudent("Rahul", age=20, roll_no=22, attendance=80, gpa=3.4, marks=rahul_marks)
    student2 = ScholarshipStudent("Saleem", age=22, roll_no=23, attendance=80, gpa=4.5, marks=saleem_marks)
    student3 = RegularStudent("Arbaaz", age=21, roll_no=24, attendance=82, gpa=3.0, marks=arbaaz_marks)

    students = [student1, student2, student3]

    for student in students:
        print(student)
        print(f"Eligibility Details: {student.is_eligible()}\n")
