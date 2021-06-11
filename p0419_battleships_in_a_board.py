from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        total = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    tmp_count = 0
                    if i == 0 or (i > 0 and board[i-1][j] == '.'):
                        tmp_count += 1
                    if j == 0 or (j > 0 and board[i][j-1] == '.'):
                        tmp_count += 1
                    if tmp_count == 2:
                        total += 1
        return total

def test_args():
    s = Solution()
    func = s.countBattleships
    test_cases = (
        (([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]],), 2),
        (([["."]],), 0)
    )
    return func, test_cases