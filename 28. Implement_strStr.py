'''
(1) string.find() but do not use the libiary fun in the interview
(2) Bruce Force
Scan the haystack, and when it encounters the same position as the first character of the needle, 
check whether the block of the haystack starting from this position and the length of the needle 
is the same as the needle.

        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i     
        return -1
Time: O(n^2)
Space: O(1)

        n, h = len(needle), len(haystack)

        for s in range(h - n + 1):
            if haystack[s: s + n] == needle:
                return s
        return -1

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # https://www.zhihu.com/question/314669016
        # https://blog.csdn.net/coder_orz/article/details/51708389
        # sliding windows
        
        
        
