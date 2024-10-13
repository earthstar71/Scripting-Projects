nums = [34, 67, 89, 345, 52, 945]

def calc_min(nums):
    length = len(nums)
    for i in range(length - 1):
        f = nums[0]
        l = nums[-1]
        if f < l:
            nums.pop()
            l = nums[-1]
        elif f > l:
            nums.pop(0)
            f = nums[0]
    if len(nums) == 1:
        print(nums[0])
calc_min(nums)