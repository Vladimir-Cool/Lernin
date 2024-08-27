
def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = dict()
    for index in range(len(nums)):
        if not nums[index] in hashMap.keys():
            hashMap[nums[index]] = list()
            hashMap[nums[index]].append(index)
        else:
            hashMap[nums[index]].append(index)

        check_num = target - nums[index]
        if check_num in hashMap.keys():
            if (len(hashMap[check_num]) > 1):
                return [index, hashMap[check_num][0]]
            elif (len(hashMap[check_num]) == 1):
                if nums[index] != check_num:
                    return [index, hashMap[check_num][0]]


# print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))