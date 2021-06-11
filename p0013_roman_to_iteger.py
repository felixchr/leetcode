class Solution:
    def romanToInt(self, s: str) -> int:
        tmpS = s
        total = 0
        rToiDict={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        specials = {
            'C': ('M', 'D'),
            'X': ('C', 'L'),
            'I': ('X', 'V')
        }
        while tmpS:
            char = tmpS[0]
            if len(tmpS) == 1:
                total += rToiDict[char]
                return total
            if char in specials and tmpS[1] in specials[char]:
                total += (rToiDict[tmpS[1]] - rToiDict[char])
                tmpS = tmpS[2:]
            else:
                total += rToiDict[char]
                tmpS = tmpS[1:]
        return total     

def test_solution():
    s = Solution()
    try:
        for roman, number in (('III', 3), ('IV', 4), ('IX', 9), ('LVIII', 58), ('MCMXCIV', 1994)):
            assert s.romanToInt(roman) == number
    except Exception:
        print(roman, number)
        print('Failed!')
    else:
        print('Passed!')

def test_args():
    s = Solution()
    func = s.romanToInt
    test_cases = (
        ('III', 3), 
        ('IV', 4), 
        ('IX', 9), 
        ('LVIII', 58), 
        ('MCMXCIV', 1994)
    )
    return func, test_cases