"""Module providing a function printing a result of math operations"""


def calc(string):
    """Function printing results of math operations"""
    try:
        result = eval(string)
    except (ValueError, SyntaxError, ZeroDivisionError, NameError):
        return 'Error'
    return result


if __name__ == '__main__':
    exp = input("Input your mathematical expression: ")
    print(calc(exp))
