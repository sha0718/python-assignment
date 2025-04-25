from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    """
    Calculates the difference in days between two dates.
    
    :param date1_str: First date as a string in dd-mm-yyyy format
    :param date2_str: Second date as a string in dd-mm-yyyy format
    :return: Number of days between the two dates
    """
    # Define the expected date format
    date_format = "%d-%m-%Y"

    try:
        # Parse the string inputs into datetime objects
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)

        # Calculate the difference between the two dates
        difference = abs((date2 - date1).days)  # abs ensures positive number

        return difference

    except ValueError as e:
        # Handle invalid date formats
        return f"Invalid date format. Please use dd-mm-yyyy. Error: {e}"

# Example usage
birthdate = input("Enter your birthdate (dd-mm-yyyy): ")
today = input("Enter today's date (dd-mm-yyyy): ")

days_lived = calculate_date_difference(birthdate, today)

print(f"You have lived for {days_lived} days." if isinstance(days_lived, int) else days_lived)
