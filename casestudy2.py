import random
import time

min_t = int(input("Enter min temp: "))
max_t = int(input("Enter max temp: "))

i = 0
while i < 10:
    t = random.randint(0,100)
    print("Temp =", t)

    if t < min_t:
        print("LOW")
    elif t > max_t:
        print("HIGH")
    else:
        print("NORMAL")

    time.sleep(2)
    i = i + 1