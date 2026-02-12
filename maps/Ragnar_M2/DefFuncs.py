##///
##||| Ragnar_M2/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Gate at tower now only plays cut-scene once if you keep pulling the lever.
##||| * Gate cut-scene can now be skipped.
##||| * Escape from prison cell scene can now be skipped.
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
import GotoMapVars
import ScriptSkip
import AbreCam
import MusicTool
import NetSounds






#************************************
#************************************
#**                                **
#** La dichosa cajita del patio... **
#**                                **
#************************************
#************************************


def QuemaLaDichosaCajita(ObjectName,use_from):
	if Actions.StdSetFireToUseFunc(ObjectName,use_from)==1:
		for n in range(7):
			Bladex.GetEntity("AdoqInvPat"+`n+1`).SubscribeToList("Pin")




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para agua.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def eSceneCam(sector,entity) :
	if entity == "Player1":
		scam.OnEnter = ""
		darfuncs.LaunchMaxCamera("ragnar_verPatrulla.cam",0,-1)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("presentapatio"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, MusicTool.LaunchMusicEvent, ("emptyloquesea",))

def CreateCascada1(Cascada,p,d,v,pc,Time = 18,Grav = 8000,PPS = 400):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaC2"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	Espuma2=Bladex.CreateEntity(Cascada+"Espuma2", "Entity Particle System D2",pc[0],pc[1],pc[2])
	Espuma2.D=d[0],d[1],d[2]
	Espuma2.ParticleType="Espuma2"
	Espuma2.PPS=40
	Espuma2.YGravity=0.0
	Espuma2.Friction=0.07
	Espuma2.Velocity=0.0, -1000.0, 0.0
	Espuma2.RandomVelocity=30.0
	Espuma2.RandomVelocity_V=30.0
	Espuma2.Time2Live=10

def CreateEspuma2(Espuma2,pc,d,PPS = 40):
	Espuma2=Bladex.CreateEntity(Espuma2, "Entity Particle System D2",pc[0],pc[1],pc[2])
	Espuma2.D=d[0],d[1],d[2]
	Espuma2.ParticleType="Espuma2"
	Espuma2.PPS=PPS
	Espuma2.YGravity=0.0
	Espuma2.Friction=0.07
	Espuma2.Velocity=0.0, -1000.0, 0.0
	Espuma2.RandomVelocity=30.0
	Espuma2.RandomVelocity_V=30.0
	Espuma2.Time2Live=10


def BorrarCascada1(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")

	Espuma2 = Bladex.GetEntity(cascada+"Espuma2")
	Espuma2.SubscribeToList("Pin")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ApareceCosita(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.UnhideBadGuy("1cos")
		darfuncs.UnhideBadGuy("2cos")
		darfuncs.UnhideBadGuy("4cos")
		sencos=Bladex.GetSector(-136750,15000,69550)
		sencos.OnEnter=""

def ApareceCosita2(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.UnhideBadGuy("1cos1")
		darfuncs.UnhideBadGuy("2cos2")
		darfuncs.UnhideBadGuy("3cos3")
		sencos2=Bladex.GetSector(-125000,8000,50000)
		sencos2.OnEnter=""

def ApareceKOMkngt(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.UnhideBadGuy("KOMkngt")
		senkom=Bladex.GetSector(-74000,-5000,51500)
		senkom.OnEnter=""

def Muere_KT_Patio(entity):
	global N_KT_Patio

	Bladex.GetEntity(entity).Data.DefImDeadFunc(entity)

	if N_KT_Patio == 1:
		AbrePuertaTres()
	else:
		N_KT_Patio = N_KT_Patio - 1

def Aparece4kngt(sectorindex,entityname):
	if entityname == "Player1":
#		darfuncs.UnhideBadGuy("4kngt")
#		darfuncs.UnhideBadGuy("5kngt")
		darfuncs.UnhideBadGuy("5bkngt")
		sen4kngt=Bladex.GetSector(-79000,-8000,70000)
		sen4kngt.OnEnter=""

def Desaparecen1(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.HideBadGuy("1cos")
		darfuncs.HideBadGuy("2cos")
		darfuncs.HideBadGuy("4cos")
		darfuncs.HideBadGuy("1cos1")
		darfuncs.HideBadGuy("2cos2")
		darfuncs.HideBadGuy("3cos3")
		darfuncs.HideBadGuy("KOMkngt")
		darfuncs.HideBadGuy("3kngt")
		darfuncs.HideBadGuy("2kngt")
		sendes1=Bladex.GetSector(-122552.583148, -6321.28490453, 48176.4895)
		sendes1.OnEnter=""

def Aparece227kngt(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.UnhideBadGuy("227kngt")
		sen227kngt=Bladex.GetSector(-135500,-5500,-93000)
		sen227kngt.OnEnter=""

def Aparece228kngt(sectorindex,entityname):
	if entityname == "Player1":
		darfuncs.UnhideBadGuy("228kngt")
		#darfuncs.UnhideBadGuy("229kngt")
		sen228kngt=Bladex.GetSector(-127727.850637, -12613.5904283, -110488.57)
		sen228kngt.OnEnter=""

def KnightDefeatsCos(person):
	Bladex.GetEntity(person).Data.ImDeadFuncX(person)
	Bladex.TriggerEvent(2)

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

	desplazamientos=(500.0, 5850.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevadormovil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador.CloseDoor()
	enmarcha=1

def BajaElevador():

	desplazamientos=(500.0, 5850.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevadormovil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador.OpenDoor()

def ElevadorArriba():

	global enmarcha
	enmarcha=0


def EsperaYBajaElevador():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador, ())


def SubeElevador2():

	desplazamientos=(500.0, 6250.0, 500.0)
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
	desplazamientos=(500.0, 6250.0, 500.0)
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
#*******************************   Definiciones para DrunkWarder.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def IniciaCarcelero(sector_index, entity_name):
	sectoriniccarc.OnEnter=""
	carcelero.Data.Murmura("Carcelero")

def Herido(entity_name):
	carcelero.Data.Molestia("Carcelero")

def Matado(entity_name):
	carcelero.Data.Muere("Carcelero")

############################
#     Apagar ronquidos     #
############################

def ApagaRonquidos(sector_index, entity_name):
	sectorapagaronq.OnEnter=""
	rastmaz1.SubscribeToList("Pin")
	rastmaz2.SubscribeToList("Pin")
	rastmaz3.SubscribeToList("Pin")
	if carcelero.Data.Muerto==0:
		carcelero.Data.ronquidos.Stop()
	if not prisionerovivo1.Data.Muerto:
		darfuncs.HideBadGuy(prisionerovivo1.Name)
	if not prisionerovivo2.Data.Muerto:
		darfuncs.HideBadGuy(prisionerovivo2.Name)




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ChaosKnight.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


###############
#   Eventos   #
###############

def ChaosDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	chaos = Bladex.GetEntity(VictimName)
	Damage.CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
	if chaos.Life < 800:
		Bladex.GetEntity("Player1").SetActiveEnemy("")
		chaos.ImDeadFunc(VictimName)
		chaos.DamageFunc = ""


####################
#     Acciones     #
####################

#####################
#     Aparicion     #
#####################

def ApareceChk():
	Bladex.SetListenerPosition(2)
	chaosk1.Data.Appear()

def ReiniciaCamaraChk(entity_name, camera_element, node):
	cam=Bladex.GetEntity("Camera")
	if (node==1) and (camera_element==1):
		cam.TType=0
		cam.CameraClearPath(1)
	if (node==0) and (camera_element==0):
		cam.SType=0
		cam.CameraClearPath(0)
		cam.SetPersonView("Player1")
		cam.Cut()
		Scorer.SetVisible(1)
		cam.ChangeNodeFunc=""
		ScriptSkip.SkipScriptEnd()
		Bladex.SetListenerPosition(1)
		chaosk1.Blind=0
		chaosk1.Deaf=0

def DetieneCamaraChk(entity_name, camera_element, node):
	global prevtpos
#	print "nodo: "+`node`+"   elemento: "+`camera_element`
	cam=Bladex.GetEntity("Camera")
	if (node==1) and (camera_element==1):
		cam.TType=0
		cam.CameraClearPath(1)
	if (node==9) and (camera_element==0):
		# Path target
		cam.AddCameraNode(1, 3.0, -114000.0, 0.0, -99500.0)
		cam.AddCameraNode(1, 3.0, prevtpos[0], prevtpos[1], prevtpos[2])
		cam.AddCameraNode(1, 3.0, -110000.0, 0.0, -96000.0)
		cam.TType=1
		cam.CameraStartPath(1)
		cam.ChangeNodeFunc=ReiniciaCamaraChk

def MueveCamaraChk(sector_index, entity_name):
	#Bladex.ExeMusicEvent(-1)
	Bladex.KillMusic()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("chaosragnar"))

	global prevtpos
	if entity_name=="Player1":
		sectorcamarachk.OnEnter=""
		ScriptSkip.SkipScriptStart("cacaos")
		cam=Bladex.GetEntity("Camera")
		opos=cam.Position
		tpos=cam.TPos
		prevtpos=cam.TPos
		# Path objetivo
		cam.AddCameraNode(0, 2.00, opos[0], opos[1], opos[2])
		cam.SetCameraStartTangentNode(0, 0, 687.5, 0.0, -1125.0)
		cam.SetCameraEndTangentNode(0, 0, -1000.0, 0.0, -4312.5)

		cam.AddCameraNode(0, 1.0, -100875.0, -1000.0, -98750.0)
		cam.SetCameraStartTangentNode(0, 1, -1250.0, 0.0, -5562.5)
		cam.SetCameraEndTangentNode(0, 1, -3062.5, 0.0, -875.0)

		cam.AddCameraNode(0, 1.5, -103250.0, 0.0, -102125.0)
		cam.SetCameraStartTangentNode(0, 2, -3812.5, 0.0, -1500.0)
		cam.SetCameraEndTangentNode(0, 2, -4187.5, 0.0, 2062.5)

		cam.AddCameraNode(0, 1.50, -107250.0, 1000.0, -101875.0)
		cam.SetCameraStartTangentNode(0, 3, -3937.5, 0.0, 1687.5)
		cam.SetCameraEndTangentNode(0, 3, -2625.0, 0.0, 3000.0)

		cam.AddCameraNode(0, 2.0, -110625.0, 1500.0, -97250.0)
		cam.SetCameraStartTangentNode(0, 4, -2500.0, 0.0, 2750.0)
		cam.SetCameraEndTangentNode(0, 4, -4000.0, 0.0, 0.0)

		cam.AddCameraNode(0, 2.0, -114125.0, 1500.0, -95750.0)
		cam.SetCameraStartTangentNode(0, 5, -4000.0, 0.0, 0.0)
		cam.SetCameraEndTangentNode(0, 5, -1187.5, 0.0, -2687.5)

		cam.AddCameraNode(0, 1.5, -117250.0, 750.0, -97875.0)
		cam.SetCameraStartTangentNode(0, 6, -1312.5, 0.0, -2687.5)
		cam.SetCameraEndTangentNode(0, 6, 1250.0, 0.0, -2687.5)

		cam.AddCameraNode(0, 1.5, -117125.0, -250.0, -100875.0)
		cam.SetCameraStartTangentNode(0, 7, 1125.0, 0.0, -2812.5)
		cam.SetCameraEndTangentNode(0, 7, 2875.0, 0.0, -625.0)

		cam.AddCameraNode(0, 1.5, -114125.0, -1250.0, -103125.0)
		cam.SetCameraStartTangentNode(0, 8, 2500.0, 0.0, -625.0)
		cam.SetCameraEndTangentNode(0, 8, 3500.0, 0.0, 0.0)

		cam.AddCameraNode(0, 1.5, -110500.0, -1750.0, -103250.0)
		cam.SetCameraStartTangentNode(0, 9, 3625.0, 0.0, 0.0)
		cam.SetCameraEndTangentNode(0, 9, 2687.5, 0.0, 2250.0)

		cam.AddCameraNode(0, 3.0, -104000.0, -1750.0, -101375.0)
		cam.SetCameraStartTangentNode(0, 10, 4437.5, 0.0, 3250.0)
		cam.SetCameraEndTangentNode(0, 10, 1375.0, 0.0, 875.0)

		# Path target
		cam.AddCameraNode(1, 3.0, tpos[0], tpos[1], tpos[2])
		cam.AddCameraNode(1, 3.0, -114000.0, 0.0, -99500.0)
		cam.AddCameraNode(1, 3.0, -110000.0, 0.0, -96000.0)

		cam.SType=1
		cam.TType=1
		cam.CameraStartPath(0)
		cam.CameraStartPath(1)
		cam.ChangeNodeFunc=DetieneCamaraChk
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ApareceChk, ())
		Scorer.SetVisible(0)
		chaosk1.UnFreeze()


def ReiniciaCamaraChaosK1():
	global prevPViewType
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.PViewType=prevPViewType
	cam.Cut()
	Bladex.ActivateInput()
	#print("Hello my babe!")

def GiraCamara(obj_name, time):
	global paso_n
	global chaospos
	global init_tpos
	cam=Bladex.GetEntity("Camera")
	vtpos=init_tpos[0]-chaospos[0], 0.0, init_tpos[2]-chaospos[2]
	vtposnorm=B3DLib.Normalize(vtpos)
	paso_n=paso_n+1
	newvtposnorm=vtposnorm[0]*math.cos(paso_n*ANGLE_VARIATION)-vtposnorm[2]*math.sin(paso_n*ANGLE_VARIATION), 0.0, vtposnorm[0]*math.sin(paso_n*ANGLE_VARIATION)+vtposnorm[2]*math.cos(paso_n*ANGLE_VARIATION)
	newvtpos=newvtposnorm[0]*2000, 0.0, newvtposnorm[2]*2000
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	if paso_n==TOTAL_STEPS:
		cam.RemoveFromList("Timer60")
		cam.TimerFunc=""
		ReiniciaCamaraChaosK1()
		AbrePuertaCaos()
		Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, MusicTool.LaunchMusicEvent, ("suspenselento",))

def MuereChaosK1(entity_name):
	global paso_n
	global chaospos
	global init_tpos
	global prevPViewType
	Bladex.DeactivateInput()
	chaosk1.Data.Disappear(entity_name)
	cam=Bladex.GetEntity("Camera")
	char=Bladex.GetEntity("Player1")
	charpos=char.Position
	chaospos=chaosk1.Position
	vtpos=chaospos[0]-charpos[0], 0.0, chaospos[2]-charpos[2]
	vtposnorm=B3DLib.Normalize(vtpos)
	newvtposnorm=vtposnorm[0]*math.cos(3.14159/2.0)-vtposnorm[2]*math.sin(3.14159/2.0), 0.0, vtposnorm[0]*math.sin(3.14159/2.0)+vtposnorm[2]*math.cos(3.14159/2.0)
	newvtpos=newvtposnorm[0]*2000.0, 0.0, newvtposnorm[2]*2000.0
	prevPViewType=cam.PViewType
	cam.PViewType=0
	cam.ESource="ChaosK1"
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	cam.SType=2
	cam.TType=0
	init_tpos=cam.TPos
	paso_n=0
	cam.TimerFunc=GiraCamara
	cam.SubscribeToList("Timer60")
	darfuncs.UnhideBadGuy("22kngt")
	darfuncs.UnhideBadGuy("23kngt")
	#darfuncs.UnhideBadGuy("226kngt")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(24,))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"), 1)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Cascadat.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateCascada2(Cascada,p,d,v,pc,Time = 16,Grav = 13000,PPS = 800):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaC"
	cascada.Friction=0.07
	cascada.RandomVelocity=8.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	espuma=Bladex.CreateEntity(Cascada+"Espuma", "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espuma"
	espuma.PPS=150
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada2(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")

	espuma = Bladex.GetEntity(cascada+"Espuma")
	espuma.SubscribeToList("Pin")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para BurningKnights.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ReduceSmoke3():
	global humo
	humo.RandomVelocity=30.0
	humo.Time2Live=30
	humo.DeathTime=Bladex.GetTime()+3.0

def ReduceSmoke2():
	global humo
	humo.Position=-89500.0, -3200.0, 21750.0
	humo.D=0.0, 0.0, -4250.0
	humo.RandomVelocity=40.0
	humo.Time2Live=40
	Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, ReduceSmoke3, ())

def ReduceSmoke1():
	global humo
	humo.Time2Live=60
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, ReduceSmoke2, ())

def LaunchSmoke():
	global humo
	humo=Bladex.CreateEntity("Humo", "Entity Particle System D2", -89500.0, -4000.0, 20750.0)
	humo.D=0.0, 0.0, -3250.0
	humo.ParticleType="LightDarkSmoke"
	humo.PPS=30
	humo.Time2Live=96
	humo.Velocity=0.0, 0.0, 0.0
	humo.RandomVelocity=60.0
	humo.Friction=0.07
	humo.YGravity=-2000
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, ReduceSmoke1, ())

def SetFireToBoxes (ObjectName,use_from):
	# Call the standard SetFireTo UseFunc
	Actions.StdSetFireToUseFunc(ObjectName,use_from)
	char = Bladex.GetEntity("Player1")
	AuxFuncs.GetSpot(Bladex.GetEntity(char.InvRight)).CastShadows = 0
	Torchs.ExtingueAntorcha(char.InvRight)

	t = Bladex.GetTime()
	t= t + 1

	for n in range(5):
		o=Bladex.GetEntity("BKBox"+`n+1`)
		o.Data.BurnTime=10-n #8-n/2.0

	Bladex.AddScheduledFunc(t, LaunchSmoke, ())

	# Set up some events

	toBurn1 = "BKBox1"
	if ObjectName != toBurn1:
		o=Bladex.GetEntity(toBurn1)
		Reference.debugprint (toBurn1 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		o.UseFunc=0
		Bladex.AddScheduledFunc(t, Actions.SetAlight,(toBurn1,),"BKBox1")

	toBurn2 = "BKBox2"
	if ObjectName != toBurn2:
		o=Bladex.GetEntity(toBurn2)
		Reference.debugprint (toBurn2 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		o.UseFunc=0
		Bladex.AddScheduledFunc(t, Actions.SetAlight,(toBurn2,),"BKBox2")

	toBurn3 = "BKBox3"
	if ObjectName != toBurn3:
		o=Bladex.GetEntity(toBurn3)
		Reference.debugprint (toBurn3 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		o.UseFunc=0
		Bladex.AddScheduledFunc(t, Actions.SetAlight,(toBurn3,),"BKBox3")

	toBurn4 = "BKBox4"
	if ObjectName != toBurn4:
		o=Bladex.GetEntity(toBurn4)
		Reference.debugprint (toBurn4 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		o.UseFunc=0
		Bladex.AddScheduledFunc(t, Actions.SetAlight,(toBurn4,),"BKBox4")

	toBurn5 = "BKBox5"
	if ObjectName != toBurn5:
		o=Bladex.GetEntity(toBurn5)
		Reference.debugprint (toBurn5 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		o.UseFunc=0
		Bladex.AddScheduledFunc(t, Actions.SetAlight,(toBurn5,),"BKBox5")

	toBurn7 = "Robin"
	if ObjectName != toBurn7:
		o=Bladex.GetEntity(toBurn7)
		Reference.debugprint (toBurn7 + ": will be burnt")
		o.Data.UsedBy = ObjectName
		Bladex.AddScheduledFunc(t, o.Data.SetOnFire,(toBurn7,),"Robin")
		Bladex.AddScheduledFunc(t+BoxBurnTime+3,    o.Data.StartRunning,(toBurn7,),"Robin")
		Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,GritaElQuemado,())


	# Should sort the other boxes according to distance from this one
	# add scheduled funcs to set them on fire from nearest to furthest
	# add scheduled funcs to destroy them from topmost to bottommost

def GritaElQuemado():
	BKnightScream.Play(-89366.8447634, -3601.40781545, 19428.7059865,0)
	#print "Gritio de condena y muerte"

def Launch():
	per=Bladex.GetEntity("Robin")
	pos=per.Position		# Should be the boxes position
	per.CatchOnFire (pos[0],pos[1], pos[2])
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,per.Data.StartRunning,("Robin",))



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para antorchas.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Apagala(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	#print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		#print"ExtingeAntorcha"


def Apagala2(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	#print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		#print"ExtingeAntorcha"

def Apagala3(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	#print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		#print"ExtingeAntorcha"

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para escape.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def PolvoRoturaMuro():
	polvorotura=Bladex.CreateEntity("PolvoRotura", "Entity Particle System D2", -110250, 8500, 86000)
	polvorotura.ParticleType="WallDust"
	polvorotura.D=2000, 0, 0
	polvorotura.YGravity=0.0
	polvorotura.Friction=0.2
	polvorotura.PPS=480
	polvorotura.Velocity=0.0, -1000.0, -2000.0
	polvorotura.RandomVelocity=80.0
	polvorotura.Time2Live=60
	polvorotura.DeathTime=Bladex.GetTime()+3.0/60.0



##################
#     Accion     #
##################


def ReiniciaCamara():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
#	print "camara reseteada..."

def DetieneCamara(entity_name, camera_element, node):
#	print "nodo: "+`node`
	if node==1:
		cam=Bladex.GetEntity("Camera")
#		print "me detengo..."
		cam.SType=0
		cam.CameraClearPath(0)
		# Bladex.ActivateInput()
		ScriptSkip.SkipScriptEnd()	# Add
		Scorer.SetVisible(1)		#

def MueveCamara():
	cam=Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
#	print "comienzo trayectoria..."
	cam.AddCameraNode(0, 6.0, -109415, 3150, 82722)
	cam.SetCameraStartTangentNode(0, 0, -6000.0, 0.0, 0.0)
	cam.SetCameraEndTangentNode(0, 0, 0.0, 0.0, 6000.0)
	cam.AddCameraNode(0, 6.0, -113000.0, 6000.0, 84000.0)
	cam.SetCameraStartTangentNode(0, 1, 0.0, 0.0, 6000.0)
	cam.SetCameraEndTangentNode(0, 1, 6000.0, 0.0, 0.0)
	cam.AddCameraNode(0, 6.0, -109500.0, 6000.0, 87500.0)
	cam.SetCameraStartTangentNode(0, 2, 6000.0, 0.0, 0.0)
	cam.SetCameraEndTangentNode(0, 2, 0.0, 0.0, -6000.0)
	cam.SType=1
	cam.TType=0
	cam.CameraStartPath(0)
	cam.ChangeNodeFunc=DetieneCamara
	AnimaPersonaje()

def RoturaMuroCelda():
#	derrumbemurocelda.Play(-109500.0, 7500.0, 86000.0)
	muroceldasup.DoBreak((0.0, 0.0, 2.0), (-109500.0, 7250.0, 85500.0), (0.0, 0.0, 0.0))
	muroceldainf.DoBreak((0.0, 0.0, 2.4), (-109500.0, 8800.0, 85500.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, PolvoRoturaMuro, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ReiniciaCamara, ())

def SonidoRotura():
	derrumbemurocelda.Play(-109500.0, 7500.0, 86000.0)

def SonidoRocasAgua():
	derrumbemuroagua.Play(-109500.0, 13000.0, 88000.0)

def AnimaPersonaje():
	pj=Bladex.GetEntity("Player1")
	pj.SetTmpAnmFlags(1, 1, 1, 0, 1, 1,0)
	punteromuro.RemoveFromWorld()
	pj.LaunchAnmType("push_wall")
	pj.Position=-109500.0, 7750.0, 84300.0
	pj.Angle = 0
	pj.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, SonidoRotura, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.5, SonidoRocasAgua, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.3, RoturaMuroCelda, ())

def DerribaMuro(obj_name, use_from):
	pj=Bladex.GetEntity("Player1")
	# Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	ScriptSkip.SkipScriptStart("escape")
	pj.Position=-109500.0, 7750.0, 84300.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, MueveCamara, ())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para InicioScene.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def Despierta2kngt(sec_idx, ent_name):
	if ent_name=="Player1":
		sec2kngt.OnEnter=""
		k=Bladex.GetEntity("2kngt")
		k.Blind=0
		k.Deaf=0


def StopCameraInicio(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	ScriptSkip.SkipScriptEnd()
	Bladex.SetListenerPosition(1)
	k = Bladex.GetEntity("2kngt")
	inv = k.GetInventory()
	inv.LinkRightHand("None")
	ant = Bladex.GetEntity("Kngtant2")
	ant.Position = -100491.9163488, 1927.6169906, 71910.102509
	ant.Orientation = 0.512640833855, -0.408463507891, -0.678020298481, 0.332633882761
	Actions.TakeObject("2kngt","RagnarEspadaromana2")
	Actions.TakeObject("2kngt","RagnarEsc2kgt")
	#Bladex.CDStop()
	Scorer.SetVisible(1)


def LanzaAnimInicio():
	char= Bladex.GetEntity("Player1")
	char.Angle = 3.1415/2
	char.Position = -111712.383,8742.335,79385.813
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnimation("Kgt_inicio_ragnar")


def RagnarInicio():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicioragnar"))

	if Reference.DEMO_MODE==0:
		GotoMapVars.MapText(2,"D_M2_T1")

	initial_time = Bladex.GetTime()

	Scorer.SetVisible(0)
	AuxFuncs.FadeFrom(2.0)
	Bladex.AddScheduledFunc(initial_time+2.0, GameText.WriteText, ("M2T2",))
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("RagnarCamera1.cam",0,800)
	cam.AddCameraEvent(-1,StopCameraInicio)
	ScriptSkip.SkipScriptStart("1erscript")
	Bladex.SetListenerPosition(2)

	char= Bladex.GetEntity("Player1")
	char.Life = 60
	char.Angle = 3.1415/2
	char.Position = -111712.383,8742.335,79385.813
	#char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	#char.LaunchAnimation("Kgt_inicio_ragnar")
	Bladex.AddScheduledFunc(initial_time+28.0+5.0, LanzaAnimInicio, ())
	carcelero.Data.Duerme(carcelero.Name)


def Apagala4(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	#print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		#print"ExtingeAntorcha"


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-103000, -5000, 21000		# Patio Burning Knight
	char.Angle=4.8

def IrPosicion2():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	#char.Position=-88000, -9000, 500		# Puente levadizo
	#char.Position=	-91479.7264466, -8748.5, -8452.27476857
	char.Position=-80340, -7696, 1430
	char.Angle=1.9

def IrPosicion3():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-100000, 0, -84000		# Antes del Caballero del Caos
	char.Angle=2.95

def IrPosicion4():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-136593, -12748.5, -88000  # Antes de Ragnar mandando enemigos
	char.Angle=1.5

def IrPosicion5():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-101000, 6000, -98000		# En los pendulos
	char.Angle=1.6

def IrPosicion6():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-142263, -29765, -89773		# Antes de Ragnar �ltimo
	char.Angle=3.3

def IrPosicion7():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-100457, -6246, 54321		# Patio con 3 enemigos
	char.Angle=1.9

def IrPosicion8():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-102575.028299, 18237.0, 69621.1240909	# catacumbas
	char.Angle=1.5

def IrPosicion9():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-82795, 1751.5, -35599.0	# Test Action Areas
	char.Angle=1.5


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Pinchos.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DeactivatePinchoOnHit (EntityName, VictimName, ImpX, ImpY, ImpZ):
	pass

def ActivatePinchos(Name,RangeMin,RangeMax):
	pass

def DeactivatePinchos(Name,RangeMin,RangeMax):
	pass


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Pendulos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def MueveLlamaradaGolpe(entity,time):
	llam = Bladex.GetEntity(entity)
	llam.Position = char.Position


def RotarPendulo(Entity,Timer):
	Pen = Bladex.GetEntity(Entity)
	llam = Bladex.GetEntity(Entity+"llamarada")
	P = Pen.Data.DatosPendulo
	Aceleracion = P.fAc * math.sin(P.Angulo)
	P.Vel = P.Vel + Aceleracion
	P.Angulo = P.Angulo + P.Vel
	Pen.RotateRel(P.Piv[0],P.Piv[1],P.Piv[2],P.Axi[0],P.Axi[1],P.Axi[2],P.Vel * P.Dir)
	pos = llam.Position
	P.sound1.Position = pos
	P.sound2.Position = pos


def CreatePendulo(Name):
	Pendulo = Bladex.GetEntity(Name)
	Pen = def_class.PENDULO()
	Pen.Pendulo = Pendulo
	Pendulo.TimerFunc = RotarPendulo
	Pendulo.Data.DatosPendulo = Pen
	luzpendulo=AuxFuncs.GetSpot(Pendulo)
	luzpendulo.Precission=0.5
	luzpendulo.CastShadows=0
	Pen.sound1=Sounds.CreateEntitySound('../../Sounds/Fire-curtains.wav', 'SonidoPenduloNazo'+Name)
	Pen.sound1.Volume=0.8
	Pen.sound1.MinDistance=5000
	Pen.sound1.MaxDistance=10000
	Pen.sound2=Sounds.CreateEntitySound('../../Sounds/fireball-swing.wav', 'SonidoPendulo'+Name)
	Pen.sound2.Volume=0.6
	Pen.sound2.MinDistance=5000
	Pen.sound2.MaxDistance=10000
	Pen.sound3=Sounds.CreateEntitySound('../../Sounds/Flame-hole.wav', 'SonidoGolpe'+Name)
	Pen.sound3.Volume=0.8
	Pen.sound3.MinDistance=10000
	Pen.sound3.MaxDistance=15000

	llamarada=Bladex.CreateEntity(Name+"llamarada", "Entity Particle System D1", 0,0,-4400)
	llamarada.ParticleType="Flame"
	llamarada.YGravity=-2000.0
	llamarada.Friction=0.01
	llamarada.PPS=100
	llamarada.Velocity=0.0, 0.0, 0.0
	llamarada.RandomVelocity=15.0
	llamarada.Time2Live=20
	Pendulo.Link(llamarada)

	return Pen

def PlayerGolpeado(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	if (WeaponName == "Pendulo1" or WeaponName == "Pendulo2"):
		char = Bladex.GetEntity("Player1")
		Pendulo = Bladex.GetEntity(WeaponName)

		P = Pendulo.Data.DatosPendulo
		D = P.Vel * P.Dir
		Angle = char.Angle
		pos = char.Position

		P.sound3.Position = x,y,z
		P.sound3.PlaySound(0)

		llamarada=Bladex.CreateEntity("llamaradagol", "Entity Particle System D1", pos[0],12300,pos[2])
		llamarada.ParticleType="Explode"
		llamarada.YGravity=-2000.0
		llamarada.Friction=0.08
		llamarada.PPS=100
		llamarada.Velocity=0.0, 0.0, 0.0
		llamarada.RandomVelocity=100.0
		llamarada.Time2Live=20
		llamarada.DeathTime=Bladex.GetTime()+0.5
		llamarada.TimerFunc = MueveLlamaradaGolpe
		llamarada.SubscribeToList("Timer30")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, llamarada.RemoveFromList, ("Timer30",))

		NetSounds.AddAnimSound(char,'Kgt_dth_penl', MuerteBarb1, 5)
		NetSounds.AddAnimSound(char,'Kgt_dth_penr', MuerteBarb1, 5)

		char.SetTmpAnmFlags(1,1,1,0,5,1)

		cam = Bladex.GetEntity("Camera")
		cam.SetTravellingView(0,2)
		cam.ETarget = "Player1"

		if D > 0:
			if Angle < 3.14:
				char.LaunchAnmType("dth_penr")
				char.Angle = 1.55
			else:
				char.LaunchAnmType("dth_penl")
				char.Angle = 4.70
		else:
			if Angle < 3.14:
				char.LaunchAnmType("dth_penl")
				char.Angle = 1.55
			else:
				char.LaunchAnmType("dth_penr")
				char.Angle = 4.70

		char.Life = 0

def Activar_Pendulos(sector,Entity):
	global Trampa_Pendulos
	if Entity == "Player1" and Trampa_Pendulos == 0:
		Trampa_Pendulos = 1


def Desactivar_Pendulos(sector,Entity):
	global Trampa_Pendulos
	global DesactivarPendulos
	if Entity == "Player1" and DesactivarPendulos == 1:
		char = Bladex.GetEntity("Player1")
		char.DamageFunc = ExHitFunc[0]
		DesactivarPendulos = 0
		Trampa_Pendulos = 0
		P1.Stop()
		P2.Stop()

def ActivarDesactivadoPendulos(sector,Entity):
	global DesactivarPendulos
	global ExHitFunc
	if Entity == "Player1":
		if DesactivarPendulos == 0:
			char = Bladex.GetEntity("Player1")
			ExHitFunc = [char.DamageFunc]
			char.DamageFunc = PlayerGolpeado
			DesactivarPendulos = 1
			P1.Play()
			P2.Play()




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Levadizo.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ReiniciaCamaraPuente():
	cam=Bladex.GetEntity("Camera")
	cam.Cut()
	cam.SetPersonView("Player1")
	Bladex.SetListenerPosition(1)
	Bladex.ActivateInput()

def DetieneCamaraPuente(entity_name, camera_element, node):
	if node==1:
		cam=Bladex.GetEntity("Camera")
		if camera_element==0:
			cam.SType=0
			cam.CameraClearPath(0)
			cam.TType=0
			cam.CameraClearPath(1)

def MueveCamaraPuente():
	Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	cam=Bladex.GetEntity("Camera")
	# Path objetivo
	cam.AddCameraNode(0, 6.0, -114500.0, -10000.0, -68000.0)
	cam.SetCameraStartTangentNode(0, 0, -6071.0, 0.0, 2821.3)
	cam.SetCameraEndTangentNode(0, 0, 4159.7, 0.0, 4320.8)
	cam.AddCameraNode(0, 6.0, -116500.0, 0.0, -59500.0)
	cam.SetCameraStartTangentNode(0, 1, 3945.5, 0.0, 4213.7)
	cam.SetCameraEndTangentNode(0, 1, 2500.0, 0.0, -1250.0)
	cam.AddCameraNode(0, 6.0, -106000.0, 0.0, -58000.0)
	cam.SetCameraStartTangentNode(0, 2, 2500.0, 0.0, -1250.0)
	cam.SetCameraEndTangentNode(0, 2, -1375.0, 0.0, -2500.0)
	# Path target
	cam.AddCameraNode(1, 6.0, -100500.0, -1000.0, -60000.0)
	cam.SetCameraStartTangentNode(1, 0, -6071.0, 0.0, 2821.3)
	cam.SetCameraEndTangentNode(1, 0, 4159.7, 0.0, 4320.8)
	cam.AddCameraNode(1, 6.0, -104500.0, -2000.0, -65000.0)
	cam.SetCameraStartTangentNode(1, 1, 3945.5, 0.0, 4213.7)
	cam.SetCameraEndTangentNode(1, 1, 2500.0, 0.0, -1250.0)
	cam.AddCameraNode(1, 6.0, -104500.0, 0.0, -70000.0)
	cam.SetCameraStartTangentNode(1, 2, 2500.0, 0.0, -1250.0)
	cam.SetCameraEndTangentNode(1, 2, -1375.0, 0.0, -2500.0)
	cam.SType=1
	cam.TType=1
	cam.CameraStartPath(0)
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=DetieneCamaraPuente


def GolpeFin():

	polvareda=Bladex.CreateEntity("PolvoGolpePuente", "Entity Particle System D2", -108250.0, 2250.0, -70500.0)
	polvareda.D=7500.0, 0.0, 0.0
	polvareda.ParticleType="LargeDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=900
	polvareda.DeathTime=Bladex.GetTime()+3.0/60.0
	polvareda.Velocity=0.0, -1000.0, 0.0
	polvareda.RandomVelocity=80.0
	angulos=(-3.14159/250.0, 3.14159/250.0)
	vel_ang_iniciales=(0.15, 0.0)
	vel_ang_finales=(0.0, 0.1)
	centros=((0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0))
	ejes=((1, 0, 0), (1, 0, 0))
	Objects.NRotateObject(puentelevadizomovil, angulos, vel_ang_iniciales, vel_ang_finales, centros, ejes, Objects.REL)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, ReiniciaCamaraPuente, ())
	puentelevadizo.ExclusionMask=0
	puentelevadizoinv.SubscribeToList("Pin")
	pers1=Bladex.GetEntity("330kngt")
	pers2=Bladex.GetEntity("331kngt")
	if pers1 and pers1.Life>0:
		pers1.UnFreeze()
		pers1.Position=-96619, -9256, -54029
		pers1.Angle=5.68
	if pers2 and pers2.Life>0:
		pers2.UnFreeze()
		pers2.Position=-122000, -8770, -13000
		pers2.GoToJogging=1
		pers2.GoTo(-117000, -8770, -48000)


def InicioApertura():

	puentelevadizomovil.estado=1
	angulos=(3.14159/18.0, 5.0*3.14159/54.0, 3.14159/54.0, -3.14159/220.0, 3.14159/220.0)
	vel_ang_iniciales=(0.1, 0.25, 0.25, 0.25, 0.0)
	vel_ang_finales=(0.25, 0.25, 0.25, 0.0, 0.1)
	son_durante=(looppuentelevadizo, looppuentelevadizo, looppuentelevadizo, "", "")
	son_finales=("", "", atranquepuentelevadizo, "", "")
	centros=((0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0))
	ejes=((1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0))
	Objects.NRotateObject(puentelevadizomovil, angulos, vel_ang_iniciales, vel_ang_finales, centros, ejes, Objects.REL, (), son_durante, son_finales)


def FinApertura():

	MueveCamaraPuente()
	puentelevadizomovil.estado=0
	angulos=(3.14159/9.0, 11.0*3.14159/54.0, 3.14159/54.0)
	vel_ang_iniciales=(0.1, 0.25, 0.25)
	vel_ang_finales=(0.25, 0.25, 0.15)
	son_durante=(looppuentelevadizo, looppuentelevadizo, looppuentelevadizo)
	son_finales=("", golpepuentelevadizo, "")
	centros=((0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0), (0.0, 7500.0, 0.0))
	ejes=((1, 0, 0), (1, 0, 0), (1, 0, 0))
	Objects.NRotateObject(puentelevadizomovil, angulos, vel_ang_iniciales, vel_ang_finales, centros, ejes, Objects.REL, (), son_durante, son_finales, "", (), GolpeFin)


def BajaPuente():

	if (puentelevadizomovil.estado):
		FinApertura()
	else:
		InicioApertura()
		if char.Position[0]>-104500:
			pers=Bladex.GetEntity("331kngt")
		else:
			pers=Bladex.GetEntity("330kngt")
		if pers and pers.Life>0:
			pers.Freeze()
			pers.RemoveFromWorldWithChilds()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Prisioners.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def PrsHerido(entity_name):
  person=Bladex.GetEntity(entity_name)
  person.Data.Agoniza(entity_name)

def PrsMatado(entity_name):
  person=Bladex.GetEntity(entity_name)
  person.Data.Muere(entity_name)

##################################
#     Prisioneros quejandose     #
##################################

def QuejaPeriodica(prisionero):
  if prisionero.Data.Muerto:
    return
  prisionero.Data.Agoniza(prisionero.Name)
  variation=whrandom.uniform(-5.0, 5.0)
  Bladex.AddScheduledFunc(Bladex.GetTime()+15.0+variation, QuejaPeriodica, (prisionero,))

def IniciaPrisioneros(sector_index, entity_name):
  sectorinic.OnEnter=""
  QuejaPeriodica(prisionerovivo1)
  QuejaPeriodica(prisionerovivo2)
  prisioneromuerto.Life=-20


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##funciones abrir-cerrar##
def AbrePuertaLlaveen():
	puertaen.OpenDoor()

def Abrerastmaz1():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastmaz1
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarastmaz1():

	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastmaz1
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerastmaz2():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastmaz2
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarastmaz2():

	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastmaz2
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerastmaz3():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastmaz3
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarastmaz3():

	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastmaz3
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CierraPuertaLlaveen(sectorindex,entityname):
	puertaen.CloseDoor()

def AbrePuerta1():
	global p1yaabierta
	puerta1.OpenDoor()
	if not p1yaabierta:
		pers=Bladex.GetEntity("330kngt")
		pers.Position=-79000, -9256, -42000
		pers.GoTo(-96619, -9256, -54029)
		p1yaabierta=1

def CierraPuerta1():
	puerta1.CloseDoor()

def AbrePuertaLlave2():
	puerta2.OpenDoor()

def CierraPuertaLlave2():
	puerta2.CloseDoor()

def AbrePuertaLlave3():
	puerta3.OpenDoor()

def CierraPuertaLlave3():
	puerta3.CloseDoor()

def CierraPuertaLlave33(sectorindex,entityname):
	puerta3.CloseDoor()

def AbrePuertaLlave4():
	puerta4.OpenDoor()

def CierraPuertaLlave4():
	puerta4.CloseDoor()

def AbrePuertaLlave5():
	puerta5.OpenDoor()

def CierraPuertaLlave5():
	puerta5.CloseDoor()

def AbrePuertaLlave6():
	global armaduraencontrada
	puerta6.OpenDoor()
	if armaduraencontrada:
		return
	armaduraencontrada=1
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("recompensa"))

def CierraPuertaLlave6():
	puerta6.CloseDoor()

def AbrePuertaLlave9():
	puerta9.OpenDoor()

def CierraPuertaLlave9():
	puerta9.CloseDoor()

def AbrePuertaLlave7():
	puerta7.OpenDoor()

def CierraPuertaLlave7():
	puerta7.CloseDoor()

def AbrePuerta8():
	puerta8.OpenDoor()

def CierraPuerta8():
	puerta8.CloseDoor()

def AbrePuertaLlave10():
	puerta10.OpenDoor()

def CierraPuertaLlave10():
	puerta10.CloseDoor()
##funciones abrir-cerrar##

def FinCamaraRaspat():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	# Bladex.ActivateInput()

GateWasOpened = 0 
def Abrerastpat():
	global GateWasOpened
	desplazamientos=(1650.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 1000)
	vel_finales=(1000.0, 500)

	#sonidos asociados a la puerta-objeto rastpat
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastpatdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	if not GateWasOpened:
		# Bladex.DeactivateInput()
		ScriptSkip.SkipScriptStart("gate_open")
		Bladex.SetListenerPosition(2)
		AuxFuncs.MoveCamFromTo(-95150.0, -14250.0, 42200.0, -91650.0, -9950.0, 49250.0, -101450.0, -12350.0, 34600.0, -93650.0, -7200.0, 39800.0, 6.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, FinCamaraRaspat, ())
		GateWasOpened = 1


def Cierrarastpat():

	desplazamientos=(1650.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastpat
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastpatdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarastfin(sectorindex,entityname):

	if entityname=='Player1':

		desplazamientos=(1980.0, 1950.0, 700.0, 700.0, 250.0, 250.0)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
		vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

		#sonidos asociados a la puerta-objeto rastfin
		son_iniciales=("", "", "", "", "", "")
		son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
		Objects.NDisplaceObject(rastfindin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
		sr1.OnEnter=""

def AbrePuertaCaos():
	puertacaos.OpenDoor()

def CierraPuertaCaos(sectorindex,entityname):
	puertacaos.CloseDoor()

def CierraPuertaRagnar():
	puertaragnar.CloseDoor()
##funciones abrir-cerrar##

def Abrerastrag():

	desplazamientos=(2250.0, 1000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastrag
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastragdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarastrag():

	desplazamientos=(2250.0, 1000.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastrag
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastragdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbrePuertaTres():
	puertatres.OpenDoor()
	enem = Bladex.GetEntity("tres1kngt")
	enem.Blind = 0
	enem.Deaf = 0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_pinchos.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


#############################################################################################
#
#										PINCHOS
#
#############################################################################################

def ReactivarTecho():
	global Trampa_Estado
	#print ("Reactivando Trampa")
	Sonido_Trampa_Reactivada.Play(-124000,-25000,-100000,0)
	Trampa_Estado = 1;

def TrampaSubida(sld_name):
	polvo1=Bladex.CreateEntity("Polvo1", "Entity Particle System D2", -123000, -27000, -96000)
	polvo1.ParticleType="SpDust"
	polvo1.D=-3600, 0, 0
	polvo1.YGravity=0.0
	polvo1.Friction=0.2
	polvo1.PPS=480
	polvo1.Velocity=0.0, 3000.0, -2000.0
	polvo1.RandomVelocity=30.0
	polvo1.Time2Live=60
	polvo1.DeathTime=Bladex.GetTime()+5.0/60.0
	polvo2=Bladex.CreateEntity("Polvo2", "Entity Particle System D2", -123000, -27000, -104500)
	polvo2.ParticleType="SpDust"
	polvo2.D=-3600, 0, 0
	polvo2.YGravity=0.0
	polvo2.Friction=0.2
	polvo2.PPS=480
	polvo2.Velocity=0.0, 3000.0, 2000.0
	polvo2.RandomVelocity=30.0
	polvo2.Time2Live=60
	polvo2.DeathTime=Bladex.GetTime()+5.0/60.0
	DesactivarPincho("Pincho1")
	DesactivarPincho("Pincho2")
	DesactivarPincho("Pincho3")
	DesactivarPincho("Pincho4")
	DesactivarPincho("Pincho5")
	DesactivarPincho("Pincho6")
	DesactivarPincho("Pincho7")
	DesactivarPincho("Pincho8")
	DesactivarPincho("Pincho9")
	DesactivarPincho("Pincho10")
	DesactivarPincho("Pincho11")
	Sonido_Trampa_Subiendo1.Stop()
	Sonido_Hit2.Play(-124000,-25000,-100000,0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,ReactivarTecho,())


def SubirTecho():
	arenilla1=Bladex.CreateEntity("Arenilla1", "Entity Particle System D2", -123000, -26500, -96000)
	arenilla1.D=-3600, 0, 0
	arenilla1.ParticleType="Sand"
	arenilla1.YGravity=4900.0
	arenilla1.Friction=0.2
	arenilla1.RandomVelocity=10.0
	arenilla1.PPS=512
	arenilla1.Time2Live=32
	arenilla1.DeathTime=Bladex.GetTime()+6.5
	arenilla2=Bladex.CreateEntity("Arenilla2", "Entity Particle System D2", -123000, -26500, -104500)
	arenilla2.D=-3600, 0, 0
	arenilla2.ParticleType="Sand"
	arenilla2.YGravity=4900.0
	arenilla2.Friction=0.2
	arenilla2.RandomVelocity=10.0
	arenilla2.PPS=512
	arenilla2.Time2Live=32
	arenilla2.DeathTime=Bladex.GetTime()+6.5
	Techo_Pinchos1.sld_area().OnStopFunc = TrampaSubida
	Techo_Pinchos1.sld_area().SlideTo(0,-100,-200)
	Techo_Pinchos2.sld_area().SlideTo(0,-100,-200)
	Techo_Pinchos3.sld_area().SlideTo(0,-100,-200)
	Techo_Pinchos1.sld_area().HitFunc = None
	Techo_Pinchos2.sld_area().HitFunc = None
	Techo_Pinchos3.sld_area().HitFunc = None
	Sonido_Trampa_Subiendo1.Play(-124000,-22000,-100000,0)
	Sonido_Trampa_Subiendo2.Play(-124000,-22000,-100000,0)


def BajarTecho():
	Techo_Pinchos1.sld_area().OnStopFunc = TrampaBajada
	Techo_Pinchos1.sld_area().SlideTo(4600,6600,4800)
	Techo_Pinchos2.sld_area().SlideTo(4600,6600,4800)
	Techo_Pinchos3.sld_area().SlideTo(4600,6600,4800)
	Techo_Pinchos1.sld_area().HitFunc = Doors.DoorHit
	Techo_Pinchos2.sld_area().HitFunc = Doors.DoorHit
	Techo_Pinchos3.sld_area().HitFunc = Doors.DoorHit
	#Sonido_Trampa_Bajando1.Play(-124000,-25000,-100000,0)
	Sonido_Trampa_Bajando2.Play(-124000,-25000,-100000,0)


def TrampaBajada(sld_name):
	#Char = Bladex.GetEntity("Player1")
	polvo3=Bladex.CreateEntity("Polvo3", "Entity Particle System D2", -123000, -22000, -96000)
	polvo3.ParticleType="SpDust"
	polvo3.D=-3600, 0, 0
	polvo3.YGravity=0.0
	polvo3.Friction=0.2
	polvo3.PPS=480
	polvo3.Velocity=0.0, -2000.0, 4000.0
	polvo3.RandomVelocity=40.0
	polvo3.Time2Live=60
	polvo3.DeathTime=Bladex.GetTime()+3.0/60.0
	polvo4=Bladex.CreateEntity("Polvo4", "Entity Particle System D2", -123000, -22000, -104500)
	polvo4.ParticleType="SpDust"
	polvo4.D=-3600, 0, 0
	polvo4.YGravity=0.0
	polvo4.Friction=0.2
	polvo4.PPS=480
	polvo4.Velocity=0.0, -2000.0, -4000.0
	polvo4.RandomVelocity=40.0
	polvo4.Time2Live=60
	polvo4.DeathTime=Bladex.GetTime()+3.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,SubirTecho,())
	#Sonido_Trampa_Bajando1.Stop()
	#Sonido_Trampa_Bajando2.Stop()
	Sonido_Hit2.Play(-124000,-22000,-100000,0)

##############	TECHO ############

def PinchoSigueTecho(Nombre,Tiempo):
	Techo = Bladex.GetEntity("TechoPinchos")
	Pincho = Bladex.GetEntity(Nombre)
	X = Pincho.Position[0]
	Z = Pincho.Position[2]
	D = Techo.Displacement
	Y = -26100 + D
	Pincho.Position = X,Y,Z

def ActivarPincho(Nombre):
	Pincho = Bladex.GetEntity(Nombre)
	Bladex.CreateTimer("Timer60",1.0/60.0)
	#Pincho.Weapon = 1
	Pincho.Solid = 0
	#Pincho.Static = 1
	Pincho.TimerFunc = PinchoSigueTecho
	Pincho.SubscribeToList("Timer60")

def DesactivarPincho(Nombre):
	Pincho = Bladex.GetEntity(Nombre)
	Pincho.RemoveFromList("Timer60")

def DesactivarTrampaPinchos():
	global Trampa_Estado
	Trampa_Estado = 0
	#Techo_Pinchos.OpenDoor()

	SubirTecho()

def ActivarTecho():
	#Techo_Pinchos.CloseDoor()
	BajarTecho()
	ActivarPincho("Pincho1")
	ActivarPincho("Pincho2")
	ActivarPincho("Pincho3")
	ActivarPincho("Pincho4")
	ActivarPincho("Pincho5")
	ActivarPincho("Pincho6")
	ActivarPincho("Pincho7")
	ActivarPincho("Pincho8")
	ActivarPincho("Pincho9")
	ActivarPincho("Pincho10")
	ActivarPincho("Pincho11")


def ActivarTrampaPinchos(Sector,Entity_Name):
	global Trampa_Puerta_Abandonada
	global Trampa_Estado
	#print("Entrando Trampa")
	if (Trampa_Estado==1 and Trampa_Puerta_Abandonada==0):
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,ActivarTecho,())
		Sonido_Trampa_Activada.Play(-124000,-25000,-100000)
		#print("Trampa Activada")
		Trampa_Puerta_Abandonada = 0
		Trampa_Estado = 0

def AbandonarPuerta(Sector,Entity_Name):
	global Trampa_Puerta_Abandonada
	Trampa_Puerta_Abandonada = 1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_flechas.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def PararFlecha(Arrow_P,Tiempo):
	Arrow = Bladex.GetEntity(Arrow_P.Lanzar)
	Arrow.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
	Arrow.MessageEvent(Reference.MESSAGE_STOP_TRAIL, 0,0)
	Arrow.Orientation	= Arrow_P.Orientation
	Arrow.Position		= Arrow_P.Position
	Arrow.Scale			= Arrow_P.Scale
	#Arrow_P.Sound.Stop()


def PasoPolvo(polvoposition, paso, trampa):

	if paso:
		if (trampa):
			despl=1150
		else:
			despl=-1150
		polvoflecha=Bladex.CreateEntity("PolvoFlecha3", "Entity Particle System D1", polvoposition[0]+despl, polvoposition[1], polvoposition[2])
		polvoflecha.ParticleType="Dust3"
		polvoflecha.YGravity=0.0
		polvoflecha.Friction=0.2
		polvoflecha.PPS=60
		polvoflecha.Time2Live=15
		polvoflecha.DeathTime=Bladex.GetTime()+3.0/60.0
	else:
		if (trampa):
			despl=950
		else:
			despl=-950
		polvoflecha=Bladex.CreateEntity("PolvoFlecha2", "Entity Particle System D1", polvoposition[0]+despl, polvoposition[1], polvoposition[2])
		polvoflecha.ParticleType="Dust2"
		polvoflecha.YGravity=0.0
		polvoflecha.Friction=0.2
		polvoflecha.PPS=60
		polvoflecha.Time2Live=15
		polvoflecha.DeathTime=Bladex.GetTime()+3.0/60.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0/60.0, PasoPolvo, (polvoposition, 1, trampa),"PasoPolvo")



def LanzarFlecha(Arrow_P,Tiempo):
	Arrow = Bladex.GetEntity(Arrow_P.Lanzar)

	if (Arrow_P.Estado == 1):
		#print ("Lanzando",Arrow_P.Lanzar)
		polvoposition=Arrow.Position[0], Arrow.Position[1]+70, Arrow.Position[2]
		char=Bladex.GetEntity("Player1")
		if (char.Position[0]<-135000.0):
			despl=750
			trampa=1
		else:
			despl=-750
			trampa=0
		Arrow.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		Arrow.MessageEvent(Reference.MESSAGE_START_TRAIL, 0,0)

		Arrow.Fly(40000 * Arrow_P.Avance,0,0)
		#Arrow_P.Ultimo_Lanzamiento = Bladex.GetTime()
		Arrow_P.Sound.Play(Arrow.Position[0],Arrow.Position[1],Arrow.Position[2],0)
		polvoflecha=Bladex.CreateEntity("PolvoFlecha", "Entity Particle System D1", polvoposition[0]+despl, polvoposition[1], polvoposition[2])
		polvoflecha.ParticleType="Dust1"
		polvoflecha.YGravity=0.0
		polvoflecha.Friction=0.2
		polvoflecha.PPS=60
		polvoflecha.Time2Live=15
		polvoflecha.DeathTime=Bladex.GetTime()+3.0/60.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0/60.0, PasoPolvo, (polvoposition, 0, trampa),"PasoPolvo")
		Bladex.AddScheduledFunc(Bladex.GetTime() + Arrow_P.Tiempo_Parada,PararFlecha,(Arrow_P,0),"PararFlecha")
		Bladex.AddScheduledFunc(Bladex.GetTime() + Arrow_P.Tiempo_Lanzamiento,LanzarFlecha,(Arrow_P,0),"LanzarFlecha")



def ActivarFlecha(Name,Tiempo):
	Arrow = Bladex.GetEntity(Name)
	#print(Arrow.Data.Lanzar," Activado")
	Arrow.Data.Estado = 1
	Bladex.AddScheduledFunc(Tiempo,LanzarFlecha,(Arrow.Data,0),"LanzarFlecha")

def DesactivarFlecha(Name):
	Arrow = Bladex.GetEntity(Name)
	#print(Arrow.Data.Lanzar," Desactivado")
	Arrow.Data.Estado = 0

def ActivarTrampaFlechas(sector,entity_Name):
	global Trampa_Flechas_Activada1
	global Trampa_Flechas
	global Player_Intro1

	if (entity_Name == "Player1"):
		if (Trampa_Flechas == 0):
			#print("Trampa Flechas Activada")
			Player_Intro1 = 1
			if (Trampa_Flechas_Activada1 == 0):
				Tiempo = Bladex.GetTime()
				ActivarFlecha("Pivote10",Tiempo + 1)#0.6)
				ActivarFlecha("Pivote11",Tiempo + 0)
				ActivarFlecha("Pivote12",Tiempo + 1.5)#0.9)
				ActivarFlecha("Pivote13",Tiempo + 0.5)#0.3)
				char = Bladex.GetEntity("Player1")
				Sonido_Flechas_Activadas.Play(-141000,-7000,char.Position[2],0)
				Trampa_Flechas_Activada1 = 1


		Trampa_Flechas = Trampa_Flechas + 1

def DesactivarTrampa1():
	global Trampa_Flechas_Activada1
	global Player_Intro1
	global Tiempo_DesactivacionFlechas1
	Tiempo = Bladex.GetTime()
	#print ("Bucle Desactivacion: Tiempo Actual ",Tiempo,"Tiempo Des ",Tiempo_DesactivacionFlechas1)
	if (Tiempo_DesactivacionFlechas1 <= Tiempo):
		if (Player_Intro1 == 0):
			#print("Desactivado")
			DesactivarFlecha("Pivote10")
			DesactivarFlecha("Pivote11")
			DesactivarFlecha("Pivote12")
			DesactivarFlecha("Pivote13")
			Trampa_Flechas_Activada1 = 0
			Sonido_Flechas_Desactivadas.Play(-141000,-7000,-100000,0)
			return
	else:
		#print("Configurada Siguiente Desactivacion")
		Bladex.AddScheduledFunc(Tiempo_DesactivacionFlechas1,DesactivarTrampa1,(),"DesactivarTrampa1")


def DesactivarTrampaFlechas(sector,entity_Name):
	global Tiempo_DesactivacionFlechas1
	global Trampa_Flechas
	global Player_Intro1

	if (entity_Name == "Player1"):
		Trampa_Flechas = Trampa_Flechas - 1

		if (Trampa_Flechas == 0):
			#print("Trampa Flechas Desactivada")
			Player_Intro1 = 0
			Tiempo = Bladex.GetTime()
			if (Tiempo_DesactivacionFlechas1 <= Tiempo):
				Bladex.AddScheduledFunc(Tiempo + 6.0,DesactivarTrampa1,(),"DesactivarTrampa1")
			Tiempo_DesactivacionFlechas1 = Tiempo + 6.1


def ActivarTrampaFlechas2(sector,entity_Name):
	global Trampa_Flechas_Activada2
	global Trampa_Flechas
	global Player_Intro2

	if (entity_Name == "Player1"):
		if (Trampa_Flechas == 0):
			Player_Intro2 = 1
			if (Trampa_Flechas_Activada2 == 0):
				#print("Trampa Flechas Activada")
				Tiempo = Bladex.GetTime()
				ActivarFlecha("Pivote0",Tiempo + 0)
				ActivarFlecha("Pivote1",Tiempo + 0.5)#0.3)
				ActivarFlecha("Pivote2",Tiempo + 1)#0.6)
				ActivarFlecha("Pivote3",Tiempo + 1.5)#0.9)
				Sonido_Flechas_Activadas.Play(-125000,-7000,char.Position[2],0)
				Trampa_Flechas_Activada2 = 1

		Trampa_Flechas = Trampa_Flechas + 1

def DesactivarFlechas2():
	global Trampa_Flechas_Activada2
	global Player_Intro2

	Tiempo = Bladex.GetTime()
	if (Tiempo_DesactivacionFlechas2 <= Tiempo):
		if (Player_Intro2 == 0):
			Trampa_Flechas_Activada2 = 0
			DesactivarFlecha("Pivote0")
			DesactivarFlecha("Pivote1")
			DesactivarFlecha("Pivote2")
			DesactivarFlecha("Pivote3")
			Sonido_Flechas_Desactivadas.Play(-125000,-7000,-100000,0)
			return
	else:
		Bladex.AddScheduledFunc(Tiempo_DesactivacionFlechas2,DesactivarFlechas2,(),"DesactivarFlechas2")


def DesactivarTrampaFlechas2(sector,entity_Name):
	global Tiempo_DesactivacionFlechas2
	global Trampa_Flechas_Activada2
	global Trampa_Flechas
	global Player_Intro2

	if (entity_Name == "Player1"):
		Trampa_Flechas = Trampa_Flechas - 1

		if (Trampa_Flechas == 0):
			#print("Trampa Flechas Desactivada")
			Player_Intro2 = 0
			Tiempo = Bladex.GetTime()
			if (Tiempo_DesactivacionFlechas2 <= Tiempo):
				Bladex.AddScheduledFunc(Tiempo + 6.0,DesactivarFlechas2,(),"DesactivarFlechas2")
			Tiempo_DesactivacionFlechas2 = Tiempo + 6.0

def StickArrow(Sticker,Stick):
	#print (Sticker," Clavada en ",Stick)
	Arrow = Bladex.GetEntity(Sticker)
	Flecha = Arrow.Data
	NewArrow = Traps_C.Prueba(Flecha.Nombre,Flecha.Flechas_Clavadas)
	Flecha.Flechas_Clavadas = Flecha.Flechas_Clavadas + 1
	Arrow = Bladex.CreateEntity(NewArrow,"Flecha",Flecha.Position[0],Flecha.Position[1],Flecha.Position[2])
	Arrow.Orientation = Flecha.Orientation
	Arrow.Scale = Flecha.Scale
	Arrow.Arrow = 1
	Flecha.Lanzar = NewArrow
	Arrow.Data = Flecha
	Arrow.StickFunc = StickArrow


def InitArrow(Name,Displacement):
	A = def_class.FLECHA()
	A.Avance = Displacement
	Arrow = Bladex.GetEntity(Name)

	A.Sound = Bladex.CreateSound('../../Sounds/dart-shoot.wav', 'LaunchArrow')
	A.Sound.Volume=0.5
	A.Sound.MinDistance=2000
	A.Sound.MaxDistance=15000

	A.Nombre      = Name
	A.Lanzar	  = Name
	A.Position    = Arrow.Position
	A.Orientation = Arrow.Orientation
	A.Scale       = Arrow.Scale

	Arrow.Data = A
	Arrow.StickFunc = StickArrow

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Talking_Knights.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


#######################################################
# Setup the sector
#######################################################

def LookAtTerry():
	# Lets set up a temporary camera to watch the fun
	#pdb.set_trace()
	cam = Bladex.GetEntity("Camera")
	cam.LookAtTime=5
	cam.Position=-84589, -9783, -6064
	cam.LookAt("Terry")

def OnEnterScript(SectorIndex, EntityName):
	if EntityName=="Player1":
		#pdb.set_trace()
		Reference.debugprint ("Player1 has entered sector "+`SectorIndex`)

		eric = Bladex.GetEntity ("Eric")
		if eric:
			#eric.Position=-91610, -8748, -7916
			eric.Angle=4.4
			eric.Data.StartTalking1 ()
		terry = Bladex.GetEntity ("Terry")
		#LookAtTerry()
		if terry:
			#terry.Position =-86500, -8748, -7250
			terry.Angle=1.5
			terry.Data.StartTalking2 ()
		sec=Bladex.GetSector(SectorIndex)
		sec.OnEnter=0
		Bladex.CheckPyErrors()

def Reset():
	targetSec=Bladex.GetSector(-80340, -7696, 1430)
	targetSec.OnEnter=OnEnterScript


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Ragnar_Actions.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def FuncionNula(entity_name):
	pass

def OnRagnarDie(entity_name):
	#print "On Kill Ragnar a crazy knight"
	ragnar.Data.VeryOldImDeadFunc(entity_name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(25,))

####################################################
#     Lanza sonido activacion trampa cuchillas     #
####################################################

def SonidoActivacion(sector_index, entity_name):
	if entity_name=="Player1":
		cuchillasactivadas.Play(-141790.0, -23249.0, -99000.0, 0)
		sectorsonidocuchillas.OnEnter=""


def RagnarDesaparece(newpos=(0.0, 0.0, 0.0), seefunc=FuncionNula):
	ragnar.LaunchAnimation("Rgn_rlx_1h")
	ragnar.Position=newpos
	ragnar.SeeFunc=seefunc
	ragnar.SetOnFloor()


def GuardaEnGuardia(person):
#	print "En guardia!"
	person.LaunchAnimation("Tkn_rlx_f")
	person.SetOnFloor()

def GuardaAtaca(person):
#	print "Al ataque!"
	person.Blind=0
	person.Data.LaunchMyWatch(person.Name)

def VozMatadle():
	matadle.Play(-142500.0, -12750.0, -110700.0, 0)

def DesactivaCambiosMusicaGuardaespaldas():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicatorre"))
	Bladex.RemoveTriggerSectorFunc("MusicaTorre4", "OnEnter")
	Bladex.RemoveTriggerSectorFunc("Silencio7", "OnEnter")

def RagnarEscapaEnemigos():
	ragnar.Position=-142500.0, -12750.0, -110700.0
	ragnar.SetOnFloor()
	ragnar.Data.CommandingAndEscaping()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, VozMatadle, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, GuardaEnGuardia, (guarda1,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, GuardaEnGuardia, (guarda2,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, GuardaAtaca, (guarda1,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, GuardaAtaca, (guarda2,))
	newpos=(-141790.0, -23249.0, -109700.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, RagnarDesaparece, (newpos, RagnarVeJugadorCuchillas))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, DesactivaCambiosMusicaGuardaespaldas, ())


def RagnarVeJugadorEnemigos(entity_name):
#	print "Ragnar te ha visto!"
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("ragnarguardaesp"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RagnarEscapaEnemigos, ())
	ragnar.SeeFunc=FuncionNula
	AbreCam.LastTime = 0.01
	AbreCam.PTS = [
	       ((-141702.115016, -14316.6380986, -87909.7057797), (-142366.840758, -13202.867904, -92220.6355477), 0.75),
	       ((-144069.469394, -13937.8515248, -100755.479001), (-143651.345295, -13319.4865829, -103140.823385), 1.0),
	       ((-141904.34761, -13938.8061199, -100580.194813), (-142164.701223, -13320.5010469, -102987.636615), 3.0)]
	AbreCam.AbreCam()

##########################################################
#     Ragnar activando trampa de cuchillas y huyendo     #
##########################################################

def RagnarEscapaCuchillas():
	ragnar.Position = (-141790.0, -23249.0, -109700.0)
	ragnar.SetOnFloor()
	ragnar.Data.Escaping(1)
	newpos=(-128000.0, -31750.0, -92000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, RagnarDesaparece, (newpos,))


def RagnarVeJugadorCuchillas(entity_name):
#	print "Ragnar te ha visto!"
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, RagnarEscapaCuchillas, ())
	ragnar.SeeFunc=FuncionNula

###
# Final con fundido
###

def FundidoFin():
	char=Bladex.GetEntity("Player1")
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	AuxFuncs.FadeTo(2.0, 31.0)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("documentoragnar"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, GameText.WriteText, ("M2T4",))       # aparicion text en pantalla

	time = 28
	if Reference.DEMO_MODE==0:
		Bladex.AddScheduledFunc(Bladex.GetTime()+time,GotoMapVars.EndOfLevel,())
		GotoMapVars.MapText(2,"D_M2_T2")
	else:
		AuxFuncs.setDemoBg(time)


def PolvoPuertaRagnar():
	polvopuertarg=Bladex.CreateEntity("PolvoPuertaRg", "Entity Particle System D2", -143875, -30275, -95625)
	polvopuertarg.ParticleType="RgDoorDust"
	polvopuertarg.D=3250, 0, 0
	polvopuertarg.YGravity=0.0
	polvopuertarg.Friction=0.2
	polvopuertarg.PPS=960
	polvopuertarg.Velocity=0.0, -2600.0, -2600.0
	polvopuertarg.RandomVelocity=40.0
	polvopuertarg.Time2Live=40
	polvopuertarg.DeathTime=Bladex.GetTime()+3.0/60.0

def CamaraSigueJugador(obj_name, time):
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	cam.TPos=char.Position

def ReiniciaCamaraRagnar():
	global original_dist
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
#	cam.Dist=original_dist
	cam.Cut()
	cam.Dist=original_dist
#	AuxFuncs.ActivateKeyboard()
	Bladex.ActivateInput()

def CamaraSigueRagnar(obj_name, time):
	cam=Bladex.GetEntity("Camera")
	#cam.TPos=ragnar.Position
	cam.TPos=ragnar.Position[0], ragnar.Position[1]+2300.0, ragnar.Position[2]

def RagnarAtaca():
	ragnar.Blind=0
	ragnar.Deaf=0
	ragnar.SeeFunc = ragnar.Data.StdSeeTheEnemy
	ragnar.Data.LaunchMyWatch(ragnar.Name)

def RagnarEnGuardia():
#	ragnar.LaunchAnmType("rlx_f")
	ragnar.LaunchAnimation("Rgn_rlx_f")
	person.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, RagnarAtaca, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ReiniciaCamaraRagnar, ())

def RagnarSePara(entity_name):
	cam=Bladex.GetEntity("Camera")
	cam.RemoveFromList("Timer60")
	cam.TimerFunc=""
	ragnar.Face(1.05)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RagnarEnGuardia, ())

def RagnarSigueAndando(entity_name):
	global nodo_n
#	print "estoy en el nodo "+`nodo_n`
	nodo_pos=[(-130500, -32750, -101250), (-132500, -32750, -102500), (-135000, -32750, -103000)]
	ragnar.GoTo(nodo_pos[nodo_n][0], nodo_pos[nodo_n][1], nodo_pos[nodo_n][2])
	if nodo_n==2:
		ragnar.RouteEndedFunc=RagnarSePara
	else:
		nodo_n=nodo_n+1
		ragnar.RouteEndedFunc=RagnarSigueAndando

def RagnarEmpiezaAndar():
	cam=Bladex.GetEntity("Camera")
#	dialogoragnar.Play(-132500, -32750, -102500, 0)
#	ragnar.GoTo(-129250.0, -32750.0, -99250.0)
	ragnar.GoTo(-130500.0, -32750.0, -100000.0)
	ragnar.RouteEndedFunc=RagnarSigueAndando
	ragnar.LookAtEntity("Player1")
	cam.TimerFunc=CamaraSigueRagnar
	cam.SubscribeToList("Timer60")

def DetieneTargetRagnar(entity_name, camera_element, node):
	if node==1:
		global nodo_n
		nodo_n=0
		cam=Bladex.GetEntity("Camera")
		cam.TType=0
		cam.CameraClearPath(1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RagnarEmpiezaAndar, ())

def MiraRagnar():
	cam=Bladex.GetEntity("Camera")
	tpos=cam.TPos
	rgpos=ragnar.Position
	# Path target
	cam.AddCameraNode(1, 1.0, tpos[0], tpos[1], tpos[2])
	cam.AddCameraNode(1, 1.0, rgpos[0], rgpos[1]+3000.0, rgpos[2])
	cam.AddCameraNode(1, 1.0, -130000.0, -31750.0, -88000.0)
	cam.TType=1
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=DetieneTargetRagnar

def RieRagnar():
	rgpos=ragnar.Position
	risaragnar.Play(rgpos[0], rgpos[1], rgpos[2], 0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, MiraRagnar, ())

def DetieneTargetCuervos(entity_name, camera_element, node):
	if node==1:
		cam=Bladex.GetEntity("Camera")
		cam.TType=0
		cam.CameraClearPath(1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, RieRagnar, ())

def MiraCuervos():
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
	v=tpos[0]-opos[0], tpos[1]-opos[1], tpos[2]-opos[2]
	vnorm=B3DLib.Normalize(v)
	cam.ESource="Player1"
	cam.SType=2
	# Path target
	cam.AddCameraNode(1, 2.0, tpos[0]+vnorm[0]*2000, tpos[1]+vnorm[1]*2000, tpos[2]+vnorm[2]*2000)
	cam.AddCameraNode(1, 2.0, -127000.0, -43900.0, -106100.0)
	cam.AddCameraNode(1, 2.0, -127000.0, -46900.0, -106100.0)
	cam.TType=1
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=DetieneTargetCuervos
	graznidocuervo.Play(-135000.0, -42000.0, -102000.0, 0)
	char.Face(4.0*3.14159/3.0)

def SigueConCuervos(entity_name):
	global original_dist
	cam=Bladex.GetEntity("Camera")
	cam.RemoveFromList("Timer60")
	cam.TimerFunc=""
	cam.SetPersonView("Player1")
	original_dist=cam.Dist
	cam.Dist=1800.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, MiraCuervos, ())
	ragnar.Position=-127000.0, -31750.0, -92000.0
	ragnar.Angle=3.14159
	ragnar.SeeFunc=FuncionNula

def Camara2RagnarFinalTermina(x,y):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	ScriptSkip.SkipScriptEnd()
	Bladex.SetListenerPosition(1)
	Scorer.SetVisible(1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, RagnarAtaca, ())
	#RagnarAtaca()

def PlayPasitoRagnar1(a,b):
	_Pasito.Play(ragnar.Position[0], ragnar.Position[1],-ragnar.Position[2], 0)

def PlayPasitoRagnar2(a,b):
	_Pasito1.Play(ragnar.Position[0], ragnar.Position[1],-ragnar.Position[2], 0)


def Camara2RagnarFinal(x,y):
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("end_ragnarCamera02.cam",121,500)

	cam.AddCameraEvent(176-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(155-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(177-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(198-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(220-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(241-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(267-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(289-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(306-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(325-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(348-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(367-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(389-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(409-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(430-121,PlayPasitoRagnar2)
	cam.AddCameraEvent(453-121,PlayPasitoRagnar1)
	cam.AddCameraEvent(466-121,PlayPasitoRagnar2)

	cam.AddCameraEvent(-1,Camara2RagnarFinalTermina)



def Camara1RagnarCaminante(x,y):
	ragnar.Position = (-127795.461,-31432.037,-94747.914)
	ragnar.Angle=3.14159
	ragnar.Wuea = Reference.WUEA_ENDED
	ragnar.SetTmpAnmFlags(1,1,1,0,5,1)
	ragnar.LaunchAnimation("Rgn_end_ragnar_ragnar")
	ragnar.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, GameText.WriteText, ("M2T3",))       # aparicion text en pantalla

def EntraHabitacionFinal(sector_index, entity_name):
	if entity_name=="Player1":
		ScriptSkip.SkipScriptStart("ragnaranda")
		sectorfinragnar.OnEnter=""
		cam=Bladex.GetEntity("Camera")
		cam.SetMaxCamera("end_ragnarCamera01.cam",0,120)
		#cam.AddCameraEvent(111,Camara1RagnarCaminante)
		Bladex.AddScheduledFunc(Bladex.GetTime()+111.0/20.0, Camara1RagnarCaminante,(0,0))
		cam.AddCameraEvent(-1,Camara2RagnarFinal)
		Scorer.SetVisible(0)

		char=Bladex.GetEntity("Player1")
		char.Angle=3.14159
		char.Position = (-142408.234,-31634.457,-98412.711)
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)
		char.LaunchAnmType("end_ragnar")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, char.SetOnFloor,())

		puertaragnar.OnEndCloseFunc=PolvoPuertaRagnar
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, puertaragnar.CloseDoor, ())
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, MusicTool.LaunchMusicEvent, ("locuraragnar",))
		sec=Bladex.GetSector(sector_index)
		sec.OnEnter=""




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para traps.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def StopBlade(blade):
	blade.TimerFunc=None
	blade.RemoveFromList("Timer60")

def RegetBlade1():
	blade = Bladex.GetEntity("Blade1")
	Sonido_Cuchilla1_Recogida.Play(blade.Position[0],blade.Position[1],blade.Position[2],0);

def RegetBlade2():
	blade = Bladex.GetEntity("Blade2")
	Sonido_Cuchilla2_Recogida.Play(blade.Position[0],blade.Position[1],blade.Position[2],0);

def Blade1RTimerFunc(blade_name,time):
	global b1_time
	itime=time-b1_time
	blade=Bladex.GetEntity(blade_name)
	if(itime<3.0):
		blade.SetPosition(-138250,-23598,-97000-2666.6*itime,0)
	blade.Rotate(0.0,1.0,0.0,-0.1,1)
	if(itime>3.0):
		StopBlade(blade)

def Blade2RTimerFunc(blade_name,time):
	global b2_time
	global blades_ready
	itime=time-b2_time
	blade=Bladex.GetEntity(blade_name)
	if(itime<3.0):
		blade.SetPosition(-145250,-23124,-97000-2666.6*itime,0)
	blade.Rotate(0.0,1.0,0.0,0.1,1)
	if(itime>3.0):
		StopBlade(blade)
		Sonido_TrampaCuchilla_Reactivada.Play(-145250,-23124,-98500,0)
		#blades_ready=1


def RBlade1():
	global b1_time
	b1_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade1")
	#Sonido_Cuchilla1_Activada.Play(blade.Position[0],blade.Position[1],blade.Position[2],0)
	blade.Solid=0
	blade.TimerFunc=Blade1RTimerFunc
	blade.SubscribeToList("Timer60")
	#Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,StopBlade,("Blade1"))


def RBlade2():
	global b2_time
	b2_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade2")
	#Sonido_Cuchilla2_Activada.Play(blade.Position[0],blade.Position[1],blade.Position[2],0)
	blade.Solid=0
	blade.TimerFunc=Blade2RTimerFunc
	blade.SubscribeToList("Timer60")
	#Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,StopBlade,("Blade2"))
def ApagaLuzChispa(luz):

	luz.SubscribeToList("Pin")


def LaunchBlade1():
	global b1_time
	Sonido_Cuchilla1_Activada.Play(-138250,-23598,-105000,0)
	b1_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade1")
	blade.Position=-138250,-23598,-105000
	luzchispa1=Bladex.CreateEntity("LuzChispa1", "Entity Spot", blade.Position[0]-200, blade.Position[1], blade.Position[2]+1500)
	luzchispa1.Color=255, 140, 0
	luzchispa1.Intensity=1.5
	luzchispa1.Visible=0
	luzchispa1.CastShadows=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, ApagaLuzChispa,(luzchispa1,))
	chispas1=Bladex.CreateEntity("Chispas1", "Entity Particle System D1", blade.Position[0], blade.Position[1], blade.Position[2]+1500)
	chispas1.ParticleType="Spark"
	chispas1.YGravity=0.0
	chispas1.Friction=0.0
	chispas1.PPS=2048
	chispas1.Velocity=-4000.0, 0.0, -4000.0
	chispas1.RandomVelocity=30.0
	chispas1.Time2Live=8
	chispas1.DeathTime=Bladex.GetTime()+0.6
	blade.Solid=0
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	blade.TimerFunc=Blade1TimerFunc
	blade.SubscribeToList("Timer60")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,RegetBlade1,())


def Blade1TimerFunc(blade_name,time):
	global b1_time
	itime=time-b1_time
	blade=Bladex.GetEntity(blade_name)
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	if(itime<1.0):
		blade.SetPosition(-138250+(-6000.0+6000.0*itime)*itime,-23598,-105000+(16000.0-8000*itime)*itime,0)
		if (itime<0.6):
			chispas1=Bladex.GetEntity("Chispas1")
			chispas1.Position=blade.Position[0], blade.Position[1], blade.Position[2]+1500
			luzchispa1=Bladex.GetEntity("LuzChispa1")
			luzchispa1.Position=blade.Position[0]-200, blade.Position[1], blade.Position[2]+1500
	blade.Rotate(0.0,1.0,0.0,0.6-0.3*itime,1)
	if(itime>2.0):
		StopBlade(blade)
		#RBlades()
		RBlade1()

def LaunchBlade2():
	global b2_time
	Sonido_Cuchilla2_Activada.Play(-145250,-23124,-105000,0)
	b2_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade2")
	blade.Position=-145250,-23124,-105000
	luzchispa2=Bladex.CreateEntity("LuzChispa2", "Entity Spot", blade.Position[0]+200, blade.Position[1], blade.Position[2]+1500)
	luzchispa2.Color=255, 140, 0
	luzchispa2.Intensity=1.5
	luzchispa2.Visible=0
	luzchispa2.CastShadows=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, ApagaLuzChispa,(luzchispa2,))
	chispas2=Bladex.CreateEntity("Chispas2", "Entity Particle System D1", blade.Position[0], blade.Position[1], blade.Position[2]+1500)
	chispas2.ParticleType="Spark"
	chispas2.YGravity=0.0
	chispas2.Friction=0.0
	chispas2.PPS=2048
	chispas2.Velocity=4000.0, 0.0, -4000.0
	chispas2.RandomVelocity=30.0
	chispas2.Time2Live=8
	chispas2.DeathTime=Bladex.GetTime()+0.6
	blade.Solid=0
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	blade.TimerFunc=Blade2TimerFunc
	blade.SubscribeToList("Timer60")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,RegetBlade1,())


def Blade2TimerFunc(blade_name,time):
	global b2_time
	itime=time-b2_time
	blade=Bladex.GetEntity(blade_name)
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	if(itime<1.0):
		blade.SetPosition(-145250+(6000.0-6000.0*itime)*itime,-23124,-105000+(16000.0-8000*itime)*itime,0)
		if (itime<0.6):
			chispas2=Bladex.GetEntity("Chispas2")
			chispas2.Position=blade.Position[0], blade.Position[1], blade.Position[2]+1500
			luzchispa2=Bladex.GetEntity("LuzChispa2")
			luzchispa2.Position=blade.Position[0]+200, blade.Position[1], blade.Position[2]+1500
	blade.Rotate(0.0,1.0,0.0,-0.6+0.3*itime,1)
	if(itime>2.0):
		StopBlade(blade)
		RBlade2()


def LaunchBlades():
	global blades_ready
	LaunchBlade2()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,LaunchBlade1,())
	#slab.SlideTo(0,-200,0)
	blades_ready=0

def RBlades():
	global blades_ready
	blades_ready=1
	#if(blades_ready == 0):
	#	RBlade2()
	#	RBlade1()
		#slab.SlideTo(100,100,0)


def ActivateBlades(SectorIndex,EntyName):
	if(blades_ready):
		Sonido_TrampaCuchilla_Activada.Play(-141750,-23000,-99000,0)
		#lever.state == lever.LEVER_ON
		#lever.LeverOff()
		LaunchBlades()





#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Musica.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def ApagaMusicaAlEntrar(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))

def EnciendeSuspenseRapido(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("suspenserapido"))

def EnciendeMusicaCapilla(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicacapilla"))

def DesactivaEnciendeMusicaCapilla(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.RemoveTriggerSectorFunc("MusicaCapilla1", "OnEnter")
		Bladex.RemoveTriggerSectorFunc("MusicaCapilla2", "OnEnter")

def EnciendeSuspenseLento(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("suspenselento"))

def EnciendeMusicaZonaCaos(trsector_name, entity_name):
	if entity_name=="Player1":
		if Bladex.GetEntity("ChaosK1").Life>=800:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicazonacaos"))
		else:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("suspenselento"))

def EnciendeMusicaTorre(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicatorre"))

def EnciendeRagnarCuchillas(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("ragnarcuchillas"))
		Bladex.RemoveTriggerSectorFunc("RagnarCuchillas", "OnEnter")

def EnciendeTrampa(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicatrampa"))
		Bladex.RemoveTriggerSectorFunc(trsector_name, "OnEnter")

def EnciendeMusicaPendulos(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicapendulos"))
