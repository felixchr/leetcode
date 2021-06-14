class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest = s[0]
        l_s = len(s)
        for i in range(l_s):
            if i == l_s - 1:
                break
            sub_s = s[i]
            if s[i] == s[i + 1]:
                sub_s = s[i:i+2]
                j = 1
                while i - j >= 0 and i + 1 + j < l_s:
                    if s[i - j] == s[i + 1 + j]:
                        sub_s = s[i - j: i + j + 2]
                        j += 1
                    else:
                        break
            if len(sub_s) > len(longest):
                longest = sub_s
            # print(i, sub_s, longest)
            if 0 < i < l_s - 1 and s[i - 1] == s[i + 1]:
                sub_s = s[i - 1: i + 2]
            else:
                continue
            j = 1
            # print(i, longest)
            while i - 1 - j >= 0 and i + 1 + j < l_s:
                if s[i - 1 - j] == s[i + 1 + j]:
                    sub_s = s[i-j-1: i+j+2]
                    # print(i, j, sub_s, longest)
                    j += 1
                else:
                    break
            if len(sub_s) > len(longest):
                longest = sub_s
        return longest

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        len_s = len(s)
        if len_s <= 1:
            return s
        ret = ''
        for i in range(len(s)):
            tmp = helper(s, i, i)
            if len(tmp) > len(ret):
                ret = tmp
            tmp = helper(s, i, i+1)
            if len(tmp) > len(ret):
                ret = tmp
        return ret

def test_args():
    s = Solution2()
    test_cases = (
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('xabax', 'xabax'),
        ('xabay', 'aba'),
        ('ccc', 'ccc'),
        ('bb', 'bb'),
        ('aaaa', 'aaaa'),
        ('aaabaaaa', 'aaabaaa')
    )
    func = s.longestPalindrome
    return func, test_cases
