class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)  
        post = len(y)
        
        center = int(post/2)
        i=0
        while i < center:
            if y[i] == y[post - 1 -i]:
                i+=1
                continue
            else:
                return False
        return True

# Better solution 
# Convert the number to string and compare it with the reversed string.
# def isPalindrome(self, x: int) -> bool:
# 	if x < 0:
# 		return False
	
# 	return str(x) == str(x)[::-1]

# Fastest Solution
# def isPalindrome(self, x: int) -> bool:
# 	if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
# 		return False
	
# 	result = 0
# 	while x > result:
# 		result = result * 10 + x % 10
# 		x = x // 10
		
# 	return True if (x == result or x == result // 10) else False