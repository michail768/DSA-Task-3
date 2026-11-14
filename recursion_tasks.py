#(a) To find the sum of first $N$ natural numbers
def sum_natural(n):
  # Base case: if n is 1 or less, return n
  if n <= 1:
    return n
  # Recursive step: n + sum of (n - 1)
  return n + sum_natural(n - 1)


# Example usage:
# sum_natural(5) -> 5 + 4 + 3 + 2 + 1 = 15
print("Sum of first 5 natural numbers:", sum_natural(5))

#------------------------------------------------------------------


#(b) To find the factorial of a number
def factorial(n):
  # Base case: factorial of 0 or 1 is 1
  if n == 0 or n == 1:
    return 1
  # Recursive step: n * factorial of (n - 1)
  return n * factorial(n - 1)


# Example usage:
# factorial(5) -> 5 * 4 * 3 * 2 * 1 = 120
print("Factorial of 5:", factorial(5))

#------------------------------------------------------------------



#(c) To find the Nth term of a Fibonacci series
def fibonacci_nth(n):
  # Base cases: 0th term is 0, 1st term is 1
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  # Recursive step: sum of the previous two terms
  return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)


# Example usage (0-indexed position):
# 6th term: 0, 1, 1, 2, 3, 5, 8 -> 8
print("6th term of Fibonacci series:", fibonacci_nth(6))

#------------------------------------------------------------------



#(d) To generate N terms of a Fibonacci series
def generate_fibonacci_series(n, current=0, series=None):
  if series is None:
    series = []

  # Base case: stop when we have generated n terms
  if current >= n:
    return series

  # Append terms using the recursive nth function defined above
  series.append(fibonacci_nth(current))

  # Recursive step for the next term
  return generate_fibonacci_series(n, current + 1, series)


# Example usage:
# Generate first 7 terms
print("First 7 terms of Fibonacci series:", generate_fibonacci_series(7))
# Output: [0, 1, 1, 2, 3, 5, 8]

