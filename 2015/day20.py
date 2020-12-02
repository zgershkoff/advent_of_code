# 2015 day 20

# This problem asks us to find divisors of a number.
# I used sage because this seems like a widely studied number theory
# thing and I don't think I'll make an implementation better than
# existing ones.

# Problem 1:
"""
sage: i = 0
sage: while True:
....:     i += 1
....:     if sum(divisors(i)) * 10 >= 29000000:
....:         break
....:
sage: i
"""

# Problem 2:
"""
sage: i = 0
sage: while True:
....:     i += 1
....:     divs = [d for d in divisors(i) if d * 50 >= i]
....:     if sum(divs) * 11 >= 29000000:
....:         break
....:
sage: i
"""
