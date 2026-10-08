squares = {x: x * x for x in range(1, 6)}

print(squares)

#Even number → Square

even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)