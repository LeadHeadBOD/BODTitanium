##///
##||| BLOOD.PY TITANIUM
##||| Change list:
##||| * Optimization to prevent mass overlapping blood pools that kill performance and fuck up SNEG's stupid engine changes.
##\\\ 

import Bladex
import math
import InitDataField

## Titanium Config Fuctions ##
import TitaniumConfig
TiCfgFound= TitaniumConfig.TitaniumSetting("BloodOptimization") == 1    # PLAGUE: This is terrible -LeadHead
checkRadius = 200


Evaporation      = 0      #  no evaporation avail  >:-(
AfterCreateBlood = None   # CARLOS! PLEAS DON'T SAVE THIS VALUE...

def BloodPrtlHit(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	global Evaporation
	if TiCfgFound:
		for p in Bladex.GetEntitiesAt(x,y,z,checkRadius):
			ent = Bladex.GetEntity(p)
			if ent.Kind == 'Entity Pool':
				# print "~Blood.py~ Pool found within "+`checkRadius`
				return
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	else:
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	prtl= Bladex.GetEntity(prtl_name);
	try:
		if(prtl.Data.evaporation):
			p.DeathTime = Bladex.GetTime()+20.0
		elif Evaporation:
			p.DeathTime = Bladex.GetTime()+50.0
	except:
		if Evaporation:
			p.DeathTime = Bladex.GetTime()+50.0
			
	if AfterCreateBlood:
		AfterCreateBlood(x,y,z)
	
def GreenBloodPrtlHit(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	global Evaporation
	if TiCfgFound:
		for p in Bladex.GetEntitiesAt(x,y,z,checkRadius):
			ent = Bladex.GetEntity(p)
			if ent.Kind == 'Entity Pool':
				# print "~Blood.py~ Pool found within "+`checkRadius`
				return
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	else:
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	p.Color = (96,192,96)
	p.DeepColor = (64,128,64)
	if Evaporation:
		p.DeathTime = Bladex.GetTime()+50.0
		
	# Generate a smoke effect
	smoke=Bladex.CreateEntity("FuegoVerde", "Entity Particle System D1", x, y, z)
	smoke.ParticleType="VenomSmoke"
	smoke.YGravity=-100.0
	smoke.Friction=0.05
	smoke.PPS=8
	smoke.Velocity=0.0, -800.0, 0.0
	smoke.RandomVelocity=5.0
	smoke.DeathTime=Bladex.GetTime()+1.5

def GreyBloodPrtlHit(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):	
	global Evaporation
	if TiCfgFound:
		for p in Bladex.GetEntitiesAt(x,y,z,checkRadius):
			ent = Bladex.GetEntity(p)
			if ent.Kind == 'Entity Pool':
				# print "~Blood.py~ Pool found within "+`checkRadius`
				return
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	else:
		p = Bladex.CreateEntity("BloodPool","Entity Pool",x,y,z)
	p.Color = (96,96,96)
	p.DeepColor = (80,80,80)
	if Evaporation:
		p.DeathTime = Bladex.GetTime()+50.0


def BleedFunc(blood_name,end_time,period):
	blood=Bladex.GetEntity(blood_name)
	if(blood):
		prtl=blood.GetParticleEntity()
		InitDataField.Initialise(prtl)
		prtl.Data.evaporation=0
		if blood.ParticleType=="GreenBlood":
			prtl.HitFunc=GreenBloodPrtlHit
		elif blood.ParticleType=="GreyBlood":
			prtl.HitFunc=GreyBloodPrtlHit
		else:						
			prtl.HitFunc=BloodPrtlHit
			
		if(Bladex.GetTime()<end_time):
			Bladex.AddScheduledFunc(Bladex.GetTime()+period,BleedFunc,(blood_name,end_time,period),blood.Name+" BleedFunc")

AGE_Number=0
def Bleed(objname,start_time,end_time,period,x=0.0,y=0.0,z=0.0,vx=0,vy=0,vz=0,ParticleType="Blood"):
	global AGE_Number
	AGE_Number=AGE_Number+1
	blood=Bladex.CreateEntity("bleed_AGE_"+str(AGE_Number),"Entity Particle System D1",x,y,z)
	blood.ParticleType=ParticleType
	blood.YGravity=9800.0
	blood.Friction=0.075
	blood.PPS=512
	blood.DeathTime=end_time+1.0/60.0;
	blood.Velocity=vx,vy,vz
	Bladex.GetEntity(objname).Link(blood)
	Bladex.AddScheduledFunc(start_time,BleedFunc,(blood.Name,end_time,period),blood.Name+" BleedFunc")

def PersonBleed(per,start_time,end_time,period,x=0.0,y=0.0,z=0.0,vx=0,vy=0,vz=0,node=0):
	global AGE_Number
	if(node<0):
		print("invalid node")
		return

	AGE_Number=AGE_Number+1
	blood=Bladex.CreateEntity("bleed_AGE_"+str(AGE_Number),"Entity Particle System D1",x,y,z)
	if per.Kind=="Spidersmall":
		blood.ParticleType="GreenBlood"
	elif per.Kind=="Lich":
		blood.ParticleType="GreyBlood"

	else:				
		blood.ParticleType="Blood"
	blood.YGravity=9800.0
	blood.Friction=0.075
	blood.PPS=512
	blood.DeathTime=end_time+1.0/60.0;
	blood.Velocity=vx,vy,vz
	per.LinkToNode(blood,node)
	Bladex.AddScheduledFunc(start_time,BleedFunc,(blood.Name,end_time,period),blood.Name+" BleedFunc")


# Lista de entidades que tiran polvo
SparkEntities     = ["Golem_metal","ChaosKnight"]
DustDeathEntities = ["Skeleton","Lich","Golem_stone","Golem_clay","Golem_lava","Golem_ice","Knight_Zombie"]+SparkEntities

def Mutilate(pj_name,obj_name,x,y,z,nx,ny,nz,node):
	global DustDeathEntities
	global SparkEntities
	
	vx=nx*2000.0
	vy=ny*2000.0
	vz=nz*2000.0
	per= Bladex.GetEntity(pj_name)
	if (Bladex.GetBloodLevel()==0) or (per.Kind in DustDeathEntities):
		return
	"""
    TODO: Make golems make smoke clouds when they shatter
	# elif :
		# if per.Kind == "Golem_clay":
			# pass
			
	# else:
		# print "BLOOD.PY - per.Kind not valid for mutilation blood"	
	"""


	if per.Kind=="Spidersmall":
		Bleed(obj_name,Bladex.GetTime()+0.0,Bladex.GetTime()+1.0,0.2,x,y,z,vx,vy,vz,"GreenBlood")
	elif per.Kind=="Lich":
		Bleed(obj_name,Bladex.GetTime()+0.0,Bladex.GetTime()+1.0,0.2,x,y,z,vx,vy,vz,"GreyBlood")        # PLAGUE: Because Liches and Zombie Knights are in DustDeathEntities, this
	else:					                                                                            # script is ended early an we never get to bleeding grey blood.
		Bleed(obj_name,Bladex.GetTime()+0.0,Bladex.GetTime()+1.0,0.2,x,y,z,vx,vy,vz)
	x,y,z=Bladex.GetEntity(obj_name).Rel2AbsPoint(x,y,z)
	PersonBleed(per,Bladex.GetTime()+0.0,Bladex.GetTime()+1.5,0.125,x,y,z,-2.0*vx,-2.0*vy,-2.0*vz,node)



def BleedingImpact(entity, x, y, z, ImpX, ImpY, ImpZ, weapon_entity,WeaponCx, WeaponCy, WeaponCz,WeaponDx, WeaponDy, WeaponDz):
	global AGE_Number
	global DustDeathEntities
	global SparkEntities
	
	AGE_Number=AGE_Number+1	

	if (entity.Kind in DustDeathEntities) or (Bladex.GetBloodLevel()==0):
		
		dust=Bladex.CreateEntity("dust_AGE_"+str(AGE_Number),"Entity Particle System D1", x, y, z)
		if entity.Kind == "Golem_clay":
			dust.ParticleType="ShitSmoke"
			dust.Time2Live=63
			dust.PPS=60
			dust.RandomVelocity=30.0
		elif entity.Kind == "Golem_lava":
			dust.ParticleType="LargeFire"
			dust.Time2Live=31
			dust.PPS=60
			dust.RandomVelocity=30.0
		elif entity.Kind in SparkEntities:
			dust.ParticleType="Splinter"
			dust.Time2Live=16
			dust.PPS=128
			dust.RandomVelocity=50.0
		else:
			dust.ParticleType="MediumDust"
			dust.Time2Live=63
			dust.PPS=60
			dust.RandomVelocity=30.0
			
		dust.YGravity=0.0
		dust.Friction=0.1
		dust.Velocity=0.0, 0.0, 0.0
		
		dust.DeathTime=Bladex.GetTime()+4.0/60.0
	
	else:
		time=Bladex.GetTime()
		
		if (weapon_entity):
			stickblood=Bladex.CreateEntity("stickbleed_AGE_"+str(AGE_Number),"Entity Particle System D2", WeaponCx, WeaponCy, WeaponCz)
			stickblood.D=WeaponDx, WeaponDy, WeaponDz
			stickblood.YGravity=9800.0
			stickblood.Friction=0.15
			stickblood.Friction2=0.0
			stickblood.DeathTime=time+0.4
			
			stickblood.RandomVelocity=100.0/60
			stickblood.RandomVelocity_V=100.0/60
			stickblood.Time2Live=26.0 # Maybe not necessarary
			stickblood.Time2Live_V=6.0
			stickblood.PPS=600
			weapon_entity.Link(stickblood)
		else:
			stickblood=None
		
		
		blood=Bladex.CreateEntity("bleed_AGE_"+str(AGE_Number),"Entity Particle System D1", x, y, z)
		blood.YGravity=9800.0
		blood.Friction=0.075
		blood.PPS=600
		blood.DeathTime=time+10.0/60.0;
		blood.Position=x, y, z		
		scale= math.sqrt(ImpX*ImpX+ImpY*ImpY+ImpZ*ImpZ)
		if scale==0.0:
			scale=1.0
		scale = -2000.0 / scale # normalized scale by -2000.0
		blood.Velocity=(ImpX*scale), (ImpY*scale)-2000.0, (ImpZ*scale)
		blood.RandomVelocity=15.0
		blood.RandomVelocity_V=10.0
		blood.Time2Live=32
		if stickblood:
			prtl1=stickblood.GetParticleEntity()
			InitDataField.Initialise(prtl1)
			prtl1.Data.evaporation=1
		else:
			prtl1=blood.GetParticleEntity()
			InitDataField.Initialise(prtl1)
			prtl1.Data.evaporation=1
		prtl2=blood.GetParticleEntity()		
		InitDataField.Initialise(prtl2)
		prtl2.Data.evaporation=1
		if entity.Kind=="Spidersmall":
			blood.ParticleType="GreenBlood"
			if stickblood:
				stickblood.ParticleType="GreenBlood"
			prtl1.HitFunc=GreenBloodPrtlHit
			prtl2.HitFunc=GreenBloodPrtlHit
		elif entity.Kind=="Lich":
			blood.ParticleType="GreyBlood"
			if stickblood:
				stickblood.ParticleType="GreyBlood"
			prtl1.HitFunc=GreyBloodPrtlHit
			prtl2.HitFunc=GreyBloodPrtlHit
		else:						
			blood.ParticleType="Blood"
			if stickblood:
				stickblood.ParticleType="Blood"
			prtl1.HitFunc=BloodPrtlHit
			prtl2.HitFunc=BloodPrtlHit
			
		
