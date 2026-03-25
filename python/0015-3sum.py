class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            
            # avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums)-1
            while j < k:
                if nums[k] < 0:
                    break

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # avoid duplicates
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                
                elif total > 0:
                    k -= 1
                
                else:
                    j += 1

        return res