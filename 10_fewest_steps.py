def sort_letters_digits(s):
    """
    Separates letters and digits from the input string,
    sorts them individually, and concatenates letters first, then digits.
    
    :param s: Input string with letters and digits
    :return: Concatenated sorted string
    """
    letters = sorted([ch for ch in s if ch.isalpha()])  # Extract and sort letters
    digits = sorted([ch for ch in s if ch.isdigit()])   # Extract and sort digits
    return ''.join(letters + digits)  # Combine both lists into one string

# Example usage
input_str = "B4A1D3"
output = sort_letters_digits(input_str)
print("Output:", output)
