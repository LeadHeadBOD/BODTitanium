##///
##||| ENEMYTYPES.PY TITANIUM
##||| Change list:
##||| * Added Gold Ork
##||| * Skeletons now explode violently on death (# PLAGUE: Needs reworking)
##||| * Aded Ice Golem
##||| * Lich limbs now are excluded from collisions giving reliable weapon drops
##||| * Liches now award experience caused by early mutilation death if the weapon is thrown.
##||| * Lich vomit attack now deals more poison damage per level.
##||| * Cositas should no longer rotate on hit when already dead.
##||| * Spider spitting should now somewhat work  (# PLAGUE: Might need adjustments)
##\\\ 


################################################################################
# Define all the basic enemy race classes here.
# All races inherit from Enm_Def.NPCPerson.
# Additional race values and behaviours defined here.
################################################################################
import Bladex
import Enm_Def
import Reference
import Combat
import AuxTran
import AniSound
import pdb
import BCopy
import math
import whrandom
import Actions
import Interpolator
import CharStats
import ItemTypes
import AuxFuncs
import Sparks
import Objects
import InitDataField
import Blood
import dust
import B3DLib
import Damage
import darfuncs
import GenFX
import OnOff
import DMusic
import ObjStore



#
# Boolean value
#
TRUE = 1==1
FALSE = not TRUE

################################################################################
# Define the Knight_Traitor class
################################################################################
class Knight_Traitor (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)
		#print "Personage Creado",me.Name,self.changed_func

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

	def ResetSounds(self, EntityName):
		me=Bladex.GetEntity(EntityName)
		if me.Kind=="Knight_Traitor":
			AniSound.AsignarSonidosCaballeroTraidor(EntityName)
		elif me.Kind=="Dark_Knight":
			AniSound.AsignarSonidosCaballeroOscuro(EntityName)

	# Functions for loading and saving state
	def __getstate__(self):
		#print "Changed Funcs",self.changed_func

		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Knight_Traitor.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Knight_Traitor"]=()
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Knight_Traitor"]
			#self.SoundPriorities=parms[0]

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 1.5
			me.BlockingPropensity = 0.7
			me.AttackList = BCopy.deepcopy(Combat.TraitorKnightAttackData)
			self.ChanceOfFuryOnHurt = 0.25
			self.ChanceOfFuryOnLeaderDeath = 1.00

################################################################################

################################################################################
# Define the Dark_Knight class
################################################################################
class Dark_Knight (Knight_Traitor):
	pass
################################################################################


################################################################################
# Define the Ork class
################################################################################
class Ork (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# anims
		me.AnmTranFunc=AuxTran.AuxTranOrc

		# Set up orc specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

	def ResetSounds(self, EntityName):
		me=Bladex.GetEntity(EntityName)
		if me.Kind=="Ork":
			AniSound.AsignarSonidosOrco(EntityName)
		elif me.Kind=="Great_Ork":
			AniSound.AsignarSonidosOrcoGrande(EntityName)
		elif me.Kind=="Dark_Ork":                           # Added
			AniSound.AsignarSonidosOrcoOscuro(EntityName)   #
		elif me.Kind=="Gold_Ork":                           #
			AniSound.AsignarSonidosOrcoGold(EntityName)     #       -LeadHead

	# Functions for loading and saving state
	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Ork.__getstate__(): Base class version differs."
			# Throw?
			return NPCPerson_state
		NPCPerson_state[1]["Ork"]=()

		return NPCPerson_state
		#self.ResetCombat(me.Name)

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Ork"]
			#self.SoundPriorities=parms[0]

		me=Bladex.GetEntity(self.Name)
		me.AnmTranFunc=AuxTran.AuxTranOrc

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.2
			me.AttackList = BCopy.deepcopy(Combat.OrkAttackData)
			self.ChanceOfFuryOnHurt = 0.45

################################################################################


################################################################################
# Define the Great_Ork class
################################################################################
class Great_Ork (Ork):
	pass

################################################################################

################################################################################
# Define the Dark_Ork class
################################################################################
class Dark_Ork (Ork):
	pass

################################################################################

################################################################################
# Define the Gold_Ork class
################################################################################
class Gold_Ork (Ork):
	pass

################################################################################

################################################################################
# Define the Skeleton class
################################################################################
class Skeleton (Enm_Def.NPCPerson):

    ### Set up constants for getting ended rightly
	pHitImpulse = [0.0,0.0,0.0]
	# dHitImpulse = [0.0,0.0,0.0]
	Absolutely_Annihilated = FALSE
    
    
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)
		self.pHitImpulse = [0.0,0.0,0.0]
		self.Absolutely_Annihilated = FALSE
		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up skeleton specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   =  1.0
		self.SoundPriorities[Reference.SND_HIT]     =  1.0
		self.SoundPriorities[Reference.SND_NPC]     = -1.0
		self.SoundPriorities[Reference.SND_NOISYPC] =  3.0
		self.SoundPriorities[Reference.SND_PC]      =  2.0
		me.ImDeadFunc=self.ImDeadFunc

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosEsqueleto(EntityName)

	# Functions for loading and saving state
	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)

		if(NPCPerson_state[0]!=1):
			print "ERROR: Skeleton.__getstate__(): Base class version differs."
			# Throw?
			return NPCPerson_state
		NPCPerson_state[1]["Skeleton"]=()

		return NPCPerson_state
		#self.ResetCombat(me.Name)

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Skeleton"]
			#self.SoundPriorities=parms[0]

		#me=Bladex.GetEntity(self.Name)
		#me.ImDeadFunc=self.ImDeadFunc

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.6
			me.AttackList = BCopy.deepcopy(Combat.SkeletonAttackData)

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		print "El esqueleto se convertira en polvo"
		Bladex.AddScheduledFunc(Bladex.GetTime()+10, dust.EnPolvoPerson,(EntityName,100,0,))

		### For shattering on powerful hits -LeadHead
        ### Unused cosita code utilized as a basis.
		if self.Absolutely_Annihilated == TRUE:
			me.InterruptCombat()
			me.Wuea=Reference.WUEA_ENDED
			me.LaunchAnmType("dth_explo")
			me.ExclusionGroup=1                 ### PLAGUE: Seems to be a solution for getting stuck in corpses.
			me_pos = me.Position

			for limb_id in (1, 2, 3, 4, 5, 6, 8):
				try: 
					limb = me.SeverLimb(limb_id)
				except:
					pass
				# print "severing "+`limb_id`
				# limb.Position = (limb.Position[0], limb.Position[1]-200, limb.Position[2])    # move the limb higher so it doesn't trigger TestHit.
				# print `limb_id`+" position set"
                
				if limb:
					limb_pos = limb.Position
					OutImpulse = B3DLib.Normalize ((limb_pos[0]-me_pos[0], limb_pos[1]-me_pos[1], limb_pos[2]-me_pos[2]))
					OutImpulse = B3DLib.Scale (OutImpulse, 4000.0)
					limb.Impulse(OutImpulse[0], OutImpulse[1], OutImpulse[2])
					limb.AngularVelocity = whrandom.uniform(-10, 10), whrandom.uniform(-10, 10), whrandom.uniform(-10, 10)
					# print `limb_id`+" OutImpulse applied"
					# limb.Impulse(self.dHitImpulse[0], self.dHitImpulse[1], self.dHitImpulse[2])
					# print `limb_id`+" pHitImpulse applied"
			else: 
				me.Angle= B3DLib.GetXZAngle(-self.pHitImpulse[0], 0.0, -self.pHitImpulse[2])


	def MutilateFunc(self,EntityName,obj_name,x,y,z,nx,ny,nz,node):
		limb= Bladex.GetEntity(obj_name)
		InitDataField.Initialise(limb)
		limb.ExclusionGroup=1   # Ensure limbs aren't causing unneeded hit detection calls -LeadHead
		if limb.TestHit:                                # 
			limb.Move(0, -160, 0)                       # Fixes disappearing limbs
			limb.PutToWorld()                           # 
			limb.Impulse(0,0,0)                         #    -LeadHead
		Bladex.AddScheduledFunc(Bladex.GetTime()+10, dust.EnPolvoObjeto,(obj_name,100,0,))

        
	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):                       ### We override this function because we want to check
		Enm_Def.NPCPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)      ### what was the last damage type and does it do enough damage
		me = Bladex.GetEntity(EntityName)                                                                                   ### -LeadHead
		
		if DamageType == "Crush" and (DamagePoints > CharStats.GetCharMaxLife(me.Kind, me.Level)):
			self.Absolutely_Annihilated = TRUE
            
	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz):                             ### Override this func to save values for weapon impulse.
		Enm_Def.NPCPerson.HitFunc(self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz)             ### -LeadHead
		me = Bladex.GetEntity(EntityName)
		if me.Life>0:
			self.pHitImpulse[0] = Px*0.2;
			self.pHitImpulse[1] = Py*0.2;
			self.pHitImpulse[2] = Pz*0.2;
			
			# self.dHitImpulse[0] = Cx*50000.0;
			# self.dHitImpulse[1] = Cy*50000.0;
			# self.dHitImpulse[2] = Cz*50000.0
			
			# print self.pHitImpulse

################################################################################

################################################################################
# Define the Knight of the Living Dead class
################################################################################
class Knight_living_dead (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# anims
		me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = -1.0
		self.SoundPriorities[Reference.SND_HIT]     = -1.0
		self.SoundPriorities[Reference.SND_NPC]     = -1.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0
		me.ImDeadFunc=self.ImDeadFunc

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosZombie(EntityName)

	# Functions for loading and saving state
	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Knight_Traitor.__getstate__(): Base class version differs."
			# Throw?
			return NPCPerson_state
		NPCPerson_state[1]["Knight_living_dead"]=()

		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Knight_living_dead"]
			#self.SoundPriorities=parms[0]

		#me=Bladex.GetEntity(self.Name)
		#me.ImDeadFunc=self.ImDeadFunc

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.0
			me.AttackList = BCopy.deepcopy(Combat.TraitorKnightAttackData)

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		print "El zombi se convertira en polvo"
		Bladex.AddScheduledFunc(Bladex.GetTime()+10, dust.EnPolvoPerson,(EntityName,100,0,))

################################################################################

################################################################################
# Define the Chaos Knight class
################################################################################

class ChaosKnight (Enm_Def.NPCPerson):

	RightWeapon=""
	LeftWeapon=""
	rightweaponsound=""
	leftweaponsound=""
	chkdisapsound=""
	chklaughsound=""
	missilesound1=None
	missilesound2=None
	missileconcsound=None

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25
		self.DamageFactorHeavy = 0.35

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		me.AddAnmEventFunc("Chkmagicstart", self.PrepareShoot)
		me.AddAnmEventFunc("Chkmagicfire", self.Shoot)
		#me.AddAnmEventFunc("Chkmagicfinish", self.FinishShoot)
		me.OnStepFunc = darfuncs.QuakeStep


		self.missilesound1=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO.wav", "MissileSound1")
		self.missilesound1.Volume=0.6
		self.missilesound1.MinDistance=10000
		self.missilesound1.MaxDistance=20000
		self.missilesound2=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO2.wav", "MissileSound2")
		self.missilesound2.Volume=0.6
		self.missilesound2.MinDistance=10000
		self.missilesound2.MaxDistance=20000
		self.missileconcsound=Bladex.CreateSound("../../Sounds/aparicion-espada.wav", "MissileConcSound")
		self.missileconcsound.Volume=0.6
		self.missileconcsound.MinDistance=10000
		self.missileconcsound.MaxDistance=20000

	# Functions for loading and saving state
	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: ChaosKnight.__getstate__(): Base class version differs."
			# Throw?
			return NPCPerson_state
		NPCPerson_state[1]["ChaosKnight"]=(self.RightWeapon,self.LeftWeapon,self.rightweaponsound,self.leftweaponsound,self.chkdisapsound,self.chklaughsound)

		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["ChaosKnight"]
			self.RightWeapon=parms[0]
			self.LeftWeapon=parms[1]
			self.rightweaponsound=parms[2]
			self.leftweaponsound=parms[3]
			self.chkdisapsound=parms[4]
			self.chklaughsound=parms[5]

		me=Bladex.GetEntity(self.Name)
		me.AddAnmEventFunc("Chkmagicstart", self.PrepareShoot)
		me.AddAnmEventFunc("Chkmagicfire", self.Shoot)
		#me.AddAnmEventFunc("Chkmagicfinish", self.FinishShoot)
		me.AddAnmEventFunc("ChkApR", self.ActivateWeapon)
		me.AddAnmEventFunc("ChkDisapR", self.DeactivateWeapon)
		me.AddAnmEventFunc("ChkApL", self.ActivateWeapon)
		me.AddAnmEventFunc("ChkDisapL", self.DeactivateWeapon)
		me.OnStepFunc = darfuncs.QuakeStep
		self.missilesound1=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO.wav", "MissileSound1")
		self.missilesound1.Volume=0.6
		self.missilesound1.MinDistance=10000
		self.missilesound1.MaxDistance=20000
		self.missilesound2=Bladex.CreateSound("../../Sounds/M-IMPACTO-FUEGO2.wav", "MissileSound2")
		self.missilesound2.Volume=0.6
		self.missilesound2.MinDistance=10000
		self.missilesound2.MaxDistance=20000
		self.missileconcsound=Bladex.CreateSound("../../Sounds/aparicion-espada.wav", "MissileConcSound")
		self.missileconcsound.Volume=0.6
		self.missileconcsound.MinDistance=10000
		self.missileconcsound.MaxDistance=20000

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosCaballeroKaos(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=FALSE
			me.AttackList = BCopy.deepcopy(Combat.ChaosKnightAttackData)

	def MissileOnHit (self, MissileName, hit_entity):
		missile=Bladex.GetEntity(MissileName)
		if hit_entity:
			#print MissileName+" hitting "+hit_entity
			pass
		else:
			missile.Data.missilesound.StopSound()
			x, y, z=missile.Position
			self.missilesound2.Play(x, y, z, 0)
			impactps=Bladex.CreateEntity("ImpactPS", "Entity Particle System D1", x, y, z)
			impactps.ParticleType="BlueMagicMissile"
			impactps.PPS=2000
			impactps.YGravity=1400.0
			impactps.Friction=0.06
			#impactps.Velocity=-ImpX/5.0, -ImpY/5.0, -ImpZ/5.0
			impactps.RandomVelocity=40.0
			impactps.Time2Live=20
			impactps.DeathTime=Bladex.GetTime()+0.25
			luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", x, y, z)
			luzimp.Color=200, 200, 255
			luzimp.Intensity=1.0
			luzimp.Precission=0.001
			luzimp.CastShadows=0
			luzimp.Flick=0
			luzimp.Visible=0

			missileesphere=missile.Data.Sphere
			if missileesphere:
				missile.Unlink(missileesphere)
				AuxFuncs.FadeObject(missileesphere.Name, missileesphere.Alpha, 0.0, 0.5, 1)

			ray1=missile.Data.MissileRay1
			if ray1:
				missileesphere.Unlink(ray1)
				ray1.MaxAmplitude=800
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, ray1.SubscribeToList, ("Pin",))

			ray2=missile.Data.MissileRay2
			if ray2:
				missileesphere.Unlink(ray2)
				ray2.MaxAmplitude=800
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, ray2.SubscribeToList, ("Pin",))

			ray3=missile.Data.MissileRay3
			if ray3:
				ray3.MaxAmplitude=800
				missileesphere.Unlink(ray3)
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, ray3.SubscribeToList, ("Pin",))

			AuxFuncs.SpotIntensityVariation(luzimp.Name, 1.0, 0.0, 1.0, 1)

			Bladex.AddScheduledFunc(Bladex.GetTime(), self.DeleteMissile, (missile.Name,),"DeleteMissile")

	def MissileImpact(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		missile=Bladex.GetEntity(EntityName)
		missile.Data.missilesound.StopSound()
		x, y, z=missile.Position
		self.missilesound2.Play(x, y, z, 0)
		impactps=Bladex.CreateEntity("ImpactPS", "Entity Particle System D1", x, y, z)
		impactps.ParticleType="BlueMagicMissile"
		impactps.PPS=2000
		impactps.YGravity=1400.0
		impactps.Friction=0.06
		impactps.Velocity=-ImpX/5.0, -ImpY/5.0, -ImpZ/5.0
		impactps.RandomVelocity=40.0
		impactps.Time2Live=20
		impactps.DeathTime=Bladex.GetTime()+0.25
		luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", x-ImpX/10.0, y-ImpY/10.0, z-ImpZ/10.0)
		luzimp.Color=200, 200, 255
		luzimp.Intensity=1.0
		luzimp.Precission=0.001
		luzimp.CastShadows=0
		luzimp.Flick=0
		luzimp.Visible=0

		missileesphere=missile.Data.Sphere
		if missileesphere:
			missile.Unlink(missileesphere)
			AuxFuncs.FadeObject(missileesphere.Name, missileesphere.Alpha, 0.0, 0.5, 1)

		ray1=missile.Data.MissileRay1
		if ray1:
			missileesphere.Unlink(ray1)
			ray1.MaxAmplitude=800
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, ray1.SubscribeToList, ("Pin",))

		ray2=missile.Data.MissileRay2
		if ray2:
			missileesphere.Unlink(ray2)
			ray2.MaxAmplitude=800
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, ray2.SubscribeToList, ("Pin",))

		ray3=missile.Data.MissileRay3
		if ray3:
			ray3.MaxAmplitude=800
			missileesphere.Unlink(ray3)
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, ray3.SubscribeToList, ("Pin",))

		AuxFuncs.SpotIntensityVariation(luzimp.Name, 1.0, 0.0, 1.0, 1)

		missile.Data.OldInflictHitFunc(EntityName, VictimName, ImpX, ImpY, ImpZ)
		Bladex.AddScheduledFunc(Bladex.GetTime(), self.DeleteMissile, (missile.Name,),"DeleteMissile")

	def DeleteMissile(self, missileName):
		missile=Bladex.GetEntity(missileName)
		if missile:
			if Reference.EntitiesObjectData.has_key(missile.Name):
				del Reference.EntitiesObjectData[missile.Name]
			missile.Damage=0
			missile.SubscribeToList("Pin")

	def ApareceElArmaPorqueSeMeCantaElCulo(self):
		if self.RightWeapon:
			Bladex.GetEntity(self.RightWeapon).Alpha = 1

	def PrepareShoot(self, EntityName, EventName):
		Bladex.AddScheduledFunc(Bladex.GetTime()+15, self.ApareceElArmaPorqueSeMeCantaElCulo, (),EntityName+"ApareceElArmaPorqueSeMeCantaElCulo")
		if self.RightWeapon:
			weapon=self.RightWeapon
			weaponpoly=weapon+"Poly"
			AuxFuncs.FadeObject(weaponpoly, 0.0, 0.98, 1.0)
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, AuxFuncs.FadeObject, (weapon, 1.0, 0.0, 0.8),EntityName+"Fade1")
			Bladex.AddScheduledFunc(Bladex.GetTime()+1.2, AuxFuncs.FadeObject, (weaponpoly, 0.98, 0.0, 1.0),EntityName+"Fade2")

		# Organize the fade back now
		me=Bladex.GetEntity(EntityName)
		if me:
			FinishShootTime= (0.70-me.AnmPos) * Bladex.GetAnimationDuration("Chk_g_magic")
			Bladex.AddScheduledFunc(Bladex.GetTime()+FinishShootTime, self.FinishShoot, (EntityName, "Chkmagicfinish"),EntityName+"FinishShoot")

			mcps=Bladex.CreateEntity("MissileConcPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
			mcps.PersonName=EntityName
			mcps.PersonNodeName="R_Hand"
			mcps.FollowFactor=1.0
			mcps.ParticleType="FastEnergyConc"
			mcps.PPS=600
			mcps.YGravity=0.0
			mcps.Friction=0.0
			mcps.Velocity=0.0, 0.0, 0.0
			mcps.RandomVelocity=-8.0
			mcps.NormalVelocity=-8.0
			mcps.Time2Live=30
			mcps.DeathTime=Bladex.GetTime()+2.5

			x,y,z= me.GraspPos("R_Hand")
			self.missileconcsound.Play(x, y, z, 0)


	def Shoot(self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			x,y,z= me.GraspPos("R_Hand")
			target= Bladex.GetEntity(me.GetEnemyName())
			target_pos= target.Position
			angle= -B3DLib.GetYAngle(target_pos[0]-x,target_pos[1]-y,target_pos[2]-z)
			vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*6000, -math.sin(angle)*6000)
			#vx,vy,vz= me.Rel2AbsVector(0,-6000.0,0.0)
			msps=Bladex.CreateEntity("MissileShootPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
			msps.PersonName=EntityName
			msps.PersonNodeName="R_Hand"
			msps.ParticleType="FastEnergyConc"
			msps.PPS=1800
			msps.YGravity=0.0
			msps.Friction=0.1
			msps.Velocity=0.0, 0.0, 0.0
			msps.RandomVelocity=20.0
			msps.NormalVelocity=40.0
			msps.Time2Live=15
			msps.DeathTime=Bladex.GetTime()+0.2
			self.missilesound1.Play(x, y, z, 0)
			missileesphere=Bladex.CreateEntity("MissileEsphere", "EsferaNegra", 0.0, 0.0, 0.0)
			missileesphere.Alpha=0.0
			AuxFuncs.FadeObject(missileesphere.Name, 0.0, 0.7, 1.0)
			missileps1=Bladex.CreateEntity("MissilePS1", "Entity Particle System D1", 0.0, 0.0, 0.0)
			missileps1.ParticleType="BlueMagicMissile"
			missileps1.PPS=200
			#missileps1.FollowFactor=1.0 -> Lo pongo despues de lincado para que no haga raros
			missileps1.YGravity=0.0
			missileps1.Friction=0.08
			missileps1.Velocity=0.0, 0.0, 0.0
			missileps1.RandomVelocity=15.0
			missileps1.Time2Live=30
			missileps2=Bladex.CreateEntity("MissilePS2", "Entity Particle System D1", 0.0, 0.0, 0.0)
			missileps2.ParticleType="BlueMagicMissile"
			missileps2.PPS=100
			missileps2.YGravity=0.0
			missileps2.Friction=0.04
			missileps2.Velocity=0.0, 0.0, 0.0
			missileps2.RandomVelocity=-5.0
			missileps2.Time2Live=25
			ray1=Bladex.CreateEntity("Ray1", "Entity ElectricBolt", 0.0, 240.0, 0.0)
			ray1.Target=0.0, -240.0, 0.0
			ray1.FixedTarget=0
			ray1.MaxAmplitude=300
			ray1.MinSectorLength=10000
			ray1.Damage=0
			ray1.Active=1
			ray2=Bladex.CreateEntity("Ray2", "Entity ElectricBolt", 240.0, 0.0, 0.0)
			ray2.Target=-240.0, 0.0, 0.0
			ray2.FixedTarget=0
			ray2.MaxAmplitude=300
			ray2.MinSectorLength=10000
			ray2.Damage=0
			ray2.Active=1
			ray3=Bladex.CreateEntity("Ray3", "Entity ElectricBolt", 0.0, 0.0, 240.0)
			ray3.Target=0.0, 0.0, -240.0
			ray3.FixedTarget=0
			ray3.MaxAmplitude=300
			ray3.MinSectorLength=10000
			ray3.Damage=0
			ray3.Active=1
			missile=ItemTypes.MakeHunterSeekerMissile("MM1", x,y,z,vx,vy,vz, me.GetEnemyName())
			missile.Intensity=1.0
			missile.Color= 200.0,200.0,255.0
			missile.CastShadows=0
			missile.Visible=0
			missile.Flick=0
			missilesound=Bladex.CreateEntity("MissileSound", "Entity Sound", 0, 0, 0)
			missilesound.SetSound("../../Sounds/M-CAMPO-MAG.wav")
			missilesound.MinDistance=10000
			missilesound.MaxDistance=20000
			missile.Link(missilesound)
			missile.Link(missileps1)
			missile.Link(missileps2)
			missile.Link(missileesphere)
			missileesphere.Link(ray1)
			missileesphere.Link(ray2)
			missileesphere.Link(ray3)
			missileps1.FollowFactor=1.0
			missilesound.PlaySound(-1)
			InitDataField.Initialise(missile)
			missile.Data.OldInflictHitFunc=missile.InflictHitFunc
			missile.InflictHitFunc=self.MissileImpact
			missile.OnHitFunc=self.MissileOnHit
			missile.Data.missilesound=missilesound
			missile.Data.Sphere=missileesphere
			missile.Data.MissileRay1=ray1
			missile.Data.MissileRay2=ray2
			missile.Data.MissileRay3=ray3
			print "Creating EntitiesObjectData for sphere in Shoot()"
			Reference.EntitiesObjectData[missile.Name]= BCopy.deepcopy(Reference.DefaultObjectData['EsferaNegra'])

	def FinishShoot(self, EntityName, EventName):
		if self.RightWeapon:
			weapon=self.RightWeapon
			weaponpoly=weapon+"Poly"
			AuxFuncs.FadeObject(weaponpoly, 0.0, 0.98, 1.0)
			Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, AuxFuncs.FadeObject, (weapon, 0.0, 1.0, 1.0),EntityName+"Fade3")
			Bladex.AddScheduledFunc(Bladex.GetTime()+1.2, AuxFuncs.FadeObject, (weaponpoly, 0.98, 0.0, 0.8),EntityName+"Fade4")

####  ACLARACION:  self=pers.Data

	def ActivateWeapon(self, EntityName, EventName):
		chk=Bladex.GetEntity(self.Name)
		inv=chk.GetInventory()
		if EventName=="ChkApR":
			weapon=self.RightWeapon
			weaponsound=self.rightweaponsound
			inv.LinkRightHand(weapon)
		else:
			weapon=self.LeftWeapon
			weaponsound=self.leftweaponsound
			inv.LinkLeftHand(weapon)
		weaponpoly=weapon+"Poly"
		weaponlight="Luz"+weapon
		weapon_pos=Bladex.GetEntity(weapon).Position
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, weaponsound.Play, (weapon_pos[0], weapon_pos[1], weapon_pos[2], 0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, AuxFuncs.SpotIntensityVariation, (weaponlight, 0.0, 3.0, 2.0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, AuxFuncs.SpotIntensityVariation, (weaponlight, 3.0, 0.0, 1.0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.FadeObject, (weaponpoly, 0.0, 0.98, 3.9))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.9, AuxFuncs.FadeObject, (weaponpoly, 0.98, 0.0, 1.0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, AuxFuncs.FadeObject, (weapon, 0.0, 1.0, 1.0))
		wps=Bladex.CreateEntity("WPS", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		wps.ObjectName=weaponpoly
		#wps.FollowFactor=1.0
		wps.ParticleType="EnergyConc"
		wps.PPS=400
		wps.YGravity=0.0
		wps.Friction=0.0
		wps.Velocity=0.0, 0.0, 0.0
		wps.RandomVelocity=-5.0
		wps.NormalVelocity=-8.0
		wps.Time2Live=60
		wps.DeathTime=Bladex.GetTime()+3.0

	def EnergyDissipation(self, weaponpoly):
		wps=Bladex.CreateEntity("WPS", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		wps.ObjectName=weaponpoly
		wps.ParticleType="EnergyDissip"
		wps.PPS=400
		wps.YGravity=0.0
		wps.Friction=0.0
		wps.Velocity=0.0, 0.0, 0.0
		wps.RandomVelocity=2.0
		wps.NormalVelocity=6.0
		wps.Time2Live=60
		wps.DeathTime=Bladex.GetTime()+1.5

	def DeactivateWeapon(self, EntityName, EventName):
		chk=Bladex.GetEntity(self.Name)
		inv=chk.GetInventory()
		if EventName=="ChkDisapR":
			weapon=self.RightWeapon
			weaponsound=self.rightweaponsound
			Bladex.AddScheduledFunc(Bladex.GetTime()+3.3, inv.LinkRightHand, ("None",))
		else:
			weapon=self.LeftWeapon
			weaponsound=self.leftweaponsound
			Bladex.AddScheduledFunc(Bladex.GetTime()+3.3, inv.LinkLeftHand, ("None",))
		weaponpoly=weapon+"Poly"
		weaponlight="Luz"+weapon
		weapon_pos=Bladex.GetEntity(weapon).Position
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, weaponsound.Play, (weapon_pos[0], weapon_pos[1], weapon_pos[2], 0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.1, self.EnergyDissipation, (weaponpoly,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.2, AuxFuncs.SpotIntensityVariation, (weaponlight, 0.0, 3.0, 1.7))
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, AuxFuncs.SpotIntensityVariation, (weaponlight, 3.0, 0.0, 1.0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, AuxFuncs.FadeObject, (weaponpoly, 0.0, 0.98, 0.7))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.FadeObject, (weapon, 1.0, 0.0, 0.8))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.7, AuxFuncs.FadeObject, (weaponpoly, 0.98, 0.0, 1.5))

	# Prepara armas para aparicion/desaparicion

	def PrepareWeapons(self, RightWeaponKind="Espadon", LeftWeaponKind="Escudon"):
		chk_name=self.Name
		chk=Bladex.GetEntity(chk_name)
		if RightWeaponKind in ("Espadon", "Escudon"):
			objname=RightWeaponKind+chk_name
			espadon=Bladex.CreateEntity(objname, RightWeaponKind, 0, 0, 0)
			espadon.Weapon=1
			espadon.Alpha=0.0
			espadonpoly=Bladex.CreateEntity(objname+"Poly", RightWeaponKind+"Poly", 0, 0, 0)
			espadonpoly.CastShadows=0
			espadonpoly.Alpha=0.0
			espadonpoly.RasterMode="AdditiveAlpha"
			espadonpoly.RasterMode="Read"
			luzespadon=Bladex.CreateEntity("Luz"+objname, "Entity Spot", 0, 0, 0)
			luzespadon.Color=100, 130, 255
			luzespadon.Intensity=0.0
			luzespadon.Precission=0.001
			luzespadon.CastShadows=0
			luzespadon.Flick=0
			luzespadon.Visible=0
			espadon.Link(espadonpoly)
			espadon.Link(luzespadon)
			espadon.RemoveFromWorld()
			self.RightWeapon=espadon.Name
			self.rightweaponsound=Bladex.CreateSound("../../Sounds/aparicion-espada.wav", chk_name+"RightWeaponSound")
			self.rightweaponsound.MinDistance=10000
			self.rightweaponsound.MaxDistance=20000
			chk.AddAnmEventFunc("ChkApR", self.ActivateWeapon)
			chk.AddAnmEventFunc("ChkDisapR", self.DeactivateWeapon)
		if LeftWeaponKind in ("Espadon", "Escudon"):
			objname=LeftWeaponKind+chk_name
			escudon=Bladex.CreateEntity(objname, LeftWeaponKind, 0, 0, 0)
			escudon.Weapon=1
			escudon.Alpha=0.0
			escudon=Sparks.MakeShield(escudon.Name)
			escudonpoly=Bladex.CreateEntity(objname+"Poly", LeftWeaponKind+"Poly", 0, 0, 0)
			escudonpoly.CastShadows=0
			escudonpoly.Alpha=0.0
			escudonpoly.RasterMode="AdditiveAlpha"
			escudonpoly.RasterMode="Read"
			luzescudon=Bladex.CreateEntity("Luz"+objname, "Entity Spot", 0, 0, 0)
			luzescudon.Color=100, 130, 255
			luzescudon.Intensity=0.0
			luzescudon.Precission=0.001
			luzescudon.CastShadows=0
			luzescudon.Flick=0
			luzescudon.Visible=0
			escudon.Link(escudonpoly)
			escudon.Link(luzescudon)
			escudon.RemoveFromWorld()
			self.LeftWeapon=escudon.Name
			self.leftweaponsound=Bladex.CreateSound("../../Sounds/aparicion-escudo.wav", chk_name+"LeftWeaponSound")
			self.leftweaponsound.MinDistance=10000
			self.leftweaponsound.MaxDistance=20000
			chk.AddAnmEventFunc("ChkApL", self.ActivateWeapon)
			chk.AddAnmEventFunc("ChkDisapL", self.DeactivateWeapon)


	# Prepara cilindro magico para desaparicion

	def PrepareDisappearance(self):
		chk_name=self.Name
		chk=Bladex.GetEntity(chk_name)
		chk.ImDeadFunc=self.Disappear
		cilint=Bladex.CreateEntity("CilInt"+chk_name, "CilindroMagico", 0, 0, 0)
		cilint.Orientation=0.707107,0.707107,0.000000,0.000000
		cilint.Scale=0.1
		cilint.RasterMode="AdditiveAlpha"
		cilint.RasterMode="Read"
		cilint.Alpha=0.0
		cilint.CastShadows=0
		cilintdin=Objects.CreateDinamicObject(cilint.Name)
		cilint.RemoveFromWorld()
		cilext=Bladex.CreateEntity("CilExt"+chk_name, "CilindroMagico2", 0, 0, 0)
		cilext.Orientation=0.707107,0.707107,0.000000,0.000000
		cilext.Scale=0.1
		cilext.RasterMode="AdditiveAlpha"
		cilext.RasterMode="Read"
		cilext.Alpha=0.0
		cilext.CastShadows=0
		cilextdin=Objects.CreateDinamicObject(cilext.Name)
		cilext.RemoveFromWorld()
		luzchk=Bladex.CreateEntity("Luz"+chk_name, "Entity Spot", 0, 0, 0)
		luzchk.Color=100, 130, 255
		luzchk.Intensity=0.0
		luzchk.Precission=0.001
		luzchk.CastShadows=0
		luzchk.Flick=0
		luzchk.Visible=0
		luzchk.RemoveFromWorld()
		self.chkdisapsound=Bladex.CreateSound("../../Sounds/chaos-desaparece.wav", chk_name+"DisappearSound")
		self.chkdisapsound.MinDistance=10000
		self.chkdisapsound.MaxDistance=20000
		self.chklaughsound=Bladex.CreateSound("../../Sounds/flus1.WAV", chk_name+"LaughSound")
		self.chklaughsound.MinDistance=10000
		self.chklaughsound.MaxDistance=20000


	# Aparicion

	def Appear(self):
		chk=Bladex.GetEntity(self.Name)
		if self.RightWeapon:
			esp=Bladex.GetEntity(self.RightWeapon)
			esp.Alpha=0
		if self.LeftWeapon:
			esc=Bladex.GetEntity(self.LeftWeapon)
			esc.Alpha=0
		chk.UnFreeze()
		chk.Alpha=1.0
		chk.Wuea=Reference.WUEA_ENDED
		chk.LaunchAnmType("appears")


	# Desaparicion

	def CilSclVariation(self, escinic, velinicvaresc, acvaresc, tinicvaresc, velvartr):
		tiempotransc=Bladex.GetTime()-tinicvaresc
		escactual=escinic+velinicvaresc*tiempotransc+0.5*acvaresc*tiempotransc**2.0
		cilint=Bladex.GetEntity("CilInt"+self.Name)
		cilext=Bladex.GetEntity("CilExt"+self.Name)
		cilint.Scale=cilext.Scale=escactual
		if velvartr>0.0:
			cilint.Alpha=cilext.Alpha=min(0.0+velvartr*tiempotransc, 0.98)
		else:
			cilint.Alpha=cilext.Alpha=max(0.98+velvartr*tiempotransc, 0.0)

	def DisappearChaosKnight(self, EntityName, EventName):
		tiempo1=1.0
		tiempo2=3.0
		velvartr1=(0.98-0.0)/(3.0*tiempo1/4.0)
		velvartr2=(0.0-0.98)/(3.0*tiempo2/4.0)
		escinic1=escfin2=0.1
		escfin1=escinic2=1.4
		varesca=escfin1-escinic1
		despla=(1210.0*varesca)/0.9 #despla=1210.0 para varesc=1.0-0.1
		desplb=(460.0*varesca)/0.9 #desplb=460.0 para varesc=1.0-0.1
		velfin1a=0.0
		velfin1b=0.0
		velinic1a=2.0*despla/tiempo1-velfin1a
		velinic1b=2.0*desplb/tiempo1-velfin1b
		velinic2a=0.0
		velinic2b=0.0
		velfin2a=2.0*despla/tiempo2-velinic2a
		velfin2b=2.0*desplb/tiempo2-velinic2b
		tiempointerm=0.0
		tiemporot=tiempo1+tiempointerm+tiempo2-0.05
		velang=1.0
		ang=velang*tiemporot
		velfinvaresc1=0.0
		velinicvaresc1=2.0*(escfin1-escinic1)/tiempo1-velfinvaresc1
		velinicvaresc2=0.0
		velfinvaresc2=2.0*(escfin2-escinic2)/tiempo2-velinicvaresc2
		acvaresc1=2.0*(velfinvaresc1*tiempo1-escfin1+escinic1)/tiempo1**2.0
		acvaresc2=2.0*(velfinvaresc2*tiempo2-escfin2+escinic2)/tiempo2**2.0
		tinicvaresc1=Bladex.GetTime()
		tinicvaresc2=tinicvaresc1+tiempo1+tiempointerm
		chk_name=self.Name
		wps=Bladex.CreateEntity("WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=chk_name
		wps.ParticleType="EnergyDissip"
		wps.PPS=200
		wps.YGravity=-300.0
		wps.Friction=0.0
		wps.Velocity=0.0, 0.0, 0.0
		wps.RandomVelocity=1.0
		wps.NormalVelocity=-3.0
		wps.Time2Live=60
		wps.DeathTime=Bladex.GetTime()+2.5
		chk=Bladex.GetEntity(chk_name)
		AuxFuncs.FadeObject(chk_name, 1.0, 0.0, tiempo1+tiempointerm+2.0*tiempo2/3.0)
		cilint=Bladex.GetEntity("CilInt"+chk_name)
		cilext=Bladex.GetEntity("CilExt"+chk_name)
		cilint.Position=chk.Position[0], chk.Position[1]+1410.0, chk.Position[2]
		cilext.Position=chk.Position[0], chk.Position[1]+1490.0, chk.Position[2]
		cilint.Scale=cilext.Scale=0.1
		cilint.Alpha=cilext.Alpha=0.98
		cilintdin=cilint.Data.dinobjdata
		cilextdin=cilext.Data.dinobjdata
		Objects.RotateObject(cilintdin, ang, velang, velang, (0.0, 0.0, 0.0), (0, 0, 1))
		Objects.RotateObject(cilextdin, -ang, velang, velang, (0.0, 0.0, 0.0), (0, 0, 1))
		Objects.DisplaceObject(cilintdin, despla, (0.0, -1.0, 0.0), velinic1a, 0.0, "", "", "", self.CilSclVariation, (escinic1, velinicvaresc1, acvaresc1, tinicvaresc1, velvartr1))
		Objects.DisplaceObject(cilextdin, desplb, (0.0, -1.0, 0.0), velinic1b, 0.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+tiempo1+tiempointerm, Objects.DisplaceObject, (cilintdin, despla, (0.0, 1.0, 0.0), 0.0, velfin2a, "", "", "", self.CilSclVariation, (escinic2, velinicvaresc2, acvaresc2, tinicvaresc2, velvartr2), cilint.RemoveFromWorld, ()), "RecogeCilInt")
		Bladex.AddScheduledFunc(Bladex.GetTime()+tiempo1+tiempointerm, Objects.DisplaceObject, (cilextdin, desplb, (0.0, 1.0, 0.0), 0.0, velfin2b, "", "", "", "", (), cilext.RemoveFromWorld, ()), "RecogeCilExt")
		luzchk_name="Luz"+chk_name
		luzchk=Bladex.GetEntity(luzchk_name)
		luzchk.Position=chk.Position
		AuxFuncs.SpotIntensityVariation(luzchk_name, 0.0, 4.0, tiempo1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+tiempo1+tiempointerm, AuxFuncs.SpotIntensityVariation, (luzchk_name, 4.0, 0.0, 3.0*tiempo2/4.0), "ApagaLuzChk")
		sound_pos=chk.Position
		self.chkdisapsound.Play(sound_pos[0], sound_pos[1]-250.0, sound_pos[2], 0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, self.chklaughsound.Play, (sound_pos[0], sound_pos[1]-500.0, sound_pos[2], 0), "PlayLaugh")
		Bladex.AddScheduledFunc(Bladex.GetTime()+tiempo1+tiempointerm+tiempo2, self.RemoveChaosKnight, ())

	def RemoveChaosKnight(self):
		chk=Bladex.GetEntity(self.Name)
		chk.Life=0
		DMusic.decEnemies(chk.Name)
		chk.Freeze()
		chk.RemoveFromWorld()

	def Disappear(self, VictimName):
		chk=Bladex.GetEntity(self.Name)
		if self.RightWeapon:
			esp=Bladex.GetEntity(self.RightWeapon)
			esp.Alpha=1
		if self.LeftWeapon:
			esc=Bladex.GetEntity(self.LeftWeapon)
			esc.Alpha=1
		chk.Alpha=1.0
		chk.AddAnmEventFunc("ChkDisap", self.DisappearChaosKnight)
		chk.Wuea=Reference.WUEA_ENDED
		chk.LaunchAnmType("disappear")

	def InteruptActions(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		Bladex.RemoveScheduledFunc(EntityName+"ApareceElArmaPorqueSeMeCantaElCulo")
		Bladex.RemoveScheduledFunc(EntityName+"Fade1")
		Bladex.RemoveScheduledFunc(EntityName+"Fade2")
		Bladex.RemoveScheduledFunc(EntityName+"Fade3")
		Bladex.RemoveScheduledFunc(EntityName+"Fade4")


################################################################################

################################################################################
# Define the Little Demon class
################################################################################

class Little_Demon (Enm_Def.NPCPerson):

	Fader=None
	FadeOutTime= 0.23333
	FadeInTime= 0.23333
	TransitTime= 0.0
	AGE_Number=0
	ImplosionPeriod = 2.5
	DeathBallPeriod = 3.5

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)
		me.ImDeadFunc=self.ImDeadFunc

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead
		#x,y,z= me.GraspPos("ViewPoint")
		#self.HunterSeeker= ItemTypes.HunterSeekerMissile("HunterSeeker"+me.Name, x, y, z)


		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# Create a linear interpolator for fading
		FadeList=[me.Name]
		self.Fader= EntitiesFader (FadeList)

		self.DamageFactorNone  = 0.1
		self.DamageFactorLight = 0.2

		me.AddAnmEventFunc("Spit", self.StartSpit)
		me.AddAnmEventFunc("Disappear", self.Disappear)
		me.AddAnmEventFunc("EndZig", self.EndZig)
		me.AddAnmEventFunc("EndZag", self.EndZag)

	# Functions for loading and saving state
	def __getstate__(self):
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Little_Demon.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Little_Demon"]=(self.AGE_Number,)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Little_Demon"]
			self.AGE_Number=parms[0]

		me=Bladex.GetEntity(self.Name)
		# Create a linear interpolator for fading
		FadeList=[me.Name]
		self.Fader= EntitiesFader (FadeList)
		self.FadeOutTime= 0.23333
		self.FadeInTime= 0.23333
		self.TransitTime= 0.0
		self.DamageFactorNone  = 0.1
		self.DamageFactorLight = 0.2
		self.ImplosionPeriod = 2.5
		self.DeathBallPeriod = 3.5
		me.AddAnmEventFunc("Spit", self.StartSpit)
		me.AddAnmEventFunc("Disappear", self.Disappear)
		me.AddAnmEventFunc("EndZig", self.EndZig)
		me.AddAnmEventFunc("EndZag", self.EndZag)
		#me.ImDeadFunc=self.ImDeadFunc

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosLittleDemon(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=FALSE
			me.AttackList = BCopy.deepcopy(Combat.LittleDemonAttackData)
			me.BlockingPropensity= 0.4

	def FadeOut (self,EntityName):
		self.Fader.FadeOut(self.FadeOutTime)

	def FadeIn (self,EntityName):
		self.Fader.FadeIn(self.FadeInTime)

	def Disappear (self,EntityName,EventName):
		#print "Disappearing..."
		me = Bladex.GetEntity(EntityName)
		# May wish to make all attacks pass through...
		self.FadeOut(EntityName)
		time= Bladex.GetTime()
		Bladex.AddScheduledFunc(time+self.FadeOutTime+self.TransitTime, self.Reappear, (EntityName,), EntityName+" Reappear")

	def IntersectCircleWithVector (self,V, P, C, r):
		PminusC= P[0]-C[0], P[1]-C[1], P[2]-C[2]

		a= V[0]*V[0] + V[1]*V[1] + V[2]*V[2]
		b= V[0]*2.0*PminusC[0] + V[1]*2.0*PminusC[1] + V[2]*2.0*PminusC[2]
		c= (PminusC[0]*PminusC[0] + PminusC[1]*PminusC[1] + PminusC[2]*PminusC[2]) - r*r

		sq_term= b*b-4*a*c
		if sq_term < 0.0:
			#print "Vector doesnt intersect circle"
			return P[0]+V[0], P[1]+V[1], P[2]+V[2]
		else:
			sq_term= math.sqrt(sq_term)
			t= (-b-sq_term)/(2.0*a)
			#print "Vector intersects circle at t="+`t`
			return P[0]+V[0]*t, P[1]+V[1]*t, P[2]+V[2]*t

	def Reappear (self,EntityName):
		#print "Reappearing..."
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.Enemy= Bladex.GetEntity(me.GetEnemyName())

			if me.AnimName=="g_jumpl":
				angle= -56.0/180.0 * Actions.PI
				closest_distance= Combat.GetMoveMinDist(Combat.ATTACK, ("G27",), me.AttackList)
			elif me.AnimName=="g_jumpr":
				angle=  56.0/180.0 * Actions.PI
				closest_distance= Combat.GetMoveMinDist(Combat.ATTACK, ("G22",), me.AttackList)
			else:
				angle=  0.0
				closest_distance= 3000.0
				#raise NameError, 'Reappearing in incorrect animation'
				#return
			startpos=me.Position
			enemypos= self.Enemy.Position
			SQoriginal_distance= me.SQDistance2(self.Enemy)
			teletransported= 0
			if SQoriginal_distance > closest_distance*closest_distance:
				relative_vector= -math.sin(angle), 0.0, math.cos(angle)
				DisplacementDistances= [2000.0, 1750.0, 1500.0, 1250.0, 1000.0, 750.0, 500.0, 2500.0, 3000.0, 3500.0, 4000.0]

				me.Angle=B3DLib.GetEntity2EntityAngle(me.Name, me.GetEnemyName())
				for distance in DisplacementDistances:
					position= me.Rel2AbsPoint(distance*relative_vector[0], -distance*relative_vector[2],0.0)
					newx= position[0]-enemypos[0]
					newy= position[1]-enemypos[1]
					newz= position[2]-enemypos[2]
					SQnew_distance=  newx*newx + newy*newy + newz*newz

					# set position as the intersection of circle
					if SQnew_distance < closest_distance*closest_distance:
						#pdb.set_trace()
						V= position[0]-startpos[0], position[1]-startpos[1],position[2]-startpos[2]
						position= self.IntersectCircleWithVector (V, startpos, enemypos, closest_distance)

					YOffset=1500.0
					max_fall= 1000.0
					if me.TestPos (position[0],position[1],position[2], me.ActionAreaMax, max_fall):

						if  SQnew_distance <= SQoriginal_distance:
							old_position= me.Position
							me.Position= position[0],position[1],position[2]
							old_angle= me.Angle
							me.Angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
							if me.CanISee(self.Enemy)and me.Dist2Floor<max_fall+YOffset:
								teletransported= 1
								#print "teletransported "+`distance`+" metres"
								me.SetOnFloor()
								break
							#print "cant see"
							me.Position= old_position[0], old_position[1], old_position[2]
							me.Angle= old_angle
							dist2Floor= me.Dist2Floor
						else:
							pass
							#print "further"

					elif me.TestPos (position[0],position[1]-YOffset,position[2], me.ActionAreaMax, max_fall+YOffset):

						if  SQnew_distance <= SQoriginal_distance:
							old_position= me.Position
							me.Position= position[0],position[1]-YOffset,position[2]
							old_angle= me.Angle
							me.Angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
							if me.CanISee(self.Enemy) and me.Dist2Floor<max_fall+YOffset:
								teletransported= 1
								#print "teletransported up and "+`distance`+" metres"
								me.SetOnFloor()
								break
							me.Position= old_position[0], old_position[1], old_position[2]
							me.Angle= old_angle
							dist2Floor= me.Dist2Floor

			if not teletransported:
				print "jump failed"
				me.SetOnFloor()
				pass
			# Maybe break enemies facing mode
			if self.Enemy.InCombat and self.Enemy.ActiveEnemy==me.Name and not self.Enemy.CanISee(me):
				self.Enemy.SetActiveEnemy(None)
			self.FadeIn(EntityName)
			Bladex.CheckPyErrors()
			#print "Reappeared"

	def EndZig (self,EntityName,EventName):
		#print "Ending Zig"
		# Decide to Zag if not close enough to the player, or to launch an attack
		me = Bladex.GetEntity(EntityName)
		self.Enemy= Bladex.GetEntity(me.GetEnemyName())
		enm_angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
		diff_angle= B3DLib.DiffAngle(me.Angle, enm_angle)
		if abs (diff_angle) <= Actions.PI:
			distance= math.sqrt(me.SQDistance2(self.Enemy))
			if distance > Combat.GetMoveMaxDist(Combat.ATTACK, ("G27",), me.AttackList):
				if distance > Combat.GetMoveMaxDist(Combat.ATTACK, ("ZAG",), me.AttackList):
					me.SetActiveEnemy(None)
					me.Angle= enm_angle
				else:
					if diff_angle > 0.0:
						#print "Will Zag next"
						res= me.SetNextAttack("ZAG")
					else:
						#print "Will Zig next"
						res= me.SetNextAttack("ZIG")
			else:
				#print "Cannot Zag, will attack"
				res= me.SetNextAttack("G27")
		else:
			#print "Not facing, Angle: "+`diff_angle`
			#print "Distance: "+`math.sqrt(me.SQDistance2(self.Enemy))`
			pass
		Bladex.CheckPyErrors()
		#print "Zig Ended"

	def EndZag (self,EntityName,EventName):
		#print "Ending Zag"
		# Decide to Zag if not close enough to the player, or to launch an attack
		me = Bladex.GetEntity(EntityName)
		self.Enemy= Bladex.GetEntity(me.GetEnemyName())
		enm_angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
		diff_angle= B3DLib.DiffAngle(me.Angle, enm_angle)
		if abs (diff_angle) <= Actions.PI:
			distance= math.sqrt(me.SQDistance2(self.Enemy))
			if distance > Combat.GetMoveMaxDist(Combat.ATTACK, ("G22",), me.AttackList):
				if distance > Combat.GetMoveMaxDist(Combat.ATTACK, ("ZIG",), me.AttackList):
					me.SetActiveEnemy(None)
					me.Angle= enm_angle
				else:
					if  diff_angle> 0.0:
						#print "Will Zag next"
						res= me.SetNextAttack("ZAG")
					else:
						#print "Will Zig next"
						res= me.SetNextAttack("ZIG")
			else:
				#print "Cannot Zig, will attack"
				res= me.SetNextAttack("G22")
		else:
			#print "Not facing, Angle: "+`diff_angle`
			#print "Distance: "+`math.sqrt(me.SQDistance2(self.Enemy))`
			pass
		Bladex.CheckPyErrors()
		#print "Zag Ended"

	def FirePrtlHit(self,prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			victim=Bladex.GetEntity(hit_entity)
			if victim:
				if victim.Person and not victim.Kind=="Little_Demon":
					Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,  1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Fire", +6.0]]
					victim.DamageFunc(hit_entity, self.Name, prtl_name, "Fire", 1, -1, x, y, z, 0)
					if Reference.EntitiesObjectData.has_key(prtl_name):
						del Reference.EntitiesObjectData[prtl_name]

					# Generate a smoke effect
					smoke=Bladex.CreateEntity("FireballSmoke", "Entity Particle System D1", x, y, z)
					smoke.ParticleType="DarkSmoke"
					smoke.YGravity=-3000.0
					smoke.Friction=0.05
					smoke.PPS=8
					smoke.Velocity=0.0, -80.0, 0.0
					smoke.RandomVelocity=5.0
					smoke.DeathTime=Bladex.GetTime()+0.5
					node= 0
					victim.LinkToNode(smoke,node)

					# Override hurt anim
					if victim.Life>0:
						if victim.InCombat:
							Damage.DropInvalidObjectsOnImpact (victim.Name)
							victim.Wuea=Reference.WUEA_ENDED
							victim.InterruptCombat()
							victim.LaunchAnmType("hurt_f_big")
						else:
							Damage.DropInvalidObjectsOnImpact (victim.Name)
							victim.Wuea=Reference.WUEA_ENDED
							victim.InterruptCombat()
							victim.LaunchAnmType("hurt_f_big")
				elif victim.Weapon:
					pass
		# This particle should be removed, as it has been converted to smoke
		ptcl=Bladex.GetEntity(prtl_name)
		ptcl.RemoveFromWorld()


	def SpitFunc(self, fireball_name,end_time,period):
		fireball=Bladex.GetEntity(fireball_name)
		if(fireball):
			prtl=fireball.GetParticleEntity()
			prtl.HitFunc=self.FirePrtlHit
			prtl.ObjCTest= 1
			if(Bladex.GetTime()<end_time):
				Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.SpitFunc,(fireball_name,end_time,period))

	def StartSpit (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me.InCombat:
			SQDistance= me.SQDistance2(Bladex.GetEntity(me.GetEnemyName()))
			max_firefan_dist= 4000.0

			# Get an angle to the target
			target= Bladex.GetEntity(me.GetEnemyName())
			target_pos= target.Position
			x,y,z= me.GraspPos("ViewPoint")
			angle= -B3DLib.GetYAngle(target_pos[0]-x,target_pos[1]-y,target_pos[2]-z)
			if  SQDistance < (max_firefan_dist*max_firefan_dist):
				# fan out spit
				duration= 0.3
				self.AGE_Number=self.AGE_Number+1
				end_time=Bladex.GetTime()+duration
				period= duration/10.0
				fireball=Bladex.CreateEntity(EntityName+"_Firefanl_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
				fireball.ParticleType="Flame"
				fireball.Time2Live=20
				fireball.YGravity=-500.0
				fireball.Friction=0.12
				fireball.PPS=512
				fireball.DeathTime=end_time;
				F= 7000.0             # Vector magnitude
				vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*F, -math.sin(angle)*F)
				fireball.Velocity=vx,vy,vz
				fireball.RandomVelocity=55.0
				node= me.GetNodeIndex("Head")
				me.LinkToNode(fireball,node)
			else:
				# fireball spit
				nparticles= 70
				duration= 1.0/60.0 # I think this is a minimum

				self.AGE_Number=self.AGE_Number+1
				end_time=Bladex.GetTime()+duration
				period= duration/7.0
				fireball=Bladex.CreateEntity(EntityName+"_Fireball_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
				fireball.ParticleType="LargeFire"
				fireball.Time2Live=31
				fireball.YGravity=-2400.0
				fireball.Friction=0.075
				fireball.PPS=nparticles/duration
				fireball.DeathTime=end_time;
				F= 25000.0             # Vector magnitude
				vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*F,-math.sin(angle)*F)
				fireball.Velocity=vx,vy,vz
				fireball.RandomVelocity=25.0

			self.SpitFunc(fireball.Name, end_time, period)


	def RemoveMe (self,EntityName):
		me  = Bladex.GetEntity(EntityName)
		if me:
			me.Alpha=0.0
			me.TimerFunc=""
			me.SubscribeToList("Pin")

	def DeathBall (self,EntityName):
		me  = Bladex.GetEntity(EntityName)
		if me:
			alfa=me.Angle+3.14159/2.0
			x=me.Position[0]+500.0*math.cos(alfa)
			y=me.Position[1]+250.0
			z=me.Position[2]+500.0*math.sin(alfa)
			me.RasterMode="Read"
			self.deathball_particle_system=Bladex.CreateEntity("BolaFuego", "Entity Particle System D1", x, y, z)
			self.deathball_particle_system.ParticleType="FuegoInvocacion"
			self.deathball_particle_system.PPS=250
			self.deathball_particle_system.YGravity=0.0
			self.deathball_particle_system.Friction=0.1
			self.deathball_particle_system.Velocity=0.0, 0.0, 0.0
			self.deathball_particle_system.RandomVelocity=50.0
			self.deathball_particle_system.Time2Live=40
			self.deathball_particle_system.DeathTime= Bladex.GetTime()+self.DeathBallPeriod
			self.FadeOutTime=self.DeathBallPeriod*0.8
			#pdb.set_trace()
			self.FadeOut(EntityName)

			# After the fade out, remove me from the world
			Bladex.AddScheduledFunc(Bladex.GetTime()+self.DeathBallPeriod*0.9, self.RemoveMe, (EntityName,))

	def ImplosionDemonio (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		impl=Bladex.CreateEntity("ImplosionDemonio", "Entity Particle System D1", me.Position[0], me.Position[1], me.Position[2])
		impl.ParticleType="Energia3"
		impl.YGravity=0.0
		impl.Friction=0.0
		impl.PPS=300
		impl.Velocity=0.0, 0.0, 0.0
		impl.RandomVelocity=-30.0
		impl.Time2Live=70
		impl.DeathTime=Bladex.GetTime()+(self.ImplosionPeriod*0.5)

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		me.UnlinkChildren()

		# Launch disappearing animation
		me.Wuea=Reference.WUEA_ENDED
		me.SetTmpAnmFlags(1,1,1,0,5,1)
		me.LaunchAnimation("Ldm_dth_disap")

		# Create an implosive particle system
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, self.ImplosionDemonio, (EntityName,))

		# After the implosion, create a fiery deathball
		Bladex.AddScheduledFunc(Bladex.GetTime()+self.ImplosionPeriod, self.DeathBall, (EntityName,))



	def InteruptActions(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		me.Data.Fader.Stop()
		Bladex.RemoveScheduledFunc(me.Name+" Reappear")

################################################################################

################################################################################
# Define the Troll_Dark class
################################################################################
class Troll_Dark (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosTroll(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.8
			me.AttackList = BCopy.deepcopy(Combat.TrollAttackData)
################################################################################

################################################################################
# Define the Troll_snow class
################################################################################
class Troll_snow (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init		
		Enm_Def.NPCPerson.__init__(self, me)
		
		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# Because we share biped data with the Troll_Dark, we start with the wrong mesh
		me.MeshName= 'Troll_snow'

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosTroll(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)	
		if me and me.Life>0:
			me.BlockingPropensity = 0.8
			me.AttackList = BCopy.deepcopy(Combat.TrollAttackData)

#class Troll_snow (Troll_Dark):
#	pass

################################################################################

################################################################################
# Define the Cos class
################################################################################
class Cos (Enm_Def.NPCPerson):

	HitImpulse = [0.0,0.0,0.0]
	last_hit_in_air= FALSE

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)
		me.ImDeadFunc=self.ImDeadFunc

		me.AddAnmEventFunc("CollisionsOff", self.CollisionsOff)
		me.InflictHitFunc = self.InflictHitFunc

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = -1.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 20.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0
		self.NoFXOnHit= TRUE

	# Functions for loading and saving state
	def __getstate__(self):
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Cos.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Cos"]=(self.HitImpulse,self.last_hit_in_air)

		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Cos"]
			self.HitImpulse=parms[0]
			self.last_hit_in_air=parms[1]

		me=Bladex.GetEntity(self.Name)
		#me.ImDeadFunc=self.ImDeadFunc
		#me.InflictHitFunc = self.InflictHitFunc
		me.AddAnmEventFunc("CollisionsOff", self.CollisionsOff)
		self.NoFXOnHit= TRUE

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosCosita(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=FALSE
			me.BlockingPropensity = 0.0
			me.AttackList = BCopy.deepcopy(Combat.CosAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def InflictHitFunc (self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		me.SetTmpAnmFlags(1,1,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
		me.LaunchAnmType("jmp_back1")
		# this should encourage the others to attack
		self.CallGroupMemberFunc(EntityName, Combat.TempMoveInProc, 0)
		Actions.Stop_Weapon(EntityName, "Stop_Weapon")

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		""" too slow....
		me.AddAnmEventFunc("Explode", self.Explode)
		print EntityName+": Im dead"
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		if self.last_hit_in_air:
			me.LaunchAnmType("dth_fly")
		"""
		# Do this instead...
		me.SetOnFloor()

	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz):
		Enm_Def.NPCPerson.HitFunc(self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz)
		me = Bladex.GetEntity(EntityName)
		self.HitImpulse[0]= Px*0.20;
		self.HitImpulse[1]= Py*0.20;
		self.HitImpulse[2]= Pz*0.20;
		#print EntityName+": Im hit"

		# discourage the others from attacking
		if me and me.Life>0:
			me.Data.CallGroupMemberFunc(EntityName, Combat.TempMoveOutProc, 0)

		self.last_hit_in_air= (not me.OnFloor) or me.AnimName=="g_01" or me.AnimName=="G_01"
		#self.last_hit_in_air= 1
		if self.last_hit_in_air:
			#pdb.set_trace()
			#me.Angle= B3DLib.GetEntity2EntityAngle (EntityName, "Player1")
			me.SetActiveEnemy(None)

		# launch appropriate hurt anim
		if me and me.Life > 0:
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			if self.last_hit_in_air:
				me.LaunchAnmType("fly")
				me.Angle= B3DLib.GetXZAngle(-self.HitImpulse[0], 0.0, -self.HitImpulse[2])  # Moved. Prevents them from rotating around when already dead. -LeadHead
			else:
				me.LaunchAnmType("hurt_lite")

	def CollisionsOff (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		#print "Collisions Off in animation "+me.AnimName
		enemy=Bladex.GetEntity(me.GetEnemyName())
		me.ExcludeHitInAnimationFor(enemy)  # PLAGUE: This func doesn't work. After animation ends, exclusion status is never reset
		#me.ExcludeHitFor(enemy)
		#enemy.ExcludeHitFor(me)

	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		me = Bladex.GetEntity(EntityName)

		# launch appropriate hurt anim
		if me and me.Life > 0:
			damage_factor = DamagePoints / (me.Life+DamagePoints)
			if damage_factor > self.DamageFactorNone:
				if DamageZone >= 0 and DamageZone < 32:
					me.SetWoundedZone(DamageZone, 1)

		# Consider getting furious
		if AttackerName and AttackerName != 'BWorld':
			me = Bladex.GetEntity(EntityName)
			if me and me.Life > 0:
				# consider getting furious
				if whrandom.random() < self.ChanceOfFuryOnHurt:
					self.GetFurious (EntityName)

	def Explode (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		me.DelAnmEventFunc(EventName)
		###Reference.debugprint(EntityName+": in Explode")
		#pdb.set_trace()
		# Check valid event type
		if EventName != "Explode":
			print(EntityName+":-( Explode has unhandled event")
			return

		me_pos = me.Position

		for limb_id in range (1, 6):
			limb= me.SeverLimb(limb_id)

			if limb:
				# explode outward
				limb_pos = limb.Position
				OutImpulse= B3DLib.Normalize ((limb_pos[0]-me_pos[0], limb_pos[1]-me_pos[1], limb_pos[2]-me_pos[2]))
				B3DLib.Scale (OutImpulse, 5000.0)
				limb.Impulse(OutImpulse[0], OutImpulse[1], OutImpulse[2])

				# we want backward impulse as well...  get this from the weapon
				limb.Impulse(self.HitImpulse[0], self.HitImpulse[1], self.HitImpulse[2])

################################################################################

################################################################################
# Define the Spidersmall class
################################################################################
class Spidersmall (Enm_Def.NPCPerson):

	HitImpulse = [0.0,0.0,0.0]
	last_hit_in_air= FALSE
	AGE_Number=0


	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)
		self.HitImpulse = [0.0,0.0,0.0]

		me.ImDeadFunc=self.ImDeadFunc
		me.AddAnmEventFunc("Spit", self.StartSpit)
		me.InflictHitFunc = self.InflictHitFunc

		# anims
		#me.AnmTranFunc=AuxTran.AuxTranKnightLivingDead

		# Set up specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = -1.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 20.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0


	# Functions for loading and saving state
	def __getstate__(self):
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Spidersmall.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Spidersmall"]=(self.AGE_Number,self.last_hit_in_air,self.HitImpulse)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Spidersmall"]
			self.AGE_Number=parms[0]
			self.last_hit_in_air=parms[1]
			self.HitImpulse=parms[2]

		me=Bladex.GetEntity(self.Name)
		#me.ImDeadFunc=self.ImDeadFunc
		me.AddAnmEventFunc("Spit", self.StartSpit)
		#me.InflictHitFunc = self.InflictHitFunc

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosAranita(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=FALSE
			me.BlockingPropensity = 0.0
			me.AttackList = BCopy.deepcopy(Combat.SpiderSmallAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def InflictHitFunc (self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		me = Bladex.GetEntity(EntityName)
		# this should encourage the others to attack
		me.Data.CallGroupMemberFunc(EntityName, Combat.TempMoveInProc, 0)

	def ImDeadFunc (self,EntityName):
		Reference.debugprint(EntityName+": (Spider) I died!")
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		#pdb.set_trace()
		if self.last_hit_in_air:
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			me.LaunchAnmType("dth2")

	# Overide the MutilateFunc because we don't want limbs we can pick up
	def MutilateFunc(self,EntityName,obj_name,x,y,z,nx,ny,nz,node):
		Blood.Mutilate (EntityName,obj_name,x,y,z,nx,ny,nz,node)
		limb = Bladex.GetEntity(obj_name)               #
		if limb.TestHit:                                # Added
			limb.ExclusionGroup=1                       #
			limb.Move(0, -160, 0)                       # Fixes disappearing limbs
			limb.PutToWorld()                           # PLAGUE: Needs further work to look better.
			limb.Impulse(0,0,0)                         #    -LeadHead

	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz):
		Enm_Def.NPCPerson.HitFunc(self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz)
		me = Bladex.GetEntity(EntityName)
		self.HitImpulse[0]= Px*0.20;
		self.HitImpulse[1]= Py*0.20;
		self.HitImpulse[2]= Pz*0.20;
		# print EntityName+": Im hit"

		# discourage the others from attacking
		if me and me.Life>0:
			me.Data.CallGroupMemberFunc(EntityName, Combat.TempMoveOutProc, 0)

		self.last_hit_in_air= Py<0
		if self.last_hit_in_air:
			me.Angle= B3DLib.GetXZAngle(-self.HitImpulse[0], 0.0, -self.HitImpulse[2])
			me.SetActiveEnemy(None)


	def VenomPrtlHit(self,prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			victim=Bladex.GetEntity(hit_entity)
			if victim:
				if victim.Person and not victim.Kind=="Spidersmall":
					# Need to check immunity
					me = Bladex.GetEntity(self.Name)                                                                                                                    # Now does VenomDamage
					VenomDamage= 2.0 + me.Level # Damage increases per level. -LeadHead                                                                                 #
					Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,   1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Venom", +VenomDamage]] #           -LeadHead
					victim.DamageFunc(hit_entity, self.Name, prtl_name, "Poison", 1, -1, x, y, z, 0)
					if Reference.EntitiesObjectData.has_key(prtl_name):
						del Reference.EntitiesObjectData[prtl_name]

					# Generate a smoke effect
					smoke=Bladex.CreateEntity("FuegoVerde", "Entity Particle System D1", x, y, z)
					smoke.ParticleType="VenomSmoke"
					smoke.YGravity=-100.0
					smoke.Friction=0.05
					smoke.PPS=8
					smoke.Velocity=0.0, -80.0, 0.0
					smoke.RandomVelocity=5.0
					smoke.DeathTime=Bladex.GetTime()+1.0
					node= 0
					victim.LinkToNode(smoke,node)

				elif victim.Weapon:
					pass
		# This particle should be removed, as it has been converted to smoke
		ptcl=Bladex.GetEntity(prtl_name)
		ptcl.RemoveFromWorld()


	def SpitFunc(self, venom_name,end_time,period):
		venom=Bladex.GetEntity(venom_name)
		if(venom):
			prtl=venom.GetParticleEntity()
			prtl.HitFunc=self.VenomPrtlHit
			prtl.ObjCTest= 1
			if(Bladex.GetTime()<end_time):
				Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.SpitFunc,(venom_name,end_time,period))

	def StartSpit (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		self.AGE_Number=self.AGE_Number+1
		end_time=Bladex.GetTime()+0.5
		period= 0.125
		node= 0
		x,y,z= me.GraspPos("ViewPoint")
		venom=Bladex.CreateEntity(EntityName+"_Venom_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
		venom.ParticleType="Venom"
		venom.YGravity=9800.0
		venom.Friction=0.075
		venom.PPS=512
		venom.DeathTime=end_time+1.0/60.0;
		vx,vy,vz=me.Rel2AbsVector(0,-14000.0,8500.0)        # vz was 6500.0
		venom.Velocity=vx,vy,vz
		venom.RandomVelocity=5.0
		me.LinkToNode(venom,node)

		self.SpitFunc(venom.Name, end_time, period)

	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		me = Bladex.GetEntity(EntityName)

		if me and me.Life > 0:
			damage_factor = DamagePoints / (me.Life+DamagePoints)
			if damage_factor > self.DamageFactorNone:
				if DamageZone >= 0 and DamageZone < 32:
					me.SetWoundedZone(DamageZone, 1)

		# Consider getting furious
		if AttackerName and AttackerName != 'BWorld':
			me = Bladex.GetEntity(EntityName)
			if me and me.Life > 0:
				# consider getting furious
				if whrandom.random() < self.ChanceOfFuryOnHurt:
					self.GetFurious (EntityName)

		# launch appropriate hurt anim
		if me and me.Life > 0:
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			damage_factor = DamagePoints / (me.Life+DamagePoints)
			if damage_factor > self.DamageFactorNone:
				if damage_factor < self.DamageFactorHeavy:
					me.LaunchAnmType("hurt_lite")
				else:
					me.LaunchAnmType("hurt_big")

################################################################################

################################################################################
# Define an Entity Fader class
################################################################################

class EntitiesFader(Interpolator.LinearInt):
	"Clase para hacer desaparecer una entidad"

	def __init__(self, Entities2Fade):
		Interpolator.LinearInt.__init__ (self,1.0,0.0)
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

		name= "Entity Fader for; "
		for entity_name in Entities2Fade:
			name= name+entity_name+", "
		self.Interpolator= Interpolator.Interp(name)
		self.Entities2Fade= Entities2Fade

	#def __del__(self):
	#	Interpolator.LinearInt.__del__(self)
	#	del self.Interpolator
	#	del self.Entities2Fade

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
		return (1,
			self.ObjId,
			self.Interpolator,
			self.Entities2Fade
			)

	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Interpolator=parm[2]
			self.Entities2Fade=parm[3]
			self.init_value=1.0
			self.end_value=0.0
			self.period=self.end_value-self.init_value
		else:
			print "Warning -> Version mismatch in EntitiesFader.__setstate__()"
			self.Interpolator= None
			self.Entities2Fade= None
			self.init_value=1.0
			self.end_value=0.0
			self.period=self.end_value-self.init_value

			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self

	def ExecuteFadeOut(self,value):
		#pdb.set_trace()
		ret= Interpolator.LinearInt.Execute(self,value)
		for entity_name in self.Entities2Fade:
			entity= Bladex.GetEntity(entity_name)
			if entity:
				entity.Alpha= ret

	def ExecuteFadeIn(self,value):
		ret= Interpolator.LinearInt.Execute(self,value)
		for entity_name in self.Entities2Fade:
			entity= Bladex.GetEntity(entity_name)
			if entity:
				entity.Alpha= 1.0-ret

	def FadeOut(self, period):
		self.Interpolator.Actions=[]
		self.Execute= self.ExecuteFadeOut
		time= Bladex.GetTime()
		self.Interpolator.AddAction (time,time+period,self)

	def FadeIn(self, period):
		#pdb.set_trace()
		self.Interpolator.Actions=[]
		self.Execute= self.ExecuteFadeIn
		time= Bladex.GetTime()
		self.Interpolator.AddAction (time,time+period,self)

	def Stop(self):
		self.Interpolator.Actions=[]

	def EndExecute(self):
		if self.Execute== self.ExecuteFadeIn:
			for entity_name in self.Entities2Fade:
				entity= Bladex.GetEntity(entity_name)
				if entity:
					entity.Alpha= 1.0
		elif  self.Execute== self.ExecuteFadeOut:
			for entity_name in self.Entities2Fade:
				entity= Bladex.GetEntity(entity_name)
				if entity:
					entity.Alpha= 0.0

################################################################################
# Define the Vampire class
################################################################################
class Vamp (Enm_Def.NPCPerson):


	Fader= None
	FadeOutTime= 0.45
	FadeInTime= 0.65
	TransitTime= 0.20
	Enemy=None
	EnemyAngle=0.0

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# constants
		FadeList=[me.Name]
		if Actions.StatR(me.Name)!=Actions.RA_NO_WEAPON:
			FadeList.append (me.InvRight)
		if Actions.StatL(me.Name)!=Actions.LA_NO_WEAPON:
			FadeList.append (me.InvLeft)
		self.Fader= EntitiesFader (FadeList)

		me.AddAnmEventFunc("Disappear", self.DisappearEvent)



	# Functions for loading and saving state
	def __getstate__(self):
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Vamp.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Vamp"]=(self.Enemy, self.EnemyAngle)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Vamp"]
			self.Enemy=parms[0]
			self.EnemyAngle=parms[1]

		me=Bladex.GetEntity(self.Name)
		# Create a linear interpolator for fading
		FadeList=[me.Name]
		if Actions.StatR(me.Name)!=Actions.RA_NO_WEAPON:
			FadeList.append (me.InvRight)
		if Actions.StatL(me.Name)!=Actions.LA_NO_WEAPON:
			FadeList.append (me.InvLeft)
		self.Fader= EntitiesFader (FadeList)
		self.FadeOutTime= 0.45
		self.FadeInTime= 0.65
		self.TransitTime= 0.20
		me.AddAnmEventFunc("Disappear", self.DisappearEvent)

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosVampiro(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me= Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind= FALSE
			self.AttackNPCTime= 2.0
			inv= me.GetInventory()
			if inv.HoldingShield:
				me.BlockingPropensity = 1.0
				me.RangeDefenceCapable = TRUE
			else:
				me.BlockingPropensity = 0.2
				me.RangeDefenceCapable = FALSE
			me.AttackList= BCopy.deepcopy(Combat.VampireAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath= 0.0

	def FadeOut (self,EntityName):
		self.Fader.FadeOut(self.FadeOutTime)

	def FadeIn (self,EntityName):
		self.Fader.FadeIn(self.FadeInTime)

	def DisappearEvent (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		# May wish to make all attacks pass through...
		self.FadeOut(EntityName)
		time= Bladex.GetTime()
		Bladex.AddScheduledFunc(time+self.FadeOutTime+self.TransitTime, self.Reappear, (EntityName,), EntityName+" Reappear")
		if Actions.StatR(EntityName)!=Actions.RA_NO_WEAPON:
			weapon= Bladex.GetEntity(me.InvRight)
			weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
			weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)

	def Disappear (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		forgetit= (me.Life*2.0)/CharStats.GetCharMaxLife(me.Kind, me.Level)
		if whrandom.random()>forgetit:# or not Actions.IsFacingEntity(me.GetEnemyName(), EntityName):
			me.SetNextAttack("disappear")
			return 1
		return 0


	def RelativeEnemyAngle2PositionAngleTuple (self, angle):
		angle= angle+self.EnemyAngle
		# Compensate for non forward attack
		#angle= angle - (25.0/360.0)*Actions.TWOPI

		if angle > Actions.PI*2.0:
			angle= angle-Actions.TWOPI
		elif angle < 0.0:
			angle= angle+Actions.TWOPI

		# What distance to use?
		pos= self.Enemy.Position
		dist= 1400
		pos= pos[0]+dist*math.sin(angle), pos[1], pos[2]-dist*math.cos(angle)
		return (pos, angle)

	def Reappear (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		# Find a suitable position to reappear in
		if whrandom.random() < 0.5:
			RelAngles=[0, Actions.PI*0.25, Actions.PI*-0.25, Actions.PI*0.5, Actions.PI*-0.5, Actions.PI*0.75, Actions.PI*-0.75]
		else:
			RelAngles=[0, Actions.PI*-0.25, Actions.PI*0.25, Actions.PI*-0.5, Actions.PI*0.5, Actions.PI*-0.75, Actions.PI*0.75]
		#pdb.set_trace()
		self.Enemy= Bladex.GetEntity(me.GetEnemyName())
		self.EnemyAngle= self.Enemy.Angle
		ReentryInfo= map(self.RelativeEnemyAngle2PositionAngleTuple, RelAngles)

		# Add current position, unnecessary
		#ReentryInfo.append ((me.Position, me.Angle))

		max_fall= 1000.0
		for info in ReentryInfo:
			if me.TestPos (info[0][0],info[0][1],info[0][2], me.ActionAreaMax,max_fall):
				me.Position= info[0][0],info[0][1],info[0][2]
				me.Angle= info[1]
				me.SetOnFloor()
				break

		# Maybe break enemies facing mode
		if self.Enemy.InCombat and self.Enemy.ActiveEnemy==me.Name and not self.Enemy.CanISee(me):
			self.Enemy.SetActiveEnemy(None)
		self.FadeIn(EntityName)
		if Actions.StatR(EntityName)!=Actions.RA_NO_WEAPON:
			#Bladex.GetEntity(me.InvRight).MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)
			dice= whrandom.random()
			if dice<0.2:
				me.SetNextAttack("g_01")
			elif dice<0.4:
				me.SetNextAttack("g_06")
			elif dice<0.6:
				me.SetNextAttack("g_07")
			elif dice<0.8:
				me.SetNextAttack("g_26")


	def InteruptActions(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		me.Data.Fader.Stop()
		Bladex.RemoveScheduledFunc(me.Name+" Reappear")

################################################################################

################################################################################
# Define the Lich class
################################################################################
class Lich (Enm_Def.NPCPerson):


	# Set up some mutilation constants
	RightFoot= 512
	RightLeg= 256
	LeftFoot= 128
	LeftLeg= 64
	RightHand= 32
	RightArm= 16
	LeftHand= 8
	LeftArm= 4
	Head= 2
	LegBits= RightFoot | RightLeg | LeftFoot | LeftLeg
	RArmAble= RightHand | RightArm
	LArmAble= LeftHand | LeftArm

	LastMutilationsMask=0
	AGE_Number=0


	def __init__(self, me):

		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		self.LastMutilationsMask= me.MutilationsMask

		self.DamageFactorLight = 0.25
		self.DamageFactorHeavy = 0.25
		# Set up sounds made
		me.ImDeadFunc=self.ImDeadFunc
		me.AddAnmEventFunc("Spit", self.StartSpit)
		self.NoFXOnHit= TRUE

	# Functions for loading and saving state
	def __getstate__(self):
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Knight_Traitor.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Lich"]=(self.AGE_Number,)

		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		# Set up some mutilation constants
		self.RightFoot= 512
		self.RightLeg= 256
		self.LeftFoot= 128
		self.LeftLeg= 64
		self.RightHand= 32
		self.RightArm= 16
		self.LeftHand= 8
		self.LeftArm= 4
		self.Head= 2
		self.LegBits= self.RightFoot | self.RightLeg | self.LeftFoot | self.LeftLeg
		self.RArmAble= self.RightHand | self.RightArm
		self.LArmAble= self.LeftHand | self.LeftArm

		Enm_Def.NPCPerson.__setstate__(self,parm)

		me=Bladex.GetEntity(self.Name)

		# the following should be saved when mutilations can be saved and loaded
		self.LastMutilationsMask=me.MutilationsMask
		self.NoFXOnHit= TRUE

		version=parm[0]
		if version==1:
			parms=parm[1]["Lich"]
			self.AGE_Number= parms[0]

		#me.ImDeadFunc=self.ImDeadFunc
		me.AddAnmEventFunc("Spit", self.StartSpit)

	def ResetSounds(self, EntityName):
		me = Bladex.GetEntity(EntityName)
		if me.Kind=="Lich":
			AniSound.AsignarSonidosLich(me.Name)
		elif me.Kind=="Knight_Zombie":
			AniSound.AsignarSonidosZombie(me.Name)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=FALSE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.0
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.00
			me.AttackList = BCopy.deepcopy(Combat.LichAttackData)
			MutilationsMask= me.MutilationsMask

			# Are we on the ground...
			#pdb.set_trace()
			if MutilationsMask & self.LegBits:
				# Only allow spit from ground
				me.AttackList.append ([Combat.ATTACK, 0.05, ("SP2",),               0.0, 3000.0, 4000.0, 6.00])
				Combat.SetCombatMoveProbability (Combat.ATTACK, 0.02, me.AttackList)

				#If we have arms, we can move on the ground,

				# No arms, no move, just spit fiercely
			else:
				# Allow spit
				me.AttackList.append ([Combat.ATTACK, 0.05, ("SP1",),             750.0, 3000.0, 4000.0, 3.00])

				# Can we use the right hand
				if MutilationsMask & self.RArmAble==0:
					# Are we carrying a weapon?
					if Actions.StatR(me.Name)!=Actions.RA_NO_WEAPON:
						me.AttackList.append ([Combat.ATTACKDOWN, 1.00, ("G18",),        2610.0, 3109.0, 3608.0, 0.35])

						me.AttackList.append ([Combat.ATTACK, 0.35, ("G12",),            2610.0, 3109.0, 3608.0, 0.35])
						me.AttackList.append ([Combat.ATTACK, 0.20, ("G13",),            1526.0, 1831.0, 2136.0, 0.35])
						me.AttackList.append ([Combat.ATTACK, 0.35, ("G16",),             750.0, 1610.0, 1965.0, 0.35])
						me.AttackList.append ([Combat.ATTACK, 0.20, ("G18",),            2418.0, 2763.0, 3108.0, 0.35])
					else:
						me.AttackList.append ([Combat.ATTACKDOWN, 1.00, ("C3",),         1000.0, 2195.0, 2356.0, 0.35])

						me.AttackList.append ([Combat.ATTACK, 0.10, ("C1",),             1000.0, 2195.0, 2261.0, 0.35])
						me.AttackList.append ([Combat.ATTACK, 0.05, ("C3",),             1000.0, 2195.0, 2356.0, 0.35])
				if MutilationsMask & self.LArmAble==0:
					if Actions.StatL(me.Name)==Actions.LA_NO_WEAPON:
						me.AttackList.append ([Combat.ATTACK, 0.10, ("C2",),             1596.0, 2105.0, 2220.0, 0.35])
						me.AttackList.append ([Combat.ATTACK, 0.05, ("C3",),             1000.0, 2195.0, 2356.0, 0.35])

				Combat.SetCombatMoveProbability (Combat.ATTACK, 0.5, me.AttackList)

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		enemy=Bladex.GetEntity(me.GetEnemyName())                                                       ### We're doing this to avoid getting stuck in dead corpses
		me.ExcludeHitInAnimationFor(enemy)                                                              ### While they're flailing about -LeadHead
		print "El lich se convertira en polvo"
		Bladex.AddScheduledFunc(Bladex.GetTime()+10, dust.EnPolvoPerson,(EntityName,100,0,))

	def MutilateFunc(self,EntityName,obj_name,x,y,z,nx,ny,nz,node):
		Blood.Mutilate (EntityName,obj_name,x,y,z,nx,ny,nz,node)
		limb= Bladex.GetEntity(obj_name)
		InitDataField.Initialise(limb)
        ### Disable collisions for limbs, otherwise they trigger TestHit on mutilations while still alive - LeadHead
        ### This is not a big deal, since the limbs will turn to dust in 10seconds anyway.
		limb.ExclusionGroup=1
		if limb.TestHit:                                
			limb.Move(0, -160, 0)                       # Fixes disappearing limbs
			limb.PutToWorld()                           # 
			limb.Impulse(0,0,0)                         #    -LeadHead

		Bladex.AddScheduledFunc(Bladex.GetTime()+10, dust.EnPolvoObjeto,(obj_name,100,0,))

	def VomitPrtlHit(self,prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			victim=Bladex.GetEntity(hit_entity)
			if victim:
				if victim.Person and not victim.Kind=="Lich":
					me = Bladex.GetEntity(self.Name)
					VmtDamage= 2.0 + me.Level #Since Python starts counting from 0, level 1 lch and zkn will do exactly 2 venom damage as in original game. -LeadHead
					# Need to check immunity ## Do we?
					Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,  1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Venom", +VmtDamage]] ### Now does VmtDamage -LeadHead
					victim.DamageFunc(hit_entity, self.Name, prtl_name, "Vomit", 1, -1, x, y, z, 0)
					if Reference.EntitiesObjectData.has_key(prtl_name):
						del Reference.EntitiesObjectData[prtl_name]
				elif victim.Weapon:
					pass
		# This particle should be removed, as it has collided
		ptcl=Bladex.GetEntity(prtl_name)
		ptcl.RemoveFromWorld()
        

	def SpitFunc(self, vomit_name,end_time,period):
		vomit=Bladex.GetEntity(vomit_name)
		if(vomit):
			prtl=vomit.GetParticleEntity()
			prtl.HitFunc=self.VomitPrtlHit
			prtl.ObjCTest= 1
			if(Bladex.GetTime()<end_time):
				Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.SpitFunc,(vomit_name,end_time,period))

	def StartSpit (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		self.AGE_Number=self.AGE_Number+1
		end_time=Bladex.GetTime()+0.5
		period= 0.125
		node= me.GetNodeIndex("Head")
		x,y,z= me.GraspPos("ViewPoint")
		vomit=Bladex.CreateEntity(EntityName+"_Vomit_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
		vomit.ParticleType="Vomit"
		vomit.YGravity=9800.0
		vomit.Friction=0.075
		vomit.PPS=512
		vomit.DeathTime=end_time+1.0/60.0;
		vx,vy,vz=me.Rel2AbsVector(0,-9000.0,6500.0)
		vomit.Velocity=vx,vy,vz
		vomit.RandomVelocity=5.0
		me.LinkToNode(vomit,node)

		self.SpitFunc(vomit.Name, end_time, period)

	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		Enm_Def.NPCPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)
		me = Bladex.GetEntity(EntityName)

		#pdb.set_trace()
		if DamageType == "Slash" and DamagePoints > CharStats.GetCharMaxLife(me.Kind, me.Level) * 0.08:
			# Chance of mutilation
			if DamageZone!= Reference.BODY_RLEG and DamageZone!= Reference.BODY_LLEG and DamageZone!= Reference.BODY_RFOOT and DamageZone!= Reference.BODY_LFOOT:
				if DamageZone==Reference.BODY_HEAD:
					me.Data.Mutilate= DamagePoints>=me.Life
				else:
					me.Data.Mutilate= TRUE
		"""
		if me.Life>0 and me.MutilationsMask & self.LegBits:
			Reference.debugprint("Launching hurt_drag")
			Damage.DropInvalidObjectsOnImpact (EntityName)
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			print "Dragging"
			me.LaunchAnmType("hurt_drag")
		"""

	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz):
		Enm_Def.NPCPerson.HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, Px, Py, Pz,wcx,wcy,wcz,wdx,wdy,wdz)
		me = Bladex.GetEntity(EntityName)
		NewMutilation= me.MutilationsMask - self.LastMutilationsMask
		if NewMutilation:
			#pdb.set_trace()
			""" commented until i work on lich again
			if NewMutilation==self.RightHand:
				print "RightHand"
			elif NewMutilation==self.RightArm:
				print "RightArm"
			elif NewMutilation==self.LeftHand:
				print "LeftHand"
			elif NewMutilation==self.LeftArm:
				print "LeftArm"
			elif NewMutilation==self.RightFoot:
				print "RightFoot"
			elif NewMutilation==self.RightLeg:
				print "RightLeg"
			elif NewMutilation==self.LeftFoot:
				print "LeftFoot"
			elif NewMutilation==self.LeftLeg:
				print "LeftLeg"
			elif NewMutilation==self.Head:
				print "Head"
			else:
				print "Unidentified"
			"""
			self.LastMutilationsMask= me.MutilationsMask

			if NewMutilation & (self.Head|self.RightFoot|self.RightLeg|self.LeftFoot|self.LeftLeg):
				if me.Life>0:
					me.Life= 0
					if WeaponName:
						weapon=Bladex.GetEntity(WeaponName)
						if weapon:
							if weapon.Person:
								AttackerEntity= weapon
							elif weapon.Parent:
								AttackerEntity= Bladex.GetEntity(weapon.Parent)
							elif weapon.Data:
								try:                                                                    # Bugfix. If mutilation is done by a thrown weapon,
									if weapon.Data.ThrownBy:                                            # previously would fail to trigger OnKilledEnemy func
										AttackerEntity= weapon.Data.ThrownBy                            # like awarding experience              
								except:                                                                 #
									AttackerEntity= None                                                #                                   -LeadHead
							else:
								AttackerEntity= None
							if AttackerEntity and AttackerEntity.Person:
								AttackerEntity.Data.OnKilledEnemy(EntityName)
			elif NewMutilation==self.RightHand or NewMutilation==self.RightArm:
				object = Bladex.GetEntity(me.InvRight)
				if me.InvRight and object:
					Actions.RemoveFromInventory (me, object,"DropRightEvent")
					object.Impulse(0.0, 0.0, 0.0)
					if object.TestHit:
						object.RemoveFromWorld()
				object = Bladex.GetEntity(me.InvLeft)
				if me.InvLeft and object:
					Actions.RemoveFromInventory (me, object,"DropLeftEvent")
					object.Impulse(0.0, 0.0, 0.0)
					if object.TestHit:
						object.RemoveFromWorld()

			elif NewMutilation==self.LeftHand or NewMutilation==self.LeftArm:
				object = Bladex.GetEntity(me.InvLeft)
				if me.InvLeft and object:
					Actions.RemoveFromInventory (me, object,"DropLeftEvent")
					object.Impulse(0.0, 0.0, 0.0)
					if object.TestHit:
						object.RemoveFromWorld()

			self.ResetCombat (EntityName)

################################################################################
# Define the Knight_Zombie class
################################################################################
class Knight_Zombie (Lich):
	pass

################################################################################

################################################################################
# Define the Minotaur class
################################################################################
class Minotaur (Enm_Def.NPCPerson):
	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0
		self.DamageFactorNone  = 0.25
		self.DamageFactorLight = 0.33
		self.DamageFactorHeavy = 0.5

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosMinotaur(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.6
			me.AttackList = BCopy.deepcopy(Combat.MinotaurAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

################################################################################
# Define the Salamander class
################################################################################
class Salamander (Enm_Def.NPCPerson):
	# variables
	AGE_Number=0


	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# constants
		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25

		me.AddAnmEventFunc("Spit", self.StartSpit)

	# Functions for loading and saving state
	def __getstate__(self):
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Salamander.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["Salamander"]=(self.AGE_Number,)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Salamander"]
			self.AGE_Number=parms[0]
		me=Bladex.GetEntity(self.Name)
		me.AddAnmEventFunc("Spit", self.StartSpit)

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosSalamander(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.2
			me.AttackList = BCopy.deepcopy(Combat.SalamanderAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def FirePrtlHit(self,prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			victim=Bladex.GetEntity(hit_entity)
			if victim:
				if victim.Person and not victim.Kind=="Salamander":
					Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,   1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Fire", +6.0]]
					victim.DamageFunc(hit_entity, self.Name, prtl_name, "Fire", 1, -1, x, y, z, 0)
					if Reference.EntitiesObjectData.has_key(prtl_name):
						del Reference.EntitiesObjectData[prtl_name]

					# Generate a smoke effect
					smoke=Bladex.CreateEntity("FireballSmoke", "Entity Particle System D1", x, y, z)
					smoke.ParticleType="DarkSmoke"
					smoke.YGravity=-3000.0
					smoke.Friction=0.05
					smoke.PPS=8
					smoke.Velocity=0.0, -80.0, 0.0
					smoke.RandomVelocity=5.0
					smoke.DeathTime=Bladex.GetTime()+0.5
					node= 0
					victim.LinkToNode(smoke,node)

					# Override hurt anim
					if victim.Life>0:
						Damage.DropInvalidObjectsOnImpact (victim.Name)
						victim.Wuea=Reference.WUEA_ENDED
						if victim.InCombat:
							victim.InterruptCombat()
							victim.LaunchAnmType("hurt_f_big")
						else:
							victim.LaunchAnmType("hurt_f_big")
				elif victim.Weapon:
					pass
		# This particle should be removed, as it has been converted to smoke
		ptcl=Bladex.GetEntity(prtl_name)
		ptcl.RemoveFromWorld()


	def SpitFunc(self, fireball_name,end_time,period):
		fireball=Bladex.GetEntity(fireball_name)
		if(fireball):
			prtl=fireball.GetParticleEntity()
			prtl.HitFunc=self.FirePrtlHit
			prtl.ObjCTest= 1
			if(Bladex.GetTime()<end_time):
				Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.SpitFunc,(fireball_name,end_time,period))

	def StartSpit (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me.InCombat:
			SQDistance= me.SQDistance2(Bladex.GetEntity(me.GetEnemyName()))
			max_firefan_dist= 4000.0

			# Get an angle to the target
			target= Bladex.GetEntity(me.GetEnemyName())
			target_pos= target.Position
			x,y,z= me.GraspPos("ViewPoint")
			angle= -B3DLib.GetYAngle(target_pos[0]-x,target_pos[1]-y,target_pos[2]-z)

			if  SQDistance < (max_firefan_dist*max_firefan_dist):
				# fan out spit
				duration= 0.3
				self.AGE_Number=self.AGE_Number+1
				end_time=Bladex.GetTime()+duration
				period= duration/10.0
				fireball=Bladex.CreateEntity(EntityName+"_Firefanl_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
				fireball.ParticleType="Flame"
				fireball.Time2Live=20
				fireball.YGravity=-4900.0
				fireball.Friction=0.12
				fireball.PPS=512
				fireball.DeathTime=end_time;
				F= 5400.0             # Vector magnitude
				vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*F, -math.sin(angle)*F)
				fireball.Velocity=vx,vy,vz
				fireball.RandomVelocity=55.0
				self.SpitFunc(fireball.Name, end_time, period)
			else:
				# fireball spit
				nparticles= 70
				duration= 2.0/60.0 # I think this is a minimum
				self.AGE_Number=self.AGE_Number+1
				end_time=Bladex.GetTime()+duration
				period= duration/7.0
				fireball=Bladex.CreateEntity(EntityName+"_Fireball_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
				fireball.ParticleType="LargeFire"
				fireball.Time2Live=30
				fireball.YGravity=-400.0
				fireball.Friction=0.075
				fireball.PPS=nparticles/duration
				fireball.DeathTime=end_time;
				F= 25000.0             # Vector magnitude
				vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*F, -math.sin(angle)*F)
				fireball.Velocity=vx,vy,vz
				fireball.RandomVelocity=15.0
				self.SpitFunc(fireball.Name, end_time, period)

################################################################################
################################################################################
# Define the Great_Demon class
################################################################################
class Great_Demon (Enm_Def.NPCPerson):

	# constants
	LevelUpTime=0.5
	ImplosionPeriod = 2.5
	DeathBallPeriod = 3.5


	ShieldIntensityMax= 8.0
	ShieldLife= 10000.0

	Fader= None
	FadeOutTime= 0.23333
	FadeInTime= 0.23333
	TransitTime= 0.0

	# variables
	Flame= None
	AGE_Number=0
	Phase= 1
	shield_light= None
	shield_particle_system= None
	LifeUpCalled=0

	back_aura=None
	front_aura=None

	GDLevelUpParticleData=[]

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25
		self.DamageFactorHeavy = 0.35

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		me.AddAnmEventFunc("Spit", self.StartSpit)
		me.AddAnmEventFunc("Stop_Spit", self.StopSpit)
		me.AddAnmEventFunc("Quake", self.Quake)
		me.AddAnmEventFunc("MagicAttackStart", self.MagicAttackStart)
		me.AddAnmEventFunc("MagicAttackLink", self.MagicAttackLink)
		me.ImDeadFunc=self.ImDeadFunc

		# Create a linear interpolator for fading
		FadeList=[me.Name]
		self.Fader= EntitiesFader (FadeList)

		pos= me.Position

		# variables
		self.shield_light= Bladex.CreateEntity(me.Name+" demonic shield light", "Entity Spot", pos[0], pos[1], pos[2])
		me.LinkToNode(self.shield_light,0)
		self.shield_light.Color= 80, 100, 255
		self.shield_light.Intensity= 0.0
		self.shield_light.Precission= 0.03125
		self.shield_light.Visible= 0
		self.shield_light.CastShadows= 0

		# more constants
		self.back_aura= Bladex.CreateEntity(me.Name+"_BackAura","Entity Aura",pos[0],pos[1],pos[2])
		self.front_aura= Bladex.CreateEntity(me.Name+"_FrontAura","Entity Aura",pos[0],pos[1],pos[2])
		self.SetAuraIntensity()
		me.Link(self.back_aura)
		me.Link(self.front_aura)
		self.back_aura.SetAuraGradient(2,  0.0, 0.0, 1.0, 0.3, 0.6, 1.0, 1.0, 1.0, 0.0, 1.0)
		self.front_aura.SetAuraGradient(2,  0.0, 0.0, 1.0, 0.1, 0.0  , 1.0, 1.0, 1.0, 0.0, 1.0)
		self.back_aura.SetAuraActive(0)
		self.front_aura.SetAuraActive(0)

		# New data, must be saved and loaded
		self.RingName=""

		Bladex.CreateTimer("Timer8",1.0/8.0)
		me.Level= 6
		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
		me.Alpha= 0.85

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
			size=300.0*aux
			self.GDLevelUpParticleData.append(a)
			self.GDLevelUpParticleData.append(size)
			Bladex.SetParticleGVal("GDLevelUpParticle",i,r,g,b,a,size)


	# Functions for loading and saving state
	def __getstate__(self):
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Great_Demon.__getstate__(): Base class version differs."
			return NPCPerson_state

		shield_light_Name=""
		if self.shield_light:
			shield_light_Name=self.shield_light.Name

		shield_particle_system_Name=""
		if self.shield_particle_system:
			shield_particle_system_Name=self.shield_particle_system.Name

		NPCPerson_state[1]["Great_Demon"]=(self.Flame,
						self.AGE_Number,
						self.Phase,
						shield_light_Name,
						shield_particle_system_Name,
						self.LifeUpCalled,
						self.RingName)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase

		Enm_Def.NPCPerson.__setstate__(self,parm)

		shield_light_Name=""
		shield_particle_system_Name=""
		me=Bladex.GetEntity(self.Name)
		version=parm[0]
		if version==1:
			parms=parm[1]["Great_Demon"]
			self.Flame=parms[0]
			self.AGE_Number=parms[1]
			self.Phase=parms[2]

			shield_light_Name= parms[3]
			shield_particle_system_Name=parms[4]
			self.LifeUpCalled=parms[5]
			self.RingName=parms[6]

			self.shield_light=Bladex.GetEntity(shield_light_Name)
			self.shield_particle_system=Bladex.GetEntity(shield_particle_system_Name)

			# constants
			self.LevelUpTime=0.5
			self.ImplosionPeriod = 2.5
			self.DeathBallPeriod = 3.5
			self.LifeUpCalled=0
			me.AddAnmEventFunc("Spit", self.StartSpit)
			me.AddAnmEventFunc("Stop_Spit", self.StopSpit)
			me.AddAnmEventFunc("Quake", self.Quake)
			me.AddAnmEventFunc("MagicAttackStart", self.MagicAttackStart)
			me.AddAnmEventFunc("MagicAttackLink", self.MagicAttackLink)
			#me.ImDeadFunc=self.ImDeadFunc
			self.ShieldIntensityMax= 8.0
			self.ShieldLife= 10000.0

			# Create a linear interpolator for fading
			FadeList=[me.Name]
			self.Fader= EntitiesFader (FadeList)
			self.FadeOutTime= 0.23333
			self.FadeInTime= 0.23333
			self.TransitTime= 0.0

			pos= me.Position
			self.back_aura= Bladex.GetEntity(me.Name+"_BackAura")
			self.front_aura= Bladex.GetEntity(me.Name+"_FrontAura")
			self.SetAuraIntensity()
			self.back_aura.SetAuraGradient(2,  0.0, 0.0, 1.0, 0.3, 0.6, 1.0, 1.0, 1.0, 0.0, 1.0)
			self.front_aura.SetAuraGradient(2,  0.0, 0.0, 1.0, 0.1, 0.0  , 1.0, 1.0, 1.0, 0.0, 1.0)
			self.back_aura.SetAuraActive(0)
			self.front_aura.SetAuraActive(0)
			Bladex.CreateTimer("Timer8",1.0/8.0)
			me.Alpha= 0.85

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
			size=300.0*aux
			self.GDLevelUpParticleData.append(a)
			self.GDLevelUpParticleData.append(size)
			Bladex.SetParticleGVal("GDLevelUpParticle",i,r,g,b,a,size)


	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosGreatDemon(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.2
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.00
			me.AttackList = BCopy.deepcopy(Combat.GreatDemonAttackData)
			if self.Phase>1 and self.LifeUpCalled:
				me.AttackList.append([Combat.ATTACK,  0.03, ("g_quake",),       1000.0, 7000.0, 9000.0, 0.50],)

	def EndPhase1 (self,EntityName):	# Call this for appearance in the House of the Lord of Chaos
		if self.Phase<2:
			me = Bladex.GetEntity(EntityName)
			self.Phase= 2
			me.Level= 9
			me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
			self.ResetCombat (EntityName)

	########################################################################
	#____ EARTHQUAKE FUNCS _________________________________________________
	########################################################################
	def ContinueQuake(self, Interval, Delta):
		cam= Bladex.GetEntity("Camera")
		cam.EarthQuakeFactor= cam.EarthQuakeFactor-Delta
		if cam.EarthQuakeFactor > 0.0:
			Bladex.AddScheduledFunc(Bladex.GetTime()+Interval,self.ContinueQuake,(Interval, Delta))
		else:
			cam.EarthQuake=FALSE

	def Quake (self,EntityName,EventName):
		QuakeRange= 35000.0
		me=Bladex.GetEntity(EntityName)
		cam= Bladex.GetEntity("Camera")
		mp=me.GraspPos ("Earthquake")

		# Shake up physical objects around
		objects_in_range= Bladex.GetEntitiesAt(mp[0], mp[1], mp[2],QuakeRange)
		impulse= 40000.0
		for obj_name in objects_in_range:
			object= Bladex.GetEntity(obj_name)
			if (object.Physic or object.Weapon) and not object.Parent:
				op= object.Position;
				x= op[0]-mp[0]; y= op[1]-mp[1]; z= op[2]-mp[2]
				dist= ((x**2.0) + (y**2.0) + (z**2.0))**0.5
				x,y,z= B3DLib.Normalize((x,y-500.0,z))
				factor= ((QuakeRange-dist)/QuakeRange) * impulse
				object.Impulse(x*factor, y*factor,z*factor)
				if AuxFuncs.GetSpot(object):
					object.OnStopFunc= OnOff.TurnOffLight
		# shake up the player
		victim=Bladex.GetEntity(me.GetEnemyName())
		if victim and victim.Life>0:
			vp= victim.Position
		else:
			vp= cam.Position
		distance= math.sqrt(((mp[0]-vp[0])*(mp[0]-vp[0]))+((mp[1]-vp[1])*(mp[1]-vp[1]))+((mp[2]-vp[2])*(mp[2]-vp[2])))
		severity=max(0.0, 1.0 - distance/QuakeRange)

		cam.EarthQuakeFactor=120.0 * severity
		cam.EarthQuake=TRUE
		QuakeTime= 1.5
		Interval= 0.25
		Delta= cam.EarthQuakeFactor/ (QuakeTime/Interval)
		Bladex.AddScheduledFunc(Bladex.GetTime()+Interval,self.ContinueQuake,(Interval, Delta))

		if victim and victim.Life>0:
			Damage.DropInvalidObjectsOnImpact (victim.Name)
			victim.Wuea=Reference.WUEA_ENDED
			victim.InterruptCombat()
			if victim.Block:
				if severity<0.5:
					victim.LaunchAnmType("df_01")
				else:
					victim.LaunchAnmType("df_02")
			else:
				if severity<0.5:
					victim.LaunchAnmType("hurt_f_lite")
				else:
					victim.LaunchAnmType("hurt_f_big")
				# Drop weapons
				if whrandom.random() < severity*0.5:
					object = Bladex.GetEntity(victim.InvLeft)
					if victim.InvLeft and object and not object.TestHit:
						Actions.DropReleaseEventHandler(victim.Name, "DropLeftEvent", FALSE)
						#Actions.RemoveFromInventory (victim, object,"DropLeftEvent")
						#object.Impulse(0.0, 1.0, 0.0)

				if whrandom.random() < severity*0.5:
					object = Bladex.GetEntity(victim.InvRight)
					if victim.InvRight and object and not object.TestHit:
						Actions.DropReleaseEventHandler(victim.Name, "DropRightEvent", FALSE)
						#Actions.RemoveFromInventory (victim, object,"DropRightEvent")
						#object.Impulse(0.0, 1.0, 0.0)



	########################################################################
	#____ MAGIC ATTACK FUNCS _______________________________________________
	########################################################################
	def MagicAttackStart (self, EntityName, EventName):
		me= Bladex.GetEntity(EntityName)
		print "MagicAttackStart "
		# enable damage

		# turn off claw damage with a scheduled func after concentration is complete
		MagicStopPos= 0.509
		anm_duration= Bladex.GetAnimationDuration("Gdm_g_magic")
		DeathTime= Bladex.GetTime()+max((MagicStopPos-me.AnmPos)*anm_duration, 0.0)
		period=0.001

		x,y,z= me.GraspPos("1H_L")
		lball=Bladex.CreateEntity(self.Name+"_Fire","Entity Particle System D1",x,y,z)
		lball.ParticleType="Flame"
		lball.PPS=256
		lball.YGravity=-300.0
		lball.Friction=0.04
		lball.RandomVelocity=-30.0
		lball.DeathTime= DeathTime
		lball.Time2Live=20
		me.LinkToNode(lball, me.GetNodeIndex("L_Hand"))
		self.lballname= lball.Name
		self.CreateTestParticle(lball.Name, DeathTime, period)

		x,y,z= me.GraspPos("1H_R")
		rball=Bladex.CreateEntity(self.Name+"_Fire","Entity Particle System D1",x,y,z)
		rball.ParticleType="Flame"
		rball.PPS=256
		rball.YGravity=-300.0
		rball.Friction=0.04
		rball.RandomVelocity=-30.0
		rball.DeathTime= DeathTime
		rball.Time2Live=20
		me.LinkToNode(rball, me.GetNodeIndex("R_Forearm"))
		self.rballname= rball.Name
		self.CreateTestParticle(rball.Name, DeathTime, period)

	def MagicAttackLink (self, EntityName, EventName):
		# Create a ring of fire radiating from the floor below the demon
		me= Bladex.GetEntity(EntityName)

		# Turn off the flame around the hands
		lball= Bladex.GetEntity(self.lballname)
		if lball: lball.DeathTime= Bladex.GetTime()
		rball= Bladex.GetEntity(self.rballname)
		if rball: rball.DeathTime= Bladex.GetTime()

		# Create the firering
		obj=Bladex.CreateEntity(EntityName+"_Disk", "FireRing", 0,0,0)
		obj.Alpha=1.0
		obj.SelfIlum=1.0
		obj.RasterMode="AdditiveAlpha"
		obj.RasterMode="Read"
		obj.Solid= 0

		# Set position & orientation
		me.LinkAnchors("FireRing",obj,"FireRing")
		me.Unlink(obj)
		self.RingName= obj.Name

		TurnOffAfter= 0.4
		AuxFuncs.FadeAndScale(obj.Name, obj.Position, 1.0, 0.0, 0.0, 1.0, 8.0, 0.0, TurnOffAfter, 1, 0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+TurnOffAfter,self.EndOfRingAttack,(EntityName, EventName),"EndOfRingAttack")

		"""
		# Create flame particle system, for collision detection
		period=0.001
		nparticles=10
		effect=Bladex.CreateEntity(obj.Name+"_Fire","Entity Particle System Dobj", 0, 0, 0)
		effect.ObjectName=obj.Name
		effect.ParticleType="LargeFlame"
		effect.YGravity=-12000.0
		effect.Friction=0.1
		#effect.PPS=512
		effect.PPS=32 # not using the visual effect really, real PPS is nparticles/period (10,000)
		effect.RandomVelocity=50.0
		effect.Velocity=0.0, -2000.0, 0.0
		self.RingPSName= effect.Name
		for i in range(nparticles):
			self.CreateTestParticle(effect.Name, Bladex.GetTime()+TurnOffAfter, period)
		"""


	def EndOfRingAttack (self, EntityName, EventName):
		obj= Bladex.GetEntity(self.RingName)
		if obj:
			me= Bladex.GetEntity(EntityName)
			if me:
				enemy= Bladex.GetEntity(me.GetEnemyName())
				if enemy and enemy.Life>0:
					distSQ= me.SQDistance2(enemy)
					#if distSQ<64000000.0:
					if distSQ<49000000.0:
						# inflict damage
						xhit_point, yhit_point, zhit_point= enemy.Position
						enemy.DamageFunc(enemy.Name, EntityName, self.RingName, "Fire", 1, -1, xhit_point, yhit_point, zhit_point, 0)
						# Override hurt anim
						if enemy.Life>0:
							Damage.DropInvalidObjectsOnImpact (enemy.Name)
							enemy.Wuea=Reference.WUEA_ENDED
							enemy.InterruptCombat()
							if enemy.InCombat: enemy.LaunchAnmType("hurt_f_big")
							else: enemy.LaunchAnmType("hurt_f_big")
			# destroy ring
			obj.SubscribeToList("Pin")


	########################################################################
	#____ FIRE SPITTING FUNCS ______________________________________________
	########################################################################
	def FirePrtlHit(self,prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			victim=Bladex.GetEntity(hit_entity)
			if victim:
				if victim.Person and not victim.Kind=="Great_Demon":
					Reference.EntitiesObjectData[prtl_name]= [Reference.OBJ_WEAPON, 0, 0,  1.0,  Reference.THR_STRAIGHT, Reference.W_FLAG_1H, ["Fire", +300.0]]
					victim.DamageFunc(hit_entity, self.Name, prtl_name, "Fire", 1, -1, x, y, z, 0)
					if Reference.EntitiesObjectData.has_key(prtl_name):
						del Reference.EntitiesObjectData[prtl_name]

					# Generate a smoke effect
					smoke=Bladex.CreateEntity("FireballSmoke", "Entity Particle System D1", x, y, z)
					smoke.ParticleType="DarkSmoke"
					smoke.YGravity=-3000.0
					smoke.Friction=0.05
					smoke.PPS=8
					smoke.Velocity=0.0, -80.0, 0.0
					smoke.RandomVelocity=5.0
					smoke.DeathTime=Bladex.GetTime()+0.5
					node= 0
					victim.LinkToNode(smoke,node)

					# Override hurt anim
					if victim.Life>0:
						if victim.InCombat:
							Damage.DropInvalidObjectsOnImpact (victim.Name)
							victim.Wuea=Reference.WUEA_ENDED
							victim.InterruptCombat()
							victim.LaunchAnmType("hurt_f_big")
						else:
							Damage.DropInvalidObjectsOnImpact (victim.Name)
							victim.Wuea=Reference.WUEA_ENDED
							victim.InterruptCombat()
							victim.LaunchAnmType("hurt_f_big")
				elif victim.Weapon:
					pass
		# This particle should be removed, as it has been converted to smoke
		ptcl=Bladex.GetEntity(prtl_name)
		ptcl.RemoveFromWorld()


	def CreateTestParticle(self, fireball_name,end_time,period):
		fireball=Bladex.GetEntity(fireball_name)
		if(fireball):
			prtl=fireball.GetParticleEntity()
			prtl.HitFunc=self.FirePrtlHit
			prtl.ObjCTest= 1
			if(Bladex.GetTime()<end_time):
				Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.CreateTestParticle,(fireball_name,end_time,period))
		else:
			pass
			#print "system finished"

	def StartSpit (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		x,y,z= me.GraspPos("ViewPoint")
		self.AGE_Number=self.AGE_Number+1
		node= me.GetNodeIndex("Head")
		# Get an angle to the target
		target= Bladex.GetEntity(me.GetEnemyName())
		target_pos= target.Position
		angle= -B3DLib.GetYAngle(target_pos[0]-x,target_pos[1]-y,target_pos[2]-z)
		print "angle was "+`angle`
		if me.AnimName=="g_spitball":
			# fireball spit
			nparticles= 360
			duration= 2.0/60.0
			end_time=Bladex.GetTime()+duration
			period= duration/7.0
			fireball=Bladex.CreateEntity(EntityName+"_Fireball_"+`self.AGE_Number`,"Entity Particle System D1",x,y,z)
			fireball.ParticleType="LargeFire"
			fireball.YGravity=-2400
			fireball.Friction=0.03
			fireball.PPS=nparticles/duration
			fireball.DeathTime=end_time;
			F= 25000.0             # Vector magnitude
			vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*F, -math.sin(angle)*F)
			fireball.Velocity=vx,vy,vz
			fireball.RandomVelocity=50.0
			self.CreateTestParticle(fireball.Name, end_time, period)
		else:
			# flamethrower style
			duration= 20.0
			end_time=Bladex.GetTime()+duration
			period= 0.05
			new_name= EntityName+"_flamethrower_"+`self.AGE_Number`
			print "Creating Flame "+new_name
			if self.Flame:
				self.StopSpit (EntityName,EventName)
			self.Flame=Bladex.CreateEntity(new_name,"Entity Particle System D1",x,y,z)
			self.Flame.ParticleType="Flame"
			self.Flame.PPS=512
			self.Flame.Time2Live=21
			#self.Flame.DeathTime=Bladex.GetTime()+0.75;
			if me.AnimName=="g_spit_around":
				F= 18000.0             # Vector magnitude
				Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, self.StopSpit, (EntityName,""), "StopSpitFunc")
				angle= 	math.fmod(angle+2.8, Actions.TWOPI)
				vx,vy,vz= me.GetDummyAxis("Mouth", -math.cos(angle)*F, -math.sin(angle)*F, 0.0, TRUE)
				self.Flame.Velocity=vx,vy,vz
				self.Flame.RandomVelocity=60.0
				self.Flame.Friction=0.05
				self.Flame.YGravity=-9000.0
			else:
				F= 15000.0             # Vector magnitude
				Bladex.AddScheduledFunc(Bladex.GetTime()+3.85, self.StopSpit, (EntityName,""), "StopSpitFunc")
				angle= 	math.fmod(angle+3.15, Actions.TWOPI)
				vx,vy,vz= me.GetDummyAxis("Mouth", -math.cos(angle)*F, -math.sin(angle)*F, 0.0, TRUE)
				#vx,vy,vz= me.GetDummyAxis("Mouth", F, 0.0, 0.0, TRUE)
				self.Flame.Velocity=vx,vy,vz
				self.Flame.RandomVelocity=50.0
				self.Flame.Friction=0.05
				self.Flame.YGravity=-6000.0
			me.LinkToNode(self.Flame,node)
			self.CreateTestParticle(self.Flame.Name, end_time, period)

	def StopSpit (self,EntityName,EventName):
		if self.Flame:
			print "Stopping Flame "+self.Flame.Name
			self.Flame.DeathTime=Bladex.GetTime()
			self.Flame= None

	########################################################################
	#____ ON HIT FUNCS _____________________________________________________
	########################################################################
	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):

		if self.shield_light.Intensity > 0.0:
			damage_absorbed= (self.shield_light.Intensity/self.ShieldIntensityMax) * DamagePoints
			me = Bladex.GetEntity(EntityName)
			if me and me.Life > -damage_absorbed:
				me.Life= me.Life+damage_absorbed
				DamagePoints= max (DamagePoints-damage_absorbed, 0.0)
				current_shield_life= (self.shield_light.Intensity/self.ShieldIntensityMax) * self.ShieldLife
				current_shield_life= current_shield_life - damage_absorbed
				self.shield_light.Intensity = (current_shield_life/self.ShieldLife)*self.ShieldIntensityMax
				self.SetAuraIntensity()
				#print "shield at "+`(self.shield_light.Intensity/self.ShieldIntensityMax)`
				if self.shield_light.Intensity < (self.ShieldIntensityMax/2.0):
					self.ShieldOff (EntityName)

		Enm_Def.NPCPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)

		if not self.LifeUpCalled:
			me = Bladex.GetEntity(EntityName)
			if me and me.Life<CharStats.GetCharMaxLife(me.Kind, me.Level) * 0.5:
				self.LifeUp (EntityName)
				self.LifeUpCalled = 1
				self.ResetCombat (EntityName)
				#pdb.set_trace()
				self.ShieldOn (EntityName)

	########################################################################
	#____ POWERUP FUNCS ____________________________________________________
	########################################################################
	def LevelUp (self,EntityName,MaxLevel):
		me = Bladex.GetEntity(EntityName)
		me.Level = me.Level +1
		time= Bladex.GetTime()
		if me.Level < MaxLevel:
			Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,MaxLevel), EntityName+" LevelUp")
		else:
			self.ResetCombat (EntityName)

	def GDLUP2(self):
		AuraParams=(5, 0, 1, 0, 0, 1)
		AuraGradient=(2, 1.0, 0.6, 0.2, 0.5, 0.0, 1.0, 0.2, 0.05, 0.0, 0.8)
		AuraVar1Args=(5, 300, 0, 1, 1.0)
		AuraVar2Args=(300, 5, 1, 0, 1.5)
		PSParams=(self.GDLevelUpParticleData, "GDLevelUpParticle", 30, 255, 120, 40, 1000, -1000, 0.0, 2, 2, 0.4, 30, 1.6)
		GenFX.LevelUpFX(self.Name, 0, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args, PSParams, 8.0, "Timer15", 15, "../../Sounds/aparicion-espada.wav")
		list_of_nodes=("Head", "L_Shoulder", "L_Elbow", "L_Hand", "R_Shoulder", "R_Elbow", "R_Forearm", "Center", "L_Knee", "L_Foot", "R_Knee", "R_Foot")
		GenFX.ElectricDischarge(self.Name, "GDRayLevelUp", 255, 120, 40, 600, list_of_nodes, 10, 1.5)

	def GDLUP1(self,EntityName,EventName):
		pslup=Bladex.CreateEntity("PSGDLifeUp", "Entity Particle System Dperson", 0, 0, 0)
		pslup.PersonName=self.Name
		pslup.ParticleType="GDLifeUpEnergyConc"
		pslup.PPS=600
		pslup.YGravity=0
		pslup.Friction=0.0
		pslup.RandomVelocity=-2
		pslup.NormalVelocity=-30
		pslup.FollowFactor=0.0
		pslup.Time2Live=50
		pslup.Velocity=0.0, 0.0, 0.0
		pslup.DeathTime=Bladex.GetTime()+1.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, self.GDLUP2, ())

	def LifeUp (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		me.LaunchAnmType("mgc_df")
		if self.Phase==1:
			MaxLevel=9
		else:
			MaxLevel=19
		if me.Level < MaxLevel:
			time= Bladex.GetTime()
			Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,MaxLevel), EntityName+" LevelUp")
			self.GDLUP1(EntityName,"no_hay_evento")

	########################################################################
	#____ SHIELD FUNCS _____________________________________________________
	########################################################################
	def SetAuraIntensity(self):
		self.back_aura.SetAuraParams(150,self.shield_light.Intensity/self.ShieldIntensityMax,1.0,0,1,1)
		self.front_aura.SetAuraParams(100.0,self.shield_light.Intensity/self.ShieldIntensityMax,1.0,1,0,1)

	def ShieldOn (self,EntityName):
		self.shield_light.TimerFunc= self.IncreaseShieldIntensity
		self.shield_light.SubscribeToList("Timer8")
		self.SetAuraIntensity()
		self.back_aura.SetAuraActive(1)
		self.front_aura.SetAuraActive(1)

	def ShieldOff (self,EntityName):
		self.shield_light.TimerFunc= self.DecreaseShieldIntensity
		self.shield_light.SubscribeToList("Timer8")

	def IncreaseShieldIntensity(self, ent_name, time):
		self.shield_light.Intensity= min(self.shield_light.Intensity+0.3, self.ShieldIntensityMax)
		self.SetAuraIntensity()
		if self.shield_light.Intensity == self.ShieldIntensityMax:
			self.shield_light.RemoveFromList("Timer8")
			self.shield_light.TimerFunc=""

	def DecreaseShieldIntensity(self, ent_name, time):
		self.shield_light.Intensity= max(self.shield_light.Intensity-0.3, 0.0)
		self.SetAuraIntensity()
		if self.shield_light.Intensity == 0.0:
			self.shield_light.RemoveFromList("Timer8")
			self.shield_light.TimerFunc=""
			self.back_aura.SetAuraActive(0)
			self.front_aura.SetAuraActive(0)

	########################################################################
	#____ DEATH FUNCS ______________________________________________________
	########################################################################
	def RemoveMe (self,EntityName):
		me  = Bladex.GetEntity(EntityName)
		if me:
			me.Alpha=0.0
			me.TimerFunc=""
			me.SubscribeToList("Pin")

	def FadeOut (self,EntityName):
		self.Fader.FadeOut(self.FadeOutTime)

	def DeathBall (self,EntityName):
		me  = Bladex.GetEntity(EntityName)
		if me:
			alfa=me.Angle+3.14159/2.0
			x=me.Position[0]+500.0*math.cos(alfa)
			y=me.Position[1]+250.0
			z=me.Position[2]+500.0*math.sin(alfa)
			me.RasterMode="Read"
			self.deathball_particle_system=Bladex.CreateEntity("BolaFuego", "Entity Particle System D1", x, y, z)
			self.deathball_particle_system.ParticleType="FuegoInvocacion"
			self.deathball_particle_system.PPS=250
			self.deathball_particle_system.YGravity=0.0
			self.deathball_particle_system.Friction=0.1
			self.deathball_particle_system.Velocity=0.0, 0.0, 0.0
			self.deathball_particle_system.RandomVelocity=50.0
			self.deathball_particle_system.Time2Live=40
			self.deathball_particle_system.DeathTime= Bladex.GetTime()+self.DeathBallPeriod
			self.FadeOutTime=self.DeathBallPeriod*0.8
			#pdb.set_trace()
			self.FadeOut(EntityName)

			# After the fade out, remove me from the world
			Bladex.AddScheduledFunc(Bladex.GetTime()+self.DeathBallPeriod*0.9, self.RemoveMe, (EntityName,))

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		me.UnlinkChildren()

		# switch off shield if activated
		if self.shield_light:
			self.shield_light.RemoveFromList("Timer8")
			self.shield_light.TimerFunc= self.DecreaseShieldIntensity
			self.shield_light.SubscribeToList("Timer8")

		if self.shield_particle_system:
			self.shield_particle_system.DeathTime= Bladex.GetTime()
			self.shield_particle_system= None

		# Create an implosive particle system
		impl=Bladex.CreateEntity("ImplosionDemonio", "Entity Particle System D1", me.Position[0], me.Position[1], me.Position[2])
		impl.ParticleType="Energia3"
		impl.YGravity=0.0
		impl.Friction=0.0
		impl.PPS=300
		impl.Velocity=0.0, 0.0, 0.0
		impl.RandomVelocity=-30.0
		impl.Time2Live=70
		impl.DeathTime=Bladex.GetTime()+(self.ImplosionPeriod*0.5)

		# After the implosion, create a fiery deathball
		Bladex.AddScheduledFunc(Bladex.GetTime()+self.ImplosionPeriod, self.DeathBall, (EntityName,))

################################################################################
# Define the DarkLord class
################################################################################
class DarkLord (Enm_Def.NPCPerson):

	# constants
	ThirdEye= (0.0, 0.0, 50.0)
	LEye= (-50.0, 0.0, 0.0)
	REye= (50.0, 0.0, 0.0)
	HidePos= (586400.75, 302647.75, 183222.469)
	Phase2MaxX= 8650.0
	FadeOutTime= 2.0
	FadeInTime= 2.0
	TransitTime= 10.0

	#variables
	positionlist=[]
	meteoritestartlist=[]
	AGE_Number= 0
	LastAppearanceTime= Bladex.GetTime()
	Phase=1
	missileRName=""
	missileLName=""
	missileCName=""
	BallName=""
	rayName=""
	rayLName=""
	rayRName=""
	luzConcName=""
	rayconcName=""
	luzglowName=""
	luzchName=""
	chorigenName=""

	LifeUpCalled=0

	MissilesFired=0

	DLLevelUpParticleData=[]

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.DamageFactorNone  = 0.15
		self.DamageFactorLight = 0.25
		self.DamageFactorHeavy = 0.35

		self.positionlist=[]
		self.meteoritestartlist=[]
		self.DLLevelUpParticleData

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		me.AddAnmEventFunc("Aim", self.Aim)
		me.AddAnmEventFunc("Fire", self.Fire)

		me.Level= 9
		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)

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
			size=250.0*aux
			self.DLLevelUpParticleData.append(a)
			self.DLLevelUpParticleData.append(size)
			Bladex.SetParticleGVal("DLLevelUpParticle",i,r,g,b,a,size)


	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosAnAhkard(EntityName)

	# Functions for loading and saving state
	def __getstate__(self):
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: DarkLord.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["DarkLord"]=(self.MissilesFired,
						self.positionlist,
						self.AGE_Number,
						self.LastAppearanceTime,
						self.Phase,
						self.missileRName,
						self.missileLName,
						self.missileCName,
						self.BallName,
						self.rayName,
						self.rayLName,
						self.rayRName,
						self.luzConcName,
						self.rayconcName,
						self.luzglowName,
						self.chorigenName,
						self.luzchName,
						self.LifeUpCalled,
						self.meteoritestartlist)
		return NPCPerson_state

	def __setstate__(self,parm):

		# constants
		self.ThirdEye= (0.0, 0.0, 50.0)
		self.LEye= (-50.0, 0.0, 0.0)
		self.REye= (50.0, 0.0, 0.0)
		self.HidePos= (586400.75, 302647.75, 183222.469)
		self.Phase2MaxX= 8650.0
		self.FadeOutTime= 2.0
		self.FadeInTime= 2.0
		self.TransitTime= 10.0

		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["DarkLord"]
			self.MissilesFired=parms[0]
			self.positionlist=parms[1]
			self.AGE_Number=parms[2]
			self.LastAppearanceTime=parms[3]
			self.Phase=parms[4]
			self.missileRName=parms[5]
			self.missileLName=parms[6]
			self.missileCName=parms[7]
			self.BallName=parms[8]
			self.rayName=parms[9]
			self.rayLName=parms[10]
			self.rayRName=parms[11]
			self.luzConcName=parms[12]
			self.rayconcName=parms[13]
			self.luzglowName=parms[14]
			self.chorigenName=parms[15]
			self.luzchName=parms[16]
			self.LifeUpCalled=parms[17]
			self.meteoritestartlist=parms[18]

		me=Bladex.GetEntity(self.Name)
		me.AddAnmEventFunc("Aim", self.Aim)
		me.AddAnmEventFunc("Fire", self.Fire)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.2
			me.AttackList = BCopy.deepcopy(Combat.AnAhkardAttackData)
			me.AttackList.append([Combat.ATTACK,  0.005, self.Launch3Missiles,         1000.0, 15000.0, 30000.0, 2.0])
			if me.Level > 9:
				me.AttackList.append([Combat.ATTACK,  0.01, self.LaunchGreatBall,         5000.0, 6000.0,30000.0, 0.5])
				me.AttackList.append([Combat.ATTACK,  0.005, self.LaunchMeteorites,       4000.0, 6000.0,30000.0, self.FadeOutTime+self.TransitTime+self.FadeInTime])
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def Aim (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me.AnimName=="g_mgc01":
			self.Aim3Missiles (EntityName)
		elif me.AnimName=="g_mgc02":
			self.AimEnergyBall (EntityName)
		elif me.AnimName=="g_mgc03":
			self.AimLaser (EntityName)

	def Fire (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me.AnimName=="g_mgc01":
			self.Fire3Missiles (EntityName)
		elif me.AnimName=="g_mgc02":
			self.FireEnergyBall (EntityName)
		elif me.AnimName=="g_mgc03":
			self.FireLaser (EntityName)


	########################################################################
	#____ 3 MISSILES FUNCS _________________________________________________
	########################################################################

	def EndCreateMissile(self, missilename, x, y, z, vx, vy, vz):
		missile=ItemTypes.MakeGenericMissile(missilename, x+vx, y+vy, z+vz)
		missile.Color=255, 180, 160
		missile.Data.SetMissileSound("shoot", "../../Sounds/Fireball-Fire.wav")
		missile.Data.SetMissileSound("while", "../../Sounds/bola-fuego.wav")
		missile.Data.SetMissileSound("impact", "../../Sounds/fireball-impact-wood.wav")
		missileps1=Bladex.CreateEntity(missilename+"PS1", "Entity Particle System D1", 0, 0, 0)
		missileps1.ParticleType="RedMagicMissile"
		missileps1.PPS=200
		missileps1.YGravity=0.0
		missileps1.Friction=0.08
		missileps1.Velocity=0.0, 0.0, 0.0
		missileps1.RandomVelocity=15.0
		missileps1.Time2Live=30
		missile.Link(missileps1)
		missileps1.FollowFactor=1
		missileps2=Bladex.CreateEntity(missilename+"PS2", "Entity Particle System D1", 0.0, 0.0, 0.0)
		missileps2.ParticleType="RedMagicMissile"
		missileps2.PPS=100
		missileps2.YGravity=0.0
		missileps2.Friction=0.04
		missileps2.Velocity=0.0, 0.0, 0.0
		missileps2.RandomVelocity=-5.0
		missileps2.Time2Live=25
		missile.Link(missileps2)
		missile.Data.missileps1=missileps1
		missile.Data.missileps2=missileps2
		missile.Data.OldInflictHitFunc=missile.InflictHitFunc
		missile.InflictHitFunc=self.MissileImpact
		l=len(missilename)
		suf=missilename[l-1:l]
		if suf=="R":
			self.missileRName=missile.Name
		elif suf=="L":
			self.missileLName=missile.Name
		else:
			self.missileCName=missile.Name
		Reference.EntitiesObjectData[missile.Name]= BCopy.deepcopy(Reference.DefaultObjectData['EsferaNegraAhk'])

	def CreateMissile(self, missilename, x, y, z, vx, vy, vz):
		missileconc=Bladex.CreateEntity(missilename+"Conc", "Entity Particle System D1", x+vx, y+vy, z+vz)
		missileconc.ParticleType="FastRedEnergyConc"
		missileconc.PPS=400
		missileconc.YGravity=0.0
		missileconc.Friction=0.0
		missileconc.Velocity=0.0, 0.0, 0.0
		missileconc.RandomVelocity=-20.0
		missileconc.Time2Live=30
		missileconc.DeathTime=Bladex.GetTime()+1.0
		missileconcsound=Bladex.CreateEntity(missilename+"ConcSound", "Entity Sound", x+vx, y+vy, z+vz)
		missileconcsound.SetSound("../../Sounds/fireball-swing.wav")
		missileconcsound.MinDistance=5000
		missileconcsound.MaxDistance=30000
		missileconcsound.PlaySound(0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, self.EndCreateMissile, (missilename, x, y, z, vx, vy, vz))

	def Aim3Missiles (self,EntityName):
		me=Bladex.GetEntity(EntityName)
		x, y, z=me.Position
		vx, vy, vz=me.Rel2AbsVector(-1500.0, -500.0, 2500.0)
		self.CreateMissile(me.Name+"MR", x, y, z, vx, vy, vz)
		vx, vy, vz = me.Rel2AbsVector(1500.0, -500.0, 2500.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, self.CreateMissile, (me.Name+"ML", x, y, z, vx, vy, vz))
		vx, vy, vz = me.Rel2AbsVector(0.0, -500.0, 3000.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, self.CreateMissile, (me.Name+"MC", x, y, z, vx, vy, vz))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, self.Fire3Missiles, (EntityName,))

	def FireMissile(self, missilename, vx, vy, vz):
		me=Bladex.GetEntity(self.Name)
		missile=Bladex.GetEntity(missilename)
		if me and missile:
			missile.OnHitFunc=self.MissileOnHit
			missile.Data.Fire(vx, vy, vz, me.GetEnemyName(), 0.5, 2.0, self.MissileDissipation, 10.0)
			x, y, z=missile.Position
			missileshootps=Bladex.CreateEntity(missilename+"ShootPS", "Entity Particle System D1", 0, 0, 0)
			missileshootps.ParticleType="RedMagicMissile"
			missileshootps.PPS=1000
			missileshootps.YGravity=0.0
			missileshootps.Friction=0.08
			missileshootps.Velocity=0.0, 0.0, 0.0
			missileshootps.RandomVelocity=40.0
			missileshootps.Time2Live=20
			missileshootps.DeathTime=Bladex.GetTime()+0.25
			missile.Link(missileshootps)

	def Fire3Missiles (self,EntityName):
		if self.MissilesFired:
			self.MissilesFired=0
			return
		self.MissilesFired=1
		me=Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			velocity=6000.0
			vx, vy, vz=me.Rel2AbsVector(-velocity*0.707107, -velocity*0.707107, 0.0)
			self.FireMissile(self.missileRName, vx, vy, vz)
			vx, vy, vz=me.Rel2AbsVector(+velocity*0.707107, -velocity*0.707107, 0.0)
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, self.FireMissile, (self.missileLName, vx, vy, vz))
			vx, vy, vz=me.Rel2AbsVector(0.0, -velocity, 0.0)
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.8, self.FireMissile, (self.missileCName, vx, vy, vz))

	def RemoveMissile(self, EntityName):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			if Reference.EntitiesObjectData.has_key(missile.Name):
				del Reference.EntitiesObjectData[missile.Name]
			missile.Unlink(missile.Data.missileps2)
			missile.Data.missileps2.DeathTime=Bladex.GetTime()+1.0/60.0
			missile.Data.RemoveMissile()

	def DecreaseMissileIntensity(self, EntityName, intreduction, sndreduction):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			missilewhilesound=missile.Data.MissileWhileSound
			missile.Intensity=missile.Intensity-intreduction
			missilewhilesound.Volume=missilewhilesound.Volume-sndreduction

	def MissileDissipation(self, EntityName):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			missile.Data.missileps1.DeathTime=Bladex.GetTime()+1.0/60.0
			missilewhilesound=missile.Data.MissileWhileSound
			intreduction=missile.Intensity/4.0
			sndreduction=missilewhilesound.Volume/4.0
			missile.Intensity=missile.Intensity-intreduction
			missilewhilesound.Volume=missilewhilesound.Volume-sndreduction
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.15, self.DecreaseMissileIntensity, (EntityName, intreduction, sndreduction))
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, self.DecreaseMissileIntensity, (EntityName, intreduction, sndreduction))
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, self.RemoveMissile, (EntityName,))

	def MissileImpact(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			x, y, z=missile.Position
			impactps=Bladex.CreateEntity("ImpactPS", "Entity Particle System D1", x, y, z)
			impactps.ParticleType="RedMagicMissile"
			impactps.PPS=2000
			impactps.YGravity=1400.0
			impactps.Friction=0.06
			impactps.Velocity=-ImpX/5.0, -ImpY/5.0, -ImpZ/5.0
			impactps.RandomVelocity=40.0
			impactps.Time2Live=20
			impactps.DeathTime=Bladex.GetTime()+0.25
			luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", x-ImpX/10.0, y-ImpY/10.0, z-ImpZ/10.0)
			luzimp.Color=255, 180, 160
			luzimp.Intensity=1.0
			luzimp.Precission=0.001
			luzimp.CastShadows=0
			luzimp.Flick=0
			luzimp.Visible=0
			AuxFuncs.SpotIntensityVariation(luzimp.Name, 1.0, 0.0, 1.0, 1)
			if missile.Data: missile.Data.OldInflictHitFunc(EntityName, VictimName, ImpX, ImpY, ImpZ)

	def MissileOnHit (self, MissileName, hit_entity):
		missile=Bladex.GetEntity(MissileName)
		if missile:
			if missile.Data:
				missile.Data.RemovePostFunc()
			if hit_entity:
				#print MissileName+" hitting "+hit_entity
				pass
			else:
				#print MissileName+" hitting world"
				x, y, z=missile.Position
				impactps=Bladex.CreateEntity("ImpactPS", "Entity Particle System D1", x, y, z)
				impactps.ParticleType="RedMagicMissile"
				impactps.PPS=2500
				impactps.YGravity=1400.0
				impactps.Friction=0.06
				impactps.Velocity=0.0, 0.0, 0.0
				impactps.RandomVelocity=40.0
				impactps.Time2Live=20
				impactps.DeathTime=Bladex.GetTime()+0.25
				luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", x, y, z)
				luzimp.Color=255, 180, 160
				luzimp.Intensity=1.0
				luzimp.Precission=0.001
				luzimp.CastShadows=0
				luzimp.Flick=0
				luzimp.Visible=0
				AuxFuncs.SpotIntensityVariation(luzimp.Name, 1.0, 0.0, 1.0, 1)
			if missile.Data:
				Bladex.AddScheduledFunc(Bladex.GetTime(), missile.Data.RemoveMissile, (1,))

	def StdDelayNoSeen (self,EntityName):
		print EntityName+": StdDelayNoSeen"
		Enm_Def.NPCPerson.StdDelayNoSeen(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me:
			if me.Alpha > 0.999:
				enemy= Bladex.GetEntity(me.GetEnemyName())
				if enemy and enemy.Life>0:
					position, angle= self.FindAdjustedFarPos (EntityName)
					if position:
						# Ok, we, going to teletransport to a better location to catch the player
						self.FadeOut(EntityName)
						time= Bladex.GetTime()
						Bladex.AddScheduledFunc(time+self.FadeOutTime, self.ReappearFar, (EntityName,), EntityName+" ReappearFar")


	def Launch3Missiles (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			if me.Alpha >= 1.0:
				# May wish to make all attacks pass through...
				time= Bladex.GetTime()
				if abs (time-self.LastAppearanceTime) > 5.0:
					enemy= Bladex.GetEntity(me.GetEnemyName())
					if enemy and enemy.Life>0:
						position, angle= self.FindAdjustedFarPos (EntityName)
						if position:
							# Ok, we, going to teletransport to a better location to lauch the ball
							self.FadeOut(EntityName)
							time= Bladex.GetTime()
							Bladex.AddScheduledFunc(time+self.FadeOutTime, self.ReappearFar, (EntityName,), EntityName+" ReappearFar")
							Bladex.AddScheduledFunc(time+self.FadeOutTime+0.01, self.Launch3MissilesQuick, (EntityName,), EntityName+" LaunchGreatBallQuick")
							return 1
						else:
							self.Launch3MissilesQuick (EntityName)
		return 0

	def Launch3MissilesQuick (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			enemy= Bladex.GetEntity(me.GetEnemyName())
			if enemy and enemy.Life>0 and me.CanISee(enemy):
				# Maybe launch a quick great ball
				distSQ= me.SQDistance2(enemy)
				mindistSQ= 1500.0**2.0
				if distSQ > mindistSQ:
					me.SetNextAttack("g_mgc01")
					return 1
		return 0

	########################################################################
	#____ ENERGY BALL FUNCS ________________________________________________
	########################################################################
	def LaunchGreatBall (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			if me.Alpha >= 1.0:
				# May wish to make all attacks pass through...
				enemy= Bladex.GetEntity(me.GetEnemyName())
				if enemy and enemy.Life>0:
					time= Bladex.GetTime()
					if abs (time-self.LastAppearanceTime) > 5.0:
						if len(self.positionlist) > 0:
							# may want to add a visibility check to the closer location as well
							# Ok, we, going to teletransport to a better location to lauch the ball
							self.FadeOut(EntityName)
							time= Bladex.GetTime()
							Bladex.AddScheduledFunc(time+self.FadeOutTime, self.ReappearFar, (EntityName,), EntityName+" ReappearFar")
							Bladex.AddScheduledFunc(time+self.FadeOutTime+0.01, self.LaunchGreatBallQuick, (EntityName,), EntityName+" LaunchGreatBallQuick")
							return 1
						else:
							self.LaunchGreatBallQuick(EntityName)
		return 0

	def LaunchGreatBallQuick (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			enemy= Bladex.GetEntity(me.GetEnemyName())
			if enemy and enemy.Life>0 and me.CanISee(enemy):
				# Maybe launch a quick great ball
				distSQ= me.SQDistance2(enemy)
				mindistSQ= 2000.0**2.0
				if distSQ > mindistSQ:
					me.SetNextAttack("g_mgc02")
					return 1
		return 0

	def AimEnergyBall (self,EntityName):
		#print "AimEnergyBall"
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			x, y, z=me.Position
			ox,oy,oz=me.Rel2AbsVector(0.0, -2500.0, 0.0)
			x=x+ox; y=y+oy; z=z+oz
			self.AGE_Number= self.AGE_Number+1
			ball= ItemTypes.MakeAnkBall(EntityName+"_Ball"+`self.AGE_Number`, x,y,z, EntityName)
			ball.Velocity= me.Rel2AbsVector(0.0, -250.0, 250.0)
			self.BallName= ball.Name

	def FireEnergyBall (self,EntityName):
		ball= Bladex.GetEntity(self.BallName)
		if ball:
			ball.Data.ReleaseThrownWeaponHandler(self.BallName, "")

	########################################################################
	#____ LASER FUNCS ______________________________________________________
	########################################################################
	def AimLaser (self,EntityName):
		#print "AimLaser"
		#just in case
		self.StopLaser(EntityName)
		me = Bladex.GetEntity(EntityName)
		head_idx=me.GetNodeIndex("Head")
		x,y,z= me.GraspPos("ViewPoint")
		ox,oy,oz=me.Rel2AbsVector(self.ThirdEye[0], self.ThirdEye[1]-500.0, self.ThirdEye[2], "Head")
		x1=x+ox; y1=y+oy; z1=z+oz
		luzconc=Bladex.CreateEntity("LuzConcRayoLaser", "Entity Spot", x1, y1, z1)
		luzconc.Color=140, 180, 255
		luzconc.Intensity=0.0
		luzconc.Precission=0.001
		luzconc.CastShadows=0
		luzconc.Visible=0
		self.luzConcName= luzconc.Name
		me.LinkToNode(luzconc, head_idx)
		ox,oy,oz=me.Rel2AbsVector(self.ThirdEye[0], self.ThirdEye[1], self.ThirdEye[2], "Head")
		x1=x+ox; y1=y+oy; z1=z+oz
		rayconc=Bladex.CreateEntity("PSConcRayoLaser","Entity Particle System D1", x1, y1, z1)
		rayconc.ParticleType="LittleBlueEnergyConc"
		rayconc.FollowFactor=1.0
		rayconc.YGravity=0
		rayconc.RandomVelocity=-10
		rayconc.Velocity=me.Rel2AbsVector(0.0, 600.0, 0.0, "Head")
		rayconc.Time2Live=30
		rayconc.PPS=200
		me.LinkToNode(rayconc, head_idx)
		self.rayconcName= rayconc.Name
		luzglow=Bladex.CreateEntity("LuzGlowRayoLaser", "Entity Spot", x1, y1, z1)
		luzglow.Color=140, 180, 255
		luzglow.Intensity=0.0
		luzglow.CastShadows=0
		me.LinkToNode(luzglow, head_idx)
		self.luzglowName= luzglow.Name
		AuxFuncs.SpotIntensityVariation(luzglow.Name, 0.0, 0.01, 3.0, 0, 0.0, 1.5)
		AuxFuncs.SpotIntensityVariation(luzconc.Name, 0.0, 4.0, 3.0)

		Bladex.RemoveScheduledFunc(EntityName+"StopLaserFunc")
		TimeToStop=5.0 # has to be enough time to get to FireLaser() normally
		Bladex.AddScheduledFunc(Bladex.GetTime()+TimeToStop, self.StopLaser, (EntityName,), EntityName+"StopLaserFunc")

	def FireLaser (self,EntityName):
		#print "FireLaser"
		Bladex.RemoveScheduledFunc(EntityName+"StopLaserFunc")
		me = Bladex.GetEntity(EntityName)
		try:
			if self.rayName or self.rayLName or self.rayRName:
				self.StopLaser(EntityName)
		except AttributeError:
			pass

		if self.rayconcName:
			rayconc=Bladex.GetEntity(self.rayconcName)
			if rayconc:
				rayconc.RandomVelocity=-4
				rayconc.Velocity=0.0, 0.0, 0.0
				rayconc.PPS=100
		head_idx=me.GetNodeIndex("Head")
		x,y,z= me.GraspPos("ViewPoint")
		ox,oy,oz=me.Rel2AbsVector(self.ThirdEye[0], self.ThirdEye[1], self.ThirdEye[2], "Head")
		x= x+ox; y= y+oy; z= z+oz
		chorigen=Bladex.CreateEntity("ChispasOrigenRayoLaser","Entity Particle System D1", x, y, z)
		chorigen.ParticleType="BlueSpark"
		chorigen.FollowFactor=1.0
		chorigen.YGravity=0
		chorigen.RandomVelocity=30
		chorigen.Velocity=me.Rel2AbsVector(0.0, -1000.0, 0.0, "Head")
		chorigen.Time2Live=6
		chorigen.PPS=800
		me.LinkToNode(chorigen, head_idx)
		self.chorigenName=chorigen.Name

		target= Bladex.GetEntity(me.GetEnemyName())
		tx,ty,tz= target.Position
		angle= -B3DLib.GetYAngle(tx-x,ty-y,tz-z)
		distance= 1000.0 + math.sqrt(((tx-x)*(tx-x))+((ty-y)*(ty-y))+((tz-z)*(tz-z)))
		vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*distance, -math.sin(angle)*distance)
		tx= x+vx; ty= y+vy; tz= z+vz

		ray= Bladex.CreateEntity("Ray", "Entity ElectricBolt", x,y,z)
		ray.FixedTarget= FALSE
		ray.MaxAmplitude=250.0
		me.LinkToNode(ray, head_idx)
		ray.Position= x,y,z	# The position gets screwed up after linking
		ray.Target= tx,ty,tz
		ray.Active= 1
		self.rayName= ray.Name

		x,y,z= me.GraspPos("ViewPoint")
		ox,oy,oz=me.Rel2AbsVector(self.LEye[0], self.LEye[1], self.LEye[2], "Head")
		x= x+ox; y= y+oy; z= z+oz
		rayL= Bladex.CreateEntity("RayL", "Entity ElectricBolt", x,y,z)
		rayL.FixedTarget= FALSE
		rayL.MaxAmplitude=150.0
		me.LinkToNode(rayL, head_idx)
		rayL.Position= x,y,z	# The position gets screwed up after linking
		rayL.Target= tx,ty,tz
		rayL.Active= 1
		self.rayLName= rayL.Name

		x,y,z= me.GraspPos("ViewPoint")
		ox,oy,oz=me.Rel2AbsVector(self.REye[0], self.REye[1], self.REye[2], "Head")
		x= x+ox; y= y+oy; z= z+oz
		rayR= Bladex.CreateEntity("RayR", "Entity ElectricBolt", x,y,z)
		rayR.FixedTarget= FALSE
		rayR.MaxAmplitude=150.0
		me.LinkToNode(rayR, head_idx)
		rayR.Position= x,y,z	# The position gets screwed up after linking
		rayR.Target= tx,ty,tz
		rayR.Active= 1
		self.rayRName= rayR.Name

		luzch=Bladex.CreateEntity("LuzChispasRayoLaser", "Entity Spot", tx, ty, tz)
		luzch.Color=140, 180, 255
		luzch.Intensity=0.5
		luzch.Precission=0.03125
		luzch.CastShadows=0
		luzch.SizeFactor=2.0
		me.LinkToNode(luzch, head_idx)
		self.luzchName= luzch.Name

		chtarget=Bladex.CreateEntity("ChispasTargetRayoLaser","Entity Particle System D1", 0, 0, 0)
		chtarget.ParticleType="LittleBlueSpark"
		chtarget.FollowFactor=1.0
		chtarget.YGravity=0
		chtarget.RandomVelocity=20
		chtarget.RandomVelocity_V=40
		chtarget.Velocity=0.0, 0.0, 0.0
		chtarget.Time2Live=6
		chtarget.PPS=400
		luzch.Link(chtarget)

		me.AnmEndedFunc=self.StopLaser
		Bladex.RemoveScheduledFunc("StopLaserFunc")
		time= Bladex.GetTime()
		period= 0.2
		Bladex.AddScheduledFunc(time+period, self.RecalibrateLaserFunc, (EntityName,time+4.0,period), "RecalibrateLaserFunc")

	def RecalibrateLaserFunc (self,EntityName, TimeToStop,Period):
		#print "RecalibrateLaserFunc"
		if not self.rayName or not self.rayLName or not self.rayRName or not self.luzchName:
			return

		me = Bladex.GetEntity(EntityName)
		ray= Bladex.GetEntity (self.rayName)
		rayL= Bladex.GetEntity (self.rayLName)
		rayR= Bladex.GetEntity (self.rayRName)
		luzch=Bladex.GetEntity(self.luzchName)
		me.Unlink(luzch)

		if not me or not ray or not rayL or not rayR or not luzch:
			return

		if me.Life < 0:
			self.StopLaser (EntityName)

		x,y,z= me.GraspPos("ViewPoint")
		ox,oy,oz=me.Rel2AbsVector(self.ThirdEye[0], self.ThirdEye[1], self.ThirdEye[2], "Head")
		x= x+ox; y= y+oy; z= z+oz
		target= Bladex.GetEntity(me.GetEnemyName())
		if not target:
			return

		tx,ty,tz= target.Position
		angle= -B3DLib.GetYAngle(tx-x,ty-y,tz-z)
		distance= 1000.0 + math.sqrt(((tx-x)*(tx-x))+((ty-y)*(ty-y))+((tz-z)*(tz-z)))
		vx,vy,vz=me.Rel2AbsVector(0.0, -math.cos(angle)*distance, -math.sin(angle)*distance)
		tx= x+vx; ty= y+vy; tz= z+vz

		ray.Target=  tx,ty,tz
		rayL.Target= tx,ty,tz
		rayR.Target= tx,ty,tz
		luzch.Position=tx,ty,tz
		me.LinkToNode(luzch, me.GetNodeIndex("Head"))
		Actions.QuickTurnToFaceEntity (EntityName, me.GetEnemyName())

		next_call_time= Bladex.GetTime() + Period
		if next_call_time < TimeToStop:
			Bladex.AddScheduledFunc(next_call_time, self.RecalibrateLaserFunc, (EntityName,TimeToStop,Period), "RecalibrateLaserFunc")
		else:
			Bladex.RemoveScheduledFunc(EntityName+"StopLaserFunc")
			Bladex.AddScheduledFunc(TimeToStop, self.StopLaser, (EntityName,), EntityName+"StopLaserFunc")

	def StopLaser (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		print "StopLaser"
		if self.luzConcName:
			AuxFuncs.SpotIntensityVariation(self.luzConcName, 4.0, 0.0, 1.0, 1)
			self.luzConcName= None
		if self.luzglowName:
			AuxFuncs.SpotIntensityVariation(self.luzglowName, 0.01, 0.0, 1.0, 1, 1.5, 0.0)
			self.luzglowName= None
		if self.rayconcName:
			rayconc= Bladex.GetEntity(self.rayconcName)
			if rayconc: rayconc.DeathTime=Bladex.GetTime()
			self.rayconcName= None
		if self.chorigenName:
			chorigen= Bladex.GetEntity(self.chorigenName)
			if chorigen: chorigen.DeathTime=Bladex.GetTime()
			self.chorigenName= None
		if self.luzchName:
			luzch=Bladex.GetEntity(self.luzchName)
			if luzch: luzch.SubscribeToList("Pin")
			self.luzchName= None
		if self.rayName:
			ray= Bladex.GetEntity (self.rayName)
			if ray:
				me.Unlink(ray)
				ray.Active= 0
				ray.SubscribeToList("Pin")
			self.rayName= None

		if self.rayLName:
			rayL= Bladex.GetEntity (self.rayLName)
			if rayL:
				me.Unlink(rayL)
				rayL.Active= 0
				rayL.SubscribeToList("Pin")
			self.rayLName= None

		if self.rayRName:
			rayR= Bladex.GetEntity (self.rayRName)
			if rayR:
				me.Unlink(rayR)
				rayR.Active= 0
				rayR.SubscribeToList("Pin")
			self.rayRName= None

	########################################################################
	#____ ON HIT FUNCS _____________________________________________________
	########################################################################
	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		Enm_Def.NPCPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)

		if not self.LifeUpCalled:
			me = Bladex.GetEntity(EntityName)
			if me and me.Life<CharStats.GetCharMaxLife(me.Kind, me.Level) * 0.5:
				self.LifeUp (EntityName)
				self.LifeUpCalled = 1

	########################################################################
	#____ POWERUP FUNCS ____________________________________________________
	########################################################################

	def DLLUP2(self):
		AuraParams=(5, 0, 1, 0, 0, 1)
		AuraGradient=(2, 1.0, 0.2, 0.1, 0.5, 0.0, 1.0, 0.07, 0.02, 0.0, 0.8)
		AuraVar1Args=(5, 250, 0, 1, 1.0)
		AuraVar2Args=(250, 5, 1, 0, 1.5)
		PSParams=(self.DLLevelUpParticleData, "DLLevelUpParticle", 30, 255, 20, 5, 800, -800, 0.0, 2, 2, 0.4, 30, 1.6)
		GenFX.LevelUpFX(self.Name, 0, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args, PSParams, 6.0, "Timer15", 15, "../../Sounds/aparicion-espada.wav")
		list_of_nodes=("Head", "L_Shoulder", "L_Elbow", "L_Hand", "R_Shoulder", "R_Elbow", "R_Hand", "Center", "L_Knee", "L_Foot", "R_Knee", "R_Foot")
		GenFX.ElectricDischarge(self.Name, "DLRayLevelUp", 255, 40, 10, 600, list_of_nodes, 10, 1.5)

	def DLLUP1(self,EntityName,EventName):
		pslup=Bladex.CreateEntity("PSDLLifeUp", "Entity Particle System Dperson", 0, 0, 0)
		pslup.PersonName=self.Name
		pslup.ParticleType="DLLifeUpEnergyConc"
		pslup.PPS=600
		pslup.YGravity=0
		pslup.Friction=0.0
		pslup.RandomVelocity=-2
		pslup.NormalVelocity=-20
		pslup.FollowFactor=0.0
		pslup.Time2Live=50
		pslup.Velocity=0.0, 0.0, 0.0
		pslup.DeathTime=Bladex.GetTime()+1.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, self.DLLUP2, ())

	def LifeUp (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Level <= 9:
			self.Phase=2
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			time= Bladex.GetTime()
			self.LevelUpTime= 0.5
			MaxLevel= 19
			Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,MaxLevel), EntityName+" LevelUp")
			self.DLLUP1(EntityName,"no_hay_evento")
			# Start the meteorites here
			Bladex.AddScheduledFunc(time+2.0, self.LaunchMeteorites, (EntityName,))

	def LevelUp (self,EntityName,MaxLevel):
		me = Bladex.GetEntity(EntityName)
		if me:
			me.Level = me.Level +1
			time= Bladex.GetTime()
			if me.Level < MaxLevel:
				Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,MaxLevel), EntityName+" LevelUp")
			else:
				self.ResetCombat (EntityName)

	def FadeOut (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			AuxFuncs.FadeObject(me.Name, me.Alpha, 0.0, self.FadeOutTime)

	def FadeIn (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			AuxFuncs.FadeObject(me.Name, me.Alpha, 1.0, self.FadeInTime)


	def NearestMeteoritePos (self,p1, p2):
		d1= (p1[0]-self.EP[0])**2 + (p1[1]-self.EP[1])**2 + (p1[2]-self.EP[2])**2
		d2= (p2[0]-self.EP[0])**2 + (p2[1]-self.EP[1])**2 + (p2[2]-self.EP[2])**2

		if d1 < d2: return -1	# CHOOSE_FIRST
		elif d1 > d2: return 1	# CHOOSE_SECOND
		else: return 0

	def MeteoritesPhase(self,duration):
		time= Bladex.GetTime()
		endtime=time+duration
		period= 1.0
		if time+period < endtime:
			Bladex.AddScheduledFunc(time+period, self.MeteoritesPhase, (duration-period,), "Next MeteoritesPhase")
		me = Bladex.GetEntity(self.Name)
		if me:
			enemy= Bladex.GetEntity(me.GetEnemyName())
			if enemy:
				self.EP= enemy.Position
				self.meteoritestartlist.sort (self.NearestMeteoritePos)
				s=7000.0
				nmets2gen= min(3, len(self.meteoritestartlist))
				for i in range(nmets2gen):
					p= self.meteoritestartlist[i]
					v= B3DLib.Normalize ((self.EP[0]-p[0], self.EP[1]-p[1], self.EP[2]-p[2]))
					v= B3DLib.Scale(v, s)
					name="Meteorite"+`i`
					Bladex.AddScheduledFunc(time+whrandom.random()*period, ItemTypes.MakeMeteorite, (name,p[0],p[1],p[2],v[0],v[1],v[2]), "Make "+name)
				del self.EP


	def LaunchMeteorites (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			if me.Alpha >= 1.0:
				# May wish to make all attacks pass through...
				time= Bladex.GetTime()
				if abs (time-self.LastAppearanceTime) > 5.0:
					self.FadeOut(EntityName)
					time= Bladex.GetTime()
					# Start the meteorites falling
					self.MeteoritesPhase(self.FadeOutTime+self.TransitTime)
					Bladex.AddScheduledFunc(time+self.FadeOutTime, self.Hide, (EntityName,), EntityName+" Hide")
					return 1
		return 0

	def Hide (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			enemy=Bladex.GetEntity(me.GetEnemyName())
			enemy.SetActiveEnemy(None)
			me.SetActiveEnemy(None)
			me.Position= self.HidePos
			me.SetOnFloor()
			self.LaunchMyWatch(EntityName)
			time= Bladex.GetTime()
			Bladex.AddScheduledFunc(time+self.TransitTime, self.ReappearNear, (EntityName,), EntityName+" ReappearNear")


	def NearestPos (self, p1, p2):
		if self.Phase==2:
			max_x= max(self.EnemyPos[0], self.Phase2MaxX)
			include_p1= p1[0] < max_x
			include_p2= p2[0] < max_x
			if include_p1 and not include_p2:
				return Enm_Def.CHOOSE_FIRST
			elif include_p2 and not include_p1:
				return Enm_Def.CHOOSE_SECOND

		d1= abs(p1[0]-self.EnemyPos[0])**2 + abs(p1[1]-self.EnemyPos[1])**2 + abs(p1[2]-self.EnemyPos[2])**2
		d2= abs(p2[0]-self.EnemyPos[0])**2 + abs(p2[1]-self.EnemyPos[1])**2 + abs(p2[2]-self.EnemyPos[2])**2

		if d1 < d2:
			return Enm_Def.CHOOSE_FIRST
		elif d1 > d2:
			return Enm_Def.CHOOSE_SECOND
		else:
			return Enm_Def.CHOOSE_EITHER

	def AdjustedFurthestPos (self, p1, p2):
		if self.Phase==2:
			max_x= max(self.EnemyPos[0], self.Phase2MaxX)
			include_p1= p1[0] < max_x
			include_p2= p2[0] < max_x
			if include_p1 and not include_p2:
				return Enm_Def.CHOOSE_FIRST
			elif include_p2 and not include_p1:
				return Enm_Def.CHOOSE_SECOND

		d1x= self.EnemyPos[0]-p1[0]
		d1y= self.EnemyPos[1]-p1[1]
		d1z= self.EnemyPos[2]-p1[2]
		d2x= self.EnemyPos[0]-p2[0]
		d2y= self.EnemyPos[1]-p2[1]
		d2z= self.EnemyPos[2]-p2[2]

		d1= (d1x**2 + d1y**2 + d1z**2)**0.5
		d2= (d2x**2 + d2y**2 + d2z**2)**0.5

		angle1 = B3DLib.DiffAngle (B3DLib.GetXZAngle (d1x, 0.0, d1z), self.EnemyAng) / Actions.TWOPI
		angle2 = B3DLib.DiffAngle (B3DLib.GetXZAngle (d2x, 0.0, d2z), self.EnemyAng) / Actions.TWOPI

		d1= d1-(d1*angle1*0.9)
		d2= d2-(d2*angle2*0.9)

		if d1 < d2:
			return Enm_Def.CHOOSE_SECOND
		elif d1 > d2:
			return Enm_Def.CHOOSE_FIRST
		else:
			return Enm_Def.CHOOSE_EITHER

	def FindAdjustedFarPos (self,EntityName):
		ret_val= None,None
		me = Bladex.GetEntity(EntityName)
		if me:
			x,y,z= me.Position
			enemy=Bladex.GetEntity(me.GetEnemyName())
			if enemy:
				self.EnemyPos= enemy.Position
				self.EnemyAng= enemy.Angle
				self.positionlist.sort(self.AdjustedFurthestPos)
				for position in self.positionlist:
					# Are we far enough from our original pos?
					distSQ= (abs(x-position[0])**2.0) + (abs(y-position[1])**2.0) + (abs(z-position[2])**2.0)
					mindistSQ= 2000.0**2.0
					#maxdistSQ= Bladex.GetCharType(me.CharType,me.CharTypeExt).MaxCombatDist**2.0
					if distSQ > mindistSQ:# and distSQ<=maxdistSQ:
						# Is this place collision free?
						max_fall=2000.0
						if me.TestPos (position[0],position[1],position[2], me.ActionAreaMax,max_fall):
							if me.CanISeeFrom (enemy, position[0],position[1],position[2]):
								angle= B3DLib.GetXZAngle (self.EnemyPos[0]-position[0], 0.0, self.EnemyPos[2]-position[2])
								ret_val= position, angle
								break
		return ret_val

	def ReappearNear (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			x,y,z= me.Position
			enemy=Bladex.GetEntity(me.GetEnemyName())
			if enemy:
				self.EnemyPos= enemy.Position
				self.positionlist.sort(self.NearestPos)
				for position in self.positionlist:
					# Are we far enough from our original pos?
					distSQ= (abs(x-position[0])**2.0) + (abs(y-position[1])**2.0) + (abs(z-position[2])**2.0)
					mindistSQ= 2000.0**2.0
					if distSQ > mindistSQ:
						# Is this place collision free?
						max_fall=2000.0
						if me.TestPos (position[0],position[1],position[2], me.ActionAreaMax,max_fall):
							me.Position= position[0],position[1],position[2]
							self.LastAppearanceTime= Bladex.GetTime()
							break
				me.Angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
				me.SetOnFloor()
				# Break enemies facing mode
				if enemy.InCombat and enemy.ActiveEnemy==me.Name and not enemy.CanISee(me):
					enemy.SetActiveEnemy(None)
			self.FadeIn(EntityName)

	def ReappearFar (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me:
			enemy=Bladex.GetEntity(me.GetEnemyName())
			if enemy:
				position, angle= self.FindAdjustedFarPos (EntityName)
				if position:
					me.Position= position
					me.Angle= angle
					me.SetOnFloor()
					self.LastAppearanceTime= Bladex.GetTime()
					# Break enemies facing mode
					if enemy.InCombat and enemy.ActiveEnemy==me.Name and not enemy.CanISee(me):
						enemy.SetActiveEnemy(None)
			self.FadeIn(EntityName)

	########################################################################
################################################################################
# Define the DalGurak class
################################################################################
class DalGurak (Enm_Def.NPCPerson):

	Phase=1
	Fader= None
	FadeOutTime= 0.23333
	FadeInTime= 0.23333
	TransitTime= 0.0
	ShieldTime= 2.0
	LevelUpTime=0.5
	dgkdisapsound=""

	#variables
	positionlist=[]
	last_disappeared_at=0.0
	AGE_Number=0
	LifeUpCalled=0
	BallName=""
	MissileName=""
	DGLevelUpParticleData=[]
	Dalweapon= None
	Dalshield= None

	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.positionlist=[]
		self.DGLevelUpParticleData=[]

		#constants
		# Create a linear interpolator for fading
		FadeList=[me.Name]
		self.Fader= EntitiesFader (FadeList)
		me.AddAnmEventFunc("StartBall", self.StartBall)
		me.AddAnmEventFunc("FireBall", self.ShootBall)
		me.AddAnmEventFunc("Diskcreate", self.CreateDisk)
		me.AddAnmEventFunc("Diskthrow", self.ShootDisk)
		me.AddAnmEventFunc("ThrowHeavyEvent", self.BoomerangWeapon)
		me.AddAnmEventFunc("StartLifeUp", self.DGLUP1)


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
			self.DGLevelUpParticleData.append(a)
			self.DGLevelUpParticleData.append(size)
			Bladex.SetParticleGVal("DGLevelUpParticle",i,r,g,b,a,size)

		# Set up Dal Gurak specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0
		me.Level=9
		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)

		self.dgkdisapsound= Bladex.CreateEntity (self.Name+"DisappearSound", "Entity Sound", 0, 0, 0)
		self.dgkdisapsound.SetSound ("../../Sounds/desaparece-Dgk.wav")
		self.dgkdisapsound.MinDistance=10000
		self.dgkdisapsound.MaxDistance=20000
		me.Link(self.dgkdisapsound)


	# Functions for loading and saving state
	def __getstate__(self):
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: DalGurak.__getstate__(): Base class version differs."
			return NPCPerson_state
		if self.Dalweapon: DalweaponName= self.Dalweapon.Name
		else: DalweaponName= ""
		if self.Dalshield: DalshieldName= self.Dalshield.Name
		else: DalshieldName= ""
		NPCPerson_state[1]["DalGurak"]=(self.positionlist,
										self.last_disappeared_at,
										self.AGE_Number,
										self.LifeUpCalled,
										self.Phase,
										self.BallName,
										self.MissileName,
										DalweaponName,
										DalshieldName)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		version=parm[0]
		if version==1:
			parms=parm[1]["DalGurak"]
			self.positionlist= parms[0]
			self.last_disappeared_at= parms[1]
			self.AGE_Number= parms[2]
			self.LifeUpCalled= parms[3]
			self.Phase= parms[4]
			self.BallName= parms[5]
			self.MissileName= parms[6]
			DalweaponName=  parms[7]
			DalshieldName=  parms[8]

			if DalweaponName: self.Dalweapon= Bladex.GetEntity(DalweaponName)
			else: self.Dalweapon= None
			if DalshieldName: self.Dalshield= Bladex.GetEntity(DalshieldName)
			else: self.Dalshield= None
			Enm_Def.NPCPerson.__setstate__(self,parm)

			#constants
			# Create a linear interpolator for fading
			me=Bladex.GetEntity(self.Name)
			FadeList=[me.Name]
			self.Fader= EntitiesFader (FadeList)
			self.FadeOutTime= 0.23333
			self.FadeInTime= 0.23333
			self.TransitTime= 0.0
			self.ShieldTime= 2.0
			self.LevelUpTime=0.5
			me.AddAnmEventFunc("StartBall", self.StartBall)
			me.AddAnmEventFunc("FireBall", self.ShootBall)
			me.AddAnmEventFunc("Diskcreate", self.CreateDisk)
			me.AddAnmEventFunc("Diskthrow", self.ShootDisk)
			me.AddAnmEventFunc("ThrowHeavyEvent", self.BoomerangWeapon)
			me.AddAnmEventFunc("StartLifeUp", self.DGLUP1)

			self.DGLevelUpParticleData=[]
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
				self.DGLevelUpParticleData.append(a)
				self.DGLevelUpParticleData.append(size)
				Bladex.SetParticleGVal("DGLevelUpParticle",i,r,g,b,a,size)

			self.dgkdisapsound= Bladex.GetEntity (self.Name+"DisappearSound")


	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosDalGurak(EntityName)

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.8
			if self.Phase==1:
				me.AttackList = BCopy.deepcopy(Combat.DalGurakPhase1)
			else:
				me.AttackList = BCopy.deepcopy(Combat.DalGurakPhase2)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		Enm_Def.NPCPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)
		me = Bladex.GetEntity(EntityName)
		# Catch cases where the magic shield does not work...
		if me and me.Life>0:
			inv= me.GetInventory()
			if inv.GetMagicShield():
				me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
		if not self.LifeUpCalled:
			me = Bladex.GetEntity(EntityName)

			if me and me.Life<CharStats.GetCharMaxLife(me.Kind, me.Level) * 0.5:
				self.LifeUp (EntityName)
				self.LifeUpCalled = 1

	########################################################################
	#____ TELETRANSPORTATION FUNCS _________________________________________
	########################################################################
	def FadeOut (self,EntityName):
		self.Fader.FadeOut(self.FadeOutTime)

	def FadeIn (self,EntityName):
		self.Fader.FadeIn(self.FadeInTime)

	def HightestScore (self, p1, p2):
		diff= p2[3] - p1[3]
		if diff < 0:
			return Enm_Def.CHOOSE_FIRST
		elif diff > 0:
			return Enm_Def.CHOOSE_SECOND
		else:
			return Enm_Def.CHOOSE_EITHER

	def Disappear (self,EntityName):
		#print "Disappearing..."
		time= Bladex.GetTime()
		if time-self.last_disappeared_at > 4.0:
			# May wish to make all attacks pass through...
			self.dgkdisapsound.PlaySound(0)
			self.FadeOut(EntityName)
			Bladex.AddScheduledFunc(time+self.FadeOutTime+self.TransitTime, self.Reappear, (EntityName,), EntityName+" Reappear")
			self.last_disappeared_at=time
			return 1
		return 0

	def Reappear (self,EntityName):
		#print "Reappearing..."
		me = Bladex.GetEntity(EntityName)
		enemy= Bladex.GetEntity(me.GetEnemyName())
		angle= me.Angle
		x,y,z= me.Position
		ex,ey,ez= enemy.Position

		min_dist= 2000.0**2
		for position in self.positionlist:
			d2enemy= (position[0]-ex)**2 + (position[1]-ey)**2 + (position[2]-ez)**2
			d2me= (position[0]-x)**2 + (position[1]-y)**2 + (position[2]-z)**2
			score= whrandom.random() * (d2enemy+d2me)
			if d2enemy<min_dist or d2me<min_dist:
				score= 0.01 * score
			position[3]= score

		self.positionlist.sort(self.HightestScore)
		for position in self.positionlist:
			me.Position= position[0],position[1],position[2]
			me.Angle= B3DLib.GetEntity2EntityAngle(EntityName, me.GetEnemyName())
			if me.CanISee(enemy):
				#me.SetOnFloor()
				break
			print "cant see"
			me.Position= x, y, z
			me.Angle= angle
		if not enemy.CanISee(me):
			enemy.SetActiveEnemy(None)
		self.FadeIn(EntityName)

	########################################################################
	#____ POWERUP FUNCS ____________________________________________________
	########################################################################
	def MagicShieldDestroyed (self, ShieldName, EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
		self.Invincibility=1
		Bladex.AddScheduledFunc(Bladex.GetTime(), self.EndPhase1, (EntityName,))
		print "MagicShieldDestroyed"

	def DGLUP2(self):
		AuraParams=(5, 0, 1, 0, 0, 1)
		AuraGradient=(2, 1.0, 0.4, 0.2, 0.5, 0.0, 1.0, 0.15, 0.04, 0.0, 0.8)
		AuraVar1Args=(5, 200, 0, 1, 1.0)
		AuraVar2Args=(200, 5, 1, 0, 1.5)
		PSParams=(self.DGLevelUpParticleData, "DGLevelUpParticle", 30, 255, 40, 10, 400, -600, 0.0, 2, 2, 0.4, 30, 1.6)
		GenFX.LevelUpFX(self.Name, 0, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args, PSParams, 4.0, "Timer15", 15, "../../Sounds/aparicion-espada.wav")
		list_of_nodes=("Head", "L_Shoulder", "L_Elbow", "L_Hand", "R_Shoulder", "R_Elbow", "R_Hand", "Center", "L_Knee", "L_Foot", "R_Knee", "R_Foot")
		GenFX.ElectricDischarge(self.Name, "DGRayLevelUp", 255, 40, 10, 600, list_of_nodes, 10, 1.5)

	def DGLUP1(self,EntityName,EventName):
		pslup=Bladex.CreateEntity("PSDGLifeUp", "Entity Particle System Dperson", 0, 0, 0)
		pslup.PersonName=self.Name
		pslup.ParticleType="DGLifeUpEnergyConc"
		pslup.PPS=400
		pslup.YGravity=0
		pslup.Friction=0.0
		pslup.RandomVelocity=-2
		pslup.NormalVelocity=-20
		pslup.FollowFactor=0.0
		pslup.Time2Live=50
		pslup.Velocity=0.0, 0.0, 0.0
		pslup.DeathTime=Bladex.GetTime()+1.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, self.DGLUP2, ())

	def EndPhase1 (self,EntityName):
		print "End Phase 1"
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()

		#me.LaunchAnimation("Dgk_lifeup1")
		#me.AnmEndedFunc=self.StartPhase2
		#anim_duration= Bladex.GetAnimationDuration("Dgk_lifeup1")
		#Bladex.AddScheduledFunc(Bladex.GetTime()+anim_duration, self.StartPhase2, (EntityName,), EntityName+" StartPhase2")
		self.StartPhase2(EntityName)
		Dgk=Bladex.GetCharType("DalGurak","Dgk")
		Dgk.DistStop=4000.0
		print "EndPhase1"

	def StartPhase2 (self,EntityName):
		if self.Phase != 2:
			print "StartPhase2"
			self.Phase=2
			me = Bladex.GetEntity (EntityName)
			me.Blind= 0
			me.Deaf= 0
			inv= me.GetInventory ()
			if self.Dalweapon:
				inv.LinkRightHand (self.Dalweapon.Name)
				self.Fader.Entities2Fade.append (me.InvRight)
			else: print "Error obtaining Dalweapon"
			if self.Dalshield:
				inv.LinkLeftHand (self.Dalshield.Name)
				self.Fader.Entities2Fade.append (me.InvLeft)
			else: print "Error obtaining Dalshield"
			self.ResetCombat (EntityName)
			me.Wuea= Reference.WUEA_ENDED
			me.InterruptCombat()
			me.LaunchAnimation("Dgk_rlx_1h")
			# Following is to reset the chase
			me.ResetChase()
			self.Invincibility=0

	def LevelUp (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.Level = me.Level +1
		me.Life= CharStats.GetCharMaxLife(me.Kind, me.Level)
		time= Bladex.GetTime()
		if me.Level < 19:
			Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,), EntityName+" LevelUp")
		else:
			self.Invincibility=0

	def LifeUp (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Level <= 9:
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			me.LaunchAnmType("lifeup1")
			self.Invincibility=2
			time= Bladex.GetTime()
			Bladex.AddScheduledFunc(time+self.LevelUpTime, self.LevelUp, (EntityName,), EntityName+" LevelUp")

	########################################################################
	#____ ENERGY BALL FUNCS ________________________________________________
	########################################################################
	def StartBall (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			xl,yl,zl= me.GraspPos("L_Hand")
			xr,yr,zr= me.GraspPos("R_Hand")
			vx,vy,vz= me.Rel2AbsVector(0,-800.0,0.0)
			x,y,z= (xl+xr)*0.5+vx, (yl+yr)*0.5+vy, (zl+zr)*0.5+vz
			self.AGE_Number=self.AGE_Number+1
			ball= ItemTypes.MakeDalBall(EntityName+"_DalBall"+`self.AGE_Number`, x,y,z, EntityName)
			self.BallName= ball.Name

	def ShootBall (self,EntityName,EventName):
		ball= Bladex.GetEntity(self.BallName)
		if ball:
			ball.Data.ReleaseThrownWeaponHandler (self.BallName, "")

	def LaunchFireBall (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.SetNextAttack("GM02")
			return 1
		return 0

	########################################################################
	#____ THROWN DISK FUNCS ________________________________________________
	########################################################################
	def CreateDisk (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			print "Making Disk"
			x,y,z= me.GraspPos("R_Hand")
			self.AGE_Number=self.AGE_Number+1
			missile=ItemTypes.MakeDalBlade("ThrownRing"+`self.AGE_Number`, x,y-600,z, me.Name)
			self.MissileName= missile.Name

	def ShootDisk (self,EntityName,EventName):
		missile= Bladex.GetEntity(self.MissileName)
		if missile:
			missile.Data.ThrowReleaseEventHandler (self.MissileName, "")


	def LaunchMissile (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			#pdb.set_trace()
			me.SetNextAttack("GM01")
			return 1
		return 0

	########################################################################
	#____ THROWN WEAPON FUNCS ______________________________________________
	########################################################################
	def LaunchWeapon (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0 and Actions.StatR(EntityName) != Actions.RA_NO_WEAPON:
			weapon= Bladex.GetEntity(me.InvRight)
			if weapon and weapon.Data and weapon.Data.SetTarget:
				weapon.Data.SetTarget(me.GetEnemyName())
			me.SetNextAttack("GTH5")
			return 1
		return 0

	def BoomerangWeapon (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		try:
			weapon= Bladex.GetEntity(me.InvRight)
			if weapon and weapon.Data and weapon.Data.ThrowReleaseEventHandler:
				weapon.Data.ThrowReleaseEventHandler (me.InvRight, EventName)
		except AttributeError:
			pass

################################################################################


################################################################################
# Define the Golem_stone class
################################################################################
class Golem_stone (Enm_Def.NPCPerson):

	#variables
	AGE= 0
	StoneType="Piedra_Glm_st"
	StoneGrowTime= 0.8
	ScaleVar= 0.0
	AlphaVar= 0.0
	StoneAlpha=1.0
	StoneSelfIlum=0.0


	def __init__(self, me):
		# base class init
		Enm_Def.NPCPerson.__init__(self, me)

		self.DamageFactorNone  = 0.25
		self.DamageFactorLight = 0.25

		# Set up traitor knight specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW]   = 10.0
		self.SoundPriorities[Reference.SND_HIT]     = 50.0
		self.SoundPriorities[Reference.SND_NPC]     = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC]      = 80.0

		# constants
		me.AddAnmEventFunc("StoneAppears", self.StoneAppearsHandler)
		me.OnStepFunc = darfuncs.QuakeStep
		me.ImDeadFunc=self.ImDeadFunc

		#variables
		self.NoFXOnHit= TRUE

	def ResetSounds(self, EntityName):
		me=Bladex.GetEntity(EntityName)
		if me.Kind=="Golem_stone":
			AniSound.AsignarSonidosGolem_st(EntityName)
		elif me.Kind=="Golem_clay":
			AniSound.AsignarSonidosGolem_cl(EntityName)
		elif me.Kind=="Golem_lava":
			AniSound.AsignarSonidosGolem_lv(EntityName)
		elif me.Kind=="Golem_metal":
			AniSound.AsignarSonidosGolem_mt(EntityName)
		elif me.Kind=="Golem_ice":
			AniSound.AsignarSonidosGolem_ic(EntityName)

	# Functions for loading and saving state
	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		#self.changed_func[6] = 1
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		me=Bladex.GetEntity(self.Name)

		if(NPCPerson_state[0]!=1):
			print "ERROR: Golem_stone.__getstate__(): Base class version differs."
			# Throw?
			return NPCPerson_state
		NPCPerson_state[1][me.Kind]=(self.AGE,
						self.StoneType,
						self.StoneGrowTime,
						self.ScaleVar,
						self.AlphaVar,
						self.StoneAlpha,
						self.StoneSelfIlum)

		return NPCPerson_state
		#self.ResetCombat(me.Name)

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		me=Bladex.GetEntity(self.Name)

		version=parm[0]
		if version==1:
			parms=parm[1][me.Kind]
			self.AGE=parms[0]
			self.StoneType=parms[1]
			self.StoneGrowTime=parms[2]
			self.ScaleVar= parms[3]
			self.AlphaVar= parms[4]
			self.StoneAlpha= parms[5]
			self.StoneSelfIlum= parms[6]

		me.AddAnmEventFunc("StoneAppears", self.StoneAppearsHandler)
		me.OnStepFunc = darfuncs.QuakeStep
		#me.ImDeadFunc=self.ImDeadFunc
		self.NoFXOnHit= TRUE

	def ImDeadFunc (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.2, self.Destroza,(EntityName,))

	def Destroza(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.SeverLimb(1)
		me.SeverLimb(2)
		me.SeverLimb(4)
		me.SeverLimb(6)
		me.SeverLimb(8)
		me.CastShadows = 0

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=TRUE
			self.AttackNPCTime = 2.0
			me.BlockingPropensity = 0.2
			me.AttackList = BCopy.deepcopy(Combat.StoneGolemAttackData)
			self.ChanceOfFuryOnHurt = 0.0
			self.ChanceOfFuryOnLeaderDeath = 0.0

	def ScaleStone (self, obj_name, time):
		obj= Bladex.GetEntity(obj_name)
		parent= obj.Parent
		if parent:
			me = Bladex.GetEntity(parent)
			me.Unlink(obj)
		obj.Scale= obj.Scale+self.ScaleVar
		if obj.Scale>=1.0:
			obj.Scale= 1.0
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""
		if parent:
			me.GetInventory().LinkLeftHand(obj.Name)

	def DownScaleStone (self, obj_name, time):
		obj= Bladex.GetEntity(obj_name)
		parent= obj.Parent
		if parent:
			me = Bladex.GetEntity(parent)
			if me and me.Person and me.InvLeft==obj_name:
				inv= me.GetInventory()
				inv.LinkLeftHand(NULL)
			me.Unlink(obj)

		obj.Scale= max (0,0, obj.Scale-self.ScaleVar)
		obj.Alpha= max (0,0, obj.Alpha-self.AlphaVar)
		if obj.Scale<=0.0 or obj.Alpha<=0.0:
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""
			obj.RemoveFromWorld()
			obj.SubscribeToList("Pin")

	def StoneStopFunc (self, EntityName):
		print "stopping stone ",EntityName
		stone= Bladex.GetEntity(EntityName)
		if stone:
			stone.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
			stone.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
			stone.Alpha=self.StoneAlpha
			stone.TimerFunc= self.DownScaleStone
			stone.SubscribeToList("Timer60")

	def StoneAppearsHandler (self,EntityName,EventName):
		me = Bladex.GetEntity(EntityName)
		if not me.InvLeft:
			self.AGE= self.AGE+1
			x,y,z= me.GraspPos("L_Hand")
			stone= Bladex.CreateEntity(EntityName+"_"+self.StoneType+"_"+`self.AGE`, self.StoneType, x,y,z, "Weapon")
			stone.Mass= 5
			init_scale= 0.25
			stone.Alpha=self.StoneAlpha
			stone.Scale= init_scale
			stone.SelfIlum= self.StoneSelfIlum

			self.ScaleVar= (1.0-init_scale)/(60.0*self.StoneGrowTime)
			self.AlphaVar= self.ScaleVar
			stone.TimerFunc= self.ScaleStone
			stone.SubscribeToList("Timer60")
			stone.OnStopFunc= self.StoneStopFunc

			me.GetInventory().LinkLeftHand(stone.Name)
			me.Data.ThrowForce= 2.0
			stone.ExcludeHitFor(me)
		me.AddAnmEventFunc("ThrowLeftEvent",self.ThrowReleaseEventHandler)

	def ThrowReleaseEventHandler(self, EntityName, EventName):
		me = Bladex.GetEntity(EntityName)

		Actions.ThrowReleaseEventHandler(EntityName, EventName)

		if me.InvLeft:
			object = Bladex.GetEntity(me.InvLeft)
			object.TimerFunc=""
			object.SubscribeToList("Pin")
			inv=me.GetInventory()
			inv.LinkLeftHand("None")

################################################################################
# Define the Golem_clay class
################################################################################
class Golem_clay (Golem_stone):
	def __init__(self, me):
		# base class init
		Golem_stone.__init__(self, me)
		self.StoneType="Piedra_Glm_cl"
		self.ClaySmoke(me.Name)
		me.ImDeadFunc=self.ImDeadFunc

	def ImDeadFunc (self,EntityName):
		self.StopSmoke(EntityName)
		Enm_Def.NPCPerson.StdImDead(self,EntityName)

	def ClaySmoke(self,EntityName):
		pslup=Bladex.CreateEntity(EntityName+" hedorshit", "Entity Particle System Dperson", 0, 0, 0)
		pslup.PersonName=EntityName
		pslup.ParticleType="ShitSmoke"
		pslup.PPS=48
		pslup.YGravity=0
		pslup.Friction=0.0
		pslup.RandomVelocity=1
		pslup.NormalVelocity=2
		pslup.FollowFactor=0
		pslup.Time2Live=64
		pslup.Velocity=0.0, -100.0, 0.0
		#self.pslup.DeathTime=Bladex.GetTime()+5.0

	def StopSmoke(self,EntityName):
		self.pslup=Bladex.GetEntity(EntityName+" hedorshit")
		self.pslup.DeathTime=Bladex.GetTime()

################################################################################
# Define the Golem_lava class
################################################################################
class Golem_lava (Golem_stone):
	def __init__(self, me):
		# base class init
		Golem_stone.__init__(self, me)
		self.StoneType="Piedra_Glm_lv"
		self.StoneSelfIlum=1.0

################################################################################
# Define the Golem_metal class
################################################################################
class Golem_metal (Golem_stone):
	def __init__(self, me):
		# base class init
		Golem_stone.__init__(self, me)
		self.StoneType="Piedra_Glm_mt"

################################################################################
# Define the Golem_ice class
################################################################################
class Golem_ice (Golem_stone):      ### Proper implementation of Ice Golem. Needs to be revisited, might have unneeded variables -LeadHead

    ag=None

    def __init__(self,me):
        # base class init
        me.Alpha=0.6
        me.SelfIlum=0.8
        Golem_stone.__init__(self, me)
        self.StoneType="Piedra_Glm_ic"
        self.StoneAlpha=0.6
        self.StoneSelfIlum=0.8
        
        ### Aura specifically for Ice Golem
        self.ag=Bladex.CreateEntity(me.Name+"_Aura", "Entity Aura", 0, 0, 0)
        me.Link(self.ag)
        self.ag.SetAuraParams(50, 1, 1, 0, 0, 1)
        self.ag.SetAuraGradient(2, 0.9, 1.0, 1.0, 0.2, 0.1, 0.4, 0.8, 1.0, 0.0, 0.8)
        self.ag.SetAuraActive(1)
        
        
    def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		me=Bladex.GetEntity(self.Name)
		version=parm[0]
		if version==1:
			parms=parm[1][me.Kind]
			self.AGE=parms[0]
			self.StoneType=parms[1]
			self.StoneGrowTime=parms[2]
			self.ScaleVar= parms[3]
			self.AlphaVar= parms[4]
			self.StoneAlpha= parms[5]
			self.StoneSelfIlum= parms[6]
			self.ag=Bladex.CreateEntity(me.Name+"_Aura", "Entity Aura", 0, 0, 0)
			self.ag.SetAuraParams(50, 1, 1, 0, 0, 1)
			self.ag.SetAuraGradient(2, 0.9, 1.0, 1.0, 0.2, 0.1, 0.4, 0.8, 1.0, 0.0, 0.8)
			self.ag.SetAuraActive(1)
		
		me.AddAnmEventFunc("StoneAppears", self.StoneAppearsHandler)
		me.OnStepFunc = darfuncs.QuakeStep
		self.NoFXOnHit= TRUE
		me.Alpha=0.6
        

        
################################################################################
# Define the Ragnar class
################################################################################
class Ragnar(Enm_Def.NPCPerson):

	risaragnar=None
	ChanceOfFury=0.0

	def __init__(self, person):
		# base class init
		Enm_Def.NPCPerson.__init__(self, person)

		# Set up orc specific sound priorities
		self.SoundPriorities[Reference.SND_ARROW] = 10.0
		self.SoundPriorities[Reference.SND_HIT] = 50.0
		self.SoundPriorities[Reference.SND_NPC] = 25.0
		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
		self.SoundPriorities[Reference.SND_PC] = 80.0

		self.risaragnar=Bladex.CreateSound("../../Sounds/risa-ragnar.wav", "RisaRagnar")
		self.risaragnar.Volume=1
		#self.risaragnar.Scale=0.56
		#self.risaragnar.MinDistance=500
		#self.risaragnar.MaxDistance=90000
		self.risaragnar.Scale=1.0
		self.risaragnar.MinDistance=5000
		self.risaragnar.MaxDistance=20000

	# Functions for loading and saving state
	def __getstate__(self):
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			print "ERROR: Ragnar.__getstate__(): Base class version differs."
			return NPCPerson_state

		me=Bladex.GetEntity(self.Name)
		NPCPerson_state[1]["Ragnar"]=(self.risaragnar.Name,
										None, # used to be SeeFunc, now just empty placeholder to maintain savegame compatibility
										self.ChanceOfFury)
		return NPCPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["Ragnar"]
			risaragnar_Name=parms[0]
			self.risaragnar=Bladex.GetSound(risaragnar_Name)
			me=Bladex.GetEntity(self.Name)
			self.ChanceOfFury=parms[2]

	def ResetSounds(self, EntityName):
		AniSound.AsignarSonidosRagnar(EntityName)

	def Laugh(self, entity_name):
		me=Bladex.GetEntity(self.Name)
		rgpos=me.Position
		self.risaragnar.Play(rgpos[0], rgpos[1], rgpos[2], 0)

	def Escaping(self, risa=0):
		person=Bladex.GetEntity(self.Name)
		person.LaunchAnimation("Rgn_escape")
		if risa:
			person.AnmEndedFunc=self.Laugh

	def CommandingAndEscaping(self, risa=0):
		person=Bladex.GetEntity(self.Name)
		person.LaunchAnimation("Rgn_escape2")
		if risa:
			person.AnmEndedFunc=self.Laugh

	def ResetCombat (self,EntityName):
		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			self.AttacksOwnKind=0
			self.ChanceOfFury = 0.00
			inv= me.GetInventory()
			if inv.HoldingShield:
				me.BlockingPropensity = 1.0
				me.RangeDefenceCapable = TRUE
			else:
				me.BlockingPropensity = 0.2
				me.RangeDefenceCapable = FALSE
			me.AttackList = BCopy.deepcopy(Combat.RagnarAttackData)
################################################################################

################################################################################
# Parse the CharType  automatically
################################################################################
classes_defined= dir()
def EnemyDefaultFuncs (pers):
	if pers.CharType in classes_defined:
		exec_string = 'pers.Data=' + pers.CharType + '(pers)'
		exec (exec_string)
		Bladex.CheckPyErrors()
		if not pers.Data:
			raise NameError, 'CharType must not have valid associated class'
		Bladex.CheckPyErrors()
	else:
		print "WARNING: "+pers.CharType+" is an unrecognised class in EnemyTypes.py!"
		pers.Data= Enm_Def.NPCPerson (pers)
################################################################################