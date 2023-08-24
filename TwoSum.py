class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype=[0,0]
        for i in range(len(nums)-1): 
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    rtype[0] = i
                    rtype[1] = j
        return rtype
   
