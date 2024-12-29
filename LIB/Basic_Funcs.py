##///
##||| BASIC_FUNCS.PY TITANIUM
##||| Change list:
##||| * Hits which deal no damage now do not cause wound zones to change.
##||| * Inventory should now remain consistently at 20 instead of reseting to 10 at load-game (# PLAGUE: Need to rework this entirely to move it to GameState).
##||| * Shield/parry reaction animations can now be cancelled by hurt animations if the previous anim is at least half-complete.
##||| * Stamina use/recharge is much smoother now. (# PLAGUE: might cause floating point rounding errors and allow attacks that shouldn't be possible.)
##||| * Limbs now always spawn - Thanks Sryml! ( PLAGUE: Might need to be reworked to retain full physics for as long as possible)
##||| * Combo text should now fade properly when something was already written.
##||| * Fixed "hurt jog" animation playing if not locked on enemy and using shield.
##\\\ 

#
#
# Basic funcions that are launch trough the code
# Both for the main player/s AND the Non Playing Characters !
#
#

import Bladex
import AuxTran
import Actions
import Blood
import Damage
import AniSound
import Reference
import pdb
import CharStats
import copy
import ItemTypes
import netgame
import whrandom
import MenuText
import AuxFuncs
import GenFX
import Auras
import ObjStore
import GameStateAux
import BInput
import InitDataField
import CombosFX

if netgame.GetNetState() != 0:
	import NetWeapon


new_combo_sound = Bladex.CreateSound('../../Sounds/sesgado-lava.wav', 'NewComboSound')
new_combo_sound.Volume=1.0
new_combo_sound.MinDistance=5000
new_combo_sound.MaxDistance=20000

"""
### Mutilation constants
RightFoot= 512
RightLeg= 256
LeftFoot= 128
LeftLeg= 64
RightHand= 32
RightArm= 16
LeftHand= 8
LeftArm= 4
Head= 2

RArm = RightArm | RightHand
LArm = LeftArm | LeftHand
RLeg = RightLeg | RightFoot
LLeg = LeftLeg | LeftFoot   
"""


# Useful general functions

############################  Energy Functions  ############################

RestoreEnergyTime= 1.0/40.0 # was /20 -LeadHead
EnergyMin= 14.0
#RestoreEnergyRateMin= 0.005*EnergyMin
#RestoreEnergyRateMin= 0.095*EnergyMin
#RestoreEnergyRateMax= 0.095*EnergyMin
RestoreEnergyRateMin= 0.005/2.0     # /2.0 for smoother energy restore
RestoreEnergyRateMax= 0.095/2.0     # with minimal calc difference.     -LeadHead

## PLAGUE: Maybe use EnergyTime = 1.0 / 60.0 ; RateMin = 1 / 600.0 ; RateMax =  0.95/ 60.0
##         just an idea, will get floating point errors anyway.

def RestoreEnergyFunc(EntityName):
	Bladex.AddScheduledFunc(Bladex.GetTime()+RestoreEnergyTime, RestoreEnergyFunc,(EntityName,),"PlayerRestoreEnergy")
	pj=Bladex.GetEntity(EntityName)
	if pj:
		if netgame.GetNetState()!=0:
			max_energy= NetWeapon.GetEnergy(pj)
		else:
			max_energy= CharStats.GetCharMaxEnergy(pj.Kind, pj.Level)

		prev_energy= pj.Energy
		if pj.InAttack:
			energy2lose= min (pj.Data.LoseEnergyRate*RestoreEnergyTime, pj.Data.Energy2Lose)
			pj.Energy= max(prev_energy-energy2lose, -max_energy*Reference.ENERGY_LOW_LEVEL)
			pj.Data.Energy2Lose= pj.Data.Energy2Lose-energy2lose
			if pj.Energy<=0.0 and pj.AnmPos>0.8:
				pj.Gof=0
				pj.Gob=0
				pj.Tl=0
				pj.Tr=0
				pj.InterruptCombat()
				pj.RaiseEvent("Interrupt")


##			if pj.Energy<=0.0 and not prev_energy<=0.0 and pj.AnimName!='Rlx_vt':
##				#pj.DoActionWI("Rlx_vt",  0, 0.65, 0.0)
##				pj.Gof=0
##				pj.Gob=0
##				pj.Tl=0
##				pj.Tr=0
##
##				pj.LaunchAnmType("Rlx_vt")

		else:
			if netgame.GetNetState()==0:
				energyF= pow(1.0-(pj.Level/(CharStats.GetMaxLevel()*1.0)), 2)
			else:
				try:
					energyF = pow(1.0-((pj.Data.NetLevel-1.0)/3.0), 2)
				except:
					energyF = 0.5

			RestoreEnergyRate= energyF*(RestoreEnergyRateMax-RestoreEnergyRateMin)+RestoreEnergyRateMin
			new_energy= max(min((prev_energy+RestoreEnergyRate*max_energy)-pj.Data.Energy2Lose, max_energy),-max_energy*Reference.ENERGY_LOW_LEVEL)


			pj.Energy= new_energy
			pj.Data.Energy2Lose= 0.0

##			if (new_energy/max_energy) > Reference.ENERGY_LOW_LEVEL and pj.AnimName=='Rlx_vt':
##				pj.InterruptCombat()
##				pj.Attack=0
##				pj.RaiseEvent("Recover")



############################                 ############################


# Define the base python person class
class PlayerPerson:

	ObjId=0
	NPC = 0
	Name = "Unnamed"
	DamageFactorNone  = -0.001
	DamageFactorLight = 0.1
	DamageFactorHeavy = 0.35
	TakeBleedingImpact= 0
	ThrownBy= None
	PowerPotion = 0
	FAttack = 1.0
	FDefense = 1.0
	AimPressed= 0
	stuff_onback_b4= 0
	toggle4t_clearback= 0
	LoseEnergyRate= 0.0
	Energy2Lose= 0.0
	last_frwdup=-1
	last_brwdup=-1
	armour_level=0
	armour_prot_factor=0
	Poisoned=0
	NoFXOnHit= 1
	Resistances=None
	ObjectsTaken= []
	LevelUpParticleData=[]
	Invincibility= 0
	LastDamageType=""
	inheritance = 0
	InventoryActive=0


	def __init__(self, me):

		# A T E N C I O N
		# Si poneis nuevos miembros en el __init__, ponerlos tambien en la definicion de la
		# clase.
		# Preguntarme a mi (Carlos) si no lo teneis claro.

		self.inheritance = 0
		self.InventoryActive = me.Name[0:6] != "Player"
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

		self.ObjectsTaken= []
		self.LevelUpParticleData=[]
		#_________________________________________#
		#  Record some personal data              #
		#_________________________________________#

		self.Name = me.Name

		#_________________________________________#
		# Set up the core functions               #
		#_________________________________________#
		me.DamageFunc = Damage.CalculateDamage
		me.AttackFunc= Damage.CalculateFatigue
		me.TakeFunc = self.TakeFunc
		me.ThrowFunc = self.ThrowFunc
		me.HitFunc = self.HitFunc
		me.ImDeadFunc = self.PCImDead
		me.NewComboFunc=self.StdNewCombo
		me.BigFallFunc=self.StdBigFall
		#me.ToggleCombatFunc=self.StdToggleCombat

		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
		if netgame.GetNetState()!=0:
			me.Energy= NetWeapon.GetEnergy(me)
		else:
			me.Energy= CharStats.GetCharMaxEnergy(me.Kind, me.Level)

		#_________________________________________#
		# Initialise core                         #
		#_________________________________________#
		me.AddAnmEventFunc("TakeArrow", Actions.TakeArrowEventHandler)
		me.AddAnmEventFunc("CheckRefireBow", Actions.CheckRefireBowEventHandler)

		me.AddAnmEventFunc("W2hToLeft", Actions.W2hToLeftHandler)
		me.AddAnmEventFunc("W2hToRight", Actions.W2hToRightHandler)
		me.AddAnmEventFunc("LaunchTrail", self.LaunchTrail)

		me.AddAnmEventFunc("Start_Weapon", Actions.Start_Weapon)
		me.AddAnmEventFunc("Stop_Weapon", Actions.Stop_Weapon)
		me.AddAnmEventFunc("Start_Trail", Actions.Start_Trail)
		me.AddAnmEventFunc("Stop_Trail", Actions.Stop_Trail)
		me.AddAnmEventFunc("GraspString", Actions.GraspString)
		me.AddAnmEventFunc("UnGraspString", Actions.UnGraspString)
		me.AddAnmEventFunc("Start_Weapon_Special", Actions.Start_Weapon_Special)
		me.AddAnmEventFunc("Stop_Weapon_Special", Actions.Stop_Weapon_Special)
		me.AddAnmEventFunc("ElevatorDeath", Actions.QuickDeath)

		if me.CharTypeExt in ("Kgt", "Bar", "Amz", "Dwf"):
			exec_string="CombosFX."+me.CharTypeExt+"CombosFX(me.Name)"
			print "asignando funciones a eventos para FX..."
			print exec_string
			exec(exec_string)

		me.MutilateFunc= self.MutilateFunc
		inv = me.GetInventory()
		inv.maxObjects = 20

		self.Resistances= copy.copy(CharStats.GetCharResistances(me.Kind))
		self.ResetSounds(self.Name)

		##### Energy Fuctions ####
		if self.Name[0:6] == "Player":
			self.LevelUpParticleData=[]
			for i in range(30):
				if i>25:
					traux=(30.0-i)/5.0 #va de 0 a 1
					aux=traux**0.5
				else:
					traux=i/25.0 #va de 1 a 0
					aux=traux**2.0
				r=255
				g=255
				b=255
				a=255.0*traux
				size=200.0*aux
				self.LevelUpParticleData.append(a)
				self.LevelUpParticleData.append(size)
				Bladex.SetParticleGVal("LevelUpParticle",i,r,g,b,a,size)
			Bladex.AddScheduledFunc(Bladex.GetTime()+RestoreEnergyTime, RestoreEnergyFunc,(self.Name,),"PlayerRestoreEnergy")


	def ResetSounds(self, EntityName):
		me=Bladex.GetEntity(EntityName)
		kind=me.Kind[:len(me.Kind)-2]
		if kind=="Barbarian":
			AniSound.AsignarSonidosBarbaro(EntityName)
		elif kind=="Knight":
			AniSound.AsignarSonidosCaballero(EntityName)
		elif kind=="Dwarf":
			AniSound.AsignarSonidosEnano(EntityName)
		elif kind=="Amazon":
			AniSound.AsignarSonidosAmazona(EntityName)

	def GetNewMembers(self):
		bases=self.__class__.__bases__
		new_members={}
		for i in bases:
			base_dict=i.__dict__
			for j in base_dict.keys():
				if type(base_dict[j])==types.IntType:
					new_members[j]=base_dict[j]


	def persistent_id(self):
		return self.ObjId

	def __save_core_funcs__(self):
		me = Bladex.GetEntity(self.Name)
		if not me:
			print "__save_core_funcs__() Warning: trying to save a non existent entity",self.Name
			return

		core_funcs = []
		j = 0

		funcs =[("DamageFunc",            Damage.CalculateDamage),
				("AttackFunc",            Damage.CalculateFatigue),
				("TakeFunc",              self.TakeFunc),
				("ThrowFunc",             self.ThrowFunc),
				("HitFunc",               self.HitFunc),
				("NewComboFunc",          self.StdNewCombo),
				("BigFallFunc",           self.StdBigFall)]

		for i in funcs:
			exec('f = me.'+i[0])
			if (i[1] <> f):
				print "Save Core Func para",me.Name," callback ",i[0]," funcion ", f
				core_funcs.append((j,GameStateAux.SaveFunctionAux(f)))
			j = j + 1

		if (self.inheritance <> 1):
			funcs2=["SeeFunc",
				    "HearFunc",
				    "DelayNoSeenFunc",
				    "NoAllowedAreaFunc",
				    "EnemyNoAllowedAreaFunc",
				    "ImHurtFunc",
				    "EnemyDeadFunc",
				    "AnmEndedFunc",
				    "EnterCloseFunc",
				    "EnterLargeFunc",
				    "EnterPrimaryAAFunc",
				    "EnterSecondaryAAFunc",
				    "CharSeeingEnemyFunc",
				    "ToggleCombatFunc"]

			for i in funcs2:
				exec('f = me.'+i)
				if (f <> None):
					print "Save Core Func para",me.Name," callback ",i," funcion ", f
					core_funcs.append((j,GameStateAux.SaveFunctionAux(f)))
				j = j + 1

			if me.ImDeadFunc <> self.PCImDead:
				core_funcs.append((j,GameStateAux.SaveFunctionAux(f)))


		return(core_funcs)

	def __load_core_funcs__(self,param):
		me = Bladex.GetEntity(self.Name)
		if not me:
			print "__load_core_funcs__ -> Warning, trying to get a non existent entity",self.Name
			return

		funcs=[ "DamageFunc",
				"AttackFunc",
				"TakeFunc",
				"ThrowFunc",
				"HitFunc",
				"NewComboFunc",
				"BigFallFunc",
				"SeeFunc",
				"HearFunc",
				"DelayNoSeenFunc",
				"NoAllowedAreaFunc",
				"EnemyNoAllowedAreaFunc",
				"ImHurtFunc",
				"EnemyDeadFunc",
				"AnmEndedFunc",
				"EnterCloseFunc",
				"EnterLargeFunc",
				"EnterPrimaryAAFunc",
				"EnterSecondaryAAFunc",
				"CharSeeingEnemyFunc",
				"ToggleCombatFunc",
				"ImDeadFunc"]

		for i in param:
			# print "Load Core Func ",i[1]," para ",me.Name," funcion ",funcs[i[0]]
			try:
				GameStateAux.LoadFunctionAux(i[1],me,funcs[i[0]])
				# print "Loaded for entity"
			except:
				GameStateAux.LoadFunctionAux(i[1],self,funcs[i[0]])
				exec("me.%s=self.%s"%(funcs[i[0]],funcs[i[0]]))

	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase

		return (1,{"PlayerPerson":(self.ObjId,
								   self.NPC,
								   self.Name,
								   self.DamageFactorNone,
								   self.DamageFactorLight,
								   self.DamageFactorHeavy,
								   self.TakeBleedingImpact,
								   self.ThrownBy,
								   self.PowerPotion,
								   self.FAttack,
								   self.FDefense,
								   self.AimPressed,
								   self.stuff_onback_b4,
								   self.toggle4t_clearback,
								   self.last_frwdup,
								   self.last_brwdup,
								   self.LoseEnergyRate,
								   self.Energy2Lose,
								   self.Resistances,
								   self.armour_level,
								   self.armour_prot_factor,
								   self.Poisoned,
								   self.ObjectsTaken,
								   self.Invincibility,
								   self.LastDamageType,
								   GameStateAux.SaveNewMembers(self),
								   PlayerPerson.__save_core_funcs__(self))
					}
				)

	def persistent_check(self):
		me=Bladex.GetEntity(self.Name)
		if not me:
			return 0
		return 1

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		version=parm[0]


		if version==1:
			parms=parm[1]["PlayerPerson"]
			self.ObjId=parms[0]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.NPC=parms[1]
			self.Name=parms[2]
			me=Bladex.GetEntity(self.Name)
			self.InventoryActive = me.Name[0:6] != "Player"
			me.GetInventory().maxObjects = 20                   # Added - LeadHead

			#_________________________________________#
			# Set up the core functions               #
			#_________________________________________#
			me.DamageFunc = Damage.CalculateDamage
			me.TakeFunc = self.TakeFunc
			me.ThrowFunc = self.ThrowFunc
			me.HitFunc = self.HitFunc
			me.ImDeadFunc = self.PCImDead
			me.NewComboFunc=self.StdNewCombo
			me.BigFallFunc=self.StdBigFall
			me.AttackFunc= Damage.CalculateFatigue

			self.DamageFactorNone=parms[3]
			self.DamageFactorLight=parms[4]
			self.DamageFactorHeavy=parms[5]
			self.TakeBleedingImpact=parms[6]
			self.ThrownBy=parms[7]
			self.PowerPotion=parms[8]
			self.FAttack=parms[9]
			self.FDefense=parms[10]
			self.AimPressed=parms[11]
			self.stuff_onback_b4=parms[12]
			self.toggle4t_clearback=parms[13]
			self.last_frwdup=parms[14]
			self.last_brwdup=parms[15]
			self.LoseEnergyRate=parms[16]
			self.Energy2Lose=parms[17]
			self.Resistances=parms[18]
			self.armour_level=parms[19]
			self.armour_prot_factor=parms[20]
			self.Poisoned=parms[21]
			self.ObjectsTaken=parms[22]
			self.Invincibility=parms[23]
			self.LastDamageType=parms[24]
			GameStateAux.LoadNewMembers(self,parms[25])
			PlayerPerson.__load_core_funcs__(self,parms[26])

		else:
			print "ERROR, Incorrect version"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self

		self.inheritance = 0


		if self.Name[0:6] == "Player":
			self.LevelUpParticleData=[]
			for i in range(30):
				if i>25:
					traux=(30.0-i)/5.0 #va de 0 a 1
					aux=traux**0.5
				else:
					traux=i/25.0 #va de 1 a 0
					aux=traux**2.0
				r=255
				g=255
				b=255
				a=255.0*traux
				size=200.0*aux
				self.LevelUpParticleData.append(a)
				self.LevelUpParticleData.append(size)
				Bladex.SetParticleGVal("LevelUpParticle",i,r,g,b,a,size)
			Bladex.AddScheduledFunc(Bladex.GetTime()+RestoreEnergyTime, RestoreEnergyFunc,(self.Name,),"PlayerRestoreEnergy")

		me=Bladex.GetEntity(self.Name)
		if not me:
			print "PlayerPerson.__setstate__() Warning, can not get entity", self.Name
			return

		#_________________________________________#
		# Initialise core                         #
		#_________________________________________#
		me.AddAnmEventFunc("TakeArrow", Actions.TakeArrowEventHandler)
		me.AddAnmEventFunc("CheckRefireBow", Actions.CheckRefireBowEventHandler)

		me.AddAnmEventFunc("W2hToLeft", Actions.W2hToLeftHandler)
		me.AddAnmEventFunc("W2hToRight", Actions.W2hToRightHandler)
		me.AddAnmEventFunc("LaunchTrail", self.LaunchTrail)
		me.AddAnmEventFunc("Start_Weapon", Actions.Start_Weapon)
		me.AddAnmEventFunc("Stop_Weapon", Actions.Stop_Weapon)
		me.AddAnmEventFunc("Start_Trail", Actions.Start_Trail)
		me.AddAnmEventFunc("Stop_Trail", Actions.Stop_Trail)
		me.AddAnmEventFunc("Start_Weapon_Special", Actions.Start_Weapon_Special)
		me.AddAnmEventFunc("Stop_Weapon_Special", Actions.Stop_Weapon_Special)
		me.AddAnmEventFunc("ElevatorDeath", Actions.QuickDeath)

		if me.CharTypeExt in ("Kgt", "Bar", "Amz", "Dwf"):
			exec_string="CombosFX."+me.CharTypeExt+"CombosFX(me.Name)"
			exec(exec_string)

		me.MutilateFunc= self.MutilateFunc

		self.NoFXOnHit= 1
		self.ResetSounds(self.Name)

	#_________________________________________#
	# Define our functions                    #
	#_________________________________________#
	def MutilateFunc(self,EntityName,obj_name,x,y,z,nx,ny,nz,node):

		
		# print EntityName+": MutilateFunc"
		me = Bladex.GetEntity(EntityName)
		limb = Bladex.GetEntity(obj_name)
		
		""" ## For now disabled this code. It sort of works, but has various inconsistencies across enemy Kinds
		# global LArm
		# global RArm
		# global LLeg
		# global RLeg
		
		mut = me.MutilationsMask
		
		isGrork = 0
		if me.MeshName == "Great_Ork":
			isGrork = 1
			RArm = Head | RightArm | RightHand
			

		
		### Remove duplicated limbs from world.
		noMutil = 0
		if (node == me.GetNodeIndex("L_Hand") or node == me.GetNodeIndex("L_Forearm") or node == me.GetNodeIndex("L_Elbow") or node == me.GetNodeIndex("L_Wrist")) and (mut & LArm):
			noMutil = 1
		elif isGrork:
			if (node == me.GetNodeIndex("R_Hand") or node == me.GetNodeIndex("R_Forearm") or node == me.GetNodeIndex("R_Elbow") or node == me.GetNodeIndex("R_Wrist") or node == me.GetNodeIndex("R_Shoulder") or node == me.GetNodeIndex("R_Arm"))	and (mut & RArm):
				noMutil = 1
		elif (node == me.GetNodeIndex("R_Hand") or node == me.GetNodeIndex("R_Forearm") or node == me.GetNodeIndex("R_Elbow") or node == me.GetNodeIndex("R_Wrist")) and (mut & RArm):
			noMutil = 1
		elif (node == me.GetNodeIndex("L_Boot") or node == me.GetNodeIndex("L_Knee") or node == me.GetNodeIndex("L_Foot")) and (mut & LLeg):
			noMutil = 1
		elif (node == me.GetNodeIndex("R_Boot") or node == me.GetNodeIndex("R_Knee") or node == me.GetNodeIndex("R_Foot")) and (mut & RLeg):
			noMutil = 1
		if noMutil:
			print "mutilation for " +EntityName+ " blocked"
			limb.SubscribeToList("Pin")
			return
		"""
		
		limb.ExclusionGroup=1337 					 	 # Added
		if limb.TestHit:                                 #
			limb.ExclusionGroup=1                        # 
			limb.Move(0, -160, 0)                        # Fixes disappearing limbs
			limb.PutToWorld()                            # PLAGUE: Needs further work to look better.
			limb.Impulse(0,0,0)                          #    -LeadHead
			
		if me and me.Kind[0:7]!="Skeleton":		# This check makes no sense, since the skeletons override this func anyway.
			Blood.Mutilate (EntityName,obj_name,x,y,z,nx,ny,nz,node)

		if me.Kind=="Golem_lava":
			return

		if me.Kind=="Minotaur" and node!=Reference.BODY_HEAD:		# This check also makes no sense, it is trying to compare skeletonnode to damagezone
			return
		
		InitDataField.Initialise(limb)
		limb.Data.NoFXOnHit= 1
		# print limb.Mass, node
		if limb.Mass > 1.5 and limb.Mass < 7.0:
			Reference.EntitiesSelectionData[obj_name]= Reference.DefaultSelectionData["Limb"]
			Reference.EntitiesObjectData[obj_name]= Reference.DefaultObjectData['Limb']

	def TakeFunc (self, MyName):
		Actions.StdUse (MyName)

	def ThrowFunc (self, MyName):
		Actions.StdThrowObject (MyName)

	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz, WeaponCx, WeaponCy, WeaponCz,WeaponDx, WeaponDy, WeaponDz):
		if self.TakeBleedingImpact:
			Blood.BleedingImpact(Bladex.GetEntity(EntityName), Cx, Cy, Cz, Px, Py, Pz,Bladex.GetEntity(WeaponName),WeaponCx, WeaponCy, WeaponCz,WeaponDx, WeaponDy, WeaponDz)
			self.TakeBleedingImpact= 0
			#print "BloodImpact"
		#else:
			#print "NoBloodImpact"

	def ReSpawn (self, EntityName):
		print "Respawn Func"
		me = Bladex.GetEntity(EntityName)

		right= me.InvRight
		left= me.InvLeft
		rightback= me.InvRightBack
		leftback= me.InvLeftBack

		self.UnlinkAll (EntityName, "")  # Dettatch arrows

		inv= me.GetInventory()
		# Right Back
		if rightback:
			inv.LinkRightHand (rightback)
			inv.LinkBack(rightback)
		# Left Back
		if leftback:
			inv.LinkLeftHand (leftback)
			inv.LinkBack(leftback)
		# Right hand
		if right:
			inv.LinkRightHand (right)
		# Left hand
		if left:
			inv.LinkLeftHand (left)

		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)

		if netgame.GetNetState()!=0:
			me.Energy= NetWeapon.GetEnergy(me)
		else:
			me.Energy= CharStats.GetCharMaxEnergy(me.Kind, me.Level)
		me.ResetWounds()

		if self.Poisoned:
			self.UnVenom ()

		# Link camera
		if(netgame.GetNetState()==0):
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, self.RelinkCamera,(),"RelinkCamera")
		angle= me.Angle
		me.Orientation= (0.0, 3.62407746479e-007, 0.707107365131, -0.707106947899)
		me.Angle= angle

	def RelinkCamera(self):
		cam=Bladex.GetEntity("Camera")
		cam.SetPersonView("Player1")
    
    ## PLAGUE: Below function does effectively nothing. Only the orc death anims have this event.
	def UnlinkAll (self, EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		# Usually done on the last frame of a death animation
		if me:
			# should also remove objects from inventory slots, hands, and give impulse
			me.UnlinkChildren()

	def GetResistance(self, DamageType):
		if self.Resistances.has_key(DamageType): resistance= self.Resistances[DamageType]
		else: resistance= 0.0
		resistance= min(resistance,1.0)

		# Do we have any items that offer protections aginst this damage
		me=Bladex.GetEntity(self.Name)
		if me:
			inv= me.GetInventory()
			for i in range (inv.nKindObjects):
				obj_name= inv.GetObject(i)
				object= Bladex.GetEntity(obj_name)
				try:
					if object.Data:
						if object.Data.Resistances:
							if object.Data.Resistances.has_key(DamageType):
								# Adding 0.5 to 0.5 gives 0.75 !!!
								extra_resistance= object.Data.Resistances[DamageType]*(1.0-resistance)
								resistance= resistance+extra_resistance
								resistance= min(resistance,1.0)
				except AttributeError: pass
		return resistance


	def UnVenom (self):
		self.Poisoned= 0

	def ReVenom (self, EntityName, VenomStrength, TimeRemaining, Frequency, Poisoner):
		if self.Poisoned:

			if BInput.GetInputManager().GetInputActionsSet()!= "Default":
				Bladex.AddScheduledFunc(Bladex.GetTime()+Frequency, self.ReVenom,(EntityName,VenomStrength, TimeRemaining, Frequency, Poisoner),self.Name+"ReVenom")
			else:
				isServer = netgame.GetNetState()==1
				NextTimeRemaining= TimeRemaining-Frequency

				me= Bladex.GetEntity(EntityName)
				if me and me.Life>0:
					special_resistance= self.GetResistance('Venom')
					if special_resistance < 1.0:
						if NextTimeRemaining>0.0:
							Bladex.AddScheduledFunc(Bladex.GetTime()+Frequency, self.ReVenom,(EntityName,VenomStrength, NextTimeRemaining, Frequency, Poisoner),self.Name+"ReVenom")
						else:

							VenomStrength= VenomStrength*(TimeRemaining/Frequency)

							# remove this poison source
							self.Poisoned= self.Poisoned-1
							if not self.Poisoned:
								self.UnVenom ()

						current_venom_damage= VenomStrength-(VenomStrength*special_resistance)
						me.Life= me.Life- current_venom_damage
						if me.Life<=0:
							if isServer: # Net -> Server
								Damage.PlayerHitFunc(me.Name,Poisoner, me.Life, 1)
								self.UnVenom ()

							enemy= Bladex.GetEntity(Poisoner)
							if enemy:
								try: enemy.Data.OnKilledEnemy(EntityName)
								except: pass
					else:
						self.UnVenom ()

	def EnVenom (self, EntityName, VenomStrength, Poisoner):
		me= Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			# Are we immune to poison?
			special_resistance= self.GetResistance('Venom')
			if special_resistance < 1.0:
				time=Bladex.GetTime()
				if not self.Poisoned:
					# Set message on the health bar if we are "Player1"
					# visual effect (green flash)
					aura= Auras.MakeAura (EntityName,0.7,   (55,0.1,1.0,1,0,0), (),(),(2,  0.0,0.35,0.0, 0.2, 0.0  , 0.0,0.35,0.0, 0.1, 1.0))
					aura.Data.AddEvent(time+0.2,           (45,1.0,1.0,1,0,0), (),(),(2,  0.0,0.35,0.0, 0.2, 0.0  , 0.0,0.35,0.0, 0.1, 1.0))
					aura.Data.AddEvent(time+0.7,           (5,0.1,1.0,1,0,0),  (),(),(2,  0.0,0.35,0.0, 0.2, 0.0  , 0.0,0.35,0.0, 0.1, 1.0))

				# Add another poison source
				self.Poisoned= self.Poisoned+1
				# add a scheduled function to suffer poison damage
				VenomTime= 60.0
				Frequency= 5.0
				Bladex.AddScheduledFunc(time+Frequency, self.ReVenom,(EntityName,VenomStrength, VenomTime, Frequency, Poisoner),self.Name+"ReVenom")


	def LaunchTrail (self, EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me and me.InvRight:
			x, y, z= me.Rel2AbsPoint(1000.0, 0.0, 0.0)
			trail= ItemTypes.MakeHalfmoonTrail (EntityName+"Trail", x,y,z,EntityName)
			trail.Data.ThrowReleaseEventHandler (EntityName,"")

	def FreezeAnmEnd(self,EntityName):
		Bladex.GetEntity(EntityName).Freeze()

	def PCImDead (self, EntityName):
		me = Bladex.GetEntity(EntityName)
		me.AddAnmEventFunc("UnlinkAll", self.UnlinkAll)

		already_death=0
		Damage.DropInvalidObjectsOnImpact(EntityName)
		anim_name=me.AnimName
		Bladex.PlayHaptic(3)
		if (anim_name[0]=="D" or anim_name[0]=="d") and (anim_name[1]=="T" or anim_name[1]=="t") and (anim_name[2]=="H" or anim_name[2]=="h"):
			already_death=1
			#print "Already death!"

		if already_death==0:
			death_anim="dth0"
			if me.MutilationsMask==2:					# PLAGUE: Should be a bitwise operation just to be safe
				dth_prob=whrandom.uniform(0.0, 1.0)
				if (dth_prob<0.142):
					death_anim="dth_c1"
				elif (dth_prob<0.286):
					death_anim="dth_c2"
				elif (dth_prob<0.428):
					death_anim="dth_c3"
				elif (dth_prob<0.571):
					death_anim="dth_c4"
				elif (dth_prob<0.714):
					death_anim="dth_c5"
				elif (dth_prob<0.857):
					death_anim="dth_c6"
				else:
					death_anim="dth_c7"
			else:
				dth_prob=whrandom.uniform(0.0, 1.0)
				#if self.LastDamageType=="Fire":
				#	death_anim="dth_burn"
				#el
				if (dth_prob<0.142):
					death_anim="dth_n00"
				elif (dth_prob<0.286):
					death_anim="dth_n01"
				elif (dth_prob<0.428):
					death_anim="dth_n02"
				elif (dth_prob<0.571):
					death_anim="dth_n03"
				elif (dth_prob<0.714):
					death_anim="dth_n04"
				elif (dth_prob<0.857):
					death_anim="dth_n05"
				else:
					death_anim="dth_n06"

			me.Wuea=Reference.WUEA_ENDED
			launch_new=1
			#print "Dth_Anim " + death_anim + " has Rsteps " + str(Bladex.AnmTypeRSteps(EntityName,death_anim)) + " and Lsteps " +str(Bladex.AnmTypeLSteps(EntityName,death_anim))
			# PLAGUE: This is terrible and needs to be re-written from scratch. 
			#         First, it should use bitwise operators. Second, steps are not a reliable method.
			if (me.MutilationsMask==512 or me.MutilationsMask==256) and Bladex.AnmTypeRSteps(EntityName,death_anim)>1:
				#print "No dth due to not having right leg!"
				launch_new=0
			elif (me.MutilationsMask==128 or me.MutilationsMask==64) and Bladex.AnmTypeLSteps(EntityName,death_anim)>1:
				#print "No dth due to not having left leg!"
				launch_new=0

			if launch_new==1:
				me.LaunchAnmType(death_anim)

			if me.AnimName<>death_anim:
				me.LaunchAnmType("dth0")
				if me.AnimName<>"dth0":
					#pdb.set_trace()
					print "BUG? -> Basdic_Funcs.py ,def PCImDead"

		if self.NPC:
			return





		#  Following only to be applied to dying PLAYER characters

		# unlink the camera
		cam=Bladex.GetEntity("Camera")
		if EntityName==cam.ETarget:
			cam.SType=0
			cam.TType=2
			cam.ETarget='Player1'



		#Do NOT respawn in demo_mode
		if netgame.GetNetState()==0:
			if Reference.DEMO_MODE==0:
				if (not self.NPC): # "and 0" by Dario (don't killme please)
					if Reference.PYTHON_DEBUG >= 2:
						if me.Wuea==Reference.WUEA_ENDED:
							print "Respawning now!, no death anim"
							self.ReSpawn(EntityName)
						else:
							#print "Respawning after anim ends"
							me.AnmEndedFunc= self.ReSpawn
					else:
						import SaveGame

						# DROP WEAPONS
						try:
							object = Bladex.GetEntity(me.InvLeft)
							if me.InvLeft and object and not object.TestHit:
								Actions.RemoveFromInventory (me, object,"DropLeftEvent")
								object.ExclusionGroup=1337  ## Added -LeadHead
								object.Impulse(0.0, 0.0, 0.0)
						except AttributeError:
							pass

						try:
							object = Bladex.GetEntity(me.InvRight)
							if me.InvRight and object and not object.TestHit:
								Actions.RemoveFromInventory (me, object,"DropRightEvent")
								object.ExclusionGroup=1337  ## Added -LeadHead
								object.Impulse(0.0, 0.0, 0.0)
						except AttributeError:
							pass

						# Call the Load Menu
						if me.Wuea==Reference.WUEA_ENDED:
							print "no death anim... So Fade an go!"
							SaveGame.MenuStart(EntityName)
						else:
							#print "after anim ends the menu will be true.."
							me.AnmEndedFunc= SaveGame.MenuStart
			else:
				if not self.NPC: # "and 0" by Dario (don't killme please)
					Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, Bladex.LoadLevel,(Bladex.GetCurrentMap(),),"ReloadAfterDeath")
		else:
			# DROP WEAPONS
			try:
				object = Bladex.GetEntity(me.InvLeft)
				if me.InvLeft and object and not object.TestHit:
					Actions.RemoveFromInventory (me, object,"DropLeftEvent")
					object.Impulse(0.0, 0.0, 0.0)
			except AttributeError:
				pass

			try:
				object = Bladex.GetEntity(me.InvRight)
				if me.InvRight and object and not object.TestHit:
					Actions.RemoveFromInventory (me, object,"DropRightEvent")
					object.Impulse(0.0, 0.0, 0.0)
			except AttributeError:
				pass

		# Bugfix, when character dies, an optimisation in the Chase()
		# thinks the character can never be reached in this sector.  ResetChase() causes refresh
		if not already_death:
			nents= Bladex.nEntities()
			for i in range(nents):
				ent= Bladex.GetEntity(i)
				if (ent.Person):
					if ent.Life>0:
						if ent.GetEnemyName()==EntityName:
							ent.ResetChase()

	def OnKilledEnemy(self,KilledEntityName):
		Reference.debugprint("OnKilledEnemy")
		KilledEntity=Bladex.GetEntity(KilledEntityName)
		if KilledEntity is None:
			print "OnKilledEnemy(): Error: None Entity"
			return
		me=Bladex.GetEntity(self.Name)
		#import CharStats # Necesario para la recarga de partida. �Paron?
		
		me.PartialLevel=me.PartialLevel+CharStats.GetCharExperienceReward(KilledEntity.CharType,KilledEntity.Level)

		LevelLimit=CharStats.GetCharExperienceCost(me.CharType,me.Level)

		if self.Name=="Player1":  #REVISAR
			inv=me.GetInventory()
			if inv:
				weapon_name=inv.GetActiveWeapon()
				if weapon_name is not None:
					weapon= Bladex.GetEntity(weapon_name)
					kind = weapon.Kind
					Reference.debugprint("Player's active weapon: " + weapon_name)
					Reference.debugprint("Player's weapon kind: " + kind)
					if kind[:4]=="Limb":
						Bladex.TriggerEvent(54)
			import Scorer
			# Ahora compruebo si sube de nivel
			if me.PartialLevel>=LevelLimit:
				while me.PartialLevel>=LevelLimit:
					me.PartialLevel=me.PartialLevel-LevelLimit
					me.Level=me.Level+1
					LevelLimit=CharStats.GetCharExperienceCost(me.CharType,me.Level)
				Scorer.LevelUp()
				Scorer.SetLevelLimits(0,CharStats.GetCharExperienceCost(me.CharType,me.Level))
				maxlevel=CharStats.GetMaxLevel()
				maxsize=50+(140/maxlevel)*me.Level # 50->190
				maxPPS=120+(600/maxlevel)*me.Level # 120->720
				maxint=0.5+(4.5/maxlevel)*me.Level # 0.5->5.0
				AuraParams=(5, 0, 1, 0, 0, 1)
				AuraGradient=(2, 0.4, 0.6, 1.0, 0.5, 0.0, 0.1, 0.2, 1.0, 0.0, 0.8)
				AuraVar1Args=(5, maxsize, 0, 1, 0.5)
				AuraVar2Args=(maxsize, 5, 1, 0, 1.0)
				PSParams=(self.LevelUpParticleData, "LevelUpParticle", 30, 50, 150, 255, maxPPS, -600, 0.0, 2, 2, 0.4, 30, 0.5)
				GenFX.LevelUpFX("Player1", 1, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args, PSParams, maxint, "Timer15", 15, "../../Sounds/aparicion-escudo.wav")

				# Restore state of the player.
				if me.Life >0: # If an enemy death by poison or trowed weapons and.. You are death!
					me.ResetWounds()
					me.Life = CharStats.GetCharMaxLife(me.Kind, me.Level)

				Scorer.SlideTBS(0)
				Scorer.LevelUpFlash()

			if netgame.GetNetState() == 0:
				Scorer.SetLevelBarValue(me.PartialLevel)

		# else:
			# Ahora compruebo si sube de nivel
			# if me.PartialLevel>LevelLimit:
				# me.PartialLevel=me.PartialLevel-LevelLimit
				# me.Level=me.Level+1



	# Launch animations in response to being hit.  Called internally in Python from the damage func
	# These animations are for a standard human skeleton.  Replace this func for other race types.
	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		me = Bladex.GetEntity(EntityName)
		


		weapon_flag=Reference.W_FLAG_1H
		if me.InvRight:
			weapon_flag=Reference.GiveWeaponFlag(me.InvRight)

		if DamagePoints<=0 and Shielded and me.GetInventory().GetMagicShield():
			return
			
		""" ### "armoured" attacks like you'd see in fighters. The code works and is fine, but currently disabled until I decide whether I want it to work.
			### the visual effect is a placeholder -LeadHead
		armouredAttacks = ["Bar_g2h_earthpow", "Bar_g2h_b6kata"]
		if me.AnimFullName in armouredAttacks:
			time=Bladex.GetTime()
			shine = Auras.MakeAura(EntityName,0.8,   (1  , 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.6, 0.0, 0.6, 0.2  ,  0.8, 0.1, 0.0, 0.0, 0.8))
			shine.Data.AddEvent(time+0.15,         (100, 1.0 , 1.0, 0, 0, 1), (), (), (2,  0.8, 0.6, 0.0, 0.6, 0.2  ,  0.8, 0.1, 0.0, 0.0, 0.8))
			shine.Data.AddEvent(time+0.8,          (160, 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.1, 0.0, 0.6, 0.2  ,  0.8, 0.0, 0.0, 0.0, 0.8))
			return
		"""
		if me and me.Life > 0:
			damage_factor = DamagePoints / (me.Life+DamagePoints)

			if damage_factor > me.Data.DamageFactorNone:
				if DamageZone >= 0 and DamageZone < 32 and DamagePoints>1:       #Added check for damagepoints>1 -LeadHead:
					me.SetWoundedZone(DamageZone, 1)

				do_not_abort=0
				# Now checks if the animation has basically already ended. Makes parrying much more viable and having your shield broken more deadly. -LeadHead
				if (me.AnimName == "df_s_broken" and me.AnmPos<0.55) or (me.AnimName == "sword_broken" and me.AnmPos<0.55) or (me.AnimName == "sw_react" and me.AnmPos<0.55) or self.Invincibility==2:
					do_not_abort=1
				if do_not_abort==0:

					Damage.DropInvalidObjectsOnImpact (EntityName)
					me.Wuea=Reference.WUEA_ENDED

					if me.InCombat:
						me.InterruptCombat()
						if Shielded:
							# Launch Blocking damage animations
							if damage_factor <= (me.Data.DamageFactorLight+me.Data.DamageFactorHeavy) / 2.0:
								Reference.debugprint("Launching .df_01")
								if weapon_flag==Reference.W_FLAG_2W:
									me.LaunchAnmType("df_01_2w")
								elif weapon_flag==Reference.W_FLAG_AXE:
									me.LaunchAnmType("df_01_axe")
								elif weapon_flag==Reference.W_FLAG_SP:
									me.LaunchAnmType("df_01_spear")
								else:
									me.LaunchAnmType("df_01")
							else:
								Reference.debugprint("Launching .df_02")
								if weapon_flag==Reference.W_FLAG_2W:
									me.LaunchAnmType("df_02_2w")
								elif weapon_flag==Reference.W_FLAG_AXE:
									me.LaunchAnmType("df_02_axe")
								elif weapon_flag==Reference.W_FLAG_SP:
									me.LaunchAnmType("df_02_spear")
								else:
									me.LaunchAnmType("df_02")
						else:
							if damage_factor <= me.Data.DamageFactorLight:
								Reference.debugprint("Launching .hurt_f_lite")
								me.LaunchAnmType("hurt_f_lite")
							elif damage_factor >= me.Data.DamageFactorHeavy:
								Reference.debugprint("Launching .hurt_f_big")
								me.LaunchAnmType("hurt_f_big")
							elif DamageZone==Reference.BODY_HEAD:
								Reference.debugprint("Launching .hurt_f_head")
								me.LaunchAnmType("hurt_f_head")
							elif DamageZone==Reference.BODY_FRONT:
								Reference.debugprint("Launching .hurt_f_breast")
								me.LaunchAnmType("hurt_f_breast")
							elif DamageZone==Reference.BODY_BACK:
								Reference.debugprint("Launching .hurt_f_back")
								me.LaunchAnmType("hurt_f_back")
							elif DamageZone==Reference.BODY_RARM or DamageZone==Reference.BODY_RHAND:
								Reference.debugprint("Launching .hurt_f_r_arm")
								me.LaunchAnmType("hurt_f_r_arm")
							elif DamageZone==Reference.BODY_LARM or DamageZone==Reference.BODY_LHAND:
								Reference.debugprint("Launching .hurt_f_l_arm")
								me.LaunchAnmType("hurt_f_l_arm")
							elif DamageZone==Reference.BODY_RLEG or DamageZone==Reference.BODY_RFOOT:
								Reference.debugprint("Launching .hurt_f_r_leg")
								me.LaunchAnmType("hurt_f_r_leg")
							elif DamageZone==Reference.BODY_LLEG or DamageZone==Reference.BODY_LFOOT:
								Reference.debugprint("Launching .hurt_f_l_leg")
								me.LaunchAnmType("hurt_f_l_leg")
					else:
						if me.Run and not Shielded:		# Added "and not Shielded"	-LeadHead
							Reference.debugprint("Launching .hurt_jog")
							me.LaunchAnmType("hurt_jog")
						else:
							if Shielded:
								# Launch Blocking damage animations
								if damage_factor <= (me.Data.DamageFactorLight+me.Data.DamageFactorHeavy) / 2.0:
									Reference.debugprint("Launching .df_01")
									if weapon_flag==Reference.W_FLAG_2W:
										me.LaunchAnmType("df_01_2w")
									elif weapon_flag==Reference.W_FLAG_AXE:
										me.LaunchAnmType("df_01_axe")
									elif weapon_flag==Reference.W_FLAG_SP:
										me.LaunchAnmType("df_01_spear")
									else:
										me.LaunchAnmType("df_01")
								else:
									Reference.debugprint("Launching .df_02")
									if weapon_flag==Reference.W_FLAG_2W:
										me.LaunchAnmType("df_02_2w")
									elif weapon_flag==Reference.W_FLAG_AXE:
										me.LaunchAnmType("df_02_axe")
									elif weapon_flag==Reference.W_FLAG_SP:
										me.LaunchAnmType("df_02_spear")
									else:
										me.LaunchAnmType("df_02")
							elif DamageZone==Reference.BODY_HEAD:
								Reference.debugprint("Launching .hurt_head")
								me.LaunchAnmType("hurt_head")
							elif DamageZone==Reference.BODY_FRONT:
								Reference.debugprint("Launching .hurt_breast")
								me.LaunchAnmType("hurt_breast")
							elif DamageZone==Reference.BODY_BACK:
								Reference.debugprint("Launching .hurt_back")
								me.LaunchAnmType("hurt_back")
							elif DamageZone==Reference.BODY_RARM or DamageZone==Reference.BODY_RHAND:
								Reference.debugprint("Launching .hurt_r_arm")
								me.LaunchAnmType("hurt_r_arm")
							elif DamageZone==Reference.BODY_LARM or DamageZone==Reference.BODY_LHAND:
								Reference.debugprint("Launching .hurt_l_arm")
								me.LaunchAnmType("hurt_l_arm")
							elif DamageZone==Reference.BODY_RLEG or DamageZone==Reference.BODY_RFOOT:
								Reference.debugprint("Launching .hurt_r_leg")
								me.LaunchAnmType("hurt_r_leg")
							elif DamageZone==Reference.BODY_LLEG or DamageZone==Reference.BODY_LFOOT:
								Reference.debugprint("Launching .hurt_l_leg")
								me.LaunchAnmType("hurt_l_leg")
							else:
								# Shouldn't get here
								#pdb.set_trace()
								pass


	#
	# Standatd function for printing ...
	#
	def StdNewCombo(self,EntityName,ComboName):
		if netgame.GetNetState() == 0:
			import GameText

			me = Bladex.GetEntity(EntityName)
			if EntityName<>"Player1":
				return

			ComboTXT = GameText.GetComboName(EntityName,ComboName)
			if ComboTXT:
				Actions.ReportMsg(("New Attack")+": "+ ComboTXT)	# Changed to ReportMsg 	-LeadHead

				new_combo_sound.Stop()
				new_combo_sound.PlayStereo()



	def StdBigFall(self,EntityName,Dist):
		me = Bladex.GetEntity(EntityName)
		chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

		if Dist>=chartype.DieFall:
			print "About to die due to DieFall in Basic_Funcs.StdBigFall"
			me.Life=0
			me.LaunchAnmType("Dth_Fll2")
			return

			return
		if Dist<5000:
			return

		diff=(Dist-5000.0)*0.001
		fall_damage=((Dist-5000.0)/(chartype.DieFall-5000))*70.0

		me.Life=me.Life-fall_damage
		if netgame.GetNetState()==1: # juego de red -> servidor
			if me.Life <=0:
				Damage.PlayerHitFunc(me.Name,"Fall", me.Life, me.Life+fall_damage)


	#def StdToggleCombat(self,EntityName):
	#	import DMusic
	#	#print "Hola! Toggle Combat"
	#	me = Bladex.GetEntity(EntityName)
	#	if self.NPC==1:
	#		DMusic.notifyCombat(EntityName)

	def RegisterObjectAsTaken(self, ObjectName):
		object= Bladex.GetEntity(ObjectName)
		if object:
			kind= object.Kind
			if not self.ObjectsTaken.count(kind):
				self.ObjectsTaken.append(kind)

	def WasObjectAlreadyTaken(self, ObjectName):
		object= Bladex.GetEntity(ObjectName)
		if object:
			kind= object.Kind
			return self.ObjectsTaken.count(kind)

	def GetObjectsTaken (self):
		return self.ObjectsTaken
