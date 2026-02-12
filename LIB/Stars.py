##///
##||| STARS.PY TITANIUM
##||| Change list:
##||| * Added reportName - on Stars.Twinkle(ObjName, 1) the picked up item will not report the picked up item in message or inventory
##||| * Fixed glitchy text fade if GameText was already printed
##\\\ 

###############################################
####                 MAGIC                 ####
###############################################
import Bladex
import netgame

import InitDataField


def DeTwinkle(ObjName):
	if netgame.GetNetState() == 0:
		import GameText
		import Select
		
		obj=Bladex.GetEntity(ObjName)
		reportName = 1
		try:
			if obj.Data.Twinkle_no_report: reportName = 0
		except:
			pass
		wps=Bladex.GetEntity(ObjName+" TwinkleStar")
		if wps:
			import ScorerWidgets
			wps.DeathTime=Bladex.GetTime()
			if reportName:
				GameText.AbortText()
				GameText.WriteTextAux(Select.GetSelectionData(ObjName)[2],5,255,255,255,[],None,1)
				ScorerWidgets.ObjSlTimer = Bladex.GetTime()
			obj.SelfIlum = 0


def Twinkle(ObjName, DoNotReport = 0):
	obj = Bladex.GetEntity(ObjName)
	if netgame.GetNetState() == 0:
		wps=Bladex.CreateEntity(ObjName+" TwinkleStar", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		wps.ObjectName=ObjName
		wps.ParticleType="LucesCools"
		wps.Time2Live=16
		wps.RandomVelocity=0
		wps.Velocity=0,0,0
		wps.NormalVelocity=2
		wps.YGravity=0
		wps.PPS=5
		obj.SelfIlum = -1
	if DoNotReport == 1:
		InitDataField.Initialise(obj)
		obj.Data.Twinkle_no_report = 1
	return wps
		
	
# Stars.Twinkle(char.InvLeft)
# Stars.Twinkle(char.InvRight)

AutoTake = 1