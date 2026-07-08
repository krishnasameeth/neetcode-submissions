class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(start_index, path):
            if start_index == len(digits):
                res.append("".join(path))
                return

            next_digit = digits[start_index]
            for letter in phone_map[next_digit]:
                path.append(letter)
                dfs(start_index + 1, path)
                path.pop()
        if len(digits) == 0:
            return []
        dfs(0, [])
        return res