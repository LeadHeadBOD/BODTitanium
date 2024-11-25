##///
##||| ITEMTYPES.PY TITANIUM
##||| Change list:
##||| * BladeSwords now have a less annoying idle sound.
##||| * BladeSword no longer returns to player if player is dead.
##||| * Dark Lord large seeking sphere now properly ends looping sound if it hits world.
##||| * 
##||| * 
##\\\ 


import Bladex
import Sparks
import CharStats
import pdb
import Reference
import Actions
import math
import AuxFuncs
import InitDataField
import Objects
import whrandom
import BCopy
import B3DLib
import netgame
import Damage
import Breakings
import Auras
import GenFX
import ObjStore
import GameStateAux

class PersistantItemType:
	def __init__(self, me):
		self.ObjId= ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]= self

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver cómo poder guardar el estado de la clase
		return (
			1,
			{"PersistantItemType": (self.ObjId, GameStateAux.SaveNewMembers(self))},
		)

	def __setstate__(self, parm):
		if parm[0] == 1:
			parms = parm[1]["PersistantItemType"]
			self.ObjId = parms[0]
			ObjStore.ObjectsStore[self.ObjId] = self
			# Backward compatible
			if len(parms) > 1:
				GameStateAux.LoadNewMembers(self, parms[1])
		else:
			print "ItemOfProtection.__setstate__() -> Version mismatch"
			self.ObjId = ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId] = self





class ActivateableSpecialWeapon(PersistantItemType):
	def __init__ (self, me):
		PersistantItemType.__init__(self, me)
		self.SpecialWeaponActive= 0
		self.SpecialWeaponActivatedKey= 0
		self.SpecialExtraDamage= []
		self.WeaponFX= None
		GenFX.AddWeaponFX(me.Name, self)
		self.Name= me.Name

	def __getstate__(self):

		state= PersistantItemType.__getstate__(self)
		state[1]["ActivateableSpecialWeapon"]=(self.SpecialWeaponActive,
									self.SpecialWeaponActivatedKey,
##									GameStateAux.SaveObjectAux(self.WeaponFX)
									self.WeaponFX,
									self.SpecialExtraDamage,
									self.Name
									)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["ActivateableSpecialWeapon"]
			self.SpecialWeaponActive=parms[0]
			self.SpecialWeaponActivatedKey= parms[1]
##			GameStateAux.LoadObjectAux(parms[2],self,"WeaponFX")
			self.WeaponFX=parms[2]
			self.SpecialExtraDamage=parms[3]
			self.Name= parms[4]
		else:
			self.SpecialWeaponActive=0
			self.SpecialWeaponActivatedKey=0
			GenFX.AddWeaponFX(me.Name, self)
			self.SpecialExtraDamage= []
			self.Name=""

	def Start_Weapon_Special (self, EntityParentName,EventName):
		previously_active= self.SpecialWeaponActive
		self.SpecialWeaponActive= 1
		print "Start_Weapon_Special active"

		if not previously_active:
			# increase the damage data
			if not Reference.EntitiesObjectData.has_key (self.Name):
				obj= Bladex.GetEntity(self.Name)
				if obj:
					Reference.EntitiesObjectData[self.Name]= BCopy.deepcopy(Reference.DefaultObjectData[obj.Kind])

			if not Reference.EntitiesObjectData.has_key (self.Name):
				print "Start_Weapon_Special() Cannot create a dictionary entry for "+`self.Name`
				return

			for damage in self.SpecialExtraDamage:
				Reference.EntitiesObjectData[self.Name].append (damage)

		# Organize the switch off, based on a key, so that our switch off corresponds just to THIS switch on
		self.SpecialWeaponActivatedKey= time= Bladex.GetTime()
		parent= Bladex.GetEntity (EntityParentName)
		if parent:
			anim_duration= Bladex.GetAnimationDuration(parent.AnimFullName)
			if not anim_duration:
				anim_duration= 1.0
			anm_pos= parent.AnmPos
			time2finish= time+(1.0-anm_pos)*anim_duration   # PLAGUE: bug - we never check if the user is still in the same anim. Special damage can be transferred across attacks if cancelled.
		else:
			time2finish= time+2.0
		Bladex.AddScheduledFunc (time2finish, self.Stop_Weapon_Special, (EntityParentName,"Stop_Weapon_Special", self.SpecialWeaponActivatedKey) , self.Stop_Weapon_Special.__name__)

	def Stop_Weapon_Special (self, EntityParentName,EventName, Key=-1):
		if Key!=-1:
			if Key != self.SpecialWeaponActivatedKey:
				return

		if not self.SpecialWeaponActive:
			return

		self.SpecialWeaponActive= 0

		print "Start_Weapon_Special deactivated"

		if Reference.EntitiesObjectData.has_key (self.Name):
			for damage in self.SpecialExtraDamage:
				Reference.EntitiesObjectData[self.Name].remove (damage)
#
# Constants
#
class TaiSword:
	def __init__ (self, me):
		GenFX.AddWeaponFX(me.Name, self)	# PLAGUE: Does not exist for TaiSword


#
# Activated
#
class CrushHammer (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Venom",+6.0],]

class SteelFeather (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Venom",+6.0],]

class QueenSword (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [['Drain'],]

class FireBigSword (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Fire", +30.0],]

class FireAxe (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Fire", +30.0],]

class FireSword (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Fire", +30.0],]

class FireBo (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Fire", +30.0],]

class IceAxe (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Ice", +30.0],]

class IceHammer (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Ice", +30.0],]

class IceSword (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Ice", +30.0],]

class IceWand (ActivateableSpecialWeapon):
	def __init__ (self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Ice", +30.0],]

class Meteorito:
	def __init__(self, me, vx,vy,vz):

		me.CastShadows=0
		me.Intensity=0
		me.Damage=1
		me.Visible=0

		me.Velocity= vx,vy,vz

		meteorite= Bladex.CreateEntity(me.Name+"_Shell", "Meteorito", 0,0,0)
		me.Link(meteorite)

		# Create a particle system to link
		fireball=Bladex.CreateEntity(me.Name+"_Fire", "Entity Particle System Dobj", 0, 0, 0)
		fireball.ObjectName=meteorite.Name
		fireball.ParticleType="RedMagicMissile"
		fireball.PPS=100
		fireball.YGravity=0.0
		fireball.Friction=0.04
		fireball.Velocity=0.0, 0.0, 0.0
		fireball.RandomVelocity=-5.0
		fireball.Time2Live=25
		self.Hit= 0
		#self.CreateTestParticle(fireball.Name, 0.1)
		self.Name= me.Name
		me.OnHitFunc= self.OnHitFunc
		Reference.EntitiesObjectData[me.Name]= BCopy.deepcopy(Reference.DefaultObjectData[meteorite.Kind])

	def OnHitFunc (self, EntityName, hit_entity):
		# NOTE: if the DamagePoints parameter has been set to 0,
		# then collisions will only be calculated with the world
		# Manuel:  We need an explosion effect here
		# ....
		if not self.Hit:
			if Reference.EntitiesObjectData.has_key(EntityName):
				del Reference.EntitiesObjectData[EntityName]
			self.Hit= 1

		if hit_entity:
			print EntityName+" hitting "+hit_entity
			me=Bladex.GetEntity(EntityName)
			if me:
				me.SubscribeToList("Pin")
		else:
			pass
			# print EntityName+" hitting world"

	def CreateTestParticle(self, fireball_name,period):
		fireball=Bladex.GetEntity(fireball_name)
		if(fireball and not self.Hit):
			prtl=fireball.GetParticleEntity()
			prtl.HitFunc=self.FirePrtlHit
			prtl.ObjCTest= 1
			Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.CreateTestParticle,(fireball_name,period), fireball_name+"_CreateTestParticle")

	# When fire hits the player
	def FirePrtlHit(self, prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld":
			if not self.Hit:
				victim= Bladex.GetEntity(hit_entity)
				print " Fire hitting "+hit_entity
				if victim.Person:
					weapon= Bladex.GetEntity(self.Name)
					if weapon:
						victim.DamageFunc(hit_entity, "", self.Name, "Fire", 1, -1, x, y, z, 0)

						# Override hurt anim
						if victim.Life>0:
							if victim.InCombat:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
							else:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
					self.OnHitFunc(self.Name,hit_entity)
				elif victim.Weapon:
					pass

class BolaDalGurak(PersistantItemType):
	DamageEntityName=""
	Name=""
	OwnerName=""
	Hit=0
	Fired=0
	MissileShootSound=None
	MissileWhileSound=None
	MissileImpactSound=None
	ThrownBy=None
	FirePS=None

	def __init__(self, me, ownerName):
		PersistantItemType.__init__(self, me)
		me.CastShadows= 0
		me.Visible= 0
		me.Flick=1
		me.Color=140, 255, 160
		me.Intensity=0.0
		me.Damage=1
		me.DamageRadius=500.0

		ball=Bladex.CreateEntity(me.Name+"_Shell", "EsferaOrbital", 0,0,0)
		ball.Orientation=0.707107,0.707107,0.000000,0.000000
		ball.RasterMode="Read"
		ball.RasterMode="AdditiveAlpha"
		ball.Alpha=0.0
		ball.SelfIlum=0.5
		ball.CastShadows=0

		AuxFuncs.FadeObject(ball.Name, 0.0, 0.99, 2.0)

		self.DamageEntityName=ball.Name
		self.Name=me.Name
		self.OwnerName=ownerName
		self.Hit=0
		self.Fired=0

		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, self.IntensityVarWithoutTimer, (0.1, 2.0))

		# Create and link a particle system here
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, self.CreateFireball, ())

		me.OnHitFunc=self.PrevOnHitFunc
		me.InflictHitFunc= self.BolaDalGurakInflictHitFunc
		me.TimerFunc=self.MoveAndRotateBall
		me.SubscribeToList("Timer30")

		# Create an energy concentration effect here for 1.0 second
		concball=Bladex.CreateEntity(me.Name+"_Conc","Entity Particle System Dobj", 0, 0, 0)
		concball.ObjectName=ball.Name
		concball.ParticleType="DeepGreenEnergyConc"
		concball.PPS=2000
		concball.YGravity=0.0
		concball.Friction=0.0
		concball.RandomVelocity=-5.0
		concball.NormalVelocity=-15.0
		concball.Time2Live=20
		concball.FollowFactor=0.1
		concball.DeathTime=Bladex.GetTime()+1.0

		concsound=Bladex.CreateEntity(me.Name+"ConcSound", "Entity Sound", 0, 0, 0)
		concsound.SetSound("../../Sounds/energy-ball-conc.wav")
		concsound.MinDistance=5000
		concsound.MaxDistance=30000
		me.Link(concsound)
		concsound.PlaySound(0)

		self.SetMissileSound("shoot", "../../Sounds/Fireball-Fire.wav")
		self.SetMissileSound("while", "../../Sounds/energy-ball.wav")
		self.SetMissileSound("impact", "../../Sounds/energy-ball-impact.wav")

		Bladex.AddScheduledFunc(Bladex.GetTime()+20.0, self.BallDissipation, (), "PostFunc"+me.Name)
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, self.ReleaseThrownWeaponHandler, (me.Name, ""))

		Reference.EntitiesObjectData[me.Name]= BCopy.deepcopy(Reference.DefaultObjectData[ball.Kind])

	def __getstate__(self):

		state= PersistantItemType.__getstate__(self)
		MissileShootSoundName= ""
		MissileWhileSoundName= ""
		MissileImpactSoundName= ""
		ThrownByName=""
		FirePSName=""
		if self.MissileShootSound: MissileShootSoundName= self.MissileShootSound.Name
		if self.MissileWhileSound: MissileWhileSoundName= self.MissileWhileSound.Name
		if self.MissileImpactSound: MissileImpactSoundName= self.MissileImpactSound.Name
		if self.ThrownBy: ThrownByName=self.ThrownBy.Name
		if self.FirePS: FirePSName= self.FirePS.Name

		state[1]["BolaDalGurak"]=(self.DamageEntityName,
									self.Name,
									self.OwnerName,
									self.Hit,
									self.Fired,
									MissileShootSoundName,
									MissileWhileSoundName,
									MissileImpactSoundName,
									ThrownByName,
									FirePSName
									)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["BolaDalGurak"]
			MissileShootSoundName=""
			MissileWhileSoundName=""
			MissileImpactSoundName=""
			ThrownByName=""
			FirePSName=""

			(self.DamageEntityName,
			self.Name,
			self.OwnerName,
			self.Hit,
			self.Fired,
			MissileShootSoundName,
			MissileWhileSoundName,
			MissileImpactSoundName,
			ThrownByName,
			FirePSName)= parms

			if MissileShootSoundName:
				self.MissileShootSound= Bladex.GetEntity(MissileShootSoundName)
			if MissileWhileSoundName:
				self.MissileWhileSound= Bladex.GetEntity(MissileWhileSoundName)
			if MissileImpactSoundName:
				self.MissileImpactSound= Bladex.GetEntity(MissileImpactSoundName)
			if ThrownByName:
				self.ThrownBy=Bladex.GetEntity(ThrownByName)
			if FirePSName:
				self.FirePS=Bladex.GetEntity(FirePSName)

		if self.Name:
			me=Bladex.GetEntity(self.Name)
			if me:
				me.OnHitFunc=self.PrevOnHitFunc
				me.InflictHitFunc= self.BolaDalGurakInflictHitFunc
				me.TimerFunc=self.MoveAndRotateBall
				me.SubscribeToList("Timer30")

	def SetMissileSound(self, kind, wavfile):
		missile=Bladex.GetEntity(self.Name)
		if missile:
			if kind=="shoot":
				missilesound=Bladex.CreateEntity(self.Name+"ShootSound", "Entity Sound", 0, 0, 0)
				self.MissileShootSound=missilesound
			elif kind=="while":
				missilesound=Bladex.CreateEntity(self.Name+"WhileSound", "Entity Sound", 0, 0, 0)
				self.MissileWhileSound=missilesound
			elif kind=="impact":
				missilesound=Bladex.CreateEntity(self.Name+"ImpactSound", "Entity Sound", 0, 0, 0)
				self.MissileImpactSound=missilesound
			missilesound.SetSound(wavfile)
			missilesound.Volume=1.0
			missilesound.MinDistance=5000
			missilesound.MaxDistance=30000
			missile.Link(missilesound)

	def BallDissipation(self):
		missile=Bladex.GetEntity(self.Name)
		ball=Bladex.GetEntity(self.DamageEntityName)
		if missile:
			intred=0.2 #2.0/10.0
			escred=0.1 #1.0/10.0
			rndvelred=-2.0 #-20.0/10.0
			PPSred=150.0 #1200/8.0
			Alphared=0.099 #0.99/10.0
			sndred=0.1 #1.0/10.0
			missile.Intensity=max(0.0, missile.Intensity-intred)
			ball.Scale=max(0.0, ball.Scale-escred)
			ball.Alpha=max(0.0, ball.Alpha-Alphared)
			self.FirePS.RandomVelocity=self.FirePS.RandomVelocity-rndvelred
			self.FirePS.PPS=max(10.0, self.FirePS.PPS-PPSred)
			self.MissileWhileSound.Volume=max(0.0, self.MissileWhileSound.Volume-sndred)
			if missile.Intensity>0.0:
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, self.BallDissipation, (), "PostFunc"+self.Name)
			else:
				self.FirePS.DeathTime=Bladex.GetTime()+1.0/60.0
				missile.Unlink(self.FirePS)
				missile.SubscribeToList("Pin")
				ball.SubscribeToList("Pin")
				self.MissileShootSound=None
				self.MissileWhileSound=None
				self.MissileImpactSound=None
				self.ThrownBy=None
				self.FirePS=None
		elif ball:
			ball.SubscribeToList("Pin")
			self.MissileShootSound=None
			self.MissileWhileSound=None
			self.MissileImpactSound=None
			self.ThrownBy=None
			self.FirePS=None

	def DissipateConc(self):
		shootball=Bladex.CreateEntity(self.Name+"_Shoot","Entity Particle System Dobj", 0, 0, 0)
		shootball.ObjectName=self.DamageEntityName
		shootball.ParticleType="DeepGreenMagicMissile"
		shootball.PPS=1000
		shootball.YGravity=0.0
		shootball.Friction=0.0
		shootball.RandomVelocity=5.0
		shootball.NormalVelocity=20.0
		shootball.Time2Live=30
		shootball.DeathTime=Bladex.GetTime()+0.5

	def IntensityVarWithoutTimer(self, intvar, end_int):
		missile=Bladex.GetEntity(self.Name)
		if missile:
			missile.Intensity=missile.Intensity+intvar
			if missile.Intensity>=end_int:
				missile.Intensity=end_int
			else:
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, self.IntensityVarWithoutTimer, (intvar, end_int))

	def MoveAndRotateBall(self, ent_name, time):
		missile=Bladex.GetEntity(ent_name)
		if missile:
			ball=Bladex.GetEntity(self.DamageEntityName)
			ball.Position=missile.Position
			ball.RotateRel(0.0, 0.0, 0.0, 0, 0, 1, -0.5)

	def CreateFireball(self):
		rayo1=Bladex.CreateEntity(self.Name+"_Ray1", "Entity ElectricBolt", 0.0, 600.0, 600.0)
		rayo1.Target=0.0, -600.0, -600.0
		rayo2=Bladex.CreateEntity(self.Name+"_Ray2", "Entity ElectricBolt", 0.0, 600.0, -600.0)
		rayo2.Target=0.0, -600.0, 600.0
		rayo1.FixedTarget=rayo2.FixedTarget=0
		rayo1.MaxAmplitude=rayo2.MaxAmplitude=600
		rayo1.MinSectorLength=rayo2.MinSectorLength=10000
		rayo1.Damage=rayo2.Damage=0
		rayo1.Active=rayo2.Active=1
		rayo1.CoreGlowColor=rayo2.CoreGlowColor=50.0, 200.0, 50.0
		rayo1.InnerGlowColor=rayo2.InnerGlowColor=10.0, 100.0, 10.0
		rayo1.OuterGlowColor=rayo2.OuterGlowColor=0.0, 0.0, 0.0
		ball=Bladex.GetEntity(self.DamageEntityName)
		ball.Link(rayo1)
		ball.Link(rayo2)
		fireball=Bladex.CreateEntity(self.Name+"_Fire","Entity Particle System D1",0,0,0)
		fireball.ParticleType="DeepGreenMagicMissile"
		fireball.PPS=400
		fireball.YGravity=0.0
		fireball.Friction=0.04
		fireball.RandomVelocity=-16.0
		fireball.FollowFactor=0.4
		fireball.Time2Live=30
		missile=Bladex.GetEntity(self.Name)
		missile.Link(fireball)
		self.FirePS=fireball

	def SetTarget(self, EntityName, OwnerName):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			owner=Bladex.GetEntity(OwnerName)
			if owner:
				missile.ETarget=owner.GetEnemyName()

	def ReleaseThrownWeaponHandler (self,EntityName,EventName):
		if self.Fired:
			return
		self.Fired=1
		me= Bladex.GetEntity(EntityName)
		if not me:
			return
		if not self.OwnerName:
			return
		owner= Bladex.GetEntity(self.OwnerName)
		if not owner:
			return
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, self.SetTarget, (EntityName, self.OwnerName))
		me.Velocity=owner.Rel2AbsVector(0.0, -3500.0, 0.0)
		self.MissileShootSound.PlaySound(0)
		self.MissileWhileSound.PlaySound(-1)
		self.ThrownBy= owner  # this pointer may not be valid
		self.DissipateConc()

	def BolaDalGurakInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		# Called on the impact of the ball on an Entity
		# NOTE: if the Damage parameter has been set to 0, this function will not be called.
		#print EntityName+" inflicting hit to "+VictimName
		if VictimName != "BWorld" and VictimName != self.OwnerName and VictimName != self.DamageEntityName and Bladex.GetEntity(VictimName).Kind[:11] != "MagicShield":
			ball=Bladex.GetEntity(self.DamageEntityName)
			if ball:
				if not self.Hit:
					self.Hit= 1
					victim= Bladex.GetEntity(VictimName)
					#print " Fire hitting "+VictimName
					if victim.Person:
						Bladex.RemoveScheduledFunc("PostFunc"+self.Name)
						ball.Alpha=0.99
						victim.DamageFunc(VictimName, "", self.DamageEntityName, "Fire", 1, -1, ImpX, ImpY, ImpZ, 0)
						# Override hurt anim
						if victim.Life>0:
							if victim.InCombat:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
							else:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
						self.OnHitFunc(self.Name,VictimName)
					elif victim.Weapon:
						if Reference.IsParryingType(victim.Kind):
							Bladex.RemoveScheduledFunc("PostFunc"+self.Name)
							ball.Alpha=0.99
							Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, self.BallDissipation, (), "PostFunc"+self.Name)


	def BallExpansion(self, ent_name, time):
		alpha_var=-0.066 #(0.0-0.99)/(0.5*30.0)
		scale_var=0.133 #(3.0-1.0)/(0.5*30.0)
		y_var=60.0 #900.0/(0.5*30.0)
		ball=Bladex.GetEntity(ent_name)
		x, y, z=ball.Position
		ball.Position=x, y+y_var, z
		ball.RotateRel(0.0, 0.0, 0.0, 0, 0, 1, -0.5)
		ball.Alpha=max(0.0, ball.Alpha+alpha_var)
		ball.Scale=ball.Scale+scale_var
		if ball.Scale>=3.0:
			ball.RemoveFromList("Timer30")
			ball.SubscribeToList("Pin")
			self.MissileShootSound=None
			self.MissileWhileSound=None
			self.MissileImpactSound=None
			self.ThrownBy=None
			self.FirePS=None

	def PrevOnHitFunc (self, EntityName, hit_entity):
		# Called on the impact of the ball with the world, or an Entity (if Damage parameter==1)
		if not hit_entity:
			self.OnHitFunc(EntityName, hit_entity)

	def OnHitFunc (self, EntityName, hit_entity):
		ball_name=self.DamageEntityName
		ball=Bladex.GetEntity(ball_name)
		x, y, z=ball.Position
		ball.SelfIlum=1.0
		impactlight=Bladex.CreateEntity(ball_name+"ImpactLight", "Entity Spot", x, y-800.0, z)
		impactlight.Color=140, 255, 160
		impactlight.Intensity=4.0
		impactlight.Precission=0.1
		impactlight.CastShadows=0
		impactlight.Flick=0
		impactlight.Visible=0
		AuxFuncs.SpotIntensityVariation(impactlight.Name, 4.0, 0.0, 1.4, 1)
		if self.MissileWhileSound: self.MissileWhileSound.StopSound()
		if self.MissileImpactSound: self.MissileImpactSound.PlaySound(0)
		victim= Bladex.GetEntity(hit_entity)
		if victim and victim.Person:
			impactps=Bladex.CreateEntity(ball_name+"ImpactPS", "Entity Particle System Dperson", 0, 0, 0)
			impactps.PersonName=hit_entity
			impactps.ParticleType="DeepGreenMagicMissile"
			impactps.PPS=600
			impactps.YGravity=2000.0
			impactps.Friction=0.0
			impactps.RandomVelocity=5.0
			impactps.NormalVelocity=25.0
			impactps.Velocity=0.0, -1000.0, 0.0
			impactps.Time2Live=30
			impactps.DeathTime=Bladex.GetTime()+0.4
		ball.TimerFunc=self.BallExpansion
		ball.SubscribeToList("Timer30")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,self.DestroyBall,(EntityName,),"DestroyBall"+EntityName)
		missile=Bladex.GetEntity(self.Name)
		missile.RemoveFromList("Timer30")
		missile.SubscribeToList("Pin")
		self.MissileShootSound=None
		self.MissileWhileSound=None
		self.MissileImpactSound=None
		self.ThrownBy=None
		self.FirePS=None
		if Reference.EntitiesObjectData.has_key(EntityName):
			del Reference.EntitiesObjectData[EntityName]

	def DestroyBall(self,EntityName):
		ball_name=self.DamageEntityName
		ball=Bladex.GetEntity(ball_name)
		if ball:
			ball.SubscribeToList("Pin")
			self.MissileShootSound=None
			self.MissileWhileSound=None
			self.MissileImpactSound=None
			self.ThrownBy=None
			self.FirePS=None



class BolaRayos(PersistantItemType):
	DamageEntityName=""
	Name=""
	InvBallName=""
	OwnerName=""
	Hit=0
	Fired=0
	MissileShootSound=None
	MissileWhileSound=None
	MissileImpactSound=None
	ThrownBy=None
	FirePS=None

	def __init__(self, me, ownerName):
		PersistantItemType.__init__(self, me)
		me.CastShadows= 0
		me.Visible= 0
		me.Flick=1
		me.Color=255, 160, 140
		me.Intensity=0.0
		me.Damage= 0

		ball=Bladex.CreateEntity(me.Name+"_Shell", "BolaRayos", 0,0,0)
		ball.RasterMode="Read"
		ball.RasterMode="AdditiveAlpha"
		ball.Alpha=0.0
		ball.SelfIlum=0.5
		ball.CastShadows=0

		invball=Bladex.CreateEntity(ball.Name+"InvBall", "SemiBolaRayos", 0, 0, 0)
		invball.Scale=0.5
		invball.Orientation=0.707107,0.707107,0.000000,0.000000
		invball.Alpha=0.0
		invball.CastShadows=0

		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, AuxFuncs.FadeObject, (ball.Name, 0.0, 0.99, 2.0))

		self.DamageEntityName=ball.Name
		self.Name=me.Name
		self.InvBallName=invball.Name
		self.OwnerName=ownerName
		self.Hit=0
		self.Fired=0

		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, self.IntensityVarWithoutTimer, (0.1, 2.0))

		# Create and link a particle system here
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, self.CreateFireball, ())

		me.OnHitFunc= self.OnHitFunc
		me.InflictHitFunc= self.BolaDarkLordInflictHitFunc
		me.TimerFunc=self.MoveAndRotateBall
		me.SubscribeToList("Timer60")

		# Create an energy concentration effect here for 1.25 seconds
		concball=Bladex.CreateEntity(me.Name+"_Conc","Entity Particle System Dobj", 0, 0, 0)
		concball.ObjectName=ball.Name
		concball.ParticleType="DeepRedEnergyConc"
		concball.PPS=1000
		concball.YGravity=0.0
		concball.Friction=0.0
		concball.RandomVelocity=-5.0
		concball.NormalVelocity=-20.0
		concball.Time2Live=60
		concball.FollowFactor=1.0
		concball.DeathTime=Bladex.GetTime()+1.25

		concsound=Bladex.CreateEntity(me.Name+"ConcSound", "Entity Sound", 0, 0, 0)
		concsound.SetSound("../../Sounds/energy-ball-conc.wav")
		concsound.MinDistance=5000
		concsound.MaxDistance=30000
		me.Link(concsound)
		concsound.PlaySound(0)

		self.SetMissileSound("shoot", "../../Sounds/Fireball-Fire.wav")
		self.SetMissileSound("while", "../../Sounds/energy-ball.wav")
		self.SetMissileSound("impact", "../../Sounds/energy-ball-impact.wav")

		Bladex.AddScheduledFunc(Bladex.GetTime()+20.0, self.BallDissipation, (), "PostFunc"+me.Name)
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, self.ReleaseThrownWeaponHandler, (me.Name, ""))

		Reference.EntitiesObjectData[me.Name]= BCopy.deepcopy(Reference.DefaultObjectData[ball.Kind])

	def __getstate__(self):
		state= PersistantItemType.__getstate__(self)
		MissileShootSoundName= ""
		MissileWhileSoundName= ""
		MissileImpactSoundName= ""
		ThrownByName=""
		FirePSName=""
		if self.MissileShootSound: MissileShootSoundName= self.MissileShootSound.Name
		if self.MissileWhileSound: MissileWhileSoundName= self.MissileWhileSound.Name
		if self.MissileImpactSound: MissileImpactSoundName= self.MissileImpactSound.Name
		if self.ThrownBy: ThrownByName= self.ThrownBy.Name
		if self.FirePS: FirePSName= self.FirePS.Name

		state[1]["BolaRayos"]=(self.DamageEntityName,
								self.Name,
								self.InvBallName,
								self.OwnerName,
								self.Hit,
								self.Fired,
								MissileShootSoundName,
								MissileWhileSoundName,
								MissileImpactSoundName,
								ThrownByName,
								FirePSName
								)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["BolaRayos"]
			MissileShootSoundName=""
			MissileWhileSoundName=""
			MissileImpactSoundName=""
			ThrownByName=""
			FirePSName=""

			(self.DamageEntityName,
			self.Name,
			self.InvBallName,
			self.OwnerName,
			self.Hit,
			self.Fired,
			MissileShootSoundName,
			MissileWhileSoundName,
			MissileImpactSoundName,
			ThrownByName,
			FirePSName)= parms

			if MissileShootSoundName:
				self.MissileShootSound= Bladex.GetEntity(MissileShootSoundName)
			if MissileWhileSoundName:
				self.MissileWhileSound= Bladex.GetEntity(MissileWhileSoundName)
			if MissileImpactSoundName:
				self.MissileImpactSound= Bladex.GetEntity(MissileImpactSoundName)
			if ThrownByName:
				self.ThrownBy=Bladex.GetEntity(ThrownByName)
			if FirePSName:
				self.FirePS=Bladex.GetEntity(FirePSName)

		if self.Name:
			me=Bladex.GetEntity(self.Name)
			if me:
				me.OnHitFunc=self.OnHitFunc
				me.InflictHitFunc= self.BolaDarkLordInflictHitFunc
				me.TimerFunc=self.MoveAndRotateBall
				me.SubscribeToList("Timer60")

	def SetMissileSound(self, kind, wavfile):
		missile=Bladex.GetEntity(self.Name)
		if missile:
			if kind=="shoot":
				missilesound=Bladex.CreateEntity(self.Name+"ShootSound", "Entity Sound", 0, 0, 0)
				self.MissileShootSound=missilesound
			elif kind=="while":
				missilesound=Bladex.CreateEntity(self.Name+"WhileSound", "Entity Sound", 0, 0, 0)
				self.MissileWhileSound=missilesound
			elif kind=="impact":
				missilesound=Bladex.CreateEntity(self.Name+"ImpactSound", "Entity Sound", 0, 0, 0)
				self.MissileImpactSound=missilesound
			missilesound.SetSound(wavfile)
			missilesound.Volume=1.0
			missilesound.MinDistance=5000
			missilesound.MaxDistance=30000
			missile.Link(missilesound)

	def BallDissipation(self):
		missile=Bladex.GetEntity(self.Name)
		ball=Bladex.GetEntity(self.DamageEntityName)
		if missile:
			intred=0.2 #2.0/10.0
			escred=0.1 #1.0/10.0
			rndvelred=-2.0 #-20.0/10.0
			PPSred=150.0 #1200/8.0
			Alphared=0.099 #0.99/10.0
			sndred=0.1 #1.0/10.0
			missile.Intensity=max(0.0, missile.Intensity-intred)
			ball.Scale=max(0.0, ball.Scale-escred)
			ball.Alpha=max(0.0, ball.Alpha-Alphared)
			self.FirePS.RandomVelocity=self.FirePS.RandomVelocity-rndvelred
			self.FirePS.PPS=max(10.0, self.FirePS.PPS-PPSred)
			self.MissileWhileSound.Volume=max(0.0, self.MissileWhileSound.Volume-sndred)
			if missile.Intensity>0.0:
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, self.BallDissipation, (), "PostFunc"+self.Name)
			else:
				invball=Bladex.GetEntity(self.InvBallName)
				self.FirePS.DeathTime=Bladex.GetTime()+1.0/60.0
				missile.Unlink(self.FirePS)
				missile.SubscribeToList("Pin")
				ball.SubscribeToList("Pin")
				invball.SubscribeToList("Pin")
				self.MissileShootSound=None
				self.MissileWhileSound=None
				self.MissileImpactSound=None
				self.ThrownBy=None
				self.FirePS=None
		elif ball:
			ball.SubscribeToList("Pin")
			self.MissileShootSound=None
			self.MissileWhileSound=None
			self.MissileImpactSound=None
			self.ThrownBy=None
			self.FirePS=None

	def DissipateConc(self):
		shootball=Bladex.CreateEntity(self.Name+"_Shoot","Entity Particle System Dobj", 0, 0, 0)
		shootball.ObjectName=self.DamageEntityName
		shootball.ParticleType="DeepRedMagicMissile"
		shootball.PPS=1000
		shootball.YGravity=0.0
		shootball.Friction=0.0
		shootball.RandomVelocity=5.0
		shootball.NormalVelocity=20.0
		shootball.Time2Live=30
		shootball.DeathTime=Bladex.GetTime()+0.5

	def IntensityVarWithoutTimer(self, intvar, end_int):
		missile=Bladex.GetEntity(self.Name)
		if missile:
			missile.Intensity=missile.Intensity+intvar
			if missile.Intensity>=end_int:
				missile.Intensity=end_int
			else:
				Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, self.IntensityVarWithoutTimer, (intvar, end_int))

	def MoveAndRotateBall(self, ent_name, time):
		missile=Bladex.GetEntity(ent_name)
		if missile:
			ball=Bladex.GetEntity(self.DamageEntityName)
			ball.Position=missile.Position
			angle1=whrandom.uniform(-0.3, 0.3)
			angle2=whrandom.uniform(-0.3, 0.3)
			angle3=whrandom.uniform(-0.3, 0.3)
			ball.RotateRel(0.0, 0.0, 0.0, 1, 0, 0, angle1)
			ball.RotateRel(0.0, 0.0, 0.0, 0, 1, 0, angle2)
			ball.RotateRel(0.0, 0.0, 0.0, 0, 0, 1, angle3)

	def CreateFireball(self):
		fireball=Bladex.CreateEntity(self.Name+"_Fire","Entity Particle System D1",0,0,0)
		#fireball.ObjectName=self.DamageEntityName
		fireball.ParticleType="DeepRedMagicMissile"
		fireball.PPS=1000
		fireball.YGravity=0.0
		fireball.Friction=0.04
		fireball.RandomVelocity=-20.0 #2.0
		#fireball.NormalVelocity=10.0
		fireball.Time2Live=30 #27
		missile=Bladex.GetEntity(self.Name)
		missile.Link(fireball)
		self.FirePS=fireball
		self.CreateTestParticle(fireball.Name, 0.1)

	def SetTarget(self, EntityName, OwnerName):
		missile=Bladex.GetEntity(EntityName)
		if missile:
			owner=Bladex.GetEntity(OwnerName)
			if owner:
				missile.ETarget=owner.GetEnemyName()

	def ReleaseThrownWeaponHandler (self,EntityName,EventName):
		if self.Fired:
			return
		self.Fired=1
		me= Bladex.GetEntity(EntityName)
		if not me:
			return
		if not self.OwnerName:
			return
		owner= Bladex.GetEntity(self.OwnerName)
		if not owner:
			return
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, self.SetTarget, (EntityName, self.OwnerName))
		me.Velocity=owner.Rel2AbsVector(0.0, -3500.0, 0.0)
		self.MissileShootSound.PlaySound(0)
		self.MissileWhileSound.PlaySound(-1)
		self.ThrownBy= owner  # this pointer may not be valid
		self.DissipateConc()

	def BolaDarkLordInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		# Called on the impact of the ball on an Entity
		# NOTE: if the DamagePoints parameter has been set to 0, this function will not be called.
		print EntityName+" inflicting hit to "+VictimName

	def BallExpansion(self, ent_name, time):
		alpha_var=-0.033 #(0.0-0.99)/(0.5*60.0)
		scale_var=0.05 #(2.0-0.5)/(0.5*60.0)
		y_var=30.0 #900.0/(0.5*60.0)
		angle1=whrandom.uniform(-0.3, 0.3)
		angle2=whrandom.uniform(-0.3, 0.3)
		angle3=whrandom.uniform(-0.3, 0.3)
		ball=Bladex.GetEntity(ent_name)
		invball=Bladex.GetEntity(self.InvBallName)
		x, y, z=ball.Position
		invball.Position=ball.Position=x, y+y_var, z
		ball.RotateRel(0.0, 0.0, 0.0, 1, 0, 0, angle1)
		ball.RotateRel(0.0, 0.0, 0.0, 0, 1, 0, angle2)
		ball.RotateRel(0.0, 0.0, 0.0, 0, 0, 1, angle3)
		ball.Alpha=max(0.0, ball.Alpha+alpha_var)
		invball.Scale=ball.Scale=ball.Scale+scale_var
		if ball.Scale>=2.0:
			ball.RemoveFromList("Timer60")
			ball.SubscribeToList("Pin")
			self.MissileShootSound=None
			self.MissileWhileSound=None
			self.MissileImpactSound=None
			self.ThrownBy=None
			self.FirePS=None
			invballdin=Objects.CreateDinamicObject(invball.Name)
			Objects.DisplaceObject(invballdin, 5000.0, (0, 1, 0), y_var*60.0, 12000.0, "", "", "", self.ScaleInvBall, (invball, scale_var), self.RemoveInvBall, (invball,))

	def ScaleInvBall(self, invball, scale_var):
		invball.Scale=invball.Scale+scale_var

	def RemoveInvBall(self, invball):
		Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, invball.SubscribeToList, ("Pin",))

	def OnHitFunc (self, EntityName, hit_entity):
		# Called on the impact of the ball with the world, or an Entity (if DamagePoints parameter==1)
		ball_name=self.DamageEntityName
		ball=Bladex.GetEntity(ball_name)
		x, y, z=ball.Position
		ball.SelfIlum=1.0
		impactlight=Bladex.CreateEntity(ball_name+"ImpactLight", "Entity Spot", x, y-800.0, z)
		impactlight.Color=255, 180, 160
		impactlight.Intensity=4.0
		impactlight.Precission=0.1
		impactlight.CastShadows=0
		impactlight.Flick=0
		impactlight.Visible=0
		AuxFuncs.SpotIntensityVariation(impactlight.Name, 4.0, 0.0, 1.8, 1)
		if self.MissileWhileSound: self.MissileWhileSound.StopSound()							# Moved here to prevent infinite looping sound
		if self.MissileImpactSound: self.MissileImpactSound.PlaySound(0)						#		-LeadHead
		invball=Bladex.GetEntity(self.InvBallName)
		invball.Position=x, y, z
		impactps=Bladex.CreateEntity(ball_name+"ImpactPS", "Entity Particle System Dobj", 0, 0, 0)
		impactps.ObjectName=invball.Name
		impactps.ParticleType="DeepRedMagicMissile"
		impactps.PPS=2000
		impactps.YGravity=0.0
		impactps.Friction=0.0
		impactps.RandomVelocity=5.0
		impactps.Time2Live=30
		impactps.DeathTime=Bladex.GetTime()+2.0
		ball.TimerFunc=self.BallExpansion
		ball.SubscribeToList("Timer60")
		missile=Bladex.GetEntity(self.Name)
		missile.RemoveFromList("Timer60")
		missile.SubscribeToList("Pin")
		self.MissileShootSound=None
		self.MissileWhileSound=None
		self.MissileImpactSound=None
		self.ThrownBy=None
		self.FirePS=None

		if Reference.EntitiesObjectData.has_key(EntityName):
			del Reference.EntitiesObjectData[EntityName]
		#if hit_entity:
		#	print EntityName+" hitting "+hit_entity
		#else:
		#	print EntityName+" hitting world"

	def CreateTestParticle(self, fireball_name, period):		# PLAGUE: This is awful. Do not use particles for hit detection. Rewrite to use generic missile or the entity itself
		fireball=Bladex.GetEntity(fireball_name)
		if(fireball and not self.Hit):
			prtl1=fireball.GetParticleEntity()
			prtl1.HitFunc=self.FirePrtlHit
			prtl1.ObjCTest= 1
			Bladex.AddScheduledFunc(Bladex.GetTime()+period,self.CreateTestParticle,(fireball_name,period), fireball_name+"_CreateTestParticle")

	# When fire hits the player
	def FirePrtlHit(self, prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
		if hit_entity != "BWorld" and hit_entity != self.OwnerName and hit_entity != self.DamageEntityName:
			ball=Bladex.GetEntity(self.DamageEntityName)
			if ball:
				if not self.Hit:
					self.Hit= 1
					victim= Bladex.GetEntity(hit_entity)
					#print " Fire hitting "+hit_entity
					if victim.Person:
						Bladex.RemoveScheduledFunc("PostFunc"+self.Name)
						ball.Alpha=0.99
						victim.DamageFunc(hit_entity, "", self.DamageEntityName, "Fire", 1, -1, x, y, z, 0)
						# Override hurt anim
						if victim.Life>0:
							if victim.InCombat:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
							else:
								victim.Wuea=Reference.WUEA_ENDED
								victim.InterruptCombat()
								victim.LaunchAnmType("hurt_f_big")
						self.OnHitFunc(self.Name,hit_entity)
					elif victim.Weapon:
						pass

class HunterSeekerMissile:

	def __init__(self, me, vx,vy,vz, targetname, owner, onDestroyedFunc):
		# Create a particle system
		# Properties of a magic missile:
		# velocity
		me.CastShadows=0
		me.Velocity= vx,vy,vz
		me.InflictHitFunc= self.MagicMissileInflictHitFunc
		self.Owner= owner
		self.OnDestroyedFunc= onDestroyedFunc
		self.Destroyed= 0

		if targetname:
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, self.SetTarget, (me.Name, targetname), me.Name+" SetTarget to "+targetname)

		# Properties of a particle:
		# Friction, Friction2, DeathTime, Velocity, Gravity, ObjCTest

	def SetTarget(self,EntityName, TargetName):
		if TargetName and not self.Destroyed:
			missile= Bladex.GetEntity(EntityName)
			if missile:
				missile.ETarget= TargetName

	def MagicMissileInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		object= Bladex.GetEntity(EntityName)
		victim= Bladex.GetEntity(VictimName)
		try:
			if not victim.Solid:
				return
		except AttributeError:
			pass
		print "Magic missile hitting "+VictimName
		self.Destroyed= 1
		if self.OnDestroyedFunc:
			self.OnDestroyedFunc(EntityName, self.Owner.Name)




class GenericMissile:

	def __init__(self, missile, owner, onDestroyedFunc):

		missile.InflictHitFunc=self.GenericMissileInflictHitFunc
		self.Owner=owner
		self.OnDestroyedFunc=onDestroyedFunc
		self.Destroyed=0
		self.MissileName=missile.Name
		self.MissileShootSound=""
		self.MissileWhileSound=""
		self.MissileImpactSound=""
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.Owner,
				self.Destroyed,
				self.MissileName,
				self.MissileShootSound,
				self.MissileWhileSound,
				self.MissileImpactSound)

	def __setstate__(self,parm):
		version=parm[0]
		if version==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Owner              = parm[2]
			self.Destroyed          = parm[3]
			self.MissileName        = parm[4]
			self.MissileShootSound  = parm[5]
			self.MissileWhileSound  = parm[6]
			self.MissileImpactSound = parm[7]
		else:
			print "Opps! Invalid Version ;_("

	def SetMissileSound(self, kind, wavfile):
		missile=Bladex.GetEntity(self.MissileName)
		if missile:
			if kind=="shoot":
				missilesound=Bladex.CreateEntity(self.MissileName+"ShootSound", "Entity Sound", 0, 0, 0)
				self.MissileShootSound=missilesound
			elif kind=="while":
				missilesound=Bladex.CreateEntity(self.MissileName+"WhileSound", "Entity Sound", 0, 0, 0)
				self.MissileWhileSound=missilesound
			elif kind=="impact":
				missilesound=Bladex.CreateEntity(self.MissileName+"ImpactSound", "Entity Sound", 0, 0, 0)
				self.MissileImpactSound=missilesound
			missilesound.SetSound(wavfile)
			missilesound.Volume=1.0
			missilesound.MinDistance=5000
			missilesound.MaxDistance=30000
			missile.Link(missilesound)

	def Fire(self, vx, vy, vz, TargetName="", SetTargetTime=0.0, UnSetTargetTime=0.0, PostFunc="", PostFuncTime=0.0):
		missile=Bladex.GetEntity(self.MissileName)
		if missile:
			missile.Velocity=vx, vy, vz
			if self.MissileShootSound:
				self.MissileShootSound.PlaySound(0)
			if self.MissileWhileSound:
				self.MissileWhileSound.PlaySound(-1)
			Bladex.AddScheduledFunc(Bladex.GetTime()+SetTargetTime, self.SetTarget, (missile.Name, TargetName, UnSetTargetTime, PostFunc, PostFuncTime))

	def SetTarget(self, EntityName, TargetName, UnSetTargetTime, PostFunc, PostFuncTime):
		if TargetName and not self.Destroyed:
			missile=Bladex.GetEntity(EntityName)
			if missile:
				missile.ETarget=TargetName
				if UnSetTargetTime:
					Bladex.AddScheduledFunc(Bladex.GetTime()+UnSetTargetTime, self.UnSetTarget, (EntityName,))
				if PostFunc:
					Bladex.AddScheduledFunc(Bladex.GetTime()+PostFuncTime, PostFunc, (EntityName,), "PostFunc"+EntityName)

	def UnSetTarget(self, EntityName):
		if not self.Destroyed:
			missile=Bladex.GetEntity(EntityName)
			if missile:
				missile.ETarget=""

	def RemovePostFunc(self):
		Bladex.RemoveScheduledFunc("PostFunc"+self.MissileName)

	def RemoveMissile(self, playimpactsound=0):
		if self.MissileWhileSound:
			self.MissileWhileSound.StopSound()
		if self.MissileImpactSound and playimpactsound:
			self.MissileImpactSound.PlaySound(0)
		missile=Bladex.GetEntity(self.MissileName)
		missile.SubscribeToList("Pin")

	def GenericMissileInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		object=Bladex.GetEntity(EntityName)
		victim=Bladex.GetEntity(VictimName)
		try:
			if not victim.Solid:
				return
		except AttributeError:
			pass
		print "Generic missile hitting "+VictimName
		self.Destroyed=1
		if self.OnDestroyedFunc:
			self.OnDestroyedFunc(EntityName, self.Owner.Name)




class VampWeapon:
	def __init__(self, me):
		me.Weapon=1
		self.PeriodicDrainTime= 10.0	# every 10 seconds
		self.Name= me.Name
		self.Active=0

		# Create a periodic callback to drain life from the user
		self.Activate()
		GenFX.AddWeaponFX(me.Name, self)
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.Name,
				self.PeriodicDrainTime)

	def __setstate__(self,parm):
		version=parm[0]
		if version==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Name=parm[2]
			self.PeriodicDrainTime =parm[3]
			self.Active=0
			self.Activate()
		else:
			print "Opps! Invalid Version ;_("


	def Activate (self):
		if not self.Active:
			Bladex.AddScheduledFunc(Bladex.GetTime()+self.PeriodicDrainTime, self.Drain, (self.Name,), self.Name+" Drain")
			self.Active= 1

	def Deactivate (self):
		if self.Active:
			Bladex.RemoveScheduledFunc(self.Name+" Drain")
			self.Active= 0

	def Drain (self, EntityName):
		me = Bladex.GetEntity(EntityName)
		# Drain holder... depending on race, level etc
		if me:
			self.PeriodicDrainTime= 10.0
			holder_name= me.Parent
			if holder_name:
				holder= Bladex.GetEntity(holder_name)
				if holder:
					if holder.Kind != "Vamp":
						self.PeriodicDrainTime= holder.Level+1.0
						holder.Life= holder.Life-1
						#
						# Blood aura effect
						time=Bladex.GetTime()
						aura= Auras.MakeAura (holder_name,0.375,   (55, 1.0,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 0.1))
						aura.Data.AddEvent(time+0.25,              (55, 0.8,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 1.0))
						aura.Data.AddEvent(time+0.375,             (255,0.0,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 1.0))


			Bladex.AddScheduledFunc(Bladex.GetTime()+self.PeriodicDrainTime, self.Drain, (self.Name,), self.Name+" Drain")

class VampShield:
	def __init__(self, me):
		me.Weapon=1
		self.Name= me.Name
		self.Rebound= 0.5

	def AbsorbFunc (self, AttackerName, WeaponName, DamagePoints):
		attacker= Bladex.GetEntity(AttackerName)
		if attacker and attacker.Person:
			effective_damage= max(DamagePoints*self.Rebound, 0.0)

			# pasted from Damage.py
			special= ['Drain']
			special_resistance= attacker.Data.GetResistance(special[0])

			if Damage.SpecialDamageFuncs.has_key(special[0]):
				special_damage_func= Damage.SpecialDamageFuncs[special[0]]
				special_damage_func (special, special_resistance, effective_damage, AttackerName, None, self.Name, special[0], Reference.BODY_FRONT, 0, 0, 0, 0, 0)

			LastDamage= min (effective_damage, attacker.Life)*(1.0-special_resistance)
			if LastDamage>0 and not attacker.Data.Invincibility:
				attacker.Life= attacker.Life-LastDamage
			# Potential problem here if attacker is not of human-like bodypart numbering
			DamageZone=Reference.BODY_FRONT
			DamageType="Drain"
			attacker.Data.RespondToHit(AttackerName, self.Name, LastDamage, DamageType, DamageZone, 0)


class MagicShield:
	def __init__(self, me, owner):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

		self.Name= self.CurrentName= me.Name
		self.OwnerName= owner.Name
		self.AuxFuncsData= None

		me.Weapon= 1
		me.Alpha= 0.0
		me.RasterMode="Read"
		me.RasterMode="AdditiveAlpha"
		me.Solid= 0
		me.CastShadows=0
		me.HitShieldFunc= self.TakeImpact
		inv= owner.GetInventory()
		inv.AddMagicShield(self.Name)

		shield2= Bladex.CreateEntity(self.Name+"Phase2","MagicShield2",0,0,0,"Weapon")
		shield2.Solid= 0
		shield2.SelfIlum=1.0
		shield2.Alpha= 0.0
		shield2.RasterMode="Read"
		shield2.RasterMode="AdditiveAlpha"
		shield2.CastShadows=0

		shield3= Bladex.CreateEntity(self.Name+"Phase3","MagicShield3",0,0,0,"Weapon")
		shield3.Solid= 0
		shield3.SelfIlum=1.0
		shield3.Alpha= 0.0
		shield3.RasterMode="Read"
		shield3.RasterMode="AdditiveAlpha"
		shield3.CastShadows=0

		shieldbr= Bladex.CreateEntity(self.Name+"Breaking","MagicShieldBreak",0,0,0,"Weapon")
		shieldbr.Solid= 0
		shieldbr.SelfIlum=1.0
		shieldbr.Alpha= 0.0
		shieldbr.RasterMode="Read"
		shieldbr.RasterMode="AdditiveAlpha"
		shieldbr.CastShadows=0

		self.shieldlight= Bladex.CreateEntity(self.Name+"ImpactLight", "Entity Spot", 0, 0, 0)
		self.shieldlight.Color=0, 0, 0
		self.shieldlight.Intensity=0.0
		self.shieldlight.Precission=0.01
		self.shieldlight.CastShadows=0
		self.shieldlight.Flick=0
		self.shieldlight.Visible=0

		me.Link(shield2)
		me.Link(shield3)
		me.Link(shieldbr)
		me.Link(self.shieldlight)

		self.AGE=0
		self.ParticleData=[]
		self.PrepareParticleData()

		kind = Bladex.GetEntity(self.Name).Kind
		if Reference.DefaultObjectData.has_key(kind):
			Reference.EntitiesObjectData[self.Name]= BCopy.deepcopy(Reference.DefaultObjectData[kind])
			self.MaxDefence= self.Defence= Reference.EntitiesObjectData[self.Name][2]
			self.IntDefence= self.MaxDefence/3.0
		else:
			print "Error -- Cannot find default object data for "+kind
			self.MaxDefence= self.Defence= 0
			self.IntDefence= 0

		# Create a looped sound
		SoundName= "../../Sounds/campo-escudo-barrera1.wav"
		self.loopsound= Bladex.CreateEntity (me.Name+"LoopSound", "Entity Sound", 0, 0, 0)
		self.loopsound.SetSound (SoundName)
		self.loopsound.MinDistance=5000
		self.loopsound.MaxDistance=10000
		owner.Link(self.loopsound)
		self.loopsound.PlaySound(-1)

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.Name,
				self.OwnerName,
				self.CurrentName,
				self.shieldlight,
				self.AGE,
				self.ParticleData,
				self.MaxDefence,
				self.Defence,
				self.IntDefence,
				self.loopsound,
				self.AuxFuncsData,
				)

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Name=parm[2]
			self.OwnerName=parm[3]
			self.CurrentName=parm[4]
			self.shieldlight=parm[5]
			self.AGE=parm[6]
			self.ParticleData=parm[7]
			self.MaxDefence=parm[8]
			self.Defence=parm[9]
			self.IntDefence=parm[10]
			self.loopsound=parm[11]
			self.AuxFuncsData=parm[12]
		else:
			print "Version mismatch in BreakSector"
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Name=""
			self.OwnerName=""
			self.CurrentName=""
			self.shieldlight=None
			self.AGE=0
			self.ParticleData=[]
			self.MaxDefence=0
			self.Defence=0
			self.IntDefence=0
			self.loopsound=None
			self.AuxFuncsData= None

		if self.Defence>0:
			owner= Bladex.GetEntity(self.OwnerName)
			if owner:
				inv= owner.GetInventory()
				inv.AddMagicShield(self.Name)



	def TakeImpact (self,hit_entity,hitting_entity,xhit_point,yhit_point,zhit_point,ximpulse,yimpulse,zimpulse,DamageType):
		hitting_ent=Bladex.GetEntity(hitting_entity)
		try:
			ball=hitting_ent.Data.DamageEntityName
			if Bladex.GetEntity(ball).Kind=="EsferaOrbital":
				return
		except AttributeError:
			pass
		hitting_ent.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		hitting_ent.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)

		hit_ent=Bladex.GetEntity(hit_entity)

		datos_esc=Reference.DefaultObjectData[hit_ent.Kind]
		if datos_esc[0]==Reference.OBJ_SHIELD:
			Reference.DefaultObjectData[hit_ent.Kind][3].Play(xhit_point, yhit_point, zhit_point, 0)
		else:
			if datos_esc[0]==Reference.OBJ_WEAPON:
				if Reference.GiveWeaponFlag(hit_entity)<>Reference.W_FLAG_1H:
					Reference.DefaultObjectData[hit_ent.Kind][5][6].Play(xhit_point, yhit_point, zhit_point, 0)

		VictimName=self.OwnerName
		AttackerName=hitting_ent.Parent
		pj=Bladex.GetEntity(VictimName)

		#if hitting_ent.Arrow and (hitting_ent.Parent):
		#	pdb.set_trace()
		pj.DamageFunc(VictimName, AttackerName, hitting_entity, DamageType, 0, -1, xhit_point, yhit_point, zhit_point, 1)

		if netgame.GetNetState() == 1:
			netgame.CallEventSound(hit_entity,4)

		# Make arrows stick temporarily
		if hitting_ent.Arrow and (not hitting_ent.Parent):
			hitting_ent.Stop()
			# Check type of damage
			impact= hitting_ent.GraspPos ("Impact")
			centre= hitting_ent.Position
			impact2centre= centre[0]-impact[0], centre[1]-impact[1], centre[2]-impact[2]
			abs_pos= xhit_point+impact2centre[0], yhit_point+impact2centre[1], zhit_point+impact2centre[2]
			rel_pos= hit_ent.Abs2RelPoint(abs_pos[0], abs_pos[1], abs_pos[2])
			# To bring it closer to centre, multiply vector by < 1.0
			hitting_ent.Position= rel_pos[0]*0.8, rel_pos[1], rel_pos[2]*0.8
			hit_ent.Link(hitting_ent)
			sticktime= (1.0)/hitting_ent.Mass
			Bladex.AddScheduledFunc (Bladex.GetTime()+sticktime, Damage.StuckWeaponFall, (hitting_ent.Name, hit_ent.Name), hitting_ent.Name+"_StuckWeaponFall")

		# Make the shield appear in the correct place
		pos= pj.Position
		hit_ent.Position= pos
		hit_ent.Orientation= (1,0,0,0)
		x= xhit_point-pos[0]; y= yhit_point-pos[1]; z= zhit_point-pos[2]
		xz_ang= B3DLib.GetXZAngle (x,y,z)
		y_ang = B3DLib.GetYAngle (x,y,z)
		hit_ent.RotateRel(0,0,0, 0,-1,0, xz_ang)
		hit_ent.RotateRel(0,0,0, 1,0,0, y_ang)


	def PrepareParticleData(self):
		for i in range(30):
			if i>25:
				traux=(30.0-i)/5.0 #va de 0 a 1
				aux=traux**0.5
			else:
				traux=i/25.0 #va de 1 a 0
				aux=traux**2.0
			self.ParticleData.append(255.0*traux)
			self.ParticleData.append(300.0*aux)


	def ChangeParticleColour(self, r, g, b):
		for i in range(30):
			Bladex.SetParticleGVal("MulticolourEnergyDissip", i, r, g, b, self.ParticleData[2*i], self.ParticleData[2*i+1])


	def FadeOut(self, EntityName, r, g, b, nv, rv, pps, fadeTime):
		me= Bladex.GetEntity(EntityName)
		if me:
			self.shieldlight.Color=r, g, b
			self.ChangeParticleColour(r, g, b)
			psimpact=Bladex.CreateEntity(self.Name+"PSImpact"+`self.AGE`, "Entity Particle System Dobj", 0, 0, 0)
			psimpact.ObjectName=self.Name
			psimpact.ParticleType="MulticolourEnergyDissip"
			psimpact.YGravity=0
			psimpact.Velocity=0, 0, 0
			psimpact.NormalVelocity=nv
			psimpact.RandomVelocity=rv
			psimpact.FollowFactor=0.0
			psimpact.PPS=pps
			psimpact.Time2Live=30
			psimpact.DeathTime=Bladex.GetTime()+0.5
			if me.Kind=="MagicShieldBreak":
				shield=Bladex.GetEntity(self.Name)
				currentshield=Bladex.GetEntity(self.CurrentName)
				shield.Unlink(currentshield)
				AuxFuncs.SpotIntensityVariation(self.shieldlight.Name, 6.0, 0.0, fadeTime)
				AuxFuncs.FadeAndScale(me.Name, me.Position, 0.9, 0.0, -1, 1.0, 2.5, -1, fadeTime, 1.0, 1)
			else:
				AuxFuncs.SpotIntensityVariation(self.shieldlight.Name, 4.0, 0.0, fadeTime+0.5)
				AuxFuncs.FadeObject(me.Name, 0.9, 0.0, fadeTime)


	def AbsorbFunc (self, AttackerName, WeaponName, DamagePoints):
		owner=Bladex.GetEntity(self.OwnerName)
		if owner and owner.Life > 0:
			me= Bladex.GetEntity(self.Name)
			self.Defence= max (self.Defence-DamagePoints, 0)
			Reference.EntitiesObjectData[self.Name][2]= self.Defence
			Reference.EntitiesObjectData[self.Name][7]= self.Defence
			#print "Defence remaining "+`self.Defence`

			# play an impact sound
			randsound= whrandom.randint(1,3)
			if randsound==1:
				SoundName= "../../Sounds/M-impacto-berrera-22.wav"
			elif randsound==2:
				SoundName= "../../Sounds/M-impacto-barrera-11.wav"
			else:
				SoundName= "../../Sounds/M-impacto-barrera-44.wav"

			self.AGE= self.AGE+1
			impsound=Bladex.CreateEntity (me.Name+"ImpactSound_"+`self.AGE`, "Entity Sound", 0, 0, 0)
			impsound.SetSound (SoundName)
			impsound.MinDistance=5000
			impsound.MaxDistance=60000
			me.Link(impsound)
			impsound.PlaySound(0)

			if self.Defence==0:
				self.CurrentName=self.Name+"Breaking"
				r=255
				g=64
				b=16
				nv=60
				rv=20
				pps=600
				fadeTime=1.0
				inv= owner.GetInventory()
				inv.RemoveMagicShield(self.Name)
				owner.Data.MagicShieldDestroyed(self.Name, owner.Name)
				self.MaxDefence= self.Defence= Reference.EntitiesObjectData[self.Name][2]= 0.0
				Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, me.RemoveFromWorld, ())
				Bladex.AddScheduledFunc(Bladex.GetTime()+4.1, me.SubscribeToList, ("Pin",))
				self.loopsound.StopSound()
			elif self.Defence<self.IntDefence:
				self.CurrentName=self.Name+"Phase3"
				n=self.Defence/self.IntDefence
				r=255
				g=min(255, max(0, 75+155*n))
				b=0
				nv=4
				rv=2
				pps=100
				fadeTime=0.5
			elif self.Defence<(2.0*self.IntDefence):
				self.CurrentName=self.Name+"Phase2"
				n=(self.Defence-self.IntDefence)/self.IntDefence
				r=min(255, max(0, 255-255*n))
				g=min(255, max(0, 230+25*n))
				b=min(255, max(0, 128*n))
				nv=4
				rv=2
				pps=100
				fadeTime=0.5
			else:
				n=(self.Defence-2.0*self.IntDefence)/self.IntDefence
				r=0
				g=min(255, max(0, 255-127*n))
				b=min(255, max(0, 128+127*n))
				nv=4
				rv=2
				pps=100
				fadeTime=0.5
			self.FadeOut (self.CurrentName, r, g, b, nv, rv, pps, fadeTime)

class Arco:
	def __init__(self, me):
		if not me.Actor:
			me.Weapon=1
		self.Name= me.Name
		String1= self.CreateAndAttachString (self.Name+"StringTop", me.GraspPos("Top"))
		self.String1Name= String1.Name

		String2= self.CreateAndAttachString (self.Name+"StringBottom", me.GraspPos("Bottom"))
		self.String2Name= String2.Name

		self.UnGraspString()

	def CreateAndAttachString (self, StringName, Position):
		bow= Bladex.GetEntity (self.Name)
		String= Bladex.CreateEntity (StringName, "Entity ElectricBolt",Position[0],Position[1],Position[2])
		bow.Link (String)
		String.Position= Position
		String.OuterGlowColor= (0,0,0)
		String.InnerGlowColor= (0,0,0)
		String.CoreGlowColor= (10,10,10)
		String.Damage= 0
		String.MaxAmplitude= 2
		String.FixedTarget= 0
		String.SimpleSections= 1
		return String

	def GraspString (self):
		bow= Bladex.GetEntity (self.Name)
		holder_name= bow.Parent
		if holder_name:
			holder= Bladex.GetEntity (holder_name)
			arrow= Bladex.GetEntity(holder.InvRight)
			if arrow and arrow.Arrow:
				tx,ty,tz= holder.GraspPos("R_Hand")

				String1= Bladex.GetEntity(self.String1Name)
				String1.ETarget= arrow.Name
				String1.Target= tx,ty,tz
				String1.Active= 1

				String2= Bladex.GetEntity(self.String2Name)
				String2.ETarget= arrow.Name
				String2.Target= tx,ty,tz
				String2.Active= 1

	def UnGraspString (self):
		bow= Bladex.GetEntity (self.Name)
		String1= Bladex.GetEntity (self.String1Name)
		String1.ETarget= ""
		x,y,z= bow.GraspPos ("Bottom")
		String1.Target= x,y,z
		String1.Active= 1

		String2= Bladex.GetEntity (self.String2Name)
		String2.ETarget= ""
		String2.Active= 0

class Arco_Amz_seleccion (Arco):
	def GraspString (self):
		bow= Bladex.GetEntity (self.Name)
		holder_name= bow.Parent
		if holder_name:
			holder= Bladex.GetEntity (holder_name)
			arrow= Bladex.GetEntity("FlechaAmz")
			if arrow:
				tx,ty,tz= holder.GraspPos("R_Hand")

				String1= Bladex.GetEntity(self.String1Name)
				String1.ETarget= arrow.Name
				String1.Target= tx,ty,tz
				String1.Active= 1

				String2= Bladex.GetEntity(self.String2Name)
				String2.ETarget= arrow.Name
				String2.Target= tx,ty,tz
				String2.Active= 1


class Arco2 (Arco):
	pass

class Arco3 (Arco):
	pass

class Quiver:
	def __init__ (self, me):
		me.Static=0

		object_data = None
		if Reference.EntitiesObjectData.has_key(me.Name):
			object_data = Reference.EntitiesObjectData[me.Name]
		elif Reference.DefaultObjectData.has_key(me.Kind):
			object_data = Reference.DefaultObjectData[me.Kind]
		if object_data:
			self.MaxArrows= object_data[1]
			self.ArrowType= object_data[2]
		else:
			self.MaxArrows= 12
			self.ArrowType="Flecha"

		self.ArrowsLeft= self.MaxArrows
		self.ArrowsFriendlyName= self.ArrowType

		self.Name= me.Name
		#import pdb
		#pdb.set_trace()

		self.BaseKind= me.Kind
		if len(self.BaseKind)>=2 and self.BaseKind[len(self.BaseKind)-2:len(self.BaseKind)-1]=='_':
			self.BaseKind= self.BaseKind[:len(self.BaseKind)-2]
		elif len(self.BaseKind)>=1 and self.BaseKind[len(self.BaseKind)-1:]=='1':
			self.BaseKind= self.BaseKind[:len(self.BaseKind)-1]
		elif len(self.BaseKind)>=1 and self.BaseKind[len(self.BaseKind)-1:]=='2':
			self.BaseKind= self.BaseKind[:len(self.BaseKind)-1]
		self.ArrowsUsed= 0
		self.ArrowCache=[]
		for i in range (self.MaxArrows):
			self.ArrowCache.append (self.Name+"_Arrow_"+`i`)


	def GetFirstArrow (self, allow_parented=0, allow_flying=0):
		for arrow_name in self.ArrowCache:
			arrow= Bladex.GetEntity (arrow_name)
			if not arrow:
				arrow= Bladex.CreateEntity(arrow_name,self.ArrowType,0,0,0,"Arrow")
			#if arrow.Scale>1.1: print "Arrow has been rescaled!!!"
			flying= arrow.Velocity!=(0.0, 0.0, 0.0)
			if (allow_parented or not arrow.Parent) and (allow_flying or not flying):
				if arrow.Parent:
					parent= Bladex.GetEntity(arrow.Parent)
					if parent: parent.Unlink(arrow)
					#if arrow.Scale>1.1: print "Arrow has been rescaled!!!"

				arrow.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				arrow.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				if flying:
					arrow.Stop()
					#if arrow.Scale>1.1: print "Arrow has been rescaled!!!"
				arrow.Position=0,0,0
				self.ArrowCache.remove(arrow_name)
				self.ArrowCache.append(arrow_name)
				return arrow

		if not allow_parented:
			return self.GetFirstArrow(1)
		else:
			# Returning flying arrows has some strange visual side effects
			return self.GetFirstArrow(1, 1)

	def GiveArrow (self, owner_name=""):
		if self.ArrowsLeft > 0:
			arrow= self.GetFirstArrow()
			# debug
			if arrow.Parent:
				print "GiveArrow giving arrow with parent"
				#pdb.set_trace()
			if not owner_name:
				me= Bladex.GetEntity(self.Name)
				owner_name= me.Parent
			if owner_name:
				owner=Bladex.GetEntity(owner_name)
				if owner and owner.Person and owner.Data and not owner.Data.NPC:
					self.SetNumberOfArrows (self.ArrowsLeft-1)

			else:
				print "Arrow given from quiver with no parent"
				#pdb.set_trace()
			self.ArrowsUsed= self.ArrowsUsed+1
			arrow.CastShadows= 1
			return arrow

	def ReceiveArrow (self, entity, owner_name=""):
		if entity and entity.Arrow and entity.Kind==self.ArrowType:
			if not owner_name:
				me= Bladex.GetEntity(self.Name)
				owner_name= me.Parent
			if owner_name:
				owner=Bladex.GetEntity(owner_name)
				if owner and owner.Person and owner.Data:
					if not owner.Data.NPC:
						if self.ArrowsLeft < self.MaxArrows:
							self.SetNumberOfArrows (self.ArrowsLeft+1,owner_name)
						else:
							return 0
			else:
				print "Arrow received to quiver with no parent"
				#pdb.set_trace()
			entity.SubscribeToList("Pin")
			return 1
		return 0

	def ReceiveArrows (self, num_arrows, owner_name=""):
		if not owner_name:
			me= Bladex.GetEntity(self.Name)
			owner_name= me.Parent
		if owner_name:
			owner=Bladex.GetEntity(owner_name)
			if owner and owner.Person and owner.Data:
				if not owner.Data.NPC:
					self.SetNumberOfArrows (min (self.ArrowsLeft+num_arrows, self.MaxArrows),owner_name)


	def NumberOfArrows (self):
		return self.ArrowsLeft

	def SetNewBOD(self, old_quiver, kind,holder_name=""):
		x,y,z= old_quiver.Position

		###########################################################
		# Destroy the old object
		#
		# Are we being held
		holder= None
		put_on_back= 0
		inv= None
		if not holder_name:
			holder_name= old_quiver.Parent
		selected_quiver=""
		if holder_name:
			holder= Bladex.GetEntity(holder_name)

			# Remove from back..., deselect, remove from inventory
			if holder:
				inv= holder.GetInventory()
				selected_quiver= inv.GetSelectedQuiver()
				if self.Name==holder.InvRightBack:
					put_on_back= 1
					inv.LinkRightBack("None")
				inv.RemoveQuiver(old_quiver.Name)
		else: print "WARNING:  changing quiver BOD with no detected holder!!!!"

		# delete the old object
		data= old_quiver.Data
		old_quiver.RemoveFromWorld()
		Bladex.DeleteEntity(old_quiver.Name)

		###########################################################
		#
		# Create the new object
		new_quiver= Bladex.CreateEntity(self.Name,kind,x,y,z,"Physic")
		new_quiver.Data= data
		self.Name= new_quiver.Name

		# Add the holders inventory, select, and link to back
		if holder:
			inv.AddQuiver(new_quiver.Name)
			if selected_quiver:
				while inv.GetSelectedQuiver()!=selected_quiver:
					inv.CycleQuivers()
			inv.SetCurrentQuiver(new_quiver.Name)
			if put_on_back:
				inv.LinkRightBack(new_quiver.Name)
				inv.SetCurrentQuiver(new_quiver.Name)
			else:
				# Hide in inventory
				new_quiver.RemoveFromWorld()

	def SetNumberOfArrows(self, num, owner_name=""):
		#import pdb
		#pdb.set_trace()
		if num<1:
			# Change to the empty quiver, if we are not using it
			old_quiver= Bladex.GetEntity(self.Name)
			newkind= self.BaseKind+'_E'
			if newkind!=old_quiver.Kind:	# Check we don't already have the empty carcaj model?
				self.SetNewBOD(old_quiver,newkind,owner_name)
		elif num==1:
			# Change to the 1 arrow quiver
			old_quiver= Bladex.GetEntity(self.Name)
			newkind= self.BaseKind+'1'
			if newkind!=old_quiver.Kind:	# Check we don't already have the 1 arrow carcaj model?
				self.SetNewBOD(old_quiver,newkind,owner_name)
		elif num==2:
			# Change to the 2 arrow quiver
			old_quiver= Bladex.GetEntity(self.Name)
			newkind= self.BaseKind+'2'
			if newkind!=old_quiver.Kind:	# Check we don't already have the 1 arrow carcaj model?
				self.SetNewBOD(old_quiver,newkind,owner_name)
		else:
			# Change to the full quiver
			old_quiver= Bladex.GetEntity(self.Name)
			newkind= self.BaseKind
			if newkind!=old_quiver.Kind:	# Check we don't already have the 1 arrow carcaj model?
				self.SetNewBOD(old_quiver,newkind,owner_name)

		self.ArrowsLeft=num


class BladeSword(PersistantItemType):

	def __init__ (self, me):
		PersistantItemType.__init__(self, me)
		me.Weapon= 1
		self.Name= me.Name
		self.Age= 0
		self.FadeTime= 1.0
		self.Speed= 10000.0
		self.AuxFuncsData= None
		self.OwnerName= "Player1"
		me.OnStopFunc=self.StartBackToPlayer

	def __getstate__(self):
		state= PersistantItemType.__getstate__(self)
		state[1]["BladeSword"]=(self.Name,
								self.Age,
								self.FadeTime,
								self.Speed,
								self.AuxFuncsData,
								self.OwnerName
								)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["BladeSword"]
			self.Name=parms[0]
			self.Age= parms[1]
			self.FadeTime=parms[2]
			self.Speed=parms[3]
			self.AuxFuncsData= parms[4]
			self.OwnerName= parms[5]

			me= Bladex.GetEntity(self.Name)
			if me: me.OnStopFunc=self.StartBackToPlayer
		else:
			self.Name="Unnamed"
			self.Age = 0
			self.FadeTime= 1.0
			self.Speed= 10000.0
			self.AuxFuncsData= None
			self.OwnerName  = "Player1"

	def BackToPlayer(self):
		weapon= Bladex.GetEntity(self.Name)
		owner= Bladex.GetEntity(self.OwnerName)
		if owner and weapon:
			if not owner.InvRight:
				AuxFuncs.FadeObject(weapon.Name, weapon.Alpha, 1.0, self.FadeTime)
			else:
				weapon.Alpha= 1.0
			Actions.TakeObject(self.OwnerName,weapon.Name)

	def StartBackToPlayer(self, EntityName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		prtl=Bladex.CreateEntity(weapon.Name+"BackToPlayerParticles", "Entity Particle System Dobj", 0, 0, 0)
		prtl.ObjectName=weapon.Name
		prtl.ParticleType="BrillosBladeSword"
		prtl.PPS=20
		prtl.Velocity=0.0, 0.0, 0.0
		prtl.NormalVelocity=0.0
		prtl.RandomVelocity=0.0
		prtl.YGravity=0.0
		prtl.Friction=0.01
		prtl.FollowFactor=0.0
		prtl.Time2Live=6
		prtl.DeathTime=Bladex.GetTime()+2.0*self.FadeTime
		AuxFuncs.FadeObject(weapon.Name, weapon.Alpha, 0.01, self.FadeTime)
		Bladex.AddScheduledFunc(Bladex.GetTime()+self.FadeTime, self.BackToPlayer, ())

	def DropReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		self.OwnerName= weapon.Parent
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner or owner.InvRight != self.Name:
			return
		if weapon.TestHit:
			return
		Actions.RemoveFromInventory (owner, weapon, EventName)
		ix, iy, iz = owner.Rel2AbsVector(-1000.0, -1500.0, 0.0)
		weapon.Impulse(ix, iy, iz)
		weapon.ExcludeHitFor(owner)
		owner.DelAnmEventFunc(EventName)


class BladeSword2(ActivateableSpecialWeapon):

	def __init__(self, me):
		ActivateableSpecialWeapon.__init__(self, me)
		self.SpecialExtraDamage= [["Light", +1000.0],]
		me.Weapon= 1
		self.Age= 0
		self.FadeTime= 1.0
		self.Speed= 10000.0
		self.missileName= ""
		self.LastHitTime=-1
		self.AuxFuncsData=None

		self.WhileSound=Bladex.CreateEntity (me.Name+"MissileLoopSound", "Entity Sound", 0, 0, 0)
		self.WhileSound.SetSound("../../Sounds/energy-ball.wav")
		self.WhileSound.MinDistance=5000
		self.WhileSound.MaxDistance=30000
		me.Link(self.WhileSound)

		self.ImpactSound=Bladex.CreateEntity (me.Name+"MissileImpactSound", "Entity Sound", 0, 0, 0)
		self.ImpactSound.SetSound("../../Sounds/energy-ball-impact.wav")
		self.ImpactSound.MinDistance=5000
		self.ImpactSound.MaxDistance=30000

		Actions.LinkContinuosSound(me.Name,"../../Sounds/powerpotion-loop.wav")     # Changed -LeadHead
		me.OnStopFunc=self.StartBackToPlayer
		self.OwnerName="Player1"


	def __getstate__(self):
		state= ActivateableSpecialWeapon.__getstate__(self)
		state[1]["BladeSword2"]=   (self.Age,
									self.FadeTime,
									self.Speed,
									self.missileName,
									self.LastHitTime,
									self.WhileSound.Name,
									self.ImpactSound.Name,
									self.AuxFuncsData,
									self.OwnerName
									)
		return state

	def __setstate__(self,parm):
		ActivateableSpecialWeapon.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["BladeSword2"]
			self.Age=parms[0]
			self.FadeTime= parms[1]
			self.Speed=parms[2]
			self.missileName= parms[3]
			self.LastHitTime= parms[4]
			self.WhileSound= Bladex.GetEntity(parms[5])
			self.ImpactSound= Bladex.GetEntity(parms[6])
			self.AuxFuncsData= parms[7]
			self.OwnerName=  parms[8]
		else:
			self.Age=0
			self.FadeTime= 1.0
			self.Speed= 10000.0
			self.missileName= ""
			self.LastHitTime=-1
			self.WhileSound= Bladex.GetEntity(self.Name+"MissileLoopSound")
			self.ImpactSound= Bladex.GetEntity(self.Name+"MissileImpactSound")
			self.AuxFuncsData= None
			self.OwnerName= "Player1"

		weapon=  Bladex.GetEntity(self.Name)
		if weapon:
			weapon.OnStopFunc=self.StartBackToPlayer

		if self.missileName:
			missile= Bladex.GetEntity(self.missileName)
			if missile:
				missile.InflictHitFunc= self.BladeSwordInflictHitFunc
				missile.OnHitFunc= self.MissileOnHitFunc
				if weapon:
					weapon.InflictHitFunc= self.BladeSwordInflictHitFunc
			else:
				print "Missile "+self.missileName+" unavailable for linking...."

	def BackToPlayer(self):
		weapon= Bladex.GetEntity(self.Name)
		owner= Bladex.GetEntity(self.OwnerName)
		if owner and weapon:
			inv= owner.GetInventory()
			flag=Reference.GiveWeaponFlag(weapon.Name)
			inv.AddWeapon(weapon.Name,flag)
			blaura=Bladex.GetEntity(weapon.Name+"Aura")
			bllight=Bladex.GetEntity(weapon.Name+"Light")
			if not owner.InvRight:
				inv.LinkRightHand(weapon.Name)
				AuxFuncs.FadeObject(weapon.Name, weapon.Alpha, 1.0, self.FadeTime)
				if blaura:
					AuxFuncs.FadeAndScaleAura(blaura.Name, 250.0, 80.0, 0.01, 1.0, self.FadeTime)
				if bllight:
					AuxFuncs.SpotIntensityVariation(bllight.Name, 0.0, 1.0, self.FadeTime)
			else:
				weapon.Alpha= 1.0
				if blaura:
					blaura.SetAuraParams(80.0, 1.0, 1, 0, 0, 1)
				if bllight:
					bllight.Intensity=1.0
				weapon.RemoveFromWorld()

	def StartBackToPlayer(self, EntityName):
		weapon= Bladex.GetEntity(self.Name)
		if Bladex.GetEntity(self.OwnerName).Life < 1:	
			print self.OwnerName + " is dead, no sword for you" # Do not return to player hand
			return										        # if dead		-LeadHead
		if not weapon:
			return
		AuxFuncs.FadeObject(weapon.Name, weapon.Alpha, 0.01, self.FadeTime)
		blaura=Bladex.GetEntity(weapon.Name+"Aura")
		if blaura:
			AuxFuncs.FadeAndScaleAura(blaura.Name, 80.0, 250.0, 1.0, 0.01, self.FadeTime)
		bllight=Bladex.GetEntity(weapon.Name+"Light")
		if bllight:
			AuxFuncs.SpotIntensityVariation(bllight.Name, 1.0, 0.0, self.FadeTime)
		Bladex.AddScheduledFunc(Bladex.GetTime()+self.FadeTime, self.BackToPlayer, ())

	def DropReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		self.OwnerName= weapon.Parent
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner or owner.InvRight != self.Name:
			return
		if weapon.TestHit:
			return
		Actions.RemoveFromInventory (owner, weapon, EventName)
		ix, iy, iz = owner.Rel2AbsVector(-1000.0, -1500.0, 0.0)
		weapon.Impulse(ix, iy, iz)
		weapon.ExcludeHitFor(owner)
		owner.DelAnmEventFunc(EventName)

	def ThrowReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		self.OwnerName= weapon.Parent
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner or owner.InvRight != self.Name:
			return

		if weapon.TestHit:
			return

		Actions.RemoveFromInventory (owner, weapon, EventName)

		# Create a magic missile
		self.Age= self.Age+1
		x,y,z= weapon.Position
		missile= Bladex.CreateEntity(self.Name+"_Missile_"+`self.Age`, "Entity Magic Missile", x,y,z)
		InitDataField.Initialise(missile)
		missile.CastShadows=0
		missile.Color=0, 0, 0
		#missile.Visible=0
		self.missileName= missile.Name

		# Set the velocity of the missile
		if owner.ActiveEnemy:
			enemy= Bladex.GetEntity(owner.ActiveEnemy)
			if enemy and enemy.Person:
				tx1,ty1,tz1= enemy.GraspPos ("ViewPoint")
				tx2,ty2,tz2= enemy.Position
				tx= (tx1+tx2)/2.0; ty= (ty1+ty2)/2.0; tz= (tz1+tz2)/2.0;
			else:
				tx,ty,tz= owner.Rel2AbsPoint(0,-30000.0,0.0)
		else:
			tx,ty,tz= owner.Rel2AbsPoint(0,-30000.0,0.0)

		angley= -B3DLib.GetYAngle(tx-x,ty-y,tz-z)
		vx,vy,vz= owner.Rel2AbsVector(0.0, -math.cos(angley)*self.Speed, -math.sin(angley)*self.Speed)

		anglexz= B3DLib.Pos2PosXZAngle(x,y,z,tx,ty,tz)
		diff_angle= min (max (B3DLib.DiffAngle(anglexz, owner.Angle), -Actions.FACINGANGLE), Actions.FACINGANGLE)
		cos_ang= math.cos(diff_angle); sin_ang= math.sin(diff_angle)
		vx,vy,vz=  (vx*cos_ang-vz*sin_ang, vy, vx*sin_ang+vz*cos_ang)

		# Reorient and Link the sword to the missile
		weapon.Orientation=0.707107,0.707107,0.000000,0.000000
		weapon.RotateRel(0,0,0, 0,-1,0, 3.14159/2.0)
		weapon.RotateRel(0,0,0, -1,0,0, (3.0*3.14159/2.0)-anglexz)
		weapon.RotateRel(0,0,0, 0,-1,0, -angley)

		weapon.Position=0, 0, 0
		missile.Link(weapon)
		AuxFuncs.FadeObject(weapon.Name, weapon.Alpha, 0.01, self.FadeTime)
		AuxFuncs.ColorObject(missile.Name, missile.Color, (150,200,255), self.FadeTime*2.0)
		missile.Velocity= vx,vy,vz

		prtl=Bladex.CreateEntity(weapon.Name+"TrailParticles"+`self.Age`, "Entity Particle System Dobj", 0, 0, 0)
		prtl.ObjectName=weapon.Name
		prtl.ParticleType="BladeSwordMissile"
		prtl.PPS=800
		prtl.Velocity=0.0, 0.0, 0.0
		prtl.NormalVelocity=14.0
		prtl.RandomVelocity=4.0
		prtl.YGravity=0.0
		prtl.Friction=0.01
		prtl.FollowFactor=0.0
		prtl.Time2Live=30

		self.WhileSound.PlaySound(-1)

		Reference.EntitiesObjectData[missile.Name]= Reference.DefaultObjectData[weapon.Kind]
		missile.OnHitFunc= self.MissileOnHitFunc
		missile.Data.ThrownBy= owner  		# this pointer may not be valid
		missile.InflictHitFunc= self.BladeSwordInflictHitFunc
		weapon.InflictHitFunc= self.BladeSwordInflictHitFunc

	def BladeSwordInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		if self.missileName:
			self.MissileOnHitFunc (self.missileName, VictimName)

	def DeleteMissileData(self):
		if self.missileName and Reference.EntitiesObjectData.has_key(self.missileName):
			del Reference.EntitiesObjectData[self.missileName]
			self.missileName= ""

	def MissileOnHitFunc (self, EntityName, hit_entity):
		time=Bladex.GetTime()
		if time==self.LastHitTime:
			return
		if hit_entity:
			#print EntityName+" hitting "+hit_entity
			pass
		else:
			pass
			#print EntityName+" hitting world"
		missile= Bladex.GetEntity(EntityName)
		weapon= Bladex.GetEntity(self.Name)
		if weapon: weapon.Data.InflictHitFunc=0
		if missile and weapon:
			Bladex.AddScheduledFunc(time, self.DeleteMissileData, (), "DeleteMissileData")
			prtl=Bladex.GetEntity(weapon.Name+"TrailParticles"+`self.Age`)
			if prtl:
				prtl.DeathTime=Bladex.GetTime()
			missile.Unlink(weapon)
			missile.Stop()
			missile.SubscribeToList("Pin")
			self.WhileSound.StopSound()
			self.ImpactSound.Position=weapon.Position
			self.ImpactSound.PlaySound(0)
			owner= Bladex.GetEntity(self.OwnerName)
			if owner:
				inv= owner.GetInventory()
				flag=Reference.GiveWeaponFlag(weapon.Name)
				inv.AddWeapon(weapon.Name,flag)
				blaura=Bladex.GetEntity(weapon.Name+"Aura")
				bllight=Bladex.GetEntity(weapon.Name+"Light")
				if not owner.InvRight:
					inv.LinkRightHand(weapon.Name)
					AuxFuncs.FadeObject(weapon.Name, 0.01, 1.0, self.FadeTime)
					if blaura:
						AuxFuncs.FadeAndScaleAura(blaura.Name, 250.0, 80.0, 0.01, 1.0, self.FadeTime)
					if bllight:
						AuxFuncs.SpotIntensityVariation(bllight.Name, 0.0, 1.0, self.FadeTime)
				else:
					weapon.Alpha= 1.0
					if blaura:
						blaura.SetAuraParams(80.0, 1.0, 1, 0, 0, 1)
					if bllight:
						bllight.Intensity=1.0
					weapon.RemoveFromWorld()

class BladeSwordBarbarian (BladeSword):
	pass

class BladeSword2Barbarian(BladeSword2):
	pass

class DalWeapon(PersistantItemType):
	Name=""
	Speed= 15000.0
	Spin= -0.8
	Axis= (1.0, 0.0, 0.0)
	OwnerName= ""
	C= None
	TimeWeaponStarted= None
	R= None
	Rn= None
	w= None
	RSQdist=None
	WeaponActive= 0
	grasped= 0
	tFinished= None
	Weapon= None
	ThrownBy= None
	Target= None
	Time2Grasp=0.4
	spinsound=None
	WeaponFX=None

	def __init__ (self, me):
		PersistantItemType.__init__(self, me)
		me.Weapon= 1
		self.Name= me.Name
		#self.Speed= 12000.0
		self.Speed= 15000.0
		self.Spin= -0.8
		self.Axis= (1.0, 0.0, 0.0)
		self.OwnerName= ""
		self.C= None
		self.TimeWeaponStarted= None
		self.R= None
		self.Rn= None
		self.w= None
		self.RSQdist=None
		self.WeaponActive= 0
		self.grasped= 0
		self.tFinished= None
		self.Weapon= None
		self.ThrownBy= None
		self.Target= None
		self.Time2Grasp=0.4
		# Create a looped sound
		SoundName= "../../Sounds/vueltas-en-el-aire.wav"
		self.spinsound= Bladex.CreateEntity (me.Name+"LoopSound", "Entity Sound", 0, 0, 0)
		self.spinsound.SetSound (SoundName)
		self.spinsound.MinDistance=5000
		self.spinsound.MaxDistance=30000
		me.Link(self.spinsound)
		GenFX.AddWeaponFX(me.Name, self)

	def __getstate__(self):
		state= PersistantItemType.__getstate__(self)
		ThrownByName=""
		WeaponName=""
		SpinSoundName=""
		if self.Weapon: WeaponName=self.Weapon.Name
		if self.ThrownBy: ThrownByName=self.ThrownBy.Name
		if self.spinsound: SpinSoundName=self.spinsound.Name

		state[1]["DalWeapon"]=(self.Name,
								self.Speed,
								self.Spin,
								self.Axis,
								self.OwnerName,
								self.C,
								self.TimeWeaponStarted,
								self.R,
								self.Rn,
								self.w,
								self.RSQdist,
								self.WeaponActive,
								self.grasped,
								self.tFinished,
								WeaponName,
								ThrownByName,
								self.Target,
								self.Time2Grasp,
								SpinSoundName,
								self.WeaponFX)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["DalWeapon"]
			ThrownByName=""
			WeaponName=""
			SpinSoundName=""

			(self.Name,
			self.Speed,
			self.Spin,
			self.Axis,
			self.OwnerName,
			self.C,
			self.TimeWeaponStarted,
			self.R,
			self.Rn,
			self.w,
			self.RSQdist,
			self.WeaponActive,
			self.grasped,
			self.tFinished,
			WeaponName,
			ThrownByName,
			self.Target,
			self.Time2Grasp,
			SpinSoundName,
			self.WeaponFX)= parms

			if WeaponName: self.Weapon=Bladex.GetEntity(WeaponName)
			if ThrownByName: self.ThrownBy=Bladex.GetEntity(ThrownByName)
			if SpinSoundName: self.spinsound=Bladex.GetEntity(SpinSoundName)

		else:
			self.Name="Unnamed"

	def SetTarget(self, TargetName):
		enemy= Bladex.GetEntity(TargetName)
		#print "setting target to "+TargetName
		#print enemy
		if enemy:
			self.Target= enemy.GraspPos ("ViewPoint")
			#print self.Target

	def ThrowReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		self.OwnerName= weapon.Parent
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner or owner.InvRight != self.Name:
			return

		if owner.Kind!="DalGurak":
			raise AttributeError

		if weapon.TestHit:
			return

		Actions.RemoveFromInventory (owner, weapon, EventName)

		SourcePos= weapon.Position

		if self.Target:
			TargetPos= self.Target
			self.Target= None
		else:
			TargetPos= owner.Rel2AbsPoint(0,-30000.0,0.0)

		# target one metre past the enemies head
		offsetx,offsety,offsetz= B3DLib.Scale(B3DLib.Normalize((TargetPos[0]-SourcePos[0], TargetPos[1]-SourcePos[1], TargetPos[2]-SourcePos[2])), 1000.0)
		TargetPos= TargetPos[0]+offsetx, TargetPos[1]+offsety, TargetPos[2]+offsetz

		self.C= (SourcePos[0]+TargetPos[0])*0.5, (SourcePos[1]+TargetPos[1])*0.5, (SourcePos[2]+TargetPos[2])*0.5
		self.TimeWeaponStarted= Bladex.GetTime()
		self.R= SourcePos[0]-self.C[0], SourcePos[1]-self.C[1], SourcePos[2]-self.C[2]
		self.RSQdist= abs(self.R[0]*self.R[0]+self.R[1]*self.R[1]+self.R[2]*self.R[2])
		moduloR= math.sqrt(self.RSQdist)
		scale= (moduloR/8.0) / math.sqrt(self.R[2]*self.R[2]+self.R[0]*self.R[0])
		self.Rn= -self.R[2]*scale, 0.0, self.R[0]*scale
		self.w = self.Speed / moduloR
		Bladex.SetAfterFrameFunc("DalWeaponMoveWeapon", self.MoveWeapon)
		self.WeaponActive= 0
		self.grasped= 0
		self.tFinished= Actions.TWOPI/self.w
		self.Weapon= weapon
		self.ThrownBy= owner  # this pointer may not be valid
		self.Time2Grasp= Bladex.GetAnimationDuration("Dgk_catch")*0.239 # currently 0.239 is the point for the catch
		self.spinsound.PlaySound(-1)
		weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)

	def MoveWeapon (self, time):
		self.Weapon.RemoveFromWorld()
		t= time-self.TimeWeaponStarted
		wt= self.w*t
		cos_wt= math.cos(wt)
		sin_wt= math.sin(wt)
		P= self.R[0]*cos_wt + self.Rn[0]*sin_wt, self.R[1]*cos_wt + self.Rn[1]*sin_wt, self.R[2]*cos_wt + self.Rn[2]*sin_wt
		self.Weapon.Position= P[0]+self.C[0], P[1]+self.C[1], P[2]+self.C[2]

		if wt>=Actions.TWOPI:
			owner=Bladex.GetEntity(self.OwnerName)
			if owner:
				inv= owner.GetInventory()
				inv.AddWeapon(self.Weapon.Name)
				if not owner.InvRight:
					inv.LinkRightHand(self.Weapon.Name)
			Bladex.RemoveAfterFrameFunc("DalWeaponMoveWeapon")
		elif wt >= Actions.PI*1.5:
			if self.WeaponActive:
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				self.WeaponActive= 0
		elif wt >= Actions.PI and self.WeaponActive:
			owner=Bladex.GetEntity(self.OwnerName)
			if owner and owner.SQDistance2(self.Weapon) < self.RSQdist/2.0:
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				self.WeaponActive= 0
		elif wt >= Actions.PI*0.5:
			if not self.WeaponActive:
				self.Weapon.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
				self.Weapon.MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)
				self.WeaponActive= 1

		if (not self.grasped) and t+self.Time2Grasp >= self.tFinished:
			self.grasped=1
			self.spinsound.StopSound()
			owner=Bladex.GetEntity(self.OwnerName)
			if owner and owner.Life>0:
				owner.Wuea=Reference.WUEA_ENDED
				owner.InterruptCombat()
				owner.LaunchAnmType("catch")
			else:
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				self.Weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				self.WeaponActive= 0
				self.Weapon.Impulse(0,10,0)
				Bladex.RemoveAfterFrameFunc("DalWeaponMoveWeapon")
		# Angular velocity
		self.Weapon.RotateRel(0.0, 0.0, 0.0 ,self.Axis[0],self.Axis[1],self.Axis[2],self.Spin,1)

class DalBlade(PersistantItemType):
	Name=""
	OwnerName=""
	TrailName=""
	LightName=""
	Speed= 18000.0
	Axis=(1.0,0.0,0.0)
	Spin=0.15
	WeaponActive=0
	CreationTime=0.0
	MissileShootSound=""
	MissileWhileSound=""
	MissileImpactSound=""
	AuxFuncsData= None
	sp=None
	tp=None
	v=None
	TimeWeaponStarted=0.0
	Weapon=None
	ThrownBy=None

	def __init__(self, me, ownerName):
		PersistantItemType.__init__(self, me)
		me.Weapon=1
		me.Alpha= 0.0
		me.SelfIlum=1.0
		me.RasterMode="AdditiveAlpha"

		self.Name= me.Name
		self.OwnerName= ownerName
		self.TrailName=self.Name+"_Trail"
		self.LightName=self.Name+"_Light"
		self.Speed= 18000.0
		self.Axis=B3DLib.Normalize((0.05,1.0,0.0))
		self.Spin= 0.15
		self.WeaponActive= 0
		me.InflictHitFunc= self.DalBladeInflictHitFunc
		self.CreationTime= 0.85 #seconds

		concdisk=Bladex.CreateEntity(me.Name+"_Conc","Entity Particle System Dobj", 0, 0, 0)
		concdisk.ObjectName=me.Name
		concdisk.ParticleType="DeepOrangeEnergyConc"
		concdisk.PPS=800
		concdisk.YGravity=0.0
		concdisk.Friction=0.0
		concdisk.RandomVelocity=-6.0
		concdisk.NormalVelocity=-6.0
		concdisk.Time2Live=30
		concdisk.FollowFactor=0.0
		concdisk.DeathTime=Bladex.GetTime()+1.0

		disklight= Bladex.CreateEntity(self.LightName, "Entity Spot", 0, 0, 0)
		disklight.Color=255, 100, 60
		disklight.Intensity=0.0
		disklight.Precission=0.01
		disklight.CastShadows=0
		disklight.Flick=1
		disklight.Visible=0
		me.Link(disklight)
		AuxFuncs.SpotIntensityVariation(self.LightName, 0.0, 6.0, 1.0)

		concsound=Bladex.CreateEntity(me.Name+"_ConcSound", "Entity Sound", 0, 0, 0)
		concsound.SetSound("../../Sounds/energy-ball-conc.wav")
		concsound.MinDistance=5000
		concsound.MaxDistance=30000
		me.Link(concsound)
		concsound.PlaySound(0)

		self.MissileShootSound=""
		self.MissileWhileSound=""
		self.MissileImpactSound=""
		self.SetMissileSound("shoot", "../../Sounds/Fireball-Fire.wav")
		self.SetMissileSound("while", "../../Sounds/energy-ball.wav")
		self.SetMissileSound("impact", "../../Sounds/energy-ball-impact.wav")

		time= Bladex.GetTime()
		Bladex.AddScheduledFunc(time, self.FadeIn, (me.Name,), me.Name+" FadeIn")
		CheckOwnerTime= 4.0
		Bladex.AddScheduledFunc(time+CheckOwnerTime, self.CheckOwner, (me.Name,), me.Name+" CheckOwner")

	def __getstate__(self):
		state= PersistantItemType.__getstate__(self)
		MissileShootSoundName= ""
		MissileWhileSoundName= ""
		MissileImpactSoundName= ""
		ThrownByName=""
		WeaponName=""
		if self.MissileShootSound: MissileShootSoundName= self.MissileShootSound.Name
		if self.MissileWhileSound: MissileWhileSoundName= self.MissileWhileSound.Name
		if self.MissileImpactSound: MissileImpactSoundName= self.MissileImpactSound.Name
		if self.Weapon and hasattr(self.Weapon, 'Name'):
			WeaponName=self.Weapon.Name
		if self.ThrownBy: ThrownByName=self.ThrownBy.Name

		state[1]["DalBlade"]=(self.Name,
								self.OwnerName,
								self.TrailName,
								self.LightName,
								self.Speed,
								self.Axis,
								self.Spin,
								self.WeaponActive,
								self.CreationTime,
								MissileShootSoundName,
								MissileWhileSoundName,
								MissileImpactSoundName,
								self.AuxFuncsData,
								self.sp,
								self.tp,
								self.v,
								WeaponName,
								ThrownByName
								)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["DalBlade"]
			MissileShootSoundName= ""
			MissileWhileSoundName= ""
			MissileImpactSoundName= ""
			ThrownByName=""
			WeaponName=""

			(self.Name,
			self.OwnerName,
			self.TrailName,
			self.LightName,
			self.Speed,
			self.Axis,
			self.Spin,
			self.WeaponActive,
			self.CreationTime,
			MissileShootSoundName,
			MissileWhileSoundName,
			MissileImpactSoundName,
			self.AuxFuncsData,
			self.sp,
			self.tp,
			self.v,
			WeaponName,
			ThrownByName)= parms

			if MissileShootSoundName: self.MissileShootSound= Bladex.GetEntity(MissileShootSoundName)
			if MissileWhileSoundName: self.MissileWhileSound= Bladex.GetEntity(MissileWhileSoundName)
			if MissileImpactSoundName: self.MissileImpactSound= Bladex.GetEntity(MissileImpactSoundName)
			if WeaponName: self.Weapon=Bladex.GetEntity(WeaponName)
			if ThrownByName: self.ThrownBy=Bladex.GetEntity(ThrownByName)

			me= Bladex.GetEntity(self.Name)
			if me: me.InflictHitFunc= self.DalBladeInflictHitFunc
		else:
			self.Name="Unnamed"

	def SetMissileSound(self, kind, wavfile):
		missile=Bladex.GetEntity(self.Name)
		if missile:
			if kind=="shoot":
				missilesound=Bladex.CreateEntity(self.Name+"_ShootSound", "Entity Sound", 0, 0, 0)
				self.MissileShootSound=missilesound
			elif kind=="while":
				missilesound=Bladex.CreateEntity(self.Name+"_WhileSound", "Entity Sound", 0, 0, 0)
				self.MissileWhileSound=missilesound
			elif kind=="impact":
				missilesound=Bladex.CreateEntity(self.Name+"_ImpactSound", "Entity Sound", 0, 0, 0)
				self.MissileImpactSound=missilesound
			missilesound.SetSound(wavfile)
			missilesound.Volume=1.0
			missilesound.MinDistance=5000
			missilesound.MaxDistance=30000
			missile.Link(missilesound)

	def DestroyMe (self):
		me=Bladex.GetEntity(self.Name)
		if me:
			if self.MissileWhileSound: self.MissileWhileSound.StopSound()
			if self.MissileImpactSound: self.MissileImpactSound.PlaySound(0)
			self.FadeOut(self.Name)
			self.WeaponActive= 0
			self.MissileShootSound=""
			self.MissileWhileSound=""
			self.MissileImpactSound=""

	def CheckOwner (self,EntityName):
		# Has the owner thrown us yet???
		me= Bladex.GetEntity(EntityName)
		if me and not self.WeaponActive:
			self.DestroyMe()

	def FadeIn(self,EntityName):
		me= Bladex.GetEntity(EntityName)
		if me:
			fadeTime=self.CreationTime
			AuxFuncs.FadeObject(me.Name, me.Alpha, 0.9, fadeTime)

	def FadeOut(self,EntityName):
		me= Bladex.GetEntity(EntityName)
		if me:
			fadeTime= 1.0
			trailps=Bladex.GetEntity(self.TrailName)
			if trailps:
				trailps.Friction=0.01
				trailps.NormalVelocity=2.0
				trailps.RandomVelocity=10.0
				trailps.DeathTime=Bladex.GetTime()+0.5
			AuxFuncs.SpotIntensityVariation(self.LightName, 6.0, 0.0, fadeTime)
			AuxFuncs.FadeAndScale(me.Name, me.Position, 0.9, 0.0, -1, 1.0, 3.0, -1, fadeTime, 1.0, 1, (0, 1, 0))
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.9, me.MessageEvent, (Reference.MESSAGE_STOP_WEAPON,0,0))
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.9, me.MessageEvent, (Reference.MESSAGE_STOP_TRAIL,0,0))

	def DalBladeInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		#print "DalBlade hitting "+VictimName
		pass

	def ThrowReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(EntityName)
		if not weapon:
			return
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner:
			return

		weapon.ExcludeHitFor(owner)

		traildisk=Bladex.CreateEntity(self.TrailName,"Entity Particle System Dobj", 0, 0, 0)
		traildisk.ObjectName=EntityName
		traildisk.ParticleType="DeepOrangeMagicMissile"
		traildisk.PPS=1000
		traildisk.YGravity=0.0
		traildisk.Friction=0.0
		traildisk.RandomVelocity=-1.0
		traildisk.NormalVelocity=-2.0
		traildisk.Time2Live=30
		traildisk.FollowFactor=0.0

		sp= weapon.Position
		if owner.ActiveEnemy:
			enemy= Bladex.GetEntity(owner.ActiveEnemy)
			tp= enemy.GraspPos ("ViewPoint")
		else:
			#print "No enemy to throw DalBlade at!!!"
			tp=owner.Rel2AbsPoint(0,-100000.0,0.0)
		v= B3DLib.Normalize((tp[0]-sp[0], tp[1]-sp[1], tp[2]-sp[2]))
		self.sp= sp
		self.tp= tp
		self.v= v
		self.TimeWeaponStarted= Bladex.GetTime()
		self.WeaponActive= 0
		self.Weapon= weapon
		self.ThrownBy= owner  # this pointer may not be valid
		weapon.TimerFunc=self.MoveWeapon
		weapon.SubscribeToList("Timer60")
		self.MissileShootSound.PlaySound(0)
		self.MissileWhileSound.PlaySound(-1)

	def MoveWeapon (self, ent_name, time):
		t= time-self.TimeWeaponStarted
		ax, ay, az= B3DLib.Scale(self.v,t*self.Speed)
		self.Weapon.Position= self.sp[0]+ax, self.sp[1]+ay, self.sp[2]+az
		if self.WeaponActive:
			if self.Weapon.TestHit:
				self.Weapon.RemoveFromList("Timer60")
				self.Weapon.TimerFunc=""
				self.DestroyMe()
				#print "Has Hit"
		elif t>0.1:
			self.Weapon.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
			self.Weapon.MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)
			self.WeaponActive= 1
		# Angular velocity
		self.Weapon.RotateRel(0.0, 0.0, 0.0 ,self.Axis[0],self.Axis[1],self.Axis[2],self.Spin,1)

class HalfmoonTrail(PersistantItemType):
	Name=""
	OwnerName=""
	TrailName=""
	Speed= 12000.0
	Axis=(1.0,0.0,0.0)
	Spin= 0.15
	Range= 2500.0
	Time2Live=2.5
	MaxAlpha= 1.0
	StartingDamage=0.0
	AbsorbedDamage= 0.0
	AuxFuncsData= None
	sp=None
	tp=None
	v=None
	TimeWeaponStarted=0.0
	WeaponActive=0
	loopsound=None
	Weapon=None
	ThrownBy=None

	def __init__(self, me, ownerName):
		PersistantItemType.__init__(self, me)
		# Create a particle system around the object as it appears
		me.Weapon=1
		me.Alpha= 0.0
		self.Name= me.Name
		self.OwnerName= ownerName
		self.TrailName=self.Name+"_Trail"
		self.Speed= 12000.0
		self.Axis=B3DLib.Normalize((0.05,1.0,0.0))
		self.Spin= 0.15
		self.Range= 2500.0
		owner=Bladex.GetEntity(self.OwnerName)

		# Really want to align our orientation with that of the weapon before linking them
		if owner:
			owner.LinkAnchors("R_Hand",me,"1H_R")
			weapon= Bladex.GetEntity(owner.InvRight)
			if weapon:
				if weapon.Kind=="BladeSword2" or weapon.Kind=="DalWeapon" or weapon.Kind=="BladeSword2Barbarian":
					self.Range= 30000.0
				#orientation= weapon.Orientation
				#me.Orientation= orientation
				#owner.LinkToNode(me, owner.GetNodeIndex("R_Hand"))


		me.InflictHitFunc= self.HalfmoonTrailInflictHitFunc
		time= Bladex.GetTime()

		if self.Speed: self.Time2Live= self.Range/self.Speed
		else: self.Time2Live= self.Range/12000.0
		self.MaxAlpha= 1.0
		Reference.EntitiesObjectData[me.Name]= BCopy.deepcopy(Reference.DefaultObjectData[me.Kind])
		self.StartingDamage= Reference.EntitiesObjectData[me.Name][1]
		self.AbsorbedDamage= 0.0
		me.Alpha= self.MaxAlpha
		me.RasterMode="AdditiveAlpha"
		me.RasterMode="Read"
		me.SelfIlum=0.9

		# Create a looped sound
		SoundName= "../../Sounds/rueda-metal.wav"
		self.loopsound= Bladex.CreateEntity (me.Name+"LoopSound", "Entity Sound", 0, 0, 0)
		self.loopsound.SetSound (SoundName)
		self.loopsound.MinDistance=500
		self.loopsound.MaxDistance=20000
		me.Link(self.loopsound)

	def __getstate__(self):
		state= PersistantItemType.__getstate__(self)

		loopsoundName= ""
		WeaponName=""
		ThrownByName=""

		if self.loopsound and hasattr(self.loopsound, "Name"): loopsoundName= self.loopsound.Name
		if self.Weapon and hasattr(self.Weapon, "Name"): WeaponName=self.Weapon.Name
		if self.ThrownBy and hasattr(self.ThrownBy, "Name"): ThrownByName=self.ThrownBy.Name

		state[1]["HalfmoonTrail"]=(self.Name,
								self.OwnerName,
								self.TrailName,
								self.Speed,
								self.Axis,
								self.Spin,
								self.Range,
								self.Time2Live,
								self.MaxAlpha,
								self.StartingDamage,
								self.AbsorbedDamage,
								self.AuxFuncsData,
								self.sp,
								self.tp,
								self.v,
								self.TimeWeaponStarted,
								self.WeaponActive,
								loopsoundName,
								WeaponName,
								ThrownByName
								)

		return state

	def __setstate__(self,parm):
		PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["HalfmoonTrail"]

			loopsoundName= ""
			ThrownByName=""
			WeaponName=""

			(self.Name,
			self.OwnerName,
			self.TrailName,
			self.Speed,
			self.Axis,
			self.Spin,
			self.Range,
			self.Time2Live,
			self.MaxAlpha,
			self.StartingDamage,
			self.AbsorbedDamage,
			self.AuxFuncsData,
			self.sp,
			self.tp,
			self.v,
			self.TimeWeaponStarted,
			self.WeaponActive,
			loopsoundName,
			WeaponName,
			ThrownByName)= parms

			if loopsoundName: self.loopsound= Bladex.GetEntity(loopsoundName)
			if WeaponName: self.Weapon=Bladex.GetEntity(WeaponName)
			if ThrownByName: self.ThrownBy=Bladex.GetEntity(ThrownByName)

			me= Bladex.GetEntity(self.Name)
			if me: me.InflictHitFunc= self.HalfmoonTrailInflictHitFunc
		else:
			self.Name="Unnamed"


	def FadeOut(self,EntityName):
		# to be called upon impact with the world??
		me= Bladex.GetEntity(EntityName)
		if me:
			fadeTime= 0.6
			AuxFuncs.FadeObject(me.Name, me.Alpha, 0.0, fadeTime)
			Bladex.AddScheduledFunc(Bladex.GetTime()+fadeTime+0.2, me.SubscribeToList, ("Pin",), me.Name+" PinMe")

	def HalfmoonTrailInflictHitFunc(self, EntityName, VictimName, ImpX, ImpY, ImpZ):
		print "HalfmoonTrail hitting "+VictimName
		victim= Bladex.GetEntity(VictimName)
		if victim and victim.Person:
			charFDef= max(CharStats.GetCharDefenseData(victim.CharType,victim.Level),0.0)
			self.AbsorbedDamage= self.AbsorbedDamage + charFDef

	def ThrowReleaseEventHandler (self,EntityName,EventName):
		weapon= Bladex.GetEntity(self.Name)
		if not weapon:
			return
		if not self.OwnerName:
			return
		owner=Bladex.GetEntity(self.OwnerName)
		if not owner:
			return
		owner.Unlink(weapon)
		weapon.ExcludeHitFor(owner)

		sp= weapon.Position
		tp= owner.Rel2AbsPoint(0,-100000.0,0.0)
		v= B3DLib.Normalize((tp[0]-sp[0], tp[1]-sp[1], tp[2]-sp[2]))
		self.sp= sp
		self.tp= tp
		self.v= v
		Bladex.SetAfterFrameFunc(self.Name+"HalfmoonTrailMoveWeapon", self.MoveWeapon)
		self.TimeWeaponStarted= Bladex.GetTime()
		self.WeaponActive= 0
		self.Weapon= weapon
		self.ThrownBy= owner  # this pointer may not be valid

		traildisk=Bladex.CreateEntity(self.TrailName,"Entity Particle System Dobj", 0, 0, 0)
		traildisk.ObjectName=self.Name
		traildisk.ParticleType="LittleDeepOrangeMagicMissile"
		traildisk.PPS=800
		traildisk.YGravity=0.0
		traildisk.Friction=0.01
		traildisk.RandomVelocity=16.0
		traildisk.NormalVelocity=0.0
		traildisk.Velocity=v[0]*3000.0, v[1]*3000.0, v[2]*3000.0
		traildisk.Time2Live=20
		traildisk.FollowFactor=0.0

		# Create a firing sound
		SoundName= "../../Sounds/disparo-cuchilla.wav"
		firesound=Bladex.CreateEntity(weapon.Name+"firesound", "Entity Sound", 0, 0, 0)
		firesound.SetSound(SoundName)
		firesound.MinDistance=5000
		firesound.MaxDistance=30000
		weapon.Link(firesound)
		firesound.PlaySound(0)

		self.loopsound.PlaySound(-1)

	def MoveWeapon (self, time):
		me= self.Weapon
		me.RemoveFromWorld()
		t= time-self.TimeWeaponStarted
		ax, ay, az= B3DLib.Scale(self.v,t*self.Speed)
		me.Position= self.sp[0]+ax, self.sp[1]+ay, self.sp[2]+az

		# Reduce DamagePoints and Alpha
		current_damage= max(0.0, self.StartingDamage*(1.0-(t/self.Time2Live))-self.AbsorbedDamage)
		intensity= current_damage/self.StartingDamage
		Reference.EntitiesObjectData[me.Name][1]= current_damage
		me.Alpha= self.MaxAlpha*intensity

		if self.WeaponActive:
			if me.TestHit:
				print "Hit world"
				me.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				me.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				self.WeaponActive= 0
				self.loopsound.StopSound()
				Bladex.RemoveAfterFrameFunc(self.Name+"HalfmoonTrailMoveWeapon")
				self.FadeOut(self.Name)
				ps=Bladex.GetEntity(self.TrailName)
				if ps:
					ps.PPS=8000
					ps.YGravity=6900.0
					ps.RandomVelocity=90.0
					ps.RandomVelocity_V=45.0
					ps.DeathTime=Bladex.GetTime()+0.05
				# Play a hut world sound
				# Create a firing sound
				SoundName= "../../Sounds/impacto-cuchilla.wav"
				hitsound=Bladex.CreateEntity(me.Name+"hitsound", "Entity Sound", 0, 0, 0)
				hitsound.SetSound(SoundName)
				hitsound.MinDistance=5000
				hitsound.MaxDistance=30000
				me.Link(hitsound)
				hitsound.PlaySound(0)
			if intensity<=0.0:
				me.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
				me.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
				self.WeaponActive= 0
				self.loopsound.StopSound()
				Bladex.RemoveAfterFrameFunc(self.Name+"HalfmoonTrailMoveWeapon")
				self.FadeOut(self.Name)
				ps=Bladex.GetEntity(self.TrailName)
				if ps:
					ps.PPS=400
					ps.DeathTime=Bladex.GetTime()+0.05
		elif t>0.01:
			me.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
			me.MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)
			self.WeaponActive= 1
		# Angular velocity
		#me.RotateRel(0.0, 0.0, 0.0,self.Axis[0],self.Axis[1],self.Axis[2],self.Spin,1)
		me.PutToWorld()

class Carcaj (Quiver):
	pass

class Carcaj_E (Carcaj):
	pass

class Carcaj1 (Carcaj):
	pass

class Carcaj2 (Carcaj):
	pass

class CarcajFuego (Quiver):
	def GiveArrow (self, owner_name=""):
		entity= Quiver.GiveArrow(self, owner_name)
		if entity:
			# Switch on flame effect
			entity.FiresIntensity=[ 0 ]
			entity.Lights=[ (1.000000,0.500000,(255,128,0)) ]
			entity.CastShadows= 0
		return entity

	def ReceiveArrow (self, entity, owner_name=""):
		if entity and entity.Arrow and entity.Kind==self.ArrowType:
			# Switch off flame effect
			entity.Lights=[ (0.000000,0.500000,(255,196,128)) ]
		return Quiver.ReceiveArrow(self, entity, owner_name)

class CarcajFuego_E (CarcajFuego):
	pass

class CarcajFuego1 (CarcajFuego):
	pass

class CarcajFuego2 (CarcajFuego):
	pass

class CarcajEnvenenado (Quiver):
	pass

class CarcajEnvenenado_E (CarcajEnvenenado):
	pass

class CarcajEnvenenado1 (CarcajEnvenenado):
	pass

class CarcajEnvenenado2 (CarcajEnvenenado):
	pass


class ItemOfProtection:
	def __init__ (self, me):
		me.UseFunc= self.UseStart
		self.UsedBy= "Player1"
		self.UseTime= 25.0
		self.Resistances= {}
		self.nUses= 1
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
		return (1,
					self.ObjId, # De GameStateAux.PersistentObject
					self.UsedBy,
					self.UseTime,
					self.Resistances,
					self.nUses
				)


	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.UsedBy=parm[2]
			self.UseTime=parm[3]
			self.Resistances=parm[4]
			self.nUses=parm[5]

		else:
			print "ItemOfProtection.__setstate__() -> Version mismatch"
			# Valores por si valen para algo.
			self.UsedBy= "Player1"
			self.UseTime= 15.0
			self.Resistances= {}
			self.nUses= 2
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self


	def UseStart (self, ObjectName, use_from):
		if use_from==Actions.USE_FROM_INV:
			object= Bladex.GetEntity(ObjectName)
			if object: object.UseFunc= 0
			Bladex.AddScheduledFunc(Bladex.GetTime()+self.UseTime, self.UseEnd,(ObjectName,self.UsedBy), ObjectName+"_UseEnd")
			GenFX.AddPersonItemFX(self.UsedBy, ObjectName, self.UseTime)

	def UseEnd (self,ObjectName, UserName):
		self.Resistances= {}
		self.nUses= self.nUses-1                # PLAGUE: Why is this being reduced only after the effect wears off?
		if self.nUses<1:
			user= Bladex.GetEntity(UserName)
			if user:
				inv= user.GetInventory()
				if inv:
					inv.RemoveObject(ObjectName)
					object= Bladex.GetEntity(ObjectName)
					if object: object.SubscribeToList("Pin")
					return

			# In case of any problems obtaining handles etc...
			Bladex.AddScheduledFunc(Bladex.GetTime()+self.UseTime, self.UseEnd,(ObjectName, UserName), ObjectName+"_UseEnd")
		else:
			object= Bladex.GetEntity(ObjectName)
			if object: object.UseFunc=self.UseStart


class Amuletofantasma (ItemOfProtection):
	def __init__ (self, me):
		ItemOfProtection.__init__(self, me)
		self.UsedBy= "Player1"
		self.UseTime= 45.0
		self.Resistances= {}
		self.nUses= 2





	def UseStart (self, ObjectName, use_from):
		ItemOfProtection.UseStart (self, ObjectName, use_from)
		self.Resistances['Venom']= 1.0
		# Manuel, quieres poner algun efecto magico aqui

	def UseEnd (self,ObjectName, UserName):
		# Manuel, termina el efecto magico aqui
		ItemOfProtection.UseEnd (self, ObjectName, UserName)






class Corona (ItemOfProtection):
	def __init__ (self, me):
		ItemOfProtection.__init__(self, me)
		self.UsedBy= "Player1"
		self.UseTime= 45.0
		self.Resistances= {}
		self.nUses= 2


	def UseStart (self, ObjectName, use_from):
		ItemOfProtection.UseStart (self, ObjectName, use_from)
		self.Resistances['Fire']= 1.0
		# Manuel, quieres poner algun efecto magico aqui

	def UseEnd (self,ObjectName, UserName):
		# Manuel, termina el efecto magico aqui
		ItemOfProtection.UseEnd (self, ObjectName, UserName)


class Brazalete (ItemOfProtection):
	def __init__ (self, me):
		ItemOfProtection.__init__(self, me)
		self.UsedBy= "Player1"
		self.UseTime= 45.0
		self.Resistances= {}
		self.nUses= 2


	def UseStart (self, ObjectName, use_from):
		ItemOfProtection.UseStart (self, ObjectName, use_from)
		self.Resistances= {'Slash':0.75, 'Impale':0.75, 'Crush':0.75}
		# Manuel, quieres poner algun efecto magico aqui

	def UseEnd (self,ObjectName, UserName):
		# Manuel, termina el efecto magico aqui
		ItemOfProtection.UseEnd (self, ObjectName, UserName)




def MakeMagicShield(EntityName, owner):
	shield= Bladex.CreateEntity(EntityName,"MagicShield",0,0,0,"Weapon")
	#shield.Solid= 0
	shield.SelfIlum=1.0
	Sparks.MakeShield(EntityName)
	shield.Data= MagicShield(shield, owner)

	return shield

def MakeShield (EntityName, ShieldKind, x=0.0, y=0.0, z=0.0):
	shield=Bladex.CreateEntity(EntityName,ShieldKind,x,y,z,"Weapon")
	Sparks.MakeShield(EntityName)
	return shield

def MakeVampireSword (EntityName):
	sword=Bladex.CreateEntity(EntityName,"VampWeapon",0,0,0)
	sword.Weapon=1
	sword.Data= VampWeapon(sword)
	return sword

def MakeDalBall (name, x,y,z, ownerName=""):
	missile= Bladex.CreateEntity(name, "Entity Magic Missile", x, y, z)
	missile.Data= BolaDalGurak (missile, ownerName)
	return missile

def MakeAnkBall (name, x,y,z, ownerName=""):
	missile= Bladex.CreateEntity(name, "Entity Magic Missile", x, y, z)
	missile.Data= BolaRayos (missile, ownerName)
	return missile

def MakeHunterSeekerMissile (name, x,y,z, vx,vy,vz, TargetEntity, owner="", onDestroyedFunc=None):
	missile= Bladex.CreateEntity(name, "Entity Magic Missile", x, y, z)
	missile.Data= HunterSeekerMissile (missile, vx,vy,vz, TargetEntity, owner, onDestroyedFunc)
	return missile

def MakeGenericMissile (name, x, y, z, owner="", onDestroyedFunc=None):
	missile=Bladex.CreateEntity(name, "Entity Magic Missile", x, y, z)
	missile.Color=255, 255, 255
	missile.Intensity=1.0
	missile.CastShadows=0
	missile.Visible=0
	missile.Flick=0
	missile.Data=GenericMissile(missile, owner, onDestroyedFunc)
	return missile

def MakeDalBlade (name, x,y,z, ownerName=""):
	missile= Bladex.CreateEntity(name, "DalBlade", x, y, z)
	missile.Weapon=1
	missile.Data= DalBlade (missile, ownerName)
	return missile

def MakeHalfmoonTrail (name, x,y,z, ownerName=""):
	missile= Bladex.CreateEntity(name, "HalfmoonTrail", x, y, z)
	missile.Weapon=1
	missile.Data= HalfmoonTrail (missile, ownerName)
	return missile

# temp test func
def LaunchTrail(EntityName):
	import ItemTypes
	me= Bladex.GetEntity(EntityName)
	x, y, z= me.Rel2AbsPoint(1000.0, 0.0, 0.0)
	missile= ItemTypes.MakeHalfmoonTrail (EntityName+"Trail", x,y,z,EntityName)
	missile.Data.ThrowReleaseEventHandler (EntityName,"")
	return missile

def MakeMeteorite (name, x,y,z, vx,vy,vz):
	missile= Bladex.CreateEntity(name, "Entity Magic Missile", x, y, z)
	missile.Data= Meteorito (missile, vx,vy,vz)
	return missile




################################################################################
# Parse the Kind automatically
################################################################################
classes_defined= dir()
def ItemDefaultFuncs (item):
	import pocimac
	class_found=0
	if item.Kind in classes_defined:
		exec_string = 'item.Data=' + item.Kind + '(item)'
		exec (exec_string)
		if not item.Data:
			raise NameError, 'Kind must have valid associated class'
			class_found=0
		else:
			class_found=1
		Bladex.CheckPyErrors()

	if pocimac.CreateDefaultPocimac(item.Name):
		pass
	elif Reference.IsParryingType(item.Kind):
		Sparks.MakeShield(item.Name)
	elif Reference.IsWeaponType(item.Kind):
		Breakings.SetBreakableWS(item.Name)
	elif not class_found:
		InitDataField.Initialise(item)


################################################################################

"""
todo list
Types of Potion....
"Saquito"
"Pocima25"
"Pocima50"
"Pocima200"


Types of Torch....
"""