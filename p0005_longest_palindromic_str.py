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


def test_solution():
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
    for in_str, out_str in test_cases:
        print('Testing {}'.format(in_str))
        out = s.longestPalindrome(in_str)
        if out != out_str:
            print(in_str, out_str, out)
            print('Failed!')
            break
    else:
        print('Passed!')
