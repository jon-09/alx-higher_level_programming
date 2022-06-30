#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    args = argc - 1
    a = 0
    b = 0
    opr = sys.argv[2]
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if opr == '+':
        rtion = add(a, b)
    elif opr == '-':
        rtion = sub(a, b)
    elif opr == '*':
        rtion = mul(a, b)
    elif opr == '/':
        rtion = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, opr, b, rtion))
