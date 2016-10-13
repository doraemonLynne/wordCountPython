# -*- coding:utf-8 -*-

# Everything is in a docstring!
"""
>>> import subprocess
>>> print subprocess.check_output('python wc.py test1.txt test2.txt',shell=True).rstrip()
   10      10      19   test1.txt
  1080   10104   66735  test2.txt
  1090   10114   66754  total
>>> print subprocess.check_output('python wc.py -w test1.txt test2.txt',shell=True).rstrip()
   10   test1.txt
 10104  test2.txt
 10114  total
>>> print subprocess.check_output('python wc.py -c test1.txt test2.txt',shell=True).rstrip()
   19   test1.txt
 66735  test2.txt
 66754  total
>>> print subprocess.check_output('python wc.py -c test1.txt',shell=True).rstrip()
   19   test1.txt
>>> print subprocess.check_output('python wc.py test1.txt',shell=True).rstrip()
   10      10      19   test1.txt
>>> print subprocess.check_output('python wc.py -help',shell=True).rstrip()
-- parameter information:
    1. wc.py -l filename line count
    2. wc.py -w filename word count
    3. wc.py -c filename byte count
    4. wc.py    filename all count
    5. wc.py    stdin input
    6. wc.py -help  help information
>>> print subprocess.check_output('python wc.py',shell=True).rstrip()
safiu
fewau
fewagsvg   3       3       20


"""

# We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()

