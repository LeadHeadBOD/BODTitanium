##///
##||| DARFUNCS.PY TITANIUM
##||| Change list:
##||| * False Cube no longer has selection data that causes character to look at and select it
##||| * Deathfile will now assign default enemytype funcs
##||| * Fire sectors now check for fire resistance
##||| * Fire sectors now cause dark smoke when taking fire damage
##||| * 
##\\\ 



###########################################################################
###
###        The dark functions of hell come true in this file
###      Beaware little coder, the force keep a power inside the
###    hell and your nightmares will bless your unholly heart with 
###                       damns and doom over the
###
###                |\   /\  |\   - | |  |\|  /  /
###                | | |__| |_| |_ | |  | | |   \
###                |/  |  | |\  |  |_|  | |  \  /
###                 the cutting edge is bladeness
###
###########################################################################

import Bladex
import AuxFuncs
import EnemyTypes
import Sparks
import Actions
import math
import Breakings
import types
import Reference
import Blood
import SolidMask
import ObjStore
import GameStateAux
import os
import Blood
import ItemTypes
import CharStats

#------------------------------------------------------------------------#
ActualLevel = Bladex.GetCurrentMap()
############ Misc camera fucs ############ 

def Cafin(entity_name, camera_element, node):  
  cam = Bladex.GetEntity("Camera")  

  if node==1:
     cam.SType = 0
     cam.ETarget = "Player1"
     cam.TType = 2
     cam.CameraClearPath(0)
     cam.CameraClearPath(1)
     
  

def BackPlayer():
    Cam = Bladex.GetEntity("Camera")
    Cam.SetPersonView("Player1")

def ChangePointOfView(ox2, oy2, oz2, time,person="Player1"):

	cam=Bladex.GetEntity("Camera")

	ox1 = cam.Position[0]
	oy1 = cam.Position[1]
	oz1 = cam.Position[2]

	#Path objetivo
	cam.AddCameraNode(0, time, ox1, oy1, oz1)
	cam.AddCameraNode(0, time/2.0, ox2, oy2, oz2)
	cam.AddCameraNode(0, time/2.0, (ox1+ox2)/2.0, (oy1+oy2)/2.0, (oz1+oz2)/2.0)
	
	cam.ETarget = person
	cam.TType = 2

	cam.SType=1
	cam.CameraStartPath(0)	
	cam.ChangeNodeFunc=Cafin


def ChangeCam(ox2, oy2, oz2,tx2,ty2,tz2, time,CafinProx):

	cam=Bladex.GetEntity("Camera")

	ox1 = cam.Position[0]
	oy1 = cam.Position[1]
	oz1 = cam.Position[2]
	
	
	tx1 = cam.TPos[0]
	ty1 = cam.TPos[1]
	tz1 = cam.TPos[2]
	
	
	#Path objetivo
	cam.AddCameraNode(0, time, ox1, oy1, oz1)
	cam.AddCameraNode(0, time/2.0, ox2, oy2, oz2)
	cam.AddCameraNode(0, time/2.0, (ox1+ox2)/2.0, (oy1+oy2)/2.0, (oz1+oz2)/2.0)

	cam.AddCameraNode(1, time, tx1, ty1, tz1)
	cam.AddCameraNode(1, time/2.0, tx2, ty2, tz2)
	cam.AddCameraNode(1, time/2.0, (tx1+tx2)/2.0, (ty1+ty2)/2.0, (tz1+tz2)/2.0)
	
	cam.ETarget = "Player1"
	cam.SType=1
	
	cam.TType=1
	cam.CameraStartPath(0)	
	cam.ChangeNodeFunc=CafinProx


def InitGiroCamera(ESource = "Player1",yPos=None):
        cam=Bladex.GetEntity("Camera")
        if yPos==None:
            VecRot = 2*cam.TPos[0]-cam.Position[0], 2*cam.TPos[1]-cam.Position[1], 2*cam.TPos[2]-cam.Position[2]
        else:
            VecRot = 2*cam.TPos[0]-cam.Position[0], 2*cam.TPos[1]-cam.Position[1], 2*cam.TPos[2]-cam.Position[2]
        cam.ESource = ESource
        cam.SType   = 2
        cam.TType   = 0
        cam.TPos    = VecRot
        
        
def GiraCamara(AngleVariation,yMode=None):
        cam          = Bladex.GetEntity("Camera")
        VecRot       = cam.TPos[0]-cam.Position[0], cam.TPos[1]-cam.Position[1], cam.TPos[2]-cam.Position[2]
        vtpos        = VecRot[0]*math.cos(AngleVariation)-VecRot[2]*math.sin(AngleVariation), VecRot[0], VecRot[0]*math.sin(AngleVariation)+VecRot[2]*math.cos(AngleVariation)
        if yMode == None:
            cam.TPos     = vtpos[0]+cam.Position[0], cam.TPos[1],           vtpos[2]+cam.Position[2]
        else:
            cam.TPos     = vtpos[0]+cam.Position[0], cam.Position[1]+yMode, vtpos[2]+cam.Position[2]

############ Deaths and limbs ############

DeathState = 0     # CARLOS : NO GRABAR ESTO, no es necesario
DeathFile  = None  # CARLOS : NO GRABAR ESTO, no es necesario

def DetieneArmaMuerto(obj_name):
	global DeathFile
	if DeathFile:
		o = Bladex.GetEntity(obj_name)
		o.OnStopFunc=None
		DeathFile.write("o = Bladex.CreateEntity('" +obj_name+"','"+o.Kind+"',"+str(o.Position[0])+","+str(o.Position[1])+","+str(o.Position[2])+",'Weapon')\n")
		DeathFile.write("o.Orientation = "+str(o.Orientation[0])+","+str(o.Orientation[1])+","+str(o.Orientation[2])+","+str(o.Orientation[3])+"\n")
		DeathFile.write("ItemTypes.ItemDefaultFuncs(o)\n\n")
	
	
def DetieneMutilacion(obj_name):
	global DeathFile
	if DeathFile:
		o = Bladex.GetEntity(obj_name)
		o.OnStopFunc=None
		DeathFile.write("\no = "+o.Data[0]+".SeverLimb("+str(o.Data[1])+")\n")
		DeathFile.write("o.Stop()\n")
		DeathFile.write("o.Position    = "+str(o.Position   [0])+","+str(o.Position   [1])+","+str(o.Position   [2])+"\n")
		DeathFile.write("o.Orientation = "+str(o.Orientation[0])+","+str(o.Orientation[1])+","+str(o.Orientation[2])+","+str(o.Orientation[3])+"\n")
	

def GrabarLaSangre(x,y,z):
	global DeathFile
	if DeathFile:
		DeathFile.write("Bladex.CreateEntity('BloodPool','Entity Pool',"+str(x)+","+str(y)+","+str(z)+")\n")

def CloseDeathFile():
	global DeathFile
	if DeathFile:
		print "closing 'death.py'..."
		DeathFile.close()
		DeathFile = None
		os.rename("pak/deaths.py_","pak/deaths.py")
		Blood.AfterCreateBlood = None
	

def MuertoyTroceado2(name,trozos):
	muertoint2=Bladex.GetEntity(name)
	muertoint2.CastShadows = 0
	muertoint2.SetOnFloor()
	muertoint2.Life = 0
	for i in trozos:
		mut = muertoint2.SeverLimb(i)
		if mut:
			mut.Data = (muertoint2.Name,i)
			mut.OnStopFunc=DetieneMutilacion

muertonum = 0
	

def MuertoyTroceado(x,y,z,raze,weapon,trozos,angul=2.19288423389,MeshName=None):
	global ActualLevel
	global muertonum
	global DeathState
	global DeathFile
	
	if DeathState:
		return

	if not DeathFile:
		try:
			os.mkdir("./Pak")
		except:
			pass
		if "deaths.py" in os.listdir("./Pak/"):
			execfile("Pak/deaths.py")
			DeathState = 1
			return
		print "Creating 'deaths.py'..."
		DeathFile = open("Pak/deaths.py_","w")
		DeathFile.write("import Bladex\nimport ItemTypes \nimport EnemyTypes\n\n")   # Added EnemyTypes
		DeathFile.write("print 'loading deaths...'\n\n\n")
		Blood.AfterCreateBlood = GrabarLaSangre

	if weapon != "" :
		armamuertoint2=Bladex.CreateEntity(ActualLevel+"WeapDeath"+`muertonum`, weapon, 0, 0, 0,"Weapon")
		ItemTypes.ItemDefaultFuncs(armamuertoint2)
		armamuertoint2.OnStopFunc=DetieneArmaMuerto
		
	muertoint2=Bladex.CreateEntity(ActualLevel+"GuyInPieces"+`muertonum`, raze, x, y, z,"Person")
	if MeshName:
		muertoint2.SetMesh(MeshName)
	muertoint2.Angle=angul
	if weapon != "" :
		Actions.TakeObject(muertoint2.Name, armamuertoint2.Name)
		print "The guy ",muertoint2.Name," got a gun named ",armamuertoint2.Name
	else:
		print "The guy ",muertoint2.Name,"is armless"
	EnemyTypes.EnemyDefaultFuncs(muertoint2)
	#Bladex.AddScheduledFunc(Bladex.GetTime()+90.0, MuertoyTroceado2, (muertoint2.Name,trozos))
	MuertoyTroceado2(muertoint2.Name,trozos)
	
	DeathFile.write(muertoint2.Name+" = "+"Bladex.CreateEntity('"+muertoint2.Name+"','"+muertoint2.Kind+"',"+str(muertoint2.Position[0])+","+str(muertoint2.Position[1])+","+str(muertoint2.Position[2])+",'Person'")
	if MeshName:
		DeathFile.write(",'"+MeshName+"')\n\n")
	else:
		DeathFile.write(")\n\n")
		
	DeathFile.write("EnemyTypes.EnemyDefaultFuncs("+muertoint2.Name+") \n")        # Added -LeadHead
	DeathFile.write(muertoint2.Name+".Angle = "+str(angul)+"\n")
	DeathFile.write(muertoint2.Name+".Life = 0\n")
	DeathFile.write(muertoint2.Name+".SetOnFloor()\n\n")
	Bladex.AddScheduledFunc(Bladex.GetTime()+60.0, CloseDeathFile, ())

	
	muertonum = muertonum+1
	

############  Quake FX ############

def Let_temblOff():
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = 0
	cam.EarthQuake = 0

def Temblores(time,pianoforte=500):
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = pianoforte
	cam.EarthQuake = 1
	Bladex.AddScheduledFunc(Bladex.GetTime()+time, Let_temblOff,())

############  Max Camera Functions ############

def DetenLaCamaraDeLaConchaELaLora(Camera,frame):
	import Scorer
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)

def LaunchMaxCamera(CamName,Start,End,Funchi=DetenLaCamaraDeLaConchaELaLora):
	import Scorer
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera(CamName,Start,End)
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	Bladex.DeactivateInput()
	cam.AddCameraEvent(-1,Funchi)

############ Bad Guys funcs ############
def HideObject(oname):
	if oname:
		obj = Bladex.GetEntity(oname)
		obj.RemoveFromWorld()		
		n_child=obj.GetNChildren()
		for n in range(n_child):
			HideObject(obj.GetChild(n))
		

def UnhideObject(oname):
	if oname:
		obj = Bladex.GetEntity(oname)
		obj.PutToWorld()		
		n_child=obj.GetNChildren()
		for n in range(n_child):
			HideObject(obj.GetChild(n))
			
			
def HideBadGuy(name,ciego=1,sordo=1):
	pers = Bladex.GetEntity(name)
	if not pers:
		print "WARNING : Trying to hide `"+name+"`but was deleted !"
		return
	pers.Deaf  = sordo
	pers.Blind = ciego
	pers.Freeze()
	pers.RemoveFromWorld()
	HideObject(pers.InvLeft)
	HideObject(pers.InvRight)
	HideObject(pers.InvRightBack)
	HideObject(pers.InvLeftBack)
	HideObject(pers.InvLeft2)
	char = Bladex.GetEntity("Player1")
	if char.ActiveEnemy == name:
		char.SetActiveEnemy("")
		

def UnhideBadGuy(name):
	pers = Bladex.GetEntity(name)
	pers.Deaf  = 0
	pers.Blind = 0
	pers.UnFreeze()
	pers.PutToWorld()
	UnhideObject(pers.InvLeft)
	UnhideObject(pers.InvRight)
	UnhideObject(pers.InvRightBack)
	UnhideObject(pers.InvLeftBack)
	UnhideObject(pers.InvLeft2)


############ Hint Funcs ############
def OnUse(entity, onuse ):
  import GameText
  GameText.WriteText(Bladex.GetEntity(entity).Data.MessageHint)

class EmptyClass:
	pass


def SetHint(gp,Name,OnUseData="",Priority=8.0,Distance=4000.0):
	import MenuText
	Reference.EntitiesSelectionData[gp.Name]=(Priority,Distance,MenuText.GetMenuText(Name))
	
	if type(OnUseData)==type(""):
		if OnUseData != "":
			gp.UseFunc          = OnUse
			if not gp.Data:
				gp.Data = EmptyClass()
			gp.Data.MessageHint = OnUseData
	else:
		gp.UseFunc = OnUseData

# SetHint(Bladex.GetEntity(char.InvRight),"Mierda","M7T4")

############ Quake steps funcs (no rocketlauncher avail) ############
QuakeFactor = 100

def QuakeStep(personaje):
	global QuakeFactor
	
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = QuakeFactor
	cam.EarthQuake = 1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.125, QuakeHalf,())

def QuakeHalf():
	QuakeStepCounter = 1
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = cam.EarthQuakeFactor/2
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.125, QuakeStop,())

def QuakeStop():
	QuakeStepCounter = 2
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = 0
	cam.EarthQuake = 0

######## FIRE SECTORS #######
FIRE_DAMAGE = 1.0/50.0

### Now affected by fire resistance
### 			-LeadHead
def QuemaTimer(e_name, time):
  char = Bladex.GetEntity(e_name)
  res = (1.0 - char.Data.GetResistance("Fire"))

  if char.Life <= 0:
    Actions.FireDeath(e_name)
    char.RemoveFromList("Timer15")
    char.TimerFunc=""
  else:
    ttlDamage = ((FIRE_DAMAGE * CharStats.GetCharMaxLife(char.Kind,char.Level)) * res)
    char.Life = char.Life - ttlDamage

    ## Also generate smoke when taking damage
    if ttlDamage:
      x,y,z = char.Position
      smoke=Bladex.CreateEntity("FireSectorSmoke", "Entity Particle System D1", x, y, z)
      smoke.ParticleType="DarkSmoke"
      smoke.YGravity=-2500.0
      smoke.Friction=0.05
      smoke.PPS=24
      smoke.Velocity=0.0, -27.0, 0.0
      smoke.RandomVelocity=19.0
      smoke.DeathTime=Bladex.GetTime()+0.5
      node= 0
      char.LinkToNode(smoke,node)
      ### Do a sound when stepping in
      snd_name=e_name+"_LoopFireSnd"
      sound=Bladex.GetEntity(snd_name)
      if not sound:
        sound=Bladex.CreateEntity(snd_name, "Entity Sound", x,y,z )
        sound.Volume = 0.9
        sound.MinDistance=5000.0
        sound.MaxDistance=10000.0
        sound.SetSound("../../Sounds/Ember-crackle.wav")
      else:
        sound.Position=char.Position

      sound.PlaySound(-1)


def EntraQuema(triggername,entityname):
  if entityname=="Player1":
    char = Bladex.GetEntity("Player1")
    if char.Life>0:
        char.SubscribeToList("Timer15")
        char.TimerFunc=QuemaTimer
        
		### Do a sound when stepping in
        snd_name=entityname+"_EntrSnd"
        EntrySound=Bladex.GetEntity(snd_name)
        if not EntrySound:
            EntrySound=Bladex.CreateEntity(snd_name, "Entity Sound", char.Position[0], char.Position[1], char.Position[2] )
            EntrySound.Volume = 0.8
            EntrySound.SetSound("../../Sounds/flus1.WAV")
        else:
            EntrySound.Position=char.Position
        EntrySound.PlaySound(0)

def SaleQuema(triggername,entityname):
  if entityname=="Player1":
    char = Bladex.GetEntity("Player1")
    if char.Life>0:
        char.RemoveFromList("Timer15")
        char.TimerFunc=""
		
        ### Stop looping sound when exiting
        snd_name=entityname+"_LoopFireSnd"
        sound=Bladex.GetEntity(snd_name)
        if sound and sound.Playing:
            sound.Stop()

######  Assignation funcs ######
def FireOnGS(name):
	Bladex.SetTriggerSectorFunc(name, "OnEnter", EntraQuema )
	Bladex.SetTriggerSectorFunc(name, "OnLeave", SaleQuema  )

def FireOnS(sec):
    	sec.OnEnter = EntraQuema
    	sec.OnLeave = SaleQuema

######## NAILS DAMAGE ########

def EntraPincha(triggername,entityname):
	import Scorer
	ent = Bladex.GetEntity ( entityname )
	if (ent.Person):
		if entityname=="Player1":
			Bladex.GetEntity("Camera").TType=0
			AuxFuncs.FadeTo(1.0,60.0,32,0,0)
			Scorer.SetVisible(0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, MuereDeVerdadPincha,(ent,))

		p = ent.Position
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],9999,0,0 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],9999,0,9999 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],3333,0,0 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],9999,0,3333 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],0,0,3333 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],0,0,9999 )
		#Blood.BleedingImpact(ent , p[0], p[1], p[2],0,0,0 )

def MuereDeVerdadPincha(ent):		
		ent.Life = 0
		ent.Wuea = Reference.WUEA_ENDED
		ent.SetTmpAnmFlags(1,1,1,0,5,1,0)
		ent.LaunchAnmType("dth_rock")		
		
def NailOnGS(name):
    	Bladex.SetTriggerSectorFunc(name, "OnEnter", EntraPincha )

def NailOnS(sec):
    	sec.OnEnter = EntraPincha

######## Enemy Deaths Detector #######
class E_GroupAux:
  ObjId=-1

  def __init__(self):
    self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
    ObjStore.ObjectsStore[self.ObjId]=self

  def persistent_id(self):
    return self.ObjId

  def __getitem__(self,key):
    return self.__dict__[key]

  def __setitem__(self,key,value):
    self.__dict__[key]=value

  def __getstate__(self):
    return (1,self.ObjId)

  def __setstate__(self,parm):
    if parm[0]==1:
      self.ObjId=parm[1]
      ObjStore.ObjectsStore[self.ObjId]=self


class E_Grup:

	ObjId=0
	n=0
	OnDeath=None
	Guys = []
	ImDeadFuncs = None
	
	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		self.n           = 0    # Zero enemies
		self.OnDeath     = None # No Callback
		self.Guys        = []
		self.ImDeadFuncs = E_GroupAux()
		ObjStore.ObjectsStore[self.ObjId]=self

	def persistent_id(self):
		return self.ObjId

	def ImDeadFunc(self,Name):
		self.ImDeadFuncs["Ch_"+Name](Name)
		self.n = self.n - 1
		#print "Quedan",self.n
		Bladex.GetEntity(Name).ImDeadFunc = self.ImDeadFuncs["Ch_"+Name]		
		self.Guys.remove(Name)
		if self.n == 0:
			if self.OnDeath:
				self.OnDeath()
			
	def AddGuy(self,Name):
		e                      = Bladex.GetEntity(Name)
		self.ImDeadFuncs["Ch_"+Name] = e.ImDeadFunc
		e.ImDeadFunc           = self.ImDeadFunc
		self.n = self.n + 1
		if Name in self.Guys:
			print "E_Grup error : "+Name+" is allready here."
		else:
			self.Guys.append(Name)
	
	def HideBadGuys(self):
		for Name in self.Guys:
			HideBadGuy(Name)
	
	def UnhideBadGuys(self,number):
		counter = 0
		for Name in self.Guys:
			counter = counter+1
			UnhideBadGuy(Name)
			if counter>=number:
				return counter
		return counter
	
	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
		ImDeadFuncsAux=[]
		for i in self.ImDeadFuncs.__dict__.keys():
			if i!="ObjId":
				ImDeadFuncsAux.append((i,GameStateAux.SaveFunctionAux( self.ImDeadFuncs[i] )))

		return (1,
					self.ObjId, # De GameStateAux.PersistentObject
					self.ImDeadFuncs,
					self.n,
					GameStateAux.SaveFunctionAux(self.OnDeath),
					self.Guys,
					ImDeadFuncsAux
				)


	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		
		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.ImDeadFuncs=parm[2]
			self.n=parm[3]
			GameStateAux.LoadFunctionAux(parm[4],self,"OnDeath")
			self.Guys=parm[5]
			ImDeadFuncsAux=parm[6]
			for i in ImDeadFuncsAux:
##				self.ImDeadFuncs[i[0]]=GameStateAux.LoadFunctionAux(i[1])
				GameStateAux.LoadFunctionAux(i[1],self.ImDeadFuncs,i[0])


		else:
			print "Door.__setstate__() -> Version mismatch"
			# Valores por si valen para algo.
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
			self.n           = 0    # Zero enemies
			self.OnDeath     = None # No Callback
			self.Guys        = []
			self.ImDeadFuncs = E_GroupAux()

#----------------------------------------------------------------#

PersonasEnLlamas = []

def EnciendeEnLlamas(o,Intensity = 15,Precission=0.1):
	global PersonasEnLlamas
	
	if not (o.Kind in PersonasEnLlamas):
		PersonasEnLlamas.append(o.Kind)
		Bladex.AddCombustionDataFor(o.Kind, "Fire", 250, 400, 4, 1, 3, 144000) # se extingira en 40 horas!
	
	o.SelfIlum = 0.0
	o.CatchOnFire(0,0,0)
	
	luz             = Bladex.CreateEntity(o.Name+"Luz","Entity Spot",0,0,0)
	luz.Color       = 200,100,0
	luz.Intensity   = Intensity
	luz.Precission  = Precission
	luz.CastShadows = 0
	luz.Visible     = 1
	luz.SizeFactor  = 0

	o.Link(luz)

### objetos Alfa ###
def ObjAlpha(o,alpha=0.8,SelfIlum=0.0):
	o.Alpha       = alpha
	o.RasterMode  ="AdditiveAlpha"
	o.RasterMode  ="Read"
	o.CastShadows = 0
	o.SelfIlum    = SelfIlum
	
	
	
#----------------------------------------------------------------#
#  Funciones auxiliares para la aparicion valida de objetos      #
#----------------------------------------------------------------#	

def ValidAppear(pos,func=None,param=None):
	entid = Bladex.GetEntitiesAt(pos[0],pos[1],pos[2],4000)
	for on in entid:
		o = Bladex.GetEntity(on)
		if o.Person:
			if o.Life > 0:
				if o.Alpha >0.01:
					print "Trying to do it, but",on,"is bothering. Next try in 5 seconds."
					if func:
						Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, ValidAppear,(pos,func,param))
					return 0
	if func:
		apply(func,param)
		print "The function was XQted"
	else:
		return 1

def CreateFalseCube(pos,timeToKill = -1,Name = ""):
	o = Bladex.CreateEntity(Name + "quad","Bloque",pos[0],pos[1]-1500,pos[2])
	o.Orientation = (0.707107245922, 0.0, 0.0, 0.707106292248)
	o.Scale = 4
	o.ExclusionMask=2|4			# PLAGUE: need to add magic excl group -LeadHead
	o.CastShadows = 0
	o.Alpha       = 0.0
	o.RasterMode  ="Read"
	if timeToKill != -1:
		Bladex.AddScheduledFunc(Bladex.GetTime()+timeToKill, o.SubscribeToList,("Pin",))
	Reference.EntitiesSelectionData[o.Name]=(0,0,"")
	return o
	
	
#
#  Destroy the pools and cadavres but the limbs and weapons, no.
#----------------------------------------------------------------#	
def CleanArea(x,y,z,radius):
	Bladex.CleanArea(x,y,z,radius)
	
	list = Bladex.GetEntitiesAt(x,y,z,radius)
	enCounter = 0
	
	for name in list:
		o = Bladex.GetEntity(name)
		if o.Person:
			if o.Life <= 0.0:
				if o.Name != "Player1":
					HideBadGuy(o.Name)
					enCounter = enCounter + 1
	
	return enCounter

#
# Detects if a player joins into a sector
#--------------------------------------------#
def EnterSecEvent(x,y,z,func):	
	sec = Bladex.GetSector(x,y,z)
	EnterSecEventSector(sec,func)

def GetSectorIdx(pos):
	if (type(pos)!=types.TupleType):
		return pos
	else:
		return Bladex.GetSector(pos[0],pos[1],pos[2]).Index
		
def EnterSecIdEvent(id,func):
	if type(id)==types.StringType:
		EnterTSEvent(id,func)
		return id
	elif type(id)==types.TupleType:
		sec = Bladex.GetSector(id[0],id[1],id[2])
		EnterSecEventSector(sec,func)
		return sec.Index
	else:
		sec = Bladex.GetSector(id)
		EnterSecEventSector(sec,func)
		return id

def EnterSecEventSector(sec,func):
	global SectorTable

	if sec:
		if not SectorTable.has_key(sec.Index):
			if sec.OnEnter:
				print "ERROR : OnEnter Asigned to",sec.OnEnter
			else:
				SectorTable[sec.Index]=[]
		else:
			numerox = len(SectorTable[sec.Index])
			if numerox>0:
				if Reference.PYTHON_DEBUG >= 2:
					print "Warning : OnEnter have",numerox,"functions"
			
		SectorTable[sec.Index].insert(0,func)
		sec.OnEnter = OnPlayerEnter
		return sec.Index
	else:
		print "ERROR : Sector invalid!"
	
def OnPlayerEnter(sectorindex,entityname):
	global SectorTable
	
	if entityname == "Player1":
		funclist = []
		
		# guarda la lista de funciones a ejecutar
		for f in SectorTable[sectorindex]:
			funclist.append(f)
		
		# borra la lista y todo lo relacionado a ella
		del SectorTable[sectorindex]
		if type(sectorindex)==types.StringType:
			Bladex.SetTriggerSectorFunc(sectorindex, "OnEnter", None )
		else:
			Bladex.GetSector(sectorindex).OnEnter = None
		
		# elimina las funciones que se llaman si se entra en mas de un sector
		for f in funclist:
			for key in SectorTable.keys():
				for e in SectorTable[key]:
					if e == f:
						SectorTable[key].remove(e)
		
		# ejecuta la lista de funciones en cuestion
		for f in funclist:			
			try:
				f()
			except:
				f(sectorindex)
	
	
SectorTable = {}

#
##   Ghost sector tools
####################################
def EnterTSEvent(secname,func):
	global SectorTable

	if secname:
		if not SectorTable.has_key(secname):
			if Bladex.GetTriggerSectorFunc(secname,"OnEnter"):
				print "ERROR : OnEnter Asigned to ",secname
			else:
				SectorTable[secname]=[]
		else:
			numerox = len(SectorTable[secname])
			if numerox>0:
				if Reference.PYTHON_DEBUG >= 2:
					print "Warning : OnEnter have",numerox,"functions"			
		SectorTable[secname].insert(0,func)
		Bladex.SetTriggerSectorFunc(secname, "OnEnter", OnPlayerEnter )		
		return secname
	else:
		print "ERROR : Sector '"+secname+"' invalid!"

# darfuncs.EnterSecEvent(char.Position[0],char.Position[1],char.Position[2],x)






###
###  Template to make a clean in a area.
###
##import darfuncs
##
##def EntrayBorra():
##	darfuncs.CleanArea(clnX,clnY,clnZ,clnRadius)
##	
##darfuncs.EnterSecEvent(secX,secY,secZ,EntrayBorra)



def LuzChapuzera(light,FinishTime,delta = 1):
	t = Bladex.GetTime()	
	light.Move(0,0,delta)
	if t<FinishTime:
		Bladex.AddScheduledFunc(t+0.0, LuzChapuzera,(light,FinishTime,-delta))

###
### Chapuza solution with the light cones
###
##
##darfuncs.LuzChapuzera(Bladex.GetEntity("luzbonita"), Bladex.GetTime() + 3.0) # mueve "luzbonita" durante 3 segundos

#
# The matrix FX is cool to show the capabilites of the engine
#################################################################

#
# Globals for the MatrixFX
#
MatrixTime = 0
MatrixCameraState = 0
MatrixPerson = ""

def MatrixFXAfterFrameFunc(time):
	global MatrixTime
	
	GiraCamara( (time-MatrixTime)*2.5,1000)
	MatrixTime = time

def StartMatrixFX(ESource = "Player1"):
	global MatrixTime
	global MatrixCameraState
	global MatrixPerson

	if MatrixPerson == "":
		Bladex.SetTimeSpeed(0.2)
		InitGiroCamera(ESource)
		Bladex.RemoveAfterFrameFunc("MatrixFX")
		Bladex.SetAfterFrameFunc("MatrixFX",MatrixFXAfterFrameFunc)
		MatrixTime = Bladex.GetTime()
		MatrixCameraState = Bladex.GetEntity("Camera").PViewType
		Bladex.GetEntity("Camera").PViewType = 0
		MatrixPerson = ESource

def StopMatrixFX():
	global MatrixTime
	global MatrixCameraState
	global MatrixPerson
	import netgame

	if MatrixPerson != "":
		Bladex.SetTimeSpeed(1.0)
		Bladex.RemoveAfterFrameFunc("MatrixFX")
		netgame.SetPersonView(MatrixPerson)
		cam = Bladex.GetEntity("Camera")
		cam.PViewType = MatrixCameraState
		cam.Cut()
	
		MatrixTime        = 0
		MatrixCameraState = 0
		MatrixPerson      = ""



def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(muertonum,ActualLevel,QuakeFactor,FIRE_DAMAGE,PersonasEnLlamas,SectorTable, MatrixTime, MatrixCameraState, MatrixPerson)
  
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()

  global muertonum
  global ActualLevel
  global QuakeFactor
  global FIRE_DAMAGE
  global PersonasEnLlamas
  global SectorTable
  
  muertonum         = d[0]
  ActualLevel       = d[1]
  QuakeFactor       = d[2]
  FIRE_DAMAGE       = d[3]
  PersonasEnLlamas  = d[4]
  SectorTable       = d[5]
  MatrixTime        = d[6]
  MatrixCameraState = d[7]
  MatrixPerson      = d[8]



import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
