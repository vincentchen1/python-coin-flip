import random
import constant
import time

for i in range(10):
    # ts stores the time in seconds
    ts = time.time()

    # use timestamp as random number seed
    random.seed(ts)
    # generate pseudo random number
    random_val = random.random();

    # If the generated random number is larger than 0.5, it's a head
    # else it's a tail
    if (random_val> 0.50):
        print(constant.HEAD)
    else:
        print(constant.TAIL)