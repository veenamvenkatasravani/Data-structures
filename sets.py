numbers = {10, 20, 30, 20, 10}

print(numbers)

#add elements

numbers = {10, 20, 30}

numbers.add(40)
numbers.add(50)
print(numbers)


#remove elements

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

#Set length

numbers = {10, 20, 30, 40}

print(len(numbers))

#Difference

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.difference(set2)

print(result)