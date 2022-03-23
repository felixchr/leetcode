class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l+1:r]
        len_s = len(s)
        if len_s <= 1:
            return s
        ret = ''
        for i in range(len_s):
            tmp_p = helper(s, i, i)
            if len(tmp_p) > len(ret):
                ret = tmp_p
            tmp_p = helper(s, i, i+1)
            if len(tmp_p) > len(ret):
                ret = tmp_p
            if len_s - i < len(ret) / 2:
                break
        return ret

def test_args():
    s = Solution()
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