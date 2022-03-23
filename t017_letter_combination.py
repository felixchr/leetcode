from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(l1, l2):
            return [ '{}{}'.format(c1, c2) for c1 in l1 for c2 in l2]
        letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        length = len(digits)
        if length == 0:
            return []
        if length == 1:
            return letter_dict.get(digits)
        l1 = letter_dict[digits[0]]
        for char in digits[1:]:
            l2 = letter_dict[char]
            l1 = helper(l1, l2)
        return l1
    
def test_args():
    s = Solution()
    func = s.letterCombinations
    test_cases = (
        ('23', ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ('2', ["a","b","c"]),
        ('', []),
    )
    return func, test_cases
