import sys

def solve():
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        print([])
        return
    
    positive_nums = [x for x in nums if x > 0]
    print(positive_nums)
    
if __name__ == '__main__':
    solve()