from math import prod

def add(*args):
    return sum(args)


def subtract(a, b):
    return a - b


def mult(*args:float) -> float:
    """Multiply a list of numbers together

    Returns:
        float: The product of the numbers
    """
    return prod(args)


if __name__ == '__main__':
    print(f'2 + 3 = {add(2, 3)}')
    print(f'3 - 1 = {subtract(3, 1)}')
    print(f'2 * 3 = {mult(2, 3)}'
