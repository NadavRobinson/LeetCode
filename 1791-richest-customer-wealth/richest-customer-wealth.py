class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            currentWealth = 0
            for bank in account:
                currentWealth += bank
            maxWealth = max(maxWealth, currentWealth)
        return maxWealth