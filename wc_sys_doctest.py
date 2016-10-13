# -*- coding:utf-8 -*-

# Everything is in a docstring!
"""
>>> import subprocess
>>> print subprocess.check_output('python wc.py testinputs/test3.txt',shell=True).rstrip()
       8     142     824  testinputs/test3.txt
>>> print subprocess.check_output('python wc.py -l testinputs/test3.txt',shell=True).rstrip()
       8                  testinputs/test3.txt
>>> print subprocess.check_output('python wc.py -l -w testinputs/test3.txt',shell=True).rstrip()
       8     142          testinputs/test3.txt
>>> print subprocess.check_output('python wc.py -l -w -c testinputs/test3.txt',shell=True).rstrip()
       8     142     824  testinputs/test3.txt
>>> print subprocess.check_output('python wc.py testinputs/test3.txt testinputs/test1.txt',shell=True).rstrip()
       8     142     824  testinputs/test3.txt
      10      10      19  testinputs/test1.txt
      18     152     843  total
>>> print subprocess.check_output('python wc.py -l testinputs/test3.txt testinputs/test1.txt',shell=True).rstrip()
       8                  testinputs/test3.txt
      10                  testinputs/test1.txt
      18                  total
>>> print subprocess.check_output('python wc.py -l -w testinputs/test3.txt testinputs/test1.txt',shell=True).rstrip()
       8     142          testinputs/test3.txt
      10      10          testinputs/test1.txt
      18     152          total
>>> print subprocess.check_output('python wc.py testinputs/test3.txt testinputs/test1.txt testinputs/test2.txt',shell=True).rstrip()
       8     142     824  testinputs/test3.txt
      10      10      19  testinputs/test1.txt
       5     136     766  testinputs/test2.txt
      23     288    1609  total
"""

# We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()

