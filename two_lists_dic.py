names = ["Sravani", "Ravi", "Anu"]
ages = [22, 21, 23]

students = {name: age for name, age in zip(names, ages)}

print(students)