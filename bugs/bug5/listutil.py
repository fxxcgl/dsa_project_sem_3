def largest(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best

def smallest(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best

def spread(nums):
    return largest(nums) - smallest(nums)
