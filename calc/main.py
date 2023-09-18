def add(*args):
    return sum(args)


def subtract(a, b):
    return a - b


def mult(a, b):
    return a * b


def division(a: int, b: int) -> float:
    """Divides a by b and returns the result.
    """
    if b == 0:
        raise ZeroDivisionError
    return a / b


if __name__ == '__main__':
    print(f'2 + 3 = {add(2, 3)}')
    print(f'3 - 1 = {subtract(3, 1)}')
    print(f'2 * 3 = {mult(2, 3)}')
