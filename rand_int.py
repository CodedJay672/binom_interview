import random

key = ""
for i in range(4):
  rand_int = str(random.randint(0,1))
  key += rand_int

print("{} => {:x}".format(key, int(key,2)))