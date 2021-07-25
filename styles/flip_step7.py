import random
import constant
import time

# ts stores the time in seconds
ts = time.time()
  
# print the current timestamp
print(ts)
# use timestamp as random number seed
random.seed(ts)
# generate pseudo random number
random_val = random.random();
# print the generated random number (ranging from 0 to 1)
print(random_val);
# If the generated random number is larger than 0.5, it's a head
# else it's a tail
if (random_val> 0.50):
    print(constant.HEAD)
else:
    print(constant.TAIL)