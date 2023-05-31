sequence = [0, 1]  
while sequence[-1] <= 4000000:
        next_number = sequence[-1] + sequence[-2]
        if next_number >= 4000000:
            break
        sequence.append(next_number)
võrdsed = []
for i in sequence:
    if i % 2 == 0:
        võrdsed.append(i)
print(võrdsed)
