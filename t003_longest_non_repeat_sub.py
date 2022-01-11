class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        i1, i2, maxl = 0, 1, 1
        while i1 < l - 1:
            tmp_max = maxl
            while i2 < l:
                # print(i1, i2, s[i1:i2+1], maxl, tmp_max)
                if s[i2] in s[i1:i2]:
                    tmp_max = i2 - i1
                    # i1 += 1
                    break
                i2 += 1
                tmp_max = i2 - i1
            else:
                maxl = i2 - i1
            i1 += 1
            if tmp_max > maxl:
                maxl = tmp_max
            if maxl > l - i1 - 1:
                break
        return maxl

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        max_l = 0
        for i, c in enumerate(s):
            if c not in d:
                l += 1
            else:
                if d[c] < i - l:
                    l += 1
                else:
                    l = i - d[c]
            d[c] = i
            if l > max_l:
                max_l = l
        return max_l



def test_args():
    s = Solution2()
    func = s.lengthOfLongestSubstring
    test_cases = (
        (('abcabcbb',), 3),
        (('bbbb',), 1),
        (('pwwkew',), 3),
        (('',), 0),
        (('ou',), 2),
    )

    return func, test_cases

