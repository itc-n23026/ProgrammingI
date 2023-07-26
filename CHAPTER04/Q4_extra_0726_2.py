for e in filter(lambda i: i % 2 == 0, range(1, 11)):
    print(e, end=" ")

pairs = [(2, "down")]
pairs.sort(key=lambda x: x[1])
print(pairs)
