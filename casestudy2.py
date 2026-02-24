import random
import time

min_t = int(input("Enter min temp: "))
max_t = int(input("Enter max temp: "))

i = 0
while i < 10:
    t = random.randint(0,100)
    print("\nCurrent Temperature value is =", t)

    if t < min_t:
        print("Warning: Temperature is LOW, below minimum limit")
    elif t > max_t:
        print("Alert: Temperature is HIGH, above maximum limit")
    else:
        print("Status: Temperature is NORMAL and within range")

    time.sleep(2)
    i = i + 1
