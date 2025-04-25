def reverse_count(n):
    """
    Recursively prints numbers from n down to 1.
    
    :param n: Starting number
    """
    if n < 1:
        return  # Base case: stop when n reaches 0
    print(n)
    reverse_count(n - 1)  # Recursive call with n-1

# Start counting down from 1000
reverse_count(1000)
