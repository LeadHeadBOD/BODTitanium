##///
##||| Ice_M11/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Final crystal key animation 60fps (camera and key movement)
##||| * Medallion recesses now have proper light fade on insert (TO DO: Need new meshes there)
##||| * Fixed Minorx not having default deadfunc being executed
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
import AbreCam
import GotoMapVars
import InitDataField
import math
import ItemTypes
import darfuncs
import ScriptSkip
import MusicTool



######################################################################################################
#                                    elevador.py
######################################################################################################

########


## DEFINIMOS LA FUNCION QUE AUTOMATICAMENTE BAJARA EL ELEVADOR 3 SEGUNDOS DESPUES DE DETENERSE EN SU PUNTO MAS ALTO

############




def AbrePuertar1():
	puertar1.OpenDoor()

def CierraPuertar1():
	puertar1.CloseDoor()
	Bladex.DeactivateInput()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Bladex.ActivateInput,())



######################################################################################################
#                                    Positions.py
######################################################################################################


def IrPosicion1():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=5750, -2000, 110000

def IrPosicion2():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=49250, -2000, -12000		# Graneros

def IrPosicion3():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-8000, -2000, 21000	# Vidrieras

def IrPosicion4():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=35000, 6000, 18000		# Subterraneo1

def IrPosicion5():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=31000, 8000, -14000		# Tablillas

def IrPosicion6():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-62000, 22000, 85000

def IrPosicion7():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=19126.9056054, -9314.22041949, -8020.6790


######################################################################################################
#                                    inicio.py
######################################################################################################


def HitSnow():
	tierra1=Bladex.CreateEntity("SnowDust", "Entity Particle System D1", -62083, 23926, 87400)
	tierra1.ParticleType="SnowDust"
	tierra1.YGravity=100.0
	tierra1.Friction=0.15
	tierra1.PPS=200
	tierra1.Time2Live=64
	tierra1.Velocity=0,-1000,0
	tierra1.RandomVelocity=10.0
	tierra1.DeathTime=Bladex.GetTime()+0.05

	PlaySound(soundhitplayer,"Player1")


def SelectSoundEsfuerzo(kind):      ### PLAGUE: wtf is this shit
	global soundesfuerzo

	if (kind[0] != 'A'):
		soundesfuerzo=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-mediano.wav', 'SoundEsfuerzo')
	else:
		soundesfuerzo=Sounds.CreateEntitySound('../../Sounds/esfuerzo-corto-amz2.wav', 'SoundEsfuerzo')
		soundesfuerzo.Volume=1.0
		soundesfuerzo.MinDistance=10000
		soundesfuerzo.MaxDistance=20000


def PlaySound(sound,entity,ciclar = 0):
	ent = Bladex.GetEntity(entity)
	sound.Position = ent.Position
	sound.PlaySound(ciclar)
	print char.Position

def StopCameraInicio2(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()


def StopCameraInicio1(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.SetOnFloor()

	if char.Kind[0] == 'K':
	    cam.SetMaxCamera("hielo_inicio_Camera_caballero.cam",0,363)
	elif char.Kind[0] == 'B':
	    cam.SetMaxCamera("hielo_inicio_Camera_barbaro.cam",0,363)
	elif char.Kind[0] == 'D':
	    cam.SetMaxCamera("hielo_inicio_Camera_enano.cam",0,363)
	else:
	    cam.SetMaxCamera("hielo_inicio_Camera_amazonas.cam",0,363)

	char.LaunchAnmType("start_ice")



	if char.Kind[0] == 'K':
		char.Position = -61716, 17081, 90600 #Kgt
	elif char.Kind[0] == 'B':
		char.Position = -61716, 17081, 90600 #Bar
	elif char.Kind[0] == 'A':
		char.Position = -61716, 17331, 90600 # Amz
	elif char.Kind[0] == 'D':
		char.Position = -61716, 17231, 90600 #dwf


	cam.AddCameraEvent(-1,StopCameraInicio2)

	time = Bladex.GetTime()

	Bladex.AddScheduledFunc(time + 7.0,PlaySound,(soundesfuerzo,"Player1"))
	Bladex.AddScheduledFunc(time + 7.8,HitSnow,())


def IniciaJuego():
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("hielo_inicio_Camera_iglesia.cam",0,200)
	cam.AddCameraEvent(-1,StopCameraInicio1)
	char.Angle    = 3.1415
	char.Position = -61716, 17331, 90600

	GameText.WriteText("M11T1")
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("inicio"))
	ScriptSkip.SkipScriptStart("ielohini")

def Musicaytexto():

	char.Position = -61716, 17331, 90600
	char.SetOnFloor()
	AuxFuncs.FadeFrom(6,6)


	#print("load")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, IniciaJuego, ())
	Scorer.SetVisible(0)



######################################################################################################
#                                    Propiedades.py
######################################################################################################

def Apagala(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"

##############
def Apagala2(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"

def Apagala22(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"

def Apagala3(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingeAntorcha"


######################################################################################################
#                                    +.py
######################################################################################################

def PlaySoundMino(sound):
	if MinoEat == 1:
		sound.Position = Mino.Position
		sound.PlaySound(0)

def FinAnimWake(entity):
    ### PLAGUE: This is very bad. Do not ever overwrite funcs like this
	Mino.DamageFunc = Damage.CalculateDamage
	Mino.AnmEndedFunc = ""
	Actions.QuickTurnToFaceEntity ("MinoEat","Player1")
	#EnemyTypes.EnemyDefaultFuncs(Mino)

def DeletePedacitos():
	ComidaMinCabeza.SubscribeToList("Pin")
	ComidaMinLeftArm.SubscribeToList("Pin")
	ComidaMinRightArm.SubscribeToList("Pin")
	ComidaMinLeftLeg.SubscribeToList("Pin")
	ComidaMinRightLeg.SubscribeToList("Pin")
	ComidaMin.SubscribeToList("Pin")

def MinoAtakka():
	Mino.DamageFunc = Damage.CalculateDamage
	Bladex.GetEntity("MinoEatquad").SubscribeToList("Pin")

def LaunchWake(Timearma = 0.5):
	#Mino.Wuea = Reference.WUEA_NONE
	Mino.SetTmpAnmFlags(1,1,1,0,5,1)
	Bladex.AddScheduledFunc(Bladex.GetTime() + Timearma,SacarArma, ())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0     ,MinoAtakka,())
	Mino.LaunchAnimation("Min_standup")
	Mino.SetOnFloor()
	Mino.AnmEndedFunc = FinAnimWake

def SacarArma():
	inv = Mino.GetInventory()
	inv.LinkRightHand("MinGarropinEat")
	arma = Bladex.GetEntity("MinGarropinEat")


def FadeOutCarne(entity,timer):
	carne = Bladex.GetEntity(entity)
	carne.Alpha = carne.Alpha - CarneFadeDelta

	if carne.Alpha <= 0:
		carne.Alpha = 0

		carne.RemoveFromList("Timer15")

def FadeInCarne(entity,timer):
	carne = Bladex.GetEntity(entity)
	carne.Alpha = carne.Alpha + CarneFadeDelta

	if carne.Alpha >= 1.0:
		carne.Alpha = 1.0

		carne.RemoveFromList("Timer15")

def StartFadeOutCarne(MinoCarne):
	MinoCarne.SubscribeToList("Timer15")
	MinoCarne.TimerFunc = FadeOutCarne

def StartFadeInCarne(MinoCarne):
	global MinoEat

	if MinoEat == 1:
		MinoCarne.SubscribeToList("Timer15")
		MinoCarne.TimerFunc = FadeInCarne


def PourBlood(MinoCarne):
	if MinoEat == 1:
		blood=Bladex.CreateEntity("MinoBlood", "Entity Particle System D1",0,0,0)
		blood.ParticleType="Blood"
		blood.YGravity=10000.0
		blood.Friction=0.2
		blood.RandomVelocity=15.0
		blood.PPS=600
		blood.Time2Live=32
		blood.DeathTime=Bladex.GetTime() + LifeMinoBlood

		MinoCarne.Link(blood)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,StartFadeOutCarne,(MinoCarne,))
		PlaySoundMino(SndBocado)

def StartMinoFX():
	global MinoEat
	if MinoEat==1:
		time = Bladex.GetTime()

		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA1,PlaySoundMino,(SndDespedaza,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA2,PlaySoundMino,(SndDespedaza,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA3,PlaySoundMino,(SndDespedaza,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA4,PlaySoundMino,(SndDespedaza,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA5,PlaySoundMino,(SndDespedaza,))

		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA1,StartFadeInCarne,(MinoCarneRight,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA2,StartFadeInCarne,(MinoCarneLeft,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA3,StartFadeInCarne,(MinoCarneRight,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA4,StartFadeInCarne,(MinoCarneLeft,))
		Bladex.AddScheduledFunc(time + MINO_FDESPEDAZA5,StartFadeInCarne,(MinoCarneRight,))

		Bladex.AddScheduledFunc(time + MINO_FMORDISCO1,PourBlood,(MinoCarneRight,))
		Bladex.AddScheduledFunc(time + MINO_FMORDISCO2,PourBlood,(MinoCarneLeft,))
		Bladex.AddScheduledFunc(time + MINO_FMORDISCO3,PourBlood,(MinoCarneRight,))
		Bladex.AddScheduledFunc(time + MINO_FMORDISCO4,PourBlood,(MinoCarneLeft,))
		Bladex.AddScheduledFunc(time + MINO_FMORDISCO5,PourBlood,(MinoCarneRight,))

		Bladex.AddScheduledFunc(time + 14.375,StartMinoFX,())
	elif MinoEat == 0:
		inv = Mino.GetInventory()
		inv.LinkRightHand("None")
		inv.LinkLeftHand("None")

		#MinoCarneLeft.SubscribeToList("Pin")
		#MinoCarneRight.SubscribeToList("Pin")
		LaunchWake()
		Mino.Deaf = 0
		Mino.Blind = 0
		MinoEat = -1

def LaunchEat():
	Mino.Angle = 2.8
	Mino.Position = 78400,-1200,18000

	#inv = Mino.GetInventory()
	#inv.LinkRightHand("Carne")

	Mino.Wuea = Reference.WUEA_ENDED
	Mino.SetTmpAnmFlags(1,0,0,0,5,1,0) # cicla, no colisiona y no hace transicion
	#Mino.SetTmpAnmFlags(1,1,1,0,5,1)
	Mino.LaunchAnimation("Min_eat")
	Mino.SetOnFloor()
	#Mino.LinkToNode(arma,0)

	StartMinoFX()

def ActivateMinoEat(sector=0,entity="Player1"):
	global MinoEat
	if entity == "Player1":
		MinoEat = 0
		SecMinEat.OnEnter = ""

def ActivateMinoEat2(sector=0,entity="Player1"):
	global MinoEat
	if entity == "Player1":
		SecMinEat2.OnEnter = ""
		MinoEat = 1
		LaunchEat()



######################################################################################################
#                                    demonio.py
######################################################################################################

def SndRugidoFuerte(ent,Time):
	_SndRugidoFuerte.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndRugidoSuave(ent,Time):
	_SndRugidoSuave.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndGolPolvo(ent,Time):
	_SndGolPolvo.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndCristalonazo(ent,Time):
	_SndCristalonazo.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndCristalero(ent,Time):
	_SndCristalero.Play(char.Position[0], char.Position[1], char.Position[2], 0)

### STEP VARS FOR TIMER ###
# They are original values multiplied by 3 (original FPS = 20, new target = 60)
camRotStep = 0.02/3.0
cStep1 = 20 * 3
cStep2 = 66 * 3
cStep3 = 160 * 3
cStep4 = 185 * 3
cStep5 = cStep4 + 3
cStep6 = 230 * 3
cStep7 = 254 * 3

def MueveTimer(e_name, time):
  global Contador
  Contador = Contador+1

  darfuncs.GiraCamara(0.02/3.0)

  lg = Bladex.GetEntity("STAR")
  luzta = Bladex.GetEntity("LuzSTAR")
  if (Contador>=cStep1) and (Contador<=cStep2):
    lg.Move(0,1700/(cStep1-cStep2),0)
    lg.Rotate(0, 0, 1,0.06532/3.0)

  elif (Contador>=cStep3) and (Contador<=cStep4):

    iTick = (1.0-(Contador-cStep3)/(555.0-480.0))
    lg.Alpha                 =  iTick
    luzta.Intensity          =  10.0*iTick
    luzta.SizeFactor         =   2.0*iTick

  elif (Contador==cStep5):
    StarFlare                =Bladex.CreateEntity("aTablillaBrillos", "Entity Particle System D2", char.Position[0], char.Position[1], char.Position[2])
    StarFlare.D1             = lg.Position[0]-StarFlare.Position[0],lg.Position[1]-StarFlare.Position[1],lg.Position[2]-StarFlare.Position[2]
    StarFlare.ParticleType   = "Estrellitas"
    StarFlare.YGravity       = 1000
    StarFlare.Friction       = 0.3
    StarFlare.PPS            = 112
    StarFlare.Velocity       = 0, 0.0, 0.0
    StarFlare.Time2Live      = 64
    StarFlare.DeathTime      = Bladex.GetTime()+1.5
    StarFlare.RandomVelocity = 20
  elif (Contador==cStep6):
    StarFlare=Bladex.CreateEntity("aTablillaBrillos", "Entity Particle System D1", char.Position[0], char.Position[1], char.Position[2])
    StarFlare.ParticleType   = "Estrellitas"
    StarFlare.YGravity       = 1000
    StarFlare.Friction       = 0.3
    StarFlare.PPS            = 112
    StarFlare.Velocity       = 0, 0.0, 0.0
    StarFlare.Time2Live      = 64
    StarFlare.DeathTime      = Bladex.GetTime()+2.0
    StarFlare.RandomVelocity = 50
  elif (Contador>=cStep7):
    lg.RemoveFromList("LlaveTimer")
    lg.TimerFunc          = ""
    luzta.SubscribeToList("Pin")
    Actions.TakeObject("Player1",lg.Name)

    cam = Bladex.GetEntity("Camera")
    cam.SetPersonView("Player1")
    cam.PViewType = Bladex.GetEntity("Player1").Data.lastCam        # Added -LeadHead


def musicayte():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("nubesllave"))
	GameText.WriteText("M11T3")


def IniciaCoger():
  global Contador

  darfuncs.InitGiroCamera()
  char.SetTmpAnmFlags(1,1,1,0,5,1)
  char.LaunchAnmType("tke_key")
  Scorer.SetVisible(0)
  #Bladex.AddScheduledFunc(Bladex.GetTime()+(256.0/20.0),Bladex.ActivateInput,())
  Contador = 0
  lg = Bladex.GetEntity("STAR")
  lg.TimerFunc     = MueveTimer
  lg.SubscribeToList("LlaveTimer")
  AuxFuncs.FadeTo(21.0, 50.0)



  GameText.WriteText("M11T3")
  Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("demonio",))
  Bladex.AddScheduledFunc(Bladex.GetTime()+25.0,GotoMapVars.EndOfLevel,())
  musicayte()


def PickUpLaLlave():
  Bladex.DeactivateInput()
  Actions.FreeBothHands("Player1")
  cam = Bladex.GetEntity("Camera")
  Bladex.GetEntity("Player1").Data.lastCam = cam.PViewType      # Add -LeadHead
  cam.PViewType = 0
  Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,IniciaCoger,())


def RotaTimer(e_name, time):
   global Contador

   lg = Bladex.GetEntity("STAR")
   lg.Rotate(0, 0, 1,0.06532/3.0)

   lg.Move(0,(0.5*(5-(Contador%11)))/3.0,0)
   Contador=Contador+1

   if Contador > 225 :
          lg.Impulse( 0, -2000, 0 )
          Bladex.ActivateInput()
          lg.RemoveFromList("LlaveTimer")
          lg.TimerFunc     = ""
          OnInitTake.AddOnInitTakeEvent("STAR", PickUpLaLlave)




def ApareceLlave(x,y,z):
   lg=Bladex.CreateEntity("STAR","LlaveBlanca",x,y,z)
   lg.Static        = 0
   lg.Scale         = 1
   lg.Orientation   = 0.7, -0.7, 0, 0
   lg.TimerFunc     = RotaTimer
   lg.SubscribeToList("LlaveTimer")
   darfuncs.SetHint(lg,"Opal Key")

   luzta=Bladex.CreateEntity("LuzSTAR","Entity Spot",x,y,z)
   luzta.Color=ColorLuz
   luzta.Intensity=10
   luzta.Precission=0.1
   luzta.CastShadows=0
   luzta.Visible=1
   luzta.Flick=0
   luzta.SizeFactor = 2
   luzta.AngVel=0.1
   luzta.GlowTexture="StarParticle"
   lg.Link(luzta)


   lemntira.RemoveFromWorld()
   #lg.Impulse( 0, -40000, 0 )



def HellSpawDeath(ent_name):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(32,))
	demonio=Bladex.GetEntity(ent_name)
	x=demonio.Position[0]
	y=demonio.Position[1]
	z=demonio.Position[2]
	Bladex.AddScheduledFunc(Bladex.GetTime()+demonio.Data.ImplosionPeriod+demonio.Data.DeathBallPeriod, ApareceLlave, (x,y,z))
	demonio.Data.ImDeadFunc (ent_name)
	Bladex.DeactivateInput()


def BreakItBaby(Camera,frame):
   Cristalera(18991.8003327, -19262.599598, -19991.1737018)
   se1.DoBreak( (0,0,-5), (17680,-19000,-19480), (0,0,-150) )
   se2.DoBreak( (0,0,-5), (19545,-19000,-19480), (0,0,-150) )
   SndCristalonazo(Camera,frame)


def Cristalera(x,y,z):
	tierra1=Bladex.CreateEntity("Cristales", "Entity Particle System D1", x, y, z)
	tierra1.ParticleType="Brillitos"
	tierra1.PPS=128
	tierra1.YGravity=9800.0
	tierra1.Friction=0.1
	tierra1.Velocity=0.0, 0.0, -2000.0
	tierra1.RandomVelocity=100.0
	tierra1.Time2Live=64
	tierra1.DeathTime=Bladex.GetTime()+1.0

def RemueveTierraGen(x,y,z   ,sx,sz):

	tierra1=Bladex.CreateEntity("TierraRemoviendose1", "Entity Particle System D3", x +sx, y, z + sz)
	tierra1.D1= -2*sx, 0, 0
	tierra1.D2= -2*sx, 0, - 2*sz
	tierra1.ParticleType="Tierrax"
	tierra1.PPS=64
	tierra1.YGravity=200.0
	tierra1.Friction=0.1
	tierra1.Velocity=0.0, -400.0, 0.0
	tierra1.RandomVelocity=15.0
	tierra1.Time2Live=64
	tierra1.DeathTime=Bladex.GetTime()+2.0


	tierra2=Bladex.CreateEntity("TierraRemoviendose2", "Entity Particle System D3", x + sx, y, z + sz)
	tierra2.D1= -2*sx, 0, - 2*sz
	tierra2.D2=     0, 0, - 2*sz
	tierra2.ParticleType="Tierrax"
	tierra2.PPS=64
	tierra2.YGravity=200.0
	tierra2.Friction=0.1
	tierra2.Velocity=0.0, -400.0, 0.0
	tierra2.RandomVelocity=15.0
	tierra2.Time2Live=64
	tierra2.DeathTime=Bladex.GetTime()+2.0


def EvCameraHit2(Camera,frame):
   RemueveTierraGen(19482, -8272, -26093,1300,1300)
   demonio.ImDeadFunc = HellSpawDeath

def EvCameraHit1(Camera,frame):
   RemueveTierraGen(18637, -17300, -20134,600,600)


def StopCameraWin4(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
 	demonio.Blind=0
 	demonio.Deaf=0
	#Bladex.ActivateInput()
	ScriptSkip.SkipScriptEnd()
	Scorer.SetVisible(1)


def StopCameraWin3(Camera,frame):
  cam = Bladex.GetEntity("Camera")
  cam.SetMaxCamera("Hielo_Camera_demonio_aterriza.cam",263,387)
  Bladex.SetListenerPosition(1)
  cam.AddCameraEvent(283-263,EvCameraHit2)
  cam.AddCameraEvent(285-263,SndGolPolvo)
  cam.AddCameraEvent(346-263,SndRugidoSuave)
  cam.AddCameraEvent(-1,StopCameraWin4)
  Cristalera(18637, -17300, -20134)
  SndCristalero(Camera,frame)


def StopCameraWin2(Camera,frame):
  cam = Bladex.GetEntity("Camera")
  cam.SetMaxCamera("Hielo_Camera_rompe_ventana.cam",120,262)
  Bladex.SetListenerPosition(1)
  cam.AddCameraEvent(150-120,EvCameraHit1)
  cam.AddCameraEvent(155-120,SndGolPolvo)
  cam.AddCameraEvent(143-120,BreakItBaby)
  cam.AddCameraEvent(179-120,SndRugidoFuerte)
  cam.AddCameraEvent(-1,StopCameraWin3)

  demonio.UnFreeze()
  demonio.PutToWorld()

  demonio.Blind=1
  demonio.Deaf=1
  char.SetTmpAnmFlags(1,1,1,0,5,1)
  demonio.Position = 18712,-18352+150,-17020
  demonio.Angle    = 3.1415

  char.Angle       = 0

  demonio.Wuea=Reference.WUEA_ENDED
  demonio.SetTmpAnmFlags(1,1,1,0,5,1)
  demonio.LaunchAnmType("Ldm_window")



def StopCameraWin1(Camera,frame):
  cam = Bladex.GetEntity("Camera")
  cam.SetMaxCamera("Hielo_Camera_enfoque vidriera.cam",56,135)
  Bladex.SetListenerPosition(1)
  cam.AddCameraEvent(-1,StopCameraWin2)



def IniciaEscenaDemoinio(x):
  cam = Bladex.GetEntity("Camera")
  cam.SetMaxCamera("hielo_Camera_aparicion_heroe.cam",0,55)
  Bladex.ExeMusicEvent(-1)
  Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("demonice",))
  #Bladex.ExeMusicEvent(Bladex.GetMusicEvent("demonice"))
  Bladex.SetListenerPosition(1)

  cam.AddCameraEvent(-1,StopCameraWin1)

  char.Angle    = 3.1415

  if char.Kind[0] == "D":
  	char.Position = 18400, -8862, -35528
  else:
  	char.Position = 18636, -8862, -35528

  se1.Active=0
  se2.Active=0
  char.SetTmpAnmFlags(1,1,1,0,5,1)
  char.LaunchAnmType("window")


def CaminaHastaInicioD(sectorindex,entityname):
  if entityname == "Player1":
    ScriptSkip.SkipScriptStart("ielodemonio")
    char = Bladex.GetEntity("Player1")
    char.GoTo(18636, -8862, -35528)
    Scorer.SetVisible(0)
    #Bladex.DeactivateInput()
    char.RouteEndedFunc = IniciaEscenaDemoinio
    DemonioSector.OnEnter = ""



######################################################################################################
#                                    Blades.py
######################################################################################################

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
	global blades_ready
	global b1_time

	itime=time-b1_time
	blade=Bladex.GetEntity(blade_name)
	if(itime<3.0):
		blade.SetPosition(13621+11000 - (3666.6*itime),8639,35991,0)
	blade.Rotate(0.0,1.0,0.0,-0.1,1)
	if(itime>3.0):
		StopBlade(blade)
		blades_ready = 1


def Blade2RTimerFunc(blade_name,time):
	global b2_time
	global blades_ready
	itime=time-b2_time
	blade=Bladex.GetEntity(blade_name)
	if(itime<3.0):
		blade.SetPosition(13528+11000-(3666.6*itime),9148,44894,0)
	blade.Rotate(0.0,1.0,0.0,0.1,1)
	if(itime>3.0):
		StopBlade(blade)
		Sonido_TrampaCuchilla_Reactivada.Play(13528,9148,44894,0)
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
	Sonido_Cuchilla1_Activada.Play(13621.695372,8639.536583,35991.447347,0)
	b1_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade1")
	blade.Position=13621.695372,8639.536583,35991.447347
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
	chispas1.Velocity=-4000.0, 0.0, 4000.0
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

		blade.SetPosition(13621+(16000.0-5000.0*itime)*itime,8639,35991+(8000.0-8000*itime)*itime,0)


		if (itime<0.6):
			chispas1=Bladex.GetEntity("Chispas1")
			chispas1.Position=blade.Position[0]+1500, blade.Position[1], blade.Position[2]
			luzchispa1=Bladex.GetEntity("LuzChispa1")
			luzchispa1.Position=blade.Position[0]-200, blade.Position[1], blade.Position[2]+1500
	blade.Rotate(0.0,1.0,0.0,0.6-0.3*itime,1)
	if(itime>2.0):
		StopBlade(blade)
		#RBlades()
		RBlade1()

def LaunchBlade2():
	global b2_time
	Sonido_Cuchilla2_Activada.Play(13528,9148,44894,0)
	b2_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade2")
	blade.Position=13528,9148,44894
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
	chispas2.Velocity=-4000.0, 0.0, -4000.0
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
		blade.SetPosition(13528+(16000.0-5000.0*itime)*itime,9148,44894-(8000.0-8000*itime)*itime,0)

		if (itime<0.6):
			chispas2=Bladex.GetEntity("Chispas2")
			chispas2.Position=blade.Position[0] + 1500, blade.Position[1], blade.Position[2]
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
	blades_ready=0

def RBlades():
	global blades_ready
	blades_ready=1

def ActivateBlades(SectorIndex,EntyName):
	if(blades_ready):
		Sonido_TrampaCuchilla_Activada.Play(13528,9148,44894,0)
		LaunchBlades()
		Bladex.GetSector(18750,6000,40500).OnEnter = ""


######################################################################################################
#                                    puertice.py
######################################################################################################
def CierraPuertaGran(sectorindex,entityname):
	if entityname=="Player1":
		Bladex.GetSector(sectorindex).OnEnter = ""
		puertagran.CloseDoor()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera1"))


def AbrePuertaLlave11():
	puert111.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera5"))

def AbrePuertaLlaveen():
	puertaen.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera12"))

def CierraPuertaLlaveen(sectorindex,entityname):
	if entityname=='Player1':
		puertaen.CloseDoor()
		sen.OnEnter=""



######RASTRILLO DEL CEMENTERIO
def Abrepuerta11(parametro):

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto puerta1
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta11din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente23",None)
	MusicTool.Music2Sector("ambiente24",None)
	MusicTool.Music2Sector("ambiente25",None)



def CierraPuertaELE():

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


def AbrePuertaELE():

	desplazamientos=(500.0, 6500.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	columnaelevador.OpenDoor()

########
def ElevadorArriba():

	global enmarcha
	enmarcha=0
########


## DEFINIMOS LA FUNCION QUE AUTOMATICAMENTE BAJARA EL ELEVADOR 3 SEGUNDOS DESPUES DE DETENERSE EN SU PUNTO MAS ALTO

def EsperaYBajaElevador():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, AbrePuertaELE, ())


def AbrePuerta8():
	puerta8.OpenDoor()
	MusicTool.Music2Sector("ambiente3",None)


def SndRujido():
	_SndRugido.Position = char.Position[0], char.Position[1], char.Position[2]
	_SndRugido.PlaySound(1)


def AbrePuertaLlave0():
	puerta0.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-3"))

def CierraPuertaLlave0():
	puerta0.CloseDoor()


def AbrePuertaLlav11():
	puert11.OpenDoor()
	MusicTool.Music2Sector("ambiente2","Atmosfera5")


def CierraPuertaLlav11():
	puert11.CloseDoor()

def AbrePuertaLlavevid():
	puertavid.OpenDoor()
	MusicTool.Music2Sector("ambiente18","emptyloquesea")

def CierraPuertaLlavevid():
	puertavid.CloseDoor()

def Abrerast6():

	desplazamientos=(1550.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast6din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrarast6():

	desplazamientos=(1550.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rast6din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbrePuertaGran():
	puertagran.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente1",None)
	MusicTool.Music2Sector("ambiente3",None)
	MusicTool.Music2Sector("ambiente5",None)
	MusicTool.Music2Sector("ambiente6",None)
	MusicTool.Music2Sector("ambiente7",None)
	MusicTool.Music2Sector("ambiente8",None)
	MusicTool.Music2Sector("ambiente9",None)
	MusicTool.Music2Sector("ambiente11",None)
	MusicTool.Music2Sector("ambiente12",None)
	MusicTool.Music2Sector("ambiente13",None)
	MusicTool.Music2Sector("ambiente15",None)


def AbrePuertaLlavetoro2():
	puertatoro2.OpenDoor()

def CierraPuertaLlavetoro2():
	puertatoro2.CloseDoor()

def Abrep1():
	puerta1a.OpenDoor()
	MusicTool.Music2Sector("ambiente19",None)
	MusicTool.Music2Sector("ambiente20",None)

def EndMinorx(entity):
	pos = char.Position
	Minorx.GoToJogging=1
	#Minorx.RouteEndedFunc = EndRoute
	Minorx.GoTo(pos[0],pos[1],pos[2])

	Minorx.Angle = 1.8
	Minorx.Deaf  = 0
	Minorx.Blind = 0
	dist = B3DLib.GetXZDistance ("Player1", "Minorx")
	if 2000>dist:
		char.Position = Minorx.Position[0]-2000, char.Position[1], char.Position[2]




def CierraPuertaMino(sectorindex,entityname):
	if entityname=='Player1':
		puertamino.CloseDoor()
#		puertagran.OpenDoor()
		s22.OnEnter=""
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3"))

		Minorx.Position = 86727, -874, 2561
		#Minorx.Angle = 2.8
		Minorx.Angle = 3.14
		Minorx.Deaf  = 1
		Minorx.Blind = 1

		Minorx.Wuea=Reference.WUEA_ENDED
		Minorx.SetTmpAnmFlags(1,1,1,0,5,1,0)
		Minorx.LaunchAnimation("Min_escena_hielo")
		Minorx.SetOnFloor()
		Quilombazo()
		Minorx.AnmEndedFunc = EndMinorx

		Bladex.SetListenerPosition(1)
		SndRujido()

def DieFukingMinorx(ent_name):
	Minorx = Bladex.GetEntity("Minorx") # Add
	Minorx.Data.OldDeadFunc(ent_name)   #   -LeadHead
	puertamino.OpenDoor()
	PoneArmas(ktrai1)
	PoneArmas(ktrai2)


def PoneArmas(pers):
	o=Bladex.CreateEntity("IcePada"+pers.Name,"Espadaelfica",0,0,0,"Weapon")
	ItemTypes.ItemDefaultFuncs(o)
	Actions.TakeObject(pers.Name,"IcePada"+pers.Name)
	o=Bladex.CreateEntity("IceCudo"+pers.Name,"Escudo1",0,0,0,"Weapon")
	ItemTypes.ItemDefaultFuncs(o)
	Actions.TakeObject(pers.Name,"IceCudo"+pers.Name)
	pers.UnFreeze()
	pers.PutToWorld()

def CreaTraidor(x,y,z,a,name):

	pers=Bladex.CreateEntity(name,"Knight_Traitor",x,y,z,"Person")
	pers.Angle=a
	pers.Level=15
	pers.ActionAreaMin=pow(2,8)
	pers.ActionAreaMax=pow(2,9)
	pers.SetOnFloor()
	EnemyTypes.EnemyDefaultFuncs(pers)
	pers.Freeze()
	pers.RemoveFromWorld()

	return pers


def CreateBarril():
	global Barrilazos
	Barrilazos[0]=Bladex.CreateEntity("camin1","Cajon2",84604.562093,-908.756320-4,944.306585)
	Barrilazos[0].Static=1
	Barrilazos[0].Scale=1.445076
	Barrilazos[0].Orientation=0.687250,0.705881,0.110856,-0.130882
	Breakings.SetBreakable(Barrilazos[0].Name,12,100)

	Barrilazos[1]=Bladex.CreateEntity("Minbar1","Barril",83920.001693,-2293.729324-9,1296.073096)
	Barrilazos[1].Static=0
	Barrilazos[1].Scale=1.549318
	Barrilazos[1].Orientation=0.684589,0.703925,0.122602,-0.144209
	Breakings.SetBreakable(Barrilazos[1].Name,12,100)

	Barrilazos[2]=Bladex.CreateEntity("Minbar2","Barril",85160.786691,-2364.942955-9,954.713235)
	Barrilazos[2].Static=0
	Barrilazos[2].Scale=1.644632
	Barrilazos[2].Orientation=0.688925,0.706917,0.101763,-0.123676
	Breakings.SetBreakable(Barrilazos[2].Name,12,100)
def Quilombazo():
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,Barrilada,())
	Barrilazos[2].Impulse(      0, -500000, -500000)
	Barrilazos[1].Impulse(-100000, -500000, -400000)
	Barrilazos[0].Impulse(-500000, -100000, -100000)
	Breakings.ExplodeSpecialObject (Barrilazos[0].Name, 3500.0)

def Barrilada():
	Breakings.ExplodeSpecialObject (Barrilazos[2].Name, 3500.0)
	Breakings.ExplodeSpecialObject (Barrilazos[1].Name, 3500.0)

def CierraPuertaLlave3(sectorindex,entityname):
	puerta3.CloseDoor()     ### PLAGUE: Super secret room 

def puertablade_closed(sld_name):
	Doors.EndCloseFunc(sld_name)
	puertablade.OpenDoor()

def MuereLlamarada():
	if puertablade.status==Doors.OPENED:
		sld_area= Bladex.GetEntity(puertablade.Name)
		sld_area.OnStopFunc= puertablade_closed
	else:
		puertablade.OpenDoor()
	OnOff.TurnOnLight("lamparaenciende")
	darfuncs.UnhideBadGuy("CR1SKL")
	darfuncs.UnhideBadGuy("CR2SKL")
	darfuncs.UnhideBadGuy("CR4SKL")

def BorraLuz():
	pers = Bladex.GetEntity("FLAMEsq")
	pers.GoToJogging = 1
	pers.Angle       = 1.7383420854
	pers.SetOnFloor()
	darfuncs.EnciendeEnLlamas(pers)
	darfuncs.UnhideBadGuy("FLAMEsq")

	egrupox = darfuncs.E_Grup()
	egrupox.AddGuy("FLAMEsq")
	egrupox.OnDeath = MuereLlamarada

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,pers.GoTo,(-1650.8895162, 10178.9562668, 31351.9058664))
	puertablade.CloseDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente30","Combate4")
	MusicTool.Music2Sector("ambiente29",None)



######################################################################################################
#                                    enemigos.py
######################################################################################################

def fastGoTo(entName,x,y,z):
	p =Bladex.GetEntity(entName)
	p.GoToJogging = 1
	p.GoTo(x,y,z)

def Suenamusica():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	MusicTool.Music2Sector("ambiente1",None)
	MusicTool.Music2Sector("ambiente7",None)

def Suenamusica2():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera5"))
	MusicTool.Music2Sector("ambiente1",None)
	MusicTool.Music2Sector("ambiente7",None)

def Suenamusica3():

	fastGoTo("23kngt",-19641.9064864, -725.624487032, -12086.3719182)

def Suenamusica4():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera1"))
	MusicTool.Music2Sector("ambiente16",None)

def Suenamusica5():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera1"))
	MusicTool.Music2Sector("ambiente30",None)


def TerminanLasMuertes1():
	sectx1=Bladex.GetSector(34869.6116357, -1417.68083049, 84066.4439684)
	sectx1.OnEnter=x1
	sectx1=Bladex.GetSector(42315.1058392, -1443.68574847, 84728.8746403)
	sectx1.OnEnter=x1
	sectx1=Bladex.GetSector(49400.369177, -1363.57821177, 84136.8562877)
	sectx1.OnEnter=x1

def KreaKaballeros1():
	darfuncs.UnhideBadGuy("IceArq4")
	darfuncs.UnhideBadGuy("9kngt")

def x1(sectorindex,entityname):
	if entityname=='Player1':
		KreaKaballeros1()
		sectx1=Bladex.GetSector(34869.6116357, -1417.68083049, 84066.4439684)
		sectx1.OnEnter=""
		sectx1=Bladex.GetSector(42315.1058392, -1443.68574847, 84728.8746403)
		sectx1.OnEnter=""
		sectx1=Bladex.GetSector(49400.369177, -1363.57821177, 84136.8562877)
		sectx1.OnEnter=""

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def x2(sectorindex,entityname):

	if entityname=='Player1':
		GoToMul("12kngt")
		sectx2.OnEnter=""

def GoToMul2(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul2

def x3(sectorindex,entityname):

	if entityname=='Player1':
		GoToMul("20kngt")
		sectx3.OnEnter=""

def GoToMul4(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul4

def x5(sectorindex,entityname):

	if entityname=='Player1':
		GoToMul4("25kngt")
		sectx5.OnEnter=""

def AparecedYa():
	darfuncs.UnhideBadGuy("24kngt")
	darfuncs.UnhideBadGuy("25kngt")

def x7(sectorindex,entityname):

	if entityname=='Player1':
		AparecedYa()
		sectx7.OnEnter=""

def ApareceYa():
	darfuncs.UnhideBadGuy("IceArq3")

def x6(sectorindex,entityname):

	if entityname=='Player1':
		ApareceYa()
		sectx6.OnEnter=""

def aparecedkeletos():

	darfuncs.UnhideBadGuy("1Esq")
	darfuncs.UnhideBadGuy("2Esq")

darfuncs.EnterSecEvent(45183.9458111, -2554.47058924, 28744.4582367,aparecedkeletos)


######################################################################################################
#                                    tablitrap.py
######################################################################################################

def DropArrow(Nflecha):
       ###  9912.665209  ###

       o=Bladex.CreateEntity(Bladex.GenerateEntityName(), "Flecha", 22200, char.Position[1], 5176+999*Nflecha,"Arrow")
       o.Scale=0.7
       o.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
       o.MessageEvent(Reference.MESSAGE_START_TRAIL, 0,0)

       o.Orientation=0.50005787611, 0.50005787611, 0.499942094088, 0.499942094088
       o.Gravity = 0,0,0
       o.Fly(-10000,-3000,0)
       return o

def DelArrows():
      for i in range(5):
         if nArrows[i] != "":
            if not nArrows[i].Parent:
               nArrows[i].SubscribeToList("Pin")
            nArrows[i] = ""


def DropALotOffArrows(triggername,entityname):
  if entityname == "Player1":
    if nails.TrapList[TrampaId].Active:
      DeactivateLocoTrap()
      flechazo.Position = char.Position
      flechazo.PlaySound(0)
      for i in range(5):
         nArrows[i]=DropArrow(i)
      Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, DelArrows,())


def DeactivateLocoTrap():
  Puerta_Mala.CloseDoor()
  Button.Turn("Piedra Loca")
  nails.TrapList[TrampaId].Active   = 0

def ActivateLocoTrap():
  Puerta_Mala.OpenDoor()
  nails.TrapList[TrampaId].Active   = 1

def tablix():
  print "Presionado!"
  if nails.TrapList[TrampaId].Active:
     DeactivateLocoTrap()
  else:
     ActivateLocoTrap()

def ComienzaAnimacionTablilla(sectorindex,entityname):
  global playertab
  if entityname =="Player1":
    ScriptSkip.SkipScriptStart("ielotablilla")
    #Bladex.DeactivateInput()
    Scorer.SetVisible(0)
    char = Bladex.GetEntity("Player1")
    char.QuickFace(0)
    Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, caminaalatablilla,())

def caminaalatablilla():
    char.GoTo(18681, 10021, 19230)
    char.RouteEndedFunc=llegoALaTablilla

def llegoALaTablilla(este):
    char.Position = (19026, 9980, 19747)
    EscenaTablilla("Player1")

    TabillaSector.OnEnter = ""
    EscenaTablilla("Player1")

def EscenaTablilla(Entity):
  Actions.FreeBothHands("Player1",IniciaEscenaTablilla,())

def IniciaEscenaTablilla():
	global playertab
	cam  = Bladex.GetEntity("Camera")
	char = Bladex.GetEntity("Player1")

	char.Angle = 3.1515
	char.Position = 19026, 9980, 19747
	char.Wuea=Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("tablilla_hielo")
	char.Position = 19026, 9980, 19747
	char.SetOnFloor()
	GameText.WriteText("M11T2")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("tablilla"))
	cam.SetMaxCamera("tablilla_hielo_Camera01.cam",0,380)
	cam.AddCameraEvent(-1,StopCameraTablilla)
	cam.AddCameraEvent(32,CogeLaTablilla)
	cam.AddCameraEvent( 65,tTablillaDust)
	cam.AddCameraEvent( 75,tTablillaDust)
	cam.AddCameraEvent(310,DesapareceTablilla)

	nails.TrapList[TrampaId].Active   = 0
	###################################################
	# Tablilla para Knight_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'K':
		o             = Bladex.GetEntity('Tablilla5')
		o.Position    =  (19022.6495554, 10106.9310005, 20343.1570952)
		o.Orientation =  (0.875617146492, 0.477774947882, -0.0312444325536, 0.0636360198259)

	###################################################
	# Tablilla para Amazon_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'A':
		o             = Bladex.GetEntity('Tablilla5')
		o.Position    =  (19022.5729343, 10131.2046508, 20411.3996149)
		o.Orientation =  (0.856372892857, 0.516007065773, 0.00814486667514, 0.0172002408653)

	###################################################
	# Tablilla para Barbarian_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'B':
		o             = Bladex.GetEntity('Tablilla5')
		o.Position    =  (19014.2142209, 9948.07326472, 20477.5232372)
		o.Orientation =  (0.866895794868, 0.496720522642, -0.0393528416753, -0.0145522104576)

	###################################################
	# Tablilla para Dwarf_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'D':
		o             = Bladex.GetEntity('Tablilla5')
		o.Position    =  (19215.7161011, 10447.9158856, 20529.1559189)
		o.Orientation =  (0.8537722826, 0.517664015293, 0.0478925295174, -0.0283396113664)

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
  cam  = Bladex.GetEntity("Camera")
  char = Bladex.GetEntity("Player1")
  cam.SetPersonView("Player1")
  ScriptSkip.SkipScriptEnd()
  #Bladex.ActivateInput()
  Scorer.SetVisible(1)
  Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera8"))

def DesapareceTablilla(Camera,frame):
  global PosX
  global PosY
  global PosZ
  global Tick
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.RemoveObject("Tablilla5")

  char.RemoveFromInventLeft()
  CreateEstrellitas()
  PosX  = tab.Position[0]
  PosY  = tab.Position[1]
  PosZ  = tab.Position[2]
  Tick  = 0
  Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CoolStart, ())
  tab.Position = PosX,  PosY, PosZ

  luztabl=Bladex.CreateEntity("Luztabl","Entity Spot",18573.6656701, 5885.64974047, 20270.579)
  luztabl.Color=255,155,55
  luztabl.Intensity=10.0
  luztabl.CastShadows=0
  luztabl.Visible=0
  luztabl.Flick=0

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


def CogeLaTablilla(Camera,frame):
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.AddTablet("Tablilla5")
  inv.LinkLeftHand("Tablilla5")
  # Bladex.AddScheduledFunc(Bladex.GetTime(), ImprimeDatosTablilla,("Tablilla5",))





######################################################################################################
#                                    Sonidospuntuales.py
######################################################################################################
def CriptaNoSuenaLaPutaAlanisMorrisete(sectorindex,entityname):
	global criptSoundActive
	global cuervo1
	global cuervo3
	global cuervo4
	global PRIM7

	if (criptSoundActive == 1) and (entityname == "Player1"):
		criptSoundActive = 0
		cuervo1.StopPeriodic()
		cuervo3.StopPeriodic()
		cuervo4.StopPeriodic()
		PRIM7.Stop()
		criptSoundActive = 0

def CriptaSuena(sectorindex,entityname):
	global criptSoundActive
	global cuervo1
	global PRIM7
	global cuervo3
	global cuervo4

	if (criptSoundActive == 0) and (entityname == "Player1"):
		criptSoundActive = 1

		cuervo1.PlayPeriodic()
		PRIM7.Play(32500,4500,35000,-1)
		cuervo3.PlayPeriodic()
		cuervo4.PlayPeriodic()

######################################################################################################
#                                    jema.py
######################################################################################################

def DetieneMusica():

	MusicTool.Music2Sector("ambiente22",None)




def CreatePartilcesMedallon():
	Bladex.AddParticleGType("EnergyMedallon1","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>10:
			traux=(60.0-i)/50.0 #va de 0 a 1
		else:
			traux=i/10.0 #va de 1 a 0
		r=255
		g=170
		b=50
		a=170.0*traux
		size=225.0*(1-i/60.0)**2.0
		Bladex.SetParticleGVal("EnergyMedallon1",i,r,g,b,a,size)


	Bladex.AddParticleGType("EnergyMedallon2","GenericParticle2",B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>50:
			traux=(60.0-i)/10.0 #va de 0 a 1
		else:
			traux=i/50.0 #va de 1 a 0
		r=255
		g=170
		b=50
		a=170.0*traux
		size=60.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("EnergyMedallon2",i,r,g,b,a,size)


def DeleteAura():
	Bladex.GetEntity("AuraMedallon").SubscribeToList("Pin")

def AuraMedallon(medallon_name,vel):
	r1, g1, b1 = AuraColor1
	r2, g2, b2 = AuraColor2
	medallon=Bladex.GetEntity(medallon_name)
	medallon.SelfIlum = 1
	amedallon=Bladex.CreateEntity("AuraMedallon", "Entity Aura", 0, 0, 0)
	amedallon.SetAuraParams(35, 0.8, 1, 0, 0, 1)
	amedallon.SetAuraGradient(2, r1, g1, b1, 1.0, 0.0, r1, g1, b1, 0.0, 0.3)
	amedallon.SetAuraGradient(1, r2, g2, b2, 0.2, 0.3, r2, g2, b2, 0.0, 1.0)
	medallon.Link(amedallon)
	amedallon.SetAuraActive(1)
	pamedallon=Bladex.CreateEntity("PartsAuraMedallon", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
	pamedallon.ObjectName=medallon_name
	pamedallon.FollowFactor=1.0
	pamedallon.ParticleType="EnergyMedallon1"
	pamedallon.PPS=70
	pamedallon.YGravity=0.0
	pamedallon.Friction=0.0
	pamedallon.Velocity=vel
	pamedallon.RandomVelocity=0.0
	pamedallon.NormalVelocity=10.0
	pamedallon.Time2Live=60
	pamedallon.DeathTime = Bladex.GetTime() + 1.5

	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,DeleteAura,())



def TimerOnLight(entity,timer):
	light = Bladex.GetEntity(entity)
	if light.Data.Intensity < 5:
		light.Intensity=light.Data.Intensity=light.Data.Intensity + 0.133
	else:
		light.Intensity=5.0

def OnLight(NameLight):
	light = Bladex.GetEntity(NameLight)
	InitDataField.Initialise(light)
	light.Data.Intensity = 0
	light.TimerFunc = TimerOnLight
	light.SubscribeToList("Timer30")
	PlaySound(SndCreceLuz,NameLight)


def DiscografiaBarata():
	global Discografia
	Discografia = Discografia - 1
	print "Quedan ",Discografia,"Discos"
	if not Discografia:
		AbreCam.PTS = [((18282.5788352, -9252.32975746, -12271.4131821), (18532.5725744, -9275.55972083, -16130.5789102), 2),
		               ((15576.7923164, -9491.97810808, -10416.8678883), (17078.4890514, -9957.96618728, -12356.8501029), 5)]
		AbreCam.AbreCam()
		AbrePuertaLlaveen()

def leaveD1(ent,event):
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	handItem = char.InvRight

	inv.RemoveObject(handItem)
	inv.LinkRightHand("None")
	gem = Bladex.GetEntity("DiscoMecano")
	gem.Position = Bladex.GetEntity("DiscoMecanoGP").Position
	gem.Orientation = 0.707106781187, 0, 0, 0.707106781187
	gem.Static      = 1
	PlaySound(SndPosaMedallon,"DiscoMecanoGP")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio2"))

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,OnLight,("LuzBRA2",))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.0,AuraMedallon,("DiscoMecano",(-500.0, 0.0, 0.0)))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.5,DiscografiaBarata,())

def useInD1GhostP(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	obj = inv.GetSelectedObject()


	if obj=="DiscoMecano":
		Bladex.DeactivateInput()
		Actions.FreeBothHands("Player1",ContiueUseD1)

def ContiueUseD1():
	Bladex.ActivateInput()
	Actions.TurnToFaceEntityNow("Player1","DiscoMecanoGP")
	inv = char.GetInventory()
	inv.LinkRightHand("DiscoMecano")
	char.LaunchAnmType("Fire2")
	char.AddAnmEventFunc("SetAlightEvent",leaveD1)


############################################################

def leaveD2(ent,event):
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	handItem = char.InvRight

	inv.RemoveObject(handItem)
	inv.LinkRightHand("None")
	gem = Bladex.GetEntity("DiscoLocomia")
	gem.Position = Bladex.GetEntity("DiscoLocomiaGP").Position
	gem.Orientation = 0.707106781187, 0, 0, 0.707106781187
	gem.Static      = 1
	PlaySound(SndPosaMedallon,"DiscoLocomiaGP")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio2"))

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,OnLight,("LuzBRA1",))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.0,AuraMedallon,("DiscoLocomia",(500.0, 0.0, 0.0)))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.5,DiscografiaBarata,())


def useInD2GhostP(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	obj = inv.GetSelectedObject()


	if obj=="DiscoLocomia":
		Bladex.DeactivateInput()
		Actions.FreeBothHands("Player1",ContiueUseD2)

def ContiueUseD2():
	Bladex.ActivateInput()
	Actions.TurnToFaceEntityNow("Player1","DiscoLocomiaGP")
	inv = char.GetInventory()
	inv.LinkRightHand("DiscoLocomia")
	char.LaunchAnmType("Fire2")
	char.AddAnmEventFunc("SetAlightEvent",leaveD2)



######################################################################################################
#                                    gen.py  /  gen2.py
######################################################################################################

def SaltaNieveGen(enmgen):
	pos=enmgen.Position
	tierra2=Bladex.CreateEntity("SnowDust", "Entity Particle System D1", pos[0], -500,pos[2])
	tierra2.ParticleType="SnowDust"
	tierra2.YGravity=100.0
	tierra2.Friction=0.15
	tierra2.PPS=100
	tierra2.Time2Live=32
	tierra2.Velocity=0,-400,0
	tierra2.RandomVelocity=50.0
	tierra2.DeathTime=Bladex.GetTime()+5.0


# especificas para el mapa de vuelta atras
def TieneTablilla():
	import GenFX
	#junto a tablilla
	GenFX.CreateMagicTransport("transp6", (19000,9850,-12000))
