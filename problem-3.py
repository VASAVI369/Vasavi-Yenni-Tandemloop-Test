def pattern(a):
    a = int(a)
    n = a if (a % 2 == 1) else (a - 1)
    if n <= 0:
        return []
    return [2*i + 1 for i in range(n)]

if __name__ == "__main__":
    a = int(input("Enter a (integer): ").strip())
    result = pattern(a)
    print(", ".join(map(str, result)))
