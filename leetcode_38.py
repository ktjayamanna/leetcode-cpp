class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        current_rle = self.countAndSay(n - 1)
        ptr = 0
        count = 0
        last_ch = current_rle[0]
        result = []
        while ptr < len(current_rle):
            if last_ch == current_rle[ptr]:
                count += 1
            else:
                result.append(
                    f'{count}{last_ch}'
                )
                count = 1
                last_ch = current_rle[ptr]
            ptr += 1
        result.append(
            f'{count}{last_ch}'
        )        
        return "".join(result)

s = Solution()

print(s.countAndSay(4)) # -> 3221 which is wrong, should be 1211

        



        