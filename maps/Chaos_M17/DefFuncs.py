##///
##||| CHAOS_M17/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Killing the 2 metal golems before the door finishes closing no longer softlocks the player
##||| * Shadow pass
##||| * Starting the great demon scene no longer has a sharp and loud sound
##||| * Great demon scene now skippable
##\\\ 

#import def_class
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
import Auras
import CharStats
import ScriptSkip
import MusicTool

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puente.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##########################################################
#                      OBJETOS DE PEGA                  �#
##########################################################
def obpega():
	o=Bladex.CreateEntity("Estatua1","Golem_metal",370335.687481,30426.025422,-42695.944976)
	o.Static=1
	o.Scale=1.000000
	o.Orientation=0.043168,0.043168,-0.705788,0.705788

	global rayotractor2
	rayotractor2=Bladex.CreateSound("../../Sounds/rayo-tractor1.wav", "RayoTractor2")
	rayotractor2.Volume=1.0
	rayotractor2.MinDistance=150000
	rayotractor2.MaxDistance=500000


	o=Bladex.CreateEntity("Estatua2","Golem_metal",370262.041632,30420.641208,-37602.686308)
	o.Static=1
	o.Scale=1.000000
	o.Orientation=0.706138,0.706138,0.037007,-0.037007

	global fuego
	fuego=Bladex.CreateSound("../../Sounds/fuego.wav", "Fuego")
	fuego.Volume=1.0
	fuego.MinDistance=150000
	fuego.MaxDistance=500000


	o=Bladex.CreateEntity("Bloque1","Adoquinpulsador",370339.309685,30428.340923,-37621.245185)
	o.Static=1
	o.Scale=3.140205
	o.Orientation=0.538868,0.453114,-0.455427,-0.544881
	o.Alpha=0
	o.CastShadows=0
	Reference.EntitiesSelectionData["Bloque1"]=[0,0,""]


	o=Bladex.CreateEntity("Bloque2","Adoquinpulsador",370160.372891,30330.841378,-42805.579611)
	o.Static=1
	o.Scale=3.235356
	o.Orientation=0.483647,0.510908,-0.507898,-0.497089
	o.Alpha=0
	o.CastShadows=0
	Reference.EntitiesSelectionData["Bloque2"]=[0,0,""]

def Abrerastsec():

	desplazamientos=(3000, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	cerraduraz.key=""
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmemptyloquesea"))



	Objects.NDisplaceObject(rastsecdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CreaGolemsPuente():
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,CreaGolemsPuenteDeVerdad,())

def CreaGolemsPuenteDeVerdad():
	Bladex.GetEntity("Estatua1").RemoveFromWorld()
	Bladex.GetEntity("Estatua2").RemoveFromWorld()
	Bladex.GetEntity("Bloque1").RemoveFromWorld()
	Bladex.GetEntity("Bloque2").RemoveFromWorld()
	darfuncs.UnhideBadGuy("Golem1")
	darfuncs.UnhideBadGuy("Golem2")
	CierraPuertagolem()


	if not cerraduraorc.key:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate4"))


	if StartSceneOrcos2.OnEnter:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("1Combate1"))
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3b"))

	Ontake.DelOnTakeEvent("Llavez")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para transp.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DeathAppears(PersonName = "Player1"):
	time=Bladex.GetTime()
	aura=Auras.MakeAura(PersonName,0.4,   ( 50, 1.0 , 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))
	aura.Data.AddEvent(time+0.2,          (150, 0.5 , 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))
	aura.Data.AddEvent(time+0.4,          (200, 0.01, 0.0, 0, 0, 0), (), (), (2,  0.9, 0.9, 0.0, 0.9, 0.0  ,  0.9, 0.9, 0.0, 0.9, 0.8))

	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=16
	wps.RandomVelocity=2.0
	wps.Velocity=0,0,0
	wps.NormalVelocity=20
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+0.25
	wps.PPS=1024
	per = Bladex.GetEntity(PersonName)
	darfuncs.UnhideBadGuy(per.Name)
	per.Alpha = 1.0
	per.SetTmpAnmFlags(1,1,1,0,5,1,0)
	per.Wuea=Reference.WUEA_ENDED
	per.LaunchAnmType("rlx")
	per.SetOnFloor()
	per.SetActiveEnemy("Player1")
	Actions.TurnToFaceEntityNow(per.Name,"Player1")
	_AppearsCagazo.Play(per.Position[0], per.Position[1], per.Position[2], 0)

def DeathDisappears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=16
	wps.RandomVelocity=2.0
	wps.Velocity=0,0,0
	wps.NormalVelocity=2
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+0.25
	wps.PPS=1024
	per = Bladex.GetEntity(PersonName)
	per.Data.InteruptActions(per.Name)
	darfuncs.HideBadGuy(per.Name)

	_AppearsCagazo.Play(per.Position[0], per.Position[1], per.Position[2], 0)

	per.Data.Exist  = 0

def Cierrabucle():
        puertaizq.CloseDoor()
        puertader.CloseDoor()
        CreaEnemigosBucle()

def OpenBucProc():
        puertaizq.OpenDoor()
        puertader.OpenDoor()

def Abrete():
	bucleinfi.OpenDoor()
	bucleinfd.OpenDoor()
	buclesupi.OpenDoor()
	buclesupd.OpenDoor()

	buclesupd.OnEndCloseFunc = ""



def Cierrate():
	buclesupi.CloseDoor()
	buclesupd.CloseDoor()
	bucleinfi.CloseDoor()
	bucleinfd.CloseDoor()

def SaltaPrimero(sectorindex,entityname):
  if entityname=='Player1':
    Cierrate()
    buclesupd.OnEndCloseFunc = Salta1

def Salta1():
    P2.OnEnter=""
    P1.OnEnter=""
    P2.OnLeave=""
    P1.OnLeave=SeteaLosSaltos
    char=Bladex.GetEntity("Player1")
    char.Position =(421110, 95177,  23395)
    Abrete()

    #darfuncs.BackPlayer()
    cam = Bladex.GetEntity("Camera")
    cam.Position = (421643, 90442, 21691)

    buclesupd.OnEndOpenFunc = ""
    puertader.OnEndOpenFunc = ""
    Cierrabucle()

# jump to the sector P2
def SaltaSegundo(sectorindex,entityname):
  if entityname=='Player1':
    Cierrate()
    buclesupd.OnEndCloseFunc = Salta2


def Salta2():
    P2.OnEnter=""
    P1.OnEnter=""
    P2.OnLeave=SeteaLosSaltos
    P1.OnLeave=""
    char=Bladex.GetEntity("Player1")
    char.Position =(421804, 65177, -12212)
    Abrete()
    #darfuncs.BackPlayer()
    cam = Bladex.GetEntity("Camera")
    cam.Position = (421663, 60618,-10103)

    buclesupd.OnEndOpenFunc = OpenBucProc
    puertader.OnEndOpenFunc = Cierrabucle
    Cierrabucle()


#reactiva los saltos de lugar
def SeteaLosSaltos(sectorindex,entityname):
  if entityname=='Player1':
     P2.OnEnter=SaltaPrimero
     P1.OnEnter=SaltaSegundo

##########################################
#  El truco de la camara que se mueve   ##
##########################################

# retorna la camara a su posicion original
def CamBack(sectorindex,entityname):
  if entityname=='Player1':
    darfuncs.BackPlayer()

# sector de mover la camara  (421595, 95177, 30789)
# sector de volver la camara (419727, 95177, 35034)
# Posicion de la camara      (421643, 90442, 21691)

# Cambia el punto de vista
def CamSet1(sectorindex,entityname):
  if entityname=='Player1':
    darfuncs.ChangePointOfView(421643, 90442, 21691,1)

def MurioElEsk(entity_name):

  global IsEnBucle
  global EnCounter

  IsEnBucle[int(entity_name[0])] = 1
  per = Bladex.GetEntity(entity_name)
  per.Data.StdImDead(entity_name)
  EnCounter = EnCounter-1

def EspectroTimer(e_name, time):
	global ESPECTRO_SEC

	e=Bladex.GetEntity(e_name)
	e.Alpha = (1.0-abs(e.Data[1]))*0.5
	e.Data[1] = e.Data[1] + e.Data[2]

	e.Data[0] = e.Data[0]+1
	e.Rotate(0,0,1,-0.04)
	e.Move(0,-15,0)
	if e.Data[0] > 15*ESPECTRO_SEC:
		e.RemoveFromList("Timer30")
		e.SubscribeToList("Pin")

def SaleEspectro(x,y,z,kind ="Espectro"):
	global ESPECTRO_SEC

	e = Bladex.CreateEntity("Espectro",kind,x,y,z)
	e.Orientation =(0.707123160362, 0.707090377808, -0.000196549459361, 6.55114272377e-005)
	e.Data = [-15*ESPECTRO_SEC,-1,1.0/(15*ESPECTRO_SEC)]
	e.SubscribeToList("Timer30")
	e.TimerFunc = EspectroTimer
	e.CastShadows = 0
	e.RasterMode="AdditiveAlpha"
	e.RasterMode="Read"
	e.Alpha = 0
	e.SelfIlum = 0.15
	return e

def ChapuAnima(pers):
	pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
	pers.Wuea = Reference.WUEA_ENDED
	pers.LaunchAnimation("Vmp_dth0")

def MurioElVamp(entity_name):
	global EnCounter
	global IsEnBucle
	global VampiroIs
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio4"))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmsorpresa8"))
	pers = Bladex.GetEntity(entity_name)
	#pers.Data.ImDeadFuncPlus(entity_name)

	time = Bladex.GetTime()

	SpiritualDeath(entity_name)

	# Drop the weapons if possible

	object = Bladex.GetEntity(pers.InvLeft)
	if pers.InvLeft and object and not object.TestHit:
		Actions.RemoveFromInventory (pers, object,"DropLeftEvent")
		object.Impulse(0.0, 0.0, 0.0)

	object = Bladex.GetEntity(pers.InvRight)
	if pers.InvRight and object and not object.TestHit:
		Actions.RemoveFromInventory (pers, object,"DropRightEvent")
		object.Impulse(0.0, 0.0, 0.0)
	pers.AnmEndedFunc = ChauVampiro

def BorratelasVapiru(entity_name):
	dust.BorraPorLasDudas2(entity_name)

def FinCamaraVamp():
	Descubre("Player1")

def ChauVampiro(entity_name):
	global EnCounter
	global EnCounter
	global IsEnBucle
	global VampiroIs

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(41,))
	Bladex.GetEntity(entity_name).Freeze()

	print("The ilussion is over")
	PhantonFX.Delta = 0.0125
	PhantonFX.DisappearsChar(entity_name,BorratelasVapiru)

	char= Bladex.GetEntity("Player1")
	#sonidobucle.Position = char.Position
	#Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,sonidobucle.PlaySound,(1,))



	per = Bladex.GetEntity(entity_name)
	#per.Data.StdImDead(entity_name)
	EnCounter = EnCounter-1

	VampiroIs = 1

def SeVaElVampiroCagandoLeches(EntityName):
       PhantonFX.Delta = 0.05
       PhantonFX.DisappearsChar("Drakula")
       Drakula = Bladex.GetEntity("Drakula")
       Drakula.Freeze()


def SaleArena(sectorindex,entityname):
  if (entityname=='Player1') and (VampiroIs==0):
     Drakula = Bladex.GetEntity("Drakula")
     if Drakula.Data.Exist :
       Drakula.Blind       = 1
       Drakula.Deaf        = 1
       Drakula.Life        = CharStats.GetCharMaxLife(Drakula.Kind, Drakula.Level)
       Drakula.Wuea=Reference.WUEA_ENDED
       DeathDisappears(Drakula.Name)


def DesocultaVampiro():
  global VampiroIs
  global EnCounter

  if VampiroIs:
    EnCounter = EnCounter+1
    VampiroIs = 0

    Drakula = Bladex.GetEntity("Drakula")
    Drakula.Position    = 422565, 77177, 1272
    Drakula.Blind       = 0
    Drakula.Deaf        = 0
    Drakula.Angle       = 3.14159
    Drakula.Alpha       = 0.0
    Drakula.Data.Exist  = 1
    Actions.TurnToFaceEntity("Drakula", "Player1")
    DeathAppears(Drakula.Name)


def EntraArena(sectorindex,entityname):
  global VampiroIs

  if VampiroIs==0:
    if entityname=='Player1':
      Drakula = Bladex.GetEntity("Drakula")
      if not Drakula.Data.Exist :
         VampiroIs           = 1
         DesocultaVampiro()

def  CreaVampiro():
    global VampiroIs
    global EnCounter
    global Drakula

    hacha   = Bladex.CreateEntity(Bladex.GenerateEntityName(), "VampWeapon", 0, 0, 0,"Weapon")
    ItemTypes.ItemDefaultFuncs (hacha)
    escudo = Bladex.CreateEntity(Bladex.GenerateEntityName(), "VampShield", 0, 0, 0,"Weapon")
    ItemTypes.ItemDefaultFuncs (escudo)

    Drakula = Bladex.CreateEntity("Drakula", "Vamp", 422565, 77177, 1272,"Person")
    Drakula.Blind       = 0
    Drakula.Deaf        = 0
    Drakula.Angle       = 3.14159
    Drakula.Level       = 19
    Drakula.Alpha       = 0.0
    Actions.TakeObject(Drakula.Name, hacha.Name)
    Actions.TakeObject(Drakula.Name, escudo.Name)
    EnemyTypes.EnemyDefaultFuncs(Drakula)
    Actions.TurnToFaceEntity("Drakula", "Player1")
    Drakula.Data.ImDeadFuncPlus	= pers.ImDeadFunc
    Drakula.ImDeadFunc		= MurioElVamp
    Drakula.Data.Exist          = 0
    darfuncs.HideBadGuy("Drakula")
#
# Crea un enemigo del blucle
#------------------------------
def CreaEnemigoBucle(n):
     global IsEnBucle
     global CosoCounter
     global BucleList
     global EnCounter



     if IsEnBucle[n]:

        IsEnBucle[n] = 0


        hacha   = Bladex.CreateEntity(Bladex.GenerateEntityName(), "HookSword", 0, 0, 0,"Weapon")
        ItemTypes.ItemDefaultFuncs (hacha)
        escudo = Bladex.CreateEntity(Bladex.GenerateEntityName(), "Escudo7", 0, 0, 0,"Weapon")
        ItemTypes.ItemDefaultFuncs (escudo)

        nameofme = `n`+" est queletum"+`CosoCounter`

        if BucleList[n] <> None:
           BucleList[n].SubscribeToList("Pin")

        nameofme = `n`+" est queletum"+`CosoCounter+1`

        if   n == 0:
          esq = Bladex.CreateEntity(nameofme, "Skeleton", 431207.70821, 66820.2642879, -41403.1340647,"Person")
        elif n == 1:
          esq = Bladex.CreateEntity(nameofme, "Skeleton", 412499.932168, 66781.0120708, -41211.0260771,"Person")
        elif n == 2:
          esq = Bladex.CreateEntity(nameofme, "Skeleton", 421886.718415, 74411.6596186, -40478.0178493,"Person")
        elif n == 3:
          esq = Bladex.CreateEntity(nameofme, "Skeleton", 422140, 76661, -30852,"Person")
        EnCounter = EnCounter+1


        BucleList[n]    = esq


        esq.Blind       = 0
        esq.Deaf        = 0

        Actions.TakeObject(esq.Name, hacha.Name)
        Actions.TakeObject(esq.Name, escudo.Name)
        esq.Level=16
        esq.ActionAreaMin=pow(2,0)
        esq.ActionAreaMax=pow(2,1)

        EnemyTypes.EnemyDefaultFuncs(esq)
        if n == 3:
          esq.Angle       = 3.14159
        esq.ImDeadFunc  = MurioElEsk

        return esq

def CreaEnemigosBucle():
  global CosoCounter
  global VampiroIs

  CosoCounter = CosoCounter+1
  #CreaVampiro()
  VampiroIs = 0

  for n in range(0, 4):
    CreaEnemigoBucle(n)

def SpiritualDeath(PersonName="Player1"):
	time = Bladex.GetTime()
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=64
	wps.RandomVelocity=0
	wps.Velocity=0,0,0
	wps.NormalVelocity=3.0
	wps.YGravity=-500
	wps.FollowFactor = 0.5
	wps.DeathTime=time+6
	wps.PPS=100

	pers = Bladex.GetEntity(PersonName)

	#Bladex.AddScheduledFunc(time+1.0,SaleEspectro,(pers.Position[0],pers.Position[1]+1200,pers.Position[2]))
	#Bladex.AddScheduledFunc(time+3.8,SaleEspectro,(pers.Position[0],pers.Position[1]+1200,pers.Position[2]))
	#Bladex.AddScheduledFunc(time+6.0,SaleEspectro,(pers.Position[0],pers.Position[1]+1200,pers.Position[2]))
	ChapuAnima(pers)
	SpiritualDeathCamerona(pers)

def SpiritualDeathCamerona(pers):
	cam=Bladex.GetEntity("Camera")
	AbreCam.ResetNode()

	AbreCam.PTS.append(( 429000,76500+0000,  8318),pers.Position,0.01)
	AbreCam.PTS.append(( 429000,76500+2000, -8318),pers.Position,6)
	AbreCam.PTS.append(( 415000,76500-0000, -8318),pers.Position,6)
	AbreCam.PTS.append(( 415000,76500-6000,  8318),pers.Position,6)
	AbreCam.LastTime = 0.01

	AbreCam.ZoomNode(0)
	AbreCam.ZoomNode(1)
	AbreCam.ZoomNode(2)
	AbreCam.ZoomNode(3)
	AbreCam.CallBack = FinCamaraVamp

	AbreCam.AbreCam()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para bucle.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Bucle():
	bucle1a.OpenDoor()
	bucle2a.OpenDoor()

def Cucle():
	bucle1a.CloseDoor()
	bucle2a.CloseDoor()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para temblores.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def distanpun(p1,p2):
	return (p1[0]-p2[0])**2 +(p1[1]-p2[1])**2 +(p1[1]-p2[1])**2

def SurteEfecto():
	global SurtiActivados
	global NivelTemblor
	if SurtiActivados:
		best     = Surtidores[0]
		bestdist = distanpun(char.Position,best)
		for s in Surtidores:
			dist = distanpun(char.Position,s)
			if dist<bestdist:
				bestdist = dist
				best     = s
		dust.DropDust(best[0],best[1],best[2],0,-10000,0,NivelTemblor*48+16)

		Bladex.AddScheduledFunc(Bladex.GetTime()+7+whrandom.random()*5, SurteEfecto, ())

		valuez = whrandom.random()
		darfuncs.Temblores(2.0,(7 + valuez*5)*(NivelTemblor+2))
		if valuez < 0.5:
			TemblorMalditoTerror.Play(char.Position[0],char.Position[1],char.Position[2])
		else:
			TemblorMalditoTerror2.Play(char.Position[0],char.Position[1],char.Position[2])


def ActivaTemblorcito():
	global SurtiActivados
	global NivelTemblor
	SurtiActivados = 1
	NivelTemblor   = 2
	SurteEfecto()

def DesactivaTemblorcito():
	global SurtiActivados
	SurtiActivados = 0

def Atenua1():
	global NivelTemblor
	NivelTemblor = 1
	darfuncs.EnterSecEvent(313516.272282, 38859.2728649, -65793.5907764,Desatenua1)
	TemblorMalditoTerror.Volume=2.0/3
	TemblorMalditoTerror2.Volume=2.0/3

	global soundtornado
	soundtornado=Bladex.CreateSound("../../Sounds/concentraccion3.wav", "SoundTornado")
	soundtornado.Volume=1.0
	soundtornado.MinDistance=150000
	soundtornado.MaxDistance=500000




def Desatenua1():
	global NivelTemblor
	NivelTemblor = 2
	darfuncs.EnterSecEvent(320494.862267, 41862.1291972, -69516.7297415,Atenua1)
	TemblorMalditoTerror.Volume=1.0
	TemblorMalditoTerror2.Volume=1.0



def Atenua2():
	global NivelTemblor
	NivelTemblor = 0
	darfuncs.EnterSecEvent(383553.858899, 61356.6809752, -37456.9631938,Desatenua2)
	TemblorMalditoTerror.Volume=1.0/3
	TemblorMalditoTerror2.Volume=1.0/3

	global rayotractor
	rayotractor=Bladex.CreateSound("../../Sounds/rayo-tractor.wav", "RayoTractor")
	rayotractor.Volume=1.0
	rayotractor.MinDistance=150000
	rayotractor.MaxDistance=500000

def Desatenua2():
	global NivelTemblor
	NivelTemblor = 1
	darfuncs.EnterSecEvent(391950.203616, 57860.6967173, -23956.6747875,Atenua2)
	TemblorMalditoTerror.Volume=2.0/3
	TemblorMalditoTerror2.Volume=2.0/3

def Atenua3():
	darfuncs.EnterSecEvent(422278,74155,-42228,Desatenua3)
	DesactivaTemblorcito()


def Desatenua3():
	global NivelTemblor
	darfuncs.EnterSecEvent(421398,76854,-24945,Atenua3)
	ActivaTemblorcito()
	NivelTemblor = 1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para StartTime.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def AnimaElChango(Camera,frame):
  char = Bladex.GetEntity("Player1")
  #char.LaunchAnmType("Kgt_start_kaos")
  char.Angle = 0.110855605057
  char.SetOnFloor()

def FrameFunc(timer):
	global alpha
	Raster.SetFillColor(0,0,0)
	Raster.SetAlpha(alpha)

	time = timer - initial_time

	#if (time > 4.0):
		#Bladex.RemoveAfterFrameFunc("FadeIn")
	if (time < FADE + BLACK):
		Raster.SolidRectangle(0,0,639,479)
		if (time > BLACK ):
			alpha = 1.0 - ((time - BLACK) * 1.0/FADE)




def StopCameraInicio(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	char.Angle = 0.110855605057
	# Bob. Removed this as unnecessary & causes a camera cut
	#char.Position  =   325973.1,  -1291.66181046, 83.29
	char.SetOnFloor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atm11prelude"))
	ScriptSkip.SkipScriptEnd()

def MusicayTexto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("abismo-carga"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+7.0,GameText.WriteText,("M17T1",))

def GurakInicio():

	global initial_time
	global alpha
	global player2

	char = Bladex.GetEntity("Player1")
	char.Position  =   325973.1,  -1291.66181046, 83.29
	char.SetOnFloor()

	initial_time = Bladex.GetTime()
	alpha = 1.0;


	#Bladex.SetAfterFrameFunc("FadeIn",FrameFunc)
	char.Angle = 0.110855605057
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("kaos_Camera_start.cam",0,800)
	cam.AddCameraEvent(-1,StopCameraInicio)

	cam.AddCameraEvent(507,AnimaElChango)

	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,MusicayTexto,())
	ScriptSkip.SkipScriptStart("CaosInicio")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AbrePuertagolem():
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(39,))
	
	### BUG FIX: If golems are killed before the door finishes closing, will no longer softlock the player.
	puertagolem.OnEndCloseFunc=puertagolem.OpenDoor
	puertagolem.OpenDoor()
	if not cerraduraorc.key:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera18"))


def CierraPuertagolem():

	puertagolem.CloseDoor()

	global viejo1
	viejo1=Bladex.CreateSound("../../Sounds/respiraviejete1.wav", "Viejo1")
	viejo1.Volume=0.2
	viejo1.MinDistance=150000
	viejo1.MaxDistance=500000


def Abreorc():

	desplazamientos=(3060, 1000)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000)
	vel_finales=(2000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", sonidofinrastrillo)
	cerraduraorc.key=""
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera18"))

	Objects.NDisplaceObject(rastorcdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrarastdem():

	desplazamientos=(2500, 500)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 5000)
	vel_finales=(5000.0, 0.0)
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)


	Objects.NDisplaceObject(rastdemdin, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)





def AbreBarrotes():
	barrote1.OpenDoor()
	barrote2.OpenDoor()
	barrote1b.OpenDoor()
	barrote2b.OpenDoor()

def CierraBarrotes():
	barrote1b.CloseDoor()
	barrote2b.CloseDoor()
	barrote1.CloseDoor()
	barrote2.CloseDoor()

	## meter aqui la creacion del moulinex

def Abrevamp():
	vampi.OpenDoor()
	vampd.OpenDoor()

	global viejo2
	viejo2=Bladex.CreateSound("../../Sounds/respiraviejete2.wav", "Viejo2")
	viejo2.Volume=0.2
	viejo2.MinDistance=150000
	viejo2.MaxDistance=500000

	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,Bladex.ExeMusicEvent,(Bladex.GetMusicEvent("Atmosfera2"),))



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para transpdes.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Descubre1():
	Cam = Bladex.GetEntity("Camera")
	Cam.SetPersonView("Player1")
	Cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)


def Descubre0():
	#AuxFuncs.MoveCamFromTo(422362,72746,25179, 426736,78226,23577,  421759,80432,22937,  431532,82430,16320, 4.5)
	AuxFuncs.MoveCamFromTo(422611,77286,25661, 426736,78226,23577,  430131,83649,22747,  431532,82430,16320, 4.5)

def Descubre(Entname):
	escalon1a.OpenDoor()
	escalon2a.OpenDoor()
	escalon3a.OpenDoor()
	escalon4a.OpenDoor()
	escalon5a.OpenDoor()
	escalon1b.CloseDoor()
	escalon2b.CloseDoor()
	escalon3b.CloseDoor()
	escalon4b.CloseDoor()
	escalon5b.CloseDoor()

	#AuxFuncs.MoveCamFromTo(412614,82609,16909,      422362,72746,25179,   421759,80432,22937,   421759,80432,22937,    4.5,Descubre0)
	AuxFuncs.MoveCamFromTo(412614,82609,16909,      422611,77286,25661,   421759,80432,22937,   430131,83649,22747,    4.5,Descubre0)

	escalon5a.OnEndOpenFunc = Descubre1
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)

def Tapa():

	escalon1a.CloseDoor()
	escalon2a.CloseDoor()
	escalon3a.CloseDoor()
	escalon4a.CloseDoor()
	escalon5a.CloseDoor()
	escalon1b.OpenDoor()
	escalon2b.OpenDoor()
	escalon3b.OpenDoor()
	escalon4b.OpenDoor()
	escalon5b.OpenDoor()

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
	char.Position=326107.232079, -1322.9, -768.178269881

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=294574.591956, 21889.1552101, -35535.3269093

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=323331.280952, 42177.1, -69805.4326766


def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=340196.669349, 44177.1, -89744.3624525

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=402105.065297, 54677.1, -46477.8361451


def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=421569.693484, 65161.8, -27704.0843803

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=431972.261163, 82677.1, 15511.4727136

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=528000,88000,45000


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para orcos.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreaOrco(n, x, y, z):

	sword=Bladex.CreateEntity("HachaEsqOrkus"+`n`, "Espadafilo", 0, 0, 0,"Weapon")
	ItemTypes.ItemDefaultFuncs(sword)

	escudo=Bladex.CreateEntity("Escudely"+`n`, "Escudo4", 0, 0, 0,"Weapon")
	ItemTypes.ItemDefaultFuncs(escudo)


	esq=Bladex.CreateEntity("Orkus"+`n`, "Dark_Knight", x, y, z,"Person")
	esq.Angle=1.24504670501
	esq.Level=14
	Actions.TakeObject(esq.Name, sword.Name)
	Actions.TakeObject(esq.Name, escudo.Name)

	esq.ActionAreaMin=pow(2,0)
	esq.ActionAreaMax=pow(2,1)

	EnemyTypes.EnemyDefaultFuncs(esq)
	esq.Blind=1
	esq.Deaf=1


	return esq



## CUIDADIN CON STALIN
def CreaOrcoGordo(n, x, y, z,CreaLlave=1):
	global ORCO_GORDO_TYPE

	esq = Bladex.GetEntity("Orkus"+`n`)
	if esq:
		darfuncs.UnhideBadGuy(esq.Name)
		esq.Blind=1
		esq.Deaf=1
		esq.Position = x, y, z
		esq.Angle = 1.24504670501
		esq.Level = 19
		esq.Data.LaunchMyWatch(esq.Name)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, esq.SetOnFloor,())
		return esq

	sword=Bladex.CreateEntity("HachaEsqOrkus"+`n`, "Espadafilo", 0, 0, 0,"Weapon")
	ItemTypes.ItemDefaultFuncs(sword)
	escudo=Bladex.CreateEntity("Escudely"+`n`, "Escudo4", 0, 0, 0,"Weapon")
	ItemTypes.ItemDefaultFuncs(escudo)

	esq=Bladex.CreateEntity("Orkus"+`n`, ORCO_GORDO_TYPE, x, y, z,"Person",ORCO_GORDO_TYPE)
	esq.Level=14
	esq.Angle=1.24504670501
	Actions.TakeObject(esq.Name, sword.Name)
	Actions.TakeObject(esq.Name, escudo.Name)


	esq.Blind=1
	esq.Deaf=1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, esq.SetOnFloor,())
	if CreaLlave:
		Llav=Bladex.CreateEntity("Llaveorc","Llavecobox",316060.535312,39467.257789,-59066.990229,"Physic")
		Llav.Scale=1.361327
		Llav.Orientation=0.964696,-0.000078,-0.263359,-0.001938
		darfuncs.SetHint(Llav,"Guardian Key")
		Actions.TakeObject(esq.Name,Llav.Name)
		EnemyTypes.EnemyDefaultFuncs(esq)


	return esq

def Escapex():
	ork = Bladex.GetEntity(  "Orkus2" )
	ork.SetTmpAnmFlags(1,1,1,0,5,1)
	ork.LaunchAnimation( "Kgt_order" )
	ork.AnmEndedFunc = Atakax
	ork.SetOnFloor()
	_GritaOrco.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def Atakax(xxx=0,yyy=0,zzz=0):
	ork = Bladex.GetEntity(  "Orkus0" )
	ork.Blind = 0
	ork.Deaf  = 0
	ork = Bladex.GetEntity(  "Orkus1" )
	ork.Blind = 0
	ork.Deaf  = 0
	ork = Bladex.GetEntity(  "Orkus2" )
	ork.GoToJogging = 1
	ork.GoTo(318245.647126, 29177.1, -70343.1697702)

	#ork.RouteEndedFunc = Eliminax

def Eliminax(xxx=0,yyy=0,zzz=0):
	ork = Bladex.GetEntity(  "Orkus2" )
	darfuncs.HideBadGuy("Orkus2")
	Cam = Bladex.GetEntity("Camera")
	Cam.SetPersonView("Player1")
	Cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	CreaOtroXX()


def CafinProx(entity_name, camera_element, node):
	cam = Bladex.GetEntity("Camera")
	if node==1:
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		Escapex()
		#Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, Atakax,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, Reposiciona,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+5.5, Eliminax,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.5, BorraBloque,())
		cam.ETarget = "Orkus2"
		cam.TType = 2


def Reposiciona():
	char = Bladex.GetEntity("Player1")
	char.Position=284944.675275, 26026.526283, -48134.90281
	char.SetOnFloor()

def BorraBloque():

	Bladex.GetEntity("Chaosbloque").SubscribeToList("Pin")

def IniciaOrcos2Plus(entity_name, camera_element, node):
	if node==1:
		cam = Bladex.GetEntity("Camera")
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		darfuncs.ChangeCam(317040,26409,-56088,   320061.510878, 28177.1, -58719.1381545, 3,CafinProx)

# huida numero 1
def IniciaOrcos(sectorindex,entityname):
	if entityname=="Player1":
		StartSceneOrcos.OnEnter = ""
		print("Entro")
		darfuncs.ChangeCam(287138, 27636, -53774,   320061.510878, 28177.1, -58719.1381545, 1,IniciaOrcos2Plus)
		Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		Bladex.SetListenerPosition(1)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmemptyloquesea"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("Atmosfera4",))

def EliminaxFin(nombrex):
	ork = Bladex.GetEntity(  "Orkus2" )
	darfuncs.HideBadGuy("Orkus2")
	CreaOtroXX()


# ultima posicion orco
def CreaOtroXX():
	ork = CreaOrcoGordo(2,315453, 38835, 19119,1)
	ork.Angle =5.9
	ork.Blind = 0
	ork.Deaf = 0
	ork.Position = 	315453, 38835, 19119



# huida numero 3 segunda huida
def IniciaOrcos3(sectorindex,entityname):
#	if(entityname=="Player1"):
		#ork = Bladex.GetEntity(  "Orkus2" )
		#ork.RouteEndedFunc = EliminaxFin
		#ork.GoTo(282536.724324, 38835.2, 10035.2367238)
		#ork.GoTo(284526.826741, 42390.0232674, 10560.0954185)
		#ork.GoToJogging = 1
		StartSceneOrcos3.OnEnter = ""



def CorreX(nombrex):
	ork = Bladex.GetEntity(  "Orkus2" )
	darfuncs.HideBadGuy("Orkus2")
	CreaOtroX()

## posicion en la que espera antes de segundo generador esqueletos

def CreaOtroX():
	print "orkos 3"
	ork = CreaOrcoGordo(2,282659.527215, 42009.6906229, 439.971990304)
	ork.Position = 282659.527215, 42009.6906229, 439.971990304
	print "deaf!"
	print ork.Deaf




## posicion en la que espera al ppio
def CreaDeNuevox():
	print "orkos 2"
	ork = CreaOrcoGordo(2,304875,38835,-43254)
	ork.Position = 304875,38835,-43254
	print "deaf!"
	print ork.Deaf



# huida numero 2  goto a la primera posicion de huida
def IniciaOrcos2(sectorindex,entityname):
#	if(entityname=="Player1"):
		#ork = Bladex.GetEntity(  "Orkus2" )
		#ork.GoTo(310301.311678, 38835.2, -32625.1482474)
		#ork.GoTo(314901.4509, 38883.893354, -34821.6325922)
		#ork.RouteEndedFunc = CorreX
		#ork.GoToJogging = 1
		#ork.Angle=5.89398415163
		StartSceneOrcos2.OnEnter = ""

		if Bladex.GetEntity("Golem1").Life > 0:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("1Combate1"))
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3b"))




#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para keletum.py         **************************
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
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen, (pos, v1, v2, v3))

def AsingaPropiedades(ent):
	ent.Level = 3
	ent.ActionAreaMin=pow(2,0)
	ent.ActionAreaMax=pow(2,1)
	ent.SetActiveEnemy("Player1")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para golem.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def TheChapuzaSolution():
	pers=Bladex.CreateEntity("GolemVomito","Golem_lava",394936,28343,-41304,"Person")
	pers.Level=14
	EnemyTypes.EnemyDefaultFuncs(pers)
	pers.Position = char.Position
	pers.Angle=-3.141569/2
	pers.Deaf=1
	pers.Blind=1
	darfuncs.HideBadGuy("GolemVomito")
	"""
	Rres = ReadGSFile.ReadGhostSectorFile("golem.sf")

	for igs in Rres:
	   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

	Bladex.SetTriggerSectorFunc("Golem", "OnEnter", GolemVomitoso )
	"""

def MuerteGolemDeVomito(ent_name):
	Bladex.GetEntity("GolemVomito").Data.ImDeadFuncPlus (ent_name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(40,))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio1"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("atmemptyloquesea",))
	AbreBarrotes()



def TierraSaltaGolemMierda(Mortadelo,Filemon):
	dust.RemueveTierraGen(394936,63500,-41304,2000,2500)
	_OstiaGolem.Play(394936,63500,-41304,0)
	char=Bladex.GetEntity("Player1")
	Actions.FreeBothHands("Player1")

def SacaLasArmasDelCagazo(Bonie,Clyde):
	Actions.StdToggleWeapons("Player1")
	Actions.QuickTurnToFaceEntity("Player1","GolemVomito")

def GolemVomitoso():
		darfuncs.UnhideBadGuy("GolemVomito")
		pers = Bladex.GetEntity("GolemVomito")
		pers.Deaf=1
		pers.Blind=1
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, GolemVomitosoCae,())
		Bladex.DeactivateInput()
		CierraBarrotes()


def ChapuzaGolemMierda(epi,blas):
	pers                            = Bladex.GetEntity("GolemVomito")
	pers.Data.ImDeadFuncPlus        = pers.ImDeadFunc
	pers.ImDeadFunc                 = MuerteGolemDeVomito
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, char.SetActiveEnemy,(Bladex.GetEntity("GolemVomito"),))
	pers.SelfIlum = 1
	pers.Deaf=0
	pers.Blind=0
	pers.SetActiveEnemy("Player1")


def GolemVomitosoCae():
	darfuncs.LaunchMaxCamera("Glm_fall_kaosCamera01.cam",0,165)

	pers=Bladex.GetEntity("GolemVomito")
	pers.Angle=-3.141569
	pers.Wuea=Reference.WUEA_ENDED
	pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
	pers.LaunchAnimation("Glm_fall_kaos")
	pers.Position = 394936,28350,-41304
	cam = Bladex.GetEntity("Camera")
	cam.AddCameraEvent(35,TierraSaltaGolemMierda)
	cam.AddCameraEvent(75,SacaLasArmasDelCagazo)
	cam.AddCameraEvent(164,ChapuzaGolemMierda)
	darfuncs.EnciendeEnLlamas(pers,15,0.1)
	Bladex.GetEntity(pers.Name+"Luz").CastShadows = 1
	pers.SelfIlum    = 1
	pers.CastShadows = 0
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-4"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("Atmosfera20a",))
	#EnemyTypes.EnemyDefaultFuncs(pers)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para FirsArenaScene.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def MuerteDemoniote(ent_name):
	demoniote.Data.ImDeadFunc (ent_name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0,Bladex.TriggerEvent,(43,))
	Bladex.ExeMusicEvent(-1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0,MusicTool.LaunchMusicEvent,("coro2-2",))
	EndOfFirstArena()

def CreaDemonioGigantesco():
	demoniote.SetTmpAnmFlags(1,1,1,0,5,1,0)
	demoniote.Wuea = Reference.WUEA_ENDED
	demoniote.LaunchAnimation("Gdm_sombra")
	Bladex.KillMusic()    # Added, fixes sharp and loud sound artifact -LeadHead
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-13"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,MusicTool.LaunchMusicEvent,("combate1",))
	demoniote.Position = 582725,307446,183505


def StopCameraInicioLosHuevos(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Bladex.SetListenerPosition(1)
	# Bladex.ActivateInput()
	ScriptSkip.SkipScriptEnd()	# Now skippable	-LeadHead
	Scorer.SetVisible(1)
	demoniote=Bladex.GetEntity("DemonioGigante")
	demoniote.Blind=0
	demoniote.Deaf=0


def StartArenaAnim():

	# Camera setup
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Demonio_Camera01.cam",0,340)
	cam.AddCameraEvent(-1,StopCameraInicioLosHuevos)

	# Player setup
	char = Bladex.GetEntity("Player1")
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.Wuea      =    Reference.WUEA_ENDED
	char           =    Bladex.GetEntity("Player1")
	char.Position  =    586400.75, 302647.75, 183222.469
	char.Angle     =   -3.1415/2
	char.LaunchAnmType("demonio_kaos")
	char.Position  =    586400.75, 302647.75, 183222.469
	char.Angle     =   -3.1415/2
	char.SetOnFloor()
	CreaDemonioGigantesco()
	AuxFuncs.FadeFrom(1.0,0.0)


def CaminaHastaEnSerioRealFinale(Entity):
	darfuncs.UnhideBadGuy(demoniote.Name)
	demoniote.Blind=1
	demoniote.Deaf=1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, StartArenaAnim, ())


def CaminaHastaRealFinale(Entity):
	char.GoToJogging=1
	char.GoTo(586400.75, 302647.75, 183222.469)
	char.QuickFace(3.14159*3/2)
	char.RouteEndedFunc = CaminaHastaEnSerioRealFinale
	AuxFuncs.FadeTo(0.5,10.0)





def CaminaHastaFinale(Entity):
	char                =    Bladex.GetEntity("Player1")
	char.GoToJogging=1
	char.GoTo(584400.75, 302647.75, 183222.469)
	char.QuickFace(5.1)
	char.RouteEndedFunc = CaminaHastaRealFinale
	darfuncs.ChangePointOfView(581094, 300540, 183262,2.5)

def IniciaSecuenciaArena(sectorindex,entityname):
	if entityname=='Player1':
		# Bladex.DeactivateInput()
		ScriptSkip.SkipScriptStart("GdmInicio")		# Now skippable -LeadHead
		Scorer.SetVisible(0)
		char                           =    Bladex.GetEntity("Player1")
		char.GoToJogging               = 1
		char.GoTo(578059.338505, 302427.1, 179200.088892)
		char.QuickFace(3.14159*3/2)
		char.RouteEndedFunc            = CaminaHastaFinale
		StartArena1SceneSector.OnEnter = ""
		darfuncs.ChangePointOfView(577868,292278,183124,2.5)



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para final.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

#------------------------------------------------------------------------


# Enciende                Sector                          Apaga
##################################################################
#                            Escalera                            #
##################################################################
#  Lucero0           (679730, 308927, 172595)             Parita6
#  Lucero1           (666873, 318927, 161774)             Lucero0
#  Lucero2           (716841, 329517, 170206)             Lucero1
#                    (758021, 333677, 168051)             Lucero2

def Stair1Proc(sectorindex,entityname):
  if entityname=='Player1':
    OnOff.SetLightInens(24)				#	Changed
    # OnOff.SetLightRadius(0.125)		# 		-LeadHead

    Stair1.OnEnter = ""
    OnOff.TurnOnLight( "Lucero0")
    OnOff.TurnOffLight("Parita6")

def Stair2Proc(sectorindex,entityname):
  if entityname=='Player1':
    OnOff.SetLightInens(100)

    Stair2.OnEnter = ""
    OnOff.TurnOnLight( "Lucero1")
    OnOff.TurnOffLight("Lucero0")

def Stair3Proc(sectorindex,entityname):
  if entityname=='Player1':
    OnOff.SetLightInens( 250)
    OnOff.SetLightRadius(0.1)

    Stair3.OnEnter = ""
    OnOff.TurnOnLight( "Lucero2")
    OnOff.TurnOffLight("Lucero1")

def Stair4Proc(sectorindex,entityname):
  if entityname=='Player1':
    OnOff.SetLightInens(100)

    Stair4.OnEnter = ""
    OnOff.TurnOffLight("Lucero2")

##################################################################
#                   Al entrar a la habitacion                    #
##################################################################
# Lucero3/Lucero9    (808033, 335177, 158327)
# Lucero3/Lucero9    (803879, 335177, 181172)

def Room1Proc(sectorindex,entityname):
  if entityname=='Player1':

    Room1.OnEnter = ""
    Room2.OnEnter = ""
    OnOff.TurnOnLight("Lucero3")
    OnOff.TurnOnLight("Lucero4")
    OnOff.TurnOnLight("Lucero5")
    OnOff.TurnOnLight("Lucero6")
    OnOff.TurnOnLight("Lucero7")
    OnOff.TurnOnLight("Lucero8")
    OnOff.TurnOnLight("Lucero9")

##################################################################
#                La casa del viejo buscapleitos
##################################################################
# Lucero10/Lucero11  (870944, 337791, 170399)
# Lucero12/Lucero13  (909429, 342677, 170371)

def OldMan1Proc(sectorindex,entityname):
  if entityname=='Player1':

    OldMan1.OnEnter = ""
    OnOff.TurnOnLight("Lucero10")
    OnOff.TurnOnLight("Lucero11")

def Final():
  char=Bladex.GetEntity("Player1")
  char.Position=907978, 342528, 169847
  char.Angle=math.pi*1.5

def OldManStartProc(sectorindex,entityname):
  if entityname=='Player1':
    OldManStart.OnEnter = ""
    # activate scene here, ends with the introduction of the combined DarkLordDemon creature
    OnOff.TurnOnLight("Lucero12")
    OnOff.TurnOnLight("Lucero13")
    CameronDiaz0()

##################################################################
#                 La Zona fantasma final
##################################################################

def EntraEnciende(triggername,entityname):
  if entityname=='Player1':
  	if Bladex.GetEntity(triggername[1:]).Data < Bladex.GetTime():
	    OnOff.TurnOnLight(triggername[1:])
	    Bladex.AddScheduledFunc(Bladex.GetTime()+10.0+whrandom.random()*5.0,OnOff.TurnOffLight,(triggername[1:],))
	    #print("Enciende "+triggername[1:])

def SaleApaga(triggername,entityname):
  if entityname=='Player1':
    OnOff.TurnOffLight(triggername[1:])
    Bladex.GetEntity(triggername[1:]).Data = Bladex.GetTime()+15

    #print("Apaga "+triggername[1:])

def Sacarracatelas():

   # ajusta la velocidad
   OnOff.LightSpeed=0.05

   # apaga todo
   OnOff.TurnOffLight("Lucero3")
   OnOff.TurnOffLight("Lucero4")
   OnOff.TurnOffLight("Lucero5")
   OnOff.TurnOffLight("Lucero6")
   OnOff.TurnOffLight("Lucero7")
   OnOff.TurnOffLight("Lucero8")
   OnOff.TurnOffLight("Lucero9")
   OnOff.TurnOffLight("Lucero10")
   OnOff.TurnOffLight("Lucero11")
   OnOff.TurnOffLight("Lucero12")
   OnOff.TurnOffLight("Lucero13")

   Bladex.SetTriggerSectorFunc("GLucero3", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero3", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero4", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero4", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero5", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero5", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero6", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero6", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero7", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero7", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero8", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero8", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero9", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero9", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero10", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero10", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero11", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero11", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero12", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero12", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero13", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero13", "OnLeave", SaleApaga     )

   Bladex.SetTriggerSectorFunc("GLucero14", "OnEnter", EntraEnciende )
   Bladex.SetTriggerSectorFunc("GLucero14", "OnLeave", SaleApaga     )


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def fastGoTo(entName,x,y,z):
	p =Bladex.GetEntity(entName)
	p.GoToJogging = 1
	p.GoTo(x,y,z)

## primer turno

def PrimerTurnoVuelta():
	Inicio0.UnhideBadGuys(3)
	#darfuncs.EnterSecEvent(319786.300877, 38928.8079704, -31379.3064295,PrimerTurnoVuelta)
	fastGoTo("8Skeleton",314859.247474, 38927.1427249, -33849.6861824)

def PrimerTurno():
	Inicio0.UnhideBadGuys(3)
	pers=Bladex.GetEntity("3Skeleton")
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0,pers.GoTo,(305865.980512, 38925.463709, -46606.7968188))

def SegundoTurno():

	#darfuncs.UnhideBadGuy("4Skeleton")
	darfuncs.UnhideBadGuy("5Skeleton")
	#pers = Bladex.GetEntity("5Skeleton")
	#darfuncs.EnciendeEnLlamas(pers,1,0.1)
	darfuncs.UnhideBadGuy("6Skeleton")
	pers=Bladex.GetEntity("6Skeleton")
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,pers.GoTo,(313317.202062, 38705.8872535, 6846.84143723))




def Skelpas():
	#pers = Bladex.GetEntity("14Skeleton")
	#darfuncs.EnciendeEnLlamas(pers,1,0.1)
	pers = Bladex.GetEntity("15Skeleton")
	darfuncs.EnciendeEnLlamas(pers,1,0.1)

def TercerTurno():
	darfuncs.UnhideBadGuy("Minot2")
	#darfuncs.UnhideBadGuy("Minot3")
	#fastGoTo("Minot2",283239.19104, 41818.0044784, -1798.9483616)
	fastGoTo("Minot2",280426.303841, 41723.6234402, -1962.29446078)


def CuartoTurno():

	darfuncs.UnhideBadGuy("7Skeleton")
	darfuncs.UnhideBadGuy("Minot7")
	pers=Bladex.GetEntity("7Skeleton")
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,pers.GoTo,(300199.393272, 43865.4130551, 31600.9272239))


def MueveMinot7():

	pers=Bladex.GetEntity("Minot7")
	Bladex.AddScheduledFunc(Bladex.GetTime()+8.0,pers.GoTo,(323860.190733, 38772.6662158, 18970.7008867))


def ApareceCaballero():

	darfuncs.UnhideBadGuy("12Kngt")



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevator.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def FinTrayectoElevador():
  global EndOfTravel
  elevador.OnEndOpenFunc = ""
  OnOff.TurnOffLight("Lamp6")
  EndOfTravel = 1
  CreateChaosSwitchOne()



def TicElevadorrr(e_name, time):
   char = Bladex.GetEntity('Player1')
   if(char.Position[1] >= 250000):
      elevador.sld_area().RemoveFromList("Elevador")
      elevador.sld_area().TimerFunc=""
      OnOff.TurnOffLight("Lamp5")
      OnOff.TurnOnLight( "Lamp7")

def TicElevadorr(e_name, time):
   char = Bladex.GetEntity('Player1')
   if(char.Position[1] >= 200000):
      elevador.sld_area().TimerFunc=TicElevadorrr
      OnOff.TurnOffLight("Lamp4")
      OnOff.TurnOnLight( "Lamp6")

def TicElevador(e_name, time):
   char = Bladex.GetEntity('Player1')
   if(char.Position[1] >= 160000):
     elevador.sld_area().TimerFunc=TicElevadorr
     OnOff.TurnOffLight("Lamp3")
     OnOff.TurnOnLight( "Lamp5")

def TicElevado(e_name, time):
   char = Bladex.GetEntity('Player1')
   if(char.Position[1] >= 130000):
     elevador.sld_area().TimerFunc=TicElevador
     OnOff.TurnOffLight("Lamp1")
     OnOff.TurnOffLight("Lamp2")

def AbreteSesamus(entity_name):
  global EndOfTravel
  global nChaos
  Bladex.ExeMusicEvent(-1)

  per = Bladex.GetEntity(entity_name)
  Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.TriggerEvent,(42,))
  Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, ParticulateDeath,(entity_name,))

  nChaos = nChaos - 1

  if EndOfTravel:
    if nChaos == 0:
      #Pasa()
      Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro6"))
      Bladex.AddScheduledFunc(Bladex.GetTime()+7.5, Pasa, ())

def AppearsChaos(e_name, time):
   global ChaosCounter

   ChaosCounter = ChaosCounter+1
   esq          =  Bladex.GetEntity(e_name)
   Der = Bladex.GetEntity(esq.InvRight)
   Izq = Bladex.GetEntity(esq.InvLeft)

   esq.Alpha    = ChaosCounter*0.025
   Der.Alpha    = esq.Alpha
   Izq.Alpha    = esq.Alpha



   if esq.Alpha >= 1.0 :
     esq.TimerFunc  = ""
     esq.RemoveFromList("ChaosTimer")
     esq.Alpha    = 1.0

def ActivaAsensorEnSerio():
      Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-5"))
      Bladex.AddScheduledFunc(Bladex.GetTime()+23.5,MusicTool.LaunchMusicEvent,("atmosfera8",))
      elevador.OpenDoor()
      elevador.sld_area().SubscribeToList("Elevador")
      elevador.sld_area().TimerFunc=TicElevado

# Este se llama cuando se activa el asensor
#------------------------------------------------
def ActivaAsensor(sectorindex,entityname):
   if entityname=='Player1':
      OnOff.TurnOffLight("Lamp0")
      OnOff.TurnOnLight("Lamp4")

      AsenderOne.OnEnter     = ""
      elevador.OnEndOpenFunc = FinTrayectoElevador
      Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, ActivaAsensorEnSerio, ())

def CuandoSeAbreLaPlataforma():
  OnOff.LightSetRadius           = 0.1
  OnOff.TurnOnLight("Parita2")
  plataforma.OnEndOpenFunc = ""


def CuandoSeCierreLaPlataforma():

  OnOff.LightSpeed               = 0.01
  OnOff.LightSetInens            = 50.0
  OnOff.LightSetRadius           = 0.25				# Changed
  OnOff.TurnOnLight("Parita0")
  OnOff.TurnOnLight("Parita1")
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio1"))
  Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("Atmosfera4",))
  plataforma.OnEndCloseFunc = ""

def NoPasa(sectorindex,entityname):

  if entityname=='Player1':
        OnOff.LightSpeed               = 0.05
        OnOff.TurnOffLight("Lamp7")
	plataforma.OpenDoor()
	plataforma.OnEndOpenFunc = CuandoSeAbreLaPlataforma

#
#  Pasa sera llamada cuando baje la plataforma y se mate al caballero del caos
#############################################################################################
def Pasa():
	#Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro5"))
	plataforma.CloseDoor()
	plataforma.OnEndCloseFunc = CuandoSeCierreLaPlataforma
	piedraenorme=Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav", "Piedraenorme")
	mecanismo1=Sounds.CreateEntitySound("../../Sounds/mechanism8.wav", "Mecanismo1")


###############################################################################################
"""
                                  Segunda Parte
                                Despues que Pasa el puente....

"""
###############################################################################################


# Para depuracion: salta a la segunda parte
def Parte2():

  OnOff.LightSpeed               = 0.05
  OnOff.LightSetInens            = 50.0
  OnOff.LightSetRadius           = 0.25

  char.Position = (528804, 298177, 138742)
  OnOff.TurnOnLight("Parita2")
  OnOff.TurnOnLight("Parita1")
  OnOff.TurnOnLight("Parita0")


# parita3  (529063.778395, 299927.1, 179809.647826)

        # La primera arena #

def LightArena1(sectorindex,entityname):

  if entityname=='Player1':
    OnOff.LightSpeed               = 0.05
    OnOff.LightSetInens            = 200.0
    OnOff.LightSetRadius           = 0.3

    OnOff.TurnOffLight("Parita0")
    OnOff.TurnOffLight("Parita1")
    OnOff.TurnOnLight( "Parita3")
    FirstArenaActivationSector.OnEnter = ""

def Enciendelox():
  OnOff.TurnOnLight( "Parita6") # enciende la luz detras de la puerta
  puertafinb.OnEndOpenFunc = ""

def Abrefin():

	puertafina.OpenDoor()
	puertafinb.OpenDoor()
	puertafinb.OnEndOpenFunc = Enciendelox
	platfin.OnEndCloseFunc   = ""
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atm12mp3"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,MusicTool.LaunchMusicEvent,("Atm1MP3",))

def TerminaLaCosa():
   OnOff.TurnOffLight( "Parita4")
   OnOff.TurnOffLight( "Parita5")
   platfin.OnEndOpenFunc =""


def CasiTerminaLaCosa(sectorindex,entityname):
  if entityname=='Player1':
	platfin.OpenDoor()
	platfin.OnEndOpenFunc =TerminaLaCosa
        EndPortalSector.OnEnter = ""

def IniciaSecuenciaDeApertura(sectorindex,entityname):
  if entityname=='Player1':

    StartPortalSector.OnEnter = ""
    platfin.CloseDoor()
    platfin.OnEndCloseFunc = Abrefin


#
#  Activa la secuencia de la primera arena
#---------------------------------------------
def EndOfFirstArena():

   OnOff.LightSetInens            = 50.0
   OnOff.LightSetRadius           = 0.2

   # apagar las dos luces de la arena
   OnOff.TurnOffLight( "Parita3")
   OnOff.TurnOffLight( "Parita2")

   # encender las dos luces de la puerta
   OnOff.TurnOnLight( "Parita4")
   OnOff.TurnOnLight( "Parita5")
   StartPortalSector.OnEnter = IniciaSecuenciaDeApertura

#####################
#     Aparicion     #
#####################

def MueveCamaraChk():
	global prevtpos
	Bladex.KillMusic()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,MusicTool.LaunchMusicEvent,("Combate3b",))

	Actions.TurnToFaceEntityNow("ChaosK1","Player1")
	chaosk1.Data.Appear()
	if (char.InvRight==""):
		Actions.StdToggleWeapons("Player1")

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0,Actions.QuickTurnToFaceEntity,("Player1","ChaosK1"))

	chaosk1.Blind=0
	chaosk1.Deaf=0
	chaosk1.Alpha = 0.0

	#darfuncs.LaunchMaxCamera("Palacio_Camera_chaos.cam",0,-1)

def ReiniciaCamaraChaosK1():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Bladex.ActivateInput()

def GiraCamara(obj_name, time):
	global paso_n
	global chaospos
	global init_tpos
	cam=Bladex.GetEntity("Camera")
	vtpos=init_tpos[0]-chaospos[0], 0.0, init_tpos[2]-chaospos[2]
	vtposnorm=AuxFuncs.Normalize(vtpos)
	paso_n=paso_n+1
	newvtposnorm=vtposnorm[0]*math.cos(paso_n*ANGLE_VARIATION)-vtposnorm[2]*math.sin(paso_n*ANGLE_VARIATION), 0.0, vtposnorm[0]*math.sin(paso_n*ANGLE_VARIATION)+vtposnorm[2]*math.cos(paso_n*ANGLE_VARIATION)
	newvtpos=newvtposnorm[0]*2000, 0.0, newvtposnorm[2]*2000
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	if paso_n==TOTAL_STEPS:
		cam.RemoveFromList("Timer60")
		cam.TimerFunc=""
		ReiniciaCamaraChaosK1()

def MuereChaosK1(entity_name):
	global paso_n
	global chaospos
	global init_tpos
	Bladex.DeactivateInput()
	#chaosk1.Data.Disappear(entity_name)
	cam=Bladex.GetEntity("Camera")
	char=Bladex.GetEntity("Player1")
	charpos=char.Position
	chaospos=chaosk1.Position
	vtpos=chaospos[0]-charpos[0], 0.0, chaospos[2]-charpos[2]
	vtposnorm=AuxFuncs.Normalize(vtpos)
	newvtposnorm=vtposnorm[0]*math.cos(3.14159/2.0)-vtposnorm[2]*math.sin(3.14159/2.0), 0.0, vtposnorm[0]*math.sin(3.14159/2.0)+vtposnorm[2]*math.cos(3.14159/2.0)
	newvtpos=newvtposnorm[0]*2000.0, 0.0, newvtposnorm[2]*2000.0
	cam.ESource="ChaosK1"
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	cam.SType=2
	cam.TType=0
	init_tpos=cam.TPos
	paso_n=0
	cam.TimerFunc=GiraCamara
	cam.SubscribeToList("Timer60")
	#AbreteSesamus(entity_name)

def CreateChaosSwitchOne():
	global nChaos

	if (char.Position[0] - 529198)**2 + (char.Position[2] - 90968)**2 > 3000**2:
		chaosk1.Position = 529198, char.Position[1], 90968
	else:
		chaosk1.Position = 529198, char.Position[1], 90968+7000

	nChaos = nChaos+1
	chaosk1.SetOnFloor()
	darfuncs.UnhideBadGuy(chaosk1.Name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, MueveCamaraChk,())
	ParticulateAppears(chaosk1.Name)

	Camerona()

def Encareitor():
	char.SetActiveEnemy(Bladex.GetEntity("ChaosK1"))
	chaosk1 = Bladex.GetEntity("ChaosK1")
	chaosk1.SetActiveEnemy(char)
	chaosk1.ResetChase()

def Camerona():
	cam=Bladex.GetEntity("Camera")
	AbreCam.PTS=[]
	AbreCam.CallBack = Encareitor

	AbreCam.PTS.append((537431,char.Position[1]-6000,100785),chaosk1.Position,3)
	AbreCam.PTS.append((520658,char.Position[1]-6000, 99322),chaosk1.Position,3)
	AbreCam.PTS.append((519897,char.Position[1]-6000, 84716),chaosk1.Position,3)
	AbreCam.PTS.append((536487,char.Position[1]-6000, 82600),chaosk1.Position,3)

	AbreCam.ZoomNode(0)
	AbreCam.ZoomNode(1)
	AbreCam.ZoomNode(2)
	AbreCam.ZoomNode(3)

	AbreCam.AbreCam()

def ParticulateAppears(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="EnergyConc"
	wps.Time2Live=60
	wps.RandomVelocity=0
	wps.Velocity=0,0,0
	wps.NormalVelocity=-5.0
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+1.5
	wps.PPS=600
	Bladex.GetEntity(PersonName).Alpha = 0.0
	PhantonFX.Delta = 0.015
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, PhantonFX.AppearsChar,(PersonName,))

def PartsDeath(PersonName = "Player1"):
	wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	wps.PersonName=PersonName
	wps.ParticleType="DeathCloud"
	wps.Time2Live=64
	wps.RandomVelocity=2.0
	wps.Velocity=0,0,0
	wps.NormalVelocity=0
	wps.YGravity=0
	wps.DeathTime=Bladex.GetTime()+5.0
	wps.PPS=600
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, PhantonFX.DisappearsChar,(PersonName,dust.BorraPorLasDudas2))
	PhantonFX.Delta  = 0.005


def FreezeMeGuy(PersonName):
	Bladex.GetEntity(PersonName).Freeze()

def ParticulateDeath(PersonName = "Player1"):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, RealPartDeath,(PersonName,))

def RealPartDeath(PersonName = "Player1"):
	per = Bladex.GetEntity(PersonName)
	per.CastShadows = 0
	per.Life = 0
	per.SetTmpAnmFlags(1,1,1,0,5,1,0)
	per.Wuea = Reference.WUEA_ENDED
	per.LaunchAnimation("Chk_dth0")
	per.AnmEndedFunc = FreezeMeGuy
	per.RasterMode  ="Read"
	"""
	fococaos=Bladex.CreateEntity("fococaos","Entity Spot",0,0,0)
	fococaos.Position = per.Position
	fococaos.Color=0,128,255
	fococaos.Intensity=2.5
	fococaos.Precission=0.5
	fococaos.CastShadows=0
	fococaos.Visible=0
	fococaos.Flick=1
	"""
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, PartsDeath,(PersonName,))

	ElectricShock(PersonName,0)

def ElectricShock(PersonName = "Player1",i=0):
	global PartesRayuela

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
	fococaos=Bladex.GetEntity("fococaos")
	if i<7*8:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.125,ElectricShock,(PersonName,(i+1)))
		if fococaos:
			fococaos.Intensity=whrandom.randint(1,5)
	else:
		if fococaos:
			fococaos.SubscribeToList("Pin")


	return rayo



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para demonio.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SndLdm1(ent,Time):
	dmn = Bladex.GetEntity("DemonioMaldito")
	_SndLdm1.Volume = 1
	_SndLdm1.Play(dmn.Position[0], dmn.Position[1], dmn.Position[2], 0)

def SndLdm2(ent,Time):
	dmn = Bladex.GetEntity("DemonioMaldito")
	_SndLdm2.Volume = 1
	_SndLdm2.Play(dmn.Position[0], dmn.Position[1], dmn.Position[2], 0)

def SndLdmOstia(ent,Time):
	dmn = Bladex.GetEntity("DemonioMaldito")
	_SndLdmOstia.Volume = 1
	_SndLdmOstia.Play(dmn.Position[0], dmn.Position[1], dmn.Position[2], 0)

def AparecenOtrosDos(sectorindex,entityname):
	if entityname == "Player1" :
		AparicionDemonio("uno",476347.827342, 84085.2, 21154.9966901)
		"""
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, AparicionDemonio,("dos",472060.019469, 84085.2, 16097.2286111,))
		"""
		AparicionDemonio("dos",472060.019469, 84085.2, 16097.2286111)
		secDem2.OnLeave = ""
		secDem2.OnEnter = ""
		AbreCam.LastTime = 2.0
		AbreCam.PTS = [((471238.092813, 79466.0381018, 19301.6233906), (476320.63871, 83514.351313, 21164.3399508), 2.0),
		               ((472030.515426, 82420.7517252, 21708.5202636), (476320.63871, 83514.351313, 21164.3399508), 2.0),
		               ((472751.933812, 82370.0325066, 20542.8341086), (472030.92739, 83516.315695, 16172.1964987), 2.0),
		               ((468614.631414, 80333.6760961, 21788.7191322), (472030.92739, 83516.315695, 16172.1964987), 2.0)]
		AbreCam.AbreCam()
		char.Angle = -3.1415*4/6

def InCoso(sectorindex,entityname):
	global insecDem2
	if entityname == "Player1" :
		insecDem2 = 1


def OutCoso(sectorindex,entityname):
	global insecDem2
	if entityname == "Player1" :
		insecDem2 = 0

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

def DespiertaDemonio(ent_name):
	demonio = Bladex.GetEntity(ent_name)
	demonio.Blind = 0
	demonio.Deaf  = 0
	demonio.ImDeadFunc=MuerteDemonio

def CreacionDemonio(name):
	demonio=Bladex.CreateEntity("Demon "+name, "Little_Demon", 0, 0, 0,"Person")
	demonio.Level=19
	EnemyTypes.EnemyDefaultFuncs(demonio)
	darfuncs.HideBadGuy(demonio.Name)

def AparicionDemonio(name,x,y,z):
	demonio=Bladex.GetEntity("Demon "+name)
	darfuncs.UnhideBadGuy(demonio.Name)
	demonio.Position = x, y, z
	demonio.Angle = 1.16677055278
	demonio.SetTmpAnmFlags(1,1,1,0,5,1)
	demonio.LaunchAnimation("Ldm_appears")
	demonio.AnmEndedFunc=DespiertaDemonio
	demonio.Alpha = 0.0
	demonio.Blind = 1
	demonio.Deaf  = 1
	PhantonFX.Delta = 0.005
	PhantonFX.AppearsChar(demonio.Name)
	LanzaMegaSurtidor(demonio.Position[0],demonio.Position[1],demonio.Position[2])

def DemonDone (ent_name):
	global NumDemMuer
	global insecDem2
	if("DemonioMaldito"==ent_name):
		if insecDem2 :
			secDem2.OnLeave = AparecenOtrosDos
		else:
			AparecenOtrosDos(0,"Player1")
	else:
		NumDemMuer = NumDemMuer-1
		if NumDemMuer == 0 :
			Abismo()

def MuerteDemonio(ent_name):
	demonio=Bladex.GetEntity(ent_name)
	demonio.Data.ImDeadFunc (ent_name)

	Bladex.AddScheduledFunc(Bladex.GetTime()+demonio.Data.ImplosionPeriod+demonio.Data.DeathBallPeriod, DemonDone, (ent_name,))

def Abismo():

	abismoi.OpenDoor()
	abismod.OpenDoor()
	#Bladex.ExeMusicEvent(-1)

def Bismo():

	abismoi.CloseDoor()
	abismod.CloseDoor()


def LastStepCameraBlaBla(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	demonio=Bladex.GetEntity("DemonioMaldito")
	demonio.Blind = 0
	demonio.Deaf  = 0




def NextStepCameraBlaBla(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Kaos_Camera_abajo.cam",249,355)
	cam.AddCameraEvent(253-249,SndLdmOstia)
	cam.AddCameraEvent(296-249,SndLdm2)

	cam.AddCameraEvent(-1,LastStepCameraBlaBla)

def ElDemonio(sectorindex,entityname):
	if(entityname == "Player1"):
		Cierrarastdem()
		ELDEMOSEC.OnEnter = ""
		demonio=Bladex.GetEntity("DemonioMaldito")
		demonio.Position = 477145, 67828, 16801
		demonio.Angle = 1.16677055278

		demonio.SetTmpAnmFlags(1,1,1,0,5,1)
		demonio.LaunchAnimation("Ldm_saltarin_enric")

		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("Kaos_Camera_arriba.cam",0,248)

		cam.AddCameraEvent(180,SndLdm1)

		cam.AddCameraEvent(-1,NextStepCameraBlaBla)
		Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-7"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("Combate4",))



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para chaos_death.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ApagaRayo():
	rayot=Bladex.GetEntity("RayoTornado")
	luzrayot=Bladex.GetEntity("LuzRayoTornado")
	rayot.Active = 0
	luzrayot.Intensity=0.0

def DisparaRayo():
	#global nr
	global sonidosrayotornado
	global sndnumber
	rayot=Bladex.GetEntity("RayoTornado")
	luzrayot=Bladex.GetEntity("LuzRayoTornado")
	soundrayot=Bladex.GetEntity("SonidoRayoTornado")
	rayot.Active   = 1
	rayot.Position = 942700+GenR.randint(-6000,6000), 325000+GenR.randint(-3000,3000), 169650+GenR.randint(-6000,6000)
	rayot.Target   = 942700+GenR.randint(-5000,5000), 325000+GenR.randint(-2000,2000), 169650+GenR.randint(-5000,5000)
	xl, yl, zl = (rayot.Position[0]+rayot.Target[0])/2.0, (rayot.Position[1]+rayot.Target[1])/2.0, (rayot.Position[2]+rayot.Target[2])/2.0
	luzrayot.Position=xl, yl, zl
	luzrayot.Intensity=80.0
	sonidosrayotornado[sndnumber].Position=xl, yl, zl
	sonidosrayotornado[sndnumber].StopSound()
	sonidosrayotornado[sndnumber].PlaySound(0)
	sndnumber=sndnumber+1
	if (sndnumber>len(sonidosrayotornado)-1):
		sndnumber=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.06, ApagaRayo, ())
	#nr=nr+1
	#print nr

def RepiteRayo():
	rayot=Bladex.GetEntity("RayoTornado")
	DisparaRayo()
	if rayot.Data.Active:
		variation=whrandom.uniform(-rayot.Data.FrecuencyVariation, rayot.Data.FrecuencyVariation)
		Bladex.AddScheduledFunc(Bladex.GetTime()+rayot.Data.Frecuency+variation, RepiteRayo, ())

def PlayRayoPeriodico():
	rayot=Bladex.GetEntity("RayoTornado")
	rayot.Data.Active=1
	RepiteRayo()

def GiraTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(3.0*30.0))
	corona.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(6.0*30.0))

def DesapareceTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.Alpha=corona.Alpha=max(0.0, corona.Alpha-1.0/(3.0*30.0))
	if vortice.Alpha<=0.0:
		vortice.RemoveFromList("Timer30")
		vortice.TimerFunc=""
		vortice.Scale=0.5
		corona.Scale=0.55
		Bladex.GetEntity("RayoTornado").Data.Active=0
	else:
		GiraTornadoGrad("Vortice", 0)

def DesapareceTornado():
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	rayot=Bladex.GetEntity("RayoTornado")
	rayot.Data.Frecuency=1.5
	rayot.Data.FrecuencyVariation=1.45
	Bladex.GetEntity("PVortice").DeathTime=Bladex.GetTime()+1.0/60.0
	Bladex.GetEntity("PCorona").DeathTime=Bladex.GetTime()+1.0/60.0
	vortice.TimerFunc=DesapareceTornadoGrad

def ApareceTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.Alpha=corona.Alpha=min(0.99, corona.Alpha+1.0/(6.0*30.0))
	if vortice.Alpha>=0.99:
		vortice.TimerFunc=GiraTornadoGrad
	else:
		GiraTornadoGrad("Vortice", 0)

def ApareceTornado():
	global vortice
	global corona
	global pvor
	global pcor

	try:
		soundtornado.Play(940000,322000,170000, -1)
	except:
		pass

	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	pvor=Bladex.CreateEntity("PVortice", "Entity Particle System Dobj", 0, 0, 0)
	pvor.ObjectName="Vortice"
	pvor.ParticleType="Tornado1"
	pvor.YGravity=0
	pvor.Velocity=0, 0, 0
	pvor.NormalVelocity=5
	pvor.RandomVelocity=6
	pvor.FollowFactor=1.0
	pvor.PPS=30
	pvor.Time2Live=90
	pcor=Bladex.CreateEntity("PCorona", "Entity Particle System Dobj", 0, 0, 0)
	pcor.ObjectName="Corona"
	pcor.ParticleType="Tornado2"
	pcor.YGravity=0
	pcor.Velocity=0, 0, 0
	pcor.NormalVelocity=10
	pcor.RandomVelocity=6
	pcor.FollowFactor=0.9
	pcor.PPS=60
	pcor.Time2Live=90
	vortice.TimerFunc=ApareceTornadoGrad
	vortice.SubscribeToList("Timer30")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, PlayRayoPeriodico, ())



#############################
#     Funciones comunes     #
#############################

def GlowSizeVariationGrad(light_name, time):
	light=Bladex.GetEntity(light_name)
	light.SizeFactor=light.SizeFactor+light.Data.SizeVar
	if ((light.Data.SizeVar>=0.0) and (light.SizeFactor>=light.Data.EndSize)) or ((light.Data.SizeVar<0.0) and (light.SizeFactor<=light.Data.EndSize)):
		light.SizeFactor=light.Data.EndSize
		light.RemoveFromList("Timer30")
		light.TimerFunc=""
		if light.Data.DestroyOnEnd:
			light.SubscribeToList("Pin")

def GlowSizeVariation(light_name, init_size, end_size, var_time, destroy=0):
	light=Bladex.GetEntity(light_name)
	light.SizeFactor=init_size
	InitDataField.Initialise(light)
	light.Data.EndSize=end_size
	light.Data.SizeVar=(end_size-init_size)/(30.0*var_time)
	light.Data.DestroyOnEnd=destroy
	light.TimerFunc=GlowSizeVariationGrad
	light.SubscribeToList("Timer30")

def FadeAndScaleAuraGrad(ent_name, time):
	aura=Bladex.GetEntity(ent_name)
	aura.Data.CurrentSize=aura.Data.CurrentSize+aura.Data.SizeVar
	aura.Data.CurrentAlpha=aura.Data.CurrentAlpha+aura.Data.AlphaVar
	if aura.Data.CurrentAlpha<0.0:
		aura.Data.CurrentAlpha=0.0
	elif aura.Data.CurrentAlpha>1.0:
		aura.Data.CurrentAlpha=1.0
	aura.SetAuraParams(aura.Data.CurrentSize, aura.Data.CurrentAlpha, 1, 0, 0, 1)
	if ((aura.Data.SizeVar>0 and aura.Data.CurrentSize>=aura.Data.EndSize) or (aura.Data.SizeVar<0 and aura.Data.CurrentSize<=aura.Data.EndSize)):
		aura.RemoveFromList("Timer30")
		aura.TimerFunc=""
		if aura.Data.DestroyOnEnd:
			aura.SubscribeToList("Pin")
		else:
			aura.SetAuraParams(aura.Data.EndSize, aura.Data.EndAlpha, 1, 0, 0, 1)

def FadeAndScaleAura(aura_name, init_size, end_size, init_alpha, end_alpha, time, destroy=0):
	aura=Bladex.GetEntity(aura_name)
	InitDataField.Initialise(aura)
	aura.Data.CurrentSize=init_size
	aura.Data.EndSize=end_size
	aura.Data.SizeVar=(end_size-init_size)/(time*30.0)
	aura.Data.CurrentAlpha=init_alpha
	aura.Data.EndAlpha=end_alpha
	aura.Data.AlphaVar=(end_alpha-init_alpha)/(time*30.0)
	aura.Data.DestroyOnEnd=destroy
	aura.TimerFunc=FadeAndScaleAuraGrad
	aura.SubscribeToList("Timer30")

def FadeAndScaleGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.InitTime
	obj.Alpha=obj.Data.InitAlpha+obj.Data.AlphaInitVel*curr_time+0.5*obj.Data.AlphaAcc*curr_time**2
	obj.Scale=obj.Data.InitScale+obj.Data.ScaleInitVel*curr_time+0.5*obj.Data.ScaleAcc*curr_time**2
	if obj.Data.AngleVar:
		ang=whrandom.uniform(-obj.Data.AngleVar, obj.Data.AngleVar)
		obj.RotateRel(0, 0, 0, 0, 0, 1, ang)
	if curr_time>=obj.Data.TotalTime:
		obj.Alpha=obj.Data.EndAlpha
		obj.Scale=obj.Data.EndScale
		obj.RemoveFromList("Timer30")
		obj.TimerFunc=""
		if obj.Data.DestroyOnEnd==1:
			obj.SubscribeToList("Pin")
		elif obj.Data.DestroyOnEnd==2:
			obj.RemoveFromWorld()

def FadeAndScale(obj_name, pos, init_alpha, end_alpha, alpha_acc, init_scl, end_scl, scl_acc, time, ang_var=0, destroy=0):
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=init_alpha
	obj.Scale=init_scl
	obj.Position=pos
	InitDataField.Initialise(obj)
	obj.Data.InitAlpha=init_alpha
	obj.Data.EndAlpha=end_alpha
	obj.Data.AlphaAcc=alpha_acc*2.0*(end_alpha-init_alpha)/time**2
	obj.Data.AlphaInitVel=(end_alpha-init_alpha-alpha_acc*(end_alpha-init_alpha))/time
	obj.Data.InitScale=init_scl
	obj.Data.EndScale=end_scl
	obj.Data.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.AngleVar=ang_var
	obj.Data.DestroyOnEnd=destroy
	obj.Data.InitTime=Bladex.GetTime()
	obj.Data.TotalTime=time
	obj.TimerFunc=FadeAndScaleGrad
	obj.SubscribeToList("Timer30")

def ScaleObjectGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.InitTime
	obj.Scale=obj.Data.InitScale+obj.Data.ScaleInitVel*curr_time+0.5*obj.Data.ScaleAcc*curr_time**2
	if obj.Data.WhileSclFunc:
		apply(obj.Data.WhileSclFunc, obj.Data.WhileSclArgs)
	if curr_time>=obj.Data.TotalTime:
		obj.Scale=obj.Data.EndScale
		obj.RemoveFromList("Timer30")
		obj.TimerFunc=""
		if obj.Data.EndSclFunc:
			apply(obj.Data.EndSclFunc, obj.Data.EndSclArgs)
		if obj.Data.DestroyOnEnd==1:
			obj.SubscribeToList("Pin")
		elif obj.Data.DestroyOnEnd==2:
			obj.RemoveFromWorld()

def ScaleObject(obj_name, init_scl, end_scl, scl_acc, time, WhileSclFunc="", WhileSclArgs=(), EndSclFunc="", EndSclArgs=(), destroy=0):
	obj=Bladex.GetEntity(obj_name)
	obj.Scale=init_scl
	InitDataField.Initialise(obj)
	obj.Data.InitScale=init_scl
	obj.Data.EndScale=end_scl
	obj.Data.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.WhileSclFunc=WhileSclFunc
	obj.Data.WhileSclArgs=WhileSclArgs
	obj.Data.EndSclFunc=EndSclFunc
	obj.Data.EndSclArgs=EndSclArgs
	obj.Data.DestroyOnEnd=destroy
	obj.Data.InitTime=Bladex.GetTime()
	obj.Data.TotalTime=time
	obj.TimerFunc=ScaleObjectGrad
	obj.SubscribeToList("Timer30")



###############################
#     Funciones de camara     #
###############################

def RestartEndScene(camera, frame):
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Dist=4500.0
	cam.Cut()
	Bladex.SetListenerPosition(1)
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.LoadLevel("final")

def LaunchNextCamera(camera, frame):
	global camera_sequence
	global current_camera
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera(camera_sequence[current_camera][0], camera_sequence[current_camera][1], camera_sequence[current_camera][2])
	cam.Cut()
	if camera_sequence[current_camera][3]:
		apply(camera_sequence[current_camera][3], camera_sequence[current_camera][4])
	current_camera=current_camera+1
	if current_camera>=len(camera_sequence):
		cam.AddCameraEvent((1580-1121)*3/4, GrantEndOfAbyss)
		cam.AddCameraEvent(-1, RestartEndScene)
	else:
		cam.AddCameraEvent(-1, LaunchNextCamera)

def GrantEndOfAbyss(camera, frame):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, Bladex.TriggerEvent, (20,))

def SonidoDePasoComoe(xax,xbx):
	i = whrandom.randint(0, 2)
	x,y,z = char.Position
	chaospasopie[i].Play(x,y,z,0)

def CorreComoLoco():
	pasoschaos=[2, 8, 14, 20, 26, 32, 38, 45, 51, 57, 65, 72, 78]
	for i in pasoschaos:
		Bladex.GetEntity("Camera").AddCameraEvent(i, SonidoDePasoComoe)

def LanzaCamarasFinal():
	global camera_sequence
	global current_camera
	current_camera=0
	camera_sequence=[]
	camera_sequence.append("FinalCamera01.cam", 1, 100, "", ())
	camera_sequence.append("FinalCamera02.cam", 101, 290, "", ())
	camera_sequence.append("FinalCamera01.cam", 291, 340, "", ())
	camera_sequence.append("FinalCamera02.cam", 341, 500, "", ())
	camera_sequence.append("FinalCamera01.cam", 501, 550, "", ())
	camera_sequence.append("FinalCamera02.cam", 551, 755, "", ())
	camera_sequence.append("FinalCamera03.cam", 756, 970, ElViejoSeQuedaSinTraje, ())
	camera_sequence.append("FinalCamera02.cam", 971, 1120, "", ())
	camera_sequence.append("FinalCamera03.cam", 1121, 1580, LanzaLenguasAPorElViejo, ())
	LaunchNextCamera(0, 0)
	CorreComoLoco()



##################
#     Escena     #
##################

def LoQueYoTeDiga():
	cv=Bladex.GetEntity("ConcentracionVortice")
	cv.DeathTime=Bladex.GetTime()+0.1
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, DesapareceTornado, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, AuxFuncs.FadeTo, (2.0, 4.0))

def YSeFundenLasPilas():
	FadeAndScaleAura("AuraCilindroGordo", 1000.0, 10.0, 1.0, 0.0, 1.5, 1)
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 160.0, 0.0, 5.0, 0, 10.0, 0.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, LoQueYoTeDiga, ())

def LoChupaGradualmente(obj_name, time):
	VejeteF=Bladex.GetEntity("VejeteFinal")
	VejeteF.Scale=VejeteF.Scale*0.9
	pdv=Bladex.GetEntity(obj_name)
	pdv.YGravity=pdv.YGravity-200
	pdv.PPS=max(100, pdv.PPS-10)
	if pdv.YGravity<=-2500:
		VejeteF.RasterMode="Full"
		pdv.RemoveFromList("Timer10")
		pdv.TimerFunc=""
		pdv.PPS=100
		pdv.DeathTime=Bladex.GetTime()+1.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, YSeFundenLasPilas, ())

def ElViejoSeVaPorElSumidero(pdv):
	pdv.NormalVelocity=-2
	pdv.TimerFunc=LoChupaGradualmente
	pdv.SubscribeToList("Timer10")

def ATomarPorCuloElViejo():
	cilgo=Bladex.GetEntity("CilindroGordo")
	cilgo.Move(500.0, 0.0, 0.0)
	FadeAndScaleAura("AuraCilindroGordo", 10.0, 1000.0, 0.0, 1.0, 1.0)
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 80.0, 160.0, 1.0, 0, 8.0, 10.0)
	pdv=Bladex.CreateEntity("DesintegracionVejete","Entity Particle System Dperson", 0, 0, 0)
	pdv.PersonName="VejeteFinal"
	pdv.ParticleType="EnergyConc"
	pdv.YGravity=0
	pdv.RandomVelocity=2
	pdv.NormalVelocity=-8
	pdv.Velocity=0.0, 0.0, 0.0
	pdv.Time2Live=60
	pdv.PPS=400

	try:
		rayotractor2.Play(940000,334000,170000, 0)
	except:
		pass

	Bladex.GetEntity("VejeteFinal").RasterMode="Read"
	AuxFuncs.FadeObject("VejeteFinal", 1.0, 0.01, 3.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, ElViejoSeVaPorElSumidero, (pdv,))

def GiraLenguasTimer(obj_name, time):
	genleng=Bladex.GetEntity(obj_name)
	genleng.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(4.0*30.0))
	genleng.RotateRel(0, 0, 0, 0, 1, 0, 3.14159/(2.0*30.0))

def GiraLenguas(genleng):
	genleng.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(4.0*30.0))
	genleng.RotateRel(0, 0, 0, 0, 1, 0, 3.14159/(2.0*30.0))

def BorraLenguas(genleng, lps):
	lps.DeathTime=Bladex.GetTime()+3.0
	genleng.TimerFunc=GiraLenguasTimer
	genleng.SubscribeToList("Timer30")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ScaleObject, (genleng.Name, 3.0, 0.1, 1, 1.0, GiraLenguas, (genleng,), ATomarPorCuloElViejo, (), 2))

def LanzaLenguasAPorElViejo():
	genleng=Bladex.GetEntity("GeneradorLenguas")
	genleng.Orientation=0.707107,0.707107,0.000000,0.000000
	lps=Bladex.CreateEntity("LenguasPS","Entity Particle System Dobj", 0, 0, 0)
	lps.ObjectName=genleng.Name
	lps.ParticleType="EnergyDisint"
	lps.YGravity=0
	lps.RandomVelocity=2
	lps.NormalVelocity=0
	lps.Velocity=0.0,0.0,0.0
	lps.Time2Live=60
	lps.PPS=300

	absorcion= Bladex.GetSound("Absorcion")
	absorcion.Play(940000,334000,170000, 0)

	genlengdin=genleng.Data.dinobjdata
	Objects.DisplaceObjectFromTo(genlengdin, (943255.0, 325500.0, 169710.0), (943255.0, 337245.0, 169710.0), 6000.0, 0.0, "", "", "", GiraLenguas, (genleng,), BorraLenguas, (genleng, lps))

def DesaparecenLosRestosDelTraje(pda):
	pda.PPS=600
	pda.DeathTime=Bladex.GetTime()+1.0

def ATomarPorCuloElTraje():
	try:
		rayotractor.Play(940000,334000,170000, 0)
	except:
		pass

	pda=Bladex.CreateEntity("DesintegracionAnAhkard","Entity Particle System Dperson", 0, 0, 0)
	pda.PersonName="Ank2Final"
	pda.ParticleType="EnergyDisint"
	pda.YGravity=-600
	pda.RandomVelocity=1
	pda.NormalVelocity=-1
	pda.Velocity=0.0, 0.0, 0.0
	pda.Time2Live=60
	pda.PPS=1200
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, DesaparecenLosRestosDelTraje, (pda,))

def ApareceYDesapareceElHazDeLuz():
	v=Bladex.GetEntity("Vortice")
	x, y, z=v.Position[0], v.Position[1]+11000.0, v.Position[2]-500.0
	cilgo=Bladex.GetEntity("CilindroGordo")
	cilgo.Position=x, y, z
	r1, g1, b1 = 0.4, 0.6, 1.0
	r2, g2, b2 = 0.1, 0.2, 1.0
	acilgo=Bladex.CreateEntity("AuraCilindroGordo", "Entity Aura", 0, 0, 0)
	acilgo.SetAuraParams(2000, 1, 1, 0, 0, 1)
	acilgo.SetAuraGradient(1, r1, g1, b1, 1.0, 0.0, r2, g2, b2, 0.0, 0.8)
	cilgo.Link(acilgo)
	acilgo.SetAuraActive(1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, FadeAndScaleAura, (acilgo.Name, 2000.0, 10.0, 1.0, 0.0, 1.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.2, AuxFuncs.SpotIntensityVariation, ("LuzImpacto", 160.0, 80.0, 1.0, 0, 15.0, 8.0))

def RemoveElTrajeDeLosCojones(Ank2F):
	Ank2F.TurnOff()
	Ank2F.RemoveFromWorld()

def ElViejoSeQuedaSinTraje():
	AuxFuncs.FadeFrom(1.0, 0.0, 200, 220, 255)
	ApareceYDesapareceElHazDeLuz()
	ank=Bladex.GetEntity("AnAhkard")
	ank.Freeze()
	ank.RemoveFromWorld()
	VejeteF=Bladex.GetEntity("VejeteFinal")
	VejeteF.Orientation=0.707107,0.707107,0.000000,0.000000
	VejeteF.Position=942824.188, 340730.531, 169709.609
	VejeteF.Animation="Vejete_final_03"
	VejeteF.SendSectorMsgs=0
	VejeteF.TurnOn()
	Ank2F=Bladex.GetEntity("Ank2Final")
	Ank2F.Orientation=0.707107,0.707107,0.000000,0.000000
	Ank2F.Position=942974.437575, 341570.40625, 169642.280646
	Ank2F.Animation="Ank_final_03"
	Ank2F.SendSectorMsgs=0
	Ank2F.TurnOn()
	Ank2F.SelfIlum=0.5
	AuxFuncs.FadeObject("Ank2Final", 1.0, 0.01, 4.0)
	ATomarPorCuloElTraje()
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, RemoveElTrajeDeLosCojones, (Ank2F,))
	FadeAndScale("OndaExp", (942700.0, 342725.0, 169750.0), 0.96, 0.0, -1, 0.1, 12.0, -1, 2.0, 1.0, 2)
	Bladex.GetEntity("LuzImpacto").Intensity=160.0

def SeConcentraEnergiaEnElVortice():
	nv=Bladex.GetEntity("NucleoVortice")
	v=Bladex.GetEntity("Vortice")
	x, y, z=v.Position[0], v.Position[1]+2000.0, v.Position[2]-500.0
	nv.Position=x, y, z
	cv=Bladex.CreateEntity("ConcentracionVortice","Entity Particle System Dobj", x, y, z)
	cv.ObjectName=nv.Name
	cv.ParticleType="BigBlueEnergyCon"
	cv.YGravity=0
	cv.RandomVelocity=5
	cv.NormalVelocity=-20
	cv.Velocity=0.0,-1000.0,0.0
	cv.Time2Live=60
	cv.PPS=400
	luzimp=Bladex.GetEntity("LuzImpacto")
	luzimp.Position=x, y+2000.0, z
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 0.0, 80.0, 3.0, 0, 0.0, 8.0)

def YApareceUnBonitoUnTornado(EntityName, EventName):
	ApareceTornado()
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, SeConcentraEnergiaEnElVortice, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+8.5, GlowSizeVariation, ("LuzImpacto", 8.0, 15.0, 1.25))
	Bladex.AddScheduledFunc(Bladex.GetTime()+9.0, AuxFuncs.FadeTo, (0.75, 0.0, 200, 220, 255))

def PeroNoLeQuedaSuficientePoder(EntityName, EventName):
	mcps=Bladex.GetEntity("MissileConcPS")
	lmc=Bladex.GetEntity("LuzMissileConc")
	mcps.ParticleType="RedMissileDissip"
	mcps.YGravity=800.0
	mcps.FollowFactor=0.0
	mcps.NormalVelocity=0.0
	mcps.Time2Live=30
	mcps.DeathTime=Bladex.GetTime()+0.5
	AuxFuncs.SpotIntensityVariation("LuzMissileConc", 4.0, 0.0, 1.15)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, lmc.SubscribeToList, ("Pin",))

def ElMuyCapulloIntentaUnUltimoAtaque(EntityName, EventName):
	mcps=Bladex.CreateEntity("MissileConcPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	mcps.PersonName="AnAhkard"
	mcps.PersonNodeName="R_Hand"
	mcps.FollowFactor=1.0
	mcps.ParticleType="RedMissileConc"
	mcps.PPS=600
	mcps.YGravity=0.0
	mcps.Friction=0.0
	mcps.Velocity=0.0, 0.0, 0.0
	mcps.RandomVelocity=-2.0
	mcps.NormalVelocity=-4.0
	mcps.Time2Live=60
	ank=Bladex.GetEntity(EntityName)
	node=ank.GetNodeIndex("R_Hand")
	x,y,z=ank.GraspPos("R_Hand")
	lmc=Bladex.CreateEntity("LuzMissileConc", "Entity Spot", x, y, z)
	lmc.Color=255, 50, 40
	lmc.Intensity=0.0
	lmc.Precission=0.01
	lmc.Visible=0
	lmc.CastShadows=0
	ank.LinkToNode(lmc,node)
	fuego.Play(940000,334000,170000, 0)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro3"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, AuxFuncs.SpotIntensityVariation, ("LuzMissileConc", 0.0, 4.0, 3.0))


def RespiraViejo1(EntityName, EventName):

	try:
		viejo1.Play(940000,334000,170000, 1)
	except:
		pass


def RespiraViejo2(EntityName, EventName):

	try:
		viejo2.Play(940000,334000,170000, 0)
	except:
		pass

def RespiraViejo3(EntityName, EventName):

	try:
		viejo1.Play(940000,334000,170000, 2)
	except:
		pass


def EmpiezaEscenaFinal():

	ank=Bladex.GetEntity("AnAhkard")
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	ank.Alpha=1.0
	ank.Wuea=Reference.WUEA_ENDED
	ank.SetTmpAnmFlags(1,1,1,0,5,1,0)
	ank.LaunchAnimation("Ank_final_02")
	ank.Position=942747.0, 341292.0, 169614.0
	ank.Angle=3.14159
	ank.AddAnmEventFunc("LastMissileConc", ElMuyCapulloIntentaUnUltimoAtaque)
	ank.AddAnmEventFunc("Respiracion1", RespiraViejo1)
	ank.AddAnmEventFunc("Respiracion2", RespiraViejo2)
	ank.AddAnmEventFunc("Respiracion3", RespiraViejo3)
	ank.AddAnmEventFunc("LastMissileDissip", PeroNoLeQuedaSuficientePoder)
	ank.AddAnmEventFunc("TornadoAppearance", YApareceUnBonitoUnTornado)
	char.Wuea=Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("final_02")
	char.Position=897522.0, 341748.0, 170437.0
	char.Angle=3.14159
	Bladex.SetListenerPosition(2)
	LanzaCamarasFinal()
	AuxFuncs.FadeFrom(1.5, 0.0)
	for i in range(3,12):
		l=Bladex.GetEntity("Lucero"+`i`)
		l.Lights=[ (80,0.1,(221,116,0)) ]
	for i in range(12,14):
		l=Bladex.GetEntity("Lucero"+`i`)
		l.Lights=[ (150,0.1,(221,116,0)) ]
		l.FiresIntensity=[ 2 ]

def Paseito2():
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	AuxFuncs.FadeFrom(1.25, 0.0)
	char.Angle=1.55059829607
	char.Position=843593.971491, 335684.430404, 181005.644166
	cam.TPos=char.Position[0]-10000.0, char.Position[1]-1000.0, char.Position[2]-2000.0
	cam.Dist=3000.0
	char.GoToJogging=1
	char.GoTo(827909.832635, 335434.407796, 180827.84805)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AuxFuncs.FadeTo, (1.25, 1.75))

def Paseito1():
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	AuxFuncs.FadeFrom(1.25, 0.0)
	char.Angle=0.0
	char.Position=825242.88592, 335431.03827, 156345.141086
	cam.TPos=char.Position[0]+4000.0, char.Position[1]-1000.0, char.Position[2]
	cam.Dist=2000.0
	char.GoToJogging=1
	char.GoTo(827442.748485, 335453.996771, 173250.30669)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AuxFuncs.FadeTo, (1.25, 1.75))

def Vistazo2():
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	cam.TPos=char.Position[0]-2000.0, char.Position[1]-1500.0, char.Position[2]-1000.0
	cam.Dist=1600.0
	AuxFuncs.FadeFrom(2.0, 0.0)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("final_01")
	char.Angle=3.14159
	char.Position=827909.832635, 335434.407796, 180827.84805
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AuxFuncs.FadeTo, (1.25, 1.75))

def Vistazo1():
	char=Bladex.GetEntity("Player1")
	cam=Bladex.GetEntity("Camera")
	cam.TPos=char.Position[0], char.Position[1]-2000.0, char.Position[2]+2000.0
	cam.Dist=1400.0
	AuxFuncs.FadeFrom(2.0, 0.0)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("final_01")
	char.Angle=3.14159
	char.Position=827442.748485, 335453.996771, 173250.30669
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AuxFuncs.FadeTo, (1.25, 1.75))


### esta funcion solo se ejecuta si el jugador mata a anakard cerca del altar

def Paseitos():
	cam=Bladex.GetEntity("Camera")
	cam.SType=2
	cam.TType=0
	cam.ESource="Player1"
	Paseito1()
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.5, Vistazo1, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, Paseito2, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+16.5, Vistazo2, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+22.0, EmpiezaEscenaFinal, ())

def MePreguntoDondeDemoniosSeHaMetido(EntityName):
	char=Bladex.GetEntity("Player1")
	Bladex.ExeMusicEvent(-1)
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	char.LaunchAnmType("final_01")
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, AuxFuncs.FadeTo, (1.5, 1.5))
	for i in range(3,15):
		Bladex.RemoveTriggerSectorFunc("GLucero"+`i`, "OnEnter")
		Bladex.RemoveTriggerSectorFunc("GLucero"+`i`, "OnLeave")
	if char.Position[0]>905000.0:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera8b"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, Paseitos, ())
	else:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-7"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.0, EmpiezaEscenaFinal, ())

def MuereElBichoMalo(EntityName):
	ank=Bladex.GetEntity(EntityName)
	char=Bladex.GetEntity("Player1")
	AuxFuncs.FadeObject(EntityName, ank.Alpha, 0.0, 1.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(44,))
	if char.Wuea==Reference.WUEA_WAIT:
		char.AnmEndedFunc=MePreguntoDondeDemoniosSeHaMetido
	else:
		MePreguntoDondeDemoniosSeHaMetido("Player1")

def CreaObjetosEnergeticos():
	global ondaexp
	global cilgo
	global cilgodin
	global luzimp
	ondaexp=Bladex.CreateEntity("OndaExp", "OndaExpansiva", 94355.2677885, -3008.18632875, 172034.430763)
	cilgo=Bladex.CreateEntity("CilindroGordo", "LuzDivinaGorda", 94375, -11000, 172000)
	ondaexp.Orientation=cilgo.Orientation=0.707107,0.707107,0.000000,0.000000
	ondaexp.CastShadows=cilgo.CastShadows=0
	ondaexp.SelfIlum=cilgo.SelfIlum=1
	ondaexp.RasterMode=cilgo.RasterMode="AdditiveAlpha"
	ondaexp.RasterMode=cilgo.RasterMode="Read"
	ondaexp.Alpha=cilgo.Alpha=0.01
	cilgodin=Objects.CreateDinamicObject(cilgo.Name)
	cilgodin.Timer="Timer30"
	luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", 0, 0, 0)
	luzimp.Color=60, 170, 255
	luzimp.Intensity=0.0
	luzimp.Precission=0.06
	luzimp.CastShadows=0
	luzimp.SizeFactor=0.0
	luzimp.GlowTestZ=0
	genleng=Bladex.CreateEntity("GeneradorLenguas", "Helice", 0, 0, 0)
	genleng.Scale=3.0
	genleng.Orientation=0.707107,0.707107,0.000000,0.000000
	genleng.CastShadows=0
	genleng.Alpha=0.0
	genlengdin=Objects.CreateDinamicObject(genleng.Name)
	genlengdin.Timer="Timer30"
	nv=Bladex.CreateEntity("NucleoVortice", "SemiBolaRayos", 0, 0, 0)
	nv.Scale=1.0
	nv.Orientation=-0.707107,0.707107,0.000000,0.000000
	nv.Alpha=0.0
	nv.CastShadows=0

def CreaTornado():
	global sonidosrayotornado
	vortice=Bladex.CreateEntity("Vortice", "Vortice1", 942700, 325000, 170250) #169650)
	corona=Bladex.CreateEntity("Corona", "Vortice2", 942700, 325500, 170250) #169650)
	vortice.Orientation=corona.Orientation=0.707107,0.707107,0.000000,0.000000
	vortice.Scale=0.5
	corona.Scale=0.55
	vortice.CastShadows=corona.CastShadows=0
	vortice.Alpha=corona.Alpha=0.0
	vortice.SelfIlum=corona.SelfIlum=1.0
	vortice.SendSectorMsgs=corona.SendSectorMsgs=0
	vortice.SendTriggerSectorMsgs=corona.SendTriggerSectorMsgs=0
	vortice.RasterMode=corona.RasterMode="AdditiveAlpha"
	vortice.RasterMode=corona.RasterMode="Read"
	rayot=Bladex.CreateEntity("RayoTornado", "Entity ElectricBolt", 942700.0, 325000.0, 169650.0)
	rayot.Target=943700.0, 326000.0, 170650.0
	rayot.MaxAmplitude=400.0
	rayot.MinSectorLength=1000000.0
	rayot.Active=0
	rayot.Damage=0
	InitDataField.Initialise(rayot)
	rayot.Data.Active=0
	rayot.Data.Frecuency=1.5
	rayot.Data.FrecuencyVariation=1.45
	xl, yl, zl = (rayot.Position[0]+rayot.Target[0])/2.0, (rayot.Position[1]+rayot.Target[1])/2.0, (rayot.Position[2]+rayot.Target[2])/2.0
	luzrayot=Bladex.CreateEntity("LuzRayoTornado", "Entity Spot", xl, yl, zl)
	luzrayot.Color=60, 170, 255
	luzrayot.Intensity=0.0
	luzrayot.Precission=0.06
	luzrayot.Visible=0
	luzrayot.CastShadows=0
	soundrayot1=Bladex.CreateEntity("SonidoRayoTornado1", "Entity Sound", xl, yl, zl)
	soundrayot1.SetSound("../../Sounds/trueno5.wav")
	soundrayot1.Volume=1.0
	soundrayot1.MinDistance=150000
	soundrayot1.MaxDistance=300000
	soundrayot2=Bladex.CreateEntity("SonidoRayoTornado2", "Entity Sound", xl, yl, zl)
	soundrayot2.SetSound("../../Sounds/trueno6.wav")
	soundrayot2.Volume=1.0
	soundrayot2.MinDistance=150000
	soundrayot2.MaxDistance=300000
	soundrayot3=Bladex.CreateEntity("SonidoRayoTornado3", "Entity Sound", xl, yl, zl)
	soundrayot3.SetSound("../../Sounds/trueno5.wav")
	soundrayot3.Volume=1.0
	soundrayot3.MinDistance=150000
	soundrayot3.MaxDistance=300000
	soundrayot4=Bladex.CreateEntity("SonidoRayoTornado4", "Entity Sound", xl, yl, zl)
	soundrayot4.SetSound("../../Sounds/trueno6.wav")
	soundrayot4.Volume=1.0
	soundrayot4.MinDistance=150000
	soundrayot4.MaxDistance=300000
	soundrayot5=Bladex.CreateEntity("SonidoRayoTornado5", "Entity Sound", xl, yl, zl)
	soundrayot5.SetSound("../../Sounds/trueno5.wav")
	soundrayot5.Volume=1.0
	soundrayot5.MinDistance=150000
	soundrayot5.MaxDistance=300000
	soundrayot6=Bladex.CreateEntity("SonidoRayoTornado6", "Entity Sound", xl, yl, zl)
	soundrayot6.SetSound("../../Sounds/trueno6.wav")
	soundrayot6.Volume=1.0
	soundrayot6.MinDistance=150000
	soundrayot6.MaxDistance=300000
	sonidosrayotornado=[soundrayot1, soundrayot2, soundrayot3, soundrayot4, soundrayot5, soundrayot6]

def mbm():
	AnAhkard.Life=0

def rbm():
	AnAhkard.UnFreeze()
	AnAhkard.PutToWorld()
	AnAhkard.Life=100
	VejeteF.TurnOff()
	VejeteF.Position=942824.188, 346730.531, 169709.609
	VejeteF.Alpha=1.0
	VejeteF.Scale=1.0
	Ank2F.Position=942974.437575, 347570.40625, 169642.280646
	Ank2F.Alpha=1.0
	luzimp=Bladex.GetEntity("LuzImpacto")
	luzimp.Intensity=0.0
	luzimp.SizeFactor=0.0
	genleng=Bladex.GetEntity("GeneradorLenguas")
	genleng.Scale=3.0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para chaos.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def PasoAnacardo1(a,b):
	x,y,z = Bladex.GetEntity("Ank2").Position
	_PasoAnacardo1.Play(x,y,z,0)

def PasoAnacardo2(a,b):
	x,y,z = Bladex.GetEntity("Ank2").Position
	_PasoAnacardo2.Play(x,y,z,0)

def SesgadoTeJodes(a,b):
	x,y,z = Bladex.GetEntity("Ank2").Position
	_SesgadoTeJodes.Play(x,y,z,0)

def EmpalaVejete(a,b):
	x,y,z = Bladex.GetEntity("Vejete").Position
	_EmpalaVejete.Play(x,y,z,0)

def SesgadoGore(a,b):
	x,y,z = Bladex.GetEntity("Vejete").Position
	_SesgadoGore.Play(x,y,z,0)

def FusionCool(a,b):
	x,y,z = Bladex.GetEntity("Vejete").Position
	_FusionCool.Play(x,y,z,0)

def Moulinex(a,b):
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("moulinex"))

def CreaAltar():
	global altar

	altar=Bladex.CreateEntity("Altar","Altar",940435.329945, 341861.349989, 169868.344306,"Physic")
	altar.Scale=1.000000
	altar.Solid=0
	altar.Orientation=0.500000,0.500000,0.500000,-0.500000
	Breakings.SetBreakable(altar.Name,12,100)

def SacaChumbos(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	Sacarracatelas()
	AnAhkard.Blind= 0
	AnAhkard.Deaf= 0
	Bladex.GetEntity("Ankurda").SubscribeToList("Pin")
	darfuncs.UnhideBadGuy(AnAhkard.Name)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Kaos"))


def CameronDiaz5(a,b):
	cam = Bladex.GetEntity("Camera")
	darfuncs.LaunchMaxCamera("Anakardo_Camera05.cam",668,968,SacaChumbos)
	#cam.AddCameraEvent(911-668,CreaOjosDemonio)
	Moulinex(0,0)

	Bladex.GetEntity("Vejete" ).SubscribeToList("Pin")
	Bladex.GetEntity("Ank2"   ).SubscribeToList("Pin")

	LocuraSangrienta(942570.5,341089.875 ,170158.094)

	Ank = Bladex.CreateEntity("Ankurda","DarkLord",942570.5,341089.875 ,170158.094,"Actor")
	Ank.Orientation = (0.70717227459, 0.70704126358, 1.63701133715e-005, 1.6357500499e-005)
	Ank.Animation="Ank_pincha_viejo"
	Ank.SendSectorMsgs=0
	Ank.TurnOn()

def CameronDiaz4(a,b):
	cam = Bladex.GetEntity("Camera")
	darfuncs.LaunchMaxCamera("Anakardo_Camera04.cam",456,667,CameronDiaz5)
	cam.AddCameraEvent(467-456,PasoAnacardo2)
	cam.AddCameraEvent(520-456,SesgadoTeJodes)
	cam.AddCameraEvent(530-456,EmpalaVejete)
	cam.AddCameraEvent(529-456,RompeAltarPiedra)
	cam.AddCameraEvent(610-456,SesgadoGore)
	cam.AddCameraEvent(620-456,SangreVeloz)
	cam.AddCameraEvent(624-456,FusionCool)

def CameronDiaz3(a,b):
	darfuncs.LaunchMaxCamera("Anakardo_Camera03.cam",250,455,CameronDiaz4)
	cam = Bladex.GetEntity("Camera")
	cam.AddCameraEvent(354-250,PasoAnacardo1)
	cam.AddCameraEvent(390-250,PasoAnacardo2)
	cam.AddCameraEvent(430-250,PasoAnacardo1)

def CameronDiaz2(a,b):
	darfuncs.LaunchMaxCamera("Anakardo_Camera02.cam",126,249,CameronDiaz3)

def CameronDiaz1(a,b):
	darfuncs.LaunchMaxCamera("Anakardo_Camera01.cam",0,125,CameronDiaz2)
	Bladex.GetEntity("VejeteW").SubscribeToList("Pin")
	char.Position = 925763.502791, 342900.813398, 170237.261377
	char.Angle=-3.1415/2
	char.SetOnFloor()

	Vejete = Bladex.CreateEntity("Vejete","Vejete",939567.5,340811.031, 170240.594,"Actor")
	Vejete.Orientation = (0.70717227459, 0.70704126358, 1.63701133715e-005, 1.6357500499e-005)
	Vejete.Animation="Vejete_pinchado"
	Vejete.SendSectorMsgs=0
	Vejete.TurnOn()

	Ank2 = Bladex.CreateEntity("Ank2","Ank2",949954.75,341003.75, 170152.688,"Actor")
	Ank2.Orientation = (0.70717227459, 0.70704126358, 1.63701133715e-005, 1.6357500499e-005)
	Ank2.Animation="Ank2_pincha_viejo"
	Ank2.SendSectorMsgs=0
	Ank2.TurnOn()


def CameronDiaz0():
	darfuncs.LaunchMaxCamera("Anakardo_Camera06.cam",0,325,CameronDiaz1)
	Bladex.ExeMusicEvent(-1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.05,MusicTool.LaunchMusicEvent,("viejeteblabla",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+7.5,GameText.WriteText,("M17T2",))


# execfile("Chaos.py")
def RompeAltarPiedra(a,b):
	print "Rompe Altar"
	Breakings.ExplodeSpecialObject(altar.Name,20000,(-50000,-50000,0))
	x = dust.DropDust(940435, 341000, 169868,0,-1000,0,500,"Tierrax",64,0.5)
	x.YGravity=1800.0
	x.RandomVelocity=100.0

def SangreVeloz(a,b):
	print "Chorrea Sangre"
	DropBlood(940346,339583,172591,0,0,2500)

def DropBlood(x,y,z,dx,dy,dz):
	blood=Bladex.CreateEntity("Sangrecita","Entity Particle System D1", x, y, z)
	blood.ParticleType="AnkBlood"
	blood.YGravity=5000
	blood.Friction=0.075
	blood.PPS=2000
	blood.Velocity=dx,dy,dz
	blood.RandomVelocity=45.0
	blood.RandomVelocity_V=10.0
	blood.Time2Live=32
	blood.DeathTime=Bladex.GetTime()+10.0/60.0

def OjoTimer(e_name, time):
	global OjoBrillo

	OjoBrillo[0].SizeFactor = OjoBrillo[0].SizeFactor + OjoBrillo[2]
	OjoBrillo[1].SizeFactor = OjoBrillo[1].SizeFactor + OjoBrillo[2]

	if OjoBrillo[0].SizeFactor > 0.5:
		OjoBrillo[2] = -0.025

	if OjoBrillo[0].SizeFactor < 0.0:
		OjoBrillo[0].SubscribeToList("Pin")
		OjoBrillo[1].SubscribeToList("Pin")
		OjoBrillo = [0,0,0.025]


def CreaOjosDemonio(a,b):
	global OjoBrillo
	print "Brillan!"

	OjoBrillo[0]=Bladex.CreateEntity("Ojera1","Entity Spot",942503,339585,170091)
	OjoBrillo[0].Color=255,0,0
	OjoBrillo[0].Intensity=0.00001
	OjoBrillo[0].Precission=1
	OjoBrillo[0].CastShadows=0
	#OjoBrillo[0].GlowTexture="OjoVejete"
	OjoBrillo[0].GlowTestZ=1
	OjoBrillo[0].AngVel=2
	OjoBrillo[0].SizeFactor=0


	OjoBrillo[1]=Bladex.CreateEntity("Ojera2","Entity Spot",942503,339585,170176)
	OjoBrillo[1].Color=255,0,0
	OjoBrillo[1].Intensity=0.00001
	OjoBrillo[1].Precission=1
	OjoBrillo[1].CastShadows=0
	#OjoBrillo[1].GlowTexture="OjoVejete"
	OjoBrillo[1].GlowTestZ=1
	OjoBrillo[1].AngVel=2
	OjoBrillo[1].SizeFactor=0

	OjoBrillo[1].SubscribeToList("Timer30")
	OjoBrillo[1].TimerFunc  = OjoTimer

	_BrilloOjos.Play(942503,339585,170176,0)

	_BrilloOjos.Play(942503,339585,170176,0)



def LocuraSangrienta(x,y,z):
	blood=Bladex.CreateEntity("Sangrecita","Entity Particle System D1", x, y, z)
	blood.ParticleType="AnkBlood"
	blood.YGravity=5000
	blood.Friction=0.075
	blood.PPS=400
	blood.Velocity=0,-10000,0
	blood.RandomVelocity=25.0
	blood.RandomVelocity_V=5.0
	blood.Time2Live=32
	blood.DeathTime=Bladex.GetTime()+10

def CreaViejoVerde():
	Vejete = Bladex.CreateEntity("VejeteW","Vejete",939567.5,340811.031, 170240.594,"Actor")
	Vejete.Orientation = (0.500055551529, 0.499942421913, 0.499964922667, -0.500037074089)
	Vejete.Animation="Vejete_rlx_no"
	Vejete.SendSectorMsgs=0
	Vejete.TurnOn()

def RelanzaEscenaDelFinal():
	darfuncs.HideBadGuy(AnAhkard.Name)
	CreaViejoVerde()
	CreaAltar()
	CameronDiaz0()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para collaps.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DisipaTemblor(ent_name, time):
	cam=Bladex.GetEntity("Camera")
	if cam.EarthQuakeFactor>8:
		cam.EarthQuakeFactor=cam.EarthQuakeFactor-8
	else:
		cam.RemoveFromList("Timer10")
		cam.TimerFunc=""
		cam.EarthQuake=0

def ContDerrumbe1():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe1.DoBreak((0.0, 0.0, 0.0), (273850, -3000, -19750), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(278000, -7000, -17250)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(272023,-4405,-26158,    2000, 2000, 512, "FastDust", 16, 0.5)

def Derrumbe1(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe1.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe1, ())


def ContDerrumbe1b():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe1b.DoBreak((0.0, 0.0, 0.0), (270000,-2000,-37000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(270000,-2000,-37000)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(282000,-5000,-17000,    2000, 2000, 512, "FastDust", 16, 0.5)

def Derrumbe1b(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe1b.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe1b, ())



def ContDerrumbe2():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe2.DoBreak((0.0, 0.0, 0.0), (323000,41000,-12000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(323468.934758, 38893.3738393, -10621.0416297)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(323001,41216,-11794,    3000, 3000, 512, "FastDust", 16, 1.5)

def Derrumbe2(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe2.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe2, ())

def ContDerrumbe3():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe3.DoBreak((0.0, 0.0, 0.0), (293000,44000,-2000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(296446.442949, 41881.9724648, -1914.3688647)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(294001,42580,-2755,    2000, 2000, 512, "FastDust", 16, 1.5)


def Derrumbe3(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe3.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, ContDerrumbe3, ())

def ContDerrumbe4():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe4.DoBreak((0.0, 0.0, 0.0), (280000,46000,24000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(283410.002083, 43292.8693136, 18973.8336377)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(281297,44722,23374,    2000, 2000, 512, "FastDust", 16, 1.5)


def Derrumbe4(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe4.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe4, ())

def ContDerrumbe5():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe5.DoBreak((0.0, 0.0, 0.0), (320000,41000,8000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(325743.040553, 38878.6999703, 7104.56499251)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(321874,40000,8007,    1000, 1000, 128, "FastDust", 16, 1.5)


def Derrumbe5(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe5.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe5, ())

def ContDerrumbe6():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe6.DoBreak((0.0, 0.0, 0.0), (285000,27000,-44000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(285196.530526, 24722.7706468, -39957.7174235)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(284728,27620,-44494,    2200, 2200, 512, "FastDust", 16, 0.5)


def Derrumbe6(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe6.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerrumbe6, ())

def ContDerrumbe7():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe7.DoBreak((0.0, 0.0, 0.0), (282000,45000,25750), (0.0, 0.0, 0.0))
	derrumbesuelopiedra2.Play(282000,45000,25750)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(286520,45829,32473,    2200, 2200, 256, "FastDust", 16, 0.5)


def Derrumbe7(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe7.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, ContDerrumbe7, ())

def ContDerrumbe8():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe8.DoBreak((0.0, 0.0, 0.0), (282500,45000,25750), (0.0, 0.0, 0.0))
	derrumbesuelopiedra3.Play(282500,45000,25750)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(289955,46220,28558,    2000, 4000, 256, "FastDust", 16, 0.5)


def Derrumbe8(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe8.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, ContDerrumbe8, ())

def ContDerrumbe9():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe9.DoBreak((0.0, 0.0, 0.0), (290000,48000,24000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra4.Play(283000,45000,25750)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(293095,46804,24819,    2000, 4000, 256, "FastDust", 16, 0.5)



def Derrumbe9(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe9.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+8.0, ContDerrumbe9, ())

def ContDerrumbe10():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe10.DoBreak((0.0, 0.0, 0.0), (300000,48000,25000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra5.Play(284000,45000,25750)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(299735,47210,26226,    2500, 2500, 256, "FastDust", 16, 0.5)


def Derrumbe10(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe10.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+9, ContDerrumbe10, ())

def ContDerrumbe11():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe11.DoBreak((0.0, 0.0, 0.0), (302000,51000,22000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra.Play(296000,47000,22000)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(301619,49804,21790,    1500, 1500, 256, "FastDust", 16, 0.5)



def Derrumbe11(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe11.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, ContDerrumbe11, ())

def ContDerrumbe12():
	cam=Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor=100
	cam.EarthQuake=1
	cam.TimerFunc=DisipaTemblor
	cam.SubscribeToList("Timer10")
	derrumbe12.DoBreak((0.0, 0.0, 0.0), (304000,50000,25000), (0.0, 0.0, 0.0))
	derrumbesuelopiedra2.Play(298000,47000,22000)
	dust.SetTierrapidaColor(75,75,75)
	dust.RemueveTierraGen(304371,48905,24857,    500, 1700, 256, "FastDust", 16, 0.5)



def Derrumbe12(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderrumbe12.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.5, ContDerrumbe12, ())


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
#*******************************   Definiciones para tropa.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abismoo():

	abismoii.OpenDoor()
	abismodd.OpenDoor()

def Bismoo():

	abismoii.CloseDoor()
	abismodd.CloseDoor()

def MuerteQeletum(ent_name):
	global NumQueletum

	esq         = Bladex.GetEntity(ent_name)
	esq.Data.ImDeadFuncAdd(ent_name)
	NumQueletum = NumQueletum - 1
	if(NumQueletum<=0):
		#Abismoo()
		darfuncs.EnterSecEvent(524964.535939, 86628.3252896, -2997.51552027,AparecenLosDosKabrones)


def CreaEsqueleto(n, x, y, z,Level):
	global NumQueletum

	hacha=Bladex.CreateEntity("HachaEsqOrkus"+`n`, "Cimitarra", 0, 0, 0,"Weapon")


	escudo=Bladex.CreateEntity("Escudely"+`n`, "Escudo7", 0, 0, 0,"Weapon")
	#Sparks.MakeShield(escudo.Name)


	esq=Bladex.CreateEntity("Keleto"+`n`, "Skeleton", x, y, z)
	esq.Person=1
	esq.Level=Level
	esq.Angle=-3.141569

	Actions.TakeObject(esq.Name, hacha.Name)
	Actions.TakeObject(esq.Name, escudo.Name)

	EnemyTypes.EnemyDefaultFuncs(esq)

	esq.GoToJogging = 1
	esq.Blind = 0
	esq.Deaf = 0
	NumQueletum = NumQueletum+1
	esq.Data.ImDeadFuncAdd = esq.ImDeadFunc
	esq.ImDeadFunc=MuerteQeletum
	darfuncs.HideBadGuy(esq.Name)

	return esq

def Cafinale(entity_name, camera_element):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def Cafin4(entity_name, camera_element, node):
	if node==1:
		cam = Bladex.GetEntity("Camera")
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		cam.SetPersonView("Player1")
		cam.Cut()

		#Bladex.ActivateInput()
		Scorer.SetVisible(1)

def Cafin3(entity_name, camera_element, node):
	if node==1:
		cam = Bladex.GetEntity("Camera")
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		darfuncs.ChangeCam(478522,83939,2769,481964,82334,12020, 5,Cafin4)

def Cafin2(entity_name, camera_element, node):
	if node==1:
		cam = Bladex.GetEntity("Camera")
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		darfuncs.ChangeCam(514629,84778,-16454,509812,83918,-7733, 5,Cafin3)

def Cafin1(entity_name, camera_element, node):
	if node==1:
		cam = Bladex.GetEntity("Camera")
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		darfuncs.ChangeCam(531199,82831,9831,525421,84009,1755, 5,Cafin2)


def SaleEskeletonazo(n):
	pers = Bladex.GetEntity("Keleto"+`n`)
	pers.Wuea=Reference.WUEA_ENDED
	pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
	pers.LaunchAnimation("Skl_jog_kaos0"+`n`)

def SaleEskeleto():
	SaleEskeletonazo(1)
	SaleEskeletonazo(2)
	SaleEskeletonazo(3)
	SaleEskeletonazo(4)

def TropelFurioso(sectorindex,entityname):
	global Pto1
	global Pto2
	global Pto3

	if entityname=='Player1':
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, Bismoo,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+15.0, Bismo,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+18.0,MusicTool.LaunchMusicEvent,("Atmosfera23",))

		if(1):
			cam = Bladex.GetEntity("Camera")
			cam.SetMaxCamera("Kaos_Camera_esqueletos.cam",0,-1)
			Bladex.GetEntity("Egipto3").SubscribeToList("Pin")
			cam.AddCameraEvent(-1,Cafinale)
		else:
			darfuncs.ChangeCam(511092,82311,-19074,516987,86085,-2869, 4,Cafin1)


		ScriptSkip.SkipScriptStart("CaosTropa")
		#Bladex.DeactivateInput()
		Scorer.SetVisible(0)

		darfuncs.UnhideBadGuy("Keleto1")
		darfuncs.UnhideBadGuy("Keleto2")
		darfuncs.UnhideBadGuy("Keleto3")
		darfuncs.UnhideBadGuy("Keleto4")

		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, SaleEskeleto,())
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("despelote"))
		TropaSector.OnEnter = ""

def AbrirSiMueren(e):
	global NCHKAS
	NCHKAS = NCHKAS-1
	ParticulateDeath(e)
	if NCHKAS<=0:
		Bladex.ExeMusicEvent(-1)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro5"))
		Abismoo()

def AparecenLosDosKabrones():
	darfuncs.LaunchMaxCamera("2ChkAppearCamera02.cam", 0,-1)
	OnOff.TurnOffLight("Egipto4")
	AparecechaosK(nchaosk1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, AparecechaosK,(nchaosk2,))

def AparecechaosK(chaosK):
	darfuncs.UnhideBadGuy(chaosK.Name)
	chaosK.Data.Appear()
	chaosK.Blind=0
	chaosK.Deaf=0
	chaosK.Alpha = 0.0
	ParticulateAppears(chaosK.Name)


def CamSet2(sectorindex,entityname):
	if entityname=='Player1':
		darfuncs.ChangePointOfView(421663, 60618,-10103,1)