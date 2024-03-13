##///
##||| GEMS.PY TITANIUM
##||| Change list:
##||| * EffectoConcentracion now uses a 60 FPS animation. Frames and Decon get multiplied by 2 
##|||   so as not to need to adjust every map script which calls it. Should work with custom maps.
##\\\ 


import Bladex
import AuxFuncs
import whrandom
import Reference
import math

#########################################################
###############  EFECTO DE CONCENTRACION  ###############
#########################################################
MaximunAlpha = 0.15

def ConcentraTimer(e_name, time):
	global MaximunAlpha
	o = Bladex.GetEntity(e_name)
	o.Data.Counter = o.Data.Counter + 1

	o.Scale = o.Data.Scale*(o.Data.Frames - o.Data.Counter)/o.Data.Frames + 1.0

	if o.Data.Counter > o.Data.Decon:
		o.Alpha = MaximunAlpha-(MaximunAlpha*(o.Data.Counter-o.Data.Decon))/(o.Data.Frames-o.Data.Decon)
	else:
		o.Alpha = MaximunAlpha*o.Data.Counter/o.Data.Frames

	o.Rotate(o.Data.x, o.Data.y, o.Data.z, o.Data.delta)
	if o.Data.Counter+1 > o.Data.Frames :
		# o.RemoveFromList("Timer30")   # 60fps animation
		o.RemoveFromList("Timer60")     #       -LeadHead
		o.SubscribeToList("Pin")

def EfectoConcentracion(pos,name,frames=150,Scale = 30.0,RotSpeed = 32.0,Decon=100):
	global ActualColor
	class vacio:
		pass

	frames = frames * 2         # Added for 60fps
	# RotSpeed = RotSpeed * 2   #
	Decon = Decon * 2           #   -LeadHead

	if ActualColor == GREEN_GEM:
		o=Bladex.CreateEntity(name,"EsferaGemaVerde", 0,0 ,0)
	if ActualColor == RED_GEM:
		o=Bladex.CreateEntity(name,"EsferaGemaRoja",  0,0 ,0)
	if ActualColor == BLUE_GEM:
		o=Bladex.CreateEntity(name,"EsferaGemaAzul",  0, 0,0)

	o.Static      = 1
	o.Orientation = 0.707107,0.707107,0.000000,0.000000
	o.Position    = pos
	o.SelfIlum    = 1
	o.CastShadows = 0
	o.RasterMode  ="AdditiveAlpha"
	o.RasterMode  ="Read"
	o.Alpha       = 0.0
	o.Scale       = 6.0
	o.TimerFunc   = ConcentraTimer
	# o.SubscribeToList("Timer30")    # 60fps animation
	o.SubscribeToList("Timer60")      #       -LeadHead
	o.Data        = vacio()
	x             = whrandom.random()
	y             = whrandom.random()
	z             = whrandom.random()
	tot           = x*x + y*y + z*z
	x             = math.sqrt(x*x/tot)
	y             = math.sqrt(y*y/tot)
	z             = math.sqrt(z*z/tot)

	if whrandom.random() >0.5:
		o.Data.x      = +x
	else:
		o.Data.x      = -x

	if whrandom.random() >0.5:
		o.Data.y      = +y
	else:
		o.Data.y      = -y

	if whrandom.random() >0.5:
		o.Data.z      = +z
	else:
		o.Data.z      = -z

	o.Data.delta   = (whrandom.random()+0.5)/RotSpeed
	o.Data.Counter = 0
	o.Data.Frames  = frames
	o.Data.Scale   = Scale
	o.Data.Decon   = Decon


	#print o.Data.x,o.Data.y,o.Data.z,o.Data.delta
	return o



Bladex.AddParticleGType("GemaConc","SmokeParticle",Reference.B_PARTICLE_GTYPE_ADD,64)

for i in range(64):
	aux = 1.0-i/64.0
	r=10
	g=205
	b=150
	a=aux*128.0
	size=aux*128+64
	Bladex.SetParticleGVal("GemaConc",i,r,g,b,a,size)

Bladex.AddParticleGType("Particulate","Estrellita",1,32)

for i in range(32):

	a = i*4

	r=128.0
	g=255.0
	b=128.0
	size= (i%8)*6
	Bladex.SetParticleGVal("Particulate",i,r,g,b,a,size)


def PiecesOfGema(pos):
	RayoHit=Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D1", pos[0],pos[1],pos[2])
	RayoHit.Time2Live=32
	RayoHit.YGravity=20000
	RayoHit.ParticleType="Particulate"
	RayoHit.Friction=0.95
	RayoHit.Velocity=0,0,0
	RayoHit.RandomVelocity=-5
	RayoHit.DeathTime     = Bladex.GetTime()+1.0

GREEN_GEM = 0
RED_GEM   = 1
BLUE_GEM  = 2

ActualColor = GREEN_GEM

def SetGemColor(color):
	global ActualColor
	ActualColor = color

	if ActualColor==GREEN_GEM:
		r = 10
		g = 205
		b = 150
	if ActualColor==RED_GEM:
		r = 205
		g = 150
		b = 10
	if ActualColor==BLUE_GEM:
		r = 10
		g = 100
		b = 205

	for i in range(64):
		aux = 1.0-i/64.0
		a=aux*128.0
		size=aux*128+64
		Bladex.SetParticleGVal("GemaConc",i,r,g,b,a,size)


	#########################################################
	if ActualColor==GREEN_GEM:
		r = 128.0
		g = 255.0
		b = 128.0
	if ActualColor==RED_GEM:
		r = 255.0
		g = 128.0
		b = 128.0
	if ActualColor==BLUE_GEM:
		r = 128.0
		g = 128.0
		b = 255.0

	for i in range(32):
		a = i*4
		size= (i%8)*6
		Bladex.SetParticleGVal("Particulate",i,r,g,b,a,size)

def ConcentratorParticulate(pos,delta=(0,0,0)):

	RayoHit=Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D1", pos[0],pos[1],pos[2])
	RayoHit.ParticleType="GemaConc"
	RayoHit.Time2Live=64
	RayoHit.YGravity=0.0
	RayoHit.Friction=0
	RayoHit.PPS=255
	RayoHit.Velocity=delta
	RayoHit.RandomVelocity=-10
	RayoHit.DeathTime     = Bladex.GetTime()+4.0

GemCallBack = None
GemParams   = ()

def FlashGem():
	if ActualColor==GREEN_GEM:
		AuxFuncs.FadeFrom(0.15,0.0,128,255,128)
	if ActualColor==RED_GEM:
		AuxFuncs.FadeFrom(0.15,0.0,255,128,128)
	if ActualColor==BLUE_GEM:
		AuxFuncs.FadeFrom(0.15,0.0,128,128,255)

	if GemCallBack != None:
		apply(GemCallBack,GemParams)

def FaderUp():
	global ABC_POS

	_SndConcentGem.Volume = _SndConcentGem.Volume+1.0/60.0
	if _SndConcentGem.Volume >= 0.95:
		_SndConcentGem.Stop()
		_SndConcentGemHit.Play(ABC_POS[0],ABC_POS[1],ABC_POS[2],0)
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1,  FaderUp,())

def Concentrator(pos,delta=(0,0,0)):
	global ABC_POS

	_SndConcentGem.Play(pos[0],pos[1],pos[2],-1)
	_SndConcentGem.Volume = 0
	ABC_POS = pos
	FaderUp()


	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,  EfectoConcentracion,(pos,"C1gema1a",))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,  EfectoConcentracion,(pos,"C2gema1a",))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,  EfectoConcentracion,(pos,"C3gema1a",))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.95, PiecesOfGema,(pos,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,  FlashGem,())
	ConcentratorParticulate(pos,delta)


_SndConcentGem=Bladex.CreateSound("../../Sounds/energy-ball.wav","SndConcentGem")
_SndConcentGem.MinDistance=10000.0
_SndConcentGem.MaxDistance=100000.0

_SndConcentGemHit=Bladex.CreateSound("../../Sounds/energy-ball-impact.wav","SndConcentGemHit")
_SndConcentGemHit.MinDistance=10000.0
_SndConcentGemHit.MaxDistance=100000.0


o=Bladex.CreateEntity("e1","EsferaGemaVerde", 0,0 ,0)
o.SubscribeToList("Pin")
o=Bladex.CreateEntity("e2","EsferaGemaRoja",  0,0 ,0)
o.SubscribeToList("Pin")
o=Bladex.CreateEntity("e3","EsferaGemaAzul",  0, 0,0)
o.SubscribeToList("Pin")
