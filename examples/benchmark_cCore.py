#!/usr/bin/env python

from vafmbase import ChannelType
from vafmcircuits import Machine

import vafmcircuits
import vafmcircuits_pycirc

from datetime import datetime



def main():
	startTime = datetime.now()
	
	machine = Machine(name='machine', dt=0.01, pushed=True);
	
	wave = machine.AddCircuit(type='waver',name='wave', amp=1, freq=1, pushed=True )
	#adder= machine.AddCircuit(type='myCirc',name='add_0', pushed=True)
	adder= machine.AddCircuit(type='myCirc',name='add_0', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_1', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_2', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_3', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_4', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_5', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_6', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_7', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_8', pushed=True)
#	adder= machine.AddCircuit(type='myCirc',name='add_9', pushed=True)
	
	machine.Connect('wave.cos','add_0.in1')
	machine.Connect('wave.sin','add_0.in2')
	for i in xrange(1,10):
		addname = "add_"+str(i)
		prvname = "add_"+str(i-1)
		adder= machine.AddCircuit(type='opMul',name=addname, pushed=True)
		machine.Connect(prvname+".out",addname+'.in1')
		machine.Connect('wave.sin',addname+'.in2')
	
	
	#machine.Wait(100000.0)	#10^7 steps	- 1.414s -	TPS = 7072135.785 -	PURE cCORE
	#machine.Wait(10000.0)	#10^6 steps	- 3.222s -	TPS = 310366.232 -	cCORE + 1 PYCircuit
	#machine.WaitPY(1000.0)	#10^5 steps	- 8.265s -	TPS = 12099.2130 -	PURE PY

	print(datetime.now()-startTime)
if __name__ == '__main__':
	main()
