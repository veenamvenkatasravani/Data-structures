students = [
    ["Sravani", 22, "CSE"],
    ["Ravi", 21, "ECE"],
    ["Anu", 22, "IT"]
]

print(students)
print(students[0])
print(students[0][0])


#loop through the nested list

students = [
    ["Sravani", 22, "CSE"],
    ["Ravi", 21, "ECE"],
    ["Anu", 22, "IT"]
]

for student in students:
    print(student)


#Access individual values
students = [
    ["Sravani", 22, "CSE"],
    ["Ravi", 21, "ECE"]
]

for student in students:
    print("Name:", student[0])
    print("Age:", student[1])
    print("Branch:", student[2])
    print()