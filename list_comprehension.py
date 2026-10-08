squares = [x * x for x in range(1, 6)]

print(squares)

#Even number
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)

#filter the number

numbers = [5, 12, 8, 20, 25, 3]

result = [x for x in numbers if x > 10]

print(result)