##///
##||| SPARKS.PY TITANIUM
##||| Change list:
##||| * Added automatic default spark-type parser.
##||| * Added dirt for grass and earth impacts on world.
##||| * Wood shields will now throw wood sparks.
##||| * Cristal now uses unique sound name to avoid conflict with the one Materials.py
##\\\ 

import Bladex
import B3DLib
import Reference
import netgame
import Damage
import Water
import whrandom
import Breakings
import Blood

###
# Titanium dirt particles - LeadHead
###

#Bladex.ReadBitMap("../../Data/Salpicadura.bmp","DirtPoofParticle")

Bladex.AddParticleGType("DirtPoof","SmokeParticle",2,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=75
	g=65
	b=45
	a=255*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("DirtPoof",i,r,g,b,a,size)
    
#Bladex.ReadBitMap("../../Data/Salpicadura.bmp","GenericParticle")

Bladex.AddParticleGType("DirtUp","SplashParticle",2,200)

for i in range(200):
	aux=(20.0-i)/200.0
	r=20
	g=15
	b=0 
	a=240
	size=200.0*(1.0-aux)
	Bladex.SetParticleGVal("DirtUp",i,r,g,b,a,size)

def ThrowSparks(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):
	obj= Bladex.GetEntity(hitting_entity)
	try:
		if obj and obj.Data.NoFXOnHit:
			return
	except: pass
	mod=B3DLib.Modulo(ximpulse, yimpulse, zimpulse)
	if mod<5000.0:
		return
	sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
	chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)

def ThrowMetalSparks(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):
	obj= Bladex.GetEntity(hitting_entity)
	try:
		if obj and obj.Data.NoFXOnHit:
			return
	except: pass
	mod=B3DLib.Modulo(ximpulse, yimpulse, zimpulse)
	if mod<5000.0:
		return
	sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
	chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)

	# sound
	on_hit_info= Reference.MaterialOnHitInfo['Metal']
	sound= on_hit_info[0]

	if sound:
		sound.Stop()
		sound.Play(xhit_point, yhit_point, zhit_point, 0)

def ThrowDustAndSparks(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):
	obj= Bladex.GetEntity(hitting_entity)
	try:
		if obj and obj.Data.NoFXOnHit:
			return
	except: pass
	mod=B3DLib.Modulo(ximpulse, yimpulse, zimpulse)
	if mod<5000.0:
		return
	sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
	chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)

	polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	polvillo.ParticleType="MediumDust"
	polvillo.YGravity=200
	polvillo.Friction=0.2
	polvillo.PPS=200
	polvillo.DeathTime=Bladex.GetTime()+2.0/60.0
	polvillo.Velocity=sparkdir[0]*500, sparkdir[1]*500, sparkdir[2]*500
	polvillo.RandomVelocity=40.0
	polvillo.RandomVelocity_V=1.0

def ThrowWoodenSparks(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):
	obj= Bladex.GetEntity(hitting_entity)
	try:
		if obj and obj.Data.NoFXOnHit:
			return
	except: pass
	mod=B3DLib.Modulo(ximpulse, yimpulse, zimpulse)
	if mod<5000.0:
		return

	# spark
	sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
	spark= Bladex.CreateSpark("Wood",xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],      0.75,2000,60,0,80,   75,46,21,   6,3,2,    900,15.0/60.0,1.0/60.0,0)
	spark.RasterMode="BlendingAlpha"

	# dust
	polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	polvillo.ParticleType="MediumDust"
	polvillo.YGravity=200
	polvillo.Friction=0.2
	polvillo.PPS=250
	polvillo.DeathTime=Bladex.GetTime()+2.0/60.0
	polvillo.Velocity=sparkdir[0]*500, sparkdir[1]*500, sparkdir[2]*500
	polvillo.RandomVelocity=40.0
	polvillo.RandomVelocity_V=1.0

	# sound
	on_hit_info= Reference.MaterialOnHitInfo['MaderaTablas']
	sound= on_hit_info[0]

	if sound:
		sound.Stop()
		sound.Play(xhit_point, yhit_point, zhit_point, 0)

def ThrowStoneSparks(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):
	obj= Bladex.GetEntity(hitting_entity)
	try:
		if obj and obj.Data.NoFXOnHit:
			return
	except: pass
	mod=B3DLib.Modulo(ximpulse, yimpulse, zimpulse)
	if mod<5000.0:
		return
	sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
	chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)

	polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	polvillo.ParticleType="MediumDust"
	polvillo.YGravity=200
	polvillo.Friction=0.2
	polvillo.PPS=200
	polvillo.DeathTime=Bladex.GetTime()+2.0/60.0
	polvillo.Velocity=sparkdir[0]*500, sparkdir[1]*500, sparkdir[2]*500
	polvillo.RandomVelocity=40.0
	polvillo.RandomVelocity_V=1.0

	on_hit_info= Reference.MaterialOnHitInfo['Piedra']
	sound= on_hit_info[0]

	if sound:
		sound.Stop()
		sound.Play(xhit_point, yhit_point, zhit_point, 0)


def SetSparkling(obj_name):
	obj=Bladex.GetEntity(obj_name)
	if obj.HitFunc:
		print "Este objeto ya es rompible o chispeante."
		return
	if obj.Static:
		obj.Static=0
	obj.HitFunc=ThrowSparks
	return obj

def SetDustySparkling(obj_name):
	obj=Bladex.GetEntity(obj_name)
	if obj.HitFunc:
		print "Este objeto ya es rompible o chispeante."
		return
	if obj.Static:
		obj.Static=0
	obj.HitFunc=ThrowDustAndSparks
	return obj

def SetWoodenSparkling(obj_name):
	obj=Bladex.GetEntity(obj_name)
	if obj.HitFunc:
		print "Este objeto ya es chispeante."
		return
	if obj.Static:
		obj.Static=0
	obj.HitFunc=ThrowWoodenSparks
	return obj

def SetMetalSparkling(obj_name):
	obj=Bladex.GetEntity(obj_name)
	if obj.HitFunc:
		print "Este objeto ya es rompible o chispeante."
		return
	if obj.Static:
		obj.Static=0
	obj.HitFunc=ThrowMetalSparks
	return obj

def SetStoneSparkling(obj_name):
	obj=Bladex.GetEntity(obj_name)
	if obj.HitFunc:
		print "Este objeto ya es rompible o chispeante."
		return
	if obj.Static:
		obj.Static=0
	obj.HitFunc=ThrowStoneSparks
	return obj

#import pdb

def ThrowSparksShield(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,DamageType):
	hitting_ent=Bladex.GetEntity(hitting_entity)

	hitting_ent.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)

	skip_sparks=0
	try:
		if hitting_ent.Data.NoFXOnHit:
            
			skip_sparks=1
			
	except: pass
	hit_ent=Bladex.GetEntity(hit_entity)
	if not skip_sparks:
		sparkdir=B3DLib.Normalize((-ximpulse, -yimpulse, -zimpulse))
		if hit_ent.Material:
			if hit_ent.Material[0:6]=="madera": ## If blocking item is made of wood, throw wood chips instead.     -LeadHead
				chispa=Bladex.CreateSpark("Wood",   xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],0.75,2000,  60,0, 80,  75,  46, 21,  6,  3, 2,900,15.0/60.0,1.0/60.0,0)
			else:
				chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2], 0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)
				
		else: 
			chispa=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2], 0.5,3000,2000,0,100, 160, 120, 40, 30, 24, 0,800,10.0/60.0,1.0/60.0,1)


	datos_esc=Reference.DefaultObjectData[hit_ent.Kind]
	if datos_esc[0]==Reference.OBJ_SHIELD:
		Reference.DefaultObjectData[hit_ent.Kind][3].Play(xhit_point, yhit_point, zhit_point, 0)
	else:
		if datos_esc[0]==Reference.OBJ_WEAPON:
			if Reference.GiveWeaponFlag(hit_entity)!=Reference.W_FLAG_1H:
				Reference.DefaultObjectData[hit_ent.Kind][5][6].Play(xhit_point, yhit_point, zhit_point, 0)

	VictimName=hit_ent.Parent
	AttackerName=hitting_ent.Parent
	pj=Bladex.GetEntity(VictimName)

	#if hitting_ent.Arrow and (hitting_ent.Parent):
	#	pdb.set_trace()

	pj.DamageFunc(VictimName, AttackerName, hitting_entity, DamageType, 0, -1, xhit_point, yhit_point, zhit_point, 1)

	if netgame.GetNetState() == 1:
		netgame.CallEventSound(hit_entity,4)

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
		try:
			if hit_ent.Data.brkobjdata and hit_ent.Data.brkobjdata.Broken==1:
				hitting_ent.Impulse(0,0,0)
			else:
				hit_ent.Link(hitting_ent)
				sticktime= (1.0)/hitting_ent.Mass
				Bladex.AddScheduledFunc (Bladex.GetTime()+sticktime, Damage.StuckWeaponFall, (hitting_ent.Name, hit_ent.Name), hitting_ent.Name+"_StuckWeaponFall")
		except AttributeError:
			hit_ent.Link(hitting_ent)
			sticktime= (1.0)/hitting_ent.Mass
			Bladex.AddScheduledFunc (Bladex.GetTime()+sticktime, Damage.StuckWeaponFall, (hitting_ent.Name, hit_ent.Name), hitting_ent.Name+"_StuckWeaponFall")
		if hitting_ent.StickFunc:
			hitting_ent.StickFunc (hitting_entity, hit_entity)


def SetShieldArea(obj_name, cone, height, radius):      ## PLAGUE: Unused
	esc=Bladex.GetEntity(obj_name)
	if not esc.Weapon:
		esc.Static=1
	esc.Weapon=1
	esc.Cone=cone
	esc.Height=height
	esc.Radius=radius
	esc.HitShieldFunc=ThrowSparksShield
	return esc

def MakeShield(obj_name):
	esc=Bladex.GetEntity(obj_name)
	if not esc.Weapon:
		esc.Static=1
	esc.Weapon=1
	datos_esc=Reference.DefaultObjectData[esc.Kind]

	if datos_esc[0]==Reference.OBJ_SHIELD:
		esc.Cone=datos_esc[4]
		esc.Height=datos_esc[5]
		esc.Radius=datos_esc[6]
		if datos_esc[7]:
			Breakings.SetBreakableWS(obj_name)
	else:
		esc.Cone=3.1416
		esc.Height=2000
		esc.Radius=750
		if datos_esc[0]==Reference.OBJ_STANDARD or datos_esc[0]==Reference.OBJ_WEAPON:
			if Reference.GiveWeaponFlag(obj_name)!=Reference.W_FLAG_1H:
				esc.Cone=datos_esc[5][1]
				esc.Height=datos_esc[5][2]
				esc.Radius=datos_esc[5][3]
				if datos_esc[5][5]:
					Breakings.SetBreakableWS(obj_name)
			else:
				print "MakeShield. Unexpected weapon FLAG"
		else:
			print "MakeShield. Unexpected type of object"


	esc.HitShieldFunc=ThrowSparksShield
	return esc

stones_active=0
max_stones_active=4

def RemoveStone(obj_name):
	global stones_active
	Piedra= Bladex.GetEntity(obj_name)
	if Piedra:
		Piedra.SubscribeToList("Pin")
		stones_active= stones_active-1

def DropStone(x,y,z,dx=1,dy=1,dz=1, Pname= "Piedra_01"):
	global stones_active

	if stones_active<max_stones_active:
		Piedra=Bladex.CreateEntity("Piedrita", Pname, x,y,z, "Physic")
		#Piedra.Mass= 1
		Piedra.Scale= 0.075 + whrandom.random()*0.13

		mod=B3DLib.Modulo(dx,dy,dz)
		dx=dx/mod + whrandom.random()*0.4 - whrandom.random()*0.4
		dy=dy/mod + whrandom.random()*0.4 - whrandom.random()*0.4
		dz=dz/mod + whrandom.random()*0.4 - whrandom.random()*0.4
		dx,dy,dz= B3DLib.Scale((dx,dy,dz),mod)

		Piedra.ExclusionGroup=1
		Piedra.ImpulseC(x+(whrandom.random()*200.0-100.0), y+(whrandom.random()*-100.0), z+(whrandom.random()*200.0-100.0),dx,dy,dz)

		Piedra.OnStopFunc= RemoveStone
		stones_active=stones_active+1
		return Piedra
	else:
		return None

def SectorThrowSparks(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	D=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
	TWO_NdotD= 2.0 * (D[0]*x_norm + D[1]*y_norm + D[2]*z_norm)
	sparkdir= (D[0]-x_norm*TWO_NdotD, D[1]-y_norm*TWO_NdotD, D[2]-z_norm*TWO_NdotD)
	spark=Bladex.CreateSpark("Chispa", xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],   0.5,3000,2000,0,100,   160,120,40,   30,24,0,     800,10.0/60.0,1.0/60.0,1)
	polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	polvillo.ParticleType="MediumDust"
	polvillo.YGravity=200
	polvillo.Friction=0.2
	polvillo.PPS=200
	polvillo.DeathTime=Bladex.GetTime()+2.0/60.0
	polvillo.Velocity=sparkdir[0]*500, sparkdir[1]*500, sparkdir[2]*500
	polvillo.RandomVelocity=40.0
	polvillo.RandomVelocity_V=1.0
	nstones= whrandom.randint(0,max_stones_active)
	stone_startx= xhit_point+x_norm*200.0
	stone_starty= yhit_point+y_norm*200.0
	stone_startz= zhit_point+z_norm*200.0
	stone_impx= x_norm*2000
	stone_impy= y_norm*2000
	stone_impz= z_norm*2000
	for i in range(nstones):
		DropStone(stone_startx, stone_starty, stone_startz, stone_impx, stone_impy, stone_impz)

def SectorThrowSnow(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	D=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
	TWO_NdotD= 2.0 * (D[0]*x_norm + D[1]*y_norm + D[2]*z_norm)
	sparkdir= (D[0]-x_norm*TWO_NdotD, D[1]-y_norm*TWO_NdotD, D[2]-z_norm*TWO_NdotD)
	spark= Bladex.CreateSpark("Snow",xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],      0.8,400,100,10,20, 200,200,200, 56,56,56,        600,90.0/60.0,1.0/60.0,0)
	spark.RasterMode="BlendingAlpha"

	tierra1=Bladex.CreateEntity("SnowDust", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	tierra1.ParticleType="SnowDust"
	tierra1.YGravity=200.0
	tierra1.Friction=0.15
	tierra1.PPS=200
	tierra1.Time2Live=64
	tierra1.Velocity=sparkdir[0]*2000.0, sparkdir[1]*2000.0, sparkdir[2]*2000.0
	tierra1.RandomVelocity=10.0
	tierra1.DeathTime=Bladex.GetTime()+0.05


def SectorThrowWood(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	#astilla
	D=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
	TWO_NdotD= 2.0 * (D[0]*x_norm + D[1]*y_norm + D[2]*z_norm)
	sparkdir= (D[0]-x_norm*TWO_NdotD, D[1]-y_norm*TWO_NdotD, D[2]-z_norm*TWO_NdotD)
	spark= Bladex.CreateSpark("Wood",xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],      0.75,2000,60,0,80,   75,46,21,   6,3,2,    900,15.0/60.0,1.0/60.0,0)
	spark.RasterMode="BlendingAlpha"

	polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	polvillo.ParticleType="MediumDust"
	polvillo.YGravity=200
	polvillo.Friction=0.2
	polvillo.PPS=250
	polvillo.DeathTime=Bladex.GetTime()+2.0/60.0
	polvillo.Velocity=sparkdir[0]*500, sparkdir[1]*500, sparkdir[2]*500
	polvillo.RandomVelocity=40.0
	polvillo.RandomVelocity_V=1.0

def SectorThrowWater(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	#astilla
	D=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
	TWO_NdotD= 2.0 * (D[0]*x_norm + D[1]*y_norm + D[2]*z_norm)
	reflectdir= (D[0]-x_norm*TWO_NdotD, D[1]-y_norm*TWO_NdotD, D[2]-z_norm*TWO_NdotD)

	Aguita1=Bladex.CreateEntity("Cristales", "Entity Particle System D1",xhit_point, yhit_point, zhit_point)
	Aguita1.ParticleType="Splash"
	Aguita1.PPS=1024
	Aguita1.YGravity=2500.0
	Aguita1.Friction=0
	Aguita1.Velocity=reflectdir[0]*2500.0, reflectdir[1]*2500.0, reflectdir[2]*2500.0
	Aguita1.RandomVelocity=15.0
	Aguita1.Time2Live=32
	Aguita1.DeathTime=Bladex.GetTime()+0.10
	Aguita1.Reflects=0

	if not Bladex.GetEntity(entity_name).Person:        # Prevents unnecessary particle entity creation which cannot be assigned        -LeadHead
		Aguita2=Bladex.CreateEntity("Cristales","Entity Particle System Dobj", 0, 0, 0)
		Aguita2.ObjectName=entity_name
		Aguita2.ParticleType= "Splash"
		Aguita2.PPS= 1024
		Aguita2.YGravity= 4500.0
		Aguita2.Friction= 0.1
		Aguita2.RandomVelocity= 13.0
		Aguita2.Time2Live= 64
		Aguita2.DeathTime= Bladex.GetTime()+0.2
		Aguita2.Reflects=0
   
"""
def SectorThrowLava(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
    pass
    
def SectorThrowAcid(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
    pass
"""

## New dirt impacts -LeadHead
## Experimental, might remove them if I can't get them to look perfect.



def SectorThrowDirt(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	D=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
	TWO_NdotD= 2.0 * (D[0]*x_norm + D[1]*y_norm + D[2]*z_norm)
	sparkdir= (D[0]-x_norm*TWO_NdotD, D[1]-y_norm*TWO_NdotD, D[2]-z_norm*TWO_NdotD)
	# spark= Bladex.CreateSpark("Snow",xhit_point, yhit_point, zhit_point, sparkdir[0], sparkdir[1], sparkdir[2],      0.8,400,100,10,20, 200,200,200, 56,56,56,        600,90.0/60.0,1.0/60.0,0)
	# spark.RasterMode="BlendingAlpha"

	dirt1=Bladex.CreateEntity("Dirt1", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	#dirt1.ObjectName=entity_name
	dirt1.ParticleType="DirtUp"
	dirt1.YGravity=10000.0
	dirt1.Friction=0.1  
	dirt1.PPS=100
	dirt1.Scale=0.1
	dirt1.Time2Live=64
	dirt1.Velocity=sparkdir[0]*5000.0, sparkdir[1]*190000.0, sparkdir[2]*5000.0
	dirt1.RandomVelocity=100
	dirt1.DeathTime=Bladex.GetTime()+0.1
    
	dirt2=Bladex.CreateEntity("Dirt2", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
	#dirt2.ObjectName=entity_name
	dirt2.ParticleType="DirtPoof"
	dirt2.YGravity=10000.0
	dirt2.Friction=0.2
	dirt2.PPS=40
	dirt2.Scale=3
	dirt2.Time2Live=20
	dirt2.Velocity=sparkdir[0]*2, sparkdir[1]*450.0, sparkdir[2]*2
	dirt2.RandomVelocity=30
	dirt2.DeathTime=Bladex.GetTime()+0.2

    


def GenericSectorOnHit(sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material):
	try:
		obj= Bladex.GetEntity(entity_name)
		if obj.Data.NoFXOnHit:
			return
	except: pass
	if Reference.MaterialOnHitInfo.has_key(material):
		on_hit_info= Reference.MaterialOnHitInfo[material]
	else:
		on_hit_info= Reference.MaterialOnHitInfo['default']
	sound= on_hit_info[0]
	func=  on_hit_info[1]

	if sound:
		sound.Stop()
		sound.Play(xhit_point, yhit_point, zhit_point, 0)
	if func:
		func (sector_index, entity_name, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm, material)

def SetSectorOnHitFuncs():
	GolpeGrava= Bladex.CreateSound('../../Sounds/golpe_grava.wav', 'GolpeGrava')
	GolpeGrava.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeNieve= Bladex.CreateSound('../../Sounds/golpe-nieve.wav', 'GolpeNieve')
	GolpeNieve.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeTierra= Bladex.CreateSound('../../Sounds/golpe_hierba.wav', 'GolpeTierra')
	GolpeTierra.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeAgua= Bladex.CreateSound('../../Sounds/golpe_agua.wav', 'GolpeAgua')
	GolpeAgua.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeHierba= Bladex.CreateSound('../../Sounds/golpe_hierba2.wav', 'GolpeHierba')
	GolpeHierba.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeMaderaTablas= Bladex.CreateSound('../../Sounds/golpe_maderamed.wav', 'GolpeMaderaTablas')      ### PLAGUE: Duplicated wtf?
	GolpeMaderaTablas.SetPitchVar(1, -8000, 8000, 0, 0)

	# GolpeMaderaTablas= Bladex.CreateSound('../../Sounds/golpe_maderamed.wav', 'GolpeMaderaTablas')
	# GolpeMaderaTablas.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeMadera= Bladex.CreateSound('../../Sounds/M-GOLPESHEAVY4.wav', 'GolpeMadera')
	GolpeMadera.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeMetal= Bladex.CreateSound('../../Sounds/GOLPE-ARMADUR-1.wav', 'GolpeMetal')
	GolpeMetal.SetPitchVar(1, -8000, 8000, 0, 0)

	GolpeCristal= Bladex.CreateSound('../../Sounds/golpe-cristal-4.wav', 'GolpeCristalWorld')
	GolpeCristal.SetPitchVar(1, -8000, 8000, 0, 0)


	Reference.MaterialOnHitInfo['default']=      [GolpeGrava, SectorThrowSparks]

	Reference.MaterialOnHitInfo['Grava']=        [GolpeGrava, SectorThrowSparks]
	Reference.MaterialOnHitInfo['Piedra']=       [GolpeGrava, SectorThrowSparks]
	Reference.MaterialOnHitInfo['Nieve']=        [GolpeNieve, SectorThrowSnow]
	Reference.MaterialOnHitInfo['Hierba']=       [GolpeHierba, SectorThrowDirt]
	Reference.MaterialOnHitInfo['Tierra']=       [GolpeTierra, SectorThrowDirt]

	Reference.MaterialOnHitInfo['Madera']=       [GolpeMadera, SectorThrowWood]
	Reference.MaterialOnHitInfo['MaderaTablas']= [GolpeMaderaTablas, SectorThrowWood]
	Reference.MaterialOnHitInfo['MaderaPodrida']=[GolpeMadera, SectorThrowWood]          ### Added -LeadHead
	Reference.MaterialOnHitInfo['Barro']=        [None, None]
	Reference.MaterialOnHitInfo['Water']=        [GolpeAgua, SectorThrowWater]
	Reference.MaterialOnHitInfo['Metal']=        [GolpeMetal, SectorThrowSparks]
	Reference.MaterialOnHitInfo['cristal']=      [GolpeCristal, None]
	Reference.MaterialOnHitInfo['Cristal']=      [GolpeCristal, None]

	if netgame.GetNetState() == 0:
		for i in range (Bladex.nSectors()):
			sector= Bladex.GetSector(i)
			if not sector.OnHit:
				sector.OnHit= GenericSectorOnHit


Bladex.AddScheduledFunc(Bladex.GetTime(), SetSectorOnHitFuncs, (), "SetSectorOnHitFuncs")


######
## Functions for adding default sparks
######
## -LeadHead
## We start off by a list of entities in which spark type they belong.
## There are items here which generally do not create sparks,
## But if you want to use them in custom maps as static objects, most should be here.


WoodSparkEntities  = ["ArbolNevado2",
                      "Arbolseco",
                      "Arbolseco2",
                      "Armero",
                      "Armero2",
                      "Atril",
                      "Banco",
                      "Barril",
                      "BlasonAurelio",
                      "ButacaMago",
                      "Caja_i_r",
                      "Cajama",
                      "Cajon",
                      "Cajon2",
                      "Camabad",
                      "Camastro",
                      "Carretilla",
                      "Cofre",
                      "Cubo",
                      "Estaca",
                      "EstacaFernando",
                      "Fuelle",
                      "Astillas1",
                      "Astillas2",
                      "Astillas3",
                      "Mesa",
                      "Mesita",
                      "Meson",
                      "Mesonroto",
                      "Palanca2",
                      "PalancaSuelo",
                      "Palancatortura",
                      "Panoplia",
                      "PasarelaLarga",
                      "Pelele",
                      "PeleleNevado",
                      "PlataformaFernando",
                      "Plataforma",
                      "PlataformaRail",
                      "PuenteAdolfoDerecho",
                      "PuenteAdolfoIzquierdo",
                      "PuenteAurelio",
                      "Puenteau_Plano",
                      "PuenteFernando",
                      "puertagran",
                      "puertamed",
                      "puertapeque1",
                      "puertapeque2",
                      "puertapeque3",
                      "puertapeque4",
                      "Rama1",
                      "Rama2",
                      "RamaNevada",
                      "Silla",
                      "Tabla_rota",
                      "Tabla_l",
                      "Tabla_rota2",
                      "Tabla_xl",
                      "Tabla_xlpieza2",
                      "Tabla_xPieza1",
                      "Tablatortura",
                      "Timon",
                      "Tocon",
                      "Totem",
                      "Totem2",
                      "Trampilla",
                      "TroncoGrande",
                      "TroncoTrampa",
                      "Trono",
                      "TronoManuel",
                      "trozogran1",
                      "trozogran2",
                      "Viga",
                      "VigaPlana",
                      "Vigaro1",
                      "Vigaro2"]

StoneSparkEntities = ["AdoquinPulsador",
                      "Adoquinpulsador2",
                      "AdoquinRuna",
                      "AdoquinRuna2",
                      "AdoquinRuna3",
                      "Altar", 
                      "AntorchaAtlante",
                      "Bloque",
                      "BloqueTallado",
                      "BoladePiedra",
                      "Brasero1",
                      "Braseroarana",
                      "CabezaFernando"
                      "Cabezon",
                      "CabezaSerpiente",
                      "Cebolla",
                      "Cepo",
                      "ColaSerpiente",
                      "Columnaestrecha",
                      "Columna",
                      "Dragon_estatua",
                      "Elefante",
                      "Esquirla",
                      "Estalact1",
                      "Estalact2",
                      "EstatuaGolem",
                      "Fetiche",
                      "GargolaFernando",
                      "Gargola",
                      "Gargola02",
                      "GargolaNevada",
                      "Gozne",
                      "Halcon",
                      "Halcon2",
                      "ElefantePartido",
                      "Hornacina",
                      "LamparaKongo",
                      "LamparaMiguel",
                      "Lapida",
                      "Obelisco",
                      "Lapida3",
                      "LapidaAmazona",
                      "LapidaBarbaro",
                      "LapidaCaballero",
                      "LapidaManuel",
                      "Menhir1",
                      "Menhir2",
                      "Menhir3",
                      "Monjecaliz",
                      "Monjema",
                      "Monjespada",
                      "ObeliscoGrande",
                      "ObeliscoNevado",
                      "Palanca1",
                      "Peanapiedra",
                      "PiedraNevada",
                      "Piedra_01",
                      "Piedra_02",
                      "Piedra_03",
                      "Piedra_04",
                      "Piedra_05",
                      "Piedra_06",
                      "Piedra_07",
                      "Piedra_08",
                      "Piedra_09",
                      "Piedra_10",
                      "PiedraInformativa",
                      "PiedrasBarbaro",
                      "PiedraNevadaCortada",
                      "PlacaTallada",
                      "PuertaMiguelDerecha",
                      "PuertaMiguelIzquierda",
                      "ReinaAurelio",
                      "Reyaurelio",
                      "Roca1Aurelio",
                      "Roca2Aurelio",
                      "Roca1",
                      "Roca2",
                      "Roca3",
                      "SoporteOrbe",
                      "Supositorio",
                      "Tablilla1",
                      "Tablilla2",
                      "Tablilla3",
                      "Tablilla4",
                      "Tablilla5",
                      "Tablilla6",
                      "Taburete",
                      "Tronoliso",
                      "TronoEscarabeu",
                      "Tronera",
                      "Lapidareina",
                      "Lapidarey",
                      "Zocalo1"]

MetalSparkEntities = ["Antorcha2",
                      "Argolla",
                      "Armadura",
                      "BarroteAurelio",
                      "Blason1",
                      "Blason2",
                      "Blason3",
                      "Blason4",
                      "Blason5",
                      "Blason6",
                      "Caja_i_i",
                      "Campana",
                      "CandilAurelio",
                      "Candelabro",
                      "Candelpeque",
                      "Candil",
                      "Candil2",
                      "Carburo",
                      "Cazo",
                      "CerraduraBlade",
                      "Cerradura",
                      "Cerraduracobox",
                      "Cerraduracutre",
                      "Cerradurcob",
                      "Cerradurdor",
                      "Cerradurpla",
                      "Cincel",
                      "Cofrepeque",
                      "Cupula",
                      "Farol",
                      "Farol2",
                      "GanchoAurelio",
                      "Gancho",
                      "Garfio",
                      "Garfio2",
                      "Garfio3",
                      "Globo",
                      "Grifoserpiente",
                      "Jaula",
                      "Keysup",
                      "Lamparatecho",
                      "LamparaNegra",
                      "Lampared",
                      "LamparaAurelio",
                      "Lampcolg",
                      "Lamparaegipto",
                      "Gancholamp",
                      "Lanzapivotes",
                      "LeonBronce",
                      "Palanca3",
                      "PasarelaCorta",
                      "Pendulo",
                      "Pendulo2",
                      "Perola",
                      "PinchoManuel",
                      "PinchoMiguel",
                      "Pinchos",
                      "PinchoSotano",
                      "PowerupGold",
                      "PowerupSilver",
                      "PuertaFernando",
                      "Rail",
                      "Rail2",
                      "Rastrillo",
                      "Rastrillo2",
                      "Rastrillo3",
                      "Rastrillo10",
                      "Rastrillo32",
                      "Rastrillo102",
                      "Reja",
                      "Semipuxero",
                      "Telescopio",
                      "Vagoneta",
                      "Varilla",
                      "Varillaancha",
                      "Yunque",
                      "Zocalo2",
                      "Zocalo3",
                      "ZocaloSerpiente",
                      "ZocaloTimon"]

## Then we simply use "SetDefaultSparkling" for any object and the game will automatically parse what it needs.

def SetDefaultSparkling(obj):
    obj=Bladex.GetEntity(obj.Name)
    if obj.Kind in WoodSparkEntities:
        SetWoodenSparkling(obj)
    elif obj.Kind in StoneSparkEntities:
        SetStoneSparkling(obj)
    elif obj.Kind in MetalSparkEntities:
        SetMetalSparkling(obj)
    else:
        SetDustySparkling(obj)