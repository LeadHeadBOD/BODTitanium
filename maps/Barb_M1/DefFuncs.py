##///
##||| BARB_M1/DEFFUNCS.PY TITANIUM
##||| Change list:
##||| * Environmental animations should now be played at 60fps
##||| * Final cutscene can be skipped now.
##||| * Doors broken by liches now are better synced with their attack animation.
##||| * Changed sound events for totem cutscene.
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 


import def_class
import Bladex
import ReadGSFile
import Enm_Gen
import B3DLib
import Traps_C
import GameText
import AuxFuncs
import Scorer
import Sounds
import EnmGenRnd
import ReadGSFile
import Actions
import Reference
import Sounds
import stone
import heavyObjects
import Button
import GotoMapVars
import ScriptSkip
import Raster
import ExtraData
import MusicTool
import darfuncs

B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3


#Bladex.LoadSampledAnimation("../../Anm/Totem2.BMV","Totem2",1,"Totem2")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Gentrampa.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CBgeneradorT1(enem):
	pass

def CBgeneradorT2(enem):
	enem.ActionAreaMin=pow(2,0)
	enem.ActionAreaMax=pow(2,1)

def CBgeneradorT3(enem):
	enem.ActionAreaMin=pow(2,8)
	enem.ActionAreaMax=pow(2,2)

def CBgeneradorT4(enem):
	enem.ActionAreaMin=pow(2,9)
	enem.ActionAreaMax=pow(2,9)

def CBgeneradorT5(enem):
	enem.ActionAreaMin=pow(2,9)
	enem.ActionAreaMax=pow(2,9)

def ActivateEnemiesMonolito():
	EnmGenRnd.ActivateEnemy(monolitoenm1)
	EnmGenRnd.ActivateEnemy(monolitoenm2)
	EnmGenRnd.ActivateEnemy(monolitoenm3)
	EnmGenRnd.ActivateEnemy(monolitoenm4)
	monolitoenm1.SetOnFloor()
	monolitoenm2.SetOnFloor()
	monolitoenm3.SetOnFloor()
	monolitoenm4.SetOnFloor()

def StopGenCamera(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Bladex.SetListenerPosition(1)
	Scorer.SetVisible(1)


def Abrepta():
	ptatrampa.OpenDoor()
	ptatrampa2.OpenDoor()

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("generador_Camera01.cam",0,-1)
	cam.AddCameraEvent(-1,StopGenCamera)
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("ABREPTAFINAL") )

	ActivateEnemiesMonolito()

	Bladex.SetListenerPosition(2)


def Cierrapta():
	ptatrampa.CloseDoor()


####### PUERTA TRAMPA DE LAS TUMBAS   ###########

def LineaPolvoGen():
	polvo=Bladex.CreateEntity("PolvoGen", "Entity Particle System D2", 157625,-49000,159750)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 2500,0,625
	polvo.ParticleType="Tierra2"
	polvo.YGravity=-100.0
	polvo.Friction=0.2
	polvo.PPS=500
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def Abrepta2():
	ptatrampa2.OpenDoor()


def Cierrapta2():
	ptatrampa2.CloseDoor()


def Abrepta3(EnmGen):
	print "Abriendo"
	ptatrampa3.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def Cierrapta3():
	ptatrampa3.CloseDoor()


######################
#     Particulas     #
######################


def CreateArenilla(r = 55,g= 43,b = 13,al = 128,type = B_PARTICLE_GTYPE_BLEND):
	Bladex.AddParticleGType("Tierra2","SmokeParticle",type,64)

	for i in range(64):
		aux=(64.0-i)/64.0
		r=r
		g=g
		b=b
		if i < 50:
			a=al + (al*(1.0-aux)**0.5)
		else:
			a=al*(1.0-aux)**0.5
		size=80.0+aux*400.0
		Bladex.SetParticleGVal("Tierra2",i,r,g,b,a,size)

###################################################
#     Funciones complementarias del generador     #
###################################################

def RemueveTierraGen(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-900.0, pos[2]+v1[2])
	tierra.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	tierra.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	tierra.ParticleType="Tierra2"
	tierra.PPS=64
	tierra.YGravity=200.0
	tierra.Friction=0.1
	tierra.Velocity=0.0, -400.0, 0.0
	tierra.RandomVelocity=15.0
	tierra.Time2Live=64
	tierra.DeathTime=Bladex.GetTime()+2.0



def SaltaTierraGen(enmgen):
#def SaltaTierraGen():

	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position
	#pos=generadorT1.Points[0].Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)

	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltatie.ParticleType="Tierra3"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0

	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltati2.ParticleType="Tierra2"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3),"RemueveTierraGen")


#######################
#     Generadores     #
#######################

def ActivateTrampaTumbaCircular(TrSector,Entity):
	if Entity == "Player1":
		generadorT2.GenerateEnemy()
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")


def ActivateTrampaTumba(TrSector,Entity):
	if Entity == "Player1":
		ptatrampa2.CloseDoor()
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("TRAMPA") )
		Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,generadorT1.GenerateEnemy,(),"GenerateEnemy")
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")


def ActivateGen3(Sector,Entity):
	if Entity == "Player1":
		generadorT3.GenerateEnemy()
		SecGen3.OnEnter = ""

def ActivateGen4(Sector,Entity):
	if Entity == "Player1":
		generadorT4.GenerateEnemy()
		SecGen4.OnEnter = ""

def ActivateGen5(Sector,Entity):
	if Entity == "Player1":
		generadorT5.GenerateEnemy()
		SecGen5.OnEnter = ""

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Generadores.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


###################################################
#     Funciones complementarias del generador     #
###################################################

def RemueveTierraGen(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-900.0, pos[2]+v1[2])
	tierra.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	tierra.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	tierra.ParticleType="Tierra2"
	tierra.PPS=64
	tierra.YGravity=200.0
	tierra.Friction=0.1
	tierra.Velocity=0.0, -400.0, 0.0
	tierra.RandomVelocity=15.0
	tierra.Time2Live=64
	tierra.DeathTime=Bladex.GetTime()+2.0

def SaltaTierraGen(enmgen):
	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)
	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltatie.ParticleType="Tierra3"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0
	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltati2.ParticleType="Tierra2"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3),"RemueveTierraGen")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para FinalScene.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************



def FadeOutSpirits(entity,time):
	global particle
	global avanceparticle

	npart= "Spirit" + `particle`

	if (particle < 10):
		avanceparticle = avanceparticle + 1

		if (avanceparticle > 6):
			particle = particle + 1
		 	avanceparticle = 0

		for i in range(6):
			spirit=Bladex.GetEntity("Spirit" + `i`)
			spirit.ParticleType=npart
			spirit.YGravity=spirit.YGravity-700
	else:
		s = Bladex.GetEntity(entity)
		s.RemoveFromList("Timer60")
		AuxFuncs.FadeTo(6,20)

#def ActivateFadeSpirits(Camera,Frame):
def ActivateFadeSpirits():
	spirit=Bladex.GetEntity("Spirit1")
	spirit.SubscribeToList("Timer60")
	spirit.TimerFunc = FadeOutSpirits


def MoveSpirits(entity,time):
	time = Bladex.GetTime()
	spirittime = time - startspirittime
	#print (spirittime)

	for i in range(6):
		pos = Traps_C.GetMaxPathPosition(ExtraData.camspirit[i],spirittime)
		spirit=Bladex.GetEntity("Spirit" + `i`)
		spirit.Position = pos

def ActivateSpirits():
	global startspirittime

	startspirittime = Bladex.GetTime()

	spirit=Bladex.GetEntity("Spirit0")
	spirit.SubscribeToList("Timer60")
	spirit.TimerFunc = MoveSpirits

def CreateAllSpirits():
	global Created
	for i in range(6):
		ExtraData.camspirit.append(Traps_C.LoadMaxPath("espiritus_Particula"+`i+1`+".cam",0,-1))

		spirit=Bladex.CreateEntity("Spirit" + `i`, "Entity Particle System D1",0,0,0)
		spirit.ParticleType="Spirit0"
		spirit.YGravity=-1200
		spirit.Friction=0.12
		spirit.PPS=60
		spirit.Velocity=0,-10000,0
		spirit.RandomVelocity=15
		spirit.Time2Live=8

def StopSpirits(Camera,Frame):
	spirit=Bladex.GetEntity("Spirit0")
	spirit.RemoveFromList("Timer60")
	spirit.TimerFunc = ""
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()          # Added     -LeadHead
	
	time = 0
	if Reference.DEMO_MODE==0:
		Bladex.AddScheduledFunc(Bladex.GetTime()+time,GotoMapVars.EndOfLevel,(),"GotoMapVars.EndOfLevel")
		GotoMapVars.MapText(1,"D_M1_T2")
	else:
		AuxFuncs.setDemoBg(time)

def StartFadeOutSpirits(Camera,Frame):
	AuxFuncs.FadeTo(1.5, 100)

def StopCameraTumba(Camera,Frame):
	#print ("Iniciando")
	char.Position = 111347,-55272,196303

	char.Wuea  = Reference.WUEA_ENDED
	char.Angle = 3.1415
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnimation("Bar_espiritus")
	char.SetOnFloor()
	#print("Animando")

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("espiritus_Camara_personaje.cam",0,-1)
	cam.AddCameraEvent(700-35,StartFadeOutSpirits)
	cam.AddCameraEvent(-1,StopSpirits)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 30,ActivateFadeSpirits,(),"ActivateFadeSpirits")

	ActivateSpirits()

def musicaytexto():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("final") )
	GameText.WriteText("M1T2")


def StartScene(trsector, ent_name):
	global startspirittime



	#player.Load("../../Sounds/")

	if (startspirittime == 0):
		cam = Bladex.GetEntity("Camera")
		Scorer.SetVisible(0)

		cam.SetMaxCamera("espiritus_Camera_tumba.cam",0,10)             # PLAGUE: Why do this nonsense?
		cam.AddCameraEvent(10,StopCameraTumba)
		CreateAllSpirits()

		time = Bladex.GetTime()

		Bladex.AddScheduledFunc(time + 1.0,musicaytexto,(),"musicaytexto")
		# Bladex.DeactivateInput()                      #
		ScriptSkip.SkipScriptStart("Barb_M1 final")     # Added -LeadHead


	startspirittime = Bladex.GetTime()

	"""
	else:
		for i in range(6):
			spirit=Bladex.GetEntity("Spirit" + `i`)
			spirit.ParticleType="Spirit0"
	"""


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para derr.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def polvoTri(a,b,c,name):
	dust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2] )
	dust.D1= b[0]-a[0] ,b[1]-a[1] ,b[2]-a[2]
	dust.D2= c[0]-a[0] ,c[1]-a[1] ,c[2]-a[2]
	dust.ParticleType="MediumDust"
	dust.YGravity=30.0
	dust.Friction=0.2
	dust.PPS=812
	dust.Velocity=0.0, -410.0, 0.0
	dust.RandomVelocity=40.0
	dust.Time2Live=13
	dust.DeathTime=Bladex.GetTime()+40.0/60.0

def polvoDelDerrumbamiento():
	p0 = -169000,-15100,218700
	p1 = -170000,-15100,211000
	p2 = -161000,-15100,208000
	p3 = -159000,-15100,214000

	polvoTri(p0,p1,p2,"dustA")
	polvoTri(p1,p2,p3,"dustB")

def Cont2Derr():
	derr1.DoBreak((0, -2, 0), (-166000,-14900,215500), (0.0, 0.0, 0.0))
	derr2.DoBreak((0,  1, 0), (-166000,-14900,213000), (0.0, 0.0, 0.0))
	derr3.DoBreak((0,  1, 0), (-168000,-14900,212500), (0.0, 0.0, 0.0))
	derr4.DoBreak((0, -2, 0), (-162500,-14900,213200), (0.0, 0.0, 0.0))
	polvoDelDerrumbamiento()

def ContDerr():
	derrumbesuelopiedra.Play(-165000,-15900,213000)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, Cont2Derr, (),"Cont2Derr")

def Derrumba(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderr.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ContDerr, (),"ContDerr")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Crows1.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def EspantarCuervo1():
	crow1.ClearPath();
	crow1.Animation="Crw_fly"
	crow1.FPS=60.0      # Was 20.0 -LeadHead
	crow1.AddPathNode(5.0,-84000,-5000,-114000);
	crow1.AddPathNode(5.0,-102000,-4000,-103000);
	crow1.AddPathNode(7.0,-122000,-5000,-101000);
	crow1.AddPathNode(5.0,-141000,-6000,-97000);
	crow1.AddPathNode(10.0,-172000,-8000,-70000);
	crow1.AddPathNode(5.0,-191000,-10000,-70000);
	crow1.AddPathNode(5.0,-206000,-10000,-84000);
	crow1.AddPathNode(5.0,-200000,-9000,-105000);
	crow1.AddPathNode(5.0,-181000,-8000,-112000);
	crow1.AddPathNode(5.0,-143000,-6000,-121000);
	crow1.AddPathNode(5.0,-106000,-5000,-139000);
	crow1.AddPathNode(5.0,-87000,-5000,-132000);
	crow1.GoToPath(0,2);

def EspantarCuervo2():
	crow2.ClearPath();
	crow2.Animation="Crw_fly"
	crow2.FPS=60.0      # Was 20.0 -LeadHead
	crow2.AddPathNode(5.0,-126000,-21000,64000);
	crow2.AddPathNode(5.0,-144000,-22000,51000);
	crow2.AddPathNode(7.0,-162000,-24000,56000);
	crow2.AddPathNode(5.0,-182000,-26000,92000);
	crow2.AddPathNode(10.0,-209000,-24000,121000);
	crow2.AddPathNode(5.0,-203000,-26000,141000);
	crow2.AddPathNode(5.0,-187000,-28000,154000);
	crow2.AddPathNode(5.0,-167000,-31000,156000);
	crow2.AddPathNode(5.0,-147000,-35000,146000);
	crow2.AddPathNode(5.0,-135000,-30000,130000);
	crow2.AddPathNode(5.0,-127000,-25000,110000);
	crow2.AddPathNode(5.0,-118000,-20000,89000);
	crow2.GoToPath(0,2);

def EspantarCuervo3():
	crow3.ClearPath();
	crow3.Animation="Crw_fly"
	crow3.FPS=60.0      # Was 20.0 -LeadHead
	crow3.AddPathNode(5.0,-128000,-24000,101000);
	crow3.AddPathNode(5.0,-146000,-24000,110000);
	crow3.AddPathNode(4.0,-166000,-22000,112000);
	crow3.AddPathNode(5.0,-185000,-23000,107000);
	crow3.AddPathNode(5.0,-188000,-24000,87000);
	crow3.AddPathNode(5.0,-179000,-26000,70000);
	crow3.AddPathNode(5.0,-161000,-24000,57000);
	crow3.AddPathNode(5.0,-142000,-22000,56000);
	crow3.AddPathNode(5.0,-124000,-20000,64000);
	crow3.AddPathNode(5.0,-116000,-20000,85000);
	crow3.GoToPath(0,2);

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Cascadapint.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateCascada(Cascada,p,d,v,pc,Time = 16,Grav = 13000,PPS = 600):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaCpi"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	espuma=Bladex.CreateEntity(Cascada+"Espumapi", "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espumapi"
	espuma.PPS=50
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")

	espuma = Bladex.GetEntity(cascada+"Espumapi")
	espuma.SubscribeToList("Pin")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Cascadaint.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateCascada(Cascada,p,d,v,pc,Time = 16,Grav = 13000,PPS = 500):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaCi"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	espuma=Bladex.CreateEntity(Cascada+"Espumai", "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espumai"
	espuma.PPS=50
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")

	espuma = Bladex.GetEntity(cascada+"Espumai")
	espuma.SubscribeToList("Pin")



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Casca.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def CreateCascada(Cascada,p,d,v,pc,Time = 16,Grav = 13000,PPS = 600):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaC"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	espuma=Bladex.CreateEntity(Cascada+"Espuma", "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espuma"
	espuma.PPS=50
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")

	espuma = Bladex.GetEntity(cascada+"Espuma")
	espuma.SubscribeToList("Pin")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para BreakDoors.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

"""
# Following funcs have been edited:
# - Introduced a 1.1s delay before door breaks to better sync with Lich animations
# - Liches made deaf and blind so they don't try to lock on to you through walls
#           -LeadHead
"""

def LichBreakDoor(TrSector,Entity):
	if Entity == "Player1":
		# b2.HitSector(0,"",b2.pos[0],b2.pos[1],b2.pos[2])
		# b3.HitSector(0,"",b3.pos[0],b3.pos[1],b3.pos[2])
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")
		doorenm1 = Bladex.GetEntity("doorenm1")
		doorenm1.Angle = 4.6
		doorenm1.LaunchAnmType("g_12")
		doorenm1.Deaf=0
		doorenm1.Blind=0
		doorenm1.SetActiveEnemy("Player1")
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.1, ShatterDoor1, (),"Shatteroor1")
		
def ShatterDoor1():
	b2.HitSector(0,"",b2.pos[0],b2.pos[1],b2.pos[2])
	b3.HitSector(0,"",b3.pos[0],b3.pos[1],b3.pos[2])
		


def LichBreakDoor2(TrSector,Entity):
	if Entity == "Player1":
		# b5.HitSector(0,"",b5.pos[0],b5.pos[1],b5.pos[2])
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")
		doorenm2 = Bladex.GetEntity("doorenm2")
		doorenm2.Angle = 1.6
		doorenm2.LaunchAnmType("g_12")
		doorenm2.Deaf=0
		doorenm2.Blind=0
		doorenm2.SetActiveEnemy("Player1")
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.1, ShatterDoor2, (),"Shatteroor2")
		
def ShatterDoor2():
		b5.HitSector(0,"",b5.pos[0],b5.pos[1],b5.pos[2])


def SetupBreakSector(pos,pos2,norm,life,dir,dir1,dir2):
	BreakS = def_class.BreakSector()
	BreakS.InitBreak(pos,pos2,norm,life,dir,dir1,dir2)

	return BreakS

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Bolas.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

# ---- funciones de activacion de las bolas

def ActivarBola1(SectorIndex,EntityName):
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa1b") )
	Raster.SetDomeColor(255,195,155)
	global bola_activada
	if (EntityName == "Player1"):
		sbol1.OnEnter= ""
		bola_activada = 1
		stone.drop( "bola1", fuerza_bola1,0,0 )

def ActivarBola2(SectorIndex,EntityName):
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa1b") )
	global bola_activada

	if (EntityName == "Player1"):
		sbol2.OnEnter= ""
		bola_activada = 1
		stone.drop( "bola2", 0,0,fuerza_bola2 )


# ---- funciones de rotura del puente

def Break():
	sderp1.DoBreak((0.0, 10.0, 0), (-28750,-30700,170000), (0.0, 0.0, 0.0))
	sderp2.DoBreak((0.0, 10.0, 0), (-26250,-30700,170000), (0.0, 0.0, 0.0))
	sderp3.DoBreak((0.0, 10.0, 0), (-27250,-30700,175000), (0.0, 0.0, 0.0))

def RomperPuente(SectorIndex,EntityName):
	global puente_break
	if (bola_activada and (EntityName=="bola1" or EntityName=="bola2" or EntityName=="Player1")) :
		puente.OnEnter=RomperPuente=""
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,Break,(),"Break")
		ent = Bladex.GetEntity(EntityName)
		SonidoDerrumbamiento.Position = ent.Position
		SonidoDerrumbamiento.PlaySound(0)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampin.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DeactivatePinchoOnHit (EntityName, VictimName, ImpX, ImpY, ImpZ):
	# Deactivate pincho
	pincho = Bladex.GetEntity(EntityName)
	pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
	pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)


def ActivatePinchos():
	for i in range(1,23):
		# Activate pincho
		# print "Pinchos1_"+`i`     # PLAGUE: stop spamming the console ffs
		pincho=Bladex.GetEntity("Pinchos1_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,1,0)
		pincho.InflictHitFunc= DeactivatePinchoOnHit

def DeactivatePinchos():
	for i in range(1,23):
		# Activate pincho
		pincho=Bladex.GetEntity("Pinchos1_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_Pinchos.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def SubirTecho():
	sld_area = Techo_Pinchos.sld_area()
	sld_area.OnStopFunc = TrampaSubida
	sld_area.SlideTo(0,-100,-200)

def TrampaSubida(sld_name):
	if (TrampaEstado == 1):
		LinkCeil.Link()
		TechoTramo1()
	else:
		SonidoClack2.Position = -48000,-30000,177000
		SonidoClack2.PlaySound(0)

		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,Puerta_Pinchos2.OpenDoor,(),"Puerta_Pinchos2.OpenDoor")
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,MusicTool.LaunchMusicEvent,("empty",),"ExeMusicEvent")
		arenilla1.DeathTime=Bladex.GetTime()
		arenilla2.DeathTime=Bladex.GetTime()
		arenilla3.DeathTime=Bladex.GetTime()
		arenilla4.DeathTime=Bladex.GetTime()

		Techo_sound.StopSound()

		LinkCeil.UnLink()

def TrampaBajada(sld_name):
	#SubirTecho()
	Doors.DoorHit(0,"Player1",0,0,0,0,0,0,0,0,0,0,0,0)

def LineaPolvo2():
	polvo=Bladex.CreateEntity("Polvo2", "Entity Particle System D2", -49200,-28250,182625)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 2600,0,0
	polvo.ParticleType="DustDoor"
	polvo.YGravity=-700.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def LineaPolvo1():
	polvo=Bladex.CreateEntity("Polvo1", "Entity Particle System D2", -49200,-28250,172000)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 2600,0,0
	polvo.ParticleType="DustDoor"
	polvo.YGravity=-700.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.Time2Live = 50
	polvo.RandomVelocity=25.0
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def TechoTramo2(sld_name):
	sld_area = Techo_Pinchos.sld_area()
	sld_area.OnStopFunc = TrampaBajada
	sld_area.SlideTo(6100,10,14000)

def TechoTramo1():
	sld_area = Techo_Pinchos.sld_area()
	sld_area.OnStopFunc = TechoTramo2
	sld_area.SlideTo(1500,1,5)

def DesactivarTrampaPinchos():
	global TrampaEstado
	TrampaEstado = 0

	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.5,Clack1,(),"Clack1")
	sld_area = Techo_Pinchos.sld_area()
	sld_area.OnStopFunc = ""
	sld_area.SlideTo(sld_area.Displacement,-3000,-3000)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.5,SubirTecho,(),"SubirTecho")

def LaunchSand():
	global arenilla1
	global arenilla2
	global arenilla3
	global arenilla4

	arenilla1=Bladex.CreateEntity("Arenilla1", "Entity Particle System D2", -50500,-36000,182500)
	arenilla1.D=5500, 0, 0
	arenilla1.ParticleType="DarkSand"
	arenilla1.YGravity=10000.0
	arenilla1.Friction=0.2
	arenilla1.RandomVelocity=10.0
	arenilla1.PPS=100
	arenilla1.Time2Live=64
	#arenilla1.DeathTime=Bladex.GetTime()+2.5

	arenilla2=Bladex.CreateEntity("Arenilla2", "Entity Particle System D2", -50500,-36000,172500)
	arenilla2.D=5500, 0, 0
	arenilla2.ParticleType="DarkSand"
	arenilla2.YGravity=10000.0
	arenilla2.Friction=0.2
	arenilla2.RandomVelocity=10.0
	arenilla2.PPS=100
	arenilla2.Time2Live=64
	#arenilla2.DeathTime=Bladex.GetTime()+2.5

	arenilla3=Bladex.CreateEntity("Arenilla3", "Entity Particle System D2", -50500,-36000,182500)
	arenilla3.D=0, 0, -10000
	arenilla3.ParticleType="DarkSand"
	arenilla3.YGravity=10000.0
	arenilla3.Friction=0.2
	arenilla3.RandomVelocity=10.0
	arenilla3.PPS=200
	arenilla3.Time2Live=64
	#arenilla1.DeathTime=Bladex.GetTime()+2.5

	arenilla4=Bladex.CreateEntity("Arenilla4", "Entity Particle System D2", -45100,-36000,182500)
	arenilla4.D=0, 0, -10000
	arenilla4.ParticleType="DarkSand"
	arenilla4.YGravity=10000.0
	arenilla4.Friction=0.2
	arenilla4.RandomVelocity=10.0
	arenilla4.PPS=200
	arenilla4.Time2Live=64
	#arenilla1.DeathTime=Bladex.GetTime()+2.5

def ActivarTecho():
	global LinkCeil
	global TrampaEstado

	if (TrampaEstado == 1):
		Techo_sound.Position = -48000,-36000,177000
		Techo_sound.PlaySound(-1)

		cam = Bladex.GetEntity("Camera")
		cam.SetPersonView("Player1")
		cam.Cut()
		Bladex.ActivateInput()
		Scorer.SetVisible(1)

		LinkCeil = def_class.PinLinkCeil("TechoPinchos","Pinchos3_",1,18,-35000,arenilla1,arenilla2,arenilla3,arenilla4,Techo_sound)
		LinkCeil.Link()
		TechoTramo1()

def FinBoom(sld):
	sld_area = Techo_Pinchos.sld_area()
	sld_area.SlideTo(200,-3000,-3000)
	sld_area.OnStopFunc = ""

def BoomActivacion():
	SonidoClack2.Position = -48000,-30000,177000
	SonidoClack2.PlaySound(0)

	sld_area = Techo_Pinchos.sld_area()
	sld_area.SlideTo(250,3000,3000)
	sld_area.OnStopFunc = FinBoom

	LaunchSand()

def DetieneCamara(entity_name, camera_element, node):
	cam = Bladex.GetEntity("Camera")
	cam.SetTravellingView(2,0)

def MoveTarget(entity,time):
	global AngX
	global VelAng
	cam = Bladex.GetEntity("Camera")
	AngX = AngX + VelAng
	VelAng = VelAng  - 0.0002

	cam.TAng = AngX,2.72,0

	if AngX >= 0.8:
		ent = Bladex.GetEntity(entity)
		ent.RemoveFromList("Timer60")
		BoomActivacion()

def MirarTecho():
	global AngX
	global VelAng

	cam = Bladex.GetEntity("Camera")

	char.Position = -47588.2312422, -29256.5266915, 174148.454479
	cam.Position = -45458,-29069,181788
	char.TimerFunc = MoveTarget
	char.SubscribeToList("Timer60")
	AngX = 0.1
	VelAng = 0.018

	cam.TAng = 0.1,2.72,0
	cam.SType = 0
	cam.TType = 3

def Clack1():
	char = Bladex.GetEntity("Player1")
	#SonidoClack.Position = -48000,-30000,177000
	SonidoClack.Position = char.Position
	SonidoClack.PlaySound(0)

def ActivarTrampaPinchos():
	global TrampaPuerta_Abandonada

	if (TrampaEstado==1):
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.7,Puerta_Pinchos1.CloseDoor,(),"Puerta_Pinchos1.CloseDoor")
		Puerta_Pinchos2.CloseDoor()
		char = Bladex.GetEntity("Player1")
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)
		char.LaunchAnmType("wlk_1h")
		char.Angle = 0
		char.Position = -47554.1528572, -28598.4429382, 172689.325103
		char.SetOnFloor()

		time = Bladex.GetTime()
		cam = Bladex.GetEntity("Camera")
		cam.Position = -45458,-29069,181788
		cam.TPos = -49306,-30000,173207
		cam.SetTravellingView(0,0)

		Bladex.DeactivateInput()
		Scorer.SetVisible(0)

		Bladex.AddScheduledFunc(time + 1.0,Clack1,(),"Clack1")
		Bladex.AddScheduledFunc(time + 1.5,MirarTecho,(),"MirarTecho")
		Bladex.AddScheduledFunc(time + 4.0,ActivarTecho,(),"ActivarTecho")
		TrampaPuerta_Abandonada = 0
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("trampapin") )

def AbandonarPuerta(Sector,Entity_Name):
	global TrampaPuerta_Abandonada
	if(Entity_Name == "Player1"):
		TrampaPuerta_Abandonada = 1


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para totem.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

### PLAGUE: The sounds for totem are just really weak. They have to be changed and more sounds added.
### Also, why does this part have no music in the background? Surely, it's an oversight.

def SonidoEsfuerzo(Esfuerzo):
	char = Bladex.GetEntity("Player1")

	if Esfuerzo == 0:
		soundesfuerzo1.Position = char.Position
		soundesfuerzo1.PlaySound(0)
	elif Esfuerzo == 1:
		soundesfuerzo2.Position = char.Position
		soundesfuerzo2.PlaySound(0)
	elif Esfuerzo == 2:
		soundesfuerzo3.Position = char.Position
		soundesfuerzo3.PlaySound(0)


def SonidoCrujido(Crujido):
	totem = Bladex.GetEntity("Totem")

	if Crujido == 0:
		soundcrujido1.Position = totem.Position
		soundcrujido1.PlaySound(0)
	else:
		soundcrujido2.Position = totem.Position
		soundcrujido2.PlaySound(0)
		
def SonidoHit(Hit):
	
	if Hit == 0:
		soundtotemhit.Position = -88742, -31228, 155657
		soundtotemhit.PlaySound(0)
	elif Hit == 1:
		soundtotemhit2.Position = -88742, -31228, 155657
		soundtotemhit2.PlaySound(0)
		soundtotemhit.Position = -88742, -31228, 155657
		soundtotemhit.PlaySound(0)
	elif Hit == 2:
		soundtotemhit3.Position = -88742, -31228, 155657
		soundtotemhit3.PlaySound(0)
	

def TotemThrow(a,b):
	totem.TurnOff()
	totem.Actor = 0
	#totem.RotateRel(0,0,0,0,1,0,1.031)
	#boingtotem.RotateRel(0,0,0,0,1,0,1.031)
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	totem.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	totem.Position = -95065.856439,-26800.893892,155774.699829
	boingtotem.Orientation = 0.610343694687, 0.640066862106, 0.339167416096, 0.32056269049
	boingtotem.Position = totem.Position


def TotemHit(a,b):
	polvareda=Bladex.CreateEntity("PolvoTotem", "Entity Particle System D1",-88742.4423416, -31228.7072266, 155657.00)
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=300
	polvareda.DeathTime=Bladex.GetTime()+15.0/60.0
	polvareda.Velocity=0.0, -300.0, 0.0
	polvareda.RandomVelocity=60.0

	# soundtotemhit.Position = -88742, -31228, 155657
	# soundtotemhit.PlaySound(0)


def ThrowTotem(entity,use_from):
	global punterototem
	char = Bladex.GetEntity("Player1")

	angle = B3DLib.GetEntity2EntityAngle ("Player1","Totem")

	if (angle > 4.35 and angle < 5.25):
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("tot_Camera01.cam",0,194)
		Bladex.DeactivateInput()                       # PLAGUE: need to make skippable

		char.QuickFace(angle)

		totem.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
		totem.Actor = 1
		totem.Animation="Totem2"
		totem.SendSectorMsgs=0
		totem.FPS=60.0              # Was 20 -LeadHead
		totem.TurnOn()

		char = Bladex.GetEntity("Player1")
		char.Position = -97917.806693, -28231.1643199, 155629.20606
		char.Angle    = 4.70365019222
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)
		char.LaunchAnimation("Bar_totem_fall")
		char.SetOnFloor()
		time = Bladex.GetTime()

		Bladex.AddScheduledFunc(time + 0.8,SonidoEsfuerzo,(1,),"SonidoEsfuerzo1")
		Bladex.AddScheduledFunc(time + 2.35,SonidoEsfuerzo,(2,),"SonidoEsfuerzo2")
		Bladex.AddScheduledFunc(time + 4.57,SonidoEsfuerzo,(3,),"SonidoEsfuerzo3")

		Bladex.AddScheduledFunc(time + 1.1,SonidoCrujido,(1,),"SonidoCrujido1")
		Bladex.AddScheduledFunc(time + 2.7,SonidoCrujido,(1,),"SonidoCrujido1")
		Bladex.AddScheduledFunc(time + 5.65,SonidoCrujido,(2,),"SonidoCrujido2")
		# Bladex.AddScheduledFunc(time + 6.39,SonidoCrujido,(2,),"SonidoCrujido2")
		
		Bladex.AddScheduledFunc(time + 7.27,SonidoHit,(1,),"SonidoHit1")
		Bladex.AddScheduledFunc(time + 7.61,SonidoHit,(2,),"SonidoHit2")
		Bladex.AddScheduledFunc(time + 8.16,SonidoHit,(0,),"SonidoHit3")
		

		cam.AddCameraEvent(147,TotemHit)
		cam.AddCameraEvent(190,TotemThrow)
		ent = Bladex.GetEntity(entity)
		ent.SubscribeToList("Pin")
		punterototem = 0

		Scorer.SetVisible(0)

		#soundcharesfuerzo.Play(char.Position[0],char.Position[1],char.Position[2],2)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

#def musicaguagua():
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Casaguagua") )


def AbrePuertar1():
	puertar1.OpenDoor()
	darfuncs.LaunchMaxCamera("Palanca_casa_jefeCamera01.cam",0,-1)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("ABREPTATRAMP") )

def CierraPuertar1():
	puertar1.CloseDoor()



def Abrepuertasag():
	puertasag1.OpenDoor()
def CierraPuertasag(sectorindex,entityname):
	if entityname=="Player1":
		#puertasag1.CloseDoor()
		ptatrampa.CloseDoor()
		serB1.OnEnter=""

def Abreptapie():
	ptapie.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("ABREPTAFINAL") )    ### PLAGUE: Why are you executing 2 music events one after another?
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def Abreptamad1():
	ptamad1.OpenDoor()
def Cierraptamad1():
	ptamad1.CloseDoor()


def Abreptamad2():
	ptamad2.OpenDoor()
def Cierraptamad2():
	ptamad2.CloseDoor()

def Abreptamad3():
	ptamad3.OpenDoor()
def Cierraptamad3():
	ptamad3.CloseDoor()

def Abrereja69():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 1000)
	vel_finales=(1000.0, 500)

	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja69():

	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(1000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position= -108000,7000,-95000			# inicio

def IrPosicion2():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	#char.Position=-136000,-7000,-33500			# 1� CASETA
	char.Position=-52888.195, -12282.512, -33827.475	# 2� CASETA

def IrPosicion3():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	#char.Position=-177000,-12000,159000			# 1� PLATAFORMA
	char.Position=-10247.011, -20262.289, 29933.041		# ACANTILADO MEDIA ALTURA

def IrPosicion4():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-111871.8, -6577.318, 88409.0		# ante la pared escalable

def IrPosicion5():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-102500, -30000,159000			# TOTEM

def IrPosicion6():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-30250,-31000,191000			# PUENTE

def IrPosicion7():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=114250, -55000,138500			# ZONA SAGRADA FINAL

def IrPosicion8():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-22805, -8164, -85943			# CON LAS ARANAS
	char.Angle= 4.35

def IrPosicion9():
	import Doors
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=119298.8, -53628.1, 181364.0		# FINAL ANTEPASADOS
	char.Angle= 4.35
"""
def IrPosicion10():
	char=Bladex.GetEntity("Player1")
	per =  Bladex.GetEntity(char.ActiveEnemy)
	if per.Person:
		per.Life = 0
		wps=Bladex.CreateEntity(per.Name+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=per.Name
		wps.ParticleType="EnergyConc"
		wps.Time2Live=60
		wps.RandomVelocity=0
		wps.Velocity=(0,0,0)
		wps.NormalVelocity=-9.0
		wps.YGravity=0
		wps.PPS=200
		wps.DeathTime=Bladex.GetTime()+1.5
"""

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para pinchos3.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DeactivatePinchoOnHit3 (EntityName, VictimName, ImpX, ImpY, ImpZ):
	# Deactivate pincho
	pincho = Bladex.GetEntity(EntityName)
	pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
	pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)

def ActivatePinchos3():
	for i in range(1,19):
		# Activate pincho
		# print "Pinchos3_"+`i`        # PLAGUE: Stop spamming the console ffs
		pincho=Bladex.GetEntity("Pinchos3_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,1,0)
		pincho.InflictHitFunc= DeactivatePinchoOnHit3

def DeactivatePinchos3():
	for i in range(1,19):
		# Activate pincho
		pincho=Bladex.GetEntity("Pinchos3_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para pinchos2.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DeactivatePinchoOnHit2 (EntityName, VictimName, ImpX, ImpY, ImpZ):
	# Deactivate pincho
	pincho = Bladex.GetEntity(EntityName)
	pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
	pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)

def ActivatePinchos2():
	for i in range(3,28):
		# Activate pincho
		# print "Pinchos2_"+`i`     # # PLAGUE: Stop spamming the console ffs
		pincho=Bladex.GetEntity("Pinchos2_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,1,0)
		pincho.InflictHitFunc= DeactivatePinchoOnHit2

def DeactivatePinchos2():
	for i in range(3,28):
		# Activate pincho
		pincho=Bladex.GetEntity("Pinchos2_"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para InicioScene.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def StopCameraInicio(Camera,frame):
	#char.Angle = 0.0
	Scorer.SetVisible(1)
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	crowinicio2.Actor = 0
	crowinicio2.Orientation = 0.7, 0.7, 0.0, 0.0
	crowinicio2.Actor = 1
	crowinicio2.Animation="Crw_pic"
	crowinicio2.TurnOn()
	if Reference.DEMO_MODE==0:
		GotoMapVars.MapText(1,"D_M1_T1")
	ScriptSkip.SkipScriptEnd()


def FlyCrow2(camera,frame):
	crowinicio.Alpha = 1.0

def FlyCrow():
	crowinicio.Actor=1
	crowinicio.Alpha = 0.0
	crowinicio.Animation="Crw_start_fly"
	crowinicio.FPS=60.0         # was 20 -LeadHead
	#crowinicio.Frame = frame
	crowinicio.SendSectorMsgs=0
	crowinicio.TurnOn()

def DestroyCrow(camera,frame):
	global crowinicio
	crowinicio.SubscribeToList("Pin")
	crowinicio = 0

def BarbInicio():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("inicio") )
	GameText.WriteText("M1T1")

	char.Position = -83243,8785,-127941

	char.Position = -83243,8785,-127941

	char.Angle = 1.047
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnimation("Bar_start_barbaros")
	char.SetOnFloor()

	crowinicio2.Actor=1
	crowinicio2.Animation="Crw_start_pic"
	crowinicio2.FPS=60.0                # Was 20 -LeadHead
	crowinicio2.SendSectorMsgs=0
	crowinicio2.TurnOn()

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Barbaro_Camera01.cam",0,533)
	cam.AddCameraEvent(-1,StopCameraInicio)
	cam.AddCameraEvent(195,FlyCrow2)
	FlyCrow()
	cam.AddCameraEvent(301,DestroyCrow)

	Bladex.SetListenerPosition(1)

def ParchePrecarga():
	ScriptSkip.SkipScriptStart("Barb_M1 intro")
	AuxFuncs.FadeFrom(4.5, 0.0)
	Bladex.AddScheduledFunc(Bladex.GetTime(),BarbInicio,(),"BarbInicio")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Barbaro_Camera01.cam",0,1)
	Bladex.SetListenerPosition(2)
	char.Position = -83243,8785,-127941




#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Enemigos.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SKELRO():
	darfuncs.UnhideBadGuy("26ZM")


def BarbDefeatsOrc(person):
	Bladex.GetEntity(person).Data.ImDeadFuncX(person)
	Bladex.TriggerEvent(2)



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para comestibles.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Apagala(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingueAntorcha"