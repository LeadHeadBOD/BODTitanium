##///
##||| VOLCANO_M14/arrowPuz.PY TITANIUM
##||| Change list:
##||| * Added sounds for sectors breaking
##\\\ 



#########################################################
#														#
# VOLCANO												#
#														#
# puzzle de la flecha									#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import Doors


apSectorA=Bladex.GetSector(-56000,10000,-34750)
apSectorA.Active=0
apSectorA.InitBreak((20,300,70),(1240,530,200),(233,143,874),'piedra pesada')

apSectorB=Bladex.GetSector(-64250,11000,-34750)
apSectorB.InitBreak((20,300,70),(1240,530,200),(233,143,874),'piedra pesada')
apSectorB.Active=0

apDoor=Doors.CreateDoor("apElevador", (-51560,12000,-26500), (0, 1, 0), 0, 3250, Doors.CLOSED)
apDoor.Squezze = 1

import LavaDefDamage

vLavaarrpz=LavaDefDamage.LAVA_AREA()
vLavaarrpz.CreateLava ("vLavaarrpz" ,-54620.7299491,14800.2,-23181.3387455 ,"cala2",0.029)

"""
apLavaStart=14800.2
apLavaStop=7138.38922796
apLavaFloodTime=120.0
apLavaPosition=-54620.7299491, -23181.3387455
apLava=Bladex.CreateEntity("apLava","Entity Water", apLavaPosition[0], apLavaStart, apLavaPosition[1] )
apLava.Reflection=0.1
apLava.Color=200,33,33

apLavaFloodStartTime=0
def apFloodTimer(ent,time):
	time = Bladex.GetTime()
	elapsedtime = time-apLavaFloodStartTime
	apLavaFloodLevel=apLavaStart+((apLavaStop-apLavaStart)/apLavaFloodTime)*elapsedtime
	apLava.Position=apLavaPosition[0],apLavaFloodLevel,apLavaPosition[1]
	print(apLavaFloodLevel)
	if (elapsedtime>apLavaFloodTime) :
		print("> Stop flood!!")
		apLava.TimerFunc=""
		apLava.RemoveFromList("apFlood")
		apTurnOnTheLights()

Bladex.CreateTimer("apFlood",0.020)
def apStartFlood():
	print("apStartFlood()")
	global apLavaFloodStartTime
	apLava.TimerFunc=apFloodTimer
	apLava.SubscribeToList("apFlood")	
	apLavaFloodStartTime=Bladex.GetTime()
"""

### Added platform breaking sounds
# 			-LeadHead

SoundBreakA=Sounds.CreateEntitySound('../../Sounds/derribo-puerta1.wav', 'SoundBreakA')
SoundBreakA.Volume=0.85
SoundBreakA.MinDistance=2500.0
SoundBreakA.MaxDistance=30000.0

apSectorABroken=0
apSectorBBroken=0
apTriggerSectorA = Bladex.GetSector(-56000,5000,-34750)
apTriggerSectorA.OnEnter=apBreakSectorA

SoundBreakB=Sounds.CreateEntitySound('../../Sounds/M-DERRIBO-MURO.wav', 'SoundBreakB')
SoundBreakB.Volume=0.85
SoundBreakB.MinDistance=2500.0
SoundBreakB.MaxDistance=30000.0

apTriggerSectorB = Bladex.GetSector(-64250,5000,-34750)
apTriggerSectorB.OnEnter=apBreakSectorB

#char.Position = -46234.1040525, 7715.4, -30163.1651636

############Pulsador provisional

o=Bladex.CreateEntity("bloque111","Bloque",-51545.228390,2883.251512,-26580.068291)
o.Static=0
o.Scale=3.333391
o.Orientation=0.707107,0.707107,0.000000,0.000000

button=Button.CreateButtonCombination(0,apActivate,"")
button.AddButton("bloque111",3,(1,0,0),400,0,0,1)

