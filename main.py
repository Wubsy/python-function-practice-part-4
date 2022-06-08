# I could just use max() but for the sake of using only what we've been taught
# I've opted to use this ugly bit of code
# I'm also not using iterative nor recursive


def max_num(one, two, three):
    if one > two:
        if one > three:
            return one
        else:
            return three
    elif two > three:
        if two > one:
            return two
        else:
            return one
    elif three > one:
        return three


def mult_list(in_list: list):
    total = 0
    for i in range(0, len(in_list)):
        if i == 0:
            total = in_list[0]
            continue
        total *= in_list[i]
    return total


# This works by multiplying the first two numbers,
# appending the number to the end of the list, removing the first two,
# and then running it through the function again.
# When only one int remains in the list, it is returned.
def recurs_mult_list(in_list: list):
    if len(in_list) != 1:
        in_list.append(in_list[0] * in_list[1])
        del in_list[0:2]
        recurs_mult_list(in_list)
    return in_list[0]


# Iteration and recursion can be totally ignored by having it be read backwards.
def rev_string(string):
    return string[::-1]


def iter_rev_string(string):
    str_return = ""
    for i in range(len(string), 0, -1):
        str_return += string[i-1]
    return str_return


def num_within(num, start, end):
    if start <= end:
        if num >= start:
            if num <= end:
                return True
    return False


"""
I had to look this up.
Source:
https://www.geeksforgeeks.org/python-program-to-print-pascals-triangle/

I first tried this using the powers of 11 method but it breaks down as soon as you go above 9
Link to that problem:
https://ide.geeksforgeeks.org/3xwG2iJyN0

I intend to redo this when better explanation on approach is given
"""


def pascal(n):
    for i in range(n + 1):
        for j in range(n - i):
            print(' ', end='')

        c = 1
        for j in range(1, i + 1):
            print(c, ' ', sep='', end='')
            c = c * (i - j) // j
        print()


# Expected output 16
print(max_num(15, 12, 16))

# Expected output 416
print(mult_list([8, 4, 13]))
print(recurs_mult_list([8, 4, 13]))

# Expected output gfedcba
print(rev_string("abcdefg"))
print(iter_rev_string("abcdefg"))

# Expected output True
print(num_within(3, 2, 4))

# Expected output True
print(num_within(3, 1, 3))

# Expected output False
print(num_within(10, 2, 5))

"""
Expected output

    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
"""
pascal(5)
