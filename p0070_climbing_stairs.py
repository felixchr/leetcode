class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, mem):
            if n<=3:
                mem[n-1] = n
                ret = n
            if mem[n-1] != 0:
                return mem[n-1]
            else:
                ret = dp(n-1, mem) + dp(n-2, mem)
                mem[n-1] = ret
            return ret
        mem = [0] * n
        return dp(n, mem)

class Solution2:
    def climbStairs(self, n: int) -> int:
        def dp(n, mem):
            if n<= 3:
                mem[n-1] = n
            else:
                mem[n-1] = mem[n-3] + mem[n-2]
                # return dp(n-2, mem) + dp(n-1, mem)
        mem = [0] * n
        for i in range(1, n+1):
            dp(i, mem)
        return mem[n-1]


def test_args():
    s = Solution2()
    func = s.climbStairs
    test_cases = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5)
    )
    return func, test_cases