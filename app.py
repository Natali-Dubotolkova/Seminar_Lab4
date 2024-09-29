# Define a function 'add_numbers' that takes two arguments: a and b.
def add_numbers(a, b):
    # Check if both 'a' and 'b' are integers using the 'isinstance' function.
    if not (isinstance(a, int) and isinstance(b, int)):
        # If either 'a' or 'b' is not an integer, return an error message.
        return "Inputs must be integers!"
    # If both 'a' and 'b' are integers, return their sum.
    return a + b

# Test the 'add_numbers' function with various input values and print the results.
print(add_numbers(10, 20))     # Valid: Both inputs are integers, and it returns the sum.
print(add_numbers(10, 20.23))  # Invalid: One of the inputs is a float, so it returns an error message.
print(add_numbers('5', 6))     # Invalid: One of the inputs is a string, so it returns an error message.
print(add_numbers('5', '6'))   # Invalid: Both inputs are strings, so it returns an error message.
