from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, ans, string):
            if left > right:
                return
            elif left == right == 0:
                ans.append(string)
                return
            else:
                if left:
                    dfs(left-1, right, ans, string+'(')
                if right:
                    dfs(left, right-1, ans, string+')')
        if not n:
            return []
        left, right, ans = n, n, []
        dfs(left, right, ans, '')
        return ans


def test_args():
    s = Solution()
    func = s.generateParenthesis
    test_cases = (
        (1, ['()']),
        (2, ['(())', '()()']),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
    )
    return func, test_cases