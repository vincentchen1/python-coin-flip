import constant
import random

random.seed(10)

print(random.random())
random_val = random.random();
if (random_val> 0.50):
    print(constant.HEAD)
else:
    print(constant.TAIL)