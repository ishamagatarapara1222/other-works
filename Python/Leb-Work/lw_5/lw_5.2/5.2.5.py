#5.  Create a class Student with appropriate attributes and methods, along with a constructor.

class Student:
    # Constructor initializing profile properties
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.attendance_percentage = 0.0

    def update_attendance(self, current_attendance):
        if 0 <= current_attendance <= 100:
            self.attendance_percentage = current_attendance
        else:
            print("Invalid value. Attendance must sit between 0 and 100.")

    def display_student_card(self):
        print(f"=== Student ID: {self.student_id} ===")
        print(f"Full Name : {self.name}")
        print(f"Course    : {self.course}")
        print(f"Attendance: {self.attendance_percentage}%")

# Creating and interacting with the Student object
student1 = Student("STU202609", "Pooja Patel", "Data Science")
student1.update_attendance(88.5)

print("--- Printing Student Academic Record ---")
student1.display_student_card()
