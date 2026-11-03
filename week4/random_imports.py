# Three ways to import a module, using random.randrange.
# randrange(1, 10, 1) gives a whole number from 1 to 9 (10 is excluded).

# 1. import the whole module and use its name
import random
print(random.randrange(1, 10, 1))

# 2. import the module with a shorter alias
import random as rnd
print(rnd.randrange(1, 10, 1))

# 3. import only the function you need
from random import randrange
print(randrange(1, 10, 1))
