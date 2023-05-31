def smallest_multiple():
    result = 1
    for i in range(1, 21):
        num = result
        while num % i != 0:
            num += result
        result = num
    return result

smallest_num = smallest_multiple()
print("The smallest positive number divisible by all the numbers from 1 to 20 is:", smallest_num)