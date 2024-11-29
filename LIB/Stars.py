##///
##||| STARS.PY TITANIUM
##||| Change list:
##||| * Added reportName argument - will not show GameText if FALSE
##||| * Fixed glitchy text fade if GameText was already printed
##\\\ 

###############################################
####                 MAGIC                 ####
###############################################
import Bladex
import netgame



def DeTwinkle(ObjName, reportName = 1):
	if netgame.GetNetState() == 0:
		import GameText
		import Select

		wps=Bladex.GetEntity(ObjName+" TwinkleStar")
		if wps:
			import ScorerWidgets
			wps.DeathTime=Bladex.GetTime()
			if reportName:
				GameText.AbortText()
				GameText.WriteTextAux(Select.GetSelectionData(ObjName)[2],5,255,255,255,[],None,1)
				ScorerWidgets.ObjSlTimer = Bladex.GetTime()
			Bladex.GetEntity(ObjName).SelfIlum = 0


def Twinkle(ObjName):
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
		Bladex.GetEntity(ObjName).SelfIlum = -1
		return wps
	
# Stars.Twinkle(char.InvLeft)
# Stars.Twinkle(char.InvRight)

AutoTake = 1