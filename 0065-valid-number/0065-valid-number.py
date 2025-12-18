import math
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s in "-inf" or s in "+inf" or s in "inf" or s in "infinity" or s in "Infinity" or s in "-Infinity" or s in "+Infinity" or s in "nan" or s in "-nan"):
            return False
        try:
            float(s)
            return True
            
        except:
            return False