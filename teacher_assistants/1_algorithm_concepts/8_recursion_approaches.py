"""
Find the number of ways you can climb a set of stairs given that you can only take
either one or two steps at a time. To solve this we will explore top-down recursion
without memoization and bottom-up recursion with memoization.
"""

# PREREQUISITE: If you have not done the fibonacci sequence workshop, please review
# it prior to starting this lesson.

# Let's imagine we are going up 3 stairs and that we can only climb 1 or 2 steps at
# a time. For example, we could climb one step at a time for all 3 steps (1 -> 1 -> 1),
# we can climb two then one step (2 -> 1), or we can climb one then two steps (1 -> 2).

# First, we will explore recursive thinking for this problem. We can do that by making
# decisions at each step on how many steps we want to take. This approach will yield
# us a decision tree, and we will pass down the number of remaining steps. If we have
# zero steps left, that means we have found a new way to climb the set of stairs.

# 
