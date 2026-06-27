#7. Create a class Student with private attributes for name and marks (of three subjects).

#Add a method to calculate and display the average.

#Add public methods to calculate and display the grade based on marks.

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.__name = name
        self.__marks = [mark1, mark2, mark3]

    def calculate_average(self):
        total = sum(self.__marks)
        avg = total / len(self.__marks)
        return avg

    def display_report(self):
        avg = self.calculate_average()
        
        # Simple grading system logic
        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 50:
            grade = 'C'
        else:
            grade = 'F'
            
        print(f"Student Name: {self.__name}")
        print(f"Average Marks: {avg:.2f}")
        print(f"Final Grade  : {grade}")

# Testing student profile
student_profile = Student("Sneha", 85, 92, 78)
print("--- Student Evaluation ---")
student_profile.display_report()
