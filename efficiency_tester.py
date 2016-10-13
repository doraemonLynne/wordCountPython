# -*-coding:utf-8 -*-

import os,sys
from subprocess import Popen, PIPE, STDOUT

def TotalSec(minute,second):
    realSecond=int(minute)*60+float(second.replace('s',''))
    return realSecond

def Sec2Min(second):
    minute=int(second/60)
    return minute

def LeftSec(second):
    leftsec=second%60
    return ('%.3f'%leftsec)

def effTest():
    for root,dirs,files in os.walk(sys.argv[1]):
        for root,dirs,files in os.walk(sys.argv[1]):
            print('Testcase\t'+'RealTime\t'+'CPUTime')
            for file in files:
                p=os.path.join(root,file)
                args = "time python wc.py "+p
                program=Popen(args,stdin=PIPE,stdout=PIPE,stderr=STDOUT,shell=True)
                out=program.stdout.readlines()
                for i in range(1,len(out)):
                    out[i]=out[i].strip().replace('real','').replace('user','').replace('sys','').split('m')
                realTime=out[2]
                userTime=out[3]
                sysTime=out[4]
                realTimeM=realTime[0]
                userTimeM=userTime[0]
                sysTimeM=sysTime[0]
                realTimeS=realTime[1]
                userTimeS=userTime[1]
                sysTimeS=sysTime[1]
                realS=TotalSec(realTimeM,realTimeS)
                userS=TotalSec(userTimeM,userTimeS)
                sysS=TotalSec(sysTimeM,sysTimeS)
                CPUTime=userS+sysS
                RealM=Sec2Min(realS)
                RealS=LeftSec(realS)
                CPUM=Sec2Min(CPUTime)
                CPUS=LeftSec(CPUTime)
                print(file+'\t'),
                print(str(RealM)+'m'+str(RealS)+'s'+'\t'),
                print(str(CPUM)+'m'+str(CPUS)+'s')
                
if __name__ == '__main__':
    if len(sys.argv)==2:
    	if os.path.exists(sys.argv[1]):
    	    effTest()
    	else:
            print('-- directory  '+sys.argv[1]+'  does not exist')
    else:
        sys.argv.append('testinputs')
        effTest()

