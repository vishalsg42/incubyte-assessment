def add(numbers: str) -> int:
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")

    numbers = numbers.replace("\n", ",")
    nums = list(map(int, numbers.split(",")))

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

    return sum(nums)
