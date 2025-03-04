class Solution:
    '''
    param:
        int n
    return:
        true -> if n is a sum of power of three
        false -> otherwise
    function:
        given an int, n, the function converts n into a base of 3 
        if the ternary encounter a remainder besides 0 or 1
        it returns false 
    '''
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 > 1:
                return False
            n //= 3
        return True

soltuion = Solution()

n = 12
print(soltuion.checkPowersOfThree(n))

n = 91
print(soltuion.checkPowersOfThree(n))

n = 21
print(soltuion.checkPowersOfThree(n))