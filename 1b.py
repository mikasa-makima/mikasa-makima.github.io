import csv
import operator

# Read the student data from the CSV file
students = []
with open('students.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        name, roll_number, marks1, marks2, marks3 = row
        # Convert marks to integers and store student data in a list of dictionaries
        students.append({
            'Name': name,
            'Roll Number': roll_number,
            'Marks1': int(marks1),
            'Marks2': int(marks2),
            'Marks3': int(marks3)
        })

# Calculate average marks for each student
for student in students:
    avg_marks = (student['Marks1'] + student['Marks2'] + student['Marks3']) / 3
    student['Average Marks'] = round(avg_marks, 2)

# Sort students by name without using lambda
students_sorted = sorted(students, key=operator.itemgetter('Name'))

# Print the student records with average marks
print("Student Records Sorted by Name:")
print(f"{'Name':<10} {'Roll Number':<12} {'Marks1':<6} {'Marks2':<6} {'Marks3':<6} {'Average Marks'}")
for student in students_sorted:
    print(f"{student['Name']:<10} {student['Roll Number']:<12} {student['Marks1']:<6} {student['Marks2']:<6} {student['Marks3']:<6} {student['Average Marks']}")
