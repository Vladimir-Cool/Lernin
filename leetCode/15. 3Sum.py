from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result_list = list()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            print(left)
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                if [nums[i], nums[left], nums[right]] not in result_list:
                    result_list.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result_list


def threeSum2(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        print("---target---")
        print(target)
        seen = set()

        for j in range(i + 1, len(nums)):
            complement = target - nums[j]
            print("---complement---")
            print(complement)
            if complement in seen:
                if [nums[i], nums[j], complement] not in result:
                    result.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
    return result


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-1, 0, -1, -2, -1, -4]
# nums = [1, -1, -1, 0]
# nums = [0, 0, 0, 0]
nums = [3, 0, -2, -1, 1, 2]
# print(threeSum(nums))
print(threeSum(nums))
