class Solution:
    def start(self):
        # parameters
        digits = "9312"
        # ============== answer ==============
        res = []
        n = len(digits)
        dct = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxy"
        }

        if n == 0:
            res = []
        elif n == 1:
            res = list(dct[digits])
        elif n == 2:
            x = dct[digits[0]]
            y = dct[digits[1]]
            res = [(a + b) for a in x for b in y]
        elif n == 3:
            x = dct[digits[0]]
            y = dct[digits[1]]
            z = dct[digits[2]]
            res = [(a + b + c) for a in x for b in y for c in z]
        else:
            x = dct[digits[0]]
            y = dct[digits[1]]
            z = dct[digits[2]]
            w = dct[digits[3]]
            res = [(a + b + c + d) for a in x for b in y for c in z for d in w]

        return res
        # ============== answer ==============


solution = Solution()
print(solution.start())
