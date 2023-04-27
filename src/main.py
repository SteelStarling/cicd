"""
System to check how far any given number is from The Answer (42).
Author: Taylor Hancock
"""

""" The Answer to Life, the Universe, and Everything """
The_Correct_Answer = 42


def check_distance(num: int) -> int:
    """ Return the distance from num to The Answer """
    return abs(num - The_Correct_Answer)


def distance_string(num: str, error_msg: str) -> str:
    """ Return a string indicating the distance from any given num to The Answer (or if it's related to The Answer), or
        the provided error message if num is not a number. """
    if num.isnumeric():
        distance = check_distance(int(num))
        return f"{num} is {'The Answer!' if distance == 0 else f'{distance} away from The Correct Answer'}"
    else:
        return error_msg


if __name__ == "__main__":
    print(distance_string("42", "Not a number"))
