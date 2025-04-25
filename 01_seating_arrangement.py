from itertools import permutations

def find_seating_arrangement(guests):
    """
    This function attempts to find a valid circular seating arrangement
    for a group of guests such that each guest is seated next to both of their preferred neighbors.
    
    :param guests: Dictionary where keys are guest names and values are lists of two preferred neighbors.
    :return: A valid circular seating arrangement (list of guests in order), or None if not possible.
    """

    # Get the list of guest names
    guest_list = list(guests.keys())

    # Try all permutations of the guest list to find a valid circular arrangement
    for arrangement in permutations(guest_list):
        valid = True
        n = len(arrangement)
        
        # Check if each guest has their two preferred neighbors adjacent (considering circular table)
        for i in range(n):
            left_neighbor = arrangement[(i - 1) % n]
            right_neighbor = arrangement[(i + 1) % n]
            guest = arrangement[i]
            preferences = guests[guest]

            # Both neighbors must be in the preference list
            if not (left_neighbor in preferences and right_neighbor in preferences):
                valid = False
                break

        if valid:
            return list(arrangement)  # Valid arrangement found

    return None  # No valid arrangement found

# Example input
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

# Find and print the arrangement
result = find_seating_arrangement(guests)

if result:
    print("Valid seating arrangement found:")
    print(" -> ".join(result) + " -> " + result[0])  # Show circular order
else:
    print("No valid seating arrangement is possible.")

