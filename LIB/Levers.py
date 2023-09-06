##///
##||| LEVERS.PY TITANIUM
##||| Change list:
##||| * Added message for when the player is too far from a lever to use it
##||| * 
##||| * 
##||| * 
##\\\ 

import Bladex
import InitDataField
import Actions
import GameStateAux
import ObjStore
import B3DLib

LEVER_DISTANCE = 2000

LEVER_OFF      = 0
LEVER_ON       = 1
LEVER_OFF2ON   = 2
LEVER_ON2OFF   = 3

class LeverType:
	bod_name=""
	stick_bod_name=""
	stick_offset=(0,0,0)
	center=(0,0,0)
	axis=(0,0,0)
	iang=0.0
	on_time=0.0
	off_time=0.0



def ActivateLever(pj_name,event):
	pj=Bladex.GetEntity(pj_name)
	lever=pj.Data.obj_used.Data.leverdata
	if(lever.state==LEVER_ON):
		lever.TurnOff()
	elif(lever.state==LEVER_OFF):
		lever.TurnOn()
	pj.Data.obj_used=None
	pj.DelAnmEventFunc("Activate")


def LeverUseFunc(lever_name,use_from):
	obj=Bladex.GetEntity(lever_name)
	
	# To avoid the telekinetic power of the jedi knight
	if B3DLib.GetXZDistance('Player1', lever_name)< LEVER_DISTANCE:
		lever=obj.Data.leverdata
		if((lever.state==LEVER_ON and lever.mode!=2) or lever.state==LEVER_OFF):
			pj=Bladex.GetEntity("Player1")
			if(lever.state==LEVER_ON):
				pj.LaunchAnmType("lvr_u")
			else:
				pj.LaunchAnmType("lvr_d")
			pj.Data.obj_used=obj
			Actions.QuickTurnToFaceEntity ("Player1", lever_name)
			pj.AddAnmEventFunc("Activate",ActivateLever)
 	else:
		Actions.ReportMsg ("Not in reach")          # Added -LeadHead

def MoveLeverFunc(lever_name,time):
	stick_obj=Bladex.GetEntity(lever_name)
	lever=stick_obj.Data.leverdata
	theta = min(max(((time-lever.start_time)/(lever.end_time-lever.start_time)),0),1)
	theta_diff = theta - lever.old_theta
	lever.old_theta = theta
	if(theta<1):
		c=lever.type.center
		e=lever.type.axis
		stick_obj.RotateRel(c[0],c[1],c[2],e[0],e[1],e[2],lever.w*theta_diff)
		lever.last_time=time;
	else:
		c=lever.type.center
		e=lever.type.axis
		stick_obj.RotateRel(c[0],c[1],c[2],e[0],e[1],e[2],lever.w*theta_diff)
		stick_obj.RemoveFromList("Timer60")
		stick_obj.TimerFunc=None
		if(lever.state==LEVER_ON2OFF):
			lever.state=LEVER_OFF
		elif(lever.state==LEVER_OFF2ON):
			lever.state=LEVER_ON
			if(lever.mode==1):
				lever.TurnOff()
	

##class Lever(GameStateAux.PersistentObject):
class Lever:

	ObjId=""
	state=LEVER_OFF
	mode=1
	OnTurnOnFunc=None
	OnTurnOnArgs=()
	OnTurnOffFunc=None
	OnTurnOffArgs=()
	stick_obj=None
	type=None
	obj=None
	old_theta = 0



	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def TurnOn(self):
		if(self.state==LEVER_OFF):
			self.stick_obj.TimerFunc=MoveLeverFunc
			self.stick_obj.SubscribeToList("Timer60")
			self.start_time=Bladex.GetTime()
			self.last_time=Bladex.GetTime()
			self.end_time=self.start_time+self.type.on_time
			self.w=self.type.iang
			self.old_theta = 0
			self.state=LEVER_OFF2ON
			if(self.OnTurnOnFunc):
				apply(self.OnTurnOnFunc,self.OnTurnOnArgs)

	def TurnOff(self):
		if(self.state==LEVER_ON):
			self.stick_obj.TimerFunc=MoveLeverFunc
			self.stick_obj.SubscribeToList("Timer60")
			self.start_time=Bladex.GetTime()
			self.last_time=Bladex.GetTime()
			self.end_time=self.start_time+self.type.off_time
			self.w=-self.type.iang
			self.old_theta = 0
			self.state=LEVER_ON2OFF
			if(self.OnTurnOffFunc):
				apply(self.OnTurnOffFunc,self.OnTurnOffArgs)


	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver cómo poder guardar el estado de la clase

		stick_objId=None
		if self.stick_obj:
			stick_objId=self.stick_obj.Name
		return (1,
				self.ObjId,
				self.state,
				self.mode,
				GameStateAux.SaveFunctionAux(self.OnTurnOnFunc),
				self.OnTurnOnArgs,
				GameStateAux.SaveFunctionAux(self.OnTurnOffFunc),
				self.OnTurnOffArgs,
				stick_objId,
				self.type,
				GameStateAux.SaveEntityAux(self.obj),
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase

		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self

			self.state=parm[2]
			self.mode=parm[3]
			GameStateAux.LoadFunctionAux(parm[4],self,"OnTurnOnFunc")
			self.OnTurnOnArgs=parm[5]
			GameStateAux.LoadFunctionAux(parm[6],self,"OnTurnOffFunc")
			self.OnTurnOffArgs=parm[7]
			stick_objId=parm[8]
			self.type=parm[9]
			self.obj=GameStateAux.LoadEntityAux(parm[10])
			GameStateAux.LoadNewMembers(self,parm[11])
			if stick_objId:
				self.stick_obj=Bladex.GetEntity(stick_objId)
			else:
				self.stick_obj=None
		else:
			print "Lever.__setstate__() -> Version mismatch"
			# Valores de creación por si valen para algo.
			self.state=LEVER_OFF
			self.mode=1
			self.OnEndOpenFunc=None
			self.OnTurnOnArgs=()
			self.OnEndCloseFunc=None
			self.OnTurnOffArgs=()
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self


LeverType1=LeverType()

LeverType1.bod_name="Zocalo1"
LeverType1.stick_bod_name="Palanca1"
LeverType1.stick_offset=(0.0,-99.0,131.0)
LeverType1.center=0.0,225.0,-125.0
LeverType1.axis=1.0,0.0,0.0
LeverType1.iang=3.1416/2
LeverType1.on_time=0.5
LeverType1.off_time=0.5


LeverType2=LeverType()

LeverType2.bod_name="Zocalo2"
LeverType2.stick_bod_name="Palanca2"
LeverType2.stick_offset=(83.0,-238.0,235.0)
LeverType2.center=0.0,237.0,-237.0
LeverType2.axis=1.0,0.0,0.0
LeverType2.iang=-3.1416/2
LeverType2.on_time=0.5
LeverType2.off_time=0.5


LeverType3=LeverType()

LeverType3.bod_name="Zocalo3"
LeverType3.stick_bod_name="Palanca3"
LeverType3.stick_offset=(0.0,-160.0,218.0)
LeverType3.center=0.0,218.0,-218.0
LeverType3.axis=1.0,0.0,0.0
LeverType3.iang=3.1416/2
LeverType3.on_time=0.5
LeverType3.off_time=0.5


LeverTypeFloor=LeverType()

LeverTypeFloor.bod_name="ZocaloSuelo"
LeverTypeFloor.stick_bod_name="PalancaSuelo"
LeverTypeFloor.stick_offset=(0.0,-297.0,467.0)
LeverTypeFloor.center=0.0,297.0,-520.0
LeverTypeFloor.axis=1.0,0.0,0.0
LeverTypeFloor.iang=-3*(3.1416/4)
LeverTypeFloor.on_time=0.5
LeverTypeFloor.off_time=0.5


LeverTypeSnake=LeverType()

LeverTypeSnake.bod_name="ZocaloSerpiente"
LeverTypeSnake.stick_bod_name="MandibulaSerpiente"
LeverTypeSnake.stick_offset=(0.0,-78.699,-118.771)
LeverTypeSnake.center=0.0,91.753,65.783
LeverTypeSnake.axis=1.0,0.0,0.0
LeverTypeSnake.iang=-3.1416/5
LeverTypeSnake.on_time=0.5
LeverTypeSnake.off_time=0.5




def PlaceLever(name,type,position,orientation,scale):
	lever=Lever()
	lever.type=type

	lever.obj=Bladex.CreateEntity(name,type.bod_name,position[0],position[1],position[2])
	lever.obj.Orientation=orientation
	abs_offset=lever.obj.Rel2AbsVector(lever.type.stick_offset[0],lever.type.stick_offset[1],lever.type.stick_offset[2])
	InitDataField.Initialise(lever.obj)
	lever.obj.Data.leverdata=lever
	
	lever.stick_obj=Bladex.CreateEntity(name+"Stick",type.stick_bod_name,position[0]+abs_offset[0],position[1]+abs_offset[1],position[2]+abs_offset[2])
	lever.stick_obj.Orientation=orientation
	InitDataField.Initialise(lever.stick_obj)
	lever.stick_obj.Data.leverdata=lever
	lever.stick_obj.UseFunc=LeverUseFunc
	lever.stick_obj.Solid=0
	return lever
