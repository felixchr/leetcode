class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')': '(', ']': '[', '}': '{'}
        for i, char in enumerate(s):
            if len(stack) == 0:
                stack.append(char)
            elif char not in p_map:
                stack.append(char)
            elif p_map[char] != stack[-1]:
                return False
            else:
                stack.pop(-1)
        return False if stack else True

def test_solution():
    s = Solution()
    test_cases = (
        ('()', True),
        ('(){}[]', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True)
    )
    for in_str, out in test_cases:
        if s.isValid(in_str) != out:
            print(in_str, out)
            print('Failed!')
            break
    else:
        print('Passed!')
    