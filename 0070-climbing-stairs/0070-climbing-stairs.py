import math
class Solution:
	def climbStairs(self, n: int) -> int:
		o = n
		t = 0
		s = 0
		x = n // 2
		while t <= x:
			# print(n,'  ',o,' ',t)
			s += int(math.factorial(n))/int(math.factorial(o)*math.factorial(t))
			# print(s)
			t += 1
			o -= 2
			n -= 1
		return int(s)