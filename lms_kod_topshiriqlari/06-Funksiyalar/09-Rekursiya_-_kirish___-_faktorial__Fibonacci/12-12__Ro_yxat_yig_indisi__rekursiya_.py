nums = list(map(int, input().split()))
def Is(a):
    if not a:
        return 0
    return a[0] + Is(a[1:])
print(Is(nums))