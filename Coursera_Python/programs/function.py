def printdigit(num):
    number = list()
    n = num
    str = ''
    while n != 0:
        r = n % 10
        n /= 10
        number.append(r)
    # print number
    for i in reversed(range(len(number))):
        if number[i] == 1:
            str += 'ONE '
        elif number[i] == 2:
            str += 'TWO '
        elif number[i] == 3:
            str += 'THREE '
        elif number[i] == 4:
            str += 'FOUR '
        elif number[i] == 5:
            str += 'FIVE '
        elif number[i] == 6:
            str += 'SIX '
        elif number[i] == 7:
            str += 'SEVEN '
        elif number[i] == 8:
            str += 'EIGHT '
        elif number[i] == 9:
            str += 'NINE '

    print(str)


def prime(num):

    i = 2

    while i <= num:
        isprime = True

        for j in range(2, (i/2 + 1)):
            if (i % j) == 0:
                isprime = False
                break

        if isprime:
            print("CALLED FOR %s" % i)
            printdigit(i)

        i += 1


def main():
    num = input('Enter a number: ')
    prime(num)

if __name__ == "__main__":
    main()