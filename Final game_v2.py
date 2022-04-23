"""Игра компьютер угадывает число,
меньше чем за 20 попыток
"""

import numpy as np

min = 1
max = 101

predict_number = np.random.randint(min, max)

count = 0

while True:
    count+=1
    mid = round((min+max) / 2)
    
    if mid > predict_number:
        max = mid
    
    elif mid < predict_number:
        min = mid

    else:
        print(f"Компьютер угадал число за {count} попыток. Это число {predict_number}")
        break #конец игры выход из цикла