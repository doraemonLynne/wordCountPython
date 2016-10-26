import unittest

from wc import fileLine,fileWord,fileByte,getArgs,getOutput

class TestFileCount(unittest.TestCase):

    # def setUp(self):
    #     print('setUp...')

    # def tearDown(self):
    #     print('tearDown...')
        
    def test_fileLine(self):
        lines=fileLine('testinputs/test1.txt')
        self.assertEqual(lines, 10)

    def test_fileWord(self):
        words=fileWord('testinputs/test1.txt')
        self.assertEqual(words, 10)

    def test_fileByte(self):
        bytes=fileByte('testinputs/test1.txt')
        self.assertEqual(bytes, 19)

class TestGetArgs(unittest.TestCase):

    def test_getArgs(self):
        args='wc.py -l testinputs/test1.txt'
        self.assertEqual(args, 'wc.py -l testinputs/test1.txt')

if __name__ == '__main__':
    unittest.main()