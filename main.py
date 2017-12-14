#!/usr/bin python

import random
import time

spins = random.randint(100, 50000000)
spinnumber= random.randint(5, 15)

for i in range(random.randint(5,15)):
    print("Spinning...")
    time.sleep(0.5)
print(f"You spun the spinner {spins} times")
