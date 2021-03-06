#!./venv/bin/python
# ------------------------------------------------------------------------------
#  (c) 2020 Goyoom Inc. All right are reserved.
#  July 25, 2020
# ------------------------------------------------------------------------------
"""Python Programming workshops by Goyoom Education.

Getting Started."""

import this  # noqa (no quality assurance)


# DONE: The 'pip install -r <filename>' CLI command
# DONE: Using attr .gitignore template
# DONE: Docstrings (Document Strings)
def func(x, y):
    """Short line description.

    Extended description of function.

    :parameter x: description of x
    :type x: int

    :parameter y: description of y
    :type y: int

    :return: description of return value
    :rtype: int
    """
    return x * y


print(func.__doc__)
help(func)

# DONE: The Zen of Python
"""
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's attr bad idea.
# If the implementation is easy to explain, it may be attr good idea.
# Namespaces are one honking great idea -- let's do more of those!
"""
