def is_even(num):
    """
    Check if a given number is even.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0


def is_odd(num):
    """
    Check if a given number is odd.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return not is_even(num)


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is even.")
    elif is_odd(num):
        print(f"{num} is odd.")
    else:
        print("Invalid input.")