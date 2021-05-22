import sys


def z(x): return 0


def pred(x): return 0 if x == 0 else x - 1


def subtr(x, y): return x if y == 0 else pred(subtr(x, y - 1))


def add(x, y): return x if y == 0 else add(x, y - 1) + 1


def mult(x, y): return add(x, mult(x, y - 1))


def prf(f): return lambda x, y, z: z if y == 0 else prf(
    f)(x, pred(y), f(x, z))


def mult_with_prf(x, y): return prf(lambda xt, yt: add(xt, yt))(x, y, 0)


def pow_with_prf(x, y): return prf(
    lambda xt, yt: mult_with_prf(xt, yt))(x, y, 1)


# RecursionError: maximum recursion depth exceeded in comparison if |x| > 1
# but it should work right
# for all power functions it is indicated that the exponent is greater than zero, I will assume that for mine too
# prf - primitive recursive function
def var15(x): return pow_with_prf(3, pow_with_prf(x, 3))


# crutch
def var15_with_minus(x): return '1/' + str(pow_with_prf(3, pow_with_prf(-x, 3)
                                                        )) if x < 0 else pow_with_prf(3, pow_with_prf(x, 3))


def main(f_arg, s_arg):
    # print(mult_with_prf(f_arg, s_arg))
    # print(pow_with_prf(f_arg, s_arg))
    # sys.setrecursionlimit(3000)
    print(var15_with_minus(f_arg))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
