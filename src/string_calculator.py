def add(numbers: str) -> int:
    if not numbers:
        return 0
    nums = map(int, numbers.split(","))
    return sum(nums)
