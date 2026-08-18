import math

def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    elif op == 'prod':
        return math.prod(args)
    
op = input().strip()
args = map(int, input().split())

print(apply_op(op, *args))