"""
McCarthy 91 function
"""


def fun(n, c, cnt):
    """
    McCarthy function which performs the calculations
    """
    if c != 0:
        if n > 100:
            return fun(n - 10, c - 1, cnt + 1)
        else:
            return fun(n + 11, c + 1, cnt + 1)
    else:
        print(cnt)
        return n


def main():
    """
    main method which calls fun method
    """
    n = input('Enter a number: ')
    res = fun(n, 1, 0)
    print(res)


if __name__ == "__main__":
    main()
