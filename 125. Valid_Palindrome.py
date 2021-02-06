'''
Bruce-Froce:

Time: O(n)
Space: O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #using isalpha and is numeric functions
        clear_str = []
        for item in s:
            if item.isalpha() or item.isnumeric():
                clear_str.append(item.lower())
        length = int(len(clear_str))
        mid = int(length/2)
        for i in range(mid):
            if clear_str[i] != clear_str[length - i - 1]:
                return False
        return True


'''
Two Pointer Solution:

Time: O(n)
Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

'''