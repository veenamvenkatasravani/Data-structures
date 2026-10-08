name="sravani"

frequency = {}

for character in name:
    if character in frequency:
        frequency[character] +=1

    else:

        frequency[character] =1

print(frequency)