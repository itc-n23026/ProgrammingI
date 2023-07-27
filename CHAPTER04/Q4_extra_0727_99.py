def multiplication_table():
    def multiply(x, y):
        return x * y

    for i in range(1, 10):
        for j in range(1, 10):
            result = multiply(i, j)
            print(result, end=" ")
        print()


if __name__ == "__main__":
    multiplication_table()
