class Solution:
    def intToEnglish(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ret = []
        for level, word in enumerate(('', 'Thousand', 'Million', 'Billion')):
            minor = (num // (1000 ** level)) % 1000
            if minor:
                if word:
                    ret.insert(0, word)
                ret.insert(0, self._minor_translate(minor))
            if num // (1000 ** (level + 1)) == 0:
                break
        return ' '.join(ret)

    def _minor_translate(self, number: int) -> str:
        if number > 1000 or number < 0:
            raise ValueError('Valid number should be 0-999')
        smaller_words = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
            'Eighteen', 'Nineteen')
        tens_words = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety')
        n1 = number // 100
        ret = []
        if n1:
            ret.append('{} Hundred'.format(smaller_words[n1 - 1]))
        n2 = number % 100
        if 0 < n2 < 20:
            ret.append(smaller_words[n2 - 1])
        elif n2:
            n3 = n2 // 10
            ret.append(tens_words[n3 - 2])
            n4 = n2 % 10
            if n4:
                ret.append(smaller_words[n4 - 1])
        return ' '.join(ret)
def test_solution():
    s = Solution()
    test_nums = (0, 11, 25, 113, 189, 500, 1015, 1089, 50000, 1000000, 10000001, 12345678000)
    for num in test_nums:
        print(num, s.intToEnglish(num))
