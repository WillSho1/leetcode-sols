class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        i = 0
        j = len(numbers)-1

        while i < j:
            total = numbers[i] + numbers[j]

            # zone in on target
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                # 1-indexed
                return [i+1, j+1]

        return None