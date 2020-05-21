#https://leetcode.com/problems/valid-parentheses/description

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(':')',
                '{':'}', 
                '[':']'}
        _stack = list()
        for i in s:
            if i in pairs:
               _stack.append(i)
            else:
               if _stack:
                   if pairs[_stack.pop()] != i:
                        return False
               else:
                   return False
        return len(_stack) == 0
