#!/usr/local/bin/python3.5
# -*- coding:utf-8 -*-

import os,sys

def fileLine(filepath):
    thefile=open(filepath, 'rb')
    linecount=len(thefile.readlines())
    thefile.close()
    return linecount

def fileWord(filepath):
    thefile=open(filepath, 'rb')
    wordcount=len(thefile.read().split())
    thefile.close()
    return wordcount

def fileByte(filepath):
    thefile=open(filepath, 'rb')
    bytecount=len(thefile.read())
    thefile.close()
    return bytecount

def filehelp():
    print ('-- parameter information:')
    print ('    1. '+sys.argv[0]+ ' -l' +' filename ' +'line count')
    print ('    2. '+sys.argv[0]+ ' -w' +' filename ' +'word count')
    print ('    3. '+sys.argv[0]+ ' -c' +' filename ' +'byte count')
    print ('    4. '+sys.argv[0]+ '   ' +' filename ' +'all count')   
    print ('    5. '+sys.argv[0]+ '   ' +' stdin input')
    print ('    6. '+sys.argv[0]+ ' -help' +'  help information')

def getSpace(a,b,c):
    space=max(len(str(a)),len(str(b)),len(str(c)))
    return space

if __name__ == '__main__':
    if len(sys.argv)>=4 and (sys.argv[1]=='-l' or sys.argv[1]=='-w' or sys.argv[1]=='-c' or sys.argv[1]=='-help'):
        if os.path.exists(sys.argv[2]) and os.path.exists(sys.argv[3]):
            if sys.argv[1]=='-l' and os.path.isfile(sys.argv[3]):
                print(str(fileLine(sys.argv[2])).center(8)+sys.argv[2])
                print(str(fileLine(sys.argv[3])).center(8)+sys.argv[3])
                print(str(fileLine(sys.argv[3])+fileLine(sys.argv[2])).center(7)+'total'.center(8))
            elif sys.argv[1]=='-w' and os.path.isfile(sys.argv[3]):
                print(str(fileWord(sys.argv[2])).center(8)+sys.argv[2])
                print(str(fileWord(sys.argv[3])).center(8)+sys.argv[3])
                print(str(fileWord(sys.argv[3])+fileWord(sys.argv[2])).center(7)+'total'.center(8))
            elif sys.argv[1]=='-c' and os.path.isfile(sys.argv[3]):
                print(str(fileByte(sys.argv[2])).center(8)+sys.argv[2])
                print(str(fileByte(sys.argv[3])).center(8)+sys.argv[3])
                print(str(fileByte(sys.argv[3])+fileByte(sys.argv[2])).center(7)+'total'.center(8))
            elif sys.argv[1]=='-help' and os.path.isfile(sys.argv[2]):
                filehelp()
        elif os.path.exists(sys.argv[2])==False and os.path.exists(sys.argv[3])==False:
            print ('-- file  '+sys.argv[2]+' and '+sys.argv[3]+'  does not exist'  )
        elif os.path.exists(sys.argv[2])==False:
            if sys.argv[1]=='-l' and os.path.isfile(sys.argv[3]):
                print(str(fileLine(sys.argv[3])).center(8)+sys.argv[3])
            elif sys.argv[1]=='-w' and os.path.isfile(sys.argv[3]):
                print(str(fileWord(sys.argv[3])).center(8)+sys.argv[3])
            elif sys.argv[1]=='-c' and os.path.isfile(sys.argv[3]):
                print(str(fileByte(sys.argv[3])).center(8)+sys.argv[3])
            print ('-- file  '+sys.argv[2]+'  does not exist'  )
        elif os.path.exists(sys.argv[3])==False:
            if sys.argv[1]=='-l' and os.path.isfile(sys.argv[2]):
                print(str(fileLine(sys.argv[2])).center(8)+sys.argv[2])
            elif sys.argv[1]=='-w' and os.path.isfile(sys.argv[2]):
                print(str(fileWord(sys.argv[2])).center(8)+sys.argv[2])
            elif sys.argv[1]=='-c' and os.path.isfile(sys.argv[2]):
                print(str(fileByte(sys.argv[2])).center(8)+sys.argv[2])
            print ('-- file  '+sys.argv[3]+'  does not exist'  )
    elif len(sys.argv)>=3:
        if sys.argv[1]=='-l' or sys.argv[1]=='-w' or sys.argv[1]=='-c' or sys.argv[1]=='-help':
            if os.path.exists(sys.argv[2]):               
                if sys.argv[1]=='-l' and os.path.isfile(sys.argv[2]):
                    print(str(fileLine(sys.argv[2])).center(8)+sys.argv[2])
                elif sys.argv[1]=='-w' and os.path.isfile(sys.argv[2]):
                    print(str(fileWord(sys.argv[2])).center(8)+sys.argv[2])
                elif sys.argv[1]=='-c' and os.path.isfile(sys.argv[2]):
                    print(str(fileByte(sys.argv[2])).center(8)+sys.argv[2])
                elif sys.argv[1]=='-help' and os.path.isfile(sys.argv[2]):
                    filehelp()
            elif os.path.exists(sys.argv[2])==False:
                print ('-- file  '+sys.argv[2]+'  does not exist'  )
        elif os.path.isfile(sys.argv[1]):
            if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
                print(str(fileLine(sys.argv[1])).center(8)+str(fileWord(sys.argv[1])).center(8)+str(fileByte(sys.argv[1])).center(8)+sys.argv[1])
                print(str(fileLine(sys.argv[2])).center(8)+str(fileWord(sys.argv[2])).center(8)+str(fileByte(sys.argv[2])).center(8)+sys.argv[2])
                print(str(fileLine(sys.argv[1])+fileLine(sys.argv[2])).center(8)+str(fileWord(sys.argv[1])+fileWord(sys.argv[2])).center(8)+str(fileByte(sys.argv[1])+fileByte(sys.argv[2])).center(7)+'total'.center(8))
            elif os.path.exists(sys.argv[2])==False:
                print(str(fileLine(sys.argv[1])).center(8)+str(fileWord(sys.argv[1])).center(8)+str(fileByte(sys.argv[1])).center(8)+sys.argv[1])
                print ('-- file  '+sys.argv[2]+'  does not exist'  )
        elif os.path.exists(sys.argv[1])==False and os.path.exists(sys.argv[2])==False:
            print ('-- file  '+sys.argv[1]+' and '+sys.argv[2]+'  does not exist'  )
        elif os.path.exists(sys.argv[1])==False:
            print(str(fileLine(sys.argv[2])).center(8)+str(fileWord(sys.argv[2])).center(8)+str(fileByte(sys.argv[2])).center(8)+sys.argv[2])
            print ('-- file  '+sys.argv[1]+'  does not exist'  )
    elif len(sys.argv)>=2:
        if os.path.isfile(sys.argv[1]):
            if os.path.exists(sys.argv[1]):
                print(str(fileLine(sys.argv[1])).center(8)+str(fileWord(sys.argv[1])).center(8)+str(fileByte(sys.argv[1])).center(8)+sys.argv[1])
        elif sys.argv[1]=='-help':
            filehelp()
        elif os.path.exists(sys.argv[1])==False:
            print ('-- file  '+sys.argv[1]+'  does not exist'  )
    elif len(sys.argv)==1:
        lines=sys.stdin.readlines()
        words=0
        bytess=0
        for line in lines:
            t=line.split(' ')
            words+=len(t)
            for eachline in t:
                bytess+=len(eachline)
        print (str(len(lines)).center(8)+str(words).center(8)+str(bytess).center(8))
    else:
        filehelp()
        


