# Input the number of students
n = int(input())

# Create a nested list to store student names and grades
students = [[input(), float(input())] for _ in range(n)]

# Find the second lowest grade
second_lowest_grade = sorted(set(score for name, score in students))[1]

# Extract names of students with the second lowest grade
second_lowest_students = sorted([name for name, score in students if score == second_lowest_grade])

# Print the names of students with the second lowest grade
for student in second_lowest_students:
    print(student)
