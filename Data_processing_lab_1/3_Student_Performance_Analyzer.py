name = input("Enter student name: ")

mark1 = float(input("Enter mark for course 1: "))
mark2 = float(input("Enter mark for course 2: "))
mark3 = float(input("Enter mark for course 3: "))
mark4 = float(input("Enter mark for course 4: "))
mark5 = float(input("Enter mark for course 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

highest = max(mark1, mark2, mark3, mark4, mark5)
lowest = min(mark1, mark2, mark3, mark4, mark5)

passed = 0

if mark1 >= 50:
    passed = passed + 1

if mark2 >= 50:
    passed = passed + 1

if mark3 >= 50:
    passed = passed + 1

if mark4 >= 50:
    passed = passed + 1

if mark5 >= 50:
    passed = passed + 1

if average >= 85:
    performance = "Excellent"
elif average >= 75:
    performance = "Good"
elif average >= 65:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Fail"

print("Student Name:", name)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Courses:", passed)
print("Performance:", performance)