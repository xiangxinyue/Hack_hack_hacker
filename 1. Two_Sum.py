'''
Bruce-force solution:
using double for loop to do it

Time Complexity: O(n^2)
Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    return [i, j]
                else:
                    continue
        
        return []

'''

'''
Hash-map solution:

Time Complexity: O(n)
Space Complexity: O(n)

'''
def twoSum(nums, target):
        hash_table = {}
        #https://www.geeksforgeeks.org/enumerate-in-python/
        for i, num in enumerate(nums): 
            num2 = target - num
            if num2 in hash_table:
                return([hash_table[num2], i])# the order do not influence the results
            else:
                hash_table[num] = i
        
        return ([])

'''
Testing:
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
print(twoSum([2,7,11,15], 9))