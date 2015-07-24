__author__ = 'Alexander Stoklasa <alexander@stoklasa.net>'

def print_header(num):
    index = 1
    print '+',
    while index <= num:
        print '- - - - +',
        index += 1
    print ''


def print_body(num):
    index2 = 1
    while index2 <= 4:
        index = 1
        print '|',
        while index <= num:
            print '        |',
            index += 1
        print ''
        index2 += 1


def print_grid(x, y):
    i = 1
    while i <= x:
        print_header(y)
        print_body(y)
        i += 1
    print_header(y)

print_grid(4, 4)