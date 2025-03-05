class Solution:
    '''
    param:
        int n
    return:
        the number of colored cells that will occur after n minutes
    function:
        when n = 1, there is 1 colored square
        as n increase the number of square increases by some multiple of 4
        when n = 2, 4 more squares get added
        when n = 3, 12 more squares get added
        when n = 4, 24 more sqaures get added
        when n = 5, 40 more sqaures get added
        so all of theses are multiples of 4
        and 40/5 = 8 = 2 * 4
        and 24/4 = 6 = 2 * 3 
        and 12/3 = 4 = 2 * 2
        and 4/2 = 2 = 2 * 1
        and 1/2 = 0 = 2 * 0
    '''
    def coloredCells(self, n: int) -> int:
        return 1+2*(n-1)*n

soultion = Solution()

n = 1
print(soultion.coloredCells(n))

n = 2
print(soultion.coloredCells(n))
