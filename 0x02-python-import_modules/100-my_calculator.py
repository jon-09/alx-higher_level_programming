#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opr = sys.argv[2]

    if argc == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[3]) 
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
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, opr, b, rtion))
