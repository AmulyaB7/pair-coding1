class Solution:
    def largeOddNum(self, s: str) -> str:
        ind = -1

        i = 0
        for i in range(len(s) - 1, -1, -1):
            
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        
        return s[i:ind + 1]

solution = Solution()
num = input()
result = solution.largeOddNum(num)
print("Largest odd number:", result)