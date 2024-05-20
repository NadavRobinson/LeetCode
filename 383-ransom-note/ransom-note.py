class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        for char in magazine:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1 
        
        for char in ransomNote:
            if char in my_dict and my_dict[char] > 0:
                my_dict[char] -= 1
            else:
                return False
        return True