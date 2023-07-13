import random

numbers = list(map(str, range(10)))
sample4 = random.sample(numbers, k=4)
num4 = "".join(sample4)

val = "".join(random.sample(numbers, k=4))
while val != num4:
    print(val, ": NG")
    val = "".join(random.sample(numbers, k=4))

print(val, ": OK")
