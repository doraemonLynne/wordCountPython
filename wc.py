import argparse
import sys

def fileLine(fileName):
    try:
        with open(fileName, 'r') as f:
            linecount=len(f.readlines())
    except IOError as err:
        print ('wc:%s'%str(err))
        exit()
    return linecount

def fileWord(fileName):
    try:
        with open(fileName, 'r') as f:
            wordcount=len(f.read().split())
    except IOError as err:
        print ('wc:%s'%str(err))
        exit()
    return wordcount

def fileByte(fileName):
    try:
        with open(fileName, 'r') as f:
            bytecount=len(f.read())
    except IOError as err:
        print ('wc:%s'%str(err))
        exit()
    return bytecount

def StdinForTest():
    sys.stdin = open('./testinputs/test4.txt', 'r')
    sys.stdin.flush()
    lines=sys.stdin.readlines()
    linecount=len(lines)
    wordcount=0
    bytecount=0
    for line in lines:
        words=line.split(" ")
        wordcount+=len(words)
        bytecount+=len(line)
    return linecount,wordcount,bytecount

def stdinLine(lines):
    linecount=len(lines)
    return linecount

def stdinWord(lines):
    wordcount=0
    for line in lines:
        words=line.split(" ")
        wordcount+=len(words)
    return wordcount

def stdinByte(lines):
    bytecount=0
    for line in lines:
        bytecount+=len(line)
    return bytecount

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--lines", help="count line", action="store_true")
    parser.add_argument("-w","--words", help="count word", action="store_true")
    parser.add_argument("-c","--bytes", help="count byte", action="store_true")
    parser.add_argument("files", help="filenames", nargs="*")
    args = parser.parse_args()
    return args

def getOutput(args,line,word,byte,filename):
    line=str(line).rjust(8)
    word=str(word).rjust(8)
    byte=str(byte).rjust(8)
    filename=str(filename)
    if (args.lines or args.words or args.bytes)!= False:
        if args.lines==False:
            line=''
        if args.words==False:
            word=''
        if args.bytes==False:
            byte=''
    print(line+word+byte+' '+filename)
    
if __name__ == "__main__":

    args=getArgs()

    totalLine=0
    totalWord=0
    totalByte=0

    if args.files:
        for n in args.files:
            totalLine+=fileLine(n)
            totalWord+=fileWord(n)
            totalByte+=fileByte(n)
            getOutput(args,fileLine(n),fileWord(n),fileByte(n),n)
        if len(args.files)>1:
            getOutput(args,totalLine,totalWord,totalByte,'total')

    elif len(args.files)==0:
        lines=sys.stdin.readlines()
        line=stdinLine(lines)
        word=stdinWord(lines)
        byte=stdinByte(lines)
        getOutput(args,stdinLine(lines),stdinWord(lines),stdinByte(lines),'')












    
