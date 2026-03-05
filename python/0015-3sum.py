class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        # i is base/start index
        for i in range(len(nums)-1):
            # exit early
            if nums[i] > 0:
                break
            # avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # j is left
            j = i+1
            # k is right
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # avoid duplicates
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return triplets