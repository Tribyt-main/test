import random
random_number = random.randint(3, 20)
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(random_number)
for x in numbers_1:
    for i in numbers_1:
        if x + i == random_number:
            if x > i:
                break
            print(x, i)
