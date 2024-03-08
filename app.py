import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fun")
parser.add_argument("num1")
parser.add_argument("num2")

args = parser.parse_args()

#print(args.num1, args.num2)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

res = 0
if args.fun == 'add':
    res = add(int(args.num1), int(args.num2))
elif args.fun == 'mul':
    res = mul(int(args.num1), int(args.num2))
else:
    res = sub(int(args.num1), int(args.num2))

print('Result of the operation:', args.fun, res, sep=' ')
print('done')