#!/usr/bin/env python


import pystrix
from crontab import CronTab


if __name__ == '__main__':
    #print "lolcat"
    agi = pystrix.agi.AGI()
    agi.execute(pystrix.agi.core.Answer()) #Answer the call
    myDate={}
    myDateIndices={0:'month',1:'day',2:'hour',3:'minute'}
    boundaries={0:[1,12],1:[1,31],2:[0,23],3:[0,59]}
    success=True
    #print "vars created"
    for i in range(0,4):
        #print ()"for loop iter:"+str(i))
        response = agi.execute(pystrix.agi.core.StreamFile('./custom/'+myDateIndices[i]))
        myDate[myDateIndices[i]] = 10 * int(agi.execute(pystrix.agi.core.WaitForDigit(timeout=5000)))
        #agi.execute(pystrix.agi.core.SayNumber(myDate[myDateIndices[i]]))

        myDate[myDateIndices[i]] = int(myDate[myDateIndices[i]] + int(agi.execute(pystrix.agi.core.WaitForDigit(timeout=5000))))
        bound=boundaries[i]
        agi.execute(pystrix.agi.core.SayNumber(myDate[myDateIndices[i]]))
        if not (bound[0]<=myDate[myDateIndices[i]] <=bound[1]):
            response = agi.execute(pystrix.agi.core.StreamFile('./custom/numberError'))
            success=False
            break
        pass
    #print "leaved for loop"
    #print myDate
    if success:
        mydateString=str(myDate["month"])+str(myDate["day"])+str(myDate["hour"])+str(myDate["minute"])
        response = agi.execute(pystrix.agi.core.StreamFile('./custom/recordMessage'))
        response = agi.execute(pystrix.agi.core.RecordFile('/usr/share/asterisk/sounds/messages/'+mydateString, format='wav', escape_digits='0', timeout=15000))
        response = agi.execute(pystrix.agi.core.StreamFile('./custom/thankYou'))
        
        #cron stuff
        #job  = cron.new(command='/usr/bin/echo')
        #job.month.on(myDate["month"])
        #job.day.on(myDate["day"])
        #job.hour.on(myDate["hour"])
        #job.minute.on(myDate["minute"])
    #print "hanging up"
    agi.execute(pystrix.agi.core.Hangup())
