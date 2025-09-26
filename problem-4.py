def parse_input(s):
    # accept comma or space separated numbers
    s = s.replace(",", " ")
    parts = s.split()
    return [int(x) for x in parts]

def count_multiples(numbers):
    counts = {}
    for d in range(1, 10):
        counts[d] = sum(1 for num in numbers if num % d == 0)
    return counts

if __name__ == "__main__":
    s = input("Enter list of integers (comma or space separated): ").strip()
    nums = parse_input(s)
    result = count_multiples(nums)
    print(result)
