class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        num = 0
        i = len(s) - 1
        while i >= 0:
            if i - 1 >= 0 and map[s[i]] > map[s[i - 1]]:
                num = num + (map[s[i]] - map[s[i - 1]])
                i = i - 1
            else:
                num = num + map[s[i]]
            i = i - 1
        return num
