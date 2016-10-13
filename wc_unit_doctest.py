# -*- coding:utf-8 -*-

# Everything is in a docstring!
"""
>>> from wc import fileLine
>>> fileLine('testinputs/test1.txt')
10
>>> from wc import fileWord
>>> fileWord('testinputs/test2.txt')
136
>>> from wc import fileByte
>>> fileByte('testinputs/test2.txt')
766
>>> from wc import getOutput
>>> getOutput('-l-w-c',11,12,23,'test1.txt')
      11      12      23  test1.txt
>>> from wc import stdin
>>> stdin()
(13, 13, 123)
"""

# We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()

