nums = [int(x) for x in input().split()]

nums.sort()

medium_index = len(nums) // 2
print(nums[medium_index])