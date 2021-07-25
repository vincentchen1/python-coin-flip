import random
import constant
import time

num_flips = input("Please Ener Number of Flips= ");
num_flips = int(num_flips)

num_heads = 0
num_tails = 0
for i in range(num_flips):
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

#Report 1: working
print ( "number of heads=" + str(num_heads))
print ( "number of tails=" + str(num_tails))
# Report 2: cleaner
print ( "number of heads=%3d" %( num_heads))
print ( "number of tails=%3d" %( num_tails))
# Report 3: cleanest
print ("number of %s = %i" % (constant.HEAD, num_heads)); 
print ("number of %s = %i" % (constant.TAIL, num_tails));  