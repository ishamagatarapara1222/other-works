import pandas as pd

# Create list of dictionaries
students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

# Print names of students
print("Student Names:")
for student in students:
    print(student["name"])

#calculate avarage score

total = 0
for student in students:
    total += student["score"]

average = total / len(students)
print("\nAverage Score:", average)

# Add new student
new_student = {"id": 104, "name": "David", "score": 88}
students.append(new_student)

print("\nAfter Adding New Student:")
print(students)

# Update score of student with ID 102 to 88
for student in students:
    if student["id"] == 102:
        student["score"] = 88

print("\nAfter Updating Bob's Score:")
print(students)

# Delete student named Charlie
students = [student for student in students if student["name"] != "Charlie"]

print("\nAfter Deleting Charlie:")
print(students)

# Print students who scored more than 80
print("\nStudents Scoring More Than 80:")
for student in students:
    if student["score"] > 80:
        print(student["name"], "-", student["score"])

# Sort students by score descending
students.sort(key=lambda x: x["score"], reverse=True)

print("\nStudents Sorted by Score:")
for student in students:
    print(student)

# Find highest score student
highest = students[0]

print("\nHighest Score Student:")
print(highest)

# Grade report
print("\nStudent Report:")

grade_count = {"A": 0, "B": 0, "C": 0}

for student in students:

    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    grade_count[grade] += 1

    print("Name:", student["name"],
          "| Score:", score,
          "| Grade:", grade)

# Count grades
print("\nGrade Count:")
for grade, count in grade_count.items():
    print(grade, "=", count)

# Convert into DataFrame
df = pd.DataFrame(students)

print("\nDataFrame:")
print(df)

# Export DataFrame to CSV
df.to_csv("students.csv", index=False)

print("\nData exported to students.csv")

# Re-import CSV
new_df = pd.read_csv("students.csv")

print("\nImported DataFrame:")
print(new_df)

# Mean, Min, Max
print("\nScore Statistics:")
print("Mean =", new_df["score"].mean())
print("Minimum =", new_df["score"].min())
print("Maximum =", new_df["score"].max())
    
