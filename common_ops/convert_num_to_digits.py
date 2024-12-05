def number_to_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)  # Extract the last digit
        num //= 10              # Remove the last digit using floor division.
    digits.reverse()  # Reverse the digits to get them in the correct order
    return digits

# Example usage
num = 12345
result = number_to_digits(num)
print(result)  # Output: [1, 2, 3, 4, 5]
