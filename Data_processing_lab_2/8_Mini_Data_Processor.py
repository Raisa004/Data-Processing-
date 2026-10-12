students = [
    {"name": "Taisa", "department": "DS",
        "marks": [80, 85, 90], "attendance": 85},
    {"name": "Raisa", "department": "DS",
        "marks": [70, 75, 72], "attendance": 90},
    {"name": "Maahi", "department": "BBA",
        "marks": [95, 92, 98], "attendance": 75},
    {"name": "Timsa", "department": "DS",
        "marks": [60, 65, 62], "attendance": 82},
    {"name": "kaisa", "department": "DS",
        "marks": [88, 84, 86], "attendance": 78}
]


def get_average(marks_list):
    total = 0
    for mark in marks_list:
        total = total + mark
    return total / len(marks_list)


def find_top_student(student_list):
    top_student = student_list[0]
    highest_avg = get_average(top_student["marks"])

    for student in student_list:
        current_avg = get_average(student["marks"])
        if current_avg > highest_avg:
            highest_avg = current_avg
            top_student = student
    return top_student


def count_low_attendance(student_list):
    count = 0
    for student in student_list:
        if student["attendance"] < 80:
            count = count + 1
    return count


print("Average Marks for all students:")
for student in students:
    avg = get_average(student["marks"])
    print(student["name"], " ", avg)

top = find_top_student(students)
print(" Student with highest marks:", top["name"])

low_att_count = count_low_attendance(students)
print("Number of students with attendance below 80%:", low_att_count)
