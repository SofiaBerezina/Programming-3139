"""Module providing a function printing a result of math operations"""


def calc(string):
    """Function printing results of math operations"""
    try:
        res = eval(string)
    except (ValueError, SyntaxError, ZeroDivisionError, NameError):
        return 'Error'
    return res


if __name__ == '__main__':
    s = input("Input your mathematical expression: ")
    print(calc(s))
