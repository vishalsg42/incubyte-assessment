def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    nums = map(int, numbers.split(","))
    return sum(nums)
