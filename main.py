from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for idxMain in range(length - 1):
        for idxSecondary in range (idxMain + 1, length):
            if nums[idxMain] + nums[idxSecondary] == target:
                return [idxMain, idxSecondary]
    return