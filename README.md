# String Calculator TDD Kata

This is a solution to the **String Calculator TDD Kata**, implemented in Python. The goal of this project is to demonstrate **Test-Driven Development (TDD)** practices by incrementally building a simple string calculator with comprehensive tests.

---

## **Problem Description**

The task is to create a method `add(numbers: str) -> int` that calculates the sum of numbers in a string based on specific rules:

1. The input is a string of numbers separated by commas (`,`) or newlines (`\n`).
2. The method should:
   - Return `0` for an empty string.
   - Handle one or more numbers.
   - Allow a custom delimiter defined in the format `//[delimiter]\n[numbers...]`.
   - Throw an exception if negative numbers are encountered, showing all negative numbers in the exception message.
   - Ignore numbers greater than `1000`.

---

## **Features**

1. **Basic Functionality**:
   - Input: `""` → Output: `0`
   - Input: `"1"` → Output: `1`
   - Input: `"1,2"` → Output: `3`

2. **Newline as Delimiter**:
   - Input: `"1\n2,3"` → Output: `6`

3. **Custom Delimiters**:
   - Input: `"//;\n1;2"` → Output: `3`
   - Input: `"//[***]\n1***2***3"` → Output: `6`

4. **Negative Numbers**:
   - Input: `"1,-2,-3"` → Exception: `"negative numbers not allowed: -2,-3"`

5. **Ignore Numbers > 1000**:
   - Input: `"2,1001"` → Output: `2`

6. **Edge Cases**:
   - Input with spaces, consecutive delimiters, or special characters as delimiters.

---

## **Getting Started**

### **Prerequisites**
- Python 3.x
- `pytest` for testing

Install dependencies:
```bash
pip install -r requirements.txt
```

