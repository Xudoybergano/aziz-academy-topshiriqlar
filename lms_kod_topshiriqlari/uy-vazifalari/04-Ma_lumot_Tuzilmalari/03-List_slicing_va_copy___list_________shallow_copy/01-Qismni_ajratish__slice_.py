import sys
lines = sys.stdin.read().splitlines()
if lines:
        
    nums = lines[0].split()
    a = int(lines[1])
    b = int(lines[2])
    
    print(*(nums[a:b]))
