def concat_words(*args, separator=","):
    return separator.join(args)


print(concat_words("a", "b", "c", "d", separator="_"))
print(concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" "))
print(concat_words("沖縄県", "那覇市", "樋川", "2丁目", "16-18", separator=" "))
print(
    concat_words(
        "home",
        "vagrant",
        "programming1_git",
        "ProgrammingI",
        "CHAPTER04",
        separator="/",
    )
)
