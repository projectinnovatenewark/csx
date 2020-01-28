"""
Understand how multi-dimensional matrices work using list comprehensions and loops
"""

# In a simple example of what a multi-dimensional array looks like, you can imagine this:
# Let's look at a simple two-dimensional tabular summary. When rolling two dice, there are
# 36 possible outcomes. We can tabulate these in a two-dimensional table with one die in the
# rows, one die in the columns, and the sum of both die where the two positions meet.

#   -	1	2	3	4	5	6
#   1	2	3	4	5	6	7
#   2	3	4	5	6	7	8
#   3	4	5	6	7	8	9
#   4	5	6	7	8	9	10
#   5	6	7	8	9	10	11
#   6	7	8	9	10	11	12


# In Python, a multi-dimensional table like this can be implemented as a sequence of sequences.
# A table is a sequence of rows. Each row is a sequence of individual cells. This allows us to use
# mathematical-like notation. Where the mathematician might say Ai,j , in Python we can say A[i][j].
# In Python, we want the row i from table A, and column j from that row.

# List of Lists Example. We can build a table using a nested list comprehension. The following
# example creates a table as a sequence of sequences and then fills in each cell of the table.

table = [[0 for i in range(6)] for j in range(6)]
print(table)
for d1 in range(6):
    for d2 in range(6):
        table[d1][d2] = d1+d2+2
print(table)

# This program produced the following output.

# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9],
# [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11], [7, 8, 9, 10, 11, 12]]

# This program did two things. It created a six by six table of zeroes. It then fills this with each
# possible combination of two dice. This is not the most efficient way to do this, but we want to
# illustrate several techniques with a simple example. We'll look at each half in detail.

# The 1st part of this program creates and prints a 6-item list, named table; each item in the table
# is a 6-item list of zeroes. It has a list comprehension & creates an object for each value of j in
# the range of 0 to 6. Each of the objects is a list of zeroes, one for each value of i in the range
# of 0 to 6. After this initialization, the two-dimensional table of zeroes is printed.

# The comprehension can be read from inner to outer, like an ordinary expression. The inner list,
# [ 0 for i in range(6) ], creates a simple list of six zeroes. The outer list,
# [ [...] for j in range(6) ], creates six copies of these inner lists.

# The 2nd part of this program then iterates over all combinations of two dice, filling in each
# cell of the table. This is done as two nested loops, one loop for each of the two dice. The
# outer enumerates all values of one die, d1. The loop enumerates all values of a second die, d2.

# Updating each cell involves selecting the row with table[d1]; this is a list of 6 values. The
# specific cell in this list is selected by ...[d2]. We set this cell to the number rolled on the
# dice, d1+d2+2.

# Additional Examples. The printed list of lists is a little hard to read. The following loop would
# display the table in a more readable form.


for row in table:
    print(row)

# the output would look like

# [2, 3, 4, 5, 6, 7]
# [3, 4, 5, 6, 7, 8]
# [4, 5, 6, 7, 8, 9]
# [5, 6, 7, 8, 9, 10]
# [6, 7, 8, 9, 10, 11]
# [7, 8, 9, 10, 11, 12]

# As an exercise, we'll leave it to the reader to add some features to this to print column and
# row headings along with the contents. As a hint, the "%2d" % value string operation might be
# useful to get fixed-size numeric conversions.

# Explicit Index Values. We'll summarize our table of die rolls, and accumulate a frequency table.
# We'll use a simple list with 13 buckets (numbered from 0 to 12) for the frequency of each
# die roll. We can see that the die roll of 2 occurs just once in our matrix, so we'll expact that
# fq[2] will have the value 1. Let's visit each cell in the matrix and accumulate a frequency table.

# There is an alternative to this approach. Rather than strip out each row sequence, we could
# use explicit indexes and look up each individual value with an integer index into the sequence.

fq = 13*[0]
for i in range(6):
    for j in range(6):
        c = table[i][j]
        fq[c] += 1

# We initialize the frequency table, fq, to be a list of 13 zeroes.

# The outer loop sets the variable i to the values from 0 to 5. The inner loop sets the variable
# j to the values from 0 to 5.

# We use the index value of i to select a row from the table, and the index value of j to select a
# column from that row. This is the value, c. We then accumulate the frequency occurances in the
# frequency table, fq.

# This looks very mathematical and formal. However, Python gives us an alternative, which can
# be somewhat simpler.

# Using List Iterators Instead of Index Values. Since our table is a list of lists, we can make
# use of the power of the for statement to step through the elements without using an index.

fq = 13*[0]
print(fq)
for row in table:
    for c in row:
        fq[c] += 1
print(fq[2:])

# We initialize the frequency table, fq, to be a list of 13 zeroes.

# The outer loop sets the variable row to each element of the original table variable.
# This decomposes the table into individual rows, each of which is a 6-element list.

# The inner loop sets the variable c to each column's value within the row. This decomposes
# the row into the individual values.

# We count the actual occurances of each value, c by using the value as an index into
# the frequency table, fq. The increment the frequency value by 1.

# Mathematical Matrices. We use the explicit index technique for managing the
# mathematically-defined matrix operations. Matrix operations are done more clearly
# with this style of explicit index operations. We'll show matrix addition as an example,
# here, and leave matrix multplication as an exercise in a later section.

m1 = [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]]
m2 = [[2, 4, 6, 0], [1, 3, 5, 0], [0, -1, -2, 0]]
m3 = [4*[0] for i in range(3)]

for i in range(3):
    for j in range(4):
        m3[i][j] = m1[i][j]+m2[i][j]

# In this example we created two input matrices, m1 and m2, each three by four. We
# initialized a third matrix, m3, to three rows of four zeroes, using a comprehension.
# Then we iterated through all rows (using the i variable), and all columns (using the j variable)
# and computed the sum of m1 and m2.
