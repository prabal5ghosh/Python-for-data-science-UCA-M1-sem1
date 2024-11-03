def plus(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except TypeError:
        return None


def square(a):
    return a**2
