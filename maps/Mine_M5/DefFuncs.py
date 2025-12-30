##///
##||| Mine_M5/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Fixed softlock in case you are hit while picking up the blue gem.
##||| * Changed sound for acid trap door
##\\\ 

import Bladex
import Ontake
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
import Gems
import GotoMapVars
import ScriptSkip
import MusicTool

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para bolas.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def dropStoneA(secIndex,ent):
	global stoneADropped
	global stoneDustAStartTime
	if (ent=="Player1" and stoneADropped==0) :
		stone.drop( "IJBolon1", 9000000,-9000,-900000 )
		#stone.unlock( "IJBolon1" )
		stoneADropped=1
		Patachof()
		stoneASector.OnEnter=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, MusicTool.LaunchMusicEvent,("sorpresa-1b",))
		Bladex.AddScheduledFunc(Bladex.GetTime()+8.0, MusicTool.LaunchMusicEvent,("Atmosfera18",))

def dropStoneB(secIndex,ent):
	global stoneBDropped
	global stoneDustBStartTime
	if (ent=="Player1" and stoneBDropped==0) :
		darfuncs.Temblores(3.0,150)
		stone.drop( "IJBolon2", 444444,-8358,72222222 )
		#stone.unlock( "IJBolon2" )
		stoneBDropped=1
		stoneBSector.OnEnter =""
		#Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Bladex.ExeMusicEvent,(Bladex.GetMusicEvent("sorpresa-1b"),),"DropStoneBMusic")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para bichitozampon.py   **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SndZampaGema(ent,Time):
	_SndZampaGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndCorreGema(ent,Time):
	_SndCorreGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def SndSorpresaGema(ent,Time):
	_SndSorpresaGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def SndMorfaGema(ent,Time):
	_SndMorfaGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndEructaGema(ent,Time):
	_SndEructaGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)
def SndEscapaGema(ent,Time):
	_SndEscapaGema.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def BLightTimerB(light,time):
	global lightTimerStartTimeB
	time=Bladex.GetTime()
	time=time-lightTimerStartTimeB
	time=time*2.0
	luz = Bladex.GetEntity(light)
	luz.Intensity = 6.0 - (time * 6.0)	# blue gem max int 6
	if (time>1.00) :
		luz.Intensity = 0
		luz.RemoveFromList("BLightTimerB")
		luz.TimerFunc=""

def takeGemB() :
	#print(">btakeGemB()  fade")
	global lightTimerStartTimeB
	lightTimerStartTimeB=0.0
	luz = Bladex.GetEntity("GemaBLight")
	luz.TimerFunc=BLightTimerB;
	luz.SubscribeToList("BLightTimerB")
	lightTimerStartTimeB=Bladex.GetTime()

def bDestroyCosita():
	#print(">bDestroyCosita()")
	o=Bladex.GetEntity("CosA")

	o.Position=-64000, -20000, -152000
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	o.ActionAreaMin=pow(2,0)
	o.ActionAreaMax=pow(2,0)
	EnemyTypes.EnemyDefaultFuncs(o)

	o.Data.ImDeadFuncPlus	= o.ImDeadFunc
	o.ImDeadFunc		= MuerteBichitoZampon

	#o.Data.JoinGroup(o.Name, "GGroup1")
	#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)

	#o.TurnOff()
	#o.RemoveFromWorld()
	#o.SubscribeToList("Pin")


def bEatGema(ent,Time):
	#print(">bEatGema(ent,Time)")
	gemaBlue=Bladex.GetEntity("GemaB")
	gemaBlue.TurnOff()
	gemaBlue.Actor=0
	gemaBlue.Static=0

	o=Bladex.GetEntity("CosA")
	#o.Unlink(c)
	inv = o.GetInventory()
	inv.LinkLeftHand("None")
	Actions.TakeObject(o.Name,"GemaB")

def bTakeGema():
	#print(">bTakeGema(ent,Time)")

	gemaBlue=Bladex.GetEntity("GemaB")
	gemaBlue.Actor=1
	gemaBlue.Position = (-101610.422,-19279.77,-100871.484)
	gemaBlue.Animation="Gem_escena01_mina"
	gemaBlue.FPS=20.0
	gemaBlue.SendSectorMsgs=0
	gemaBlue.TurnOn()
	#o.SetTmpAnmFlags(1,1,1,0,5,1)

	#inv = o.GetInventory()
	#inv.LinkLeftHand("GemaB")

def bCreateCosita():
	#print(">bCreateCosita()")
	o=Bladex.CreateEntity("CosA","Cos",-97848.07,-19566.262,-115691.469,"Person")
	o.Angle=3.14
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	darfuncs.HideBadGuy("CosA")


	########
	####     Actor cool
	########

	o=Bladex.CreateEntity("CosActor","Cos",-97848.07,-19840.262,-115691.469)
	o.Actor=1
	o.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	o.Animation="Cos_escena01_mina"
	o.FPS=20.0
	o.SendSectorMsgs=0
	o.TurnOn()

	darfuncs.HideBadGuy("CosA")

	#o.LaunchAnimation("Cos_escena01_mina")

def bCameraOff(ent,Time):
	print(">bCameraOff(ent,Time)")
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	bDestroyCosita()
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	darfuncs.UnhideBadGuy("CosA")
	Bladex.GetEntity("CosA").SetOnFloor()
	Bladex.GetEntity("CosActor").SubscribeToList("Pin")

def bCameraE(ent,Time):
	#print(">bCameraE(ent,Time)")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("cosita_GemaCamera05.cam",291,380)
	cam.AddCameraEvent(-1,bCameraOff)
	cam.AddCameraEvent(298-291,SndEscapaGema)


def bCameraD(ent,Time):
	#print(">bCameraD(ent,Time)")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("cosita_GemaCamera04.cam",189,290)
	cam.AddCameraEvent(-1,bCameraE)

	cam.AddCameraEvent(211-189,SndMorfaGema)
	cam.AddCameraEvent(240-189,SndEructaGema)




def bCameraC(ent,Time):
	#print(">bCameraC(ent,Time)")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("cosita_GemaCamera03.cam",71,188)
	cam.AddCameraEvent(-1,bCameraD)

	cam.AddCameraEvent( 93-71,SndCorreGema)
	cam.AddCameraEvent(141-71,SndSorpresaGema)
	cam.AddCameraEvent(183-71,SndZampaGema)
	cam.AddCameraEvent(185-71,bEatGema)




def bCameraB(ent,Time):
	#print(">bCameraB(ent,Time)")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("cosita_GemaCamera02.cam",21,70)
	cam.AddCameraEvent(-1,bCameraC)




def bCameraA():
	#print(">bCameraA()")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("cosita_GemaCamera01.cam",0,20)
	bTakeGema()
	cam.AddCameraEvent(-1,bCameraB)



def bSceneStart(trsector_name,ent):
	global bScenePlayed
	Bladex.SetListenerPosition(1)
	if (ent<>"Player1") : return
	#print(">bSceneStart()")
	if (bScenePlayed) : return
	bScenePlayed=1
	bCreateCosita()
	bCameraA()
	char = Bladex.GetEntity("Player1")
	char.Position=-88014.711,-26092.023,-99069.961
	char.Angle=3.14
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("escena01_mina")
	char.Position=-88014.711,-26092.023,-99069.961
	char.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+8.35, takeGemB, (),"takeGemB")
	Bladex.SetTriggerSectorFunc("bicho", "OnEnter", "" )
	ScriptSkip.SkipScriptStart("MineBichozampon")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-zampon"))

def BorraLuzAzulada():
	gemaBlue = Bladex.GetEntity("GemaB")
	luz      = Bladex.GetEntity("GemaBlueLight")
	gemaBlue.Unlink(luz)
	luz.SubscribeToList("Pin")
	Ontake.DelOnTakeEvent(gemaBlue.Name)			# Should fix blue gem softlock 	-LeadHead


def MuerteBichitoZampon(ent_name):
	global LuzGemaintensity
	Bladex.GetEntity(ent_name).Data.ImDeadFuncPlus (ent_name)
	gemaBlue=Bladex.GetEntity("GemaB")
	gemaBlue.PutToWorld()
	gemaBlue.SelfIlum= -2

	luz = Bladex.CreateEntity("GemaBlueLight","Entity Spot",0,0,0)
	luz.Color = 74,89,128
	luz.Intensity = 4
	luz.CastShadows = 0
	luz.Precission = 0.06
	luz.Visible = 0
	luz.Flick = 0
	gemaBlue.Link(luz)
	Ontake.AddOnTakeEvent(gemaBlue.Name,BorraLuzAzulada)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera18"))

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para bgates.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def dustTriangle (name,p1,p2,p3):
	#print(p1)
	#print(p2)
	#print(p3)
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

def revientaPuertaA(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global puertaReventadaA
	if (puertaReventadaA) : return

	#print ("hit")

	char=Bladex.GetEntity("Player1")
	weapon=Bladex.GetEntity(entity_name)
	if (not weapon.Weapon) : return				# tiene que llevar un arma en la mano

	bgateA1.DoBreak((2.5, 0.0, 1.0), (px, py, pz), (0.0, 0.0, 0.0))
	bgateA2.DoBreak((2.5, 0.0, -1.0), (px, py, pz), (0.0, 0.0, 0.0))

	p0 = 85750, -13000, -157500
	p1 = 85750, -11000, -159250
	p2 = 85750, -10000, -157500
	p3 = 85750, -10000, -159250

	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)
	derrumbebgate1.Play(85650, -13000, -157800)
	puertaReventadaA=1

def revientaPuertaB(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global puertaReventadaB

	#print ("hit")

	if (puertaReventadaB) : return

	char=Bladex.GetEntity("Player1")
	weapon=Bladex.GetEntity(entity_name)
	if (not weapon.Weapon) : return				# tiene que llevar un arma en la mano

	bgateB1.DoBreak((0.4, 0.0, -3.5), (px, py, pz), (0.0, 0.0, 0.0))
	bgateB2.DoBreak((0.4, 0.0, -3.5), (px, py, pz), (0.0, 0.0, 0.0))

	p0 = -122700,-16000,10330
	p1 = -123950,-17000,10330
	p2 = -122700,-15000,10330
	p3 = -123950,-15000,10330

	dustTriangle("rppolvo3",p0,p1,p2)
	dustTriangle("rppolvo4",p3,p1,p2)
	derrumbebgate2.Play(-122900,-16000,10430)
	puertaReventadaB=1


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para aranas.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def runSpiderA() :
	spider = Bladex.GetEntity("spiderA")
	spider.Alpha = 1.0
	spider.Angle=3.14
	spider.Position=-134863.797,-13737.034,-33938.094
	spider.SetTmpAnmFlags(1,1,1,0,5,1)
	spider.LaunchAnimation("Spd_1_mina_01")

def runSpiderB() :
	spider = Bladex.GetEntity("spiderB")
	spider.Alpha = 1.0
	spider.Angle=3.14
	spider.Position=-129907.125,-21510.701,-31688.512
	spider.SetTmpAnmFlags(1,1,1,0,5,1)
	spider.LaunchAnimation("Spd_2_mina_01")

def runSpiderC() :
	spider = Bladex.GetEntity("spiderC")
	spider.Alpha = 1.0
	spider.Angle=3.14
	spider.SetTmpAnmFlags(1,1,1,0,5,1)
	spider.Position=-124953.977,-19139.791,-34780.535
	spider.LaunchAnimation("Spd_3_mina_01")

def stopSpiderA() :
	o=Bladex.GetEntity("spiderA")
	#o.Position=-64000, -20500, -152000
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	o.ActionAreaMin=pow(2,0)
	o.ActionAreaMax=pow(2,1)
	EnemyTypes.EnemyDefaultFuncs(o)
	o.SetOnFloor()

def stopSpiderB() :
	o=Bladex.GetEntity("spiderB")
	#o.Position=-64000, -20500, -152000
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	o.ActionAreaMin=pow(2,0)
	o.ActionAreaMax=pow(2,1)
	EnemyTypes.EnemyDefaultFuncs(o)
	o.SetOnFloor()

def stopSpiderC() :
	o=Bladex.GetEntity("spiderC")
	#o.Position=-64000, -20500, -152000
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	o.ActionAreaMin=pow(2,0)
	o.ActionAreaMax=pow(2,1)
	EnemyTypes.EnemyDefaultFuncs(o)
	o.SetOnFloor()

def spidersAttack() :
	stopSpiderA()
	stopSpiderB()
	stopSpiderC()

def CaeArana(arana,sound):
	ara = Bladex.GetEntity(arana)
	sound.Position = ara.Position
	sound.PlaySound(0)

def runSpyders():
	runSpiderA()
	runSpiderB()
	runSpiderC()

def runSpiders() :
	SoundDesliz.Position = char.Position
	SoundDesliz.PlaySound(-1)
	darfuncs.UnhideBadGuy("spiderA")
	darfuncs.UnhideBadGuy("spiderB")
	darfuncs.UnhideBadGuy("spiderC")
	time = Bladex.GetTime()

	Bladex.AddScheduledFunc(time + 5.4, CaeArana,("spiderA",SoundCaida1),"spiderA CaeArana")
	Bladex.AddScheduledFunc(time + 5.6, CaeArana,("spiderB",SoundCaida2),"spiderB CaeArana")
	Bladex.AddScheduledFunc(time + 4.7, CaeArana,("spiderC",SoundCaida3),"spiderB CaeArana")

	Bladex.AddScheduledFunc(time + 6.0, SoundDesliz.StopSound,(),"SoundDesliz.StopSound")
	Bladex.AddScheduledFunc(time + 7.0, spidersAttack, (),"spidersAttack")

	Bladex.AddScheduledFunc(time + 0.0, runSpyders,(),"runSpyders")

########################## camera ########################################################

def restoreSpdrSceneCam(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)

def setSpdrSceneCamC(camera, frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("spd_minacamera01.cam",97,120)
	cam.AddCameraEvent(-1,restoreSpdrSceneCam)

def setSpdrSceneCamB(Camera,Frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("spd_minacamera03.cam",50,97)
	cam.AddCameraEvent(-1,setSpdrSceneCamC)


def setSpdrSceneCamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("spd_minacamera02.cam",0,50)
	cam.AddCameraEvent(-1,setSpdrSceneCamB)
	Bladex.DeactivateInput()
	Scorer.SetVisible(0)

def playSpdrScene()  :
	runSpiders()
	setSpdrSceneCamA()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-aranas"))


def startSpiderScenePlay(trsector_name, ent) :
	global smallSpidersScene
	if (smallSpidersScene or ent<>"Player1") : return

	smallSpidersScene = 1
	char.Position = (-128110.203, -5178, -33928.453)
	playSpdrScene()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para cosgen.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


#char.Position = (14751.9727814, 9108.77554621, -207685.060963)


def CreaGremilinDichoso(o):
	o.Level = 3
	o.Life  = 50
	o.SetOnFloor()
	#print "Crea",o.Name, o.Position

def SaltaTierraGen(enmgen):
	#enmgen.SetActiveEnemy("Player1")
	Actions.QuickTurnToFaceEntity(enmgen.Name,"Player1")
	enmgen.GoTo(char.Position[0],char.Position[1],char.Position[2])


	#print "Sale",enmgen.Name, enmgen.Position

def ActivateCositaEnemyGenerator(TrSector,Entity):
	if Entity == "Player1":
		#print "Cosita Generator"
		generadorT1.GenerateEnemy()
		RodEnemyGen1.OnEnter = ""


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************  Definiciones para desprendimientos.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def runDespA(trsector_name, ent):
	global despABreak
	if(despABreak==0):
		despA1.DoBreak((0,-1,0),(7500,-16350,-71000),(0,0,0))
		despA2.DoBreak((0,-1,0),(8750,-16350,-72750),(0,0,0))
		despA3.DoBreak((0,-1,0),(9750,-16350,-71250),(0,0,0))

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

def runDespB(trsector_name, ent):
	global despBBreak
	if(despBBreak==0):
		despB1.DoBreak((0,-1,0),(-32750,-28300,-65000),(0,0,0))
		despB2.DoBreak((0,-1,0),(-31500,-28300,-66250),(0,0,0))
		despB3.DoBreak((0,-1,0),(-30250,-28300,-65000),(0,0,0))

		p0 = -32750,-28300,-62500
		p1 = -30000,-28300,-62000
		p2 = -30250,-28300,-67750
		p3 = -33000,-28300,-67750

		dust0=Bladex.CreateEntity("despSDustA", "Entity Particle System D3", p0[0],p0[1],p0[2] )
		dust0.D1= p1[0]-p0[0] ,p1[1]-p0[1] ,p1[2]-p0[2]
		dust0.D2= p2[0]-p1[0] ,p2[1]-p1[1] ,p2[2]-p1[2]
		dust1=Bladex.CreateEntity("despSDustb", "Entity Particle System D3", p3[0],p3[1],p3[2] )
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
		derrumbesuelopiedra2.Play(-32750,-29300,-65000)

		despBBreak=1


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************                                        **************************
#*******************************   Definiciones para iscene.py          **************************
#*******************************                                        **************************
#*************************************************************************************************
#*************************************************************************************************

def FinCameraInicio(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()
	Bladex.SetListenerPosition(1)

def ChangeCameraInicio(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("inicio_enanoCameraFinal_Enano.cam",0,298)
	cam.AddCameraEvent(242,PolvilloRabioso)
	cam.AddCameraEvent(-1,FinCameraInicio)
	AuxFuncs.FadeFrom(3, 0.0)

	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	inv.LinkBack("MineEscudoInvPrb1")
	inv.LinkBack("MineWeaponInvPrb1")
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.Angle = 3.14

	if (char.Kind=="Dwarf_N")	:
		char.Position = 51675.887, -3999, -27680
	if (char.Kind=="Amazon_N")	:
		char.Position = 51540.156, -4368.544+250.0, -27677.617
	if (char.Kind=="Knight_N")	:
		char.Position = 51516.891, -4274.743+250.0, -27699.855
	if (char.Kind=="Barbarian_N") :
		char.Position = 51440.32, -4020.991, -27680.65

	char.LaunchAnmType("start_mina")


def StartInicio():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("iniciomina"))
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("vistaminaCamera01.cam",0,340)
	Bladex.SetListenerPosition(2)
	cam.AddCameraEvent(-1,ChangeCameraInicio)
	ScriptSkip.SkipScriptStart("minaini")

	Bladex.AddScheduledFunc(Bladex.GetTime() + 14.5,AuxFuncs.FadeTo,(3,1),"AfterSceneFade")


def PreStartInicio():
	AuxFuncs.FadeFrom(4.5, 0.0)
	GameText.WriteText("M5T1")

	#Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,StartInicio,(),"StartInicio")
	StartInicio()

def PolvilloRabioso(x,y):
	dust.RemueveTierraGen(51810, -400, -19488 ,500,500,125,"FastDust",16,0.25)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para GEnems.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##
## Enemigos iniciales
##
##
##

def getOrksN() :
	nOrcs = 0

	orc = Bladex.GetEntity("18orc")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("18borc")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("18corc")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("g1ork1")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("g1ork2")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("g2ork3")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("g2ork1")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1

	orc = Bladex.GetEntity("g2ork2")
	if (orc) :
		if (orc.Life>0) :
			nOrcs=nOrcs+1


	#print nOrcs

	return nOrcs

###
### enemyGroupOut()
###
### (saca el grupo enemigo correspondiente)
###

def DeleteEnemFromMine(Name):
	ork=Bladex.GetEntity(Name)
	if ork:
		if ork.Life<=0:
			ork.SubscribeToList("Pin")

def ClearCentralMine():
	Bladex.CleanArea(-31904.4750235, -31069.6038644, -20990.3075888,18000)

def enemyGroupOut( ax, az, ay, bx, bz, by, cx, cz, cy ) :
	global EnemyGroupsOut

	DeleteEnemFromMine("18orc")
	DeleteEnemFromMine("18borc")
	DeleteEnemFromMine("18corc")
	DeleteEnemFromMine("g1ork1")
	DeleteEnemFromMine("g1ork2")
	DeleteEnemFromMine("g1ork3")
	DeleteEnemFromMine("g2ork1")
	DeleteEnemFromMine("g2ork2")
	ClearCentralMine()

	orksInScene=getOrksN()



	if (EnemyGroupsOut==0 ) :
		# primer grupo ( 3 orcos con escudos y espadas ) en el punto A
		#print"primer grupo fuera"

		# grupo 1 orco 1
		if (orksInScene<2) :
			orkweapon=Bladex.CreateEntity("mineg1ork1espad","Gladius",0,0,0,"Weapon")
			shield=Bladex.CreateEntity("mineg1ork1escud","Escudo1",0,0,0)
			Sparks.MakeShield("mineg1ork1escud")
			ork=Bladex.CreateEntity("g1ork1","Ork",ax,az,ay,"Person")
			ork.Angle=6
			ork.Level=lvl_control.GiveLevel(1,4)
			Actions.TakeObject(ork.Name,"mineg1ork1espad")
			Actions.TakeObject(ork.Name,"mineg1ork1escud")
			ork.ActionAreaMin=pow(2,0)
			ork.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(ork)
			ork.Data.JoinGroup(ork.Name, "GGroup1")
			ork.SetOnFloor()
			#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)
			orksInScene=orksInScene+1

		# grupo 1 orco 2
		if (orksInScene<2) :
			orkweapon=Bladex.CreateEntity("mineg1ork2espad","Gladius",0,0,0,"Weapon")
			shield=Bladex.CreateEntity("mineg1ork2escud","Escudo1",0,0,0)
			Sparks.MakeShield("mineg1ork2escud")
			ork=Bladex.CreateEntity("g1ork2","Ork",bx,bz,by,"Person")
			ork.Angle=4.7
			ork.Level=lvl_control.GiveLevel(1,4)
			Actions.TakeObject(ork.Name,"mineg1ork2espad")
			Actions.TakeObject(ork.Name,"mineg1ork2escud")
			ork.ActionAreaMin=pow(2,0)
			ork.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(ork)
			ork.Data.JoinGroup(ork.Name, "GGroup1")
			ork.SetOnFloor()
			#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)
			orksInScene=orksInScene+1

		# grupo 1 orco 3
		if (orksInScene<2) :
			orkweapon=Bladex.CreateEntity("mineg1ork3espad","Gladius",0,0,0,"Weapon")
			shield=Bladex.CreateEntity("mineg1ork3escud","Escudo1",0,0,0)
			Sparks.MakeShield("mineg1ork3escud")
			ork=Bladex.CreateEntity("g1ork3","Ork",cx,cz,cy,"Person")
			ork.Angle=4.7
			ork.Level=lvl_control.GiveLevel(1,4)
			Actions.TakeObject(ork.Name,"mineg1ork3espad")
			Actions.TakeObject(ork.Name,"mineg1ork3escud")
			ork.ActionAreaMin=pow(2,0)
			ork.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(ork)
			ork.Data.JoinGroup(ork.Name, "GGroup1")
			ork.SetOnFloor()
			#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)
			orksInScene=orksInScene+1

		EnemyGroupsOut=EnemyGroupsOut+1

		return

	if (EnemyGroupsOut==1) :
		# segundo grupo ( 2 orcos con escudos y espadas y un troll ) en el punto C
		#print"segundo grupo fuera"

		# grupo 2 orco 1
		if (orksInScene<2) :
			orkweapon=Bladex.CreateEntity("mineg2ork1espad","Gladius",0,0,0,"Weapon")
			shield=Bladex.CreateEntity("mineg2ork1escud","Escudo1",0,0,0)
			Sparks.MakeShield("mineg2ork1escud")
			ork=Bladex.CreateEntity("g2ork1","Ork",ax,az,ay,"Person")
			ork.Angle=0
			ork.Level=lvl_control.GiveLevel(1,4)
			Actions.TakeObject(ork.Name,"mineg2ork1espad")
			Actions.TakeObject(ork.Name,"mineg2ork1escud")
			ork.ActionAreaMin=pow(2,0)
			ork.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(ork)
			ork.Data.JoinGroup(ork.Name, "GGroup2")
			ork.SetOnFloor()
			#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)
			orksInScene=orksInScene+1

		# grupo 2 orco 2
		if (orksInScene<2) :
			orkweapon=Bladex.CreateEntity("mineg2ork2espad","Gladius",0,0,0,"Weapon")
			shield=Bladex.CreateEntity("mineg2ork2escud","Escudo1",0,0,0)
			Sparks.MakeShield("mineg2ork2escud")
			ork=Bladex.CreateEntity("g2ork2","Ork",bx,bz,by,"Person")
			ork.Angle=0
			ork.Level=lvl_control.GiveLevel(1,4)
			Actions.TakeObject(ork.Name,"mineg2ork2espad")
			Actions.TakeObject(ork.Name,"mineg2ork2escud")
			ork.ActionAreaMin=pow(2,0)
			ork.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(ork)
			ork.Data.JoinGroup(ork.Name, "GGroup2")
			ork.SetOnFloor()
			#AniSound.AsignarSonidosCaballeroTraidor(ork.Name)
			orksInScene=orksInScene+1

		# grupo 2 troll 1
		if (orksInScene<2) :
			trollweapon=Bladex.CreateEntity("mineg2TrollGarr","Garropin",0,0,0,"Weapon")
			troll=Bladex.CreateEntity("g2Troll","Great_Ork",cx,cz,cy,"Person")
			troll.Angle=0
			troll.Level=lvl_control.GiveLevel(1,3)
			Actions.TakeObject(troll.Name,"mineg2TrollGarr")
			troll.ActionAreaMin=pow(2,0)
			troll.ActionAreaMax=pow(2,1)
			EnemyTypes.EnemyDefaultFuncs(troll)
			troll.Data.JoinGroup(troll.Name, "GGroup2")
			troll.SetOnFloor()
			orksInScene=orksInScene+1
			#AniSound.AsignarSonidosCaballeroTraidor(troll.Name)

		EnemyGroupsOut=EnemyGroupsOut+1

		return

def putAGroup():
	global tunnelAGroupOut
	if (tunnelAGroupOut==0) :
		a = -38252.5290135, -31056.3535663, -36801.717
		b = -43064.5150714, -31122.6147559, -24891.889
		c = -42064.5150714, -31122.6147559, -24891.889
		enemyGroupOut( a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2] );
		tunnelAGroupOut =1

def putBGroup():
	global tunnelBGroupOut
	if (tunnelBGroupOut==0) :
		a = -38252.5290135, -31056.3535663, -36801.717
		b = -43064.5150714, -31122.6147559, -24891.889
		c = -42064.5150714, -31122.6147559, -24891.889
		enemyGroupOut( a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2] );
		tunnelBGroupOut =1

def checkItem(item):
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	invElements = inv.nKindObjects

	checkItemRVal = 0
	for i in range(invElements):
		Obj=inv.GetObject(i)
		#print(Obj)
		if (Obj==item) :
			checkItemRVal = 1
			return 1
	return 0

def tunnelACheck(SectorIndex,ent):
	if (ent=="Player1" and checkItem("GemaR")) :
		putAGroup()
		tunnelASector.OnEnter=""

def tunnelBCheck(SectorIndex,ent):
	if (ent=="Player1" and checkItem("GemaB")) :
		putBGroup()
		tunnelBSector.OnEnter=""

def tunnelCCheck(SectorIndex,ent):
	if (ent=="Player1"):
		tunnelCSector.OnEnter=""
		darfuncs.UnhideBadGuy("18orc")
		darfuncs.UnhideBadGuy("18borc")
		darfuncs.UnhideBadGuy("18corc")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para gemas.py           **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

################ polvo en el sector del hexagonal

def platformStartDust():
	h= -10000-12000-50

	p= 14830,-24827
	l= 4500
	w= 4000

	dust0=Bladex.CreateEntity("platformSDustA", "Entity Particle System D3", p[0],h,p[1] )
	dust0.D1= l,0,0
	dust0.D2= 0,0,-w
	dust1=Bladex.CreateEntity("platformSDustB", "Entity Particle System D3", p[0]+l,h,p[1]-w )
	dust1.D1= -l,0,0
	dust1.D2= 0,0,w

	dust0.ParticleType="Dust"
	dust1.ParticleType="Dust"
	dust0.YGravity=-900.0
	dust1.YGravity=-900.0
	dust0.Friction=0.5
	dust1.Friction=0.5
	dust0.PPS=150
	dust1.PPS=150
	dust0.DeathTime=Bladex.GetTime()+3.4
	dust1.DeathTime=Bladex.GetTime()+3.4
	dust0.Time2Live=8
	dust1.Time2Live=8
	dust0.Velocity=0.0, 3000.0, 0.0
	dust1.Velocity=0.0, 3000.0, 0.0
	dust0.RandomVelocity=30.0
	dust1.RandomVelocity=30.0

def platformDust(h):
	a= 17080	 ,-24827+220
	b= 19330-220 ,-25577
	c= 19330-220 ,-28327
	d= 17080	 ,-29077-220
	e= 14830+220 ,-28327
	f= 14830+220 ,-25577

	#a-b
	dust0=Bladex.CreateEntity("platformDust0", "Entity Particle System D2", a[0],h,a[1] )
	dust0.D=b[0]-a[0],0,b[1]-a[1]
	#b-c
	dust1=Bladex.CreateEntity("platformDust1", "Entity Particle System D2", b[0],h,b[1] )
	dust1.D=c[0]-b[0],0,c[1]-b[1]
	#c-d
	dust2=Bladex.CreateEntity("platformDust2", "Entity Particle System D2", c[0],h,c[1] )
	dust2.D=d[0]-c[0],0,d[1]-c[1]
	#d-e
	dust3=Bladex.CreateEntity("platformDust3", "Entity Particle System D2", d[0],h,d[1] )
	dust3.D=e[0]-d[0],0,e[1]-d[1]
	#e-f
	dust4=Bladex.CreateEntity("platformDust4", "Entity Particle System D2", e[0],h,e[1] )
	dust4.D=f[0]-e[0],0,f[1]-e[1]
	#f-a
	dust5=Bladex.CreateEntity("platformDust5", "Entity Particle System D2", f[0],h,f[1] )
	dust5.D=a[0]-f[0],0,a[1]-f[1]

	dust0.ParticleType="DesertDust"
	dust1.ParticleType="DesertDust"
	dust2.ParticleType="DesertDust"
	dust3.ParticleType="DesertDust"
	dust4.ParticleType="DesertDust"
	dust5.ParticleType="DesertDust"
	dust0.YGravity=0.0
	dust1.YGravity=0.0
	dust2.YGravity=0.0
	dust3.YGravity=0.0
	dust4.YGravity=0.0
	dust5.YGravity=0.0
	dust0.Friction=0.3
	dust1.Friction=0.3
	dust2.Friction=0.3
	dust3.Friction=0.3
	dust4.Friction=0.3
	dust5.Friction=0.3
	dust0.PPS=10
	dust1.PPS=10
	dust2.PPS=10
	dust3.PPS=10
	dust4.PPS=10
	dust5.PPS=10
	dust0.DeathTime=Bladex.GetTime()+3.4
	dust1.DeathTime=Bladex.GetTime()+3.4
	dust2.DeathTime=Bladex.GetTime()+3.4
	dust3.DeathTime=Bladex.GetTime()+3.4
	dust4.DeathTime=Bladex.GetTime()+3.4
	dust5.DeathTime=Bladex.GetTime()+3.4
	dust0.Time2Live=50
	dust1.Time2Live=50
	dust2.Time2Live=50
	dust3.Time2Live=50
	dust4.Time2Live=50
	dust5.Time2Live=50
	dust0.Velocity=0.0, -400.0, 0.0
	dust1.Velocity=0.0, -400.0, 0.0
	dust2.Velocity=0.0, -400.0, 0.0
	dust3.Velocity=0.0, -400.0, 0.0
	dust4.Velocity=0.0, -400.0, 0.0
	dust5.Velocity=0.0, -400.0, 0.0
	dust0.RandomVelocity=10.0
	dust1.RandomVelocity=10.0
	dust2.RandomVelocity=10.0
	dust3.RandomVelocity=10.0
	dust4.RandomVelocity=10.0
	dust5.RandomVelocity=10.0

################ control de la plataforma por timer

def openGemRoomDoor():
	gemRoomDoor.opentype=Doors.AC_UNIF_DEC
	gemRoomDoor.o_init_vel=0
	gemRoomDoor.o_init_displ=1000
	gemRoomDoor.o_med_vel=-500
	gemRoomDoor.o_med_displ=2000
	gemRoomDoor.o_end_vel=0
	gemRoomDoor.o_end_displ=500
	gemRoomDoor.SetWhileOpenSound(maderadesliz2)
	gemRoomDoor.SetEndOpenSound(maderagolpe2)
	gemRoomDoor.OpenDoor()


def platformDustEvent(sld_areaName,time):
	sld_area = Bladex.GetEntity(sld_areaName)

	disp = sld_area.Displacement

	if (disp > 7500) :
		platformDust(-12000 - disp )

	if (disp < 100) :
		platformDust(-12000 )

	if (disp < 5) :
		sld_area.RemoveFromList("PlatformDustTimer")
		sld_area.TimerFunc="";
		time = Bladex.GetTime()
		Bladex.AddScheduledFunc(time + 4.0, openGemRoomDoor, () ,"openGemRoomDoor")


def RLightTimerB(light,time):
	global lightTimerStartTime
	luz = Bladex.GetEntity("GemaRLight")
	time=Bladex.GetTime()
	time=time-lightTimerStartTime
	time=time*7.0
	luz = Bladex.GetEntity(light)
	luz.Intensity = 3.0 - (time * 3.0)	# red gem max int 3
	if (time>1.00) :
		luz.Intensity = 0.0
		luz.RemoveFromList("RLightTimerB")
		luz.TimerFunc=""

def GLightTimerB(light,time):
	global lightTimerStartTime
	time=Bladex.GetTime()
	time=time-lightTimerStartTime
	time=time*7.0
	luz = Bladex.GetEntity("GemaBLight")
	luz = Bladex.GetEntity(light)
	luz.Intensity = 3.0 - (time * 3.0)	# green gem max int 3
	if (time>1.00) :
		luz.Intensity = 0.0
		luz.RemoveFromList("GLightTimerB")
		luz.TimerFunc=""

def RLightTimer(light,time):
	global lightTimerStartTime
	time=Bladex.GetTime()
	time=time-lightTimerStartTime
	luz = Bladex.GetEntity("GemaRLight")
	luz = Bladex.GetEntity(light)
	luz.Intensity = time * 3.0		# red gem max int 3
	if (time>1.00) :
			luz.RemoveFromList("Timer15")
			luz.TimerFunc=""

def GLightTimer(light,time):
	global lightTimerStartTime
	time=Bladex.GetTime()
	time=time-lightTimerStartTime
	luz = Bladex.GetEntity("GemaGLight")
	if (time>1.00) :
		time=1.00
		luz.RemoveFromList("Timer15")
		luz.TimerFunc=""
	luz = Bladex.GetEntity(light)
	luz.Intensity = time * 3.0		# green gem max int 3

def BLightTimer(light,time):
	global lightTimerStartTime
	time=Bladex.GetTime()
	time=time-lightTimerStartTime
	luz = Bladex.GetEntity("GemaBLight")
	if (time>1.00) :
		time=1.00
		luz.RemoveFromList("Timer15")
		luz.TimerFunc=""
	luz = Bladex.GetEntity(light)
	luz.Intensity = time * 6.0

############################ Colocacion de la gema

def takeGemR() :
	global lightTimerStartTime
	luz = Bladex.GetEntity("GemaRLight")
	Bladex.CreateTimer("RLightTimerB",0.010)
	luz.TimerFunc=RLightTimerB;
	luz.SubscribeToList("RLightTimerB")
	lightTimerStartTime=Bladex.GetTime()
	
	Ontake.DelOnTakeEvent("GemaR")			# Added

def takeGemG() :
	global lightTimerStartTime
	luz = Bladex.GetEntity("GemaGLight")
	Bladex.CreateTimer("GLightTimerB",0.010)
	luz.TimerFunc=GLightTimerB;
	luz.SubscribeToList("GLightTimerB")
	lightTimerStartTime=Bladex.GetTime()
	MusicTool.Music2Sector("ambiente33","Atmosfera18")
	MusicTool.ModifyMusicEvent("ambiente33","ambiente30")
	
	Ontake.DelOnTakeEvent("GemaG")				# Added

def Print(x):
	print x

def leaveGem(ent,event) :
	global lightTimerStartTime


	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	handItem = char.InvRight
	inv.LinkRightHand("None")

	inv.RemoveObject(handItem)
	gemobj = None

	if (handItem=="GemaR") :

		gspt = Bladex.GetEntity("GemRGPointer")
		gemobj = Bladex.GetEntity(handItem)
		gemobj.Position = gspt.Position
		gemobj.Static = 1
		gemobj.Scale = 1.061520
		gemobj.Orientation = 0.707080,0.006171,-0.006171,-0.707080

		luz = Bladex.GetEntity("GemaRLight")
		luz.Position = gemobj.Position
		luz.TimerFunc=RLightTimer;
		luz.SubscribeToList("Timer15")
		lightTimerStartTime=Bladex.GetTime()
		gemaazulson.Play(33929.460208,-24853.672511,-27032.143880)
		Gems.SetGemColor(Gems.RED_GEM)
		Gems.Concentrator(gemobj.Position)

	if (handItem=="GemaG") :
		gemobj = Bladex.GetEntity(handItem)
		gemobj.Position = 24287.778000,-24835.662000,-40362.065000
		gemobj.Static = 1
		gemobj.Scale = 1.115668
		gemobj.Orientation = 0.586218,0.415627,0.395409,0.572061
 		luz = Bladex.GetEntity("GemaGLight")
		luz.Position = 24250,-24835.662000,-40250
		luz.TimerFunc=GLightTimer;
		luz.SubscribeToList("Timer15")
		lightTimerStartTime=Bladex.GetTime()
		gemaazulson.Play(24221.778245,-24645.661639,-40392.065057)
		Gems.SetGemColor(Gems.GREEN_GEM)
		Gems.Concentrator(gemobj.Position)

	if (handItem=="GemaB") :
		gemobj = Bladex.GetEntity(handItem)
		gemobj.Position = 24267.933167,-24811.917853,-13673.558495
		gemobj.Static = 1
		gemobj.Scale = 1.082857
		gemobj.Orientation = 0.568413,0.420603,-0.420603,-0.568413
		luz = Bladex.GetEntity("GemaBLight")
		luz.Position = gemobj.Position
		luz.TimerFunc=BLightTimer;
		luz.SubscribeToList("Timer15")
		lightTimerStartTime=Bladex.GetTime()
		gemaazulson.Play(24267.933167,-24211.917853,-13673.558495)
		Gems.SetGemColor(Gems.BLUE_GEM)
		Gems.Concentrator(gemobj.Position)

	if gemobj:
		gemobj.SelfIlum = 1

		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-3"))


def restoreHand(ent):
	Change.RestoreHand(ent,1)

def leaveMovement(ent,object) :
	char = Bladex.GetEntity(ent)
	char.LaunchAnmType("Fire2")							# hace el gesto de dejar
	char.AddAnmEventFunc("SetAlightEvent",leaveGem)		# deja la gema y pone la luz cuando el tio deja la gema
	char.AnmEndedFunc = restoreHand						# vuelve a coger la espada
	if not (RGemOk and GGemOk and BGemOk):
		Bladex.ActivateInput()


def resetCam():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def stopCam(ent, cam, node):
	cam=Bladex.GetEntity("Camera")
	if node==2:
		cam.SType=0
		cam.CameraClearPath(0)
		time=Bladex.GetTime()
		Bladex.AddScheduledFunc(time + 1.5, resetCam, () ,"resetCam")
	cam.Cut()

def camTravelling():
	cam=Bladex.GetEntity("Camera")
	cam.Position = 7798, -28297, -25126
	cam.TPos = 17000, -21500, -27000
	opos=cam.Position
	tpos=cam.TPos
	cam.AddCameraNode(0, 4.0, opos[0], opos[1], opos[2])
	cam.SetCameraStartTangentNode(0, 0, -3000.0, 0.0, 0.0)
	cam.SetCameraEndTangentNode(0, 0, 3000.0, 0.0, 0.0)
	cam.AddCameraNode(0, 4.0, 18500, -27000, -30750)
	cam.SetCameraStartTangentNode(0, 1, 0.0, 0.0, 3000.0)
	cam.SetCameraEndTangentNode(0, 1, 0.0, 0.0, -3000.0)
	cam.AddCameraNode(0, 4.0, 20250, -26000, -28000)
	cam.SetCameraStartTangentNode(0, 2, -3000.0, 0.0, 6000.0)
	cam.SetCameraEndTangentNode(0, 2, 3000.0, 0.0, 0.0)
	cam.SType=1
	cam.TType=0
	cam.CameraStartPath(0)
	cam.ChangeNodeFunc=stopCam


def allGemsOk(a=0,b=0) :
	gemRoomPlatform.opentype=Doors.AC_UNIF_DEC
	gemRoomPlatform.o_init_vel=0
	gemRoomPlatform.o_init_displ=3000
	gemRoomPlatform.o_med_vel=-900
	gemRoomPlatform.o_med_displ=6000
	gemRoomPlatform.o_end_vel=0
	gemRoomPlatform.o_end_displ=1000
	gemRoomPlatform.SetWhileOpenSound(maderadesliz1)
	gemRoomPlatform.SetEndOpenSound(maderagolpe1)
	gemRoomPlatform.OpenDoor()


	Bladex.CreateTimer("PlatformDustTimer",1 )
	#gemRoomPlatform.sld_area.TimerFunc=platformDustEvent;
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5, dust.RemueveTierraGen,(16873, -23316+1300, -26828,2000,1500),"dust.RemueveTierraGen 1")

	Bladex.AddScheduledFunc(Bladex.GetTime() + 13.5, dust.RemueveTierraGen,(16873, -13332+1300, -26828,2000,1500) ,"dust.RemueveTierraGen 2")
	Bladex.AddScheduledFunc(Bladex.GetTime() + 14.0, openGemRoomDoor, () ,"openGemRoomDoor")
	#gemRoomPlatform.sld_area.SubscribeToList("PlatformDustTimer")

	time=Bladex.GetTime()+3
	#Bladex.AddScheduledFunc(time + 1.5, platformStartDust, () )
	#Bladex.AddScheduledFunc(time + 2.0, platformStartDust, () )
	Bladex.AddScheduledFunc(time + 0.5, camTravelling, () ,"camTravelling")
	char.QuickFace(1.52093983276)

def useInGemGhostP(gpointer,usefrom):
	global RGemOk
	global GGemOk
	global BGemOk

	if B3DLib.GetXZDistance('Player1', gpointer)> 1750:
		return

	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()

	# chequeando si es la gema roja
	if (gpointer=="GemRGPointer" and inv.CarringObject("GemaR")) :
		Actions.TurnToFaceEntityNow("Player1",gpointer)	# orienta el mu�eco a al gost pointer
		Change.ChangeObject("Player1","GemaR",leaveMovement)	# pone el objeto de la gema en la mano
		Bladex.DeactivateInput()
		RGemOk=1

	# chequeando si es la gema verde
	if (gpointer=="GemGGPointer" and inv.CarringObject("GemaG")) :
		Actions.TurnToFaceEntityNow("Player1",gpointer)	# orienta el mu�eco a al gost pointer
		Change.ChangeObject("Player1","GemaG",leaveMovement)	# pone el objeto de la gema en la mano
		Bladex.DeactivateInput()
		GGemOk=1

	# chequeando si es la gema azul
	if (gpointer=="GemBGPointer" and inv.CarringObject("GemaB")) :
		Actions.TurnToFaceEntityNow("Player1",gpointer)	# orienta el mu�eco a al gost pointer
		Change.ChangeObject("Player1","GemaB",leaveMovement)	# pone el objeto de la gema en la mano
		Bladex.DeactivateInput()
		BGemOk=1

	if (RGemOk==1 and GGemOk==1 and BGemOk==1 ) :
		time=Bladex.GetTime()
		Bladex.AddScheduledFunc(Bladex.GetTime() + 9.0, GemsReallyOk,(),"GemsReallyOk")


def GemsReallyOk():
	ScriptSkip.SkipScriptStart("minagemas")
	char.Position = (13911.5049788, -23088.9345387, -31823.6603442)
	char.Angle    = 5.79084712343
	char.SetOnFloor()
	char.GoTo(17194.632685, -23067.4041519, -27183.3163339)
	char.RouteEndedFunc = allGemsOk
	cam = Bladex.GetEntity("Camera")
	cam.ETarget = "Player1"
	cam.TType = 2
	cam.SType = 0
	cam.Position = (21215, -24721, -31735)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro1"))
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	AuxFuncs.FadeFrom(4.5, 0.0)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para eScene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def eSceneCamFinale(camera,frame) :
	ScriptSkip.SkipScriptEnd()
	GotoMapVars.EndOfLevel()

def eSceneCamRestore(camera,frame) :
	AuxFuncs.FadeTo(5,20)

def eSceneCam() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("mural_final_minaCamera01.cam",0,510)
	cam.AddCameraEvent(410,eSceneCamRestore)
	cam.AddCameraEvent(-1,eSceneCamFinale)
	Scorer.SetVisible(0)

def eSceneAnim() :
	char.Position = 210000,30000,8000
	char.Angle = esceneOrientation
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("final_mina")
	char.SetOnFloor()

def eSceneStart() :
	eSceneCam()
	eSceneAnim()
	ScriptSkip.SkipScriptStart("mimural")

def eSceneFace(ent):
	o = Bladex.GetEntity("Player1")
	o.Face(esceneOrientation)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, eSceneStart, (),"eSceneStart")

def Musicaytexto():
	if char.Kind[0] == "D":

		GameText.WriteText("M5T3")
	else:

		GameText.WriteText("M5T5")

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("finalmina"))
	GotoMapVars.MapText(5,"D_M5_T1")

def eScenePrepare(index, ent):
	global player
	global eScenePlayed
	if (ent<>"Player1") : return
	if (eScenePlayed) : return
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, Musicaytexto, (),"Musicaytexto")
	eScenePlayed=1

	"""
	char = Bladex.GetEntity("Player1")
	char.GoTo( 210000,30000,8000)
	char.RouteEndedFunc = eSceneFace
	"""

	Scorer.SetVisible(0)
	Bladex.DeactivateInput()
	eSceneFace("Player1")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Patachof():
	pass
	#Actions.QuickTurnToFaceEntity("orc0", "Player1")

def CreaOrcoListo():
	darfuncs.UnhideBadGuy("4orc4")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, CorreOrcoListo,(),"CorreOrcoListo")

def CorreOrcoListo():
	o = Bladex.GetEntity("4orc4")
	o.GoTo(8646.97465705, -17107.1787131, -57971.7129489)
	o.RouteEndedFunc = MueveOrcoListo

def MueveOrcoListo(Entity):
	o = Bladex.GetEntity("4orc4")
	o.GoTo(8586.44725557, -17433.8788229, -62196.4230045)

def x1(sectorindex,entityname):

  if entityname=='Player1':
    CreaOrcoListo()
    sectx1.OnEnter=""

def OnFinalTrollDied(entityname):
	#print "OnFinalTrollDied()"
	troll_final.Data.VeryOldImDeadFunc(entityname)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(27,))

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para emboscada.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def StopCameraEmboscada(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()

	Scorer.SetVisible(1)

	ambushork1.Blind = 0
	ambushork1.Deaf = 0

	ambushork2.Blind = 0
	ambushork2.Deaf = 0

	ambushork3.Blind = 0
	ambushork3.Deaf = 0

	Actions.QuickTurnToFaceEntity("MineAmbushOrk1","Player1")
	Actions.QuickTurnToFaceEntity("MineAmbushOrk2","Player1")
	Actions.QuickTurnToFaceEntity("MineAmbushOrk3","Player1")

	Bladex.SetListenerPosition(1)
	Bladex.ActivateInput()

def SonidoOrco(orco,sound):
	ork = Bladex.GetEntity(orco)
	sound.Position = ork.Position
	sound.PlaySound(0)

def Emboscada2():
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("ambush_mine")
	char.Position = -126613,-11533,62396
	char.Angle = 3.14
	char.SetOnFloor()
	#char.LaunchAnmType("ambush_mine")
	Scorer.SetVisible(0)

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ambush_mineCamera01.cam",0,-1)
	cam.AddCameraEvent(-1,StopCameraEmboscada)

	#SoundMatadle.Position = -126613,-11533,62396
	#SoundSalto.Position = -126613,-11533,62396

	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,SonidoOrco,("Player1",SoundSalto),"SonidoOrcoSoundSalto")
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,SonidoOrco,("MineAmbushOrk1",SoundSalto),"SonidoOrcoSoundSalto")
	Bladex.AddScheduledFunc(Bladex.GetTime() + 4.0,SonidoOrco,("Player1",SoundSalto),"SonidoOrcoSoundSalto2")

	ambushork1.UnFreeze()
	ambushork1.Position = ambushork1.Data.Position
	ambushork1.PutToWorld()
	ambushork1.Angle = 3.14

	ambushork1.Wuea = Reference.WUEA_ENDED
	ambushork1.SetTmpAnmFlags(1,1,1,0,5,1)
	ambushork1.LaunchAnimation("Ork_1_ambush_mine")

	ambushork2.UnFreeze()
	ambushork2.Position = ambushork2.Data.Position
	ambushork2.PutToWorld()
	ambushork2.Angle = 3.14

	ambushork2.Wuea = Reference.WUEA_ENDED
	ambushork2.SetTmpAnmFlags(1,1,1,0,5,1)
	ambushork2.LaunchAnimation("Ork_2_ambush_mine")

	ambushork3.UnFreeze()
	ambushork3.Position = ambushork3.Data.Position
	ambushork3.PutToWorld()
	ambushork3.Angle = 3.14

	ambushork3.Wuea = Reference.WUEA_ENDED
	ambushork3.SetTmpAnmFlags(1,1,1,0,5,1)
	ambushork3.LaunchAnimation("Ork_3_ambush_mine")

	Bladex.SetListenerPosition(2)
	Bladex.DeactivateInput()

def Emboscada():
	Emboscada2()

def StartEmboscada(sector,entity):
	if (entity == "Player1"):
		EmboscadaSec.OnEnter = ""
		Emboscada()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-orkos"))

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador4.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador4():

	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador4movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador4.CloseDoor()


def BajaElevador4():

	global enmarcha
	if enmarcha:
		return
	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador4movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador4.OpenDoor()
	enmarcha=1


def EsperaYSubeElevador4():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, SubeElevador4, (),"SubeElevador4")


def Elevador4Arriba():

	global enmarcha
	enmarcha=0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador3.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##DEFINIMOS COMO SER�N LAS FUNCIONES QUE RIJAN LOS MOVIMIENTOS DE BAJAR Y SUBIR

def SubeElevador3():

	global enmarcha
	if enmarcha:
		return

	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador3movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador3.CloseDoor()
	enmarcha=1


def BajaElevador3():

	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador3movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador3.OpenDoor()

########
def Elevador3Arriba():

	global enmarcha
	enmarcha=0
########


## DEFINIMOS LA FUNCION QUE AUTOMATICAMENTE BAJARA EL ELEVADOR 3 SEGUNDOS DESPUES DE DETENERSE EN SU PUNTO MAS ALTO

def EsperaYBajaElevador3():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador3, (),"BajaElevador3")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador2.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador2():

	global enmarcha
	if enmarcha:
		return

	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.CloseDoor()
	enmarcha=1


def BajaElevador2():


	desplazamientos=(500.0, 6250.0, 500.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.OpenDoor()

########
def Elevador2Arriba():

	global enmarcha
	enmarcha=0
########


def EsperaYBajaElevador2():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador2, (),"BajaElevador2")



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevador.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##DEFINIMOS COMO SER�N LAS FUNCIONES QUE RIJAN LOS MOVIMIENTOS DE BAJAR Y SUBIR


### PLAGUE: These funcs are bloated. All of the params (displacement, vector etc.)
###			is supposed to be used on a dynamic object for displacement (and sound).
###			For this elevator, there is no such object ever created. 


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
	columnaelevador.CloseDoor()
	enmarcha=1

def BajaElevador():

	desplazamientos=(500.0, 5850.0, 500.0)
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

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador, (),"BajaElevador")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para musica.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

#################
#################antes de la primera bola
#################

def Musicainicasc(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("suspenselento") )
	ms1.OnEnter=""

def Musicainicascfin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	ms2.OnEnter=""


#################
#################antes de la segunda bola
#################


def Musicaantbich(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("suspenselento") )
	msab1.OnEnter=""

def Musicaantbichfin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	msab2.OnEnter=""

#################
#################desde las piedras que caen hasta la plataforma
#################


def Musicapta1(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("suspenserapido") )
	msab1.OnEnter=""

def Musicapta1fin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	msab2.OnEnter=""

#################
#################antes de las aranas
#################


def Musicapatiotres(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("suspenserapido") )
	msab1.OnEnter=""

def Musicapatiotresfin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	msab2.OnEnter=""


#################
#################segundo recorrido antes del bichito
#################


def Musicaescaleras(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("suspenselento") )
	msab1.OnEnter=""

def Musicaescalerasfin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	msab2.OnEnter=""

#################
#################tercer recorrido tablilla
#################


def Musicaantecaos(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("tablilla") )
	msab1.OnEnter=""

def Musicaantecaosfin(index,ent):
	if (ent<>"Player1") : return
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("emptyloquesea") )
	msab2.OnEnter=""


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertmn.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

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

def AbrePuertaLlaver3():
	puertar3.OpenDoor()

def CierraPuertaLlaver3():
	puertar3.CloseDoor()

def AbrePuertar1():
	puertar1.OpenDoor()


def CierraPuertar1():
	puertar1.CloseDoor()


def AbrePuertabug2():
	puertabug2.OpenDoor()


def CierraPuertabug2():
	puertabug2.CloseDoor()

def AbrePuertar2():
	puertar2.OpenDoor()


def CierraPuertar2():
	puertar2.CloseDoor()

def Abrep1():

	puerta1a.OpenDoor()

def Cierrap1(sectorindex,entityname):
	puerta1a.CloseDoor()
	ChauLava()


def AbrePuertaLlaveen():
	puertaen.OpenDoor()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para propiedades.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

############################################
def Apagala(sectorindex,entityname):
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)


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
	char.Position=78000, -20000, -76000

def IrPosicion2():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-32000, -32000, -28000

def IrPosicion3():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-87635.554464, -25803.8215306, -89447.316

def IrPosicion4():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-133092.556152, -10013.464898, 60822.5704208

def IrPosicion5():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=9000, -6000, -229000

def IrPosicion6():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=52500, -3000, -13500		# inicio


def IrPosicion7():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=94500, -8000, -142000

def IrPosicion8():
	Doors.Restore()
	char=Bladex.GetEntity("Player1")
	char.Position=-34500, -3000, -21000




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para pocimas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def BorraLuz():
	powp_PP.Unlink(luz2_PP)
	luz2_PP.SubscribeToList("Pin")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para piedras.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def BedRockDie(EntityName, VictimName, ImpX, ImpY, ImpZ):
	boludo = Bladex.GetEntity(VictimName)
	boludo.LaunchAnmType("hurt_head")
	boludo.Life = boludo.Life - 10.0

def dropDStoneA():
	o=Bladex.GetEntity("Stone0")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,90,-16000000)
	stone.drop( "Stone0", 0,90,-16000000 )

def dropDStoneB():
	o=Bladex.GetEntity("Stone1")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,90,-23000000)
	stone.drop( "Stone1", 0,90,-23000000 )

def dropDStoneC():
	o=Bladex.GetEntity("Stone2")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,90,-9999999)
	stone.drop( "Stone2", 0,90,-9999999 )

def dropDStoneD():
	o=Bladex.GetEntity("Stone3")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,99,-9990000)
	stone.drop( "Stone3", 0,99,-9990000 )

def dropDStoneE():
	o=Bladex.GetEntity("Stone4")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,99,-9999999)
	stone.drop( "Stone4", 0,99,-9990000 )

def dropDStoneF():
	o=Bladex.GetEntity("Stone5")
	o.SendTriggerSectorMsgs=1
	#o.Impulse(0,-999,-9999999)
	stone.drop( "Stone5", 0,-999,-9999999 )

def dropDMiniStoneA():
	o=Bladex.CreateEntity("MiniStone0","Piedra_08",-1832.387823,-30598.658465,-52009.738656)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Impulse(0,-400,0)

def dropDMiniStoneB():
	o=Bladex.CreateEntity("MiniStone1","Piedra_08",557.640020,-30646.304128,-54069.111998)
	o.Static=0
	o.Scale=0.819544
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Impulse(0,-400,0)

def dropDMiniStoneC():
	o=Bladex.CreateEntity("MiniStone2","Piedra_01",-10568.862164,-33274.310306,-55490.420629)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Impulse(0,-400,-4000)

def dropDMiniStoneD():
	o=Bladex.CreateEntity("MiniStone3","Piedra_01",-7698.870797,-31564.444478,-52154.700939)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Impulse(0,-400,0)

def dropDMiniStoneE():
	o=Bladex.CreateEntity("MiniStone4","Piedra_01",-4070.789465,-31062.063125,-52332.511616)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.Impulse(0,-400,0)

def dropAllStones(secIndex,ent):
	global dropUsed

	if (ent<>"Player1") : return
	if (dropUsed) : return
	DSector.OnEnter = ""

	dropUsed=1
	darfuncs.Temblores(6.0,150)

	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time + 0.1, dropDStoneA, () ,"dropDStoneA")
	Bladex.AddScheduledFunc(time + 1.2, dropDStoneB, () ,"dropDStoneB")
	Bladex.AddScheduledFunc(time + 1.2, dropDStoneC, () ,"dropDStoneC")
	Bladex.AddScheduledFunc(time + 0.1, dropDStoneD, () ,"dropDStoneD")
	Bladex.AddScheduledFunc(time + 3.0, dropDStoneE, () ,"dropDStoneE")
	Bladex.AddScheduledFunc(time + 1.0, dropDStoneF, () ,"dropDStoneF")
	Bladex.AddScheduledFunc(time + 1.1, dropDMiniStoneA, () ,"dropDMiniStoneA")
	Bladex.AddScheduledFunc(time + 1.2, dropDMiniStoneB, () ,"dropDMiniStoneB")
	Bladex.AddScheduledFunc(time + 1.5, dropDMiniStoneC, () ,"dropDMiniStoneC")
	Bladex.AddScheduledFunc(time + 0.3, dropDMiniStoneD, () ,"dropDMiniStoneD")
	Bladex.AddScheduledFunc(time + 1.3, dropDMiniStoneE, () ,"dropDMiniStoneE")

def brokeBridge(trsector_name, ent):
	global bridgeBroken
	if (bridgeBroken==1) : return
	if (ent=="Stone0" or ent=="Stone1" or ent=="Stone2" or ent=="Stone3" or ent=="Stone4" or ent=="Stone5" or ent=="Stone6" ) :
		brokenBridge1.DoBreak((0,-1,0),(-7250, -15500, -58125),(0,0,0))
		brokenBridge2.DoBreak((0,-1,0),(-4750, -15500, -58125),(0,0,0))
		brokenBridge3.DoBreak((0,-1,0),(-1750, -15500, -58125),(0,0,0))

		p1 = -6250,-15750, -59000
		p0 = -6750,-15750, -57000
		p3 = -2500, -15750,-57250
		p2 = -1750, -15750,-58500


		dust0=Bladex.CreateEntity("bridgeDustA", "Entity Particle System D3", p0[0],p0[1],p0[2] )
		dust0.D1= p1[0]-p0[0] ,p1[1]-p0[1] ,p1[2]-p0[2]
		dust0.D2= p2[0]-p1[0] ,p2[1]-p1[1] ,p2[2]-p1[2]
		dust1=Bladex.CreateEntity("bridgeDustb", "Entity Particle System D3", p3[0],p3[1],p3[2] )
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
		bridgeBroken=1
		Bladex.SetTriggerSectorFunc("Tmp", "OnEnter", "" )

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para orcelevador.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def setOElevUnused() :
	global oelInUse
	oelInUse=0

def downOElev() :
	global oelInUse
	colA.OpenDoor()
	colB.OpenDoor()

	displ=(500,10000,500)
	displ_vector=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	init_vel=(0.0,  2000.0, 2000.0)
	end_vel=( 2000.0, 2000.0, 0.0)

	startSnd=(golpeelevador, "", golpeelevador)
	runSnd=(loopelevador, loopelevador, loopelevador)
	stopSnd=("","","")
	Objects.NDisplaceObject(oElev, displ, displ_vector, init_vel, end_vel, startSnd, runSnd, stopSnd, "", (), setOElevUnused, ())


def fight() :
	pOrk = Bladex.GetEntity("platformOrk")
	if (pOrk) :
		pOrk.Deaf = 1
		pOrk.Blind = 1
		EnemyTypes.EnemyDefaultFuncs(pOrk)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5, pOrk.LaunchAnimation,("Ork_jmp_elevator",),"LaunchAnimationOrk_jmp_elevator")
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5, Bladex.ActivateInput,() ,"ActivateInput")
		pOrk.SetActiveEnemy(Bladex.GetEntity("Player1"))


def oElevDownTimer() :
	time = Bladex.GetTime()
	if (orcOut==1) :
		pOrk = Bladex.GetEntity("platformOrk")
		if (pOrk):
			fight()

	Bladex.AddScheduledFunc(time + 4.0, downOElev, () ,"downOElev")

def upOElev():
	global oelInUse

	if (oelInUse) : return
	colA.CloseDoor()
	colB.CloseDoor()

	displ=(500,10000,500)
	displ_vector=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	init_vel=(0.0,  5000.0, 5000.0)
	end_vel=( 5000.0, 5000.0, 0.0)

	startSnd=(golpeelevador, "", golpeelevador)
	runSnd=(loopelevador, loopelevador, loopelevador)
	stopSnd=("","","")
	Objects.NDisplaceObject(oElev, displ, displ_vector, init_vel, end_vel, startSnd, runSnd, stopSnd, "", (), oElevDownTimer, ())

	oelInUse=1

def runOrcAndElev(secIndex,ent):
	global orcOut

	if (orcOut or ent<>"Player1") : return
	orkweapon=Bladex.CreateEntity("platformOrkespad","Espadaromana",0,0,0)
	orkweapon.Weapon=1
	shield=Bladex.CreateEntity("platformOrkescud","Escudo1",0,0,0)
	Sparks.MakeShield("platformOrkescud")
	pOrk=Bladex.CreateEntity("platformOrk","Ork", -94000, -17000, -21000)
	pOrk.Person=1
	pOrk.Angle=-3.14/2
	Actions.TakeObject(pOrk.Name,"platformOrkespad")
	Actions.TakeObject(pOrk.Name,"platformOrkescud")
	pOrk.ActionAreaMin=pow(2,0)
	pOrk.ActionAreaMax=pow(2,0)
	#AniSound.AsignarSonidosCaballeroTraidor(pOrk.Name)
	#EnemyTypes.EnemyDefaultFuncs(pOrk)
	pOrk.Deaf = 0
	pOrk.Blind = 0
	pOrk.SetOnFloor()
	Bladex.DeactivateInput()
	orcOut=1

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1, upOElev,(),"upOElev")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para .py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para tablillas.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def playChorrito(source):
	# sonido del chorrito

	s2=Bladex.CreateSound("../../Sounds/agua-canal.wav","cascada1")
	s2.MaxDistance=40000
	s2.MinDistance=600
	s2.Volume=1.0
	s2.BaseVolume=1.0
	s2.Scale=1.4
	s2.SendNotify=0
	s2.Play(source[0], source[1], source[2],-1)

	return s2

def acidFall(name, source, target, long, time, intensity, density):
	stream=Bladex.CreateEntity(name, "Entity Particle System D1", source[0],source[1],source[2] )
	stream.ParticleType="acidF"
 	stream.YGravity=4400.0
	stream.Friction=0.05
	stream.PPS=100*density
	stream.Velocity=(target[0]-source[0])*intensity,(target[1]-source[1])*intensity,(target[2]-source[2])*intensity
	stream.RandomVelocity=12
	stream.Time2Live=long
	stream.DeathTime=Bladex.GetTime()+time+10
	playChorrito(source)
	return stream

def acidSplash(name, source, time, density):
	splash=Bladex.CreateEntity(name, "Entity Particle System D1", source[0],source[1],source[2] )
	splash.ParticleType="acidF"
 	splash.YGravity=8000.0
	splash.Friction=0.2
	splash.PPS=40*density
	splash.Velocity=0,-1500,0
	splash.RandomVelocity=100
	splash.Time2Live=6
	splash.DeathTime=Bladex.GetTime()+time+10

	return splash

################################ eventos importantes ############################################################

def tSceneDoorDust() :
	doorDust=Bladex.CreateEntity("aDoorDust", "Entity Particle System D2", 138500.0 , 5000.0, -162850)
	doorDust.D= 0.0, 0.0, -5000.0
	doorDust.ParticleType="dustAcidDoor"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=1512
	doorDust.Velocity=750.0, 0.0, 0.0
	doorDust.RandomVelocity=20.0
	doorDust.Time2Live=30
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Coro1"))

def tSceneCloseDoor() :
	tSceneDoor=Doors.CreateDoor("tDoor", (140000,1000,-164000), (0.0,1.0,0.0), 0.0, 9000.0, Doors.OPENED)
	tSceneDoor.closetype=Doors.AC_UNIF_DEC
	tSceneDoor.c_init_vel=3000.0
	tSceneDoor.c_init_displ=1000.0
	tSceneDoor.c_med_vel=3400.0
	tSceneDoor.c_med_displ=7000.0
	tSceneDoor.c_end_vel=0.0
	tSceneDoor.c_end_displ=1000.0
	tSceneDoor.SetWhileCloseSound(maderadeslizTab)
	tSceneDoor.SetEndCloseSound(maderagolpeTab)
	tSceneDoor.CloseDoor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.7, tSceneDoorDust, (),"tSceneDoorDust")

def tAcidFloodTimer(ent,time):
	global aguaSUBE2Lev;
	time = Bladex.GetTime()
	elapsedtime = time-aguaSUBE2FloodStartTime
	aguaSUBE2Lev=aguaSUBE2LevStart+((aguaSUBE2LevEnd-aguaSUBE2LevStart)/aguaSUBE2LevfloodTime)*elapsedtime
	aguaSUBE2.Position=aguaSUBE2P[0],aguaSUBE2Lev,aguaSUBE2P[1]
	if (elapsedtime>aguaSUBE2LevfloodTime) :
		aguaSUBE2.TimerFunc=""
		aguaSUBE2.RemoveFromList("aguaSUBE2Flood")

def tAcidFloodTimerB(ent,time):
	global aguaSUBE1Lev;
	global aAcidDust
	global bAcidDust
	time = Bladex.GetTime()
	elapsedtime = time-aguaSUBE1FloodStartTime
	aguaSUBE1Lev=aguaSUBE1LevStart+((aguaSUBE1LevEnd-aguaSUBE1LevStart)/aguaSUBE1LevfloodTime)*elapsedtime
	aguaSUBE1.Position=aguaSUBE1P[0],aguaSUBE1Lev,aguaSUBE1P[1]
	aAcidDust.Position = aAcidDust.Position[0],aguaSUBE1Lev-30,aAcidDust.Position[2]
	bAcidDust.Position = bAcidDust.Position[0],aguaSUBE1Lev-30,bAcidDust.Position[2]
	#luztab1.Position=luztab1P[0],aguaSUBE1Lev-2000,luztab1P[1]
	#luztab2.Position=luztab2P[0],aguaSUBE1Lev-2000,luztab2P[1]
	#luztab3.Position=luztab3P[0],aguaSUBE1Lev-2000,luztab3P[1]
	#luztab4.Position=luztab4P[0],aguaSUBE1Lev-2000,luztab4P[1]
	#luztab5.Position=luztab5P[0],aguaSUBE1Lev-2000,luztab5P[1]
	if (elapsedtime>aguaSUBE1LevfloodTime  or stopSUBE1Flood ) :
		aguaSUBE1.TimerFunc=""
		aguaSUBE1.RemoveFromList("aguaSUBE2Flood")


def tAcidFlood():
	#print("> Start flood!!")
	global aguaSUBE2FloodStartTime
	aguaSUBE2.TimerFunc=tAcidFloodTimer
	aguaSUBE2.SubscribeToList("aguaSUBE2Flood")
	aguaSUBE2FloodStartTime=Bladex.GetTime()

	Bladex.AddScheduledFunc(aguaSUBE2FloodStartTime+10.0,tAchalay,(),"tAchalay")

# Achalal yuyo ma chu�o! (en Quechua)
def tAchalay():
	CosoRaro = LavaDefDamage.LAVA_AREA()
	CosoRaro.CreateLava ("aguatrucha",106500,-11900-203,-143500, "lava", 0.03 )

	CosoRarox = LavaDefDamage.LAVA_AREA()
	CosoRarox.CreateLava ("AguaTrucha",106500,-11900-203,-186000, "lava", 0.03 )


def tAcidFloodB():
	#print("> Start flood B!!")
	global aguaSUBE1FloodStartTime
	aguaSUBE1.TimerFunc=tAcidFloodTimerB
	aguaSUBE1.SubscribeToList("aguaSUBE2Flood")
	aguaSUBE1FloodStartTime=Bladex.GetTime()


def tAcidFall(ent,Time) :
	#print("tAcidFall(ent,Time)")
	o = Bladex.GetEntity("Player1")

	source = acidfallsource
	target = acidfalltarget
	s=Bladex.CreateEntity("afall", "Entity Particle System D2", source[0], source[1], source[2]-400.0 )
	s.D= 0.0, 0.0, 800.0
	s.ParticleType="acidF"
 	s.YGravity=4400.0
	s.Friction=0.05
	s.PPS=100*3.5
	s.Velocity=(target[0]-source[0])*0.8,(target[1]-source[1])*0.8,(target[2]-source[2])*0.8
	s.RandomVelocity=12
	s.Time2Live=35
	s.DeathTime=Bladex.GetTime()+Time+10

	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time+1.5, tAcidFlood, (), "tAcidFlood")

	o.Angle = 3.14*0.5		# parche para que recupere la orientacion antes de que se note

def tGargolaAStart(ent,Time) :
	global gargaacidDust
	global aAcidDust

	s=acidFall("pbaf2", gargaacidsource, gargaacidtarget, 100, 36000, 0.8, 3.5)
	aAcidDust = acidSplash("ADA", gargaacidDust,36000 , 50)


def tGargolaBStart(ent,Time) :
	global gargbacidDust
	global bAcidDust

	s=acidFall("pbaf3", gargbacidsource, gargbacidtarget, 100, 36000, 0.8, 3.5)
	bAcidDust = acidSplash("ADB", gargbacidDust,36000 , 50)


################################ Camaras y animaciones #########################################################

def tSceneAPosition() :
	#print(">tSceneBPosition()")
	o = Bladex.GetEntity("Player1")
	o.Position = 133531.219,3886.128,-163670.469
	o.SetOnFloor()
	o.Angle = 3.14
#	o.Angle = 3.14*0.5

def tSceneRestoreCam(ent,Time) :
	#print(">tSceneRestoreCam(ent,Time)")
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	tAcidFloodB()
	Bladex.SetListenerPosition(1)

def tSceneAAnim() :
	#print(">tSceneAAnim()")
	o = Bladex.GetEntity("Player1")
	o.SetTmpAnmFlags(1,1,1,0,5,1)
	o.LaunchAnmType("escena_mina_acido")
	o.Position = 133531.219,3886.128,-163670.469
	o.SetOnFloor()

def tSceneACam()  :
	#print(">tSceneACam()")
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("escena_acidcamera01.cam",0,720)
	cam.AddCameraEvent(445,tAcidFall)
	cam.AddCameraEvent(550,tGargolaAStart)
	cam.AddCameraEvent(590,tGargolaBStart)
	cam.AddCameraEvent(-1 ,tSceneRestoreCam)
	Bladex.SetListenerPosition(2)

def tSceneAStartAnim() :
	tSceneAPosition()
	tSceneCloseDoor()
	tSceneAAnim()
	tSceneACam()

def tSceneAFaceAnim(ent) :
	o = Bladex.GetEntity("Player1")
	o.Angle = (3.14*0.5)
	o.SetOnFloor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, tSceneAStartAnim, (),"tSceneAFaceAnim:tSceneAStartAnim")

def tSceneAStart(index, ent) :
	global tSceneAStartFlag
	#print(">tSceneAStart()")

	if (ent<>"Player1") : return
	if (tSceneAStartFlag) : return
	tSceneAStartFlag=1

	ScriptSkip.SkipScriptStart("MineAcido")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, tSceneAStartAnim,(),"tSceneAStart:tSceneAStartAnim")
	tSceneASector.OnEnter=""


def tSceneBPosition() :
	#print(">tSceneBPosition()")
	o = Bladex.GetEntity("Player1")
	o.Position = 116287.258,-18596.377-100,-164280.813
	o.SetOnFloor()
	o.Angle = (3.14*0.5)

def TransfusionTablilla():
	Transfusion=Bladex.CreateEntity("Transfusion", "Entity Particle System D2", 0,0,0)
	Transfusion.Position = rtablilla.Position
	Transfusion.D = char.Position[0]-Transfusion.Position[0],char.Position[1]-Transfusion.Position[1],char.Position[2]-Transfusion.Position[2]

 	Transfusion.ParticleType="Chispas"
	Transfusion.YGravity=0.0
	Transfusion.Friction=0.3
	Transfusion.PPS=1024
	Transfusion.Velocity=40, -40.0, 0.0
	Transfusion.RandomVelocity=9.0
	Transfusion.Time2Live=60
	Transfusion.DeathTime=Bladex.GetTime()+10.0/60.0

	Transfusion=Bladex.CreateEntity("Transfusion", "Entity Particle System D1", 0,0,0)
	Transfusion.Position = rtablilla.Position
	Transfusion.ParticleType="Chispas"
	Transfusion.Friction=0.05
	Transfusion.YGravity=0.0
	Transfusion.PPS=512
	Transfusion.Velocity=40, -40.0, 0.0
	Transfusion.RandomVelocity=9.0
	Transfusion.Time2Live=60
	Transfusion.DeathTime=Bladex.GetTime()+0.25

def AlTipoTablilla():
	Transfusion=Bladex.CreateEntity("Transfusion", "Entity Particle System D1", 0,0,0)
	Transfusion.Position = char.Position
	Transfusion.ParticleType="Chispas"
	Transfusion.Friction=0.05
	Transfusion.YGravity=0.0
	Transfusion.PPS=512
	Transfusion.Velocity=40, -40.0, 0.0
	Transfusion.RandomVelocity=9.0
	Transfusion.Time2Live=60
	Transfusion.DeathTime=Bladex.GetTime()+10.0/60.0



def tTablillaFadeTimer(ent,Time):
	time = Bladex.GetTime()
	elapsedTime = time-tablillaFadeStartTime

	if (elapsedTime>tablillafadetime) :
		Bladex.GetEntity("Player1").GetInventory().LinkLeftHand("None")
		rtablilla.RemoveFromList("tablillaFadeTimer")
		rtablilla.TimerFunc=""
		rtablilla.RemoveFromWorld()
		luztablilla.SubscribeToList("Pin")
		luztablilla.RemoveFromWorld()
		AlTipoTablilla()
	else :
		if (elapsedTime<0.0) : elapsedTime=0.0
		if (elapsedTime>1.0) : elapsedTime=1.0
		coef = elapsedTime/tablillafadetime
		coef = 1.0 - coef
		rtablilla.Alpha = coef
		luztablilla.Intensity =  coef*luztablillaintensity;


def tTablillaFade(index, ent) :
	global tablillaFadeStartTime;
	tablillaFadeStartTime = Bladex.GetTime()
	rtablilla.SubscribeToList("tablillaFadeTimer")
 	rtablilla.TimerFunc=tTablillaFadeTimer;
 	TransfusionTablilla()

def tTablillaDust(ent,Time) :
	doorDust=Bladex.CreateEntity("aTablillaDust", "Entity Particle System D1", rtablilla.Position[0]+100, rtablilla.Position[1]-100, rtablilla.Position[2])
 	doorDust.ParticleType="dustAcidDoor"
	doorDust.YGravity=0.0
	doorDust.Friction=0.3
	doorDust.PPS=112
	doorDust.Velocity=40, -40.0, 0.0
	doorDust.RandomVelocity=7.0
	doorDust.Time2Live=15
	doorDust.DeathTime=Bladex.GetTime()+10.0/60.0

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

def tTakeTablilla(index, ent)  :
	#print(">tTakeTablilla()")
	inv = char.GetInventory()
	inv.AddTablet("Tablilla1")
	inv.LinkLeftHand("Tablilla1")
	#ImprimeDatosTablilla("Tablilla1")


def tSceneBAnim() :
	#print(">tSceneBAnim()")
	o = Bladex.GetEntity("Player1")
	o.Angle = 3.14*0.5
	o.SetTmpAnmFlags(1,1,1,0,5,1,0)
	o.Wuea = Reference.WUEA_ENDED
	o.LaunchAnmType("tablilla_mina")
	o.Position = 116287.258,-18596.377-100,-164280.813
	o.SetOnFloor()
	#Bladex.AddScheduledFunc( Bladex.GetTime()+0.97 ,tTakeTablilla, (),"tTakeTablilla")

def tSceneBRestoreHit(ent) :
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	d=Doors.CreateDoor("tplat1", (100000,-16500,-164700), (1,0,0), 0,11250, Doors.OPENED)
	d.closetype=Doors.AC_UNIF_DEC
	d.c_init_vel=0
	d.c_init_displ=1000
	d.c_med_vel=3000
	d.c_med_displ=9250
	d.c_end_vel=0
	d.c_end_displ=1000
	d.SetWhileCloseSound(maderadesliz1)		# Changed
	d.SetEndCloseSound(PlatSlideFin)		#		-LeadHead
	d.CloseDoor()
	d=Doors.CreateDoor("tplat2", (108000,-16500,-164700), (-1,0,0), 0,4500, Doors.OPENED)
	d.closetype=Doors.AC_UNIF_DEC
	d.c_init_vel=0
	d.c_init_displ=1000
	d.c_med_vel=1000
	d.c_med_displ=2500
	d.c_end_vel=0
	d.c_end_displ=1000
	d.SetWhileCloseSound(PlatSlide2)		# Changed
	d.SetEndCloseSound(maderagolpeTab)		# 		-LeadHead
	d.CloseDoor()

def tSceneBRestoreCam(ent,Time) :
	#print(">tSceneBRestoreCam(ent,Time)")
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	o = Bladex.GetEntity("Player1")
	#o.GoTo(117626.189727, -18664.8, -164264.34366)
	#o.RouteEndedFunc = tSceneBRestoreHit
	tSceneBRestoreHit("Player1")
	Bladex.SetListenerPosition(1)


def tSceneBCam()  :
	#print(">tSceneBCam()")

	tSceneBAnim()
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Kgt_tablilla_minaCamera01.cam",0,360)
	cam.AddCameraEvent(32 , tTakeTablilla)

	GameText.WriteText("M5T2")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("tablillamina"))
	GotoMapVars.MapText(5,"TT")

	cam.AddCameraEvent(75 , tTablillaDust)
	cam.AddCameraEvent(240, tTablillaFade)
	cam.AddCameraEvent(360, tSceneBRestoreCam)
	Bladex.SetListenerPosition(2)


def tSceneBFaceAnim(ent) :
	o = Bladex.GetEntity("Player1")
	o.Angle = (3.14*0.5)
	tSceneBCam()

def tSceneBStartMove()	:
	o = Bladex.GetEntity("Player1")
	#o.GoTo(116287.258,-18596.377-100,-164280.813)
	#o.RouteEndedFunc = tSceneBFaceAnim
	time = Bladex.GetTime()
	time = time + 1.0
	tSceneBPosition()
	tSceneBFaceAnim("")

def FaceTablilla(coso):
	char.QuickFace(1.75432366785)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, GoToRune, ())
	char.RouteEndedFunc = None

def GoToRune():
	print "Hola!!!!!"
	Actions.FreeBothHands("Player1",tSceneBStartMove,(),1)

def tSceneBKeepWeapons(xx):
	char.AnmEndedFunc = None
	char.RouteEndedFunc = FaceTablilla
	if not char.GoTo(116287.258,-18596.377-100,-164280.813):
		char.Position = 116287.258,-18596.377-100,-164280.813
		FaceTablilla("Player1")



def tSceneBStart(index, ent) :
	global stopSUBE1Flood
	global tSceneBStartFlag
	global ChauLavaActivado


	stopSUBE1Flood=1

	if (ent<>"Player1") : return
	if (tSceneBStartFlag) : return
	tSceneBStartFlag=1


	ScriptSkip.SkipScriptStart("MineTablilla")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)

	char.AnmEndedFunc = tSceneBKeepWeapons
	ChauLavaActivado = 1

	###################################################
	# Tablilla para Knight_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'K':
		o             = Bladex.GetEntity('Tablilla1')
		o.Position    =  (115725.582136, -18588.7126934, -164219.464898)
		o.Orientation =  (0.603017628193, 0.286374509335, -0.642498493195, 0.376238107681)



	###################################################
	# Tablilla para Amazon_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'A':
		o             = Bladex.GetEntity('Tablilla1')
		o.Position    =  (115706.147387, -18576.1033253, -164182.266569)
		o.Orientation =  (0.615332365036, 0.354134917259, -0.595730245113, 0.375580012798)


	###################################################
	# Tablilla para Dwarf_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'D':
		o             = Bladex.GetEntity('Tablilla1')
		o.Position    =  (115587.505252, -18278.3880278, -164042.979206)
		o.Orientation =  (0.640779137611, 0.385677814484, -0.570568442345, 0.339273750782)



	###################################################
	# Tablilla para Barbarian_N
	###################################################
	if Bladex.GetEntity('Player1').Kind[0] == 'B':
		o             = Bladex.GetEntity('Tablilla1')
		o.Position    =  (115503.559773, -18760.0163689, -164129.044651)
		o.Orientation =  (0.588673233986, 0.362303763628, -0.638302445412, 0.338776826859)

	tSceneBSector=Bladex.GetSector(115000,-21000,-164000)
	tSceneBSector.OnEnter=None


def ChauLava():
	global ChauLavaActivado

	if ChauLavaActivado:
		aguaSUBE1.Position=(122339.604851, -1316.67860432, -133703.540076)
		ChauLavaActivado = 0


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ultimasbolas.py    **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

######### LANZAMIENTO DE LAS PIEDRAS


def uDropDelMe(ent):
	uBolo =  Bladex.GetEntity(ent)
	uBolo.SubscribeToList("Pin")
	uBolo.RemoveFromWorld()

def uImpulseA():
	"""
	uBoloA.Impulse(0,0,444444)
	uBoloA.Impulse(0,0,444444)
	"""
	pass

def uDropA():
	global uBoloAStartTime

	#----impulse
	stone.drop( "UBolo1", -9999999,0,0 )
	"""
	uBoloA.Impulse(-9999999,0,0)
	uBoloA.Impulse(-9999999,0,0)
	uBoloA.Impulse(-9999999,0,0)
	uBoloA.Impulse(-9999999,0,0)

	#----impulso de seguridad
	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time + 0.6, uImpulseA, () ,"uImpulseA")
	Bladex.AddScheduledFunc(time + 24.0, uDropDelMe, ("UBolo1",) ,"uDropDelMe")
	"""

def uImpulseB():
	"""
	uBoloA.Impulse(0,0,444444)
	uBoloA.Impulse(0,0,444444)
	"""
	pass

def uDropB():
	global uBoloBStartTime

	#----impulse
	stone.drop( "UBolo2", 6154,233040,2321 )
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-2b"))
	"""
	uBoloB.Impulse(6415,233040,2351)
	uBoloB.Impulse(4415,233040,2324)

	#----impulso de seguridad
	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time + 0.6, uImpulseB, () ,"uImpulseB")
	Bladex.AddScheduledFunc(time + 24.0, uDropDelMe, ("UBolo2",),"uDropDelMe")
	"""


def uDrop(index,ent):
	global bolasDropped

	if (bolasDropped==1) : return

	if (ent<>"Player1") : return

	darfuncs.Temblores(6.0,150)

	time = Bladex.GetTime()
	Bladex.AddScheduledFunc(time + 3.6, uDropA, () ,"uDropA")
	Bladex.AddScheduledFunc(time + 3.0, uDropB, () ,"uDropB")

	char = Bladex.GetEntity("Player1")
	TemblorMalditoTerror.Play(char.Position[0], char.Position[1], char.Position[2], 0)

	bolasDropped=1
	uDropSector.OnEnter=""



# especificas para el mapa de vuelta atras
def TieneTablilla():
	import GenFX
	#junto a tablilla
	GenFX.CreateMagicTransport("transp5", (82000,-18400,-164625))
