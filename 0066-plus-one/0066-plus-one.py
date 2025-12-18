class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new="".join(map(str,digits))
        new=str(int(new)+1)
        return list(map(int,new))
