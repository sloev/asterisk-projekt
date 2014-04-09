#!/usr/bin/env python
import pystrix
from crontab import CronTab


if __name__ == '__main__':
    agi = pystrix.agi.AGI()

    agi.execute(pystrix.agi.core.Answer()) #Answer the call
#    agi.execute(pystrix.agi.core.Wait(100)) #Answer the call
    myDate={}
    myDateIndices={0:"month",1:"day",2:"hour",3:"minute"}
    boundaries={0:[1,12],1:[1,31],2:[0,23],3:[0,59]}
    success=True
    for i in range(0,3):
	    response = agi.execute(pystrix.agi.core.StreamFile('./custom/'+myDateIndices[i])) #Play a file; allow DTMF '1' or '2' to interrupt
	    myDate[myDateIndices[i]] = 10 * agi.execute(pystrix.agi.core.WaitForDigit(timeout=5000)
	    myDate[myDateIndices[i]] = myDate[myDateIndices[i]] + agi.execute(pystrix.agi.core.WaitForDigit(timeout=5000)
	    bound=boundaries[i]
	    if not bound[0]<=myDate[myDateIndices[i]] <=bound[1]:
		    response = agi.execute(pystrix.agi.core.StreamFile('./custom/numberError')) 
		    success=False
		    break		 
		
	print myDate
	if success:
		mydateString=str(myDate["month"])+str(myDate["day"])+str(myDate["hour"])+str(myDate["minute"])
	    response = agi.execute(pystrix.agi.core.StreamFile('./custom/recordMessage') #indtal besked og tryk 0
	    response = agi.execute(pystrix.agi.core.RecordFile('./messages/'+mydateString+".wav", format='wav', escape_digits='0', timeout=15000)
	    response = agi.execute(pystrix.agi.core.StreamFile('./custom/thankYou')) 
	    
	    #cron stuff
		#job  = cron.new(command='/usr/bin/echo')
		#job.month.on(myDate["month"])
		#job.day.on(myDate["day"])
		#job.hour.on(myDate["hour"])
		#job.minute.on(myDate["minute"])
		
	
	    
	agi.execute(pystrix.agi.core.Hangup())
