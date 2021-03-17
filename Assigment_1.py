import math
# print math.factorial(20)
from scipy import stats
X = stats.binom(5, 0.8) # Declare X to be a binomial random variable
print("Probability at X=4")
print (X.pmf(4),"\n")          # P(X = 4)
print("which is approximately equal to 0.4096(theoritical value)")