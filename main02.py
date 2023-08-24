from typing import List

def splitArray(nums: List[int], X: int) -> List[List[int]]:
    subArrays = []
    currentSubArray = []
    subSum = 0
    for num in nums:
        if subSum + num <= X:
            currentSubArray.append(num)
            subSum += num
        else:
            subArrays.append(currentSubArray)
            currentSubArray = []
            currentSubArray.append(num)
            subSum = num
    subArrays.append(currentSubArray)
    return subArrays

nums = [5, 3, 4, 5, 6, 4]
X = 9
subArrays = splitArray(nums, X)

print("Подмассивы с суммой менее или равной", X, ":")
for subArray in subArrays:
    print(subArray)