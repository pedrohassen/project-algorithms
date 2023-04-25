def find_duplicate(nums):
    nums.sort()

    for num in range(len(nums)):
        if (
            num + 1 >= len(nums)
            or not isinstance(nums[num], int)
            or not isinstance(nums[num + 1], int)
            or nums[num] < 0
        ):
            return False
        if nums[num] == nums[num + 1]:
            return nums[num]
    return False
