##///
##||| VOLCANO_M14/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Final door to fire golem fight can no longer be triggered multiple times.
##||| * Fire statue trap now checks for fire resistance.
##||| * Added sounds for sectors breaking in great fire sword area (arrowPuz).
##||| * Lava golem head now explodes when gem emerges (SaltanPiedritasDelGolem)
##||| * Adjusted ftDoor displacement and velocity to prevent player from softlocking themselves
##||| * Cleaned up lava golem cutscene scripts, lots of redundancy and unneeded stuff there.
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
import Room
import Button
import GotoMapVars
import ScriptSkip
import darfuncs
import MusicTool

def BorraLuz():
	volcancorona.Unlink(luz2_PP)
	luz2_PP.SubscribeToList("Pin")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para arania.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreaLlaveFX(coso):
	Cuerpo=Bladex.CreateEntity("Pegote", "Entity Particle System D1", 0, 0, 0)
	Cuerpo.ParticleType="llavemier"
	Cuerpo.Time2Live=32
	Cuerpo.PPS=128
	Cuerpo.YGravity=0
	Cuerpo.Friction=0.5
	Cuerpo.Velocity=0,0,0
	Cuerpo.RandomVelocity=50
	Cuerpo.DeathTime=Bladex.GetTime()+3.5
	coso.Link(Cuerpo)
	return Cuerpo

def musicayte():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("AranyaNegra"))
	GameText.WriteText("M14T2")

def SaltanPiedritasDelGolem(pos):
	dust.DropPiedra(pos[0], pos[1]-2000, pos[2], 40000,-20000, 40000)
	dust.DropPiedra(pos[0], pos[1]-2000, pos[2], 50000,-30000,-50000)
	dust.DropPiedra(pos[0], pos[1]-2000, pos[2],-60000,-40000, 30000)
	dust.DropPiedra(pos[0], pos[1]-2000, pos[2],-40000,-50000,-50000)
	head = finalGolem.SeverLimb(1)
	if head:
		head.SubscribeToList("Pin")
		# BoomLlave()


def Camerita():
	global arxx
	global SoundLlaveInn
	cam = Bladex.GetEntity("Camera")
	Pos = finalGolem.Position

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, SaltanPiedritasDelGolem,(Pos,))
	if arxx == 0:
		arxx = def_class.Arania(finalGolem.Position[0], 6000, finalGolem.Position[2],LlaveNegra)
		arxx.SoundLlaveInn = SoundLlaveInn
		arxx.CreaLlaveFX   = CreaLlaveFX
	else:
		arxx.Pos = (finalGolem.Position[0], 6000, finalGolem.Position[2])

	AbreCam.ResetNode()


	pos = (cam.Position[0],cam.Position[1]-5000,cam.Position[2])
	AbreCam.AddNode(pos, Pos)

	pos = (cam.Position[0],cam.Position[1]-3000,cam.Position[2])
	AbreCam.AddNode(pos, arxx.Pos)

	pos = ((cam.Position[0]+arxx.Pos[0])/2,(cam.Position[1]+arxx.Pos[1])/2,(cam.Position[2]+arxx.Pos[2])/2)
	AbreCam.AddNode(pos, arxx.Pos)

	pos = ((cam.Position[0]*3+arxx.Pos[0])/4,(cam.Position[1]*3+arxx.Pos[1])/4,(cam.Position[2]*3+arxx.Pos[2])/4)
	AbreCam.AddNode(pos, arxx.Pos)

	AbreCam.AbreCam()
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, arxx.Crea,(Pos,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, musicayte,())
	SoundLlaveOn.Position = Pos
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.8, SoundLlaveOn.PlaySound,(0,))
	SoundLlaveFUEGO.Position = char.Position
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, SoundLlaveFUEGO.PlaySound,(0,))

	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, arxx.Borra,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,ScriptSkip.SkipScriptEnd,())
	ScriptSkip.SkipScriptStart("arania")


# pata.DeathTime=Bladex.GetTime()
# Camerita(a,(4938, 494, 31092))

# pata=Bladex.CreateEntity("Brillo", "Entity Particle System D1", 0,0,0)
# pata.Position = char.Position
# pata.Time2Live=64
# pata.ParticleType="Estrellita"
# pata.PPS=64
# pata.YGravity=0
# pata.Friction=0
# pata.Velocity= 0,0,0
# pata.RandomVelocity=35

def BoomLlave():		# PLAGUE: Unused func
	wps=Bladex.CreateEntity("EfectoLlaveCool", "Entity Particle System Dobj", 0, 0, 0)
	wps.ObjectName=LlaveNegra.Name
	wps.ParticleType="DemonShield"
	wps.Time2Live=128
	wps.RandomVelocity=1.0
	wps.Velocity=-1000,0,0		# Is this supposed to actually be 0,-1000,0?
	wps.NormalVelocity=3
	wps.YGravity=0
	wps.PPS=256
	wps.DeathTime=Bladex.GetTime()+5

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para trollscene.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IniciaTrollScene():
	darfuncs.UnhideBadGuy(trollazo.Name)
	trollazo.GoTo(-42100,-9600,32600)
	AbreCam.PTS = [((-46437.1445315, -11264.511065, 45015.5177079), (-42123.4055478, -10149.4618117, 44336.2858746), 2)]
	AbreCam.AbreCam()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, char.QuickFace,(0,) )


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para rflames.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

### PLAGUE: All three funcs here end up being unused, because gfireHit is overwritten later on in the file, so commented out.
"""
def killPlayer():
	char.Life=0

def burnPlayer(x,y,z):
	char = Bladex.GetEntity("Player1")
	char.CatchOnFire(x,y,z)

def gfireHit(name,hit_entity,x,y,z,vx,vy,vz):
	global burned
	if (hit_entity=="Player1"):
		print("hit_entity:"+hit_entity+" , name:"+name)
		char = Bladex.GetEntity("Player1")
		if (char.Life<6):
			burnPlayer(x,y,z)
			Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, killPlayer, ())
		else:
			char.Life=char.Life-5
"""
##################################### lanzamiento de una llama a partir de una posicion y un destino #############

def gfire(ama,amb) :

	flame=Bladex.CreateEntity("gaFlame", "Entity Particle System D1", ama[0],ama[1],ama[2] )
	flame.ParticleType="GargFlame"
	flame.YGravity=-2400.0
	flame.Friction=0.12
	flame.PPS=250
	flame.Velocity=(amb[0]-ama[0])*8.4,(amb[1]-ama[1])*8.4,(amb[2]-ama[2])*8.4
	flame.RandomVelocity=40.0
	flame.Time2Live=21
	flame.DeathTime=Bladex.GetTime()+0.75

	return flame

def gfireA() :
	ama=-706.782000,-2214.992000,-19259.705000
	amb=294.209000,-1205.156000,-19271.135000
	flame = gfire(ama,amb)
	PSCheckerA.startCheck(flame,0.90)

def gfireB() :
	ama=-718.667000,-2021.287000,-24027.319000
	amb=-127.090000,-1268.045000,-24040.059000
	flame = gfire(ama,amb)
	PSCheckerB.startCheck(flame,0.90)

def gfireC() :
	ama=8179.589000,-600.381000,-26584.325000
	amb=8208.890000,1.357000,-25872.719000
	flame = gfire(ama,amb)
	PSCheckerC.startCheck(flame,0.90)

def gfireD() :
	ama=13003.259000,-25.820000,-26567.800000
	amb=13001.671000,1148.737000,-25722.709000
	flame = gfire(ama,amb)
	PSCheckerD.startCheck(flame,0.90)

def gfireE() :
	ama=17158.718000,204.740000,-24092.217000
	amb=16131.801000,1578.375000,-24123.553000
	flame = gfire(ama,amb)
	PSCheckerE.startCheck(flame,0.90)

def gfireF() :
	ama=17024.655000,694.751000,-18843.980000
	amb=16345.664000,1431.909000,-18799.498000
	flame = gfire(ama,amb)
	PSCheckerF.startCheck(flame,0.90)

def gfireG() :
	ama=17280.078000,1161.316000,-14279.819000
	amb=16454.231000,2099.823000,-14233.318000
	flame = gfire(ama,amb)
	PSCheckerG.startCheck(flame,0.90)

def gfireH() :
	ama=12836.790000,3951.247000,2169.814000
	amb=12846.609000,4678.739000,1586.701000
	flame = gfire(ama,amb)
	PSCheckerH.startCheck(flame,0.90)

def gfireI() :
	ama=7695.600000,4391.301000,2231.533000
	amb=7710.367000,5218.089000,1572.052000
	flame = gfire(ama,amb)
	PSCheckerI.startCheck(flame,0.90)

def gFireEven() :
	global gfperiod
	global gfstop
	gfireA()
	gfireC()
	gfireE()
	gfireG()
	gfireI()
	if (gfstop==0) : Bladex.AddScheduledFunc(Bladex.GetTime()+gfperiod, gFireEven, ())

def gFireOdd() :
	global gfperiod
	global gfstop
	gfireB()
	gfireD()
	gfireF()
	gfireH()
	if (gfstop==0) : Bladex.AddScheduledFunc(Bladex.GetTime()+gfperiod, gFireOdd, ())

def gFireStart() :
	global gfperiod
	global gfstop
	print("gfire on")
	gfstop=0
	gFireEven()
	Bladex.AddScheduledFunc(Bladex.GetTime()+(gfperiod*0.5), gFireOdd, ())

def gFireStop() :
	global gfstop
	print("gfire off")
	gfstop=1

def gFireSectorIn(sec, ent):
	if (ent=="Player1") : gFireStart()

def gFireSectorOut(sec, ent):
	if (ent=="Player1") : gFireStop()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertvol2.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AbrirP():
	puertaP.OpenDoor()
	puertaPP.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera18"))



def AbrePuerta5():
	puerta5.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))


def CierraPuerta5():
	puerta5.CloseDoor()

def Abrerast2():

	desplazamientos=(1700.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast21
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast21din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

	orc5=Bladex.GetEntity("ORC5")
	orc5.GoToJogging = 1
	orc5.Deaf=0
	orc5.Blind=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,orc5.GoTo,(34766.9433215, -1595.2633672, 32166.1452959))

	orc6=Bladex.GetEntity("ORC6")
	orc6.Deaf=0
	orc6.Blind=0



def Abrepuerta4():
	global NoSeAbrioNuncaLaPuerta
	#if(abs(puerta4din.obj.Position[1]-16514) < 10):

	desplazamientos=(1750.0, 1750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto puerta4
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	if NoSeAbrioNuncaLaPuerta:
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("inicioatm20"))
		NoSeAbrioNuncaLaPuerta = 0
	s1.OnEnter = Cierrarastfin


def Cierrapuerta4():

	desplazamientos=(1750.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto puerta4
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(puerta4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	s1.OnEnter=""


def Cierrarastfin(sectorindex,entityname):

	if entityname=='Player1':
		Cierrapuerta4()
		cerradura4.state = Locks.LOCK

def Abrepuerta4b():

	desplazamientos=(1300.0, 1300.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 500)

	#sonidos asociados a la puerta-objeto puerta4b
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta4bdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrapuerta4b():

	desplazamientos=(1300.0, 1300.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto puerta4b
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(puerta4bdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrep1():
	puerta2a.OpenDoor()
	darfuncs.UnhideBadGuy("8Lich")
	darfuncs.UnhideBadGuy("9Lich")
	darfuncs.UnhideBadGuy("9bLich")
	darfuncs.UnhideBadGuy("9cLich")


def Abrerastrag():

	desplazamientos=(2250.0, 1000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 500)

	#sonidos asociados a la puerta-objeto rastrag
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastragdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Atmosfera18"))


def CierrapuertaTEM(sectorindex,entityname):

	puertaTEM.CloseDoor()

def Abrepuerta1():

	desplazamientos=(1750.0, 1750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto puerta1
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrapuerta1():

	desplazamientos=(1750.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto puerta1
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(puerta1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbrePuertaLlaveen():
	puertaen.OpenDoor()

def CierraPuertaLlaveen(sectorindex,entityname):

	if entityname=='Player1':
		puertaen.CloseDoor()
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Combate3"))
		sen.OnEnter=""

def SigueAdelante():

	puertaTEM.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea"))

def SigueAdelante2():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2,MusicTool.LaunchMusicEvent,("Coro1",))


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=5000, -10000, 31000       # Sala de las dos palancas

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-17000, -13000, 13000		# Minotauro

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=500, -2000, -12000	# Vidrieras

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=30000, 5000, 12000		# Subterraneo1

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=6000, -10000, -88000		# Tablillas



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para lavax.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

########## final con el golem
def MakeLavita():
	vLavaDMf.CreateLava ("vLavaf" ,-6200  ,  11400 ,-152000 ,"cala2",0.025)



def SubeLavaHasta(lava,delta,hasta):
	lava.Position = lava.Position[0],lava.Position[1]-delta,lava.Position[2]
	if hasta<lava.Position[1]:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,SubeLavaHasta,(lava,delta,hasta))

### Esta funcion creara los salamanders!!!!

def subelavera():

	darfuncs.UnhideBadGuy("23Salamander")
	darfuncs.UnhideBadGuy("23bSalamander")
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Combate6"))
	MusicTool.Music2Sector("ambiente10",None)
	MusicTool.Music2Sector("ambiente11","emptyloquesea")








#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para iscene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def playerAnim():
	char = Bladex.GetEntity("Player1")
	char.Position = 99532.281, 1800.692, 8184.168
	char.Angle=3.14
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("start_volcan")
	char.SetOnFloor()

def iSceneStop(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Scorer.SetVisible(1)
	Bladex.ActivateInput()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Atmosfera19"))
	ScriptSkip.SkipScriptEnd()

def iSceneSetupCam() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("volcanCamera02.cam",0,798)
	cam.AddCameraEvent(-1,iSceneStop)

def MusicayTexto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("iniciovolcan"))
	GameText.WriteText("M14T1")

def iSceneStart() :
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	#inv.LinkBack("EscudoInvPrb1")
	#inv.LinkBack("WeaponInvPrb1")
	playerAnim()
	iSceneSetupCam()

	MusicayTexto()
	ScriptSkip.SkipScriptStart("inicio")


def ParchePrecarga():
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	AuxFuncs.FadeFrom(4,5.1)

	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, iSceneStart, ())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para hurryup.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def hpTurnOnTheLights():
	luzSL1=Bladex.CreateEntity("LuzSL1","Entity Spot",-50630,4748,25500)
	luzSL1.Color=255,100,50
	luzSL1.Intensity=19.0
	luzSL1.CastShadows=0
	luzSL1.Precission=0.06
	luzSL1.Visible=0
	#luzSL1.Flick=0

	luzSL2=Bladex.CreateEntity("LuzSL2","Entity Spot",-36900,3750,29219)
	luzSL2.Color=255,100,50
	luzSL2.Intensity=19.0
	luzSL2.CastShadows=0
	luzSL2.Precission=0.03
	luzSL2.Visible=0
	#luzSL2.Flick=0

def hpFloodTimer(ent,time):
	time = Bladex.GetTime()
	elapsedtime = time-hpLavaFloodStartTime
	hpLavaFloodLevel=hpLavaStart+((hpLavaStop-hpLavaStart)/hpLavaFloodTime)*elapsedtime
	hpLava.Position=hpLavaPosition[0],hpLavaFloodLevel,hpLavaPosition[1]

	#hlavasubelooper.Position = hpLavaPosition[0],hpLavaFloodLevel,hpLavaPosition[1]

	if (elapsedtime>hpLavaFloodTime) :
		hpLava.TimerFunc=""
		hpLava.RemoveFromList("hpFlood")
		hlavasubelooper.StopSound()


def hpStartFlood():
	global hpLavaFloodStartTime
	hpLava.TimerFunc=hpFloodTimer
	hpLava.SubscribeToList("hpFlood")
	hpLavaFloodStartTime=Bladex.GetTime()

	hlavasubelooper.Position = -55175,6219, 25799
	hlavasubelooper.PlaySound(-1)


def hpDust(name,p1,p2,p3):
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

def hpBreakFloor(trsector,entity):
	global hpFloorBroken
	if (hpFloorBroken) : return
	if (entity<>"Player1") : return

	hpSector.DoBreak((0,2,0),(-36000,-1500,31000),(0,30,0))
	a=-37500,-2400,33250
	b=-34750,-2400,33250
	c=-37500,-2400,29000
	d=-34750,-2400,29000
	hpDust("hpDust1",a,b,c)
	hpDust("hpDust2",c,b,d)
	hpFloorBroken=1

	hderrumbamiento.Position = -36000,-1500,31000
	hderrumbamiento.PlaySound(0)

def hpSubeElevador():
	global hpElevadorArriba

	if (hpElevadorArriba) : return
	hpElevadorArriba=1

	hpcolumnaelevador.closetype=Doors.AC_UNIF_DEC
	hpcolumnaelevador.c_init_vel=0
	hpcolumnaelevador.c_init_displ=325
	hpcolumnaelevador.c_med_vel=300
	hpcolumnaelevador.c_med_displ=6000
	hpcolumnaelevador.c_end_vel=1000
	hpcolumnaelevador.c_end_displ=325
	hpcolumnaelevador.SetWhileCloseSound(hploopelevador)
	hpcolumnaelevador.SetEndCloseSound(hpgolpeelevador)
	hpcolumnaelevador.CloseDoor()
	MusicTool.Music2Sector("ambiente3","Atmosfera18")

	hpStartFlood()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para generadores.py     **************************
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
	v=AuxFuncs.Normalize(v)
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


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para gargolas.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DropPiedrita():
	r=whrandom.randint(-4000,4000)
	return dust.DropPiedra(5843+r, 8893, 48670,-r*15,-140000,whrandom.randint(-6000,6000))

# Func now checks for fire resistance.	-LeadHead
def gfireHit(name,hit_entity,x,y,z,vx,vy,vz,a9=0,a10=0,a11=0,a12=0,a13=0,a14=0,a15=0,a16=0,a18=0):
	global killed
	global GARGULUS_FIRE_DAMAGE
	if (hit_entity=="Player1"):
		#print("hit_entity:"+hit_entity+" , name:"+name)
		char = Bladex.GetEntity("Player1")
		res = (1.0 - char.Data.GetResistance("Fire"))
		if (char.Life<GARGULUS_FIRE_DAMAGE+1):
			if (not killed) :
				killed=1
				char.Life = 0
				Actions.FireDeath("Player1")
		else:
			ttlDamage = (GARGULUS_FIRE_DAMAGE * res)
			
			# If resistance does not counteract all damage, also generate smoke
			if ttlDamage:
				char.Life= char.Life - ttlDamage
				# print "inflicting " + `ttlDamage`
				
				smoke=Bladex.CreateEntity("FireballSmoke", "Entity Particle System D1", x, y, z)
				smoke.ParticleType="DarkSmoke"
				smoke.YGravity=-3000.0
				smoke.Friction=0.05
				smoke.PPS=12
				smoke.Velocity=0.0, -90.0, 0.0
				smoke.RandomVelocity=7.0
				smoke.DeathTime=Bladex.GetTime()+0.5
				node= 0
				char.LinkToNode(smoke,node)


##################################### lanzamiento de una llama a partir de una posicion y un destino #############
def cuadraduchi(c):
	return c*c

def sqrDistancia(pos1,pos2):
	return cuadraduchi(pos1[0]-pos2[0])+cuadraduchi(pos1[1]-pos2[1])+cuadraduchi(pos1[2]-pos2[2])

def PlayFogonazo(pos):
	global _SndFogonazoPos

	if sqrDistancia(pos,char.Position)-sqrDistancia(_SndFogonazoPos,char.Position) <10 :
		_SndFogonazoPos = pos
		_SndFogonazo.Stop()
		_SndFogonazo.Play(pos[0],pos[1],pos[2],0)



def gfire(ama,amb,i,p,r,gaz) :

	flame=Bladex.CreateEntity("gaFlame", "Entity Particle System D1", ama[0],ama[1],ama[2] )
	PlayFogonazo((ama[0],ama[1],ama[2]))

	if (gaz) :
		flame.ParticleType="GargFlame"
	else :
		flame.ParticleType="Hoguera"
	flame.YGravity=-2400.0
	flame.Friction=0.12
	flame.PPS=p
	flame.Velocity=(amb[0]-ama[0])*i,(amb[1]-ama[1])*i,(amb[2]-ama[2])*i
	flame.RandomVelocity=r
	flame.Time2Live=21
	flame.DeathTime=Bladex.GetTime()+0.75

	return flame

def gfireA() :
	ama=-706.782000,-2214.992000,-19259.705000
	amb=294.209000,-1205.156000,-19271.135000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerA.startCheck(flame,0.90)

def gfireB() :
	ama=-718.667000,-2021.287000,-24027.319000
	amb=-127.090000,-1268.045000,-24040.059000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerB.startCheck(flame,0.90)


def gfireC() :
	ama=8179.589000,-600.381000,-26584.325000
	amb=8208.890000,1.357000,-25872.719000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerC.startCheck(flame,0.90)

def gfireD() :
	ama=13003.259000,-25.820000,-26567.800000
	amb=13001.671000,1148.737000,-25722.709000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerD.startCheck(flame,0.90)

def gfireE() :
	ama=17158.718000,204.740000,-24092.217000
	amb=16131.801000,1578.375000,-24123.553000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerE.startCheck(flame,0.90)

def gfireF() :
	ama=17024.655000,694.751000,-18843.980000
	amb=16345.664000,1431.909000,-18799.498000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerF.startCheck(flame,0.90)

def gfireG() :
	ama=17280.078000,1161.316000,-14279.819000
	amb=16454.231000,2099.823000,-14233.318000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerG.startCheck(flame,0.90)

def gfireH() :
	ama=12836.790000,3951.247000,2169.814000
	amb=12846.609000,4678.739000,1586.701000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerH.startCheck(flame,0.90)


def gfireI() :
	ama=7695.600000,4391.301000,2231.533000
	amb=7710.367000,5218.089000,1572.052000
	flame = gfire(ama,amb,8.4,250,40.0,1)
	PSCheckerI.startCheck(flame,0.90)


##################################### fire timing control #############

def gFireEven() :
	global gfperiod
	global gfstop
	global _SndFogonazoPos
	gfireA()
	gfireC()
	gfireE()
	gfireG()
	gfireI()
	if (gfstop==0) : Bladex.AddScheduledFunc(Bladex.GetTime()+gfperiod, gFireEven, ())
	_SndFogonazoPos = 0,0,0

def gFireOdd() :
	global gfperiod
	global gfstop
	global _SndFogonazoPos
	gfireB()
	gfireD()
	gfireF()
	gfireH()
	if (gfstop==0) : Bladex.AddScheduledFunc(Bladex.GetTime()+gfperiod, gFireOdd, ())
	_SndFogonazoPos = 0,0,0

def gFireStart() :
	global gfperiod
	global gfstop
	#print("gfire on")
	gfstop=0
	gFireEven()
	Bladex.AddScheduledFunc(Bladex.GetTime()+(gfperiod*0.5), gFireOdd, ())

def gFireStop() :
	global gfstop
	#print("gfire off")
	gfstop=1

def gFireSectorIn(sec, ent):
	if (ent=="Player1") : gFireStart()

def gFireSectorOut(sec, ent):
	if (ent=="Player1") : gFireStop()

def fosoFireA() :
	global generator
	global fosofirestop
	global fosofireperiod

	#print("flameA")

	i = generator.random()*1.2
	r = generator.randint(-500,500)
	ama=2500+r,10000,47500
	amb=2500+r,-500,47500
	flame = DropPiedrita()[1]
	PSCheckerFosoA.startCheck(flame,20.0)

	p = generator.random()*1.0
	if (not fosofirestop) :
		Bladex.RemoveScheduledFunc("fosoFireA")
		Bladex.AddScheduledFunc(Bladex.GetTime()+fosofireperiod+p, fosoFireA, (),"fosoFireA")


def fosoFireB() :
	global generator
	global fosofirestop
	global fosofireperiod

	#print("flameB")

	i = generator.random()*1.2
	r = generator.randint(-2000,2000)
	ama=5850+r,10000,47500
	amb=5850+r,-500,47500
	flame = DropPiedrita()[1]
	PSCheckerFosoB.startCheck(flame,20.0)

	p = generator.random()*1.0
	if (not fosofirestop) :
		Bladex.RemoveScheduledFunc("fosoFireB")
		Bladex.AddScheduledFunc(Bladex.GetTime()+fosofireperiod+p, fosoFireB, (),"fosoFireB")

def fosoFireC() :
	global generator
	global fosofirestop
	global fosofireperiod

	#print("flameC")

	i = generator.random()*1.2
	r = generator.randint(-500,500)
	ama=9250+r,10000,47500
	amb=9250+r,-500,47500
	flame = DropPiedrita()[1]
	PSCheckerFosoC.startCheck(flame,20.0)

	p = generator.random()*1.0
	if (not fosofirestop) :
		Bladex.RemoveScheduledFunc("fosoFireB")
		Bladex.AddScheduledFunc(Bladex.GetTime()+fosofireperiod+p, fosoFireC, (),"fosoFireB")

def fosoFire() :
	global generator
	global fosofireperiod
	pA = generator.random()*fosofireperiod
	pB = generator.random()*fosofireperiod
	pC = generator.random()*fosofireperiod
	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time+fosofireperiod+pA, fosoFireA, ())
	Bladex.AddScheduledFunc(time+fosofireperiod+pB, fosoFireB, ())
	Bladex.AddScheduledFunc(time+fosofireperiod+pC, fosoFireC, ())

def fosoFireSectorIn(sec, ent) :
	global fosofirestop
	#print("foso fire on")
	fosofirestop=0
	fosoFire()

def fosoFireSectorOut(sec, ent) :
	global fosofirestop
	#print("foso fire off")
	fosofirestop=1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para fourLDS.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ftDead(ent_name):
	demonio=Bladex.GetEntity(ent_name)
	demonio.Data.ImDeadFunc (ent_name)
	global ldsDeads;
	ldsDeads=ldsDeads+1
	if (ldsDeads==2):
		ftOpenDoors()
		SigueAdelante2()

def ftBuildDemonTimer( ent, time ):
	dem=Bladex.GetEntity(ent)
	dem.Alpha=dem.Alpha+0.007
	if dem.Alpha>=1.0:
		dem.Alpha=1.0
		dem.RemoveFromList("Timer60")
		dem.TimerFunc=""

def ftBuildDemonLightFadeOutTimer( ent, time ):
	demonFireLight=Bladex.GetEntity(ent)
	demonFireLight.Intensity=demonFireLight.Intensity-0.1
	if (demonFireLight.Intensity<0.0) :
		demonFireLight.Intensity=0.0
		demonFireLight.RemoveFromList("Timer60")
		demonFireLight.TimerFunc=""
		print("nolight")

def ftBuildDemonLightFadeOut(light):
	demonFireLight.TimerFunc=ftBuildDemonLightFadeOutTimer
	demonFireLight.SubscribeToList("Timer60")

def ftBuildDemonLightFadeInTimer( ent, time ):
	demonFireLight=Bladex.GetEntity(ent)
	demonFireLight.Intensity=demonFireLight.Intensity+0.05
	if (demonFireLight.Intensity>17.0) :
		print("fadeout")
		demonFireLight.TimerFunc=ftBuildDemonLightFadeOutTimer
		Bladex.AddScheduledFunc( Bladex.GetTime()+3.0, ftBuildDemonLightFadeOut, (demonFireLight,) )

def ftBuildDemonLightFadeIn(light):
	demonFireLight.TimerFunc=ftBuildDemonLightFadeInTimer
	demonFireLight.SubscribeToList("Timer60")

def ftBuildDemonExplode(n, v1):
	print("explode")
	demonExp=Bladex.CreateEntity("demonExp", "Entity Particle System D1", v1[0], v1[1], v1[2])
	demonExp.ParticleType="ftManuelChispa"
	demonExp.YGravity=0.0
	demonExp.Friction=0.1
	demonExp.PPS=4000
	demonExp.Velocity=0.0, 0.0, 0.0
	demonExp.RandomVelocity=90.0
	demonExp.Time2Live=40
	demonExp.DeathTime=Bladex.GetTime()+0.2


def ftBuildDemonFire( n, v1 ):
	demonFire=Bladex.CreateEntity(n, "Entity Particle System D3", v1[0]-150.0, v1[1], v1[2]-150.0)
	demonFire.D1=300, 0, 0
	demonFire.D2=150, 0, 170
	demonFire.ParticleType="ftManuelFire"
	demonFire.PPS=60
	demonFire.YGravity=0.0
	demonFire.Friction=0.0
	demonFire.Velocity=0.0, -50.0, 0.0
	demonFire.RandomVelocity=20.0
	demonFire.Time2Live=30.0
	demonFire.DeathTime=Bladex.GetTime()+6.0

	"""
	demonFireLight=Bladex.CreateEntity(n+"light", "Entity Spot", v1[0], v1[1]-3000, v1[2])
	demonFireLight.Color=250, 50, 40
	demonFireLight.Intensity=0.0
	demonFireLight.Precission=0.03125
	demonFireLight.Visible=0
	demonFireLight.CastShadows=0

	demonFireLight.Intensity=10.0         #test
	Bladex.AddScheduledFunc( Bladex.GetTime()+8.0, ftBuildDemonLightFadeOut, (demonFireLight,) )
	"""
	#ftBuildDemonLightFadeIn(demonFireLight)

def ftBuildDemon( demonN ):
	if (demonN==0) :
		ang=2.19939587242
		dem=demA
		x=(20974+22171)/2; y=-5550; z=(-101681-97728)/2
	elif (demonN==2) :
		ang=4.41041027288
		dem=demC
		x=(-11135-9938)/2; y=-5550.2; z=(-101681-97728)/2
	else :
		print("Eres tonto o eres listo??... no hay tantos demonios")
		return

	dem.Position=x,y,z
	dem.Angle=ang
	dem.Alpha=0.0
	dem.RasterMode="Full"
	dem.ImDeadFunc=ftDead
	dem.TimerFunc=ftBuildDemonTimer
	dem.SubscribeToList("Timer60")
	darfuncs.UnhideBadGuy(dem.Name)
	dem.Blind = 1
	dem.Deaf  = 1
	dem.LaunchAnimation("Ldm_appears")
	dem.SetOnFloor()
	RugidoDemonio.Position = (x,y,z)
	FireBallCool.Position  = (x,y,z)

	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, RugidoDemonio.PlaySound,(0,))
	FireBallCool.PlaySound(0)

	ftBuildDemonFire(dem.Name+"fire", (dem.Position[0], dem.Position[1], dem.Position[2]) )
	Bladex.AddScheduledFunc( Bladex.GetTime()+5.1, ftBuildDemonExplode, (dem.Name+"expl", dem.Position) )

def ftWakeUpDemons() :
	demA.Blind=0; demA.Deaf=0
	demC.Blind=0; demC.Deaf=0

def ftSceneProtaPosition():
	char = Bladex.GetEntity("Player1")
	char.Position=6596,-5046.8,-96401
	char.Angle=3.14

def ftSceneProtaAnim():
	char = Bladex.GetEntity("Player1")
	char.Angle = 3.14159
	char.Position = (5988.00928756, -5345.51067262, -96959.8349711)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("aparecen_4_demonios")
	char.SetOnFloor()

def ftSceneRestoreCamera(ent,frame):
	print("restoreCamera")
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	ftWakeUpDemons()
	ScriptSkip.SkipScriptEnd()

def ftSceneCamC(ent,frame):
	print("camc")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Kgt_aparecen_4_demoniosCamera03.cam",273,376)
	cam.AddCameraEvent(-1,ftSceneRestoreCamera)

def ftSceneCamB(ent,frame):
	print("camb")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Kgt_aparecen_4_demoniosCamera02.cam",160,273)
	cam.AddCameraEvent(-1,ftSceneCamC)
	ftSceneProtaAnim()

def ftSceneCamA():
	print("cama")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Kgt_aparecen_4_demoniosCamera01.cam",0,160)
	cam.AddCameraEvent(-1,ftSceneCamB)
	Scorer.SetVisible(0)

def ftSceneStart(index, ent):
	global ftSceneStarted
	if (ent<>"Player1") : return
	if (ftSceneStarted) : return
	ftSceneStarted=1
	ftSceneProtaPosition()
	ftSceneCamA()
	Bladex.AddScheduledFunc( Bladex.GetTime()+12.7, ftBuildDemon, (0,) )
	Bladex.AddScheduledFunc( Bladex.GetTime()+12.2, ftBuildDemon, (1,) )
	Bladex.AddScheduledFunc( Bladex.GetTime()+4.0, ftBuildDemon, (2,) )
	Bladex.AddScheduledFunc( Bladex.GetTime()+5.5, ftBuildDemon, (3,) )
	ScriptSkip.SkipScriptStart("fourLDS")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate1"))


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para final.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def GreatQuake(x,y):
	SoundQuake.Position = char.Position
	SoundQuake.PlaySound(0)

def GreatClank(x,y):
	SoundClank.Position = char.Position
	SoundClank.PlaySound(0)

def GreatBrum(x,y):
	SoundBrum.Position = char.Position
	SoundBrum.PlaySound(0)

###########################################################################################################################
def GreatRokus(Pos):
	SoundRokus.Position = Pos
	SoundRokus.PlaySound(0)

def GreatCrash(Pos):
	SoundCrash.Position = Pos
	SoundCrash.PlaySound(0)

def TruchOnFireTimer(ent,Time):
	fire = Bladex.GetEntity(ent+"Fuego")
	if fire:
		fire.Position = Bladex.GetEntity(ent).Position
	else:
		Bladex.GetEntity(ent).RemoveFromList("Timer30")

def TruchOnFire(Piedra,Time=10,Size=35,PPS=128):
	Fuego=Bladex.CreateEntity(Piedra.Name+"Fuego", "Entity Particle System D1", 0,0,0)
	Fuego.ParticleType="LavaFire"
	Fuego.PPS=PPS
	Fuego.YGravity=1000
	Fuego.Friction=0.1
	Fuego.Velocity=0,0,0
	Fuego.RandomVelocity=Size
	Fuego.Time2Live=32
	Fuego.DeathTime=Bladex.GetTime()+Time
	Piedra.SubscribeToList("Timer30")
	Piedra.TimerFunc=TruchOnFireTimer









def ftOpenDoors():
	ftDoorA.opentype=Doors.AC_UNIF_DEC
	ftDoorA.o_init_vel=0	; ftDoorA.o_init_displ=300
	ftDoorA.o_med_vel=-1000 ; ftDoorA.o_med_displ=3000
	ftDoorA.o_end_vel=0		; ftDoorA.o_end_displ=380
	ftDoorA.SetWhileOpenSound(puertapiedrai)
	ftDoorA.SetEndOpenSound(finpuertapiedrai)
	ftDoorA.OpenDoor()

	ftDoorB.opentype=Doors.AC_UNIF_DEC
	ftDoorB.o_init_vel=0	; ftDoorB.o_init_displ=300
	ftDoorB.o_med_vel=-1000 ; ftDoorB.o_med_displ=3000
	ftDoorB.o_end_vel=0		; ftDoorB.o_end_displ=380
	ftDoorB.SetWhileOpenSound(puertapiedrad)
	ftDoorB.SetEndOpenSound(finpuertapiedrad)
	ftDoorB.OpenDoor()

def ftCloseDoors():
	ftDoorA.closetype=Doors.AC_UNIF_DEC
	ftDoorA.c_init_vel=0	; ftDoorA.c_init_displ=380
	ftDoorA.c_med_vel=1200 ; ftDoorA.c_med_displ=3000
	ftDoorA.c_end_vel=0	; ftDoorA.c_end_displ=385
	ftDoorA.SetWhileCloseSound(puertapiedrai)
	ftDoorA.SetEndCloseSound(finpuertapiedrai)
	ftDoorA.CloseDoor()

	ftDoorB.closetype=Doors.AC_UNIF_DEC
	ftDoorB.c_init_vel=0	; ftDoorB.c_init_displ=380
	ftDoorB.c_med_vel=1200 ; ftDoorB.c_med_displ=3000
	ftDoorB.c_end_vel=0	; ftDoorB.c_end_displ=385
	ftDoorB.SetWhileCloseSound(puertapiedrad)
	ftDoorB.SetEndCloseSound(finpuertapiedrad)
	ftDoorB.CloseDoor()

###########################################################################################################################
###########################################                                    ############################################
###########################################	          C A M A R A S            ############################################
###########################################                                    ############################################
###########################################################################################################################

################# primera secuencia
def eSecOnEnter(index,ent) :
	global eSecEntered
	if (ent!="Player1") or (eSecEntered==1): return
	# print("close")
	eSecEntered = 1 						# Added 
	ftDoorB.OnEndOpenFunc=ftCloseDoors 		#		-LeadHead
	ftCloseDoors()

def eSceneCameraRestore(ent,frame):
	print("eSceneCameraRestore()")
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	char.Angle = 0.2
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	stoneFalse.SubscribeToList("Pin")
	ScriptSkip.SkipScriptEnd()
	fStopAnimGolem()

def eSceneCameraC(ent,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Geoda_golemCamera05.cam",0,143)
	cam.AddCameraEvent(55,fGolemAppears)
	cam.AddCameraEvent(-1,eSceneCameraRestore)
	eSceneStoneAnimStop()
	fAnimGolemBall()
	fTurnOnGolemBall()

def eSceneCameraB(ent,frame):
	print("eSceneCameraB()")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("rotura_volcanCamera04.cam",192,291)
	cam.AddCameraEvent(1,GreatBrum)
	cam.AddCameraEvent(-1,eSceneCameraC)

def eSceneCameraA():
	print("eSceneCameraA()")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("rotura_volcanCamera01.cam",0,192)
	cam.AddCameraEvent(140,GreatQuake)
	cam.AddCameraEvent(160,GreatClank)
	cam.AddCameraEvent(-1,eSceneCameraB)

def eSceneStoneAnim():
	print("eSceneStoneAnim()")
	stone = Bladex.GetEntity("lavaStone")
	stone.Actor=1
	stone.Animation="Sct_cae"
	stone.FPS=20.0
	stone.SendSectorMsgs=0
	stone.TurnOn()

### PLAGUE: Func is unused in the map, since the animation doesn't exist.
"""
def eSceneStoneAnimLoop():
	print("eSceneAnimLoop()")
	stone = Bladex.GetEntity("lavaStone")
	stone.Animation="Sct_ondula"
"""

def eSceneStoneAnimStop():
	print("eSceneAnimStop()")
	CambiazoBerreta()

def CambiazoBerreta():
	Bladex.GetEntity("lavaStone").SubscribeToList("Pin")
	Bladex.GetSector(7000,15000,-140000).Active = 0

def HellSpawDeath(ent_name):
	Camerita()
	finalGolem.Data.ImDeadFunc (ent_name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(35,))

def fCreateGolem(pos) :
	finalGolem.Position = pos[0],pos[1]+1000,pos[2]
	finalGolem.Angle = -3.14159

def fTurnOnGolem():
	finalGolem.CatchOnFire(finalGolem.Position[0],finalGolem.Position[1],finalGolem.Position[2])

def fStopAnimGolem(a=0,b=0,c=0):
	finalGolem.Blind = 0
	finalGolem.Deaf  = 0
	print "Pegado al suelo"
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, finalGolem.SetOnFloor,() )

def fAnimGolem() :
	finalGolem.Wuea = Reference.WUEA_ENDED
	finalGolem.SetTmpAnmFlags(1,1,1,0,5,1,0)
	finalGolem.LaunchAnimation("Glm_awake")



def fCreateGolemBall(pos) :
	geodaTocha.Position = pos

def fTurnOnGolemBall() :
	pass
	#geodaTocha.CatchOnFire(geodaTocha.Position[0],geodaTocha.Position[1],geodaTocha.Position[2])
	#TruchOnFire(geodaTocha,7,85,256)

def fTurnOffGolemBall(pos) :
	pass

def SaltanPiedritas(pos):
	dust.DropPiedra(pos[0], pos[1], pos[2], 40000,-70000, 40000)
	dust.DropPiedra(pos[0], pos[1], pos[2], 50000,-50000,-50000)
	dust.DropPiedra(pos[0], pos[1], pos[2],-60000,-60000, 30000)
	dust.DropPiedra(pos[0], pos[1], pos[2],-40000,-40000,-50000)


def fAnimGolemBall() :
	pos = -5412.1, 17822.2, -126512.6
	GreatRokus(pos)
	fCreateGolemBall(pos)
	geodaTocha.Actor=1
	geodaTocha.Animation="Geo_jump"
	geodaTocha.FPS=20.0
	geodaTocha.SendSectorMsgs=0
	geodaTocha.TurnOn()
	dust.DropPiedra(-5412.1, 11022.2, -126512.6,20000,-220000,-20000)
	dust.DropPiedra(-5000.1, 11022.2, -126000.6,22000,-240000,-19000)
	dust.DropPiedra(-5999.1, 11022.2, -126000.6,19000,-200000,-17000)

def fStopGolemBallAnim() :
	geodaTocha.TurnOff()
	geodaTocha.Actor=0
	geodaTocha.Position = 3278.0, 9800.0, -131497.0

def fDeleteGolemBall() :
	geodaTocha.SubscribeToList("Pin")
	geodaTocha.RemoveFromWorld()

def fCreateGolemBallRota(pos) :
	geodaTrozoA.Position = pos[0]-131.3	, pos[1]-60.9	,	pos[2]+701.6
	geodaTrozoB.Position = pos[0]-71.6	, pos[1]-517.3	,	pos[2]+51.4
	geodaTrozoC.Position = pos[0]+329.7	, pos[1]+88.3	,	pos[2]-83.4
	geodaTrozoD.Position = pos[0]-219.1	, pos[1]+253.4	,	pos[2]+362.2
	geodaTrozoE.Position = pos[0]-134.8	, pos[1]+64.8	,	pos[2]-686.6


def RescalePiece(obj_name,Size):
	pieza = Bladex.GetEntity(obj_name)
	if Size<=0.01:
		pieza.SubscribeToList("Pin")
		return
	pieza.Scale = Size
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.1, RescalePiece,(obj_name, Size-0.05) )


def DestroyPiece(obj_name):
	pieza=Bladex.GetEntity(obj_name)
	x,y,z =  pieza.Position
	if pieza:
		Fuego=Bladex.CreateEntity(obj_name+"Smoken", "Entity Particle System D1", x,y,z)
		Fuego.ParticleType="DarkSmoke"
		Fuego.PPS=22
		Fuego.YGravity=0
		Fuego.Friction=0.0
		Fuego.Velocity=0,-500,0
		Fuego.RandomVelocity=5.0
		Fuego.Time2Live=96
		Fuego.DeathTime=Bladex.GetTime()+1.5
		RescalePiece(obj_name,pieza.Scale)

def fAnimGolemBallRota() :
	m=250.0
	geodaTrozoA.Impulse( -131.3*m, -60.9 *m, +701.6*m )
	geodaTrozoB.Impulse( -71.6 *m, -517.3*m, +51.4 *m )
	geodaTrozoC.Impulse( +329.7*m, +88.3 *m, -83.4 *m )
	geodaTrozoD.Impulse( -219.1*m, +253.4*m, +362.2*m )
	geodaTrozoE.Impulse( -134.8*m, +64.8 *m, -686.6*m )
	geodaTrozoA.OnStopFunc=DestroyPiece
	geodaTrozoB.OnStopFunc=DestroyPiece
	geodaTrozoC.OnStopFunc=DestroyPiece
	geodaTrozoD.OnStopFunc=DestroyPiece
	geodaTrozoE.OnStopFunc=DestroyPiece


	#Bladex.AddScheduledFunc( Bladex.GetTime()+0.5, ftSectorABreak, () )

def fTurnOffGolemBallRota(pos) :
	pass

def GolemTocho(geodaTochaPosition):
	fCreateGolem(geodaTochaPosition)
	fAnimGolem()
	fTurnOnGolem()

def fGolemAppears(cam,frame):
	fStopGolemBallAnim()
	fCreateGolemBallRota(geodaTocha.Position)
	SaltanPiedritas(geodaTocha.Position)
	GreatCrash(geodaTocha.Position)
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.0, GolemTocho,(geodaTocha.Position,) )
	fDeleteGolemBall()
	fAnimGolemBallRota()
	finalGolem.UnFreeze()
	finalGolem.PutToWorld()

###########################################################################################################################
###########################################                                    ############################################
###########################################	      P R O T A G O N I S T A      ############################################
###########################################                                    ############################################
###########################################################################################################################

### PLAGUE: This func is useless.
def eSceneProtPosition():
	print("eSceneProtPosition()")
	char = Bladex.GetEntity("Player1")
	char.Position=6422.1,-1099.1,-147752.9
	char.Angle=3.14

def eSceneProtAnim():
	print("eSceneProtAnim()")
	char = Bladex.GetEntity("Player1")
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.Wuea = Reference.WUEA_ENDED
	char.Position=6422.1,-1099.1,-147752.9
	char.Angle = 3.14159					# For reasons I cannot figure out, the angle is actually never initialized properly.
	char.LaunchAnmType("cae_lava")

###########################################################################################################################
###########################################                                    ############################################
###########################################	            L A U N C H            ############################################
###########################################                                    ############################################
###########################################################################################################################

def eSceneStart1(sec, ent):
	
	print("eSceneStart()")
	eSceneCameraA()
	eSceneProtAnim()
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.0, eSceneStoneAnim,())
	# ftSectorsBreak()			# PLAGUE: Func is commented out and never actually defined
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)

def eSceneStart(sec, ent):
	Bladex.SetTriggerSectorFunc("muere", "OnEnter", "" )
	ScriptSkip.SkipScriptStart("final")

	Bladex.AddScheduledFunc( Bladex.GetTime()+0.0, eSceneStart1,(sec, ent))


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def fastGoTo(entName,x,y,z):
	p =Bladex.GetEntity(entName)
	p.GoToJogging = 1
	p.GoTo(x,y,z)

"""
def x1(sectorindex,entityname):

	if entityname=='Player1':
		pers=Bladex.GetEntity("5ORC")
		pers.GoToJogging = 1
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(34766.9433215, -1595.2633672, 32166.1452959))
		sectx1.OnEnter=""
"""

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def x7(sectorindex,entityname):
	if entityname=='Player1':
		GoToMul("7Kngt")
		sectx7.OnEnter=""

def kavayeros2blabla():
	GoToMul("10Kngt")
	GoToMul("11Kngt")

def x2(sectorindex,entityname):
	if entityname=='Player1':
		kavayeros2blabla()
		sectx2.OnEnter=""


def x3(sectorindex,entityname):
	if entityname=='Player1':
		GoToMul("13Zombi")
		sectx3.OnEnter=""

def activakeletos():
	darfuncs.UnhideBadGuy("16Esq")
	darfuncs.UnhideBadGuy("17Esq")
	darfuncs.UnhideBadGuy("18Esq")





def x15(sectorindex,entityname):
	if entityname=='Player1':
		fastGoTo("20Kngt",15915.25056, 4275.2649472, -447.241534481)
		sectx15.OnEnter=""


def x5(sectorindex,entityname):
	if entityname=='Player1':
		GoToMul("22Kngt")
		sectx5.OnEnter=""

def TerminanLasMuertes1():
	sectx6=Bladex.GetSector(33854.9106369, 1387.76612009, -25371.1894891)
	sectx6.OnEnter=x6

def KreaLichs():
	darfuncs.UnhideBadGuy("29Lich")
	darfuncs.UnhideBadGuy("30Lich")
	darfuncs.UnhideBadGuy("31Lich")


def x6(sectorindex,entityname):
	if entityname=='Player1':
		KreaLichs()
		sectx6=Bladex.GetSector(33854.9106369, 1387.76612009, -25371.1894891)
		sectx6.OnEnter=""

def Skelpas():
	pers = Bladex.GetEntity("32Esq")
	darfuncs.EnciendeEnLlamas(pers,1,0.1)


def x8(sectorindex,entityname):
	if entityname=='Player1':
		darfuncs.UnhideBadGuy("32Esq")
		darfuncs.UnhideBadGuy("33Esq")
		GoToMul("32Esq")
		Skelpas()
		sectx8.OnEnter=""

def x9(sectorindex,entityname):
	if entityname=='32Esq':
		GoToMul("33Esq")
		sectx9.OnEnter=""


def zombisenaccion():
	darfuncs.UnhideBadGuy("36Zombi")
	darfuncs.UnhideBadGuy("37Zombi")
	GoToMul("36Zombi")
	GoToMul("37Zombi")

def x10(sectorindex,entityname):
	if entityname=='Player1':
		zombisenaccion()
		sectx10.OnEnter=""

def zombisenaccion2():
	darfuncs.UnhideBadGuy("38Zombi")
	darfuncs.UnhideBadGuy("39Zombi")
	GoToMul("38Zombi")
	GoToMul("39Zombi")

def x11(sectorindex,entityname):
	if entityname=='Player1':
		zombisenaccion2()
		sectx11.OnEnter=""

def zombisenaccion4():
	darfuncs.UnhideBadGuy("VolcanoArq6")
	darfuncs.UnhideBadGuy("VolcanoArq7")
	GoToMul("VolcanoArq6")
	GoToMul("VolcanoArq7")

def x13(sectorindex,entityname):
	if entityname=='Player1':
		zombisenaccion4()
		sectx13.OnEnter=""


def Suenamusica1(sectorindex,entityname):
	if entityname=='10Kngt'or 'Player1':
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3"))
		sectx14.OnEnter=""

def TerminanLasMuertes2():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente1",None)
	MusicTool.Music2Sector("ambiente3",None)
	MusicTool.Music2Sector("ambiente4",None)

def TerminanLasMuertes3():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio2atm20b"))
	MusicTool.Music2Sector("ambiente6",None)
	MusicTool.Music2Sector("ambiente8","Atmosfera20a")



def TerminanLasMuertes4():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicioatm20"))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmemptyloquesea"))
	MusicTool.Music2Sector("ambiente8",None)


def TerminanLasMuertes5():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera1"))

def TerminanLasMuertes6():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera4"))
	MusicTool.Music2Sector("ambiente9",None)

def aparecensalam():
	darfuncs.EnterSecEvent(-47782.1198357, 13511.1579817, -27138.7117614,aparecensalamAlAntrar)

def aparecensalamAlAntrar():
	#darfuncs.UnhideBadGuy("24Salamander")
	darfuncs.UnhideBadGuy("25Salamander")





#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador2.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador2():
	desplazamientos=(500.0, 2500.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.CloseDoor()


def BajaElevador2():

	global enmarcha
	if enmarcha:
		return
	desplazamientos=(500.0, 2500.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.OpenDoor()
	enmarcha=1


def EsperaYSubeElevador2():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, SubeElevador2, ())


def Elevador2Arriba():

	global enmarcha
	enmarcha=0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador():

	global enmarcha
	if enmarcha:
		return
	desplazamientos=(500.0, 6500.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	columnaelevador.CloseDoor()
	enmarcha=1

def BajaElevador():

	desplazamientos=(500.0, 6500.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	columnaelevador.OpenDoor()


def ElevadorArriba():

	global enmarcha
	enmarcha=0


def EsperaYBajaElevador():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador, ())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para desprendimientos.py**************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def runDespA(trsector_name, ent):
	global despABreak
	if(despABreak==0):
		despA1.DoBreak((0,-1,0),(7500,-16350,-71000),(0,0,0))
#		despA2.DoBreak((0,-1,0),(8750,-16350,-72750),(0,0,0))
#		despA3.DoBreak((0,-1,0),(9750,-16350,-71250),(0,0,0))

		p0 = 7000,-16350,-69000
		p1 = 9750,-16350,-68550
		p2 = 10000,-16350,-74750
		p3 = 7250,-16350,-74000

		dust0=Bladex.CreateEntity("despSDustA", "Entity Particle System D3", p0[0],p0[1],p0[2] )
		dust0.D1= p1[0]-p0[0] ,p1[1]-p0[1] ,p1[2]-p0[2]
		dust0.D2= p2[0]-p1[0] ,p2[1]-p1[1] ,p2[2]-p1[2]
		dust1=Bladex.CreateEntity("despSDustB", "Entity Particle System D3", p3[0],p3[1],p3[2] )
		dust1.D1= p1[0]-p3[0] ,p1[1]-p3[1] ,p1[2]-p3[2]
		dust1.D2= p2[0]-p1[0] ,p2[1]-p1[1] ,p2[2]-p1[2]

		dust0.ParticleType="MediumDust"
		dust1.ParticleType="MediumDust"
		dust0.YGravity=30.0
		dust1.YGravity=30.0
		dust0.Friction=0.2
		dust1.Friction=0.2
		dust0.PPS=412
		dust1.PPS=412
		dust0.Velocity=0.0, -410.0, 0.0
		dust1.Velocity=0.0, -410.0, 0.0
		dust0.RandomVelocity=40.0
		dust1.RandomVelocity=40.0
		dust0.Time2Live=10
		dust1.Time2Live=10
		dust0.DeathTime=Bladex.GetTime()+29.0/60.0
		dust1.DeathTime=Bladex.GetTime()+29.0/60.0
		derrumbesuelopiedra.Play(7500,-17350,-71000)

		despABreak=1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para arrowpuz.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def apDust(name,p1,p2,p3):
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

def apOpenDoor():
	apDoor.opentype=Doors.AC_UNIF_DEC
	apDoor.o_init_vel=0
	apDoor.o_init_displ=625
	apDoor.o_med_vel=-1000
	apDoor.o_med_displ=2000
	apDoor.o_end_vel=0
	apDoor.o_end_displ=625
	apDoor.OpenDoor()

def apCloseDoor():
	apDoor.closetype=Doors.AC
	apDoor.c_init_displ=3250
	apDoor.c_med_vel=16000
	apDoor.CloseDoor()

def apDust(name,p1,p2,p3):
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

def apBreakSectorA(sector,entity):
	global apSectorABroken
	if (apSectorABroken) : return
	if (entity!="Player1") : return
	print("abBreakSectorA(trsector,entity)")
	apSectorA.DoBreak((0,2,0),(-56000,10000,-34750),(0,100,0))
	apSectorABroken=1

	# Coordinates have been adjusted, original was tiny -LeadHead
	a = -53900.0, 9500.0, -36420.0
	b = -58230.0, 9500.0, -36100.0
	c = -54050.0, 9500.0, -33050.0
	d = -58230.0, 9500.0, -33010.0
	apDust("apDustA1",a,b,c)
	apDust("apDustA2",d,b,c)
	
	# Add sound -LeadHead
	SoundBreakA.Position = -56000,10000,-34750
	SoundBreakA.PlaySound(0)
	

def apBreakSectorB(sector,entity):
	global apSectorBBroken
	if (apSectorBBroken) : return
	if (entity!="Player1") : return
	print("abBreakSectorB(trsector,entity)")
	apSectorB.DoBreak((0,2,0),(-64250,11000,-34750),(0,100,0))
	apSectorBBroken=1

	# Coordinates have been adjusted, original was tiny -LeadHead
	a = -62120.0, 9700.0, -36500.0
	b = -66650.0, 10000.0, -36300.0
	c = -62120.0, 9560.0, -33000.0
	d = -66650.0, 10000.0, -33100.0
	apDust("apDustB1",a,b,c)
	apDust("apDustB2",d,b,c)
	
	# Add sound -LeadHead
	SoundBreakB.Position = -56000,10000,-34750
	SoundBreakB.PlaySound(0)

def apActivate():
	apOpenDoor()
	#Bladex.AddScheduledFunc(Bladex.GetTime()+20.0, apStartFlood, () )


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para wscene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def TerminanLasMuertes():
	AbrirP()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera18"))

def ApareceMinorx(JMinX):
	darfuncs.UnhideBadGuy(JMinX.Name)
	JMinX.Angle = -3.1415/2
	JMinX.Deaf  = 1
	JMinX.Blind = 1

def CreateMinorx(x,y,z,angle,name):
	garrote=Bladex.CreateEntity(name+"w","Hachacarnicero",0,0,0)
	garrote.Weapon=1


	JMinX=Bladex.CreateEntity(name,"Minotaur",x,y,z)
	JMinX.Person = 1
	JMinX.Angle = angle
	JMinX.Level=lvl_control.GiveLevel(5,10)
	Actions.TakeObject(JMinX.Name,garrote.Name)
	JMinX.Deaf = 1
	JMinX.Blind = 1
	#AniSound.AsignarSonidosMinotaur(JMinX.Name)
	EnemyTypes.EnemyDefaultFuncs(JMinX)
	JMinX.SetOnFloor()
	darfuncs.HideBadGuy(JMinX.Name)


	return JMinX

def wSceneMinAnim(a,b) :
	JMinA.Position = 12500,7059,16628
	JMinA.SetOnFloor()
	JMinA.LaunchAnimation("Min_1_escena01_volcan")
	GrupoMuerte.AddGuy("JMinA")

	GrupoMuerte.AddGuy("JMinB")


def wSceneMinsFight() :
	print(">wSceneMinsFight()")
	JMinA.Deaf = 0
	JMinA.Blind = 0
	JMinA.LookAtEntity("Player1")

	JMinB.Deaf = 0
	JMinB.Blind = 0
	JMinB.LookAtEntity("Player1")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3"))
"""
def Abrerast89():

	desplazamientos=(1700.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast8
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast8din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

	desplazamientos=(1750.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast9
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast9din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
"""
def wFlame(name,x,y):
	flame=Bladex.CreateEntity(name, "Entity Particle System D1", x,8900,y )
	flame.ParticleType="PrisBurn"
	flame.YGravity=-2400.0
	flame.Friction=0.12
	flame.PPS=30
	flame.Velocity=0,-1000,0
	flame.RandomVelocity=40
	flame.Time2Live=11
	flame.DeathTime=Bladex.GetTime()+8.25
	PlayQueMeQuemo((x,8900,y))

def jaulaADownTimer(ent,Time) :
	global BurnA
	c=Bladex.GetEntity("cuerda1")
	JPrisA.Move(0.0,fallSpeed,0.0)
	wjA.Move(0.0,fallSpeed,0.0)
	c.Move(0.0,fallSpeed,0.0)
	if (BurnA==0 and wjA.Position[1]>7500) :
		wFlame("JaulaFA",7007.476,11462.973)
		BurnA=1
	if (wjA.Position[1]>11000) :
		JPrisA.RemoveFromList("jaulaADownTimer")
		JPrisA.TimerFunc=""
		wjA.RemoveFromWorld()
		wjA.SubscribeToList("Pin")
		JPrisA.RemoveFromWorld()
		JPrisA.SubscribeToList("Pin")

def jaulaBDownTimer(ent,Time) :
	global BurnB
	c=Bladex.GetEntity("cuerda2")
	JPrisB.Move(0.0,fallSpeed,0.0)
	wjB.Move(0.0,fallSpeed,0.0)
	c.Move(0.0,fallSpeed,0.0)
	if (BurnB==0 and wjB.Position[1]>7500) :
		wFlame("JaulaFB",5013,15141)
		BurnB=1
	if (wjB.Position[1]>11000) :
		JPrisB.RemoveFromList("jaulaBDownTimer")
		JPrisB.TimerFunc=""
		wjB.RemoveFromWorld()
		wjB.SubscribeToList("Pin")
		JPrisB.RemoveFromWorld()
		JPrisB.SubscribeToList("Pin")

def jaulaCDownTimer(ent,Time) :
	global BurnC
	c=Bladex.GetEntity("cuerda3")
	JPrisC.Move(0.0,fallSpeed,0.0)
	wjC.Move(0.0,fallSpeed,0.0)
	c.Move(0.0,fallSpeed,0.0)
	if (BurnC==0 and wjC.Position[1]>7500) :
		wFlame("JaulaFC",-431.065,7736.838)
		BurnC=1
	if (wjC.Position[1]>11000) :
		JPrisB.RemoveFromList("jaulaCDownTimer")
		JPrisB.TimerFunc=""
		wjC.RemoveFromWorld()
		wjC.SubscribeToList("Pin")
		JPrisC.RemoveFromWorld()
		JPrisC.SubscribeToList("Pin")

def jaulasDown(a,b):

	PlayTrakaTraka((5003.131,3043.779,15117.294))

	l=Bladex.GetEntity("MPalanca")
	mpalanca.TurnOn()

	Bladex.CreateTimer("jaulaADownTimer",0.1 )
	j=Bladex.GetEntity("jaula1")
	j.TimerFunc=jaulaADownTimer;
	j.SubscribeToList("jaulaADownTimer")

	Bladex.CreateTimer("jaulaBDownTimer",0.1 )
	j=Bladex.GetEntity("jaula2")
	j.TimerFunc=jaulaBDownTimer;
	j.SubscribeToList("jaulaBDownTimer")

	Bladex.CreateTimer("jaulaCDownTimer",0.1 )
	j=Bladex.GetEntity("jaula3")
	j.TimerFunc=jaulaCDownTimer;
	j.SubscribeToList("jaulaCDownTimer")

def GreatMuu(x,y):
	SoundMuu.Position = JMinA.Position
	SoundMuu.PlaySound(0)

def PlayQueMeQuemo(pos):
	global SoundQueMeQuemo
	global iSoundQueMeQuemo
	SoundQueMeQuemo[iSoundQueMeQuemo].Position = pos
	SoundQueMeQuemo[iSoundQueMeQuemo].PlaySound(0)
	iSoundQueMeQuemo=iSoundQueMeQuemo+1
	if iSoundQueMeQuemo == len(SoundQueMeQuemo):
		iSoundQueMeQuemo = 0

	try:
		GritoBife1.StopPeriodic()
		GritoBife2.StopPeriodic()
		GritoBife3.StopPeriodic()
	except:
		print "ERROR ERROR NO SE GRABO EL SONIDO!!!!!!!!"

def PlayTrakaTraka(pos):
	SoundTrakaTraka.Position = pos
	SoundTrakaTraka.PlaySound(30)


def wScenePrisAnim():
	print(">wSceneAnim()")
	JPrisA.Position = 6966.004,6099.657,11428.789
	JPrisA.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	JPrisA.Actor = 1
	JPrisA.Animation="Prs_1_escena01_volcan"
	JPrisA.FPS=20.0
	JPrisA.SendSectorMsgs=0
	JPrisA.TurnOn()
	JPrisB.Position = 5003.131,3043.779,15117.294
	JPrisB.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	JPrisB.Actor = 1
	JPrisB.Animation="Prs_2_escena01_volcan"
	JPrisB.FPS=20.0
	JPrisB.SendSectorMsgs=0
	JPrisB.TurnOn()
	JPrisC.Position = -472.472,3709.12,7702.817
	JPrisC.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	JPrisC.Actor = 1
	JPrisC.Animation="Prs_3_escena01_volcan"
	JPrisC.FPS=20.0
	JPrisC.SendSectorMsgs=0
	JPrisC.TurnOn()

	try:
		GritoBife1.PlayPeriodic()
		GritoBife2.PlayPeriodic()
		GritoBife3.PlayPeriodic()
	except:
		print "ERROR ERROR NO SE GRABO EL SONIDO!!!!!!!!"


def wScenePrisAnimLoop() :

	#JPrisA.Actor = 1
	JPrisA.Animation="Prs_1gotohell"
	JPrisA.FPS=20.0
	JPrisA.SendSectorMsgs=0
	JPrisA.TurnOn()
	JPrisA.RotateRel(0,0,0,1,0,0,0.0001)
	#JPrisB.Actor = 1
	JPrisB.Animation="Prs_2gotohell"
	JPrisB.FPS=20.0
	JPrisB.SendSectorMsgs=0
	JPrisB.TurnOn()
	JPrisB.RotateRel(0,0,0,1,0,0,0.0001)
	#JPrisC.Actor = 1
	JPrisC.Animation="Prs_1gotohell"
	JPrisC.FPS=20.0
	JPrisC.SendSectorMsgs=0
	JPrisC.TurnOn()
	JPrisC.RotateRel(0,0,0,1,0,0,0.0001)

	try:
		GritoBife1.PlayPeriodic()
		GritoBife2.PlayPeriodic()
		GritoBife3.PlayPeriodic()
	except:
		print "ERROR ERROR NO SE GRABO EL SONIDO!!!!!!!!"


def	wScenePrisAnimStop() :
	JPrisA.TurnOff()
	JPrisB.TurnOff()
	JPrisC.TurnOff()

	try:
		GritoBife1.StopPeriodic()
		GritoBife2.StopPeriodic()
		GritoBife3.StopPeriodic()
	except:
		print "ERROR ERROR NO SE GRABO EL SONIDO!!!!!!!!"

##################################### C A M A R A S #####################################################
##################################### C A M A R A S #####################################################
##################################### C A M A R A S #####################################################

def wSceneStop(camera,frame):
	print("STOP #")
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	wScenePrisAnimStop()
	wScenePrisAnimLoop()
	wSceneMinsFight()
	#Abrerast89()
	ScriptSkip.SkipScriptEnd()

def wSceneSetupCamD(camera,frame) :
	print(">wSceneSetupCamD")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("PrisioneroALaParrilla05.cam",514,590)
	cam.AddCameraEvent(-1,wSceneStop)

def wSceneSetupCamC(camera,frame) :
	print(">wSceneSetupCamC")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("PrisioneroALaParrilla04.cam",388,513)
	cam.AddCameraEvent(-1,wSceneSetupCamD)

def wSceneSetupCamB(camera,frame) :
	print(">wSceneSetupCamB")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("PrisioneroALaParrilla03.cam",240,387)
	cam.AddCameraEvent(-1,wSceneSetupCamC)

def FadePrisCool(a,b):
	AuxFuncs.FadeTo(0.5,0.125,0,0,0)

def wSceneSetupCamA() :
	print(">wSceneSetupCamA")
	cam = Bladex.GetEntity("Camera")
	#cam.SetMaxCamera("prisioneros_a_la_brasaCamera02.cam",0,-1)
	cam.SetMaxCamera("prisioneros_a_la_brasaCamera02.cam",0,160)
	cam.AddCameraEvent(130,wSceneMinAnim)
	cam.AddCameraEvent(150,FadePrisCool)
	cam.AddCameraEvent(-1,wSceneNextCamera)

def wSceneNextCamera(a,b):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("PrisioneroALaParrilla04.cam",388,513)
	cam.AddCameraEvent(35,GreatMuu)
	cam.AddCameraEvent(90,jaulasDown)
	cam.AddCameraEvent(-1,wSceneStop)
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)


############################## I N I C I A L I Z A C I O N ##############################################
############################## I N I C I A L I Z A C I O N ##############################################
############################## I N I C I A L I Z A C I O N ##############################################

def wrstrtre():
	wScenePrisAnimStop()
	wScenePrisAnim()
	wSceneSetupCamA()

def wSceneStart() :
	print("PLAY >")
	ApareceMinorx(JMinA)
	JMinA.Position = 12500,7059,16628
	JMinA.SetOnFloor()
	ApareceMinorx(JMinB)
	JMinB.Position= 11882.421,7040.655,10077.036
	JMinB.SetOnFloor()
	ScriptSkip.SkipScriptStart("wscene")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2,MusicTool.LaunchMusicEvent,("inicio4",))

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, wrstrtre,() )

def triggerSecIn(index,ent) :
	global wAct
	if (ent!="Player1") : return
	if (wAct==0) :
		wSceneStart()
		wAct=1
