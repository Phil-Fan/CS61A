HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if 0 <= x < 10:
        return 1 if x == 8 else 0
    else :
        return num_eights(x%10) + num_eights(x//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def calc(x):
        if 0 <= x < 8:
            return 0
        return 1+calc(x-1) if (num_eights(x) >= 1 or x % 8 == 0) else calc(x-1)
    if n == 1:
        return 1

    print("DEBUG: ",n,calc(n))
    return pow(-1,calc(n-1)) + pingpong(n-1)



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    digit_list = list(map(int,str(n)))
    #print(digit_list)
    a = [i for i in range(digit_list[0],digit_list[-1]+1) if digit_list.count(i) == 0]
    print(len(a))


def next_largest_coin(coin):
    """Return the next coin.
    """
    if coin == 5:
        return 1
    elif coin == 10:
        return 5
    elif coin == 25:
        return 10
    else:
        return coin



def count_coins(total):#放苹果问题 #背包问题
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def f(n,m):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif m == 1:
            return 1
        else:
            return f(n-m,m) + f(n,next_largest_coin(m))
    return f(total,25)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #return (lambda f: lambda n: 1 if n == 1 else mul(n, f(f)(sub(n, 1))))(lambda f: lambda n: 1 if n == 1 else mul(n, f(f)(sub(n, 1))))

    return (lambda f: lambda n: 1 if n == 1 else mul(n,f(f)(n-1)))(lambda f: lambda n: 1 if n == 1 else mul(n,f(f)(n-1)))