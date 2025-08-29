##///
##||| DUST.PY TITANIUM
##||| Change list:
##||| * Lava stones now lose selection data, so they can no longer be picked up potentially causing crashes
##\\\ 


#
# Polvo de tierra
#----------------------------
import whrandom
import Bladex
import math
import PhantonFX
import Reference
import Actions
import ObjStore

Bladex.AddParticleGType("Tierrax","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=100
	g=100
	b=100
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*900.0
	Bladex.SetParticleGVal("Tierrax",i,r,g,b,a,size)


def SetTierraColor(r,g,b):
	for i in range(64):
		aux=(64.0-i)/64.0
		a=255.0*(1.0-aux)**0.5
		size=80.0+aux*900.0
		Bladex.SetParticleGVal("Tierrax",i,r,g,b,a,size)


Bladex.AddParticleGType("FastDust","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,16)

for i in range(16):
	aux=(16.0-i)/16.0
	r=50
	g=50
	b=50
	a=255.0*(1.0-aux)**0.5
	size=40.0+aux*450.0
	Bladex.SetParticleGVal("FastDust",i,r,g,b,a,size)


def SetTierrapidaColor(r,g,b):
	for i in range(16):
		aux=(16.0-i)/16.0
		a=255.0*(1.0-aux)**0.5
		size=40.0+aux*450.0
		Bladex.SetParticleGVal("FastDust",i,r,g,b,a,size)


def RemueveTierraGen(x,y,z   ,sx,sz,pps=64,Ptypo="Tierrax",t2l=64,Death=2.0):

	tierra1=Bladex.CreateEntity("TierraRemoviendose1", "Entity Particle System D3", x +sx, y, z + sz)
	tierra1.D1= -2*sx, 0, 0
	tierra1.D2= -2*sx, 0, - 2*sz
	tierra1.ParticleType=Ptypo
	tierra1.PPS=pps
	tierra1.YGravity=200.0
	tierra1.Friction=0.1
	tierra1.Velocity=0.0, -400.0, 0.0
	tierra1.RandomVelocity=15.0
	tierra1.Time2Live=t2l
	if Death !=-1:
		tierra1.DeathTime=Bladex.GetTime()+Death


	tierra2=Bladex.CreateEntity("TierraRemoviendose2", "Entity Particle System D3", x + sx, y, z + sz)
	tierra2.D1= -2*sx, 0, - 2*sz
	tierra2.D2=     0, 0, - 2*sz
	tierra2.ParticleType=Ptypo
	tierra2.PPS=pps
	tierra2.YGravity=200.0
	tierra2.Friction=0.1
	tierra2.Velocity=0.0, -400.0, 0.0
	tierra2.RandomVelocity=15.0
	tierra2.Time2Live=t2l
	if Death !=-1:
		tierra2.DeathTime=Bladex.GetTime()+Death
	return tierra1,tierra2

def DropDust(x,y,z,vx,vy,vz,pps = 64,Ptypo="Tierrax",t2l=64,Death=1.0):
	tierra1=Bladex.CreateEntity("Cristales", "Entity Particle System D1", x, y, z)
	tierra1.ParticleType=Ptypo
	tierra1.PPS=pps
	tierra1.YGravity=9800.0
	tierra1.Friction=0.1
	tierra1.Velocity=vx,vy,vz
	tierra1.RandomVelocity=50.0
	tierra1.Time2Live=t2l
	tierra1.DeathTime=Bladex.GetTime()+Death
	return tierra1



########## Efecto de polvareda casual ##########

Bladex.AddParticleGType("Polvin","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

intensidad = 60

def SetPolvinColor(r,g,b):
	for i in range(68):
		a    = 255*i/64.0
		size = 512*(64-i)/64.0
		if i>64: a =0;size = 0

		Bladex.SetParticleGVal("Polvin",i,r,g,b,a,size)

for i in range(68):
	r=255.0
	g=255.0
	b=255.0
	a    = 255*i/64.0
	size = 512*(64-i)/64.0
	if i>64: a =0;size = 0

	Bladex.SetParticleGVal("Polvin",i,r,g,b,a,size)

# Tierrilla(char.Position[0], char.Position[1], char.Position[2])

def Tierrilla(x, y, z,dx,dz):
	global intensidad

	tierra1=Bladex.CreateEntity("Tierrilla", "Entity Particle System D3", x, y, z)
	tierra1.D1= 3000, 0, 0
	tierra1.D2= 3000, 0, 3000
	tierra1.Time2Live=68
	tierra1.YGravity=-500
	tierra1.Velocity=dx,1000,dz
	tierra1.RandomVelocity=5
	tierra1.ParticleType="Polvin"
	tierra1.PPS = intensidad
	tierra1.DeathTime=Bladex.GetTime()+2.0

class WindFX:
	Variance = 0
	Sector=None
	Sonido=None
	x=0
	y=0
	z=0
	wx=0
	wy=0
	wz=0

	def __init__(self,x,y,z):
		self.Sector = Bladex.GetSector(x,y,z)
		self.Sector.OnEnter = self.EntroElIluso
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
		return(1,
				self.ObjId, # De GameStateAux.PersistentObject
				self.Variance,
				self.Sector,
				self.Sonido,
				self.x,
				self.y,
				self.z,
				self.wx,
				self.wy,
				self.wz
				)


	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Variance=parm[2]
			self.Sector=parm[3]
			self.Sonido=parm[4]
			self.x=parm[5]
			self.y=parm[6]
			self.z=parm[7]
			self.wx=parm[8]
			self.wy=parm[9]
			self.wz=parm[10]
		else:
			print "WindFX.__setstate__() -> Version mismatch"

			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self


	def SetSound(self,sonidox):
		self.Sonido = sonidox

	def SetGenerationPoint(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def SetWindVector(self,x,z):
		self.wx = x
		self.wz = z

	def DropWind(self):
		self.Sonido.Position = self.x, self.y, self.z
		self.Sonido.PlaySound(0)
		Tierrilla(self.x, self.y, self.z,self.wx,self.wz)

	def EntroElIluso(self,Sector,Entity_Name):
		if Entity_Name == "Player1":
			if whrandom.randint(0,self.Variance) == 0:
				self.DropWind()

#------------------------------#------------------------------#------------------------------#------------------------------#

Bladex.AddParticleGType("LavaFire","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,31)

for i in range(32):
	if(i>16):
		aux=0.0
	else:
		aux=(16.0-i)/16.0
	r=255
	g=min(100.0*(1.0-aux*aux)+35,255.0)
	b=min( 50.0*(1.0-aux),255.0)
	a=min(200.0*(1.0-aux),255.0)
	size=130.0+math.sqrt(1.0-aux)*110.0
	Bladex.SetParticleGVal("LavaFire",i,r,g,b,a,size)

D_SPEED=0.05
def ChauPiedruchaTick(obj_name,time):
	global D_SPEED

	pieza = Bladex.GetEntity(obj_name)
	luz   = Bladex.GetEntity(obj_name+"Luz")

	if not pieza:
		return
	else:
		pieza.Alpha = pieza.Alpha-D_SPEED
		luz.Intensity=pieza.Alpha*10
		if luz.Intensity < 1:
			pieza.RemoveFromList("Timer15")
			pieza.SubscribeToList("Pin")


def ChauPiedrucha(obj_name):

	pieza=Bladex.GetEntity(obj_name)
	if not pieza:
		return
	else:
		pieza.SubscribeToList("Timer15")
		pieza.TimerFunc=ChauPiedruchaTick
		pieza=Bladex.GetEntity(obj_name)
		fuego = Bladex.GetEntity(obj_name+"Fuego")
		fuego.DeathTime=Bladex.GetTime()


def DropPiedra(x,y,z,dx=1,dy=1,dz=1,Pname="Piedra_02"):
	Piedra=Bladex.CreateEntity("Piedrita", Pname, x,y,z, "Physic")

	Fuego=Bladex.CreateEntity(Piedra.Name+"Fuego", "Entity Particle System D1", 0,0,0)
	Fuego.ParticleType="LavaFire"
	Fuego.PPS=64
	Fuego.YGravity=1000
	Fuego.Friction=0.1
	Fuego.Velocity=0,0,0
	Fuego.RandomVelocity=30.0
	Fuego.Time2Live=32
	Piedra.Link(Fuego)


	Luz=Bladex.CreateEntity(Piedra.Name+"Luz","Entity Spot",0,0,0)
	Luz.Color=255,100,50
	Luz.Intensity=3
	Luz.CastShadows=0
	Luz.Precission=0.5
	Luz.Visible=0
	Luz.Flick=1
	Piedra.Link(Luz)

	Piedra.Solid = 0
	Piedra.Impulse(dx,dy,dz)
	### Added, stops these things from being pickable up 	-LeadHead
	Reference.EntitiesSelectionData[Piedra.Name]=(0,0,"")

	Piedra.OnStopFunc=ChauPiedrucha

	return Piedra,Fuego,Luz

def BorraPorLasDudas2(PersonName):
	wps=Bladex.GetEntity(PersonName+"WPS")
	if wps:
		wps.SubscribeToList("Pin")

def BorraPorLasDudas(PersonName):
	Bladex.GetEntity(PersonName).CastShadows = 0
	Bladex.AddScheduledFunc(Bladex.GetTime()+5, BorraPorLasDudas2,(PersonName,))

def EnPolvoObjeto(ObjName,dx,dz):
	me= Bladex.GetEntity(ObjName)
	if me:
		wps=Bladex.CreateEntity(ObjName+"WPS", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		wps.ObjectName=ObjName
		wps.ParticleType="EnPolvo"
		wps.Time2Live=64
		wps.RandomVelocity=0
		wps.Velocity=dx,300,dz
		wps.NormalVelocity=2.0
		wps.YGravity=-300
		wps.DeathTime=Bladex.GetTime()+1.5

		wps.PPS=300
		PhantonFX.Delta = 0.1
		PhantonFX.SecAgo = 10
		PhantonFX.DisappearsChar(ObjName,BorraPorLasDudas)

def EnPolvoPerson(PersonName,dx,dz):
	# We don't want the held weapons to disappear....  be sure they are already dropped
	me= Bladex.GetEntity(PersonName)
	object = Bladex.GetEntity(me.InvLeft)
	if me.InvLeft and object and not object.TestHit:
		Actions.RemoveFromInventory (me, object,"DropLeftEvent")
		object.Alpha=1.0
		object.Impulse(0.0, 0.0, 0.0)

	object = Bladex.GetEntity(me.InvRight)
	if me.InvRight and object and not object.TestHit:
		Actions.RemoveFromInventory (me, object,"DropRightEvent")
		object.Alpha=1.0
		object.Impulse(0.0, 0.0, 0.0)

	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="EnPolvo"
	wps.Time2Live=64
	wps.RandomVelocity=0
	wps.Velocity=dx,300,dz
	wps.NormalVelocity=2.0
	wps.YGravity=-300
	wps.DeathTime=Bladex.GetTime()+1.5

	wps.PPS=300
	PhantonFX.Delta = 0.1
	PhantonFX.SecAgo = 10
	PhantonFX.DisappearsChar(PersonName,BorraPorLasDudas)

Bladex.AddParticleGType("EnPolvo","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

for i in range(68):
	r=255.0
	g=255.0
	b=255.0
	a    = 255*i/64.0
	size = 128*(64-i)/64.0+16


	Bladex.SetParticleGVal("EnPolvo",i,r,g,b,a,size)

"""
import dust
import whrandom

def DropPiedrita():
	r=whrandom.randint(-4000,4000)
	dust.DropPiedra(5843+r, 8893, 48670,-r*15,-140000,whrandom.randint(-6000,6000))



dust.DropPiedra(5647, 8882, 47433,30000,-140000,0)
dust.DropPiedra(5647, 8882, 47433,-30000,-140000,0)
dust.DropPiedra(5647, 8882, 47433,30000,-140000,20000)
dust.DropPiedra(5647, 8882, 47433,-30000,-140000,20000)
dust.DropPiedra(5647, 8882, 47433,-30000,-140000,-20000)
dust.DropPiedra(5647, 8882, 47433,30000,-140000,-20000)

Bladex.SetCallCheck(1)


------------------------------------------------------------------

import dust
import Sounds

dust.intensidad = 240                           # pps
dust.SetPolvinColor(255,255,255)                # snow winds

WindSound = Sounds.CreateEntitySound("../../Sounds/M-caida-nieve1.wav", "CasualWind")

Efepolvo = dust.WindFX(-18272, 727, 30667)      # sector as params
Efepolvo.SetSound(WindSound)                    # coolsound
Efepolvo.SetGenerationPoint(-22836,300, 31593)  # Start
Efepolvo.SetWindVector(1000,1000)               # This way is the win
Efepolvo.Variance = 0                           # Allways

------------------------------------------------------------------
"""