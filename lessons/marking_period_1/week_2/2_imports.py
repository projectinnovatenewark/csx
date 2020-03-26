"""
Importing other files
"""

# You can import data or functions from files that you yourself defined.
# In this folder theres a file called importable_stuff.py . Let's import
# the file and use things from it.

import importable_stuff

# The most straightforward way to import a file is:
# `import importable_stuff`
# Then, to access the constant `DAYS_OF_WEEK` from that file,
# you would do so with "dot notation". For example, in this import case,
# you would find that constant using print(importable_stuff.DAYS_OF_WEEK)

# you could also rename imports such as:
# `import importable_stuff as week` then refer to that file as `week`

# Additionally, say you just wanted to import the DAYS_OF_WEEK constant
# instead of the whole file. Then, you could do the following:
# `from importable_stuff import DAYS_OF_WEEK`

# You could also do the above and rename it with `as`, by doing the following:
# `from importable_stuff import DAYS_OF_WEEK as week`

# TODO: Try each of the above methods for importing and test them by printing
# TODO: your import.
