import random
import constant
import time

num_heads = 0
num_tails = 0
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
        num_heads += 1;
    else:
        print(constant.TAIL)
        num_tails += 1;

# print ( "number of heads=" + num_heads)
# print ( "number of tails=" + num_tails)
print ( "number of heads=" + str(num_heads))
print ( "number of tails=" + str(num_tails)) 