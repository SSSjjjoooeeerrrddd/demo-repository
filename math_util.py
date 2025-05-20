def add(x, y):
    """Adds two numbers and returns the result"""
    return x + y

def substract(x, y):
    """Substracts two numbers and returns the result"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the result"""
    return x * y

def divide(x, y):
    """Divides two numbers and returns the result
    Raises ZeroDivisionError if the second number (y) is zero"""
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Wie deelt door nul is een sul.")