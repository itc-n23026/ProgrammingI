def concat_words(*args, separator=","):
    return separator.join(args)


print(concat_words("a", "b", "c", "d", separator="_"))
print(concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" "))
