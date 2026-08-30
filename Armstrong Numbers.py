def is_armstrong(num: int) -> bool:
    # Convert number to string to easily get digits and total length (order n)
    num_str = str(num)
    order = len(num_str)

    # Calculate sum of each digit raised to power of 'order'
    total = sum(int(digit) ** order for digit in num_str)

    return total == num


# Example usage
number = int(input("Enter a positive integer: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
