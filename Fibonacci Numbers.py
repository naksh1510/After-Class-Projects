def fibonacci(n):
    # Base cases: return n directly for 0 and 1
    if n <= 1:
        return n
    # Recursive step: sum of the previous two terms
    return fibonacci(n - 1) + fibonacci(n - 2)

# Number of terms to display
n_terms = 15

# Print the sequence
print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")