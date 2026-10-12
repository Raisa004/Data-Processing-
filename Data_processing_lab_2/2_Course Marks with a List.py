
marks = []


print("Please enter the marks for 5 courses:")

for i in range(5):

    mark = int(input("Enter mark for course " + str(i + 1) + ": "))
    marks.append(mark)

print("Marks entered:", marks)

total_marks = sum(marks)
average_mark = total_marks / len(marks)


highest_mark = max(marks)
lowest_mark = min(marks)

passed_count = 0
for mark in marks:
    if mark >= 50:
        passed_count = passed_count + 1

print("Total Marks:", total_marks)
print("Average Mark:", average_mark)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Courses Passed:", passed_count)
