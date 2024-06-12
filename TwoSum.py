from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashTable
        hashTable={}
        
        #length of nums
        n = len(nums)

        #Iterate through array 
        for i in range(n):
            complement = target - nums[i]
            if complement in hashTable:
                return [hashTable[complement],i]
            hashTable[nums[i]] = i  