def first_n_odds(a):
    a = int(a)
    if a <= 0:
        return []
    return [2*i + 1 for i in range(a)]

if __name__ == "__main__":
    a = int(input("Enter a (integer): ").strip())
    result = first_n_odds(a)
    print(", ".join(map(str, result)))
