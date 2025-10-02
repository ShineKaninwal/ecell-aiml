# Student Marks Management System

# Sample data: List of dictionaries
students = [
    {"roll_no": 1, "name": "Shine", "subject": "Math", "marks": 100},
    {"roll_no": 2, "name": "Avni", "subject": "Math", "marks": 92},
    {"roll_no": 3, "name": "Manvi", "subject": "Math", "marks": 78},
    {"roll_no": 4, "name": "Jaya", "subject": "Math", "marks": 88},
    {"roll_no": 5, "name": "Devanshi", "subject": "Math", "marks": 95}
]

# Function to display all student records
def display_students():
    print("\n--- Student Records ---")
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, "
              f"Subject: {student['subject']}, Marks: {student['marks']}")

# Function to find student with highest marks
def highest_marks():
    topper = max(students, key=lambda x: x['marks'])
    print(f"\n🏆 Topper: {topper['name']} "
          f"(Roll No: {topper['roll_no']}, Marks: {topper['marks']})")

# Function to calculate average marks
def average_marks():
    avg = sum(student['marks'] for student in students) / len(students)
    print(f"\n📊 Class Average Marks: {avg:.2f}")

# Main Program Execution
if __name__ == "__main__":
    display_students()
    highest_marks()
    average_marks()
