def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)


def print_num(n):
    print(n)


def do_num(f, n):
    f(n)
    f(n)


do_num(print_num, 1)
