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

def stdin():
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

def fileHelp():
    print ('-- parameter information:')
    print ('    1. '+sys.argv[0]+ ' -l' +' filename ' +'line count')
    print ('    2. '+sys.argv[0]+ ' -w' +' filename ' +'word count')
    print ('    3. '+sys.argv[0]+ ' -c' +' filename ' +'byte count')   
    print ('    4. '+sys.argv[0]+ '   ' +' stdin input')
    print ('    5. '+sys.argv[0]+ ' -help' +'  help information')

def getArgs():
    flags=[]
    files=[]   
    for arg in sys.argv:
        if arg[:1]=='-':
            if arg=='-l' or arg=='-w' or arg=='-c':
                if not arg in flags:
                    flags.append(arg)
            elif arg=='-help':
                fileHelp()
            else:
                print("wc: illegal option -- '%s'"%arg[1:])
        else:
            if arg!='wc.py':
                files.append(arg)

    return {'flags':flags,'files':files}

def getOutput(flags,line,word,byte,name=''):
    output=''
    if len(flags)!=0:
        if not "-l" in flags:
            line=''
        if not "-w" in flags:
            word=''
        if not "-c" in flags:
            byte=''
    output=str(line).rjust(8)+str(word).rjust(8)+str(byte).rjust(8)+'  '+name
    print (output)

if __name__ == "__main__":
    args=getArgs()
    totalLine=0
    totalWord=0
    totalByte=0
    line=0
    word=0
    byte=0
    if len(args['files'])==0:
        if len(args['flags'])==0:
            lines=sys.stdin.readlines()
            getOutput(args['flags'],stdinLine(lines),stdinWord(lines),stdinByte(lines))
        else:
            lines=sys.stdin.readlines()
            for arg in args['flags']:
                if arg=='-l':
                    line=stdinLine(lines)
                elif arg=='-w':
                    word=stdinWord(lines)
                elif arg=='-c':
                    byte=stdinByte(lines)
            getOutput(args['flags'],line,word,byte)
    else:
        for file in args['files']:
            if len(args['flags'])==0:
                line=fileLine(file)
                word=fileWord(file)
                byte=fileByte(file)
                totalLine+=line
                totalWord+=word
                totalByte+=byte
            else:
                for arg in args['flags']:
                    if arg=='-l':
                        line=fileLine(file)
                        totalLine+=line
                    if arg=='-w':
                        word=fileWord(file)
                        totalWord+=word
                    if arg=='-c':
                        byte=fileByte(file)
                        totalByte+=byte
            getOutput(args['flags'],line,word,byte,file)
        if len(args['files'])>1:
            getOutput (args['flags'],totalLine,totalWord,totalByte,"total")
                        

                














    
