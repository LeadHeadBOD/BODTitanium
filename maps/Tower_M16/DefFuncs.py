##///
##||| Tower_M16/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Burning skeleton maze lights now fade in after 3 sec rather than 10
##||| * Restored one of the forgotten burning skeleton maze lights to fade in
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
import Room
import Button
import MusicTool
import ScriptSkip
import Language
import Credits

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrereja1():
	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	cerradurp1.key=""

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def Cierrapta1a():
	pta1a.CloseDoor()

def Cierrapta2a():
	pta2a.CloseDoor()

def Cierrapta3a():
	pta3a.CloseDoor()

def Cierrapta4a():
	pta4a.CloseDoor()

def Abre1():
	pta1a.OpenDoor()
	pta2a.OpenDoor()
	pta3a.OpenDoor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, pta4a.OpenDoor,())

def Abrepta1B():
	pta1B.OpenDoor()

def Cierrapta1B():
	pta1B.CloseDoor()

def AbrePuerta1():
	puerta1.OpenDoor()

def CierraPuerta1():
	puerta1.CloseDoor()

def AbrePuerta2OnDie(ent=0):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(37,))
	AbrePuerta2(ent)

def AbrePuerta2(ent=0):
	puerta2.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def CierraPuerta2():
	puerta2.CloseDoor()


def AbrePuerta3():
	puerta3.OpenDoor()

def CierraPuerta3():
	puerta3.CloseDoor()

def AbrePuerta3():
	puerta3.OpenDoor()

def CierraPuerta3():
	puerta3.CloseDoor()

def AbrePuerta5():
	puerta5.OpenDoor()

def CierraPuerta5():
	puerta5.CloseDoor()

def AbrePuerta6():
	puerta6.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty2") )

def CierraPuerta6():
	puerta6.CloseDoor()

def AbrePuerta7():
	puerta7.OpenDoor()

def CierraPuerta7():
	puerta7.CloseDoor()

def LineaPolvo():
	polvo=Bladex.CreateEntity("Polvo2", "Entity Particle System D2", -9250,-111200,7000)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 0,0,4000
	polvo.ParticleType="DustDoor"
	polvo.YGravity=-700.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def AbrePuerta9():
	puerta9.OpenDoor()

def CierraPuerta9():
	puerta9.CloseDoor()

def AbrePuerta10():
	puerta10.OpenDoor()

def CierraPuerta10():
	puerta10.CloseDoor()

def AbrePuerta11():
	puerta11.OpenDoor()

def CierraPuerta11():
	puerta11.CloseDoor()


def Abreptasector0():
	ptasector0.OpenDoor()

def Cierraptasector0():
	ptasector0.CloseDoor()


def Abreptasector00():
	ptasector00.OpenDoor()

def Cierraptasector00():
	ptasector00.CloseDoor()


def Abreptasector1():
	ptasector1.OpenDoor()

def Cierraptasector1():
	ptasector1.CloseDoor()

def Abreptasector2():
	ptasector2.OpenDoor()

def Cierraptasector2():
	ptasector2.CloseDoor()


def Abreptasector3():
	ptasector3.OpenDoor()

def Cierraptasector3():
	ptasector3.CloseDoor()


def Abreptasector4():
	ptasector4.OpenDoor()

def Cierraptasector4():
	ptasector4.CloseDoor()


def Abreptasector5():
	ptasector5.OpenDoor()

def Cierraptasector5():
	ptasector5.CloseDoor()

def Abrepuerta12():
	puerta12.OpenDoor()

def Cierrapuerta12():
	puerta12.CloseDoor()

def Abrepuerta13():
	puerta13.OpenDoor()

def Cierrapuerta13():
	puerta13.CloseDoor()



def Abrepuerta14():
	puerta14.OpenDoor()

def Cierrapuerta14():
	puerta14.CloseDoor()


def Abrepuerta15():
	puerta15.OpenDoor()

def Cierrapuerta15():
	puerta15.CloseDoor()


def Abrepuerta16():
	puerta16.OpenDoor()

def Cierrapuerta16():
	puerta16.CloseDoor()

def Abrepuerta17():
	puerta17.OpenDoor()

def Cierrapuerta17():
	puerta17.CloseDoor()


def Abrepuerta18():
	puerta18.OpenDoor()

def Cierrapuerta18():
	puerta18.CloseDoor()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para VelasKyalf      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def PolvoDeVelaskyalf(name,p,d,pps):
	tierra1=Bladex.CreateEntity(name, "Entity Particle System D2", p[0]-100000, p[1], p[2])
	tierra1.D1= d
	tierra1.ParticleType="VsSmoke"
	tierra1.PPS=pps
	tierra1.YGravity=0
	tierra1.Friction=0.0
	tierra1.Velocity=-5000.0, 0.0, 0.0
	tierra1.RandomVelocity=-20
	tierra1.Time2Live=64
	return tierra1

def PolvoQueEntra(par):
	global Polvazo
	Polvazo = []
	Polvazo.append(PolvoDeVelaskyalf("Polvazo1",(-26709, -111999, 4717),(0, 0,9000),512*par))
	Polvazo.append(PolvoDeVelaskyalf("Polvazo2",(-26709, -111999, 4717),(0, 0,9000),512*par))
	Polvazo[1].Velocity=-15000.0, 0.0, 0.0
	Polvazo[1].RandomVelocity=20

	#Polvazo.append(PolvoDeVelaskyalf("Polvazo2",(-26709, -111420, 4717),(0,-8000,0),512*par))
	#Polvazo.append(PolvoDeVelaskyalf("Polvazo3",(-26709, -111420,13500),(0,-8000,0),512*par))
	#Polvazo.append(PolvoDeVelaskyalf("Polvazo4",(-26709, -123000, 8988),(0, 1500, 4000),128*par))
	#Polvazo.append(PolvoDeVelaskyalf("Polvazo5",(-26709, -123000, 8988),(0, 1500,-4000),128*par))
	#Polvazo.append(PolvoDeVelaskyalf("Polvazo6",(-26709, -120000, 4717),(0, -1500, 800),64*par))
	#Polvazo.append(PolvoDeVelaskyalf("Polvazo7",(-26709, -120000,13500),(0, -1500,-800),64*par))

def BorraPolvoQueEntra():
	global Polvazo

	for p in Polvazo:
		p.DeathTime=Bladex.GetTime()

def ApareceVelaskyalf(Alpha):
	global HojaIzquierda
	global HojaDerecha

	HojaIzquierda.Alpha = Alpha
	HojaDerecha.Alpha   = Alpha
	if Alpha<=1:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,ApareceVelaskyalf,(Alpha+0.0125,))
	else:
		HojaIzquierda.Alpha = 1
		HojaDerecha.Alpha   = 1



def CreaVelaskyalf(a,b):
	global HojaIzquierda
	global HojaDerecha
	global HojaIzquierda2
	global HojaDerecha2


	HojaIzquierda             = Bladex.CreateEntity("HojaIzquierda","PuertaMiguelIzquierda",0,0,0)
	HojaIzquierda.Position    = -28681,-117514,4126
	HojaIzquierda.Orientation = (0.499998003244, 0.499997347593, -0.500005304813, 0.499999344349)
	HojaIzquierda.Scale       = 1.0
	HojaIzquierda.Alpha       = 0.0
	HojaIzquierda.SelfIlum    = 0.0

	HojaDerecha             = Bladex.CreateEntity("HojaDerecha","PuertaMiguelDerecha",0,0,0)
	HojaDerecha.Position    = -28693, -117505, 14116
	HojaDerecha.Orientation = (0.499998003244, 0.499997347593, -0.500005304813, 0.499999344349)
	HojaDerecha.Scale       = 1.0
	HojaDerecha.Alpha       = 0.0
	HojaDerecha.SelfIlum    = 0.0


	HojaIzquierda2             = Bladex.CreateEntity("HojaIzquierda2","PuertaMiguelIzquierda",0,0,0)
	HojaIzquierda2.Position    = -128681,-117514,4126
	HojaIzquierda2.Orientation = (0.499998003244, 0.499997347593, -0.500005304813, 0.499999344349)
	HojaIzquierda2.Scale       = 1.0
	HojaIzquierda2.Alpha       = 1.0
	HojaIzquierda2.SelfIlum    = 0.0

	HojaDerecha2             = Bladex.CreateEntity("HojaDerecha2","PuertaMiguelDerecha",0,0,0)
	HojaDerecha2.Position    = -128693, -117505, 14116
	HojaDerecha2.Orientation = (0.499998003244, 0.499997347593, -0.500005304813, 0.499999344349)
	HojaDerecha2.Scale       = 1.0
	HojaDerecha2.Alpha       = 1.0
	HojaDerecha2.SelfIlum    = 0.0


	darfuncs.LaunchMaxCamera("MuerteGurakCamera02.cam",671-550,791-550,CambiazoCampuza)
	Bladex.GetEntity("Camera").AddCameraEvent(120-3,AbreVelaskyalf)
	Bladex.GetEntity("Camera").AddCameraEvent(120-20,flashy)



	ApareceVelaskyalf(0)

def Selflash(i):
	global LuzFlash1
	global LuzFlash2

	if i>0:
		s = 1-i
		LuzFlash1.Intensity = s*50.0
	else:
		s = 1+i
		LuzFlash2.Intensity = s*50.0


	if i > -1.0:
		if i > 0.0:
			Bladex.AddScheduledFunc(Bladex.GetTime() + 0.0125,Selflash,(i-0.0125,))
		else:
			Bladex.AddScheduledFunc(Bladex.GetTime() + 0.025,Selflash,(i-0.0125,))
	else:
		LuzFlash1.SubscribeToList("Pin")
		LuzFlash2.SubscribeToList("Pin")


def flashy(a,b):
	global LuzFlash1
	global LuzFlash2

	LuzFlash1=Bladex.CreateEntity("FlashCool","Entity Spot",-24770, -115054, 8312)
	LuzFlash1.Color=255,255,255
	LuzFlash1.Intensity=0
	LuzFlash1.Precission=0.1
	LuzFlash1.Visible=0
	LuzFlash1.CastShadows=0
	LuzFlash1.Flick=0

	LuzFlash2=Bladex.CreateEntity("FlashCool","Entity Spot",-124770, -115054, 8312)
	LuzFlash2.Color=255,255,255
	LuzFlash2.Intensity=50
	LuzFlash2.Precission=0.1
	LuzFlash2.Visible=0
	LuzFlash2.CastShadows=0
	LuzFlash2.Flick=0

	Selflash(1)

def AbreHojasMagicas(counter):
	global TimeToOpenDoors

	if counter <= 0:
		return

	HojaDerecha2.Rotate  (0,0,1,-0.039269875/TimeToOpenDoors)
	HojaIzquierda2.Rotate(0,0,1, 0.039269875/TimeToOpenDoors)
	#HojaDerecha2.Alpha   = HojaDerecha.Alpha-1/(40*TimeToOpenDoors)
	#HojaIzquierda2.Alpha = HojaDerecha.Alpha
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.025,AbreHojasMagicas,(counter-1,))

def AbreVelaskyalf(a,b):
	AuxFuncs.FadeTo(0.125,1.0,255,255,255)

def CambiazoCampuza(a,b):
	AuxFuncs.FadeFrom(0.125,0.0,255,255,255)

	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,AbreHojasMagicas,(40*TimeToOpenDoors,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,PolvoQueEntra,(0.5,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 20.0,BorraPolvoQueEntra,())

	char.Move(-100000,0,0)
	char.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,char.GoTo,(-134717.36454, -112848.40838, 9247.63213226))
	darfuncs.LaunchMaxCamera("MuerteGurakCamera03.cam",792-550,1000-550,SaltoAlNivelDelCaos)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 7.5,AuxFuncs.FadeTo,(3.0,10.0,0,0,0))

def SaltoAlNivelDelCaos(a,b):
	GotoMapVars.EndOfLevel()
	#Bladex.LoadLevel("Chaos_M17")

def Velaskyalf():
	HojaIzquierda  = Bladex.GetEntity("HojaIzquierda")
	HojaDerecha    = Bladex.GetEntity("HojaDerecha")
	HojaIzquierda2 = Bladex.GetEntity("HojaIzquierda2")
	HojaDerecha2   = Bladex.GetEntity("HojaDerecha2")


	if HojaDerecha:
		HojaDerecha.SubscribeToList("Pin")
	if HojaIzquierda:
		HojaIzquierda.SubscribeToList("Pin")
	if HojaDerecha2:
		HojaDerecha2.SubscribeToList("Pin")
	if HojaIzquierda2:
		HojaIzquierda2.SubscribeToList("Pin")


	darfuncs.LaunchMaxCamera("MuerteGurakCamera02.cam",550-550,670-550,CreaVelaskyalf)
	char.Position    = -11764.01,-112426,8661.881
	char.Angle       = 3.14159/2
	char.SetOnFloor()
	char.GoToJogging = 0
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,char.GoTo,(-18862, -112069, 10299))


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para skelsB.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def sksBSkelActiv(ent):
	skel = Bladex.GetEntity(ent)
	skel.Blind = 0
	skel.Deaf = 0
	persPath.unlock(ent)

def sksBStartB():
	Bladex.GetEntity("sksBSkeletonB").GoToJogging=1
	a = (8000,-33000,1300)
	b = (2840,-33000,2375)
	c = (2840,-33000,5000)
	persPath.lock("sksBSkeletonB",sksBSkelActiv,3,(a,b,c))

def sksBStart():
	Bladex.GetEntity("sksBSkeletonA").GoToJogging=1
	a = (7500,-33000,2800)
	b = (3840,-33000,2870)
	c = (3000,-33000,5800)
	persPath.lock("sksBSkeletonA",sksBSkelActiv,3,(a,b,c))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,sksBStartB,())

def sklTimer( entName, startTime, totalTime, val, data ) :
	skl=Bladex.GetEntity(entName)
	p = 0.70
	h = 2.5
	if (val<p) :
		val = (val/p) * h
	else:
		val = 1 + ( (1-((val-p)/(1-p))) * (h-1) )
	skl.Lights=[ (data[1]*val,data[2],(data[3],data[4],data[5])) ]
	skl.FiresIntensity = [ 20-((20-data[0])*val) ]
	skl.Move(0,0,0)

def sklFStart(ent):
	timerAux.unlock(ent)

def sklEStart(ent):
	timerAux.run("eskalet4")
	timerAux.unlock(ent)

def sklDStart(ent):
	timerAux.run("eskalet3")
	timerAux.unlock(ent)

def sklCStart(ent):
	timerAux.run("eskalet2")
	timerAux.unlock(ent)

def sklBStart(ent):
	timerAux.run("eskalet1")
	timerAux.unlock(ent)


def sklAStart(index, ent):
	global sklOk
	if (ent<>"Player1") : return
	if (sklOk) : return
	sklOk=1

	timerAux.lock( "eskalet5", (8, 7,0.060000,255, 80,4), 3, sklTimer, sklBStart )
	timerAux.lock( "eskalet1", (7,20,0.031250,221, 55,0), 3, sklTimer, sklCStart )
	timerAux.lock( "eskalet2", (8, 3,0.040000,221,116,0), 3, sklTimer, sklDStart )
	timerAux.lock( "eskalet3", (3,24,0.070000,231, 75,1), 3, sklTimer, sklEStart )
	timerAux.lock( "eskalet4", (3, 8,0.100000,238, 83,0), 3, sklTimer, sklFStart )

	timerAux.run("eskalet5")
	sksBStart()



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para skels.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def sksSkelActiv(ent):
	skel = Bladex.GetEntity(ent)
	skel.Blind = 0
	skel.Deaf = 0
	persPath.unlock(ent)

def sksStart(index, ent):
	global sksStarted
	if (sksStarted) : return
	if (ent<>"Player1") : return
	sksStarted=1
	a = (3250,-33000,18250)
	b = (3000,-33000,19625)
	c = (2250,-33000,21000)
	d = ( 750,-33000,23125)
	e = (-2500,-33000,24625)
	persPath.lock("sksSkeletonA",sksSkelActiv,5,(a,b,c,d,e))
	persPath.lock("sksSkeletonB",sksSkelActiv,4,(b,c,d,e))
	persPath.lock("sksSkeletonC",sksSkelActiv,3,(c,d,e))

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ZONAOSCURA.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************
### All of the lights now turn on after 3 seconds, rather than the original 10.
def FinGrupoMuerte1(a=0,b=0,c=0):
	OnOff.LightSetInens   = 6.0
	OnOff.LightSetRadius  = 0.077
	OnOff.LightSetColor   = (255,142,17)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, OnOff.TurnOnLight,("Lsector1",))
	Abreptasector2()

def Sorpresa1():
	Cierraptasector0()
	Cierraptasector00()
	Cierraptasector2()
	darfuncs.UnhideBadGuy("11HSKL")
	darfuncs.UnhideBadGuy("12HSKL")
	o1 = Bladex.GetEntity("11HSKL")
	o2 = Bladex.GetEntity("12HSKL")
	darfuncs.EnciendeEnLlamas(o1,3,0.066)
	darfuncs.EnciendeEnLlamas(o2,3,0.066)
	o1.GoTo(-17000,-33000,26000)
	#o2.GoTo(-17000,-33000,26000)

def FinGrupoMuerte2(a=0,b=0,c=0):
	OnOff.LightSetInens   = 6.0
	OnOff.LightSetRadius  = 0.077
	OnOff.LightSetColor   = (255,142,17)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, OnOff.TurnOnLight,("Lsector2",))		# Added 	-LeadHead
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, OnOff.TurnOnLight,("Lsector3",))
	Abreptasector4()

def Sorpresa2():
	Cierraptasector1()
	Cierraptasector4()
	darfuncs.UnhideBadGuy("13HSKL")
	darfuncs.UnhideBadGuy("14HSKL")
	o3 = Bladex.GetEntity("13HSKL")
	o4 = Bladex.GetEntity("14HSKL")
	darfuncs.EnciendeEnLlamas(o3,3,0.066)
	darfuncs.EnciendeEnLlamas(o4,3,0.066)
	o3.GoTo(-4000,-33000,26000)
	#o4.GoTo(-4000,-33000,26000)

def FinGrupoMuerte3(a=0,b=0,c=0):
	OnOff.LightSetInens   = 6.0
	OnOff.LightSetRadius  = 0.077
	OnOff.LightSetColor   = (255,142,17)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, OnOff.TurnOnLight,("Lsector4",))

	Abreptasector5()
	darfuncs.UnhideBadGuy("17HSKL")
	o7 = Bladex.GetEntity("17HSKL")
	darfuncs.EnciendeEnLlamas(o7,3,0.066)

def Sorpresa3():
	Cierraptasector3()
	darfuncs.UnhideBadGuy("15HSKL")
	darfuncs.UnhideBadGuy("16HSKL")
	o5 = Bladex.GetEntity("15HSKL")
	o6 = Bladex.GetEntity("16HSKL")
	darfuncs.EnciendeEnLlamas(o5,3,0.066)
	darfuncs.EnciendeEnLlamas(o6,3,0.066)
	o5.GoTo(7000,-33000,15000)
	#o6.GoTo(7000,-33000,15000)

def FinGrupoMuerte4(a=0,b=0,c=0):
	Abrepuerta12()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para 3Golems.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def GolemDeath():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,AbrePuerta6,())

def EnciendeLuzGolem(entity,time):
	Light = Bladex.GetEntity(entity)

	Light.Data.ILuz = Light.Data.Luz.Intensity = Light.Data.ILuz + 1.33
	Light.Data.IFire = Light.Data.Fire.Intensity = Light.Data.IFire - 1



def ActivateGolem3_1():
	EnmGenRnd.ActivateEnemy(EnmGlm1)
	EnmGlm1.SetOnFloor()
	EnmGlm1.SetEnemy(char)
	SonidoWakeGolem1.PlaySound(0)
	GolemSmoke("EnmGlm1")


def ActivateGolem3_2():
	EnmGenRnd.ActivateEnemy(EnmGlm2)
	EnmGlm2.SetOnFloor()
	EnmGlm2.SetEnemy(char)
	SonidoWakeGolem2.PlaySound(0)

	GolemSmoke("EnmGlm2")

	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,ActivateGolem3_1,())

def StopLuzGolem():
	golamp = Bladex.GetEntity("golamp")
	golamp.RemoveFromList("Timer60")

	Bladex.AddScheduledFunc(Bladex.GetTime(),ActivateGolem3_2,())

def StartLightGolem():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,StopLuzGolem,())
	golamp = Bladex.GetEntity("golamp")
	golamp.TimerFunc = EnciendeLuzGolem
	golamp.SubscribeToList("Timer60")
	golamp.Data = def_class.FLuz()
	golamp.Data.Fire = AuxFuncs.GetFire(golamp)
	golamp.Data.Luz = AuxFuncs.GetSpot(golamp)

	darfuncs.UnhideBadGuy(EnmGlm1.Name)
	darfuncs.UnhideBadGuy(EnmGlm2.Name)
	EnmGlm1.Alpha = 0
	EnmGlm2.Alpha = 0
	PhantonFX.AppearsChar(EnmGlm1.Name)
	PhantonFX.AppearsChar(EnmGlm2.Name)
	#EnmGlm1.Data.ClaySmoke(EnmGlm1.Name)
	#EnmGlm2.Data.ClaySmoke(EnmGlm2.Name)


def StartGolem3(sector,entity):
	if entity == "Player1":
		GolemSec.OnEnter = ""
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("atm20A") )
		Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,StartLightGolem,())
		char.Angle = 1.6
		CierraPuerta5()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Orks3.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def embosc1():
	Cierrapta1B()
	CierraPuerta3()
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, Abush1Final,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Acombate6") )

def Abush1Final():
	Abre1()
	darfuncs.UnhideBadGuy("1ORC")
	darfuncs.UnhideBadGuy("2ORC")
	darfuncs.UnhideBadGuy("3ORC")
	darfuncs.UnhideBadGuy("4ORC")
	ok1 = Bladex.GetEntity("1ORC")
	ok2 = Bladex.GetEntity("2ORC")
	ok3 = Bladex.GetEntity("3ORC")
	ok1.GoTo(-3436.8, -5048.4, -12386.2)
	ok2.GoTo(-10954.2, -5065.4, -9770.0)
	ok3.GoTo(-19050.9, -5068.6, -9832.9)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para MINORX.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def finGrupoMin1(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("6DKGT")
	Abrepuerta17()
	oP1 = Bladex.GetEntity("6DKGT")
	oP1.GoTo(72882.49, -62.55, 20045.48)
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def MINORXO():
	CierraPuerta10()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("acomblh") )
	#darfuncs.UnhideBadGuy("1MINOT")
	darfuncs.UnhideBadGuy("2MINOT")
	darfuncs.UnhideBadGuy("5DKGT")
	#o1 = Bladex.GetEntity("1MINOT")
	o2 = Bladex.GetEntity("2MINOT")
	o3 = Bladex.GetEntity("3MINOT")
	o3.Blind = 0
	o3.Deaf  = 0
	#o1.GoTo(-17000,-33000,26000)
	#o2.GoTo(-17000,-33000,26000)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para iscene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def iLaunchPersAnim(A,B) :
	char = Bladex.GetEntity("Player1")
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("inicio_torre")
	char.Position = iCharPosition
	char.Angle = iCharAngle
	char.SetOnFloor()


def iLaunchCamFadeOut(camera,frame) :
	AuxFuncs.FadeTo(2.5, 0.0)

def iLaunchCamReset(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1) # Add -LeadHead

def iLaunchCamC(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dwf_inicio_torreCamera03.cam",450,800)
	cam.AddCameraEvent(155,iLaunchPersAnim)
	cam.AddCameraEvent(-1,iLaunchCamReset)

def iLaunchCamB(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dwf_inicio_torreCamera02.cam",300,450)
	cam.AddCameraEvent(-1,iLaunchCamC)

def iLaunchCamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dwf_inicio_torreCamera01.cam",0,300)
	cam.AddCameraEvent(-1,iLaunchCamB)

def iLaunchB() :
	iLaunchCamA()

def MusicayTexto():
  	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("iniciotower"))
  	GameText.WriteText("M16T1")

def iLaunch() :
	iLaunchB()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,MusicayTexto,())


def ParchePrecarga():
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2) # Add -LeadHead
	AuxFuncs.FadeFrom(5.0, 0.125)
	ScriptSkip.SkipScriptStart("EscenainicioTower")
	#Bladex.DeactivateInput()
	char.Position = iCharPosition
	char.UnFreeze()

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.125, iLaunch, ())


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Glm11.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def GolemSmoke(glm,dir = (0,0,-300)):
	g = Bladex.GetEntity(glm)
	pc = g.Position

	p1 = pc[0] - 300 ,pc[1] - 1000,pc[2] + 200
	p2 = 600,0,0
	p3 = 300,1100,0

	hombro1 = pc[0] - 400 ,pc[1] - 1000,pc[2] + 200
	hombro2 = pc[0] + 300 ,pc[1] - 1000,pc[2] + 200

	mano1 = pc[0] - 900, pc[1], pc[2] + 500
	mano2 = pc[0] + 950, pc[1], pc[2] - 200

	vm1 = hombro1[0] - mano1[0],hombro1[1] - mano1[1],hombro1[2] - mano1[2]
	vm2 = hombro2[0] - mano2[0],hombro2[1] - mano2[1],hombro2[2] - mano2[2]

	pierna1 = pc[0] - 150, pc[1], pc[2] + 200
	pierna2 = pc[0] + 150, pc[1], pc[2] + 200

	pie1 = pierna1[0] - 150, pierna1[1] + 1400, pierna1[2]
	pie2 = pierna2[0] + 150, pierna2[1] + 1400, pierna2[2]

	vp1 = pie1[0] - pierna1[0],pie1[1] - pierna1[1],pie1[2] - pierna1[2]
	vp2 = pie2[0] - pierna2[0],pie2[1] - pierna2[1],pie2[2] - pierna2[2]

	head = pc[0] + 100 ,pc[1] - 1300,pc[2] + 200

	polvo=Bladex.CreateEntity("PolvoHead"+glm, "Entity Particle System D1", head[0],head[1],head[2])
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=75
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoPierna1"+glm, "Entity Particle System D2", pierna1[0],pierna1[1],pierna1[2])
	polvo.D = vp1[0],vp1[1],vp1[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoPierna2"+glm, "Entity Particle System D2", pierna2[0],pierna2[1],pierna2[2])
	polvo.D = vp2[0],vp2[1],vp2[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoMano1"+glm, "Entity Particle System D2", mano1[0],mano1[1],mano1[2])
	polvo.D = vm1[0],vm1[1],vm1[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoMano2"+glm, "Entity Particle System D2", mano2[0],mano2[1],mano2[2])
	polvo.D = vm2[0],vm2[1],vm2[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoCuerpo"+glm, "Entity Particle System D3", p1[0],p1[1],p1[2])
	polvo.D1 = p2[0],p2[1],p2[2]
	polvo.D2 = p3[0],p3[1],p3[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=350
	polvo.Velocity=dir
	polvo.RandomVelocity=0.0
	polvo.Time2Live=30
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0


def StopSceneGurak(camera,frame):

	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	Bladex.ActivateInput()
	Bladex.SetListenerPosition(1) # Add -LeadHead
	gen_DalGurak.SubscribeToList("Pin")


def ActivateGurakGlm(sector,entity):
	if entity == "Player1":
		DalGurakActSec.OnEnter = ""
		#EnmGenRnd.ActivateEnemy(gen_DalGurak)
		gen_DalGurak.Person=1
		#gen_DalGurak.UnFreeze()
		gen_DalGurak.Position = -23000,-13291,7716
		gen_DalGurak.Angle = 3.14
		gen_DalGurak.LaunchAnmType("first_appears")
		gen_DalGurak.SetOnFloor()
		gen_DalGurak.Alpha = 1.0

		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb4") )
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("AparicionGurak_Camera.cam",0,-1)
		Bladex.SetListenerPosition(2) # Add -LeadHead
		cam.AddCameraEvent(-1,StopSceneGurak)

		#darfuncs.HideBadGuy("7DKGT")
		darfuncs.HideBadGuy("8DKGT")
		darfuncs.HideBadGuy("9DKGT")

		char = Bladex.GetEntity("Player1")
		char.GoTo(-3500,-6100,24000)

		Bladex.AddScheduledFunc(Bladex.GetTime() + 9.0,AuxFuncs.FadeTo,(1.0, 1.0))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 11.0,AuxFuncs.FadeFrom,(1.0, 0.0))

		Scorer.SetVisible(0)
		Bladex.DeactivateInput()

def AbrirPuertaGlm1(entity):
	DalGurakActSec.OnEnter = ActivateGurakGlm
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,AbrePuerta1,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 23.0,pta4a.OpenDoor,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

	apply(OldImDeadFunc,(entity,))

def WakeUpGlm11(sector,entity):
	if entity == "Player1":
		char = Bladex.GetEntity("Player1")
		Glm11ActSec.OnEnter = ""
		glm11 = Bladex.GetEntity("1GLM")
		#glm11.Position
		glm11.UnFreeze()
		glm11.SetActiveEnemy(char)
		glm11.Blind = 0
		glm11.Deaf = 0

		GolemSmoke("1GLM")

		#SonidoWakeGolem.PlaySound(0)

		#gen_DalGurak.Person=1
		#gen_DalGurak.UnFreeze()
		gen_DalGurak.Position = 3104, -11807, 13467
		gen_DalGurak.Alpha = 0.0

		Cierrapta4a()
		#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Acombate5") )
		darfuncs.HideBadGuy("1ORC")
		darfuncs.HideBadGuy("2ORC")
		darfuncs.HideBadGuy("3ORC")
		darfuncs.HideBadGuy("4ORC")
		#darfuncs.UnhideBadGuy("7DKGT")
		darfuncs.UnhideBadGuy("8DKGT")
		darfuncs.UnhideBadGuy("9DKGT")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************



def finGrupoesc1(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("20DKGT")
	darfuncs.UnhideBadGuy("21DKGT")
	darfuncs.UnhideBadGuy("22DKGT")
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("atm16") )
	AbrePuerta7()
	oe1 = Bladex.GetEntity("20DKGT")
	oe1.GoToJogging = 1
	oe1.GoTo(56718.2, 18935.4, 5082.8)

def finGrupocaracoll(a=0,b=0,c=0):
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )


def finGrupominorxo(a=0,b=0,c=0):
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )


def finGrupokgteros(a=0,b=0,c=0):
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )


def finGrupoMuerte2(a=0,b=0,c=0):
	Abrepuerta15()


def Skelpas():
	darfuncs.UnhideBadGuy("23HSKL")
	darfuncs.UnhideBadGuy("24HSKL")
	darfuncs.UnhideBadGuy("25HSKL")
	darfuncs.UnhideBadGuy("26HSKL")
	opa1 = Bladex.GetEntity("23HSKL")
	opa2 = Bladex.GetEntity("24HSKL")
	opa3 = Bladex.GetEntity("25HSKL")
	opa4 = Bladex.GetEntity("26HSKL")
	darfuncs.EnciendeEnLlamas(opa1,2,0.066)
	darfuncs.EnciendeEnLlamas(opa2,2,0.066)
	darfuncs.EnciendeEnLlamas(opa3,2,0.066)
	darfuncs.EnciendeEnLlamas(opa4,2,0.066)

def arqueroslistos1(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("37DKGT")
	darfuncs.UnhideBadGuy("38DKGT")
	darfuncs.UnhideBadGuy("39DKGT")


def finGrupoalist1(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("40DKGT")
	darfuncs.UnhideBadGuy("40bDKGT")
	Abrepuerta18()
	ole1 = Bladex.GetEntity("40DKGT")
	ole1.GoToJogging = 1
	ole1.GoTo(5822.93490853, -12565.2758688, -1743.05691535)


def arquerocobarde(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("41DKGT")

def darkk42(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("42DKGT")

def darkko42(a=0,b=0,c=0):
	darfuncs.HideBadGuy("42DKGT")
	darfuncs.UnhideBadGuy("42bDKGT")

def MINORXO43(a=0,b=0,c=0):
	darfuncs.UnhideBadGuy("43MINOT")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Elevators.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevadorPalanca():
	global elevInAction

	if (elevInAction) : return
	elevInAction=1

	CierraPuerta2()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,SubeElevador,())

def elevadorTurnOffLights():
   OnOff.TurnOffLight("brasania1")
   OnOff.TurnOffLight("brasania2")

def SubeElevador():
	desplazamientos=(500.0, 20000.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(laelmovil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador.CloseDoor()

def BajaElevador():
	desplazamientos=(500.0, 20000.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(laelmovil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador.OpenDoor()

def ElevadorEndOpenFunc():
	#print("ElevadorEndOpenFunc")
	global elevInAction
	elevInAction=0

def ElevadorEndCloseFunc():
	#print("ElevadorEndCloseFunc")
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, BajaElevador, ())

def Abreelevator2():
	elevator2.OpenDoor()


def Cierraelevator2():
	elevator2.CloseDoor()

def Abreelevator3():
	elevator3.OpenDoor()
	darfuncs. EnterSecEvent(-27738.0913588, -19306.4828945, 18197.2,eleto3)


def Cierraelevator3():
	elevator3.CloseDoor()

def eleto3(a=0,b=0,c=0):
	Abreelevator3()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para DERR.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Cont2Derr():
	derr1.DoBreak((0, 3, 0), (57500, 20500, -11400), (0.0, 0.0, 0.0))

	derr2.DoBreak((0, 3, 0), (58500, 20700, -23500), (0.0, 0.0, 0.0))
	derr3.DoBreak((0, 3, 0), (58500, 20700, -29000), (0.0, 0.0, 0.0))


def ContDerr():
	derrumbesuelopiedra.Play(58500, 18700, -29000)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Cont2Derr, ())

def Derrumba(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderr.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ContDerr, ())



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Demons.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CBgeneradorD2(enem):
	enem.ActionAreaMin=pow(2,3)
	enem.ActionAreaMax=pow(2,4)



def LanzaMegaSurtidor2(v1, v2, v3):
	impl=Bladex.CreateEntity("MegaSurtidor", "Entity Particle System D1", v1, v2, v3)
	impl.ParticleType="Energia3"
	impl.YGravity=0.0
	impl.Friction=0.0
	impl.PPS=300
	impl.Velocity=0.0, 0.0, 0.0
	impl.RandomVelocity=-30.0
	impl.Time2Live=70
	impl.DeathTime=Bladex.GetTime()+3.0

def LanzaMegaSurtidor(v1, v2, v3):
	explms=Bladex.CreateEntity("ExplMegaSurtidor", "Entity Particle System D1", v1, v2, v3)
	explms.ParticleType="FuegoInvocacion"
	explms.PPS=1200
	explms.YGravity=4000.0
	explms.Friction=0.1
	explms.Velocity=0.0, -4000.0, 0.0
	explms.RandomVelocity=60.0
	explms.RandomVelocity_V=40.0
	explms.Time2Live=40
	explms.DeathTime=Bladex.GetTime()+0.25
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LanzaMegaSurtidor2, (v1, v2, v3,))

def ParticulateAppears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="FuegoInvocacion"
	wps.Time2Live=40
	wps.RandomVelocity=0
	wps.Velocity=0,0,0
	wps.NormalVelocity=5.0
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+0.25
	wps.PPS=512

def AparicionDemonioGenerado(demonio):
	FireBallCool.PlaySound(0)
	ParticulateAppears(demonio.Name)

def AparicionDemonio(demonio):
	darfuncs.UnhideBadGuy(demonio.Name)
	EnemyTypes.EnemyDefaultFuncs(demonio)
	demonio.Alpha      = 1.0
	demonio.SetOnFloor()
	demonio.ImDeadFunc = MuerteDemonio
	AparicionDemonioGenerado(demonio)


def CoolDemon(name):
	demonio=Bladex.GetEntity(name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, AparicionDemonio, (demonio,))




def MuerteDemonio(ent_name):
	demonio=Bladex.GetEntity(ent_name)
	demonio.Data.ImDeadFunc (ent_name)
	darfuncs.UnhideBadGuy("golemla")
	golemla = Bladex.GetEntity("golemla")
	darfuncs.EnciendeEnLlamas(golemla,2,0.077)
	golemla.SelfIlum = 1.0
	Abrepuerta14()

	dm = Bladex.GetEntity("demoniox")
	if dm:
		if dm.Life>0:
			dm.ImDeadFunc = dm.Data.ImDeadFunc
	dm = Bladex.GetEntity("demonioxx")
	if dm:
		if dm.Life>0:
			dm.ImDeadFunc = dm.Data.ImDeadFunc

def ElDemonio(sectorindex,entityname):
	if(entityname == "Player1"):
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb4") )
		Bladex.AddScheduledFunc(Bladex.GetTime()+7, MusicTool.LaunchMusicEvent,( "atm20A" ,) )

		ELDEMOSEC.OnEnter = ""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, CoolDemon,("demoniox",))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, CoolDemon,("demonioxx",))
		Cierrapuerta13()
		darfuncs.EnterSecEvent(2500,-50000,25500,Abrepuerta13)


def Startgendaemon():
	#Cierrapuerta15()
	generadordemon.GenerateEnemy()


def finGeneradaemons(a=0,b=0,c=0):
	Abrepuerta16()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty2") )


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para demon.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def CalculateDamageDemon(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	demon = Bladex.GetEntity(VictimName)

	if (demon.Life > 7950):
		Damage.CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
	else:
		demon.SubscribeToList("Pin")
		AbrePuerta2("")



def Descubre():
	escalon1a.OpenDoor()
	escalon2a.OpenDoor()
	escalon3a.CloseDoor()
	SubeLuzDemonioMaldito()



def Tapa():
	escalon1a.CloseDoor()
	escalon2a.CloseDoor()
	escalon3a.OpenDoor()
	demonlight.Position = -2200.0, -85500.0, 9100.0


def yCloseDDoor(Camera,Frame) :
	pta1D.CloseDoor()
	pta2D.CloseDoor()

def StopDemonCamera(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	gen_GDM.Deaf = 0
	gen_GDM.Blind = 0
	gen_GDM.SetEnemy(char)
	#gen_GDM.Angle = 3.14159/2
	gen_GDM.InitPos = -7098, -91351, 9840
	gen_GDM.Position = -7098, -91351, 9840
	gen_GDM.SetOnFloor()
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	gen_DalGurakGDM.SubscribeToList("Pin")
	escalon1a.CloseDoor()
	escalon2a.CloseDoor()
	demonlight.SubscribeToList("Pin")
	o = Bladex.GetEntity("Demonputch")
	o.FiresIntensity=[ 0 ]
	o.Lights=[ (40.000000,0.10000,(255,151,36)) ]


def SubeDemonio(camera,frame):
	SubeElevadorPalanca()
	Descubre()

def ChangeDemonCamera2(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("DemonioGurak_Camera3.cam",607,-1)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0,FuegoDemonioMaldito,(0.0, -88950.0, 9100.0))
	cam.AddCameraEvent(7,SubeDemonio)
	cam.AddCameraEvent(-1,StopDemonCamera)

def CierraPuertaElevator(camera,frame):
	CierraPuerta2()

def ChangeDemonCamera1(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("DemonioGurak_Camera2.cam",470,607)
	cam.AddCameraEvent(80,CierraPuertaElevator)
	cam.AddCameraEvent(-1,ChangeDemonCamera2)

def TextDemon():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,GameText.WriteText,("M16T2",))

def StartSceneDemonio(sector,entity):
	if entity == "Player1":
		ActDemonSec.OnEnter = ""
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("DemonioGurak_Camera1.cam",0,470)
		cam.AddCameraEvent(130,yCloseDDoor)
		cam.AddCameraEvent(-1,ChangeDemonCamera1)

		SoundScreamDemon.Position = 861, -78412, 9128

		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atm23"))
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("fortaleza-meskal"))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 4.0,TextDemon,())
		Bladex.AddScheduledFunc(Bladex.GetTime() + 37.0,SoundScreamDemon.PlaySound,(1,))

		char.Wuea=Reference.WUEA_ENDED
		char.Angle = 3.14159
		char.SetTmpAnmFlags(1,0,1,0,5,1,0)
		char.LaunchAnmType("demoniogurak")
		char.Position = -23232, -88050,16564
		char.SetOnFloor()

		gen_DalGurakGDM.UnFreeze()
		gen_DalGurakGDM.Position = 3629, -90539, 9113
		gen_DalGurakGDM.PutToWorld()
		gen_DalGurakGDM.Angle = 3.14
		gen_DalGurakGDM.SetTmpAnmFlags(1,0,1,0,5,1)
		gen_DalGurakGDM.Wuea=Reference.WUEA_ENDED
		gen_DalGurakGDM.LaunchAnimation("Dgk_demoniogurak")
		gen_DalGurakGDM.Position = 3629, -90539, 9113
		gen_DalGurakGDM.SetOnFloor()
		#gen_DalGurak

		gen_GDM.UnFreeze()
		gen_GDM.Position = 1800, -80412, 9928
		#gen_GDM.Position = 861, -90412, 9128
		gen_GDM.PutToWorld()
		gen_GDM.Angle = 3.14
		gen_GDM.SetTmpAnmFlags(1,0,1,0,5,1)
		gen_GDM.LaunchAnmType("demoniogurak")
		gen_GDM.SetOnFloor()

		#gen_DalGurak3.UnFreeze()

		Scorer.SetVisible(0)
		ScriptSkip.SkipScriptStart("EscenaMeskalandug")
		#Bladex.DeactivateInput()

def SubeLuzDemonioMaldito():
	demonlight.Move(0,-20,0)
	gen_GDM.SetOnFloor()
	if demonlight.Position[1] >= -88950:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.025,SubeLuzDemonioMaldito,())


def FuegoDemonioMaldito(x,y,z):
	d             = dust.RemueveTierraGen(x,y,z,2000,2000,80,"LargeFire",32,8)
	d[0].YGravity = 0
	d[1].YGravity = 0
	d[0].Velocity = 0.0, -1000.0, 0.0
	d[1].Velocity = 0.0, -1000.0, 0.0
	d[0].Friction = 0.0
	d[1].Friction = 0.0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para DalGurak3Scene.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def CreateArenilla(r = 55,g= 43,b = 13,al = 128,type = Reference.B_PARTICLE_GTYPE_BLEND):
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

def RemueveTierraGen(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-1300.0, pos[2]+v1[2])
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
	v=AuxFuncs.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)

	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-1300.0, pos[2])
	saltatie.ParticleType="Tierra3"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0

	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-1300.0, pos[2])
	saltati2.ParticleType="Tierra2"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3))

def GetBetterPositionDalGurak():
	char = Bladex.GetEntity("Player1")
	pos = char.Position

	MaxDist = 0

	for i in range(NDalPositions):
		v = pos[0] - DalPosition[i][0],pos[2] - DalPosition[i][2]
		dist = v[0] * v[0] + v[1] * v[1]

		if dist >= MaxDist:
			MaxDist = dist
			index = i

	return DalPosition[index]

def ReapearDalGurak3(gen):

	gen_DalGurak3.UnFreeze()
	gen_DalGurak3.PutToWorld()
	gen_DalGurak3.Position = GetBetterPositionDalGurak()
	gen_DalGurak3.Angle = 4.9
	gen_DalGurak3.Blind = 0
	gen_DalGurak3.Deaf = 0
	gen_DalGurak3.SetOnFloor()

def VozYTexto():
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("fortaleza-desafio"))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 4.0,GameText.WriteText,("M16T3",))
	#Bladex.AddScheduledFunc(Bladex.GetTime() + 15.0,GameText.WriteText,("M16T4",))
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("combo1") )

def ActivateDalGurak():
	#EnmGenRnd.ActivateEnemy(gen_DalGurak3)
	gen_DalGurak3.Position = -32794,-118018,8916
	gen_DalGurak3.Angle = 3.14
	gen_DalGurak3.LaunchAnmType("appears3")
	gen_DalGurak3.SetOnFloor()
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("combatedalgurak") )



def StopSceneGurak3(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	#gen_DalGurak3.SubscribeToList("Pin")
	gen_DalGurak3.Freeze()
	gen_DalGurak3.RemoveFromWorld()


def ChangeGurak3Camera6(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera07.cam",970,1050)
	cam.AddCameraEvent(-1,StopSceneGurak3)

def ChangeGurak3Camera5(camera,frame):
	global LaSagradaBlade
	LaSagradaBlade = TieneLaSagradaBlade(PerName = "Player1")

	if LaSagradaBlade:
		print "Cool! tienes la espada de luz!"
	else:
		print "Te jodes por no tener las tablillas!"

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera06.cam",890,970)
	cam.AddCameraEvent(-1,ChangeGurak3Camera6)


def ChangeGurak3Camera4(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera05.cam",700,890)
	cam.AddCameraEvent(-1,ChangeGurak3Camera5)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 9.5,generadorDlGk.GenerateEnemy,())


def ChangeGurak3Camera3(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera04.cam",480,700)
	cam.AddCameraEvent(-1,ChangeGurak3Camera4)

def ChangeGurak3Camera2(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera03.cam",360,480)
	cam.AddCameraEvent(-1,ChangeGurak3Camera3)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.6,CierraPuerta9,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.5, ActivateDalGurak,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, VozYTexto,())


def ChangeGurak3Camera1(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dgk_appears3camera01.cam",160,360)
	cam.AddCameraEvent(-1,ChangeGurak3Camera2)

def StartSceneGurak3(sector=0,entity="Player1"):
	if entity == "Player1":
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("fortaleza-desafio"))
		GurakAparicion3Sec.OnLeave = ""
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("Dgk_appears3Camera02.cam",0,160)
		cam.AddCameraEvent(-1,ChangeGurak3Camera1)

		char.SetTmpAnmFlags(1,0,1,0,5,1)
		char.Position = 3769,-111096,8852
		char.Angle = 3.14
		char.LaunchAnmType("dalgurak_appears3")
		char.SetOnFloor()
		gen_DalGurak3.UnFreeze()

		Scorer.SetVisible(0)
		ScriptSkip.SkipScriptStart("EscenaFINALDALGURAK")
		#Bladex.DeactivateInput()
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ExeMusicEvent, ( Bladex.GetMusicEvent("combo1"),) )

def DisapDal(alpha):
	if alpha <=0.0:
		gen_DalGurak3.Alpha = 1.0
		gen_DalGurak3.UnFreeze()
		MuereDalGurakEscena()
		return
	gen_DalGurak3.Alpha = alpha
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.025, DisapDal,(alpha-0.025,))




def MuereDalGurak(dalname):
	gen_DalGurak3.Data.VeryOldImDeadFunc(dalname)
	gen_DalGurak3.Freeze()
	DisapDal(1)

def MuereDalGurakEscena():
	global LaSagradaBlade

	gen_DalGurak3.Wuea = Reference.WUEA_ENDED
	gen_DalGurak3.SetTmpAnmFlags(1,1,1,0,5,1)
	gen_DalGurak3.LaunchAnmType("dth0")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25,Bladex.TriggerEvent,(38,))

	gen_DalGurak3.Position = -22044,-112426,8780
	gen_DalGurak3.Angle    = -3.14159
	gen_DalGurak3.SetOnFloor()

	char.Position          = -11764.01,-112426,8661.881
	Actions.TurnToFaceEntityNow(char.Name,gen_DalGurak3.Name)
	char.SetOnFloor()
	if LaSagradaBlade:
		darfuncs.LaunchMaxCamera("MuerteGurakCamera01.cam",0,550,FinCamaraFinal)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("FinalBueno"))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,GameText.WriteText,("M16T7",))
	else:
		darfuncs.LaunchMaxCamera("MuerteGurakCamera01.cam",0,550,FinCamaraJodeteFinal)
		Bladex.GetEntity("Camera").AddCameraEvent(480,GrantTowerComplete)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("FinalMalo"))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,GameText.WriteText,("M16T6",)) 

def FinCamaraFinal(cam,num):
	gen_DalGurak3.SubscribeToList("Pin")
	Velaskyalf()

def FinCamaraJodeteFinal(cam,num):
	FinalChungo()
	Bladex.AddScheduledFunc(Bladex.GetTime() + 4.0,GameText.WriteText,("M16T5",))

def GrantTowerComplete(camera,frame):
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.25,Bladex.TriggerEvent,(18,))

def TieneLaSagradaBlade(PerName = "Player1"):
	inv = Bladex.GetEntity(PerName).GetInventory()
	for i in range(inv.nWeapons):
		if (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2") or (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2Barbarian"):
			return 1
	return 0


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ChungEnd.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreaViejoVerde():
	Vejete = Bladex.CreateEntity("VejeteW","Vejete",939567.5,340811.031, 170240.594)
	Vejete.Orientation = (0.500055551529, 0.499942421913, 0.499964922667, -0.500037074089)

	Vejete.Actor=1
	Vejete.Animation="Vejete_rlx_no"
	Vejete.SendSectorMsgs=0
	Vejete.TurnOn()

def ParaCabezaCool(obj_name):
	global Posiciones_De_Cabezas

	o              = Bladex.GetEntity(obj_name)
	pos            = Posiciones_De_Cabezas[obj_name]
	o.Position     = pos[0],pos[1]-400,pos[2]
	o.Orientation  = 0.707105398178, 0.0, -0.707108199596, 0.0

def QueCabeza(pos,C_Mesh = "Knight_N"):
	global Posiciones_De_Cabezas

	K = Bladex.CreateEntity("Cadavre","Skeleton",940447, 341959, 169900,"Person")
	K.SetMesh(C_Mesh)
	K.SetWoundedZone(3, 1)

	o = K.SeverLimb(1)
	o.OnStopFunc = ParaCabezaCool

	bo = Bladex.CreateEntity(o.Name+"Bo", "EstacaFernando",pos[0], pos[1]+500, pos[2])
	bo.Orientation = 0.499999344349, 0.500000655651, 0.499998658895, -0.500001311302
	bo.Scale = 0.5

	K.SubscribeToList("Pin")
	Posiciones_De_Cabezas[o.Name] = pos

	o.Position     = pos[0],pos[1]-400,pos[2]
	o.Orientation  = 0.707105398178, 0.0, -0.707108199596, 0.0

	LuzTerror1=Bladex.CreateEntity(o.Name+"Luz","Entity Spot",pos[0],pos[1],pos[2])
	LuzTerror1.Color=145,80,40
	LuzTerror1.Intensity=25
	LuzTerror1.Precission=0.1
	LuzTerror1.Visible=0
	LuzTerror1.CastShadows=0
	LuzTerror1.Flick=1

	return o,bo,LuzTerror1

def BorraQueCabeza(CabezaK):
	for i in CabezaK:
		i.SubscribeToList("Pin")

def ShowCredits(a,b):
    cam = Bladex.GetEntity("Camera")
    cam.TType   = 0
    cam.SType   = 0

    cam.Position = 915400,322000, 175300
    cam.TPos     = 939500,340811, 170240

    Scorer.SetVisible(0)
    Bladex.ActivateInput()
    Bladex.GetEntity("Player1").Freeze()
    AuxFuncs.FadeFrom(4.0,0)

    import TutorialScorer
    import GameText
    TutorialScorer.ActivateTutorialScorer(Language.LetrasMenuBig)
    GameText.Textos["THE_END"] = ["THE END"]
    TutorialScorer.ShowUC("THE_END",0)
    Credits.Show(1)

def TerminaCool(a,b):
	darfuncs.LaunchMaxCamera("Anakardo_Camera06.cam",101,600,ShowCredits)
	Bladex.GetEntity("Camera").AddCameraEvent(10,GrantBadEnding)
	Bladex.GetEntity("Camera").AddCameraEvent((600-101)*9/10,GrantRank)
	AuxFuncs.FadeTo(20.0,3600)

def GrantBadEnding(camera, frame):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, Bladex.TriggerEvent, (19,))
	
def GrantRank(camera, frame):
	GotoMapVars.GrantRank()

def FinalChungo():
	AuxFuncs.FadeFrom(5.0,0.0,0,0,0)

	darfuncs.LaunchMaxCamera("Anakardo_Camera06.cam",0,100,TerminaCool)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para BurnSkl.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

#def CreaSkeletoLlamarada(o):
def GenerateBurnSkl(o):

	#o.ActionAreaMin=pow(2,6)
	#o.ActionAreaMax=pow(2,7)
	o.CatchOnFire(0,0,0)

	luz             = Bladex.CreateEntity(o.Name+"Luz","Entity Spot",0,0,0)
	#luz.Color       = 200,100,0
	luz.Color       = 181,99,10
	luz.Intensity   = 6
	luz.Precission  = 0.077
	luz.CastShadows = 0
	luz.Visible     = 1
	luz.SizeFactor  = 0
	o.Link(luz)



def ApagaLuz(luz,l):
	luze = Bladex.GetEntity(luz)
	Luz=AuxFuncs.GetSpot(luze)
	Luz.Intensity = 0.0
	Luz.CastShadows = 0
	Fire=AuxFuncs.GetFire(luze)
	Fire.Intensity = 20.0

def AbrirPuertaSkl(entity):
	AbrePuerta4()


def StartBurnSkl2(sector,entity):
	if (entity == "Player1"):
		BrnSklSec2.OnEnter = ""
		generadorBrnSkl.GenerateEnemy()
		Cierrapuerta12()


def finGeneraFuego(a=0,b=0,c=0):
	OnOff.LightSetInens   = 60.0
	OnOff.LightSetRadius  = 0.077
	OnOff.LightSetColor   = (255,70,9)
	OnOff.TurnOnLight("olimpia")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=116085.24, 12233.57, 49133.79		# INICIO

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-29745.23, 4875.73, 51583.46	# SALIDA DE LA GRUTA
	#char.Position=940435.3, 340861.3, 169868.3	#chaos

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=2959.28, -6130.73, 8516.678	# PLANTA BAJA


def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=3000,-27000,10000		# delante de 2� SALA GORDA


def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-11000.42, -25343.55, -4286.24		# DETRAS de 2� SALA GORDA

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-14828.4547, -41895.3344, 23832.574	# DELANTE DE LOS SALAMANDERS

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=4408.1052, -56566.702, 24427.723		# ANTES DE LOS DEMONIOS

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-25345.64, -88045.52, 22333.45		# ANTES DEL GRAN DEMONIO

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=7808.85, -90081.82, 8354.38		# FINAL





#####################################################################################################