##///
##||| GenFX.PY TITANIUM
##||| Change list:
##||| * Added support for empty powerpotions.
##||| * 
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 

import Bladex
import AuxFuncs
import whrandom
import InitDataField
import GameStateAux
import Auras
import Objects
import CharStats
import ObjStore




############################################
#     Level effects y cosas del estilo     #
############################################


def LevelUpFX(EntityName, ColourGradation, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args, PSParams, LightIntensity, timer="Timer15", timespersec=15, sound=""):

	# ColourGradation=0/1
	# AuraParams=(Size, Alpha, ColourIntensity, HideFrontFaces, HideBackFaces, AlphaMode)
	# AuraGradient=(Gap, r1, g1, b1, alpha1, StartingPoint, r2, g2, b2, alpha2, EndingPoint)
	# AuraVarArgs=(init_size, end_size, init_alpha, end_alpha, time)
	# PSParams=(LevelUpParticleData, ParticleType, ParticleLife, r, g, b, PPS, YGravity, Friction, RandomVelocity, NormalVelocity, FollowFactor, Time2Live, DeathTime)

	ent=Bladex.GetEntity(EntityName)
	if ColourGradation:
		maxlevel=CharStats.GetMaxLevel()
		frlevel=maxlevel/4.0
		fr1level=round(frlevel)
		fr2level=round(2.0*frlevel)
		fr3level=round(3.0*frlevel)
		clevel=ent.Level
		if clevel>fr3level:
			r=255
			g=255*(min(max(0, (maxlevel-clevel)/(maxlevel-fr3level)), 1)) # 255->0
			b=0
		elif clevel>fr2level:
			r=255*(min(max(0, (clevel-fr2level)/(fr3level-fr2level)), 1)) # 0->255
			g=255
			b=0
		elif clevel>fr1level:
			r=0
			g=255
			b=255*(min(max(0, (fr2level-clevel)/(fr2level-fr1level)), 1)) # 255->0
		else:
			r=0
			g=255*(min(max(0, (clevel/fr1level)), 1)) # 0->255
			b=255
		AuraGradient=(AuraGradient[0], r/255.0, g/255.0, b/255.0, AuraGradient[4], AuraGradient[5], r/255.0, g/255.0, b/255.0, AuraGradient[9], AuraGradient[10])
	else:
		r=PSParams[3]
		g=PSParams[4]
		b=PSParams[5]
	LevelUpParticleData=PSParams[0]
	for i in range(PSParams[2]):
		Bladex.SetParticleGVal(PSParams[1], i, r, g, b, LevelUpParticleData[2*i], LevelUpParticleData[2*i+1])
	AuraName=EntityName+"AuraLevelUp"
	a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2=AuraName, AuraVar2Args[0], AuraVar2Args[1], AuraVar2Args[2], AuraVar2Args[3], AuraVar2Args[4], 1, "", (), timer, timespersec
	a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1=AuraName, AuraVar1Args[0], AuraVar1Args[1], AuraVar1Args[2], AuraVar1Args[3], AuraVar1Args[4], 0, AuxFuncs.FadeAndScaleAura, (a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2), timer, timespersec
	alup=Bladex.CreateEntity(AuraName, "Entity Aura", 0, 0, 0)
	alup.SetAuraParams(AuraParams[0], AuraParams[1], AuraParams[2], AuraParams[3], AuraParams[4], AuraParams[5])
	alup.SetAuraGradient(AuraGradient[0], AuraGradient[1], AuraGradient[2], AuraGradient[3], AuraGradient[4], AuraGradient[5], AuraGradient[6], AuraGradient[7], AuraGradient[8], AuraGradient[9], AuraGradient[10])
	ent.Link(alup)
	alup.SetAuraActive(1)
	AuxFuncs.FadeAndScaleAura(a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1)
	PSName=EntityName+"PSLevelUp"
	pslup=Bladex.CreateEntity(PSName, "Entity Particle System Dperson", 0, 0, 0)
	pslup.PersonName=EntityName
	pslup.ParticleType=PSParams[1]
	pslup.PPS=PSParams[6]
	pslup.YGravity=PSParams[7]
	pslup.Friction=PSParams[8]
	pslup.RandomVelocity=PSParams[9]
	pslup.NormalVelocity=PSParams[10]
	pslup.FollowFactor=PSParams[11]
	pslup.Time2Live=PSParams[12]
	pslup.Velocity=0.0, 0.0, 0.0
	pslup.DeathTime=Bladex.GetTime()+PSParams[13]
	LightName=EntityName+"LightLevelUp"
	llup=Bladex.CreateEntity(LightName, "Entity Spot", 0, 0, 0)
	llup.Color=r, g, b
	llup.Intensity=0.0
	llup.Precission=0.01
	llup.CastShadows=0
	llup.Visible=0
	llup.Flick=0
	ent.Link(llup)
	AuxFuncs.SpotIntensityVariation(LightName, 0.0, LightIntensity, f1/1.6, 0, 0.0, 0.0, timer, timespersec)
	Bladex.AddScheduledFunc(Bladex.GetTime()+f1, AuxFuncs.SpotIntensityVariation, (LightName, LightIntensity, 0.0, f2/1.2, 1, 0.0, 0.0, timer, timespersec))
	if sound:
		soundlup=Bladex.CreateSound(sound,EntityName+"SoundLevelUp")
		soundlup.MinDistance=10000
		soundlup.MaxDistance=20000
		soundlup.PlayStereo()


def ChangeNodesElectricDischarge(person_name, ray_name, list_of_nodes, timespersec, endtime):
	person=Bladex.GetEntity(person_name)
	ray=Bladex.GetEntity(ray_name)
	n1=whrandom.randint(0, len(list_of_nodes)-1)
	n2=whrandom.randint(0, len(list_of_nodes)-1)
	while n1==n2:
		n2=whrandom.randint(0, len(list_of_nodes)-1)
	node1=list_of_nodes[n1]
	node2=list_of_nodes[n2]
	ray.Position=person.Rel2AbsPoint(0, 0, 0, node1)
	ray.Target=person.Rel2AbsPoint(0, 0, 0, node2)
	if Bladex.GetTime()>endtime:
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0/timespersec, ray.SubscribeToList, ("Pin",))
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0/timespersec, ChangeNodesElectricDischarge, (person_name, ray_name, list_of_nodes, timespersec, endtime))

def ElectricDischarge(person_name, ray_name, r, g, b, amplitude, list_of_nodes, timespersec, time):
	person=Bladex.GetEntity(person_name)
	ray=Bladex.CreateEntity(ray_name, "Entity ElectricBolt", 0, 0, 0)
	ray.Target=0, 0, 0
	ray.FixedTarget=0
	ray.MaxAmplitude=amplitude
	ray.MinSectorLength=10000
	ray.CoreGlowColor=r, g, b
	ray.InnerGlowColor=r/2, g/2, b/2
	ray.OuterGlowColor=0.0, 0.0, 0.0
	ray.Damage=0
	ray.Active=1
	n1=whrandom.randint(0, len(list_of_nodes)-1)
	n2=whrandom.randint(0, len(list_of_nodes)-1)
	while n1==n2:
		n2=whrandom.randint(0, len(list_of_nodes)-1)
	node1=list_of_nodes[n1]
	node2=list_of_nodes[n2]
	ray.Position=person.Rel2AbsPoint(0, 0, 0, node1)
	ray.Target=person.Rel2AbsPoint(0, 0, 0, node2)
	endtime=Bladex.GetTime()+time
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0/timespersec, ChangeNodesElectricDischarge, (person_name, ray_name, list_of_nodes, timespersec, endtime))




#############################################
#     Efectos visuales de algunas armas     #
#############################################


class WeaponFX:

	def __init__(self, WeaponName, auraparams, auragradient, prtldata, lightdata):
		self.ObjId= ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]= self
		weapon=Bladex.GetEntity(WeaponName)
		self.WeaponName=WeaponName
		self.Aura=None
		self.Particles=None
		self.Light=None
		if auraparams:
			s, a, ci, f, b, am=auraparams
			m, r1, g1, b1, a1, imd, r2, g2, b2, a2, emd=auragradient
			self.Aura=Bladex.CreateEntity(WeaponName+"Aura", "Entity Aura", 0, 0, 0)
			self.Aura.SetAuraParams(s, a, ci, f, b, am)
			self.Aura.SetAuraGradient(m, r1, g1, b1, a1, imd, r2, g2, b2, a2, emd)
			weapon.Link(self.Aura)
			self.Aura.SetAuraActive(1)
		if prtldata:
			pt, pps, v, nv, rv, g, fr, ff, t2l=prtldata
			self.Particles=Bladex.CreateEntity(WeaponName+"Particles", "Entity Particle System Dobj", 0, 0, 0)
			self.Particles.ObjectName=WeaponName
			self.Particles.ParticleType=pt
			self.Particles.PPS=pps
			self.Particles.Velocity=v
			self.Particles.NormalVelocity=nv
			self.Particles.RandomVelocity=rv
			self.Particles.YGravity=g
			self.Particles.Friction=fr
			self.Particles.FollowFactor=ff
			self.Particles.Time2Live=t2l
		if lightdata:
			i, color, fl=lightdata
			self.Light=Bladex.CreateEntity(WeaponName+"Light", "Entity Spot", 0, 0, 0)
			self.Light.Intensity=i
			self.Light.Color=color
			self.Light.Flick=fl
			self.Light.CastShadows=0
			self.Light.Visible=0
			weapon.Link(self.Light)

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.WeaponName,
				GameStateAux.SaveEntityAux(self.Aura),
				GameStateAux.SaveEntityAux(self.Particles),
				GameStateAux.SaveEntityAux(self.Light)
			)


	def __setstate__(self,parm):
		print "GenFX.__setstate__()",parm
		if parm[0]==1:
			self.ObjId= parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.WeaponName=parm[2]
			self.Aura=GameStateAux.LoadEntityAux(parm[3])
			self.Particles=GameStateAux.LoadEntityAux(parm[4])
			self.Light=GameStateAux.LoadEntityAux(parm[5])
		else:
			print "WeaponFX.__setstate__() -> Version mismatch"
			self.WeaponName=""
			self.Aura=""
			self.Particles=""
			self.Light=""
			self.ObjId= ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self



def AddWeaponFX(WeaponName, data):
	weapon=Bladex.GetEntity(WeaponName)
	if not weapon:
		print "El arma especificada no existe!"
		return
	if not data:
		InitDataField.Initialise(weapon)
		data= weapon.Data

	if weapon.Kind in ("QueenSword", "VampWeapon"):
		auraparams=(80, 1, 1, 0, 0, 0) # (Size, Alpha, ColorIntensity, HideFrontFaces, HideBackFaces, AdditiveMode)
		auragradient=(2, 0.8, 0.1, 0.1, 0.2, 0.0, 0.4, 0.0, 0.0, 0.0, 0.6) # (Margin, r, g, b, a, InitMarginDistance, r, g, b, a, EndMarginDistance)
		if weapon.Kind=="VampWeapon":
			prtldata=("GotasSangre", 20, (0.0, 0.0, 0.0), 0.0, 0.0, 2000.0, 0.01, 0.0, 24) # (PrtlType, PPS, Vel=(v1, v2, v3), NormalVel, RndVel, YGrav, Friction, FollowFactor, Time2Live)
		else:
			prtldata=()
		lightdata=() # (Intensity, Color=(r, g, b), Flick)
	elif weapon.Kind in ("CrushHammer", "DalWeapon", "SteelFeather"):
		auraparams=(80, 1, 1, 0, 0, 0)
		auragradient=(2, 0.5, 0.6, 0.0, 0.2, 0.0, 0.2, 0.3, 0.0, 0.1, 0.5)
		prtldata=("GasVenenoso", 30, (0.0, 0.0, 0.0), 0.0, 1.0, 0.0, 0.02, 0.0, 60)
		lightdata=()
	elif weapon.Kind in ("FireBigSword", "FireAxe", "FireSword", "FireBo"):
		auraparams=(40, 1, 1, 0, 0, 1)
		auragradient=(2, 0.8, 0.6, 0.0, 0.6, 0.0, 0.8, 0.1, 0.0, 0.0, 0.6)
		prtldata=("Llamita", 400, (0.0, 0.0, 0.0), 1.0, 0.0, -1000.0, 0.02, 0.0, 10)
		lightdata=(1.0, (255, 120, 0), 1)
		weapon.SelfIlum=0.8
	elif weapon.Kind in ("IceAxe", "IceHammer", "IceSword", "IceWand"):
		auraparams=(15, 0.8, 1, 0, 1, 0)
		auragradient=(2, 0.9, 1.0, 1.0, 0.2, 0.1, 0.4, 0.8, 1.0, 0.2, 1.0)
		prtldata=("Vaho", 20, (0.0, 0.0, 0.0), 0.0, 1.0, 150.0, 0.02, 0.0, 60)
		lightdata=()
		# weapon.SelfIlum=0.2
		weapon.Alpha=0.0
		# weapon.RasterMode="AdditiveAlpha"
		CreateMultiParts(WeaponName)
		
	elif weapon.Kind in ("BladeSword2", "BladeSword2Barbarian"):
		auraparams=(80, 1, 1, 0, 0, 1)
		auragradient=(2, 0.8, 0.9, 1.0, 0.6, 0.0, 0.3, 0.4, 0.9, 0.0, 0.6)
		prtldata=("BrillosBladeSword", 15, (0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.01, 0.0, 6)
		lightdata=(1.0, (235, 245, 255), 0)
		weapon.SelfIlum=0.8
	else:
		print "No hay efecto definido para este tipo de arma!"
		return
	data.WeaponFX=WeaponFX(WeaponName, auraparams, auragradient, prtldata, lightdata)

###			 	  ###
# Multi-part object #
#					#
###				  ###
def CreateMultiParts(objName):
	obj    = Bladex.GetEntity(objName)
	kind   = obj.Kind
	oldPos = obj.Position
	oldOri = obj.Orientation
	obj.Position = 0.0, 0.0, 0.0
	obj.Orientation = (1.0, 0.0, 0.0, 0.0)

	# x,y,z = 1.0 / obj.Position[0] , 1.0 / obj.Position[1], 1.0 / obj.Position[2]
	if kind == ("IceHammer"):
		type_part = kind+"Pieza"
		partposrel= [(-176.01,0,413.108), (179.492,-58.747,444.756), (179.494,0,413.737), (-179.494,58.747,444.756), (0,0,318.22), (0,0,0)]
		n_parts   = (0, 1, 2, 3, 4, 5)
		partsAlph = (0.7, 0.7, 0.7, 0.7, 0.7, 1.0)
		partsIlum = (0.2, 0.2, 0.2, 0.2, 0.2, 0.0)
	elif kind == ("IceSword"):
		type_part = kind+"Part"
		partposrel= [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
		n_parts   = (0, 1)
		partsAlph = (1.0, 0.7)
		partsIlum = (0.0, 0.2)
	elif kind == ("IceWand"):
		type_part = kind+"Part"
		partposrel= [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
		n_parts   = (0, 1)
		partsAlph = (1.0, 0.7)
		partsIlum = (0.0, 0.2)
	elif kind == ("IceAxe"):
		type_part = kind+"Part"
		partposrel= [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
		n_parts   = (0, 1)
		partsAlph = (1.0, 0.7)
		partsIlum = (0.0, 0.2)
	else: 
		print "error in GenFX.CreateMultiParts() - invalid kind!"
		obj.Position    = oldPos
		obj.Orientation = oldOri
		return
        
	for n in n_parts:
		int_obj_name=objName+"Part"+`n+1`
		part=Bladex.CreateEntity(int_obj_name, type_part+`n+1`, 0.0, 0.0, 0.0)
		part.Solid=0
		part.CastShadows=0
		part.Alpha=partsAlph[n]
		part.SelfIlum=partsIlum[n]
		partpos=obj.Rel2AbsPoint(partposrel[n][0], partposrel[n][1], partposrel[n][2])
		part.Position=partpos[0], partpos[1], partpos[2]
		obj.Link(part)
	obj.Position = oldPos
	obj.Orientation = oldOri
		


#############################################
#     Efectos visuales de algunos items     #
#############################################


class PersonItemFX:

	def __init__(self, PersonName, ItemName, TimeEffect):
		pers=Bladex.GetEntity(PersonName)
		item=Bladex.GetEntity(ItemName)
		time=Bladex.GetTime()
		self.PersonName=PersonName
		self.ItemName=ItemName

		AuraParams0=(240, 0.01, 1.0, 0, 1, 1)
		AuraParams1=(50 , 1.0 , 1.0, 0, 1, 1)
		AuraParams2=(40 , 0.6 , 1.0, 0, 1, 1)

		XtraParam0=('Bladex.GetEntity("'+PersonName+'").SelfIlum', 0.0)
		XtraParam1=('Bladex.GetEntity("'+PersonName+'").SelfIlum', 0.6)
		XtraParam2=('Bladex.GetEntity("'+PersonName+'").SelfIlum', 0.1)

		if item.Kind in ("PowerPotion", "PowerPotion_E"): ### Added PowerPotion_E. There has to be a better way tho. -LeadHead

			AuraGradient0=(2,  0.2, 0.4, 0.8, 1.0, 0.2  ,  0.0, 0.2, 0.8, 0.0, 0.7)
			AuraGradient1=(2,  0.8, 0.9, 1.0, 1.0, 0.2  ,  0.0, 0.2, 0.9, 0.1, 1.0)

			self.Aura=Auras.MakeAura(PersonName, TimeEffect, AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)
			self.Aura.Data.AddEvent (time+1.0,               AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-4.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-3.6,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-3.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.7,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-2.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.0,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.7,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.5,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.2,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.05,   AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.0,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect,        AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)

		elif item.Kind=="Brazalete":

			AuraGradient0=(2,  0.8, 0.6, 0.0, 1.0, 0.2  ,  0.4, 0.3, 0.0, 0.0, 0.7)
			AuraGradient1=(2,  1.0, 0.9, 0.5, 1.0, 0.1  ,  0.4, 0.3, 0.0, 0.0, 1.0)

			self.Aura=Auras.MakeAura(PersonName, TimeEffect, AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)
			self.Aura.Data.AddEvent (time+1.0,               AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-4.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-3.6,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-3.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.7,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-2.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.0,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.7,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.5,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.2,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.05,   AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.0,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect,        AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)

		elif item.Kind=="Corona":

			AuraGradient0=(2,  1.0, 0.4, 0.0, 1.0, 0.2  ,  1.0, 0.0, 0.0, 0.0, 0.7)
			AuraGradient1=(2,  1.0, 0.7, 0.0, 1.0, 0.1  ,  1.0, 0.0, 0.0, 0.0, 1.0)

			self.Aura=Auras.MakeAura(PersonName, TimeEffect, AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)
			self.Aura.Data.AddEvent (time+1.0,               AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-4.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-3.6,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-3.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.7,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-2.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.0,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.7,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.5,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.2,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.05,   AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.0,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect,        AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)

		else: # para item.Kind=="Amuletofantasma"

			AuraGradient0=(2,  0.0, 1.0, 0.4, 1.0, 0.2  ,  0.0, 0.8, 0.0, 0.0, 0.7)
			AuraGradient1=(2,  0.0, 1.0, 0.7, 1.0, 0.1  ,  0.0, 0.6, 0.0, 0.0, 1.0)

			self.Aura=Auras.MakeAura(PersonName, TimeEffect, AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)
			self.Aura.Data.AddEvent (time+1.0,               AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-4.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-3.6,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-3.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.7,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-2.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-2.0,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.7,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.5,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.3,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.2,    AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.1,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect-1.05,   AuraParams2, (), (), AuraGradient1  ,  1,  XtraParam2)
			self.Aura.Data.AddEvent (time+TimeEffect-1.0,    AuraParams1, (), (), AuraGradient1  ,  1,  XtraParam1)
			self.Aura.Data.AddEvent (time+TimeEffect,        AuraParams0, (), (), AuraGradient0  ,  1,  XtraParam0)


	def __getstate__(self):
		return (1,
				self.PersonName,
				self.ItemName,
				GameStateAux.SaveEntityAux(self.Aura),
			)


	def __setstate__(self,parm):
		if parm[0]==1:
			self.PersonName=parm[1]
			self.ItemName=parm[2]
			self.Aura=GameStateAux.LoadEntityAux(parm[3])
		else:
			print "ItemFX.__setstate__() -> Version mismatch"
			self.PersonName=""
			self.ItemName=""
			self.Aura=""



def AddPersonItemFX(PersonName, ItemName, TimeEffect):
	pers=Bladex.GetEntity(PersonName)
	item=Bladex.GetEntity(ItemName)
	if ((not item) or (item.Kind not in ("PowerPotion", "PowerPotion_E", "Amuletofantasma", "Brazalete", "Corona"))): # Same as above. -LeadHead
		print "El item especificado no existe no hay efecto definido para este tipo de item!"
		return
	pers.Data.PersonItemFX=PersonItemFX(PersonName, ItemName, TimeEffect)




###############################
#     Teletransportadores     #
###############################


def ChangeRasterMode(ent_name, mode):
	Bladex.GetEntity(ent_name).RasterMode=mode

def PersonMagicallyAppearing():
	TimeEffect=2.0
	time=Bladex.GetTime()
	char=Bladex.GetEntity("Player1")
	char.Alpha=0.01
	char.RasterMode="Read"
	Bladex.AddScheduledFunc(time+TimeEffect, ChangeRasterMode, ("Player1", "Full"))
	AuxFuncs.FadeObject("Player1", 0.01, 1.0, 2.0)
	if char.InvLeft<>"":
		obj=Bladex.GetEntity(char.InvLeft)
		obj.RasterMode="Read"
		Bladex.AddScheduledFunc(time+TimeEffect, ChangeRasterMode, (char.InvLeft, "Full"))
		AuxFuncs.FadeObject(char.InvLeft, 0.01, obj.Alpha, TimeEffect)
	if char.InvRight<>"":
		obj=Bladex.GetEntity(char.InvRight)
		obj.RasterMode="Read"
		Bladex.AddScheduledFunc(time+TimeEffect, ChangeRasterMode, (char.InvRight, "Full"))
		AuxFuncs.FadeObject(char.InvRight, 0.01, obj.Alpha, TimeEffect)
	if char.InvLeftBack<>"":
		obj=Bladex.GetEntity(char.InvLeftBack)
		obj.RasterMode="Read"
		Bladex.AddScheduledFunc(time+TimeEffect, ChangeRasterMode, (char.InvLeftBack, "Full"))
		AuxFuncs.FadeObject(char.InvLeftBack, 0.01, obj.Alpha, TimeEffect)
	if char.InvRightBack<>"":
		obj=Bladex.GetEntity(char.InvRightBack)
		obj.RasterMode="Read"
		Bladex.AddScheduledFunc(time+TimeEffect, ChangeRasterMode, (char.InvRightBack, "Full"))
		AuxFuncs.FadeObject(char.InvRightBack, 0.01, obj.Alpha, TimeEffect)
	AuraParams0=(240, 0.01, 1.0, 0, 1, 1)
	AuraParams1=(50 , 1.0 , 1.0, 0, 1, 1)
	AuraParams2=(50 , 0.01, 1.0, 0, 1, 1)
	AuraGradient0=(2,  0.2, 0.4, 0.8, 1.0, 0.2  ,  0.0, 0.2, 0.8, 0.0, 0.7)
	AuraGradient1=(2,  0.8, 0.9, 1.0, 1.0, 0.2  ,  0.0, 0.2, 0.9, 0.1, 1.0)
	aura=Auras.MakeAura("Player1", TimeEffect, AuraParams0, (), (), AuraGradient0)
	aura.Data.AddEvent (time+TimeEffect/2.0, AuraParams1, (), (), AuraGradient1)
	aura.Data.AddEvent (time+TimeEffect, AuraParams2, (), (), AuraGradient0)
	ps=Bladex.CreateEntity("PSPersonMagicallyAppearing", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	ps.PersonName="Player1"
	ps.ParticleType="FastEnergyConc"
	ps.PPS=200
	ps.YGravity=0.0
	ps.Friction=0.0
	ps.Velocity=0.0, 0.0, 0.0
	ps.RandomVelocity=0.5
	ps.NormalVelocity=-2.0
	ps.Time2Live=30
	ps.DeathTime=time+TimeEffect/2.0


def PersonMagicallyDisappearing():
	TimeEffect=2.0
	time=Bladex.GetTime()
	char=Bladex.GetEntity("Player1")
	char.Alpha=1.0
	char.RasterMode="Read"
	AuxFuncs.FadeObject("Player1", 1.0, 0.01, TimeEffect)
	if char.InvLeft<>"":
		obj=Bladex.GetEntity(char.InvLeft)
		obj.RasterMode="Read"
		AuxFuncs.FadeObject(char.InvLeft, obj.Alpha, 0.01, TimeEffect)
	if char.InvRight<>"":
		obj=Bladex.GetEntity(char.InvRight)
		obj.RasterMode="Read"
		AuxFuncs.FadeObject(char.InvRight, obj.Alpha, 0.01, TimeEffect)
	if char.InvLeftBack<>"":
		obj=Bladex.GetEntity(char.InvLeftBack)
		obj.RasterMode="Read"
		AuxFuncs.FadeObject(char.InvLeftBack, obj.Alpha, 0.01, TimeEffect)
	if char.InvRightBack<>"":
		obj=Bladex.GetEntity(char.InvRightBack)
		obj.RasterMode="Read"
		AuxFuncs.FadeObject(char.InvRightBack, obj.Alpha, 0.01, TimeEffect)
	AuraParams0=(240, 0.01, 1.0, 0, 1, 1)
	AuraParams1=(50 , 1.0 , 1.0, 0, 1, 1)
	AuraParams2=(50 , 0.01, 1.0, 0, 1, 1)
	AuraGradient0=(2,  0.2, 0.4, 0.8, 1.0, 0.2  ,  0.0, 0.2, 0.8, 0.0, 0.7)
	AuraGradient1=(2,  0.8, 0.9, 1.0, 1.0, 0.2  ,  0.0, 0.2, 0.9, 0.1, 1.0)
	aura=Auras.MakeAura("Player1", TimeEffect, AuraParams2, (), (), AuraGradient0)
	aura.Data.AddEvent (time+TimeEffect/2.0, AuraParams1, (), (), AuraGradient1)
	aura.Data.AddEvent (time+TimeEffect, AuraParams0, (), (), AuraGradient0)
	ps=Bladex.CreateEntity("PSPersonMagicallyAppearing", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	ps.PersonName="Player1"
	ps.ParticleType="EnergyDissip"
	ps.PPS=200
	ps.YGravity=0.0
	ps.Friction=0.0
	ps.Velocity=0.0, 0.0, 0.0
	ps.RandomVelocity=0.5
	ps.NormalVelocity=2.0
	ps.Time2Live=60
	ps.DeathTime=time+TimeEffect/3.0



class MagicTransport:

	def __init__(self, trsector_name, magictr_position):
		self.Position=x, y, z=magictr_position
		self.TrSectorMax=trsector_name
		self.TrSectorMin=trsector_name+"_In"
		self.MagicCilinder=Bladex.CreateEntity(trsector_name+"_Cil", "CilindroTransportador", x, y, z)
		self.MagicCilinder.Orientation=0.707107,0.707107,0.000000,0.000000
		self.MagicCilinder.Scale=0.1
		self.MagicCilinder.Alpha=0.0
		self.MagicCilinder.CastShadows=0
		self.AGE_Number=0
		Bladex.AddTriggerSector(trsector_name+"_In", "Transportadores", y+1150.0, y-1150.0, [(x+500.0, z+500.0), (x-500.0, z+500.0), (x-500.0, z-500.0), (x+500.0, z-500.0)])
		Bladex.SetTriggerSectorFunc(trsector_name+"_In", "OnEnter", self.UseMagicTransport)
		Bladex.SetTriggerSectorFunc(trsector_name, "OnEnter", self.OpenMagicTransport)
		Bladex.SetTriggerSectorFunc(trsector_name, "OnLeave", self.CloseMagicTransport)
		self.ObjId=ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]=self

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
			  self.ObjId,
			  self.Position,
			  self.TrSectorMax,
			  self.TrSectorMin,
			  self.AGE_Number,
			  GameStateAux.SaveEntityAux(self.MagicCilinder)
			 )

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Position=parm[2]
			self.TrSectorMax=parm[3]
			self.TrSectorMin=parm[4]
			self.AGE_Number=parm[5]
			self.MagicCilinder=GameStateAux.LoadEntityAux(parm[6])
		else:
			print "MagicTransport.__setstate__() -> Version mismatch"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Position=""
			self.TrSectorMax=""
			self.TrSectorMin=""
			self.AGE_Number=""
			self.MagicCilinder=""

	def RotateMagicCilinderGrad(self, obj_name, time):
		self.MagicCilinder.RotateRel(0, 0, 0, 0, 0, 1, 0.08)

	def RotateMagicCilinder(self):
		self.MagicCilinder.TimerFunc=self.RotateMagicCilinderGrad
		self.MagicCilinder.SubscribeToList("Timer30")

	def OpenMagicTransport(self, trsector, ent_name):
		import GameText
		import MenuText
		AuxFuncs.ScaleObjectV2(self.MagicCilinder.Name, self.MagicCilinder.Scale, 1.0, -1, 2.0, self.RotateMagicCilinderGrad, (0 ,0), self.RotateMagicCilinder, (), 0)
		self.AGE_Number=self.AGE_Number+1
		openps=Bladex.CreateEntity(self.MagicCilinder.Name+"_PS_"+`self.AGE_Number`, "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		openps.ObjectName=self.MagicCilinder.Name
		openps.ParticleType="LittleEnergyDissip"
		openps.PPS=600
		openps.YGravity=0.0
		openps.Friction=0.0
		openps.Velocity=0.0, 0.0, 0.0
		openps.RandomVelocity=0.0
		openps.NormalVelocity=0.0
		openps.Time2Live=30
		GameText.ShowMessage(MenuText.GetMenuText("Enter the transporter to leave the map"))

	def CloseMagicTransport(self, trsector, ent_name):
		import GameText
		openps=Bladex.GetEntity(self.MagicCilinder.Name+"_PS_"+`self.AGE_Number`)
		if openps:
			openps.DeathTime=Bladex.GetTime()+2.0
			AuxFuncs.ScaleObjectV2(self.MagicCilinder.Name, self.MagicCilinder.Scale, 0.1, 1, 2.0, self.RotateMagicCilinderGrad, (0 ,0), "", (), 0)
			GameText.HideMessage()

	def UseMagicTransport(self, trsector, ent_name):
		import GotoMapVars
		import Scorer
		Bladex.RemoveTriggerSectorFunc(trsector, "OnEnter")
		Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		PersonMagicallyDisappearing()
		self.CloseMagicTransport(0, 0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, AuxFuncs.FadeTo, (2.0, 2.0))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, GotoMapVars.EndOfLevel, ())


def CreateMagicTransport(trsector_name, magictr_position):
	magictr=MagicTransport(trsector_name, magictr_position)
	return magictr





#######################################################################
#     Funciones genericas para generacion de FX en ciertos golpes     #
#######################################################################


####### Iluminacion

class LightFX:

	def __init__(self):
		self.Entity="Player1"
		self.TurnOnTime=1.0
		self.TurnOffTime=1.0
		self.QuickTurnOffTime=0.5
		self.MaxIntensity=2.0
		self.TimeMaxIntensity=2.0
		self.Color=255, 255, 255
		self.Flick=0


def AddParticles(entity_source_name, prtl_type, pps, rnd_vel, normal_vel, friction, time2live, death_time, ygravity=0):
	ent_src=Bladex.GetEntity(entity_source_name)
	if not ent_src:
		print "La entidad especificada como fuente de las particulas no existe!!!"
		return
	id_number=int(10.0*Bladex.GetTime())
	if ent_src.Person:
		prtl_sys=Bladex.CreateEntity(entity_source_name+"prtlsys"+`id_number`, "Entity Particle System Dperson",0,0,0)
		prtl_sys.PersonName=entity_source_name
	else:
		prtl_sys=Bladex.CreateEntity(entity_source_name+"prtlsys"+`id_number`, "Entity Particle System Dobj",0,0,0)
		prtl_sys.ObjectName=entity_source_name
	prtl_sys.ParticleType=prtl_type
	prtl_sys.Time2Live=time2live
	prtl_sys.PPS=pps
	prtl_sys.NormalVelocity=normal_vel
	prtl_sys.RandomVelocity=rnd_vel
	prtl_sys.Friction=friction
	prtl_sys.YGravity=ygravity
	prtl_sys.Velocity=0, 0, 0
	if death_time:
		prtl_sys.DeathTime=Bladex.GetTime()+death_time
	return prtl_sys


def ModifyParticles(prtl_sys, new_pps, new_rnd_vel, new_normal_vel, new_friction, new_time2live, new_death_time, new_ygravity=-1):
	prtl_sys.Time2Live=new_time2live
	prtl_sys.PPS=new_pps
	prtl_sys.NormalVelocity=new_normal_vel
	prtl_sys.RandomVelocity=new_rnd_vel
	prtl_sys.Friction=new_friction
	if new_ygravity<>-1:
		prtl_sys.YGravity=new_ygravity
	if new_death_time:
		prtl_sys.DeathTime=Bladex.GetTime()+new_death_time


def PlaySoundFX(sound, entity_source_name, volume, pitch):
	ent_src=Bladex.GetEntity(entity_source_name)
	if not ent_src:
		print "La entidad especificada como fuente del sonido no existe!!!"
		return
	sound.Volume=volume
	sound.Pitch=pitch
	sound.Position=ent_src.Position
	sound.PlaySound(0)


def InflictDamageFX(VictimName, aura_size_var=250.0, aura_exp_time=0.7, r=10, g=50, b=240, light_intensity=0.0, sound=None, volume=1.0, pitch=1.0):
	victim=Bladex.GetEntity(VictimName)
	x, y, z=victim.Position
	ar=r/255.0
	ag=g/255.0
	ab=b/255.0
	r1=ar+(1.0-ar)/1.5
	g1=ag+(1.0-ag)/1.5
	b1=ab+(1.0-ab)/1.5
	dif=min(ar, ag, ab)
	r2=ar-dif
	g2=ag-dif
	b2=ab-dif
	time=Bladex.GetTime()
	if aura_size_var:
		aura=Auras.MakeAura(VictimName,aura_exp_time,   (1                    , 0.01, 1.0, 0, 0, 1), (), (), (2,  r1, g1, b1, 0.6, 0.3  ,  ar, ag, ab, 0.4, 1.0))
		aura.Data.AddEvent(time+aura_exp_time/4.0   ,   (2.0*aura_size_var/3.0, 1.0 , 1.0, 0, 0, 1), (), (), (2,  r1, g1, b1, 0.6, 0.3  ,  ar, ag, ab, 0.4, 1.0))
		aura.Data.AddEvent(time+aura_exp_time       ,   (aura_size_var        , 0.01, 1.0, 0, 0, 1), (), (), (2,  ar, ag, ab, 0.6, 0.4  ,  r2, g2, b2, 0.4, 0.5))
	if light_intensity:
		id_number=int(10.0*Bladex.GetTime())
		limp=Bladex.CreateEntity(VictimName+"ImpactLight"+`id_number`, "Entity Spot", x, y, z)
		limp.Color=r, g, b
		limp.Intensity=light_intensity
		limp.Precission=0.01
		limp.CastShadows=0
		limp.Visible=0
		limp.Flick=0
		AuxFuncs.SpotIntensityVariation(limp.Name, light_intensity, 0.0, aura_exp_time, 1, 0.0, 0.0, "Timer30", 30)
	if sound:
		sound.Volume=volume
		sound.Pitch=pitch
		sound.Play(x, y, z, 0)
