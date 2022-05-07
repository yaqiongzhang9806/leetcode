#Iterative Approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right
        
        return -1
		

#Recursive Approach
class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        return self.binarySearch(nums, target, 0, len(nums) -1) 
    
    
    def binarySearch(self, nums: List[int], target: int, left: int, right : int) -> int:
        if nums[left] == target:
            return left
        
        if nums[right] == target: 
            return right
        
        if left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                return self.binarySearch(nums, target, left, middle - 1)
            else:
                return self.binarySearch(nums, target, middle + 1, right)
            
        return -1 
    