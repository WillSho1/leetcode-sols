class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # ch2 is the prioritized second character in first run
        ch1, ch2 = 'a', 'b' 
        val1, val2 = x, y
        if x < y:
            ch1, ch2 = 'b', 'a'
            val1, val2 = y, x
        stack = []
        score = 0

        # run 1 - build stack and remove ch1ch2
        for c in s:
            if c == ch2 and stack and stack[-1] == ch1:
                stack.pop()
                score += val1
            else:
                stack.append(c)
        
        # go through remaining stack, cound ch2 occurence and score for each ch1
        ch2_count = 0
        for c in stack:
            if c == ch1 and ch2_count:
                ch2_count -= 1
                score += val2
            elif c == ch2:
                ch2_count += 1
            else:
                ch2_count = 0
        
        return score