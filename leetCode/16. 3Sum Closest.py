from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    result = 0
    min_distance = 1000000
    len_list = len(nums)

    for i in range(len_list - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len_list - 1
        while left < right:
            check_sum = nums[i] + nums[left] + nums[right]
            print(
                f"{check_sum}: i = {nums[i]}: left = {nums[left]}: right = {nums[right]}"
            )
            if check_sum == target:
                return target

            if abs(check_sum - target) < min_distance:
                result = check_sum
                min_distance = abs(check_sum - target)

            if check_sum < target:
                left += 1
            else:
                right -= 1

    return result


nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
print(threeSumClosest(nums, -2))
