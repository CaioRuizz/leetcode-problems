class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        temp = ''
        temp = ''.join([i for i in s if i in chars])
        return temp == temp[::-1]