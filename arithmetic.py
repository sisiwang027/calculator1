"""Math functions for calculator."""

def bulk_add(p_list):
    acc = p_list[0]
    for i in range(1, len(p_list)):
        acc = add(acc, p_list[i])
    return acc    


def add(num1, num2):
    """Return the sum of the two input integers."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
