'''
We could still apply the [Hash table] approach, but it costs us O(n) extra space, plus it does not make use of the 
fact that the input is already sorted.

There are two ways to do it, the best and quickest one is two pointers

Ai + Aj > target. 
Ai + Aj < target. 
Ai + Aj == target. We have found the answer.

Time: O(n)
Space: O(1)

'''

def twoSum(nums, target):
        low, high = 0, len(nums) -1
        
        while(low < high):
            if nums[low] + nums[high] == target:
                return [low+1, high+1]
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        return []

print(twoSum([2,7,11,15], 9))


'''
The binary search solution

Time: O(nlogn)
Space: O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            num = nums[i]
            num2 = target - num
            if self.binary_search_recursive(nums, num2, 0, len(nums)-1) != -1 and i != self.binary_search_recursive(nums, num2, 0, len(nums)-1):
                return sorted([self.binary_search_recursive(nums, num2, 0, len(nums)-1)+1, i+1])
            else:
                continue
        return []
        
    
    
    def binary_search_recursive(self, array, target, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        
        if target == array[mid]:
            return mid
        if target < array[mid]:
            return self.binary_search_recursive(array, target, start, mid-1)
        else:
            return self.binary_search_recursive(array, target, mid+1, end)
'''