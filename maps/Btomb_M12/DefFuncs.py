##///
##||| Btomb_M12/DEFFUNCS.PY TITANIUM
##||| Change list:
##||| * Fixed error with broken walking introduced in re-release at the end of the level
##||| * Better visual effects for breakable walls/pillars.
##\\\ 

import def_class
import Bladex
import EnemyTypes
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
import Room
import Button
import MusicTool
import GotoMapVars
import ScriptSkip
import CharStats
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para collaps.py         **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

### 
def dustTriangle (name,p1,p2,p3):
	dust=Bladex.CreateEntity(name, "Entity Particle System D3", p3[0],p3[1],p3[2] )
	dust.D1= p1[0]-p3[0] ,p1[1]-p3[1] ,p1[2]-p3[2]
	dust.D2= p2[0]-p3[0] ,p2[1]-p3[1] ,p2[2]-p3[2]
 	dust.ParticleType="MediumDust"
	dust.YGravity=30.0
	dust.Friction=0.2
	dust.PPS=412*2
	dust.Velocity=0.0, -410.0, 0.0
	dust.RandomVelocity=40.0
	dust.Time2Live=10
	dust.DeathTime=Bladex.GetTime()+29.0/60.0

### Optimized below func 
### and added dust particles on breaking
###             -LeadHead

def RompeMuroFalso(sector_index, entity_name, px, py, pz,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0):
	print sector_index,"rompete",px,py,pz
	if (pz!=0):
		if (sector_index in sectorGroupBarrote):
			sonidoroturamurofalso.Play(340000,1000,-157000, 0)
			sectorbarrote.DoBreak((600.0, -50.0, -100.0), (30000,-1000,0), (0.0, 0.0, 0.0))
			sectorrompebarrote.OnHit=""
			sectorrompebarroteb.OnHit=""
			sectorrompebarrotec.OnHit=""
            
			p0 = (339867.0, -932.0, -156476.0)
			p1 = (339867.0, 2608.0, -156476.0)
			p2 = (339727.0, -932.0, -157566.0)
			p3 = (339727.0, 2708.0, -157566.0)
			
			dustTriangle("breakDustBarrote1",p0,p1,p2)
			dustTriangle("breakDustBarrote2",p1,p2,p3)

		"""
		if ((sectorrompebarroteb.Index == sector_index) and (pz!=0)):
			sonidoroturamurofalso.Play(340000,1000,-157000, 0)
			sectorbarrote.DoBreak((600.0, -50.0, -100.0), (30000,-1000,0), (0.0, 0.0, 0.0))
			sectorrompebarroteb.OnHit=""

		if ((sectorrompebarrotec.Index == sector_index) and (pz!=0)):
			sonidoroturamurofalso.Play(340000,1000,-157000, 0)
			sectorbarrote.DoBreak((600.0, -50.0, -100.0), (30000,-1000,0), (0.0, 0.0, 0.0))
			sectorrompebarrotec.OnHit=""
		"""


		if (sectorrompesecreto.Index == sector_index):
			sonidoroturamurofalso.Play(342000,0,-148000, 0)
			sectorsecreto.DoBreak((950.0, -20.0, -2.5), (30000,-1000,0), (0.0, 0.0, 0.0))
   	     
			p0 = (342000.0, -725.0, -146880.0)
			p1 = (342000.0, -1830.0, -150480.0)
			p2 = (342000.0, 2170.0, -150480.0)
			p3 = (342000.0, 2170.0, -146880.0)
			
			dustTriangle("breakDustSecreto1",p0,p1,p2)
			dustTriangle("breakDustSecreto2",p0,p2,p3)
			sectorrompesecreto.OnHit=""

		if (sector_index in sectorGroupBarrote2):
			sonidoroturamurofalso.Play(329100,0,-181500, 0)
			sectorbarrote2.DoBreak((650.0, -70.0, -2.5), (30000,-1000,0), (0.0, 0.0, 0.0))
			sectorrompebarrote2.OnHit=""
			sectorrompebarrote2b.OnHit=""
			sectorrompebarrote2c.OnHit=""
            
			p0 = (329263.0, -2012.0, -181235.0)
			p1 = (329263.0, -2012.0, -181985.0)
			p2 = (329248.0, 988.0, -181985.0)
			p3 = (329263.0, 988.0, -181235.0)
            
			dustTriangle("breakDustBarrote21",p0,p1,p2)
			dustTriangle("breakDustBarrote22",p0,p2,p3)

		"""
	if ((sectorrompebarrote2b.Index == sector_index) and (pz!=0)):
		sonidoroturamurofalso.Play(329100,0,-181500, 0)
		sectorbarrote2.DoBreak((0.0, 0.0, -2.5), (30000,-1000,0), (0.0, 0.0, 0.0))
		sectorrompebarrote2b.OnHit=""

	if ((sectorrompebarrote2c.Index == sector_index) and (pz!=0)):
		sonidoroturamurofalso.Play(329100,0,-181500, 0)
		sectorbarrote2.DoBreak((0.0, 0.0, -2.5), (30000,-1000,0), (0.0, 0.0, 0.0))
		sectorrompebarrote2c.OnHit=""
		"""

	#if ((sectorrompebarrote4.Index == sector_index) and (pz!=0)):
		#sonidoroturamurofalso.Play(333100,0,-183000)
		#sectorbarrote4.DoBreak((0.0, 0.0, -2.5), (30000,-1000,0), (0.0, 0.0, 0.0))
		#sectorrompebarrote4.OnHit=""

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def TerminanLasMuertes():
	sectx3=Bladex.GetSector(386578.916808, 8867.48182393, -211720.872601)
	sectx3.OnEnter=x3

def ParaMusicaCombate():

	Bladex.ExeMusicEvent(-1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))
	MusicTool.Music2Sector("ambiente20",None)



def Musicafondo(sectorindex,entityname):

	if entityname=='Player1':
		fastGoTo("6ORC",373724.019977, 8774.43040523, -211521.181187)
		sectxmusica.OnEnter=""



def Suenamusica1():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))



def Suenamusica2():

	Bladex.ExeMusicEvent(-1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))

def Suenamusica3():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera7"))
	MusicTool.Music2Sector("ambiente17","Atmosfera7")
	MusicTool.Music2Sector("ambiente18","Atmosfera5")
	MusicTool.Music2Sector("ambiente4",None)
	MusicTool.Music2Sector("ambiente7",None)

def Suenamusica4():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))

def Suenamusica5():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera7"))

def Suenamusica6():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))

def Suenamusica7():

	Bladex.ExeMusicEvent(-1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, MusicTool.LaunchMusicEvent,("Atm12mp3",))
	MusicTool.Music2Sector("ambiente33",None)


def KreaOrkos():
	darfuncs.UnhideBadGuy("7ORC")
	darfuncs.UnhideBadGuy("8ORC")


def x3(sectorindex,entityname):

	if entityname=='Player1':
		KreaOrkos()
		sectx3.OnEnter=""


def x3b(sectorindex,entityname):

	if entityname=='Player1':
		GoToGol("13aORC")
		sectx3b.OnEnter=""

def x3c():

	GoToGol("17ORC")
	GoToGol("18ORC")
	Subegas()
	Cierrate()



def x3d(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("Golem1")
		pers=Bladex.GetEntity("Golem1")
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,pers.GoTo,(356127.488618, 403.925448391, -185658.845326))
		sectx3e.OnEnter=""






def x4(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("OasisArq3")
		darfuncs.UnhideBadGuy("OasisArq4")
		darfuncs.UnhideBadGuy("3ORC")
		darfuncs.UnhideBadGuy("19ORC")
		sectx4a.OnEnter=""
		sectx4b.OnEnter=""

def CreaCastillo():
	darfuncs.UnhideBadGuy("20ORC")
	darfuncs.UnhideBadGuy("21ORC")
	darfuncs.UnhideBadGuy("21ORCb")
	darfuncs.UnhideBadGuy("21ORCc")
	GoToGol("20ORC")
	GoToGol("21ORC")


def x9(sectorindex,entityname):

	if entityname=='Player1':
		pers=Bladex.GetEntity("26bEsq")
		pers.GoToJogging = 1
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(354128.907509, 11758.5140098, -107744.42926))
		sectx9.OnEnter=""



def fastGoTo(entName,x,y,z):
	p =Bladex.GetEntity(entName)
	p.GoToJogging = 1
	p.GoTo(x,y,z)


def x10(sectorindex,entityname):

	if entityname=='Player1':
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,fastGoTo,("31Esq",371838.484577, 40244.0880987, 36458.5445663))
		fastGoTo("32Esq",376302.568618, 41354.8020703, 36612.4154227)
		sectx10.OnEnter=""

def x11(sectorindex,entityname):

	if entityname=='Player1':
		GoToGol("33Esq")
		GoToGol("34Esq")
		GoToGol("35Esq")
		sectx11.OnEnter=""


	#if entityname=='Player1':
		#fastGoTo("33Esq",487605.272802, 57946.8756132, 85582.0257655)
		#fastGoTo("34Esq",479654.364488, 54901.6366898, 99993.165494)
		#fastGoTo("35Esq",477407.874525, 53730.92171, 103898.050251)
		#sectx11.OnEnter=""

def x12(sectorindex,entityname):

	if entityname=='Player1':
		fastGoTo("36Esq",448054.522616, 48558.9713996, 30894.6591573)
		fastGoTo("37Esq",449078.357274, 47667.5906275, 34939.5928367)
		sectx12.OnEnter=""


def xtrl1():
	#darfuncs.UnhideBadGuy("TRL2")
	pers=Bladex.GetEntity("TRL2")
	pers.GoTo(313895.545458, 42402.9528677, -123820.440824)


#def xtrl2(sectorindex,entityname):

	#if entityname=='Player1':
		#pers=Bladex.GetEntity("TRL2")
		#pers.GoTo,(325131.464411, 43952.6537602, -109995.694982)
		#sectxtrl2.OnEnter=""


def x5(sectorindex,entityname):

  if entityname=='Player1':
    CreaCastillo()
    sectx5.OnEnter=""
"""
def CreaGolem():
	darfuncs.UnhideBadGuy("Golem2")
	darfuncs.HideBadGuy("30Esq")
	darfuncs.HideBadGuy("31Esqx")


def x6(sectorindex,entityname):

  if entityname=='Player1':
    CreaGolem()
    sectx6.OnEnter=""


def CreaGolem2():
	darfuncs.UnhideBadGuy("30Esq")
	darfuncs.HideBadGuy("Golem2")
	darfuncs.UnHideBadGuy("31EsqX")

def x7(sectorindex,entityname):

  if entityname=='Player1':
    CreaGolem2()
    sectx7.OnEnter=""
"""
def GoToGol(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToGol


def MueveGol():
	for enemigo in listabichos:
		GoToGol(enemigo.Name)


def KreaGol():
	darfuncs.UnhideBadGuy("GolemFinal2")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, MueveGol,())

def x8(sectorindex,entityname):

  if entityname=='Player1':
    KreaGol()
    sectx8.OnEnter=""


def DerribaMuro(obj_name, use_from):
        EscenaGranFinal()
        punteromuro         = Bladex.GetEntity(obj_name)
        punteromuro.UseFunc = ""

def MurioElEsqueleto():
	punteromuro        = Bladex.CreateEntity("PunteroMuro","GhostPointer", 483625,47100,61250)
	punteromuro.Static = 1
	punteromuro.Scale  = 1.000000
	punteromuro.Orientation = 0.707107,0.707107,0.000000,0.000000
	punteromuro.UseFunc=DerribaMuro
	darfuncs.SetHint(punteromuro,"Gravestone")
"""
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para esqueletos.py      **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def AsingaPropiedadesEsqueletos(ent):
	ent.Level = 15
	ent.ActionAreaMin=pow(2,2)
	ent.ActionAreaMax=pow(2,3)
	ent.SetActiveEnemy("Player1")
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
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3))
"""
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para lichs.py           **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def AsingaPropiedadesLich(ent):
	ent.Level = 12
	ent.Life = CharStats.GetCharMaxLife(ent.Kind,ent.Level)
	ent.ActionAreaMin=pow(2,8)
	ent.ActionAreaMax=pow(2,9)
	ent.SetActiveEnemy("Player1")

def CreateParticle(r= 30,g = 40,b = 50,al = 230.0,part = "BubbleParticle"):
	Bladex.AddParticleGType("Espuma",part,2,8)

	for i in range(8):
		if i < 4:
			aux=1.0 - ((4.0-i)/4.0)

		else:
			aux=(4.0-(i-4))/4.0

		size=10+aux*30.0
		Bladex.SetParticleGVal("Espuma",i,r,g,b,al,size)

def CalculatePositionWave(espuma,cam,posi,deathtime):
	time = Bladex.GetTime()

	if time < deathtime:
		campos = cam.Position
		v=campos[0]-posi[0], 0.0, campos[2]-posi[2]
		v=AuxFuncs.Normalize(v)

		pos = posi[0] + v[0] * 1000,posi[1],posi[2] + v[2] * 1000
		desp = v[2] * -500,v[0] * 500

		espuma.Position = pos[0] + desp[0],16700.0,pos[2] + desp[1]
		espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2

		Bladex.AddScheduledFunc(time + 0.05,CalculatePositionWave,(espuma,cam,posi,deathtime))

def SaltaAguaGen(enmgen):
#def SaltaAguaGen():
	global Esp
	Esp = Esp +1
	pos=enmgen.Position
	#pos = -35000, 10000, -47000
	#pos = char.Position
	cam = Bladex.GetEntity("Camera")
	charpos = cam.Position
	v=charpos[0]-pos[0], 0.0, charpos[2]-pos[2]
	v=AuxFuncs.Normalize(v)

	rpos = pos[0] + v[0] * 800,pos[1],pos[2] + v[2] * 800
	desp = v[2] * -400,v[0] * 400

	espuma=Bladex.CreateEntity("Espuma"+`Esp`, "Entity Particle System D2", rpos[0] + desp[0],16700.0,rpos[2] + desp[1])
	espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2
	espuma.ParticleType="Espuma"
	espuma.PPS=512
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, 0.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.Time2Live=8
	espuma.DeathTime = Bladex.GetTime() + 7.0

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,CalculatePositionWave,(espuma,cam,pos,espuma.DeathTime))


def SaltaAguaGenActivate(enmgen):
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,SaltaAguaGen,(enmgen,))

def ActivateGen1(sector,entity):
	if (entity == "Player1"):
		Gen1Sec.OnEnter = ""
		generadorT1.GenerateEnemy()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para inicio.py          **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def StopCameraInicio2(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	ScriptSkip.SkipScriptEnd()
	Scorer.SetVisible(1)
	cam.SetPersonView("Player1")
	cam.Cut()

def Cierrapuertadeldemonio(Camera,frame):

	desplazamientos=(2000, 2025, 400.0, 400.0, 100.0, 100.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 3000, 5000.0, 0.0, 4000.0, 0.0)
	vel_finales=(3000.0, 5000, 0.0, 4000.0, 0.0, 1000.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastrinidin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def MusicayTextoA():
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("btomb-carga"))
  GameText.WriteText("M12T1")

def IniciaJuego():
  Scorer.SetVisible(0)
  ScriptSkip.SkipScriptStart("BtombInicio")
  cam = Bladex.GetEntity("Camera")
  cam.SetMaxCamera("Oasis_inicio.cam",0,600)
  cam.AddCameraEvent( -1,StopCameraInicio2)
  cam.AddCameraEvent(400,Cierrapuertadeldemonio)
  char.SetTmpAnmFlags(1,1,1,0,5,1,0)
  char.Angle    = -3.14159265
  char.Position = 325966, -70, -235386
  char.Wuea=Reference.WUEA_ENDED
  char.LaunchAnmType("start_oasis")
  char.SetOnFloor()



  Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,MusicayTextoA,())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para Granfinal.py       **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def MusicaytextoB():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("btomb-mural"))
	GameText.WriteText("M12T3")


def MurioElVamp(entity_name):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent, (33,))
	global EnCounter
	global IsEnBucle
	global VampiroIs

	PhantonFX.Delta = 0.0125
	PhantonFX.DisappearsChar(entity_name)
	per = Bladex.GetEntity(entity_name)
	AuxFuncs.FadeTo(5.5,24.0)
	Bladex.DeactivateInput()
	import GotoMapVars
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.5,GotoMapVars.EndOfLevel,())



def CreaElVampiro():
	darfuncs.UnhideBadGuy("Drakula")
	Drakula = Bladex.GetEntity("Drakula")
	Drakula.Blind       = 1
	Drakula.Deaf        = 1

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, AnimaElVampiro,())

def AnimaElVampiro():
	Drakula = Bladex.GetEntity("Drakula")

	Drakula.ImDeadFunc  = MurioElVamp
	Drakula.SetTmpAnmFlags(1,1,1,0,5,1,0)
	Drakula.Wuea=Reference.WUEA_ENDED
	Drakula.LaunchAnmType("Vmp_oasis_muraldoble")
	Drakula.Angle       = -3.14159/2
	Drakula.Position    = 475631.781, 46365.336, 61025.301
	Drakula.SetOnFloor()



#----------------------------------------------------------------------------------------#

def EscenaGranFinal():
        char = Bladex.GetEntity("Player1")
        char.Position = 483729.844, 46114.094, 60870.043
        char.SetOnFloor()
        char.Angle       = -3.14159/2
        ScriptSkip.SkipScriptStart("BtombFinal")
        #Bladex.DeactivateInput()
        Scorer.SetVisible(0)
        global player



        Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, MusicaytextoB,())

        char.Wuea=Reference.WUEA_ENDED
        char.LaunchAnimation("Kgt_oasis_muraldoble")

        char.SetOnFloor()
        cam = Bladex.GetEntity("Camera")
        cam.SetMaxCamera("Oasis_Camera_heroe_mira.cam",0,169)
        print "Oasis_Camera_heroe_mira.cam"
        cam.AddCameraEvent( -1,Camara1)
        CreaElVampiro()

def Camara1(Camera,frame):
        cam = Bladex.GetEntity("Camera")
        cam.SetMaxCamera("Oasis_Camera_muraldcha.cam",170,378)
        print "Oasis_Camera_muraldcha.cam"
        cam.AddCameraEvent( -1,Camara2)

def Camara2(Camera,frame):
        cam = Bladex.GetEntity("Camera")
        cam.SetMaxCamera("Oasis_Camera_heroe_mira.cam",379,540)
        print "Oasis_Camera_heroe_mira.cam"
        cam.AddCameraEvent( -1,Camara3)

def Camara3(Camera,frame):
        cam = Bladex.GetEntity("Camera")
        cam.SetMaxCamera("Oasis_Camera_muralizda.cam",541,741)
        print "Oasis_Camera_muralizda.cam"
        cam.AddCameraEvent( -1,Camara4)
        Actions.QuickTurnToFaceEntity("Drakula", "Player1")

def Camara4(Camera,frame):
        cam = Bladex.GetEntity("Camera")
        print "Oasis_Camera_final.cam"
        cam.SetMaxCamera("Oasis_Camera_final.cam",742,909)
        cam.AddCameraEvent( -1,Camara5)

def Camara5(Camera,frame):
        cam = Bladex.GetEntity("Camera")
        ScriptSkip.SkipScriptEnd()
        #Bladex.ActivateInput()
        GotoMapVars.MapText(-1,"NEJEVMURAL")
        Scorer.SetVisible(1)
        cam.SetPersonView("Player1")
        cam.Cut()
        Drakula = Bladex.GetEntity("Drakula")
        Drakula.Blind       = 0
        Drakula.Deaf        = 0
        Actions.QuickTurnToFaceEntity("Drakula", "Player1")
        Actions.QuickTurnToFaceEntity("Player1", "Drakula")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para Gases.py           **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrete():

	desplazamientos=(2369, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastrillomovildin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrate():

	desplazamientos=(1684.5, 1684.5, 500.0, 500.0, 125.0, 125.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 3000, 5000.0, 0.0, 4000.0, 0.0)
	vel_finales=(3000.0, 5000, 0.0, 4000.0, 0.0, 1000.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastrillomovildin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)





##funcion que abre y cierra la puertagas

def Subegas():
	puertagas.CloseDoor()


def Bajagas():
	puertagas.OpenDoor()



def CreateGas(vx,vy,vz,delta):
   Gasero=Bladex.CreateEntity(Bladex.GenerateEntityName(), "Entity Particle System D1", vx,vy,vz)
   Gasero.ParticleType="LargeDust"
   Gasero.Time2Live= 20    #*self.size_factor
   Gasero.YGravity=-3000
   Gasero.Friction=0
   Gasero.RandomVelocity=+50.0
   Gasero.RandomVelocity_V=0.0
   Gasero.Velocity = delta,0,0
   Gasero.PPS=24
   return Gasero

def SetGasSpeed(delta):
  if(delta==0):
    Gas1.Time2Live = 0
    Gas2.Time2Live = 0
    Gas3.Time2Live = 0
    Gas4.Time2Live = 0
  else:
    Gas1.Velocity = +delta,0,0
    Gas2.Velocity = +delta,0,0
    Gas3.Velocity = -delta,0,0
    Gas4.Velocity = -delta,0,0

    Gas1.Time2Live = 20
    Gas2.Time2Live = 20
    Gas3.Time2Live = 20
    Gas4.Time2Live = 20

def GasTimer(e_name, time):
  global GasCounter

  GasCounter = GasCounter + 1

  if(GasCounter==20):
    Bladex.ActivateInput()
    Scorer.SetVisible(1)

  if (GasCounter >=44):
    #p1.Move(-25,0,0)
    #p2.Move(-25,0,0)
    #p3.Move( 25,0,0)
    #p4.Move( 25,0,0)
  #else:
    SetGasSpeed(2000)
    char=Bladex.GetEntity("Player1")
    if GasCounter%5==0:
        char.Life = char.Life-(CharStats.GetCharMaxLife(char.Kind,char.Level)*0.50)/60.0


def DeActivateTrap(sectorindex,entityname):
  if entityname=='Player1':
    Gas1.TimerFunc=""
    Gas1.RemoveFromList("GasTimer")
    SetGasSpeed(0)
    CerraduraGas.OnUnLockFunc=""
    sectOutGas.OnEnter=""


def EndGasTrap():
  Abrete()
  #sectOutGas.OnEnter=DeActivateTrap
  Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, DeActivateTrap, (1,"Player1"))
  _GasSound.Stop()
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))
  MusicTool.Music2Sector("ambiente1",None)
  MusicTool.Music2Sector("ambiente3",None)
  MusicTool.Music2Sector("ambiente5",None)
  MusicTool.Music2Sector("ambiente7",None)
  MusicTool.Music2Sector("ambiente8",None)
  MusicTool.Music2Sector("ambiente9",None)
  MusicTool.Music2Sector("ambiente10",None)
  MusicTool.Music2Sector("ambiente11",None)
  MusicTool.Music2Sector("ambiente12",None)
  MusicTool.Music2Sector("ambiente14",None)
  MusicTool.Music2Sector("ambiente15",None)
  MusicTool.Music2Sector("ambiente16",None)
  MusicTool.Music2Sector("ambiente17",None)
  MusicTool.Music2Sector("ambiente18",None)
  MusicTool.Music2Sector("ambiente19",None)


def InitGasTrap():
  # retornar la camara a su posicion inicial
  Cam = Bladex.GetEntity("Camera")
  Cam.SetPersonView("Player1")
  Cam.Cut()
  Bladex.GetEntity("Orkus0").SubscribeToList("Pin")
  Bladex.GetEntity("Orkus1").SubscribeToList("Pin")


  # activar la Apertura de puertas
  CerraduraGas.OnUnLockFunc=EndGasTrap
  CerraduraGas.OnUnLockArgs=()

  CerraduraGas.key="LlaveGas1"

  Subegas()           # puerta de atras

  # Puerta rastrillo

  #Cierrate()
  
  Gas1.SubscribeToList("GasTimer")
  Gas1.TimerFunc=GasTimer
  Ontake.DelOnTakeEvent("GoldKey")
  _GasSound.Play(char.Position[0], char.Position[1], char.Position[2],-1)




#crea un orco
def CreaOrco(n, x, y, z,flag):

	if not flag:
		hacha=Bladex.CreateEntity("HachaEsqOrkus"+`n`, "Hacha", 0, 0, 0)
		hacha.Weapon=1

		esq=Bladex.CreateEntity("Orkus"+`n`, "Ork", x, y, z)
		esq.Person=1
		esq.Angle=0.0
		esq.Level=7
		esq.Blind=1
		esq.Deaf=1
		esq.Position = x, y, z
		Actions.TakeObject(esq.Name, hacha.Name)

		#esq.ActionAreaMin=pow(2,0)
		#esq.ActionAreaMax=pow(2,1)

		darfuncs.HideBadGuy("Orkus"+`n`)
	else:
		esq=Bladex.GetEntity("Orkus"+`n`)
		darfuncs.UnhideBadGuy("Orkus"+`n`)

	return esq

def endofanima(o):
	print "Fin!"
	esq       = Bladex.GetEntity(o)
	EnemyTypes.EnemyDefaultFuncs(esq)
	esq.Blind = 0
	esq.Deaf  = 0

def endofanima11(o):
	print "11"
	ork       = Bladex.GetEntity(o)
	ork.SetTmpAnmFlags(1,1,1,0,5,1,0)
	ork.Wuea=Reference.WUEA_ENDED
	ork.LaunchAnimation("Ork_laughing1")
	_OrcoFuckOff.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
	ork.AnmEndedFunc = endofanima


def endofanima22(o):
	print "22"
	ork       = Bladex.GetEntity(o)
	ork.SetTmpAnmFlags(1,1,1,0,5,1)
	ork.Wuea=Reference.WUEA_ENDED
	ork.LaunchAnimation("Ork_laughing2")
	_OrcoDancing.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
	ork.AnmEndedFunc = endofanima

def endofanima1(o):
	print "1"
	ork       = Bladex.GetEntity(o)
	ork.SetTmpAnmFlags(1,1,1,0,5,1)
	ork.Wuea=Reference.WUEA_ENDED
	ork.LaunchAnimation("Ork_laughing1")
	_OrcoFuckOff.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
	ork.AnmEndedFunc = endofanima11


def endofanima2(o):
	print "2"
	ork       = Bladex.GetEntity(o)
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	ork.Wuea=Reference.WUEA_ENDED
	ork.LaunchAnimation("Ork_laughing2")
	_OrcoDancing.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
	ork.AnmEndedFunc = endofanima22

#
# escena de los orcos
#----------------------------
def StartSecuence0():
  Bladex.DeactivateInput()
  Scorer.SetVisible(0)
  cam=Bladex.GetEntity("Camera")
  opos=cam.Position
  tpos=cam.TPos
  AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2],326221, 5089, -207313, tpos[0],tpos[1], tpos[2],326455, -4152, -211128, 3, StartSecuence1)
  Bladex.ExeMusicEvent(-1)
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-1b"))
  Cierrate()



def StartSecuence1():
  cam=Bladex.GetEntity("Camera")
  opos=cam.Position
  tpos=cam.TPos
  AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2], 326610, 1872, -208542, tpos[0],tpos[1], tpos[2], 322976, -4446, -215389, 3, StartSecuence2)

  ork = CreaOrco(0,325753-600, -1000, -211227,1)
  ork.SetTmpAnmFlags(1,1,1,0,5,1,0)
  ork.Wuea=Reference.WUEA_ENDED
  ork.LaunchAnimation("Ork_laughing1")
  _OrcoFuckOff.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
  ork.AnmEndedFunc = endofanima2
  ork.SetOnFloor()

  ork = CreaOrco(1,325753+800, -1000, -211227,1)
  ork.SetTmpAnmFlags(1,1,1,0,5,1,0)
  ork.Wuea=Reference.WUEA_ENDED
  ork.LaunchAnimation("Ork_laughing2")
  _OrcoDancing.Play(ork.Position[0], ork.Position[1], ork.Position[2],0)
  ork.AnmEndedFunc = endofanima1
  ork.SetOnFloor()

def StartSecuence2():
  cam=Bladex.GetEntity("Camera")
  opos=cam.Position
  tpos=cam.TPos
  AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2], 325632, 2119, -208252, tpos[0],tpos[1], tpos[2], 322354, -5925, -213207, 3, InitGasTrap)


def MuereElOtroIdiota0(entity):
	o = Bladex.GetEntity(entity)
	o.Freeze()
	o.RemoveFromWorld()
	o.Life = 0

def MuestraPobreIdiota0():
	NPC_FALSE0.PutToWorld()

def CreaPobreIdiota0():
	global NPC_FALSE0

	if Bladex.GetEntity("Player1").Kind[0]=="K":
		NPC_FALSE0 = Bladex.CreateEntity("FalseGuy0","Knight_Traitor",325210, 8890, -208000,"Person","Amazon_N")
	else:
		NPC_FALSE0 = Bladex.CreateEntity("FalseGuy0","Knight_Traitor",325210, 8890, -208000,"Person","Knight_N")
	
	NPC_FALSE0.Angle = 3.1415
	
	NPC_FALSE0.AnmEndedFunc=MuereElOtroIdiota0
	NPC_FALSE0.LaunchAnimation("Tkn_death_btomb")
	NPC_FALSE0.Position = 325210, 8890, -208000







def iniciagas():
	if NPC_FALSE0:
		SetGasSpeed(5000)
		_GasSound.Play(325718,6476,-207521,-1)
		darfuncs.EnterSecEvent(318247, 9180, -234475,finalizagas)



def finalizagas():
	if NPC_FALSE0:
		SetGasSpeed(0)
		_GasSound.Stop()
		darfuncs.EnterSecEvent(330151,  8942, -234932,iniciagas)
		darfuncs.EnterSecEvent(349986, 15874, -229334,iniciagas)


def aparecefalseguy0():

	darfuncs.UnhideBadGuy("FalseGuy")


def CreaPobreIdiota():
	global NPC_FALSE

	if Bladex.GetEntity("Player1").Kind[0]=="K":
		NPC_FALSE = Bladex.CreateEntity("FalseGuy","Knight_Traitor",325210, 8890, -208000,"Person","Amazon_N")
	else:
		NPC_FALSE = Bladex.CreateEntity("FalseGuy","Knight_Traitor",325210, 8890, -208000,"Person","Knight_N")
	
	NPC_FALSE.Angle = 3.1415
	darfuncs.HideBadGuy("FalseGuy")

def ReiniciaEscenita():
	global NPC_FALSE

	NPC_FALSE.SubscribeToList("Pin")
	
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, CreaPobreIdiota,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CaeElOtroIdiota,())

def TerminaLaEscenaDelOtroIdiota():
	Bajagas()
	Abrete()
	SetGasSpeed(0)
	_GasSound.Stop()

def MuereElOtroIdiota(entity):
	o = Bladex.GetEntity(entity)
	o.Freeze()
	o.Life = 0



def CaeElOtroIdiota():
	global NPC_FALSE0
	import AbreCam
	
	NPC_FALSE0.SubscribeToList("Pin")
	NPC_FALSE0 = None
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-13"))
	
	AbreCam.PTS = [((325509, 10928, -213686), (325851,9048, -209702), 0),
	               ((324605,  3890, -208256), (325851,9048, -209702), 15)
	              ]
	AbreCam.LastTime = 0
	AbreCam.AbreCam()
	_GasSound.Play(char.Position[0], char.Position[1], char.Position[2],-1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, TerminaLaEscenaDelOtroIdiota, ())

	darfuncs.UnhideBadGuy("FalseGuy")
	NPC_FALSE.AnmEndedFunc=MuereElOtroIdiota
	NPC_FALSE.LaunchAnimation("Tkn_death_btomb")
	NPC_FALSE.Position = 325210, 8890, -208000


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=335157,-736,-158733

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=324369.111235, 43677.1, -110513.438684

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=323990,3000,-26000


def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=325576.346627, -322.9, -183250.583375

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=292135.121946, 8927.1, -211542.829346


def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=353647.954789, 15777.1, -226879.691572

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=374073.510374, 20761.8003815, -228898.684307



def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=43000, 46335.2, 60805.3383983


def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=359709.344068, 8722.80599176, -113006.368505


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para tablilla.py        **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def ImprimeDatosTablilla(Name):
	print "--- Cut here ---"
	print "###################################################"
	print "# Tablilla para",char.Kind
	print "###################################################"

	print "if Bladex.GetEntity('Player1').Kind[0] == '"+char.Kind[0]+"':"
	print "	o             = Bladex.GetEntity('"+Name+"')"
	print "	o.Position    = ",Bladex.GetEntity(Name).Position
	print "	o.Orientation = ",Bladex.GetEntity(Name).Orientation
	print "--- Cut here ---"


# Achalay my brother!
def ComienzaAnimacionTablilla(sectorindex,entityname):


  if entityname =="Player1":
    char = Bladex.GetEntity("Player1")

    EscenaTablilla("Player1")
    TabillaSector.OnEnter = ""
    Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, desenergiza, ())


def EscenaTablilla(Entity):
  #Bladex.DeactivateInput()
  #Scorer.SetVisible(0)
  Actions.FreeBothHands(Entity,IniciaEscenaTablilla,())

def MusicaytextoC():
	GameText.WriteText("M12T2")

def IniciaEscenaTablilla(coso1,coso2):
  cam  = Bladex.GetEntity("Camera")
  char = Bladex.GetEntity("Player1")

  ###################################################
  # Tablilla para Knight_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'K':
  	o             = Bladex.GetEntity('Tablilla4')
  	o.Position    =  (325075.634237, 6397.87919524, 18328.8473839)
  	o.Orientation =  (0.877426445484, 0.479523926973, 0.00159038591664, -0.0133063020185)
  ###################################################
  # Tablilla para Barbarian_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'B':
  	o             = Bladex.GetEntity('Tablilla4')
  	o.Position    =  (325054.818449, 6182.41188138, 18459.8421414)
  	o.Orientation =  (0.851606965065, 0.523882269859, -0.0128540648147, -0.0121524231508)
  ###################################################
  # Tablilla para Dwarf_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'D':
  	o             = Bladex.GetEntity('Tablilla4')
  	o.Position    =  (325112.047752, 6704.5802554, 18435.4046063)
  	o.Orientation =  (0.88255739212, 0.468666285276, -0.0363581739366, -0.0110633997247)

  ###################################################
  # Tablilla para Amazon_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'A':
  	o             = Bladex.GetEntity('Tablilla4')
  	o.Position    =  (325106.003828, 6332.37025713, 18279.6841054)
  	o.Orientation =  (0.818497002125, 0.57433116436, 0.00605202466249, 0.0130280461162)

  char.Position = TablStartPosition[0],TablStartPosition[1],TablStartPosition[2]
  char.SetOnFloor()
  char.Angle = AnglStartPosition
  char.SetTmpAnmFlags(1,1,1,0,5,1,0)
  char.Wuea=Reference.WUEA_ENDED
  char.LaunchAnmType(AnimationName)

  char.Position = TablStartPosition[0],TablStartPosition[1],TablStartPosition[2]
  char.SetOnFloor()

  cam.SetMaxCamera(CameraName,TabSFrame,TabLFrame)
  cam.AddCameraEvent(-1,StopCameraTablilla)

  cam.AddCameraEvent(Event_CogeLaTablilla     ,CogeLaTablilla)
  cam.AddCameraEvent(Event_tTablillaDust1     ,tTablillaDust)
  cam.AddCameraEvent(Event_tTablillaDust2     ,tTablillaDust)
  cam.AddCameraEvent(Event_DesapareceTablilla ,DesapareceTablilla)
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("btomb-tablilla"))


def CreateEstrellitas():
        StarFlare=Bladex.CreateEntity("aTablillaBrillos", "Entity Particle System D1", tab.Position[0], tab.Position[1], tab.Position[2])
        StarFlare.ParticleType="Estrellitas"
        StarFlare.YGravity=1000
        StarFlare.Friction=0.3
        StarFlare.PPS=112
        StarFlare.Velocity= 0, 0.0, 0.0
        StarFlare.Time2Live=64
        StarFlare.RandomVelocity=50



def tTablillaDust(ent,Time) :
	doorDust=Bladex.CreateEntity("aTablillaDust", "Entity Particle System D1", tab.Position[0]+100, tab.Position[1]-100, tab.Position[2])
 	doorDust.ParticleType="Polvillo"
	doorDust.YGravity=0.0
	doorDust.Friction=0.3
	doorDust.PPS=112
	doorDust.Velocity=40, -40.0, 0.0
	doorDust.RandomVelocity=7.0
	doorDust.Time2Live=15
	doorDust.DeathTime=Bladex.GetTime()+10.0/60.0


def StopCameraTablilla(Camera,frame):
  global LastPViewType
  cam  = Bladex.GetEntity("Camera")
  char = Bladex.GetEntity("Player1")
  cam.SetPersonView("Player1")
  cam.Cut()
  cam.PViewType = LastPViewType
  ScriptSkip.SkipScriptEnd()
  #Bladex.ActivateInput()
  Scorer.SetVisible(1)

def DesapareceTablilla(Camera,frame):
  global PosX
  global PosY
  global PosZ
  global Tick
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.RemoveObject("Tablilla4")

  char.RemoveFromInventLeft()
  CreateEstrellitas()
  PosX  = tab.Position[0]
  PosY  = tab.Position[1]
  PosZ  = tab.Position[2]
  Tick  = 0
  Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CoolStart, ())
  tab.Position = PosX,  PosY, PosZ

def CoolStart():
  tab.SubscribeToList("TablillaTimer")
  tab.TimerFunc=TickTablilla


def TickTablilla(ent,time):
  global PosX
  global PosY
  global PosZ
  global Tick

  char      = Bladex.GetEntity("Player1")
  StarFlare = Bladex.GetEntity("aTablillaBrillos")

  iTick = 1.0-Tick
  tab.Position = PosX*iTick+char.Position[0]*Tick,  PosY*iTick+char.Position[1]*Tick, PosZ*iTick+char.Position[2]*Tick
  tab.Alpha                =  iTick
  tab.Scale                =  2.0*iTick

  StarFlare.Position       =  tab.Position
  StarFlare.RandomVelocity =  50.0*iTick

  luzta.Intensity          =  10.0*iTick
  luzta.SizeFactor         =   2.0*iTick

  Tick = Tick+0.0075

  if Tick>1:
    tab.RemoveFromList("TablillaTimer")
    tab.RemoveFromWorld()
    StarFlare.DeathTime=Bladex.GetTime()+0.005

#
# Todavia me da cosa decir cojer pero bueno
#------------------------------------------------------
def CogeLaTablilla(Camera,frame):
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.AddTablet("Tablilla4")
  inv.LinkLeftHand("Tablilla4")
  MusicaytextoC()
  ImprimeDatosTablilla("Tablilla4")
  desenergiza()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para rayos.py           **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def Chisporroteo(x,y,z):
	tierra1=Bladex.CreateEntity("Cristales", "Entity Particle System D1", x, y, z)
	tierra1.ParticleType="Chispitas"
	tierra1.PPS=128
	tierra1.YGravity=9800.0
	tierra1.Friction=0.1
	tierra1.Velocity=0.0, 0.0, -2000.0
	tierra1.RandomVelocity=50.0
	#tierra1.Time2Live=64
	tierra1.DeathTime=Bladex.GetTime()+1.5

#def CamaraDeDestruccion1():
  #Bladex.DeactivateInput()
  #Scorer.SetVisible(0)
  #cam=Bladex.GetEntity("Camera")
  #opos=cam.Position
  #tpos=cam.TPos
  #AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2],334136,-2409,-12271, tpos[0],tpos[1], tpos[2],326670,975,-6542, 3.5, CamaraDeDestruccion2)
  #Bladex.DeactivateInput()

#def CamaraDeDestruccion2():
  #cam=Bladex.GetEntity("Camera")
  #opos=cam.Position
  #tpos=cam.TPos
  #AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2],315969,756,-12011, tpos[0],tpos[1], tpos[2],324293,1070,-6479, 3.5, CamaraDeDestruccion3)

#def CamaraDeDestruccion3():
  #cam=Bladex.GetEntity("Camera")
  #opos=cam.Position
  #tpos=cam.TPos
  #AuxFuncs.MoveCamFromTo(opos[0], opos[1], opos[2],325025,4524,3082, tpos[0],tpos[1], tpos[2], 324682,4083,13066, 3.5, CamaraDeDestruccion4)

def desenergiza():
  Ojo1A.SetEnergiza(0)
  Ojo1B.SetEnergiza(0)
  Ojo2A.SetEnergiza(0)
  Ojo2B.SetEnergiza(0)

#def CamaraDeDestruccion4():
  #cam = Bladex.GetEntity("Camera")
  #cam.SType = 0
  #cam.TType = 0
  #Bladex.ActivateInput()
  #Scorer.SetVisible(1)

def BreakItBaby():
        Colu1.DoBreak( (0,0,-18), (324000,6000,15000), (0,0,-400) )
        Colu2.DoBreak( (0,0,-10), (326000,6000,15000), (0,0,-700) )

        #Colu1.Active=1
        #Colu2.Active=1
        #Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, VuelveDeNuevo, ())

#def VuelveDeNuevo():
        #Cam = Bladex.GetEntity("Camera")
        #Cam.SetPersonView("Player1")
        #Cam.Cut()
        #Bladex.ActivateInput()
        #Scorer.SetVisible(1)

def AddRayConcentrator(vx,vy,vz):

    parts=Bladex.CreateEntity(Bladex.GenerateEntityName(), "Entity Particle System D1", vx, vy, vz)
    parts.ParticleType="Energiza"
    parts.Time2Live= 20    #*self.size_factor
    parts.YGravity=9000
    parts.Friction=0
    parts.RandomVelocity=+50.0
    parts.RandomVelocity_V=0.0
    parts.PPS=64
    parts.DeathTime=3




def StopCameraPasarela(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	cam.SetPersonView("Player1")
	cam.Cut()

#
#  Entra al sector y se activa la camara
###########################################
def Pasa(sectorindex,entityname):

    if entityname=='Player1':
        plat2.CloseDoor()
        plat1.OpenDoor()
        s1=Bladex.GetSector(325000,7000,-22000)
        s1.OnEnter=""
        # Camara a su lugar
        Bladex.DeactivateInput()
        Scorer.SetVisible(0)
        #StartSecuence0()

        char.Position = 325106.642965, 6398.03854789, -22000
        char.SetTmpAnmFlags(1,1,1,0,5,1,0)
        char.Wuea=Reference.WUEA_ENDED
        char.LaunchAnmType("rlx")
        char.Angle = 0
        char.Position = 325106.642965, 6398.03854789, -22000
        char.SetOnFloor()

        Cam = Bladex.GetEntity("Camera")
        Cam.SetMaxCamera("Btomb_pasarelaCamera01.cam",0,120)
        Cam.AddCameraEvent( -1,StopCameraPasarela)

def FuncionQueDiceSiEstaAbierta():
  global EstaAbierta
  EstaAbierta = 1

  #Ojo1A.Ojo.Position = (345700.0, 3081.0, -1462.0)
  #Ojo1A.StartEnergiza(345700.0, 3081.0, -1462.0)
  #Ojo1B.StartEnergiza(345700.0, 3081.0, -5062.0)

  #Ojo2A.StartEnergiza(304300.0, 3081.0, -1462.0)
  #Ojo2B.StartEnergiza(304300.0, 3081.0, -5062.0)

def Tachan():
    izquierda1.OpenDoor()
    izquierda2.OpenDoor()
    derecha1.OpenDoor()
    derecha2.OpenDoor()

def Button1Hit(stick=0,sticker=0,x=0,y=0,z=0,xc=0,yc=0,zc=0):
	print "Button1Hit"
	bts1.OnEnter = ""
	PushButton(1)
	sonido_clank.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def Button2Hit(stick=0,sticker=0,x=0,y=0,z=0,xc=0,yc=0,zc=0):
	print "Button2Hit"
	bts2.OnEnter = ""
	PushButton(2)
	sonido_clank.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def Button3Hit(stick=0,sticker=0,x=0,y=0,z=0,xc=0,yc=0,zc=0):
	print "Button3Hit"
	bts3.OnEnter = ""
	PushButton(3)
	sonido_clank.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def Button4Hit(stick=0,sticker=0,x=0,y=0,z=0,xc=0,yc=0,zc=0):
	print "Button4Hit"
	bts4.OnEnter = ""
	PushButton(4)
	sonido_clank.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def IniciaBotones():
  global btv1
  global btv2
  global btv3
  global btv4
  global SecActive

  bt1.Position = (313036 ,5528 ,8550)
  bt2.Position = (337420,5373,8925)
  bt3.Position = (312522,5414,-15781)
  bt4.Position = (337341, 5324, -15701)

  bts1.OnEnter = Button1Hit
  bts2.OnEnter = Button2Hit
  bts3.OnEnter = Button3Hit
  bts4.OnEnter = Button4Hit

  btv1=0
  btv2=0
  btv3=0
  btv4=0
  SecActive=0

# not optimized but quite simple!
def PushButton(val):
  global btv1
  global btv2
  global btv3
  global btv4
  global SecActive
  global LuzA

  hastahaora = (btv1==1) & (btv2==1) & (btv3==1) & (btv4==1)

  LuzA=50
  if(val==1):
    btv1=1
    bt1.Position = (311051,5539,10702)

  if(val==2):
    btv2=1
    bt2.Position = (339147,5438,10703)

  if(val==3):
    btv3=1
    bt3.Position = (310926,5458,-17419)

  if(val==4):
    btv4=1
    bt4.Position = (338987,5494,-17424)

  if((btv1==1) & (btv2==1) & (btv3==1) & (btv4==1) & (hastahaora==0)):
    # Activar Secuencia de destruccion
    SecActive=1

    Bladex.SetTriggerSectorFunc("tablilla", "OnEnter", "" )
    Bladex.SetTriggerSectorFunc("tablilla", "OnLeave", "" )

    Actions.FreeBothHands("Player1")
    cam = Bladex.GetEntity("Camera")

    Scorer.SetVisible(0)
    ScriptSkip.SkipScriptStart("BtombTablilla")
    #Bladex.DeactivateInput()
    cam.SetMaxCamera("Tablilla_btombCamera02.cam",0,210)
    cam.AddCameraEvent(-1,IniciaEscenaTablilla)
    Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-3"))
  else:
    LuzA=50

def ApagaBotones():
  global btv1
  global btv2
  global btv3
  global btv4

  bts1.OnEnter = ""
  bts2.OnEnter = ""
  bts3.OnEnter = ""
  bts4.OnEnter = ""

  bt1.Position = (311051,5539,10702)
  bt2.Position = (339147,5438,10703)
  bt3.Position = (310926,5458,-17419)
  bt4.Position = (338987,5494,-17424)
  btv1 = 1
  btv2 = 1
  btv3 = 1
  btv4 = 1

#
#  Actualiza los colores de los ojos
##########################################
def LuzOjos(intens):
  Ojo1A.SetEnergiza(intens)
  Ojo1B.SetEnergiza(intens)
  Ojo2A.SetEnergiza(intens)
  Ojo2B.SetEnergiza(intens)

  if(intens<1.5):
      _SndConcentRay.Volume     = intens/1.5
  else:
      _SndConcentTunder.Volume  = (intens-1.5)/0.5




#
# 1: Se ven los rayos. 2: No se ven
######################################
def SetRayo(i):
    rayo1.Active = i
    rayo2.Active = i
    rayo3.Active = i
    rayo4.Active = i
    rayo1.Position = 345700.0, 3081.0, -1462.0
    rayo2.Position = 345700.0, 3081.0, -5062.0
    rayo3.Position = 304300.0, 3081.0, -1462.0
    rayo4.Position = 304300.0, 3081.0, -5062.0

    if(i==1):
    	Bladex.SetTriggerSectorFunc("tablilla", "OnEnter", "" )
    	Bladex.SetTriggerSectorFunc("tablilla", "OnLeave", "" )
    	_SndConcentRay.Stop()
    	_SndConcentTunder.Stop()
    	_SndTunderRay.Play(324843.784557, 6403.39003147, -4043.70232667,0)



def PartLimber(char,idx):
	if idx == 1:
	        o = char.SeverLimb(1)
	        o.Impulse(0,-10000,0)
	if idx == 2:
	        o = char.SeverLimb(2)
	        o = o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
	if idx == 4:
	        o = char.SeverLimb(4)
	        o = o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))
	if idx == 6:
	        o = char.SeverLimb(6)
	        o = o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
	if idx == 8:
	        o = char.SeverLimb(8)
	        o = o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))


PartesRayuela = ("L_Hand","R_Hand","L_Foot","R_Foot","Head")

def ElectricShock(PersonName = "Player1",i=0):

	rayo=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt",0, 0, 0)
	per = Bladex.GetEntity(PersonName)
	rayo.Target           = per.Position
	rayo.MaxAmplitude     = 200
	rayo.MinSectorLength  = 100000
	rayo.Active           = 1
	rayo.Damage           = 0
	node = per.GetNodeIndex(PartesRayuela[i%len(PartesRayuela)])
	if node != -1:
		per.LinkToNode(rayo,node)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, per.Unlink,(rayo,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, rayo.SubscribeToList,("Pin",))

	return rayo

import whrandom

def FlickLight(luzname):

	o = Bladex.GetEntity(luzname)
	if o:
		o.Intensity   = whrandom.random()
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.05, FlickLight,(luzname,))

def Destrozator(persname="Player1"):
	pers=Bladex.GetEntity(persname)
	pers.Life = 0
	pers.Move(0,-100,0)
	pers.CastShadows = 0
	pers.LaunchAnmType("dth_n02")


	Bladex.AddScheduledFunc(Bladex.GetTime()+0.05, ElectricShock,(persname,4))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.30, ElectricShock,(persname,0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.55, ElectricShock,(persname,1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.80, ElectricShock,(persname,2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.05, ElectricShock,(persname,3))

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, PartLimber, (pers,1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.50, PartLimber, (pers,2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, PartLimber, (pers,4))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.00, PartLimber, (pers,6))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, PartLimber, (pers,8))


	luzta             = Bladex.CreateEntity("Luz2","Entity Spot",0,0,0)
	luzta.Color       = 0,255,255
	luzta.Intensity   = 1
	luzta.Precission  = 0.09
	luzta.CastShadows = 0
	luzta.SizeFactor  = 0
	luzta.Flick       = 1
	pers.Link(luzta)

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.45, pers.Unlink,(luzta,))
	FlickLight(luzta.Name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.50, luzta.SubscribeToList, ("Pin",))

#
# Timers de la trampa
##########################################
def OjoTimer(e_name, time):
  global LuzA
  global rayo1
  global rayo2
  global rayo3
  global rayo4
  global EstaAbierta
  global SecActive

  if(EstaAbierta):
    if (LuzA>200): # Muere maldito bastardo!
      char=Bladex.GetEntity("Player1")


      if(SecActive): # si se activo la secuencia...
        if (SecActive==1):
          AddRayConcentrator(326229, 3678, 14665)
          AddRayConcentrator(323626, 3599, 14615)
          SetRayo(1)
          Chisporroteo(323626, 3599, 14615)
          Chisporroteo(326229, 3678, 14665)



        if (SecActive==50):
          plat1.CloseDoor()
          plat2.OpenDoor()
          SetRayo(0)
          BreakItBaby()


        SecActive=SecActive+1
      else:
        SetRayo(1)
        rayo1.Target = char.Position
        rayo2.Target = char.Position
        rayo3.Target = char.Position
        rayo4.Target = char.Position
        Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, SetRayo, (0,))

        Destrozator("Player1")

        EstaAbierta = 0
    else:
      LuzA = LuzA+1
      LuzOjos(LuzA/100.0)

def DesOjoTimer(e_name, time):
    global LuzA

    if (LuzA>=1):
      LuzA = LuzA-1
      LuzOjos(LuzA/100.0)
    else:
      Ojo1A.Ojo.TimerFunc=""
      Ojo1A.Ojo.RemoveFromList("OjoTimer")
      _SndConcentRay.Stop()
      _SndConcentTunder.Stop()

#
## Puede arrugar...
#########################
def Arruga(triggername,entityname):
    global LuzA

    if entityname == 'Player1': ## abre la puerta y las cabezotas asesinas!
            central.CloseDoor()
            Ojo1A.Ojo.TimerFunc=DesOjoTimer
            ApagaBotones()

#
## Si pisa Kago!
#########################
def PisaTrap(triggername,entityname):
    global LuzA
    global Botones
    global LastPViewType


    if entityname=='Player1': ## abre la puerta y las cabezotas asesinas!
                central.OpenDoor()
                # Si sale no puede volver atras.
                Tachan()


                # arranca el timer
                Ojo1A.Ojo.SubscribeToList("OjoTimer")
                Ojo1A.Ojo.TimerFunc=OjoTimer

                ## Toda la secuencia de vuelta ###
                IniciaBotones()
                _SndConcentRay.Play(   324843.784557, 6403.39003147, -4043.70232667,-1)
                _SndConcentRay.Volume    = 0.0
                _SndConcentTunder.Play(324843.784557, 6403.39003147, -4043.70232667,-1)
                _SndConcentTunder.Volume = 0.0

                LastPViewType = Bladex.GetEntity("Camera").PViewType

##### Jiura! Solo pa' depura' canejo! #####
def Rayos():
	PushButton(1)
	PushButton(2)
	PushButton(3)
	PushButton(4)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abresc():

	desplazamientos=(1840, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2500)
	vel_finales=(2500.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastrescdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	MusicTool.ModifyMusicEvent("ambiente7","ambiente1")

def Cierresc():

	desplazamientos=(1840, 1000)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 5000)
	vel_finales=(5000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastrescdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def Abregol():

	desplazamientos=(1840, 1300)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2500)
	vel_finales=(2500.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastgoldin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierragol():

	desplazamientos=(1840, 1000)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 5000)
	vel_finales=(5000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastgoldin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abregol2():

	desplazamientos=(1840, 1500)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2500)
	vel_finales=(2500.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastgol2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abregol3():

	desplazamientos=(1840, 1500)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2500)
	vel_finales=(2500.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastgol3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)




def Abreinf():

	desplazamientos=(1840, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2500)
	vel_finales=(2500.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	cerradurainf.OnUnLockFunc=""


	Objects.NDisplaceObject(rastinfdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)





def Cierrax():
	if(rastrilloxdin.OnMovement == 0):
		desplazamientos=(1545, 1545, 400.0, 400.0, 100.0, 100.0)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 3000, 5000.0, 0.0, 4000.0, 0.0)
		vel_finales=(3000.0, 5000, 0.0, 4000.0, 0.0, 1000.0)
		son_iniciales=("", "")
		son_durante=(sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano)


		Objects.NDisplaceObject(rastrilloxdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)






def Abrex():

	if(abs(rastrilloxdin.obj.Position[1]-14272.233194) < 10):

		desplazamientos=(2090, 1000)
		vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
		vel_iniciales=(0.0, 2000)
		vel_finales=(2000.0, 0.0)
		son_iniciales=("", "")
		son_durante=(sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano)


		Objects.NDisplaceObject(rastrilloxdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	else:
		Cierrax()

def x1(sectorindex,entityname):


  if rastrilloxdin.obj.Position[1]<=11300 and entityname=='Player1':
    Cierrax()


def x2(sectorindex,entityname):


  if rastrilloxdin.obj.Position[1]<=11300 and entityname=='Player1':
    Cierrax()

def Abregran():

	desplazamientos=(3000, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	cerradura1.OnUnLockFunc=""
	Objects.NDisplaceObject(granrastdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abregord():

	desplazamientos=(1840, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)



	Objects.NDisplaceObject(rastgordin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	Objects.NDisplaceObject(rastgor2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def StopCameraPuertus(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	cam.SetPersonView("Player1")
	cam.Cut()

def Abreg():
	gordai.OpenDoor()
	gordad.OpenDoor()
	Abregord()
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("btomb_opendoor1Camera01.cam",0,125)
	cam.AddCameraEvent( -1,StopCameraPuertus)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-3"))
	Bladex.DeactivateInput()


def Cierrag():
	gordai.CloseDoor()
	gordad.CloseDoor()

##funcion que sube y baja el elevador

def Sube():
	elevador1.CloseDoor()
	elevador1.CloseDoor()


def Baja():
	elevador1.OpenDoor()
	elevador1.OpenDoor()





def Pisa(triggername,entityname):


    if entityname=='Player1':

	Sube()

	Bladex.RemoveTriggerSectorFunc("ascensor", "OnEnter")

def Vuelve0():

	Bladex.AddScheduledFunc(Bladex.GetTime()+15.0, Baja, ())


def Vuelve01():
	print"jajajajaja"
        Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, Bladex.SetTriggerSectorFunc,("ascensor", "OnEnter", Pisa ))

def Sube2():
	elevador2.CloseDoor()
	elevador2.CloseDoor()
	Bladex.DeactivateInput()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput,())
	MusicTool.Music2Sector("ambiente22",None)
	MusicTool.Music2Sector("ambiente24",None)

def Baja2():
	elevador2.OpenDoor()
	elevador2.OpenDoor()

def Vuelve():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, Baja2, ())

def Sube3():
	elevador3.CloseDoor()
	elevador3.CloseDoor()
	Bladex.DeactivateInput()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput,())


def Baja3():
	elevador3.OpenDoor()
	elevador3.OpenDoor()


def Abrepuen():

	desplazamientos=(2090, 1200)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastpuendin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	MusicTool.Music2Sector("ambiente30","Atmosfera5")
	MusicTool.Music2Sector("ambiente21",None)
	MusicTool.Music2Sector("ambiente22",None)
	MusicTool.Music2Sector("ambiente23",None)
	MusicTool.Music2Sector("ambiente24",None)
	MusicTool.Music2Sector("ambiente26",None)


def jiji(sectorindex,entityname):
  print "jiji"
  if entityname=='Player1':
    Abrepuen()
    sectOut.OnEnter=""
def Sube4():
	elevador4.CloseDoor()
	elevador4.CloseDoor()


def Baja4():
	elevador4.OpenDoor()
	elevador4.OpenDoor()

def Cierrala():
        if(rastladin.OnMovement == 0):
		desplazamientos=(3250, 1000)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 7000)
		vel_finales=(7000.0, 0.0)
		son_iniciales=("", "")
		son_durante=(sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano)


		Objects.NDisplaceObject(rastladin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrela():

	if(abs(rastladin.obj.Position[1]-8259.796229) < 10):
		if(rastladin.OnMovement == 0):
		        desplazamientos=(3250, 1000)
			vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
			vel_iniciales=(0.0, 4000)
			vel_finales=(4000.0, 0.0)
			son_iniciales=("", "")
			son_durante=(sonidorastrillo, sonidorastrillo)
			son_finales=("", golpemetalmediano)

			Objects.NDisplaceObject(rastladin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def bb(sectorindex,entityname):


  if rastladin.obj.Position[1]<=5259 and entityname=='Player1':
    Cierrala()


def Cierralb():
        if(rastlbdin.OnMovement == 0):
		desplazamientos=(3250, 1000)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 7000)
		vel_finales=(7000.0, 0.0)
		son_iniciales=("", "")
		son_durante=(sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano)



		Objects.NDisplaceObject(rastlbdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)




def Abrelb():

	if(abs(rastlbdin.obj.Position[1]-8381.893569) < 10):
		if(rastlbdin.OnMovement == 0):
		        desplazamientos=(3250, 1000)
			vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
			vel_iniciales=(0.0, 4000)
			vel_finales=(4000.0, 0.0)
			son_iniciales=("", "")
			son_durante=(sonidorastrillo, sonidorastrillo)
			son_finales=("", golpemetalmediano)


			Objects.NDisplaceObject(rastlbdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def bbb(sectorindex,entityname):


  if rastlbdin.obj.Position[1]<=5259 and entityname=='Player1':
    Cierralb()

def Abrexx():
	tabi.OpenDoor()
	tabd.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-3"))

def Cierraxx():
	tabi.CloseDoor()
	tabd.CloseDoor()

def Sube5():
	elevador5.CloseDoor()


def Baja5():
	elevador5.OpenDoor()

def EsperaYBajaElevadorX():
	print "mimamamemima"
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, Baja5, ())

def StopCameraInicio20(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	cam.SetPersonView("Player1")
	cam.Cut()



def Abremega(triggername,entityname):
	if entityname == "Player1":
		mega1.OpenDoor()
		mega2.OpenDoor()
		Bladex.SetTriggerSectorFunc("Abrete", "OnEnter", Cierramega )
		Bladex.SetTriggerSectorFunc("Cierrate", "OnEnter", Abremega )

def Cierramega(triggername,entityname):
	if entityname == "Player1":
		global nolohizo
		if(nolohizo):
			nolohizo=0
			#ScriptSkip.SkipScriptStart("BtombCaminante")
			Bladex.DeactivateInput()
			Actions.FreeBothHands("Player1",EscenaCaminateMegaloco,())
		else:
			mega1.CloseDoor()
			mega2.CloseDoor()
			Bladex.SetTriggerSectorFunc("Abrete", "OnEnter", Cierramega )
			Bladex.SetTriggerSectorFunc("Cierrate", "OnEnter", Abremega )



def DetenLaCamaraDeLaConchaELaLora(Camera,frame):
	import Scorer
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()

def LlegoElPersonajeYActivo(EntityName):
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)

def EscenaCaminateMegaloco():
	mega1.CloseDoor()
	mega2.CloseDoor()
	Bladex.SetTriggerSectorFunc("Abrete", "OnEnter", Cierramega )
	Bladex.SetTriggerSectorFunc("Cierrate", "OnEnter", Abremega )
	char = Bladex.GetEntity("Player1")
	# char.Position = 445623.418741, 46386.2976427, 60304.2812214       # PLAGUE: The game REALLY doesn't want the chars to
	# char.Angle = -3.14159/2                                           # cross over that one specific sector.
	# char.SetOnFloor()                                                 # also, we aren't even centered.
	# char.GoTo(467636.504179, 46535.2, 61334.3951578)

	char.Position=445900, 46395, 61310
	char.Angle = -3.14159/2
	char.SetOnFloor()
	char.GoTo(461600, 46335, 61310) # Doesn't go as far, but at least should never bug out -LeadHead

	char.RouteEndedFunc = LlegoElPersonajeYActivo
	darfuncs.LaunchMaxCamera("Entrada_fin_oasisCamera01.cam",0,200,DetenLaCamaraDeLaConchaELaLora)


def achalaymybrother():
	Bladex.SetTriggerSectorFunc("Abrete", "OnEnter", Cierramega )
	Bladex.SetTriggerSectorFunc("Cierrate", "OnEnter", Abremega )




############
############
########### ENIGMA COLUMNAS + GOLEM + BOTONES + LA MADRE QUE LO PARIO




### columnas enigma zona pre tablilla





def Abreii():
	columnaii.OpenDoor()


def Cierraii():
	columnaii.CloseDoor()


def Abreim():
	columnaim.OpenDoor()

def Cierraim():
	columnaim.CloseDoor()


def Abreis():
	columnais.OpenDoor()

def Cierrais():
	columnais.CloseDoor()


def Abredi():
	columnadi.OpenDoor()

def Cierradi():
	columnadi.CloseDoor()



def Abredm():
	columnadm.OpenDoor()

def Cierradm():
	columnadm.CloseDoor()


def Abreds():
	columnads.OpenDoor()

def Cierrads():
	columnads.CloseDoor()



### SECUENCIA PRIMERA PARTE -el jugador va saltando sobre los botones y las
######columnas se van abriendo

#######funciones enigma primera parte

def SuenaBotonx():
	cierrepiedra.Position = char.Position
	cierrepiedra.PlaySound(0)



def xdi(sectorindex,entityname):

	if entityname=='Player1':
		Abreim()
		sectxdi.OnEnter=""
		bloquedi.Move(0,180,0)
		SuenaBotonx()


def xim(sectorindex,entityname):

	if entityname=='Player1':
		Abreds()
		sectxim.OnEnter=""
		bloqueim.Move(0,180,0)
		SuenaBotonx()

def xds(sectorindex,entityname):

	if entityname=='Player1':
		Abreis()
		sectxds.OnEnter=""
		bloqueds.Move(0,180,0)
		SuenaBotonx()

def xis_(sectorindex,entityname):

	if entityname=='Player1':
		Abredm()
		sectxis_.OnEnter=""
		bloqueis.Move(0,180,0)
		SuenaBotonx()

def xdm(sectorindex,entityname):

	if entityname=='Player1':
		Abreii()
		sectxdm.OnEnter=""
		bloquedm.Move(0,180,0)
		SuenaBotonx()
		Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,FirstTaBomTrevianVerbotemEsta,())

def VuelveBotonazosX():
	bloquedi.Position=(331219.021000,15707.684000,-68142.036000)
	bloquedm.Position=(331190.287000,15707.684000,-56822.480000)
	bloqueds.Position=(331204.437000,15707.684000,-45612.243000)
	bloqueis.Position=(318795.517000,15707.684000,-45592.309000)
	bloqueim.Position=(318837.827000,15707.684000,-56889.620000)
	bloqueii.Position=(318833.028000,15707.684000,-68089.010000)

# cuando aparezca la llave
def FirstTaBomTrevianVerbotemEsta():
	VuelveBotonazosX()
	t = Bladex.GetTime()
	Bladex.AddScheduledFunc(t+2.0,Cierradi,())
	Bladex.AddScheduledFunc(t+4.0,Cierraim,())
	Bladex.AddScheduledFunc(t+6.0,Cierrads,())
	Bladex.AddScheduledFunc(t+8.0,Cierrais,())
	Bladex.AddScheduledFunc(t+10.0,Cierradm,())
	Bladex.AddScheduledFunc(t+12.0,Cierraii,())

	Bladex.AddScheduledFunc(t+18.0,ApareceLlaveDeLasPelotas,())
	VuelveBotonazosX()

import Gems
import Ontake
import Stars

def ApareceLlaveDeLasPelotas():

	Gems.SetGemColor(Gems.BLUE_GEM)
	Gems.Concentrator((325258, 10645, -39992))
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.5,CreaLLavePutadaGolem,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.5, MusicTool.LaunchMusicEvent,("sorpresa-3",))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente28",None)


def CreaLLavePutadaGolem():
	llave = Bladex.CreateEntity("LlavePutada","Llavecobox",325258, 10645, -39992,"Physic")
	llave.ExclusionGroup = 1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,llave.Impulse,(0,1,0))
	darfuncs.SetHint(llave,"Lem Key")
	Stars.Twinkle("LlavePutada")


### funciones abre y cierra puertas sopresa golem


def Abreputada():
	izquierdaprimera.OpenDoor()
	derechaprimera.OpenDoor()
	darfuncs.UnhideBadGuy("Golem2")


def segundaparteputada():
	Abredi()
	Abreim()
	Abreds()
	Abreis()
	Abredm()
	Abreii()
	sectxii.OnEnter=""
	sectxim.OnEnter=""
	sectxis_.OnEnter=""
	sectxds.OnEnter=""
	sectxdm.OnEnter=""
	sectxdi.OnEnter= x2di

def CleanPuzzSectors():
	sectxii.OnEnter =""
	sectxim.OnEnter =""
	sectxis_.OnEnter=""
	sectxds.OnEnter =""
	sectxdm.OnEnter =""
	sectxdi.OnEnter =""

def ReseteaSegundaPutada(sectorindex,entityname):
	segundaparteputada()
	ReseteaBotonazos(sectorindex,entityname)


def ReseteaBotonazosPress():
	VuelveBotonazosX()
	bloqueis.Move(0,180,0)
	bloqueim.Move(0,180,0)
	bloqueii.Move(0,180,0)
	bloqueds.Move(0,180,0)
	bloquedm.Move(0,180,0)
	bloquedi.Move(0,180,0)

def ReseteaBotonazos(sectorindex,entityname):
	VuelveBotonazosX()
	if sectorindex == sectxis_.Index:
		bloqueis.Move(0,180,0)
	elif sectorindex == sectxim.Index:
		bloqueim.Move(0,180,0)
	elif sectorindex == sectxii.Index:
		bloqueii.Move(0,180,0)
	elif sectorindex == sectxds.Index:
		bloqueds.Move(0,180,0)
	elif sectorindex == sectxdm.Index:
		bloquedm.Move(0,180,0)
	elif sectorindex == sectxdi.Index:
		bloquedi.Move(0,180,0)


def ListoParaResetar():
	sectxii.OnEnter=ReseteaSegundaPutada
	sectxim.OnEnter=ReseteaSegundaPutada
	sectxis_.OnEnter=ReseteaSegundaPutada
	sectxdi.OnEnter=ReseteaSegundaPutada
	sectxdm.OnEnter=ReseteaSegundaPutada
	sectxds.OnEnter=ReseteaSegundaPutada


def x2di(sectorindex,entityname):

	if entityname=='Player1':
		Cierradi()
		SuenaBotonx()
		ReseteaBotonazosPress()
		CleanPuzzSectors()
		Bladex.AddScheduledFunc(Bladex.GetTime()+9.0,cosox1,(sectorindex,entityname))

def cosox1(sectorindex,entityname):
		ListoParaResetar()
		sectxim.OnEnter= x2im
		sectxdi.OnEnter= None
		ReseteaBotonazos(sectorindex,entityname)

def x2im(sectorindex,entityname):

	if entityname=='Player1':
		Cierraim()
		SuenaBotonx()
		ReseteaBotonazosPress()
		Bladex.AddScheduledFunc(Bladex.GetTime()+9.0,cosox2,(sectorindex,entityname))
		CleanPuzzSectors()

def cosox2(sectorindex,entityname):
		ListoParaResetar()
		sectxds.OnEnter= x2ds
		sectxim.OnEnter= None
		ReseteaBotonazos(sectorindex,entityname)


def x2ds(sectorindex,entityname):

	if entityname=='Player1':
		Cierrads()
		SuenaBotonx()
		ReseteaBotonazosPress()
		Bladex.AddScheduledFunc(Bladex.GetTime()+9.0,cosox3,(sectorindex,entityname))
		CleanPuzzSectors()

def cosox3(sectorindex,entityname):
		ListoParaResetar()
		sectxis_.OnEnter= x2is
		sectxds.OnEnter= None
		ReseteaBotonazos(sectorindex,entityname)

def x2is(sectorindex,entityname):

	if entityname=='Player1':
		Cierrais()
		SuenaBotonx()
		ReseteaBotonazosPress()
		Bladex.AddScheduledFunc(Bladex.GetTime()+9.0,cosox4,(sectorindex,entityname))
		CleanPuzzSectors()

def cosox4(sectorindex,entityname):
		ListoParaResetar()
		sectxdm.OnEnter= x2dm
		sectxis_.OnEnter= None
		ReseteaBotonazos(sectorindex,entityname)

def x2dm(sectorindex,entityname):

	if entityname=='Player1':
		Cierradm()
		SuenaBotonx()
		ReseteaBotonazosPress()
		Bladex.AddScheduledFunc(Bladex.GetTime()+9.0,cosox5,(sectorindex,entityname))
		CleanPuzzSectors()

def cosox5(sectorindex,entityname):
		ListoParaResetar()
		sectxii.OnEnter= x2ii
		sectxdm.OnEnter= None
		ReseteaBotonazos(sectorindex,entityname)

def x2ii(sectorindex,entityname):

	if entityname=='Player1':
		Cierraii()
		SuenaBotonx()
		abresegundapuerta()
		sectxii.OnEnter= None
		ReseteaBotonazosPress()
		CleanPuzzSectors()


def abresegundapuerta():
	izquierdasegunda.OpenDoor()
	derechasegunda.OpenDoor()
	#Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera1"))
	MusicTool.Music2Sector("ambiente28",None)
