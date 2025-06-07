##///
##||| POCIMAC.PY TITANIUM
##||| Change list:
##||| * Changed functions SoltarPocima, BeberPocima
##||| * Added new function EmptyPotion (implementation needs to be redone probably, current one is way too messy)
##||| * Self Iluminated potions lose their luminosity as they fade
##||| * Added support for potion hot-keys
##||| * Chars will no longer turn their head to empty potions or be selectable at all
##||| * Potions will now start fading with a 5s delay
##||| * Fixed a bug which would cause drawing right item from back (AND ONLY THE RIGHT) after drinking a potion
##||| * Using a potion from inventory while a standard object is in hand will properly make you drink the potion now
##\\\ 

import OnInitTake
import ReadGSFile
import Bladex
import Actions
import CharStats
import whrandom
import GenFX
import Reference
import AuxFuncs
import darfuncs
import os
#import BCopy


POTION_STATE_USED = 0
POTION_STATE_UNUSED = 1

POTION_TYPE_EAT = 0
POTION_TYPE_DRINK_RIGHT = 1
POTION_TYPE_GULP = 2
POTION_TYPE_DRINK_LEFT = 3

POWERUP_TYPE_LIFE = 0
POWERUP_TYPE_ATTACK = 1

POWERUP_DEACTIVATED	 = 2
POWERUP_ACTIVATED = 1

#B_PARTICLE_GTYPE_BLEND=1


def RestoreWounds(EntityName, woundfactor=0.0):
	me= Bladex.GetEntity(EntityName)
	woundlist= []
	for i in range (32):
		if me.GetWoundedZone(i):
			woundlist.append(i)

	while len(woundlist) and len(woundlist)/11.0 > woundfactor:
		if woundlist.count(3):
			wound2clear= 3 # Head
		elif whrandom.randint(0,1):
			wound2clear= whrandom.choice(woundlist)
		else:
			wound2clear= woundlist[0]
		me.SetWoundedZone(wound2clear, 0)
		woundlist.remove(wound2clear)

def RestoreWoundsToLifeLevel(EntityName):
	me= Bladex.GetEntity(EntityName)
	woundfactor= 1.0- (me.Life / CharStats.GetCharMaxLife(me.Kind,me.Level))
	RestoreWounds(EntityName, woundfactor)

class Pocima:
	def __init__(self,pot):
		self.Hand = 0
		self.Estado = POTION_STATE_UNUSED
		self.Increment = 25
		self.MaxLife = 200
		self.DrinkFunc = 0
		self.DrinkFuncArguments = ()
		self.Sonido=0
		self.Type = POTION_TYPE_DRINK_RIGHT
		self.OHand = ""
		self.PowerPotion = 0
		self.TimeStartPowerPotion = 5.0
		self.TimePowerPotion = 10.0
		self.OldFDefense = 0.0
		self.OldFAttack	= 0.0
		self.FDefense = 4.0
		self.FAttack = 4.0
		self.PowerUpEstado = POWERUP_DEACTIVATED
		self.LifePowerUpI = 0
		self.LifePowerUp = 100
		self.FadeDelta = (0.2 /60.0)
		self.CuresPoison= 0
		self.Takeable=1


	def IncrementLife(self):
		UsedBy2 = Bladex.GetEntity(self.entity)
		UsedBy = self

		if (UsedBy.PowerUpEstado == POWERUP_ACTIVATED):
			if (UsedBy.LifePowerUpI < UsedBy.LifePowerUp):
				life = UsedBy2.Life + 1.0

				if life <= self.MaxLife:
					UsedBy.LifePowerUpI = UsedBy.LifePowerUpI + 1.0
					UsedBy2.Life =  life
					RestoreWoundsToLifeLevel(UsedBy2.Name)

				timenext = 0.50

				Bladex.AddScheduledFunc(Bladex.GetTime() + timenext,self.IncrementLife,())
			else:
				UsedBy.PowerUpEstado = POTION_STATE_USED

	def ActivatePowerUp(self,sector,entity):
		#UsedBy = Bladex.GetEntity(entity)
		UsedBy = self

		if (UsedBy.PowerUpEstado == POWERUP_DEACTIVATED):
			self.entity = entity
			UsedBy.PowerUpEstado = POWERUP_ACTIVATED
			Bladex.AddScheduledFunc(Bladex.GetTime() + 0.50,self.IncrementLife,())

	def DeactivatePowerUp(self,sector,entity):
		if (entity == self.entity):
			#UsedBy = Bladex.GetEntity(entity)
			UsedBy = self

			if (UsedBy.PowerUpEstado == POWERUP_ACTIVATED):
				UsedBy.PowerUpEstado = POWERUP_DEACTIVATED

	def FinishPowerAtack(self,entity):
		UsedBy = Bladex.GetEntity(entity)
		if UsedBy.Data.PowerPotion==1 :
			UsedBy.SelfIlum = 0.0
			UsedBy.Data.FDefense = self.OldFDefense
			UsedBy.Data.FAttack = self.OldFAttack
			UsedBy.Data.PowerPotion = 2

	def StartPowerAtack(self):
		if (self.PowerUpEstado == POWERUP_ACTIVATED):
			UsedBy = Bladex.GetEntity(self.entity)
			UsedBy.SelfIlum = 1.0
			self.OldFDefense = 1.0
			self.OldFAttack = 1.0

			UsedBy.Data.FDefense = self.FDefense
			UsedBy.Data.FAttack = self.FAttack
			UsedBy.Data.PowerPotion = 1

			Bladex.AddScheduledFunc(Bladex.GetTime() + self.TimePowerPotion,self.FinishPowerAtack,(self.entity,))

	def ActivatePowerUpAtack(self,sector,entity):
		if (self.PowerUpEstado == POWERUP_DEACTIVATED):
			UsedBy = Bladex.GetEntity(entity)

			if (UsedBy.Data.PowerPotion == 0):
				self.PowerUpEstado = POWERUP_ACTIVATED
				self.entity = entity
				Bladex.AddScheduledFunc(Bladex.GetTime() + self.TimeStartPowerPotion,self.StartPowerAtack,())

	def DeactivatePowerUpAtack(self,sector,entity):
		if (entity == self.entity):
			self.PowerUpEstado = POWERUP_DEACTIVATED

	def Reset(self,Players = 0):
		#UsedBy = Bladex.GetEntity(self.entity)

		if (self.Type == POWERUP_TYPE_LIFE):
			UsedBy = self

			UsedBy.PowerUpEstado = POWERUP_DEACTIVATED
			UsedBy.LifePowerUpI = 0.0
		else:
			for name in Players:
				ent = Bladex.GetEntity(name)
				ent.Data.PowerPotion = 0
				ent.Data.FDefense = 1.0
				ent.Data.FAttack = 1.0
				ent.SelfIlum = 0.0

	def FadeOut(self,entity,timer):
		poc = Bladex.GetEntity(entity)
		poc.Alpha = poc.Alpha - poc.Data.FadeDelta
		if len(poc.Lights):
			poc.Lights = [(poc.Alpha/2, poc.Lights[0][1], poc.Lights[0][2])]
        
		if poc.SelfIlum:                                     # Should make drunk power potions fade better now
			poc.SelfIlum = poc.SelfIlum - (0.1 / 60.0)       #       - LeadHead
        
		if poc.Alpha <= 0:
			poc.SubscribeToList("Pin")

def RestoreHand(entidad):
	char = Bladex.GetEntity(entidad)
	char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
	char.LaunchAnmType("Chg_r")

def TakePotionUsed():
	pass

def PocimaNoSoltada(entidad):
	Reference.debugprint("PocimaNoSoltada")
	char = Bladex.GetEntity(entidad)
	object = Bladex.GetEntity(char.Data.obj_used)

	if object.Data.Estado == POTION_STATE_USED:
		SoltarPocima(entidad,0)
	else:
		object.ExcludeHitFor(char)
		inv = char.GetInventory()

		if object.Data.Type == POTION_TYPE_DRINK_LEFT:
			# In Combat and using left hand's second slot
			object.Data.Estado = POTION_STATE_UNUSED
			inv.LinkLeftHand2("None")
			inv.RemoveObject(object.Name)
			impulse = char.Rel2AbsVector(1000.0 * object.Mass, -1000.0 * object.Mass, 0.0)
			object.Impulse(impulse[0],impulse[1],impulse[2])
		else:
			object.Data.Estado = POTION_STATE_USED
			object.Data.Takeable= 0
			inv.LinkRightHand("None")

			if object.Data.Hand == 1:          
				char.AnmEndedFunc = RestoreHand

			inv.RemoveObject(char.Data.obj_used)
			impulse = char.Rel2AbsVector(-1000.0 * object.Mass, -1000.0 * object.Mass, 0.0)
			object.Impulse(impulse[0],impulse[1],impulse[2])

def SoltarFood(Entidad):
	char = Bladex.GetEntity(Entidad)
	char.AnmEndedFunc = ""
	inv = char.GetInventory()
	inv.LinkRightHand("None")
	inv.RemoveObject(char.Data.obj_used)
	Actions.TakeStraightRecover(Entidad)

def SoltarPocima(Entidad,Evento = 0):
	char = Bladex.GetEntity(Entidad)
	char.AnmEndedFunc = ""
	if Evento:
		char.DelAnmEventFunc(Evento)
	object = Bladex.GetEntity(char.Data.obj_used)

	inv = char.GetInventory()

	if object.Data.Type == POTION_TYPE_DRINK_LEFT:
		# In Combat and using left hand's second slot
		inv.LinkLeftHand2("None")
		inv.RemoveObject(char.Data.obj_used)
		impulse = char.Rel2AbsVector(1000.0 * object.Mass, -1000.0 * object.Mass, 0.0)
		object.Impulse(impulse[0],impulse[1],impulse[2])
	else:
		inv.LinkRightHand("None")

		if object.Data.Hand == 1:
			char.AnmEndedFunc = RestoreHand
		else:
			char.AnmEndedFunc= Actions.TakeStraightRecover
		inv.RemoveObject(char.Data.obj_used)
		impulse = char.Rel2AbsVector(-1000.0 * object.Mass, -1000.0 * object.Mass, 0.0)
		object.Impulse(impulse[0],impulse[1],impulse[2])

### New func - now will fade potions only when they stop moving.
### Makes them stay on the screen longer so you have more time to witness my awful code in action. -LeadHead
def FadeOnStop(potName):
	Poti = Bladex.GetEntity(potName)
	Poti.TimerFunc = Poti.Data.FadeOut
	Poti.SubscribeToList("Timer60")
	# print `potName` + " stopped moving, fading"
	# Poti.OnStopFunc = None

### PLAGUE: To do - make lights and self-ilum fade immediately after drinking, but have the mesh fade only on stop.

def RestorePowerPotion(Entidad,Potion):
	char = Bladex.GetEntity(Entidad)

	char.Data.FDefense = Potion.OldFDefense
	char.Data.FAttack = Potion.OldFAttack
	char.Data.PowerPotion = 0

def BeberPocima(Entidad,Evento):
	char = Bladex.GetEntity(Entidad)
	char.DelAnmEventFunc(Evento)
	Poti = Bladex.GetEntity(char.Data.obj_used)
	Pot = Poti.Data
	Pot.Estado = POTION_STATE_USED

	if os.path.exists("../../3DObjs/"+Poti.Kind+"_E.bod"):
		PotE = EmptyPotion(Poti.Name)
		char.Data.obj_used = PotE.Name
		Poti = Bladex.GetEntity(char.Data.obj_used)
		Pot = Poti.Data
		#print "Potion emptied and assigned data successfully"
	else:
		print "potion_E not found for "+Poti.Name
		pass
        
	if (Pot.PowerPotion):
		Pot.OldFDefense = 1.0
		Pot.OldFAttack = 1.0

		char.Data.FDefense = Pot.FDefense
		char.Data.FAttack = Pot.FAttack
		char.Data.PowerPotion = 1
		Bladex.AddScheduledFunc(Bladex.GetTime() + Pot.TimePowerPotion,RestorePowerPotion,(Entidad,Pot))
		GenFX.AddPersonItemFX(Entidad, Poti.Name, Pot.TimePowerPotion)
	else:
		if Pot.Increment == -1:
			char.Life = CharStats.GetCharMaxLife(char.Kind,char.Level)
			# Restore wounds
			RestoreWounds(Entidad)
		else:
			Life = char.Life + Pot.Increment
			LimitLife = CharStats.GetCharMaxLife(char.Kind,char.Level)

			if (Life > LimitLife):
				char.Life = LimitLife
			else:
				char.Life = Life
			RestoreWoundsToLifeLevel(Entidad)

		if Pot.CuresPoison:
			char.Data.UnVenom ()
	if (Pot.DrinkFunc != 0):   
		Bladex.AddScheduledFunc(Bladex.GetTime(),Pot.DrinkFunc,Pot.DrinkFuncArguments)
	Pot.Sonido.Play(char.Position[0],char.Position[1],char.Position[2],0)

    ### The following entries were originally under function "SoltarPocima"
    ### They have been moved here to fix a bug when a potion is dropped due to taking damage
    ### before the drink animation completes, creating "ghost" potions that cannot be interacted with -LeadHead
	Poti.ExcludeHitFor(char)
	if Pot.Type != POTION_TYPE_EAT:                                                  #  Now fades only when stopped moving.
		Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, FadeOnStop,(Poti.Name,))     #        -LeadHead
	# Poti.TimerFunc = Poti.Data.FadeOut    #
	# Poti.SubscribeToList("Timer60")       #
	Poti.Data.Takeable=0
	# darfuncs.SetHint(Poti,"")
	darfuncs.SetHint(Poti,"",0,0,0)   # Stop looking at empty potions -LeadHead
	OnInitTake.AddOnInitTakeEvent(Poti.Name,TakePotionUsed)

        


def CreateMiguillas(Entidad,Evento):
	char = Bladex.GetEntity(Entidad)
	Poti = Bladex.GetEntity(char.Data.obj_used)

	miguillas=Bladex.CreateEntity("Miguillas", "Entity Particle System D1",0,0,0)
	#miguillas.D=-3600, 0, 0
	miguillas.ParticleType="Miguillas"
	miguillas.YGravity=10000.0
	miguillas.Friction=0.2
	miguillas.RandomVelocity=10.0
	miguillas.PPS=200
	miguillas.Time2Live=32
	miguillas.DeathTime=Bladex.GetTime() + 0.1

	Poti.Link(miguillas)

	if Evento == "Bocado1Event":            # PLAGUE: Useless piece of code,
		Poti.TimerFunc = Poti.Data.FadeOut  #   because it would get executed
		Poti.SubscribeToList("Timer60")     #   in BeberPocima() anyway???
		Poti.Data.Takeable=0                #

	#Pot.Estado = POTION_STATE_UNUSED


def UsePotion3(Entity):
	char = Bladex.GetEntity(Entity)
	UsePotion2(char.Data.obj_used)

def UsePotion2(NombrePocima):
	Reference.debugprint("UsePotion2")
	Pocima = Bladex.GetEntity(NombrePocima)
	#Pocima.Data.Estado = POTION_STATE_USED
	Char = Bladex.GetEntity(Pocima.Data.UsedBy)
	Reference.debugprint(Char.AnmEndedFunc)
	#Char.HitFunc = TirarPocima
	Char.AnmEndedFunc= Actions.TakeStraightRecover

	if (Pocima.Data.Type==POTION_TYPE_EAT):
		Char.LaunchAnmType("eat00")
		Char.AddAnmEventFunc("Bocado1Event",CreateMiguillas)
		Char.AddAnmEventFunc("Bocado2Event",CreateMiguillas)
		Char.AnmEndedFunc= SoltarFood
	elif (Pocima.Data.Type == POTION_TYPE_DRINK_RIGHT):
		Char.LaunchAnmType("drink")
		Char.AddAnmEventFunc("PickBottle",PickPotion)
	elif (Pocima.Data.Type == POTION_TYPE_GULP):
		Char.LaunchAnmType("gulp00")
	else:
		print 'Unknown Potion Type' + `Pocima.Data.Type`

	Char.AddAnmEventFunc("drinkingEvent",BeberPocima)
	#print 'should throw bottle with event ThrowBottle in animation '+Char.AnimName
	Char.AddAnmEventFunc("ThrowBottle",SoltarPocima)

def TryToUsePotion(me, object):
	if not Reference.HealthIncrease.has_key(object.Kind):
		#print `object.Name`+" has no health increase"    
		return 1

	if Reference.DefaultObjectData[object.Kind][0] == Reference.OBJ_ITEM:
		#print object.Name+" is an item"
		return 1
    
	#print "Trying to use " + `object.Name`
	return CanIUseThePotion(me, object)

def CanIUseThePotion(me, object):
	if CharStats.GetCharMaxLife(me.Kind,me.Level) <= me.Life:
		if me.Name == "Player1":
			# import GameText
			# import MenuText
			
			# GameText.WriteTextAux(MenuText.GetMenuText("I don't need it yet"),2.0,255,255,255,[],None,1)
			
			Actions.ReportMsg("I don't need it yet")	# Optimization		-LeadHead
		return 0
	else:
		return 1

Actions.TryToTakeCallBacks.append(TryToUsePotion)

def UsePotion(NombrePocima,TipoUso):
	Pocima = Bladex.GetEntity(NombrePocima)
	Char = Bladex.GetEntity(Pocima.Data.UsedBy)

	if Reference.HealthIncrease.has_key(Pocima.Kind):
		if not CanIUseThePotion(Char,Pocima):
			return

	if (TipoUso == Actions.USE_FROM_INV and Pocima.Data.Estado == POTION_STATE_UNUSED):
		# Check if its a power potion, and we have one....
		try:
			if Pocima.Data.PowerPotion and Char.Data.PowerPotion:
				if Char.Name == "Player1":
					# import GameText
					# import MenuText

					# GameText.WriteTextAux(MenuText.GetMenuText("I don't need it yet"),2.0,255,255,255,[],None,1)
					Actions.ReportMsg("I don't need it yet")	# Optimization		-LeadHead
				return
		except AttributError: pass

		Pocima.Data.Hand = 0
		Char.Data.obj_used = NombrePocima
		Char.AnmEndedFunc = PocimaNoSoltada

		# Use from inventory
		Pocima.Data.Type = 1
		if not Char.InvRight:
			Char.Data.stuff_onback_b4 = Char.InvRightBack	# Added -LeadHead
			UsePotion2(NombrePocima)
		else:
			if Char.InCombat:
				if not Char.InvLeft2:
					Pocima.Data.Type = 3
					Char.LaunchAnmType("attack_drink")
					Char.AddAnmEventFunc("PickBottle",PickPotion)
					Char.AddAnmEventFunc("drinkingEvent",BeberPocima)
					Char.AddAnmEventFunc("ThrowBottle",SoltarPocima)

			elif Actions.IsRightHandStandardObject(Char.Name):
				if Actions.TryDropRight(Char.Name):
					Actions.DropReleaseEventHandler(Char.Name, "DropRightEvent")
				if not Char.InvRight:
					# UsePotion2(NombrePocima)		# This did nothing, now should work.
					Char.AnmEndedFunc=UsePotion3	#			-LeadHead

			else:
				Char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
				Char.LaunchAnmType("Chg_r")
				Pocima.Data.Hand = 1
				Pocima.Data.OHand = Char.InvRight
				Char.AnmEndedFunc=UsePotion3
	elif (TipoUso == Actions.USE_FROM_TAKE and Pocima.Data.Estado == POTION_STATE_UNUSED):
		# Automatic use from take
		Pocima.Data.Hand = 0
		Char.Data.obj_used = NombrePocima

		if (Pocima.Data.Type != POTION_TYPE_EAT):
			Pocima.Data.Type = POTION_TYPE_GULP
			Char.AnmEndedFunc=UsePotion3
		else:
			Char.AnmEndedFunc=UsePotion3


def PickPotion(Entidad,Evento):
	char=Bladex.GetEntity(Entidad)
	char.DelAnmEventFunc(Evento)
	Pocima = char.Data.obj_used
	object = Bladex.GetEntity(char.Data.obj_used)

	inv = char.GetInventory()
	if object.Data.Type==3:
		inv.LinkLeftHand2(Pocima)
	else:
		inv.LinkRightHand(Pocima)

def CreatePotion(Nombre,Increment = 25,MaxLife = 180):
	Pot = Bladex.GetEntity(Nombre)
	Pot.Static = 0
	Pot.Data = Pocima(Pot)
	Pot.UseFunc = UsePotion
	Pot.Data.Increment = Increment
	Pot.Data.MaxLife = MaxLife

	if Reference.HealthIncrease.has_key(Pot.Kind):
		Pot.Data.Increment   = Reference.HealthIncrease[Pot.Kind][0]
		Pot.Data.CuresPoison = Reference.HealthIncrease[Pot.Kind][1]

	Pot.Data.Sonido = Bladex.CreateSound('../../Sounds/Drink.wav', 'Drinking')
	Pot.Data.Sonido.Volume=1
	Pot.Data.Sonido.MinDistance=10000
	Pot.Data.Sonido.MaxDistance=20000

	return Pot.Data


def CreateFood(Nombre,Increment = 25,MaxLife = 180):
	Pot = Bladex.GetEntity(Nombre)
	Pot.Static = 0
	Pot.Data = Pocima(Pot)
	Pot.UseFunc = UsePotion
	Pot.Data.Increment = Increment
	Pot.Data.MaxLife = MaxLife

	Pot.Data.Type = POTION_TYPE_EAT
	Pot.Data.Sonido = Bladex.CreateSound('../../Sounds/bugbite-bone2.wav', 'Eating')
	#Pot.Data.Sound = Bladex.CreateSound('../../Sounds/Drink.wav', 'Drinking')
	Pot.Data.Sonido.Volume=1
	Pot.Data.Sonido.MinDistance=10000
	Pot.Data.Sonido.MaxDistance=20000

	Pot.Data.FadeDelta = (0.8 /60.0)

	if Reference.HealthIncrease.has_key(Pot.Kind):
		Pot.Data.Increment   = Reference.HealthIncrease[Pot.Kind][0]
		Pot.Data.CuresPoison = Reference.HealthIncrease[Pot.Kind][1]

	return Pot.Data

def CreatePowerPotion(Nombre,FD = 4.0,FA = 4.0,Time = 45):
	PowerPot = CreatePotion(Nombre)
	PowerPot.TimePowerPotion = Time
	PowerPot.PowerPotion = 1
	PowerPot.FDefense = FD
	PowerPot.FAttack = FA
	PowerPot.Increment = 0
	PowerPot.CuresPoison = 0
	pp                = Bladex.GetEntity(Nombre)
	pp.FiresIntensity = [ 45 ]
	pp.Lights         = [ (0.50000,0.050000,(0,128,255)) ]
	pp.SelfIlum       = 1
	spot = AuxFuncs.GetSpot(pp)
	if spot:
		spot.Visible      = 0
		spot.CastShadows  = 0




def CreatePowerUp(Sector,Name,Life = 100,MaxLife = 100):
	res=ReadGSFile.ReadGhostSectorFile(Sector)

	for igs in res:
		Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

	PowerUp = Pocima(0)

	Bladex.SetTriggerSectorFunc(Name, "OnLeave", PowerUp.DeactivatePowerUp)
	Bladex.SetTriggerSectorFunc(Name, "OnEnter", PowerUp.ActivatePowerUp)

	PowerUp.Type = POWERUP_TYPE_LIFE
	PowerUp.LifePowerUp = Life
	PowerUp.MaxLife = MaxLife

	return PowerUp

def CreatePowerUpAtack(Sector,Name,FD = 4.0,FA = 4.0,TimeD = 10,TimeL = 5):
	res=ReadGSFile.ReadGhostSectorFile(Sector)

	for igs in res:
		Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

	PowerUp = Pocima(0)

	Bladex.SetTriggerSectorFunc(Name, "OnLeave", PowerUp.DeactivatePowerUpAtack)
	Bladex.SetTriggerSectorFunc(Name, "OnEnter", PowerUp.ActivatePowerUpAtack)

	PowerUp.Type = POWERUP_TYPE_ATTACK
	PowerUp.TimeStartPowerPotion = TimeL
	PowerUp.TimePowerPotion = TimeD
	PowerUp.FDefense = FD
	PowerUp.FAttack = FA


	return PowerUp


def CreateDefaultPocimac(ObjectName):
	obj = Bladex.GetEntity(ObjectName)

	# check for Power Potions
	if obj.Kind == "PowerPotion":
		CreatePowerPotion(ObjectName)
		return 1

	# check for other stuff of PociMacs
	if not Reference.HealthIncrease.has_key(obj.Kind):
		return 0

	# check for Food
	if Reference.HealthIncrease[obj.Kind][2] == Reference.POCIMAC_FOOD:
		CreateFood(ObjectName)
		return 1

	# check for Potions
	if Reference.HealthIncrease[obj.Kind][2] == Reference.POCIMAC_POTION:
		CreatePotion(ObjectName)
		return 1

	print "FATAL ERROR: The PociMac type is not defined, yet."
	return 0


####
# Functions for empty potion meshes -LeadHead
####

def EmptyPotion(PotionName):
    obj  = Bladex.GetEntity(PotionName)
    user = Bladex.GetEntity(obj.Data.UsedBy)
    inv  = user.GetInventory()
    

    newPot=Bladex.CreateEntity(obj.Name+"_E", obj.Kind+"_E", obj.Position[0], obj.Position[1], obj.Position[2],"Physic")
    newPot.Orientation = obj.Orientation
    newPot.Scale       = obj.Scale
    
    Reference.EntitiesObjectData[newPot.Name] = Reference.DefaultObjectData[obj.Kind]
    newPot.Data           = obj.Data
    newPot.UseFunc        = obj.UseFunc
    newPot.FiresIntensity = obj.FiresIntensity
    newPot.Lights         = obj.Lights
    newPot.SelfIlum       = obj.SelfIlum
    spot    = AuxFuncs.GetSpot(obj)
    newSpot = AuxFuncs.GetSpot(newPot)
    if spot and newSpot:
        newSpot.Visible     = spot.Visible
        newSpot.CastShadows = spot.CastShadows
    elif newSpot:
        newSpot.Visible     = 0    
        newSpot.CastShadows = 0

    if (obj.Data.Type == POTION_TYPE_DRINK_LEFT):
        # In Combat and using left hand's second slot
        inv.LinkLeftHand2(newPot.Name)
        newPot.Data.Type = 3
    else:
        inv.LinkRightHand(newPot.Name)
        
    inv.RemoveObject(obj.Name)
    obj.SubscribeToList("Pin")
    return newPot



####               ####
# Potion hotkey stuff #
###                ####
# 
# Please note the script does NOT check whether an existing potion has had any of its functions altered.
# The only thing it checks is whether the called entity.Kind is located in character's iventory.
# Try to stay true to it and use a new Kind if you are using custom potions, do not edit existing ones.
#
####

### PLAGUE: Todo - automatically parse how much health you have, what potions you have available and use the most appropriate one.

"""
def AutoPotHandler(EntityName):
    pass
    me=Bladex.GetEntity(EntityName)
    inv=me.GetInventory()
    
"""
USE_FROM_INV=0

def QuickPot(EntityName, PotionKind):
    FriendlyName=Reference.GetObjectFriendlyName(PotionKind)
    me = Bladex.GetEntity(EntityName)
    inv = me.GetInventory()
    
    if me.Wuea==Reference.WUEA_ENDED:
        return
        
    if me.Wuea==Reference.WUEA_WAIT:
        return

    if not inv.nObjects:
        Actions.ReportMsg ("I don't have a "+FriendlyName)
        return

    if me.AnimName=="Rlx" and me.AnmEndedFunc:
        me.AnmEndedFunc= None
        
    if me.AnmEndedFunc:
        return
    
    else:
        for i in range(inv.nObjects):
            potname = inv.GetObject(i)                                        ### BUG!!! If 2 more items are stacked in the same slot, the script dies because it seemingly returns a list rather than string?
            if not potname:
                Actions.ReportMsg ("I don't have a "+FriendlyName)
                break
            potentialpot = Bladex.GetEntity(potname)
            if potentialpot.Kind == PotionKind:
                #Actions.ForceUse(me.Name, potname)            
                me = Bladex.GetEntity(EntityName)
                object=Bladex.GetEntity(potname)
                if not object.UseFunc:
                    print "!ERROR! @ pocimac.QuickPot - " +ItemName+ " has no UseFunc"
                    return
                else:
                    me.Data.obj_used=object
                    try: object.Data.UsedBy = EntityName ; object.UseFunc(potname, USE_FROM_INV)
                    except: print "!ERROR! @ pocimac.QuickPot - " +ItemName+ " has no Data"
                        
                break
            elif i+1 >= inv.nObjects:
                Actions.ReportMsg ("I don't have a "+FriendlyName)