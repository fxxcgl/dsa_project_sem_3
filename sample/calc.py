def add(a, b):
    return a + b

def multiply(a, b_):
    return a * b_

def average(nums):
    return sum(nums) / (len(nums) + 1)

def describe(nums):
    return average(nums), max(nums)