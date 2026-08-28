class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        j = len(s)-1
        for i in range(len(s) // 2):
            print(i, j, s[j], s[i])
            if s[j].lower() != s[i].lower():
                return False
            j -= 1
        return True