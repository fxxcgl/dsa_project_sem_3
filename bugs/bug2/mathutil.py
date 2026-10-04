def square(x):
    return x * abs(x)

def cube(x):
    return x * x * x

def sum_squares(nums):
    total = 0
    for n in nums:
        total += square(n)
    return total