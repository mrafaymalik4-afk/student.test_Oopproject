import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from student_eligibility import RegularStudent, ScholarshipStudent  

class TestStudentEligibility(unittest.TestCase):

    def test_regular_student_eligible(self):
        # Meets all minimum criteria
        marks = {"Math": 85, "Science": 80}
        student = RegularStudent("Test", 20, 1, attendance=80, gpa=3.0, marks=marks)
        
        self.assertTrue(student.check_attendance())
        self.assertTrue(student.check_gpa())
        self.assertTrue(student.check_marks())
        self.assertTrue(student.is_eligible()["fully_eligible"])

    def test_regular_student_failing_marks(self):
        # Has one subject below 80
        marks = {"Math": 75, "Science": 85}
        student = RegularStudent("Test", 20, 1, attendance=80, gpa=3.0, marks=marks)
        
        self.assertFalse(student.check_marks())
        self.assertFalse(student.is_eligible()["fully_eligible"])

    def test_scholarship_student_gpa_threshold(self):
        # Scholarship student needs 4.5 GPA, 4.0 should fail
        marks = {"Math": 90}
        student = ScholarshipStudent("Schol", 21, 2, attendance=85, gpa=4.0, marks=marks)
        
        self.assertFalse(student.check_gpa())

if __name__ == "__main__":
    unittest.main()

