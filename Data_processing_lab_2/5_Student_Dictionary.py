
student = {
    "name": "Raisa Begum",
    "id": "25-63011-1",
    "department": "DATA SCIENCE",
    "CGPA": 2.22
}

for key in student:
    print(key, ":", student[key])

if student["CGPA"] >= 2.50:
    print("Good Standing")
else:
    print("Academic Warning")
