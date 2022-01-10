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
import Enm_Def
import MusicTool
import ScriptSkip
import Breakings

#####################################################################################
#################################### enemigos.py ####################################
#####################################################################################
def ElArqueroSeDestapaLosOidos():
	Bladex.GetEntity("entraguardia").Deaf = 0

def MuerteesqueletoDeMierda(NombreDelEsqueletoQueMurio):
	global Nukeleto

	Bladex.GetEntity(NombreDelEsqueletoQueMurio).Data.ImDeadFuncPlus(NombreDelEsqueletoQueMurio)
	Nukeleto = Nukeleto - 1
	if Nukeleto == 0:
		Bladex.GetSector(5993.06275304, -1412.8642963, 11477.6074933).OnEnter=x3

def MuerteZombiDeMierda(NombreDelZombiQueMurio):
	global Nukezombi

	Bladex.GetEntity(NombreDelZombiQueMurio).Data.ImDeadFuncPlus(NombreDelZombiQueMurio)
	Nukezombi = Nukezombi - 1
	if Nukezombi == 0:
		sectx6=Bladex.GetSector(70423.7564936, 5884.1021296, 45583.4819898)
		sectx6.OnEnter=x6



def CreaOrcoListo():
	darfuncs.UnhideBadGuy("4ORC")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, CorreOrcoListo,())

def CorreOrcoListo():
	o = Bladex.GetEntity("4ORC")
	o.GoTo(64660.0775465, 5298.15296703, -19302.6592888)
	o.RouteEndedFunc = MueveOrcoListo

def MueveOrcoListo(Entity):
	o = Bladex.GetEntity("4ORC")
	o.GoTo(61230.5556921, 5300.7567276, -19674.879695)


def x1(sectorindex,entityname):

  if entityname=='Player1':
    CreaOrcoListo()
    sectx1.OnEnter=""


def MuerteOrcoDeMierda(ent):
	Bladex.GetEntity(ent).Data.ImDeadFuncPlus(ent)
	sectx2=Bladex.GetSector(82549.2476466, -8213.97187842, -30831.7899736)
	sectx2.OnEnter=x2


def x2(sectorindex,entityname):
	if entityname=='Player1':
		darfuncs.UnhideBadGuy("6ORCb")
		sectx2=Bladex.GetSector(82549.2476466, -8213.97187842, -30831.7899736)
		sectx2.OnEnter=""
def x3(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("KeletoSorpresa1")
		Bladex.GetSector(5993.06275304, -1412.8642963, 11477.6074933).OnEnter=""

def ApareceKeletoKapullo():
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, CorreKeletoKapullo,())

def CorreKeletoKapullo():
	o = Bladex.GetEntity("Keleton1")
	o.GoTo(81181.1000696, -721.514535247, 30691.7782871)
	o.RouteEndedFunc = MueveKeletoKapullo

def MueveKeletoKapullo(Entity):
	o = Bladex.GetEntity("Keleton1")
	o.GoTo(80583.1578282, -719.296426509, 33778.1785987)


def x5(sectorindex,entityname):

  if entityname=='Player1':
    ApareceKeletoKapullo()
    sectx5.OnEnter=""



def KeletosLlave():
	darfuncs.UnhideBadGuy("Keleton4")
	darfuncs.UnhideBadGuy("Keleton5")

def x7(sectorindex,entityname):

	if entityname=='Player1':
		KeletosLlave()
		sectx7.OnEnter=""

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul


def MueveTodos():
	for enemigo in listaeskeletos:
		GoToMul(enemigo.Name)


def KreaKeletos():
	darfuncs.UnhideBadGuy("Keleton2")
	darfuncs.UnhideBadGuy("Keleton3")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, MueveTodos,())


def x6(sectorindex,entityname):

	if entityname=='Player1':
		KreaKeletos()
		sectx6.OnEnter=""

#####################################################################################
#################################### Pendulos.py ####################################
#####################################################################################


def CreatePendulo(Name):
	Pendulo = Bladex.GetEntity(Name)
	Pendulo.FireParticleType = "LargeFire"

	Pen = def_class.PENDULO(Pendulo)
	Pendulo.Data = Pen
	Pen.Pendulo = Pendulo
	Pen.Luz=AuxFuncs.GetSpot(Pendulo)
	Pen.Luz.Intensity = 0.0
	Pen.Luz.Precission=0.15
#	Pen.Luz.CastShadows=0
	Pen.Fire=AuxFuncs.GetFire(Pendulo)
	Pen.Fire.Intensity = 20.0

	Pen.sound1=Sounds.CreateEntitySound('../../Sounds/Fire-curtains.wav', 'SonidoPendulo')
	Pen.sound1.Volume=1.0
	Pen.sound1.MinDistance=5000
	Pen.sound1.MaxDistance=30000
	Pen.sound2=Sounds.CreateEntitySound('../../Sounds/fireball-swing.wav', 'SonidoPendulo')
	Pen.sound2.Volume=1.0
	Pen.sound2.MinDistance=5000
	Pen.sound2.MaxDistance=30000
	Pen.sound3=Sounds.CreateEntitySound('../../Sounds/Flame-hole.wav', 'SonidoGolpe')
	Pen.sound3.Volume=1.0
	Pen.sound3.MinDistance=10000
	Pen.sound3.MaxDistance=35000

	return Pen


def ExplosionPendulo(golpeado,golpeador,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	pos = Bladex.GetEntity("Player1").Position

	P1.sound3.Position = pos
	P1.sound3.PlaySound(0)

	llamarada=Bladex.CreateEntity("llamaradagol", "Entity Particle System D1", pos[0],pos[1],pos[2])
	llamarada.ParticleType="Explode"
	llamarada.YGravity=-10000.0
	llamarada.Friction=0.12
	llamarada.PPS=50
	llamarada.Velocity=0.0, 0.0, 0.0
	llamarada.RandomVelocity=30.0
	llamarada.Time2Live=10
	llamarada.DeathTime = Bladex.GetTime() + 0.2


def Desactivar_Pendulos(sector,Entity):
	if Entity == "Player1":
		char = Bladex.GetEntity("Player1")
		Pendulo_Sector2.OnEnter = ""
		P1.Stop()
		char.HitFunc = ExHitFunc



def Activar_Pendulos(sector,Entity):
	global ExHitFunc

	if Entity == "Player1":
		char = Bladex.GetEntity("Player1")
		Pendulo_Sector1.OnEnter = ""
		P1.Play()

		ExHitFunc = char.HitFunc
		char.HitFunc = ExplosionPendulo


def PararPendulos(sector,entity):
	if (entity == "Player1"):
		if P1.Activado:
			P1.Stop()
			Pendulo_Sector1.OnEnter = Activar_Pendulos

#####################################################################################
#################################### Pinchos.py ####################################
#####################################################################################

def DeactivatePinchoOnHit (EntityName, VictimName, ImpX, ImpY, ImpZ):
	# Deactivate pincho
	pincho = Bladex.GetEntity(EntityName)
	pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
	pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)

def ActivatePinchos():
	for i in range(181,255):
		# Activate pincho
		pincho=Bladex.GetEntity("Pincho"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,1,0)
		pincho.InflictHitFunc= DeactivatePinchoOnHit

def DeactivatePinchos():
	for i in range(181,255):
		# Activate pincho
		pincho=Bladex.GetEntity("Pincho"+`i`)
		pincho.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		pincho.MessageEvent(Reference.MESSAGE_SETSTATICWEPONMODE,0,0)


#####################################################################################
#################################### Positions.py ####################################
#####################################################################################

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position= -38000,5000,-41500		# inicio
	Doors.Restore()

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=57000,3000,-18500			# delante de la torre
	Doors.Restore()

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=19500,-3000,-1000			# dentro del templo
	Doors.Restore()

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=78500,4000,0			# en el cementerio
	Doors.Restore()

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=4500, -4000, -1250		# sala rota
	Doors.Restore()

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=121500, 3000, -8500		# estatuilla
	Doors.Restore()

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=33500, 3000, 12000		# pendulo
	Doors.Restore()

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=97000, -4000, 21000		# pinchos
	Doors.Restore()

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=67789, 5946, 37113
	Doors.Restore()




#####################################################################################
#################################### Puertas.py ####################################
#####################################################################################

def Abrereja1():

	desplazamientos=(2000.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja1():

	desplazamientos=(2000.0, 2000.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abreptatorre1():
	ptatorre1.OpenDoor()

def Cierraptatorre1():
	ptatorre1.CloseDoor()


def AbrePuertaLlave1():
	Lorenzo1.OpenDoor()

def CierraPuertaLlave1():
	Lorenzo.CloseDoor()

def Abrepuertatemplo():
	puertatemplo.OpenDoor()

def Cierrapuertatemplo():
	puertatemplo.CloseDoor()

def AbrePuertaLlave2():
	puertaZ2.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def CierraPuertaLlave2():
	puertaZ2.CloseDoor()

def CierraPuertaZ3():
	puertaZ3.CloseDoor()


def AbrePuertaz4(sectorindex,entityname):
	if entityname=="Player1":
		puertaz4.OpenDoor()
		serT.OnEnter=""
def Abrerejasi1():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejasi2():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejas():
	Abrerejasi1()
	Abrerejasi2()

def Cierrarejasi1():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 8000)

	#sonidos asociados a la puerta-objeto rejasi1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejasi2():

	desplazamientos=(2000.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 8000)

	#sonidos asociados a la puerta-objeto rejasi1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejas():
	Cierrarejasi1()
	Cierrarejasi2()


def Cierralados():
	global ladosCerrados
	if (ladosCerrados==0) :
		Cierrarejasi1()
		Cierrarejasi2()
		ladosCerrados=1

def EntroEnTriggerSector(trsector_name, entity_name):
	#print("entidad:"+entity_name+", en sector"+trsector_name);
	if (entity_name<>"Player1") : return
	Cierralados()

def AbrePuertata():
	puertata1.OpenDoor()
	puertata1.OnEndOpenFunc = AbrePuertataAditional


def AbrePuertataAditional():
	puertata2.OpenDoor()

def AbrerejaF1():

	desplazamientos=(2000.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rejaF1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejaF1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def LineaPolvo():
	polvo=Bladex.CreateEntity("Polvo2", "Entity Particle System D2", 28125,-600,-1500)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 0,-4400,0
	polvo.ParticleType="DustDoor"
	polvo.YGravity=-700.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def AbrePuertadobleT():
	puertadobleT1.OpenDoor()
	puertadobleT2.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def CierraPuertadobleT():
	puertadobleT1.CloseDoor()
	puertadobleT2.CloseDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("templo") )

def AbrePuertac1():
	puertac1.OpenDoor()

def CierraPuertac1():
	puertac1.CloseDoor()

def AbrePuertag2():
	puertag2.OpenDoor()

def CierraPuertag2():
	puertag2.CloseDoor()

def ChangeChapuzaFunctionFlag():
	global ChapuzaFunctionFlag
	ChapuzaFunctionFlag = 0

def ChapuzaFunction(delta):
	global ChapuzaFunctionFlag
	if ChapuzaFunctionFlag:
		Bladex.GetEntity("pucheroT").Move(0,0,delta)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.000,ChapuzaFunction,(-delta,))


def BajaSarcofago():
	global ChapuzaFunctionFlag

	ChapuzaFunctionFlag = 1
	sarcofago1.OpenDoor()
	sarcofago2.OpenDoor()
	sarcofago3.OpenDoor()
	sarcofago4.OpenDoor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.001,ChapuzaFunction,(1,) )
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0,ChangeChapuzaFunctionFlag,() )



def SubeSarcofago():
	sarcofago1.CloseDoor()
	sarcofago2.CloseDoor()
	sarcofago3.CloseDoor()
	sarcofago4.CloseDoor()


def AbrePuertaCE1():
	puertaCE1.OpenDoor()

def CierraPuertaCE1():
	puertaCE1.CloseDoor()

#####################################################################################
####################################        .py  ####################################
#####################################################################################

def RemueveTierraGen2(pos, v1, v2, v3):
	tierra=Bladex.CreateEntity("TierraRemoviendose", "Entity Particle System D3", pos[0]+v1[0], pos[1]-900.0, pos[2]+v1[2])
	tierra.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	tierra.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	tierra.ParticleType="Tierra2x"
	tierra.PPS=64
	tierra.YGravity=200.0
	tierra.Friction=0.1
	tierra.Velocity=0.0, -400.0, 0.0
	tierra.RandomVelocity=15.0
	tierra.Time2Live=64
	tierra.DeathTime=Bladex.GetTime()+2.0

def SaltaTierraGen2(enmgen):
	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=B3DLib.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)

	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltatie.ParticleType="Tierra3x"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=60
	saltatie.DeathTime=Bladex.GetTime()+10.0/60.0

	saltati2=Bladex.CreateEntity("TierraSaltando2", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltati2.ParticleType="Tierra2x"
	saltati2.PPS=128
	saltati2.YGravity=200.0
	saltati2.Friction=0.1
	saltati2.Velocity=0.0, -300.0, 0.0
	saltati2.RandomVelocity=15.0
	saltati2.Time2Live=32
	saltati2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveTierraGen2, (pos, v1, v2, v3))

#####################################################################################
#################################### cementerio.py ##################################
#####################################################################################

def Abrir(recibe1):
	#print ("Muertos")
	AbrePuertadoble()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def CreaSkeletoDichoso(o):
	pass
	#o.Level = 5
	#o.ActionAreaMin=pow(2,14)
	#o.ActionAreaMax=pow(2,15)

def EntroEnTriggerSector(trsector_name, entity_name):
	#print("entidad:"+entity_name+", en sector"+trsector_name);
	if (entity_name<>"Player1") : return
	generadorT1.GenerateEnemy()
	Bladex.RemoveTriggerSectorFunc(trsector_name, "OnEnter")
	CierraPuertaLlave2()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("cementerio") )

#####################################################################################
#################################### tumbarey.py ####################################
#####################################################################################

def AbrePuertadoble():
	puertadoble1.OpenDoor()
	puertadoble2.OpenDoor()

def CierraPuertadoble():
	puertadoble1.CloseDoor()
	puertadoble2.CloseDoor()

def Descubre():

	escalon1a.OpenDoor()
	escalon3a.CloseDoor()



def Tapa():

	escalon1a.CloseDoor()
	escalon3a.OpenDoor()
#####################################################################################
####################################  bgates.py  ####################################
#####################################################################################

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
	global vidapuertaA


	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta


	bgateA1.DoBreak((0,0,2.0), (31000,-2000,53875), (0.0, 0.0, 0.0))
	bgateA2.DoBreak((0,0,4.0), (32000,-2000,53875), (0.0, 0.0, 0.0))

	p0 = 30250,-600,53750
	p1 = 30250,-3800,53750
	p2 = 32750,-600,53750
	p3 = 32750,-3800,53750

	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)

	bgateA.OnHit = ""

	break_sound.Position = px,py,pz
	break_sound.PlaySound(0)


def revientaPuertaB(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global vidapuertaB

	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta

	bgateB1.DoBreak((0, 0.0, 6), (px, py, pz), (0.0, 0.0, 0.0))
	bgateB2.DoBreak((0, 0.0, 6), (px, py, pz), (0.0, 0.0, 0.0))

	p0 = 40500,-600,53750
	p1 = 40500,-3800,53750
	p2 = 43000,-600,53750
	p3 = 43000,-3800,53750

	dustTriangle("rppolvo3",p0,p1,p2)
	dustTriangle("rppolvo4",p3,p1,p2)

	bgateB.OnHit = ""

	break_sound.Position = px,py,pz
	break_sound.PlaySound(0)

#####################################################################################
####################################  twoskel.py ####################################
#####################################################################################

def tsSkelBOut():
	tsSkeletonB.GoTo(31500,-3000,43000)
	tsSkeletonB.RouteEndedFunc = tsSkelActiv

def tsSkelActiv(ent):
	skel = Bladex.GetEntity(ent)
	skel.Blind = 0
	skel.Deaf = 0

def tsSkelAOut():
	tsSkeletonA.GoTo(41500,-3000,43000)
	tsSkeletonA.RouteEndedFunc = tsSkelActiv




def tsOpenDoorA():
	tsDoorA.opentype=Doors.AC_UNIF_DEC
	tsDoorA.o_init_vel=0.0
	tsDoorA.o_init_displ=400.0
	tsDoorA.o_med_vel=-800.0
	tsDoorA.o_med_displ=3000.0
	tsDoorA.o_end_vel=0.0
	tsDoorA.o_end_displ=300.0
	tsDoorA.SetWhileOpenSound(tsmaderadesliz)
	tsDoorA.SetEndOpenSound(tsmaderagolpe)
	tsDoorA.OpenDoor()
	Bladex.AddScheduledFunc( Bladex.GetTime()+2.0, tsSkelAOut , () )

def tsOpenDoorB():
	tsDoorB.opentype=Doors.AC_UNIF_DEC
	tsDoorB.o_init_vel=0.0
	tsDoorB.o_init_displ=400.0
	tsDoorB.o_med_vel=-800.0
	tsDoorB.o_med_displ=3000.0
	tsDoorB.o_end_vel=0.0
	tsDoorB.o_end_displ=300.0
	tsDoorB.SetWhileOpenSound(tsmaderadesliz)
	tsDoorB.SetEndOpenSound(tsmaderagolpe)
	tsDoorB.OpenDoor()

	Bladex.AddScheduledFunc( Bladex.GetTime()+2.0, tsSkelBOut , () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+10.0, tsOpenDoorA , () )


def tsStart(index,ent):
	global tsStarted
	if (ent<>"Player1") : return
	if (tsStarted) : return
	tsStarted=1
	Bladex.AddScheduledFunc( Bladex.GetTime()+1.0, tsOpenDoorB, () )

#####################################################################################
#################################### WallSkel.py ####################################
#####################################################################################

def wsDustTri(name,a,b,c):
	doorDust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2])
 	doorDust.D1= b[0]-a[0], b[1]-a[1], b[2]-a[2]
 	doorDust.D2= c[0]-a[0], c[1]-a[1], c[2]-a[2]
	doorDust.ParticleType="wsarenadust"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=1112
	doorDust.Velocity=0.0, -210.0, 0.0
	doorDust.RandomVelocity=20.0
	doorDust.Time2Live=30
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0

def wsWakeUp() :
	wsSkeleton.Blind=0
	wsSkeleton.Deaf=0

def wsStart(index, ent) :
	global wsStarted
	if (ent<>"Player1") : return
	if (wsStarted==1) : return
	wsStarted=1

	wsWall.DoBreak((4.2, 0.0, 0.0), (56375,-2500,56625), (0.0, 0.0, 0.0))
	a = 56500, -1000, 57750
	b = 56500, -3600, 57750
	c = 56500, -1000, 55750
	d = 56500, -3600, 55750
	wsDustTri("wsa1",a,b,c)
	wsDustTri("wsa2",b,c,d)

	Bladex.AddScheduledFunc( Bladex.GetTime()+2.0, wsWakeUp , () )

#####################################################################################
####################################  templo.py  ####################################
#####################################################################################


def deKeletum(name):
	global NumKeletumVitaEst
	#print "Quedan",NumKeletumVitaEst
	NumKeletumVitaEst = NumKeletumVitaEst - 1
	if NumKeletumVitaEst == 0:
		AbrePuertadobleT()
	Bladex.GetEntity(name).Data.ImDeadFuncX(name)

def AfterSkeletonJump(EntityName):
	print "------"+EntityName+"------"
	if EntityName=="SKLt1":
		Bladex.GetEntity(EntityName).Position = (14220.4952226, -1764.23495981, 11949.6976356)
		Bladex.GetEntity(EntityName).SetOnFloor()
		Bladex.GetEntity(EntityName).GoTo(16373, -1471, 8066)
	if EntityName=="SKLt2":
		Bladex.GetEntity(EntityName).Position = (24811.5373954, -1764.23495981, 11949.6976356)
		Bladex.GetEntity(EntityName).SetOnFloor()
		Bladex.GetEntity(EntityName).GoTo(21627, -1465, 8925)
	if EntityName=="SKLt3":
		Bladex.GetEntity(EntityName).Position = (14220.4952226, -1760.28262453, -15431.2928818)
		Bladex.GetEntity(EntityName).SetOnFloor()
		Bladex.GetEntity(EntityName).GoTo(16349, -1465, -11728)
	if EntityName=="SKLt4":
		Bladex.GetEntity(EntityName).Position = (24811.5373954, -1760.28262453, -15431.2928818)
		Bladex.GetEntity(EntityName).SetOnFloor()
		Bladex.GetEntity(EntityName).GoTo(21745, -1465, -10449)



def Abretelas2():
    EsqueletSec4.DoBreak( (-100,0,0), (9750, 4000, -1500), (0,0,0) )
    pers=Bladex.GetEntity("SKLt4")
    EnemyTypes.EnemyDefaultFuncs(pers)
    pers.PutToWorld()
    pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
    pers.Wuea = Reference.WUEA_ENDED
    pers.LaunchAnimation("Ork_jmp_elevator")
    pers.Data.ImDeadFuncX = pers.ImDeadFunc
    pers.ImDeadFunc       = deKeletum
    Bladex.AddScheduledFunc(Bladex.GetTime()+2.15, AfterSkeletonJump,(pers.Name,))





def Abretelas1():
    EsqueletSec3.DoBreak( (100,0,0), (9750, 4000, -1500), (0,0,0) )
    pers=Bladex.GetEntity("SKLt3")
    EnemyTypes.EnemyDefaultFuncs(pers)
    pers.PutToWorld()
    Bladex.AddScheduledFunc(Bladex.GetTime()+10, Abretelas2,())
    pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
    pers.Wuea = Reference.WUEA_ENDED
    pers.LaunchAnimation("Ork_jmp_elevator")
    pers.Data.ImDeadFuncX = pers.ImDeadFunc
    pers.ImDeadFunc = deKeletum
    Bladex.AddScheduledFunc(Bladex.GetTime()+2.15, AfterSkeletonJump,(pers.Name,))



def Abretelas0():
    EsqueletSec2.DoBreak( (-100,0,0), (9750, 4000, -1500), (0,0,0) )
    pers=Bladex.GetEntity("SKLt2")
    EnemyTypes.EnemyDefaultFuncs(pers)
    pers.PutToWorld()
    Bladex.AddScheduledFunc(Bladex.GetTime()+10, Abretelas1,())
    pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
    pers.Wuea = Reference.WUEA_ENDED
    pers.LaunchAnimation("Ork_jmp_elevator")
    pers.Data.ImDeadFuncX = pers.ImDeadFunc
    pers.ImDeadFunc = deKeletum
    Bladex.AddScheduledFunc(Bladex.GetTime()+2.15, AfterSkeletonJump,(pers.Name,))


def Abretelas(sectorindex,entityname):
   global ActivaLosEsqueletos
   if ActivaLosEsqueletos:
          if entityname == "Player1":
            EsqueletSec1.DoBreak( (100,0,0), (9750, 4000, -1500), (0,0,0) )
            pers=Bladex.GetEntity("SKLt1")
            EnemyTypes.EnemyDefaultFuncs(pers)
            pers.PutToWorld()
            Bladex.AddScheduledFunc(Bladex.GetTime()+10, Abretelas0,())
            SectorEsqueletosAC.OnEnter = ""
            pers.Wuea = Reference.WUEA_ENDED
            pers.SetTmpAnmFlags(1,1,1,0,5,1,0)
            pers.LaunchAnimation("Ork_jmp_elevator")
            pers.Data.ImDeadFuncX = pers.ImDeadFunc
            pers.ImDeadFunc = deKeletum
            CierraPuertadobleT()
            Cierrapuertatemplo()
            Bladex.AddScheduledFunc(Bladex.GetTime()+2.15, AfterSkeletonJump,(pers.Name,))


#####################################################################################
#################################### generador.py ###################################
#####################################################################################

def ActivaEnemigosFetichePuesto():
	global fetichonKK
	if fetichonKK==0:
		fetichonKK = 1
		#1
		Espada1r=Bladex.CreateEntity("TombHacha1r","Espadaelfica",0,0,0,"Weapon")
		escudo=Bladex.CreateEntity("TombEscudo1r","Escudo2",0,0,0,"Weapon")
		Sparks.MakeShield("TombEscudo1r")
		Breakings.SetBreakableWS("TombEscudo1r")
		Breakings.SetBreakableWS("TombHacha1r")

		pers=Bladex.CreateEntity("1rSKL","Skeleton",12507.5270023, -8458.79769897, -14263.12,"Person")
		pers.Level=8
		pers.Angle=1.5
		Actions.TakeObject(pers.Name,"TombHacha1r")
		Actions.TakeObject(pers.Name,"TombEscudo1r")
		#pers.ActionAreaMin=pow(2,15)
		#pers.ActionAreaMax=pow(2,0)
		EnemyTypes.EnemyDefaultFuncs(pers)
		#AniSound.AsignarSonidosOrco('1rSKL')

		#2
		Espada2r=Bladex.CreateEntity("TombHacha2r","Espadaelfica",0,0,0,"Weapon")
		escudo=Bladex.CreateEntity("TombEscudo2r","Escudo2",0,0,0,"Weapon")
		Sparks.MakeShield("TombEscudo2r")
		Breakings.SetBreakableWS("TombEscudo2r")
		Breakings.SetBreakableWS("TombHacha2r")

		pers=Bladex.CreateEntity("2rSKL","Skeleton",5865.50532924, -8475.03963992, -12938.01,"Person")
		pers.Level=8
		pers.Angle=1.5
		Actions.TakeObject(pers.Name,"TombHacha2r")
		Actions.TakeObject(pers.Name,"TombEscudo2r")
		#pers.ActionAreaMin=pow(2,15)
		#pers.ActionAreaMax=pow(2,0)
		EnemyTypes.EnemyDefaultFuncs(pers)
		#AniSound.AsignarSonidosOrco('2rSKL')

		#3
		Espada3r=Bladex.CreateEntity("TombHacha3r","Espadaelfica",0,0,0,"Weapon")
		escudo=Bladex.CreateEntity("TombEscudo3r","Escudo2",0,0,0,"Weapon")
		Sparks.MakeShield("TombEscudo3r")
		Breakings.SetBreakableWS("TombEscudo3r")
		Breakings.SetBreakableWS("TombHacha3r")

		pers=Bladex.CreateEntity("3rSKL","Skeleton",13118.739806, -8477.75714068, 11387.66,"Person")
		pers.Level=8
		pers.Angle=1.5
		Actions.TakeObject(pers.Name,"TombHacha3r")
		Actions.TakeObject(pers.Name,"TombEscudo3r")
		#pers.ActionAreaMin=pow(2,15)
		#pers.ActionAreaMax=pow(2,0)
		EnemyTypes.EnemyDefaultFuncs(pers)


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
	#pos=generadorT1x.Points[0].Position
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

def ActivateGen1o(Sector,Entity):
	if Entity == "Player1":
		generadorT1x.GenerateEnemy()
		SecGen1o.OnEnter = ""

def ActivateGen2(Sector,Entity):
	if Entity == "Player1":
		generadorT2.GenerateEnemy()
		SecGen2.OnEnter = ""


def ActivativaGeneradoresFeticho():

	darfuncs.EnterSecEvent(32000, -2000, 27750,generadorT2.GenerateEnemy)
	darfuncs.EnterSecEvent(47500, -2000, 17000,generadorT2.GenerateEnemy)
	SecGen1o.OnEnter = ActivateGen1o



def acAreafuncT2(pers):
	pers.ActionAreaMin=pow(2,30)
	pers.ActionAreaMax=1<<31


def acAreafuncT1x(pers):
	pers.ActionAreaMin=pow(2,16)
	pers.ActionAreaMax=pow(2,17)

#####################################################################################
#################################### fetiche.py ####################################
#####################################################################################
def GotFetiche():
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	obj = inv.GetSelectedObject()
	return obj == "Fetiche1"


def PutFetiche(ent,place):
	global fetiche_located
	global hand
	global o_hand
	Bladex.ActivateInput()

	if (fetiche_located == 0):
		char = Bladex.GetEntity("Player1")
		inv = char.GetInventory()
		obj = inv.GetSelectedObject()
		if (obj == "Fetiche1"):
			fetiche_located = 1
			Actions.QuickTurnToFaceEntity ("Player1","PunteroFetiche")

			if not char.InvRight:
				GetFetiche("Player1")
			else:
				if Actions.IsRightHandStandardObject(char.Name):
					if Actions.TryDropRight("Player1"):
						Actions.DropReleaseEventHandler("Player1", "DropRightEvent")
					if not char.InvRight:
						GetFetiche("Player1")
				else:
					char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
					#char.AddAnmEventFunc("ChangeREvent",GetFetiche)
					char.Wuea = Reference.WUEA_ENDED
					char.LaunchAnmType("Chg_r")
					o_hand = char.InvRight
					hand = 1
					char.AnmEndedFunc=GetFetiche

def GetFetiche(entity):
	char = Bladex.GetEntity(entity)
	#char.LaunchAnmType("Chg_r")
	#char.AddAnmEventFunc("ChangeREvent",GetingFetiche)
	char.AddAnmEventFunc("ChangeRLEvent",GetingFetiche)
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("Chg_r_l")


def GetingFetiche(entity,event):
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	inv.LinkRightHand("Fetiche1")
	char.AnmEndedFunc=PutingFetiche

def PutingFetiche(entity):
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("Fire1")
	char.AddAnmEventFunc("SetAlightEvent",FeticheLocated)
	ActivaEnemigosFetichePuesto()

def SetupPutFetiche(ent,place):
	if GotFetiche():
		Bladex.DeactivateInput()
		Actions.FreeBothHands("Player1",PutFetiche,(ent,place))


def ActivateLever(lever,s):
	global levers_activates

	if (levers_activates <> 0):
	 if (levers_activates <> lever):
		LeversActivateds()
	else:
		levers_activates = lever
def FeticheLocated(entity,event):
	global hand
	global chapu_flag
	if chapu_flag:
		chapu_flag = 0
		char = Bladex.GetEntity("Player1")
		inv = char.GetInventory()

		inv.LinkRightHand("None")

		if (hand == 1):
			hand = 0
			char.AnmEndedFunc=ChangeWeapon

		inv.RemoveObject("Fetiche1")

		ff.Position = (37326.822380,-2032.869097,-1484.375504)
		ff.Orientation = (0.504344,0.504344,-0.495618,0.495618)
		ff.Static = 1
		punterofetiche.Static = 1

		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("coro2.2") )
		darfuncs.LaunchMaxCamera("puertas_idoloCamera01.cam",0,-1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, puerta1.OpenDoor,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, puerta2.OpenDoor,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, puertaZ3.OpenDoor,())

def ChangeWeapon(entity):
	char = Bladex.GetEntity(entity)
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("Chg_r")
	char.AddAnmEventFunc("ChangeREvent",Toggle)

def Toggle(ent,event):
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	inv.LinkRightHand(o_hand)

def LeversActivateds():
	puerta3.OpenDoor()
	puerta4.OpenDoor()

def MusicayTexto2():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("fetichetomb"))
	GameText.WriteText("M7T2")

def useInGhostFetiche(gpointer,usefrom):
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,MusicayTexto2,())

#####################################################################################
#################################### tScene.py ####################################
#####################################################################################

def PlaySound(sonido):
	sonido.Position = char.Position
	sonido.PlaySound(0)

def SetSoundsEsfuerzo(type):
	global sonido_esfuerzo1
	global sonido_esfuerzo2

	if type == "K":
		sonido_esfuerzo1=Sounds.CreateEntitySound("../../Sounds/esfuerzo-barb-golpe-atras.wav","sonido_esfuerzo1")
		sonido_esfuerzo2=Sounds.CreateEntitySound("../../Sounds/esfuerzo-barb-largo.wav","sonido_esfuerzo2")
	if type == "A":
		sonido_esfuerzo1=Sounds.CreateEntitySound("../../Sounds/esfuerzo-mediano-amz.wav","sonido_esfuerzo1")
		sonido_esfuerzo2=Sounds.CreateEntitySound("../../Sounds/esfuerzo-largo-amz.wav","sonido_esfuerzo2")
	if type == "B":
		sonido_esfuerzo1=Sounds.CreateEntitySound("../../Sounds/esfuerzos_barb_largo_2.wav","sonido_esfuerzo1")
		sonido_esfuerzo2=Sounds.CreateEntitySound("../../Sounds/esfuerzos_barb_corto_8.wav","sonido_esfuerzo2")
	if type == "D":
		sonido_esfuerzo1=Sounds.CreateEntitySound("../../Sounds/enano-esfuerzos.wav","sonido_esfuerzo1")
		sonido_esfuerzo2=Sounds.CreateEntitySound("../../Sounds/enano-esfuerzo3.wav","sonido_esfuerzo2")
	else:
		return


	sonido_esfuerzo1.Volume = 0.7
	sonido_esfuerzo1.MaxDistance=1000000.0
	sonido_esfuerzo1.MinDistance=900000.0

	sonido_esfuerzo2.Volume = 0.7
	sonido_esfuerzo2.MaxDistance=1000000.0
	sonido_esfuerzo2.MinDistance=900000.0


def SndPiedra(ent,Time):
	_SndPiedra.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def SndPiedraHit(ent,Time):
	_SndPiedraHit.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def tLaunchPersAnim() :
	global tCharAngle
	char = Bladex.GetEntity("Player1")

	if char.Kind[0] == "K":
		char.Position = 19354 , 6361, 358
	if char.Kind[0] == "A":
		char.Position = 19354 , 6361, 158
	if char.Kind[0] == "D":
		char.Position = 19354 , 6361, 450
	if char.Kind[0] == "B":
		char.Position = 19354 , 6361, 350
	char.Angle = tCharAngle
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("abrirsarcofago")
	char.SetOnFloor()

	Bladex.AddScheduledFunc(Bladex.GetTime() + TUMBA_ESFUERZO1,PlaySound,(sonido_esfuerzo1,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + TUMBA_ESFUERZO2,PlaySound,(sonido_esfuerzo2,))


#def tLaunchTombAnimStop():
# 	tLapida.TurnOff()
#	Bladex.AddScheduledFunc(Bladex.GetTime(), tLaunchTombAnimStopPoneStatic,())

#def tLaunchTombAnimStopPoneStatic():
#	tLapida.RemoveFromWorld()
#	tLapida2             = Bladex.CreateEntity(tLapida.Name+"1",tLapida.Kind,tLapida.Position[0],tLapida.Position[1],tLapida.Position[2],"Physic")
#	tLapida2.Orientation = tLapida.Orientation
#	tLapida2.Scale       = tLapida.Scale





#def tLaunchTombAnim() :
#	tLapida.Actor=1
#	tLapida.Animation="Tapa_sarcofago"
#	tLapida.SendSectorMsgs=0
#	tLapida.TurnOn()
	#tLapida.RotateRel(0,0,0,0,1,0,-1.57)
#	tLapida.RotateRel(0,0,0,0,1,0,0.0001)

def tLaunchCamReset(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()

	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def tLaunchCamC(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("TumbaReina_Camera_Sarcofago.cam",332,479)
	cam.AddCameraEvent(-1,tLaunchCamReset)
	GameText.WriteText("M7T5")


#def tLaunchCamB(ent,frame) :
#	cam = Bladex.GetEntity("Camera")
#	cam.SetMaxCamera("TumbaReina_Camera_heroe.cam",81,331)
#
#	cam.AddCameraEvent(188-81,SndPiedra)
#	cam.AddCameraEvent(235-81,SndPiedra)
#	cam.AddCameraEvent(281-81,SndPiedraHit)
#	Bladex.AddScheduledFunc(Bladex.GetTime() +6.0,_SndPiedra.Stop,())
#
#	cam.AddCameraEvent(-1,tLaunchCamC)

#def tLaunchCamA() :
#	cam = Bladex.GetEntity("Camera")
#	cam.SetMaxCamera("TumbaReina_Camera_Sarcofago.cam",0,80)
#	#cam.AddCameraEvent(5,SndDemonio4)
#	#cam.AddCameraEvent(20,SndDemonio1)
#	#cam.AddCameraEvent(40,SndDemonio2)
#	#cam.AddCameraEvent(60,SndDemonio3)
#	cam.AddCameraEvent(-1,tLaunchCamB)

#	ScriptSkip.SkipScriptStart("EscenaFinalTumba")
#	#Bladex.DeactivateInput()
#	Scorer.SetVisible(0)
#	Bladex.SetListenerPosition(1)
#	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("ttomb"))

def MapaSiguiente() :
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,GotoMapVars.EndOfLevel,())

def fundido() :
	char=Bladex.GetEntity("Player1")
	Scorer.SetVisible(0)
	AuxFuncs.FadeTo(7.0, 2.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+8.0, MapaSiguiente, ())
	Bladex.DeactivateInput()



#def tLaunchB() :
#	tLaunchCamA()
#	tLaunchPersAnim()
#	tLaunchTombAnim()
#
#
#	Bladex.AddScheduledFunc(Bladex.GetTime()+14.0, tLaunchTombAnimStop, () )
#	#Bladex.AddScheduledFunc(Bladex.GetTime()+40.0, fundido, () )


#def tLaunch() :
#	char = Bladex.GetEntity("Player1")
#	Actions.FreeBothHands("Player1")
#	Scorer.SetVisible(0)
#	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, tLaunchB, ())

#def tGPointerInUse(gpointer,usefrom) :
#	global tGPointerUsed
#	if (tGPointerUsed) : return
#	tGPointerUsed=1
#	Qo=Bladex.CreateEntity("Qo","QueenSword",19124.809000,7393.641000,-1478.599000,"Weapon")
#	ItemTypes.ItemDefaultFuncs (Qo)
#	Qo.Scale=1.000000
#	Qo.Orientation=0.708658,-0.024863,-0.698539,-0.096066
#	tLaunch()

#####################################################################################
#################################### Pergamino.py ####################################
#####################################################################################

def CreaPutaLlave():
	o=Bladex.CreateEntity("llave1","Llavecutre",68479.487043,-3067.012072,-13816.221982)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.006885,0.957583,-0.004492,0.288042
	Stars.Twinkle("llave1")
	darfuncs.SetHint(o,"Iron Key")
	Ontake.DelOnTakeEvent("Vergamino")


#####################################################################################
#################################### Tablilla.py ####################################
#####################################################################################

def ComienzaAnimacionTablilla(sectorindex,entityname):



  if entityname =="Player1":
    char = Bladex.GetEntity("Player1")
    #char.GoTo(TablStartPosition[0],TablStartPosition[1],TablStartPosition[2])
    #char.RouteEndedFunc = EscenaTablilla
    EscenaTablilla("Player1")
    TabillaSector.OnEnter = ""


def EscenaTablilla(Entity):
  ScriptSkip.SkipScriptStart("EscenaTablillaTumba")
  #Bladex.DeactivateInput()
  Scorer.SetVisible(0)
  Actions.FreeBothHands(Entity,IniciaEscenaTablilla,())
  AuxFuncs.FadeFrom(0.5,10.0,0,0,0)


def Musicaytexto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("tablillatomb"))
	GameText.WriteText("M7T4")

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


def IniciaEscenaTablilla():
  cam  = Bladex.GetEntity("Camera")
  char = Bladex.GetEntity("Player1")
  AuxFuncs.FadeFrom(1.0,0.1,0,0,0)


  if Bladex.GetEntity('Player1').Kind[0] == 'D':
  	o             = Bladex.GetEntity('Tablilla3')
  	o.Position    =  (164604.961192, 6731.0164527, 519.634520188)
  	o.Orientation =  (0.624461948872, 0.371651053429, 0.588417828083, -0.354523897171)

  if Bladex.GetEntity('Player1').Kind[0] == 'K':
  	o             = Bladex.GetEntity('Tablilla3')
  	o.Position    =  (163984.81624, 6411.07512475, 590.330033321)
  	o.Orientation =  (0.642702579498, 0.376409798861, 0.602748334408, -0.286257714033)

  if Bladex.GetEntity('Player1').Kind[0] == 'B':
  	o             = Bladex.GetEntity('Tablilla3')
  	o.Position    =  (164537.08826, 6256.25336649, 580.541312389)
  	o.Orientation =  (0.63854521513, 0.338820904493, 0.588419079781, -0.362247794867)

  if Bladex.GetEntity('Player1').Kind[0] == 'A':
  	o             = Bladex.GetEntity('Tablilla3')
  	o.Position    =  (164467.288519, 6426.71606551, 785.943453547)
  	o.Orientation =  (0.596105694771, 0.375627458096, 0.614991188049, -0.354044884443)

  char.Angle = AnglStartPosition
  char.SetTmpAnmFlags(1,1,1,0,5,1)
  char.Wuea = Reference.WUEA_ENDED
  char.LaunchAnmType(AnimationName)
  char.Position = TablStartPosition[0],TablStartPosition[1],TablStartPosition[2]
  char.SetOnFloor()


  cam.SetMaxCamera(CameraName,0,CameraNumFrames)
  cam.AddCameraEvent(-1,StopCameraTablilla)

  cam.AddCameraEvent(Event_CogeLaTablilla     ,CogeLaTablilla)
  cam.AddCameraEvent(Event_tTablillaDust1     ,tTablillaDust)
  cam.AddCameraEvent(Event_tTablillaDust2     ,tTablillaDust)
  cam.AddCameraEvent(Event_DesapareceTablilla ,DesapareceTablilla)

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

def DesapareceTablilla(Camera,frame):
  global PosX
  global PosY
  global PosZ
  global Tick
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.RemoveObject("Tablilla3")

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

def CogeLaTablilla(Camera,frame):
  char = Bladex.GetEntity("Player1")
  inv  = char.GetInventory()
  inv.AddTablet("Tablilla3")
  inv.LinkLeftHand("Tablilla3")
  ImprimeDatosTablilla("Tablilla3")
  Musicaytexto()

#####################################################################################
#################################### Golem.py ####################################
#####################################################################################

def GolemSmoke(glm,dirx =  300):
	vida = 45
	g = Bladex.GetEntity(glm)
	pc = g.Position

	p1 = pc[0] + 200 ,pc[1] - 1000,pc[2] - 300
	p2 = 0,0,600
	p3 = 0,1100,300

	hombro1 = pc[0] + 200 ,pc[1] - 1000,pc[2] - 400
	hombro2 = pc[0] + 200 ,pc[1] - 1000,pc[2] + 300

	mano1 = pc[0] + 500, pc[1], pc[2] - 900
	mano2 = pc[0] - 200, pc[1], pc[2] + 950

	vm1 = hombro1[0] - mano1[0],hombro1[1] - mano1[1],hombro1[2] - mano1[2]
	vm2 = hombro2[0] - mano2[0],hombro2[1] - mano2[1],hombro2[2] - mano2[2]

	pierna1 = pc[0] + 200, pc[1], pc[2] - 150
	pierna2 = pc[0] + 200, pc[1], pc[2] + 150

	pie1 = pierna1[0], pierna1[1] + 1400, pierna1[2] - 150
	pie2 = pierna2[0], pierna2[1] + 1400, pierna2[2] + 150

	vp1 = pie1[0] - pierna1[0],pie1[1] - pierna1[1],pie1[2] - pierna1[2]
	vp2 = pie2[0] - pierna2[0],pie2[1] - pierna2[1],pie2[2] - pierna2[2]

	head = pc[0] + 200 ,pc[1] - 1300,pc[2] + 100

	polvo=Bladex.CreateEntity("PolvoHead"+glm, "Entity Particle System D1", head[0],head[1],head[2])
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=75
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoPierna1"+glm, "Entity Particle System D2", pierna1[0],pierna1[1],pierna1[2])
	polvo.D = vp1[0],vp1[1],vp1[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoPierna2"+glm, "Entity Particle System D2", pierna2[0],pierna2[1],pierna2[2])
	polvo.D = vp2[0],vp2[1],vp2[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoMano1"+glm, "Entity Particle System D2", mano1[0],mano1[1],mano1[2])
	polvo.D = vm1[0],vm1[1],vm1[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoMano2"+glm, "Entity Particle System D2", mano2[0],mano2[1],mano2[2])
	polvo.D = vm2[0],vm2[1],vm2[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=150
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

	polvo=Bladex.CreateEntity("PolvoCuerpo"+glm, "Entity Particle System D3", p1[0],p1[1],p1[2])
	polvo.D1 = p2[0],p2[1],p2[2]
	polvo.D2 = p3[0],p3[1],p3[2]
	polvo.ParticleType="DustGolem"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=350
	polvo.Velocity=dirx, 0.0, 0.0
	polvo.RandomVelocity=0.0
	polvo.Time2Live=vida
	polvo.DeathTime=Bladex.GetTime()+5.0/60.0

def Golemalo():
	_Golemalo.Play(char.Position[0], char.Position[1], char.Position[2], 0)

DespDust = 5000
def RompeParedGolem(camera,frame):
	GolemSmoke("GolemFinal",DespDust)
	#Golemalo()
	ParedGolem.DoBreak( (10.5,0,0), (9750, 5000,1500), (0,0,0) )
	#ParedGolem.DoBreak( (5,0,0), (9750, 5000, -1500), (0,0,0) )

def StopCameraX(Camera,frame):
	cam  = Bladex.GetEntity("Camera")
	char = Bladex.GetEntity("Player1")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	troll=Bladex.GetEntity("GolemFinal")
	troll.Blind   = 0
	troll.Deaf    = 0

def deGolem(x=0,y=0,z=0,w=0):
	global tGPointerUsed
	tGPointerUsed = 0
	troll.Data.ImDeadFuncX(x)
	Bladex.AddScheduledFunc(Bladex.GetTime()+ 1.0, Bladex.TriggerEvent,(29,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+ 3.0, BajaSarcofago,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+ 3.0, RotateToQSword,())
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, tLaunchCamC,(1,1))

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("ttomb"))
	ScriptSkip.SkipScriptStart("EscenaFinalTumba")
	Scorer.SetVisible(0)

def RotateToQSword():
	angle = B3DLib.GetEntity2EntityAngle ("Player1", "Qo")
	char.Face(angle)


def PlayStepGolem(sound):
	sound.Position = char.Position
	sound.PlaySound(0)

FrameRotura = 20

def IniciaEscenaGolem(sectorindex,entityname):
	global tGPointerUsed
	if entityname == "Player1":
		tGPointerUsed = 1
		Scorer.SetVisible(0)
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa4") )
		cam  = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("reina_Camera_golem.cam",0,178)
		Bladex.DeactivateInput()
		cam.AddCameraEvent(-1,StopCameraX)
		cam.AddCameraEvent(FrameRotura,RompeParedGolem)
		#garrotex=Bladex.CreateEntity("GarropinT3","Garropin",0,0,0)
		#garrotex.Weapon=1

		troll          = Bladex.GetEntity("GolemFinal")
		troll.Person   = 1
		troll.Position = 9027, 5775,-1203
		troll.Angle    =-3.1415/2.0
		EnemyTypes.EnemyDefaultFuncs(troll)
		troll.Blind    = 1
		troll.Deaf     = 1
		troll.Data.ImDeadFuncX = troll.ImDeadFunc
		troll.ImDeadFunc = deGolem

		#Actions.TakeObject(troll.Name, garrotex.Name)

		troll.SetOnFloor()
		troll.SetTmpAnmFlags(1,1,1,0,5,1)
		troll.Wuea = Reference.WUEA_ENDED
		troll.LaunchAnmType("break_wall")
		ParedGolemSectInit1.OnEnter = ""

		Bladex.AddScheduledFunc(Bladex.GetTime() + FPASO1,PlayStepGolem,(Golempaso1,))
		Bladex.AddScheduledFunc(Bladex.GetTime() + FPASO2,PlayStepGolem,(Golempaso2,))
		Bladex.AddScheduledFunc(Bladex.GetTime() + FPASO3,PlayStepGolem,(Golempaso3,))
		Bladex.AddScheduledFunc(Bladex.GetTime() + FPASO4,PlayStepGolem,(Golempaso1,))
		Bladex.AddScheduledFunc(Bladex.GetTime() + FPASO5,PlayStepGolem,(Golempaso2,))


#####################################################################################
####################################  Inicio.py  ####################################
#####################################################################################

def StopCameraInicioXxX(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	#ork = Bladex.GetEntity("OrkoMalito")
	#if ork:
	#	ork.SubscribeToList("Pin")
	Bladex.SetListenerPosition(1)
	char.SetOnFloor()

def CaminaElTio(Camera,frame):
	char.Position = -33016.645, 6941.047, -51226.363
	char.Angle    = 3.141592
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnmType("reina_start")
	char.SetOnFloor()

def inicio():
	Scorer.SetVisible(0)
	ScriptSkip.SkipScriptStart("EscenaInicioTumba")
	#Bladex.DeactivateInput()
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Reina_camera_inicio.cam",0,1000)
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,MusicTool.LaunchMusicEvent,("iniciotomb",))
	GameText.WriteText("M7T1")
	char.Position = (-28612.0673802, 6936.37479719, -47467.5534717)
	char.Angle    = 63.856*3.1415/180
	char.SetOnFloor()

	# orco
	#ork=Bladex.CreateEntity("OrkoMalito", "Ork", -34889.594,-5473.812, -16484.982)
	#ork.Person=1
	#ork.Angle=3.1415
	#ork.Blind=1
	#ork.Deaf=1
	#EnemyTypes.EnemyDefaultFuncs(ork)
	#ork.SetTmpAnmFlags(1,1,1,0,5,1)
	#ork.LaunchAnmType("Ork_reina_palanca")
	#ork.SetOnFloor()

	# camara
	cam.AddCameraEvent(818,CaminaElTio)
	cam.AddCameraEvent(-1,StopCameraInicioXxX)

#####################################################################################
#################################### King.py ####################################
#####################################################################################

#def SndDemonio1(ent,Time):
#	_SndDemonio1.Play(char.Position[0], char.Position[1], char.Position[2], 0)
#
#def SndDemonio2(ent,Time):
#	_SndDemonio2.Play(char.Position[0], char.Position[1], char.Position[2], 0)
#
#def SndDemonio3(ent,Time):
#	_SndDemonio3.Play(char.Position[0], char.Position[1], char.Position[2], 0)
#
#def SndDemonio4(ent,Time):
#	_SndDemonio4.Play(char.Position[0], char.Position[1], char.Position[2], 0)
#
#def SndDemonio5(ent,Time):
#	_SndDemonio5.Play(char.Position[0], char.Position[1], char.Position[2], 0)
#
def SndFireBall(ent,Time):
	_SndFireBall.Play(char.Position[0], char.Position[1], char.Position[2], 0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, _SndFireWarp.Play,(char.Position[0], char.Position[1], char.Position[2], 3))


def SndHostia(ent,Time):
	_SndHostia.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def SndGritoKeletum(ent,Time):
	_SndGritoKeletum.Play(char.Position[0], char.Position[1], char.Position[2], 0)

def sSceneKeepShield(ent,event):
	print(">>sSceneKeepShield()")
	# deslinkar el escudo de la mano
	# meter el escudo al inventario
	inv = char.GetInventory()
	inv.LinkRightHand("None")
	Actions.TakeObject("Player1","EscudoDeFuegoBueno")

def sSceneTakeShield(ent,event):
	print(">>sSceneTakeShield()")
	# linkar el escudo a la mano
	inv = char.GetInventory()
	inv.LinkRightHand("EscudoDeFuegoBueno")

def VozyTexto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("kingtomb"))
  	GameText.WriteText("M7T3")

def sSceneReadStartEvent(ent,event):
	# xavi , aqui tienes que poner los textos

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, VozyTexto,())

def sSceneLaunchTakeAnimationB():
	print(">>sSceneLaunchTakeAnimationB()")
	char = Bladex.GetEntity("Player1")
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnimation("Kgt_read_shield_b")
	char.AddAnmEventFunc("RightStoreShield",sSceneKeepShield)
	char.AddAnmEventFunc("RightPickupShield",sSceneTakeShield)
	char.AddAnmEventFunc("StartRead",sSceneReadStartEvent)

def sSceneLaunchTakeAnimationA():
	print(">>sSceneLaunchTakeAnimationA()")
	char = Bladex.GetEntity("Player1")
	char.Wuea = Reference.WUEA_ENDED
	char.LaunchAnimation("Kgt_read_shield_a")
	char.AddAnmEventFunc("RightStoreShield",sSceneKeepShield)
	char.AddAnmEventFunc("RightPickupShield",sSceneTakeShield)
	char.AddAnmEventFunc("StartRead",sSceneReadStartEvent)

def sSceneOnTake() :
	print(">>sSceneOnTake()");

	shieldY=Bladex.GetEntity("EscudoDeFuegoBueno").Position[1]
	charY=Bladex.GetEntity("Player1").Position[1]

	if (shieldY>charY) :
		sSceneLaunchTakeAnimationA()	# animacion baja
	else:
		sSceneLaunchTakeAnimationB()	# animacion alta

def sScenePrepare() :
	skel = Bladex.GetEntity("TheKing")
	shield = Bladex.CreateEntity("EscudoDeFuegoBueno", "KingShield", skel.Position[0], skel.Position[1]-350, skel.Position[2],"Weapon")
	ItemTypes.ItemDefaultFuncs (shield)
	OnInitTake.AddOnInitTakeEvent("EscudoDeFuegoBueno",sSceneOnTake)
	shield.Impulse(1,1,1)

def CaminaHastaLapidaRey(sectorindex,entityname):
	if entityname == "Player1":
		KingStartSector.OnEnter = ""
		Actions.FreeBothHands("Player1",IniciaLapidaRey)
		ScriptSkip.SkipScriptStart("EscenaKingCalentito")
		#Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		AuxFuncs.FadeFrom(0.5,0.5,0,0,0)


def IniciaLapidaRey():

   char.SetTmpAnmFlags(1,1,1,0,5,1)
   char.Wuea = Reference.WUEA_ENDED
   char.Angle              = 3.1415

   if char.Kind[0] == "K":
   	char.Position           = 104767, 1556, 714
   if char.Kind[0] == "A":
   	char.Position           = 104467, 1556, 714
   if char.Kind[0] == "B":
   	char.Position           = 104400, 1793, 714
   if char.Kind[0] == "D":
   	char.Position           = 104450, 1793, 714


   char.LaunchAnmType("tumba_rey")
   Bladex.AddScheduledFunc(Bladex.GetTime() + 0.2,char.SetOnFloor,())

   cam = Bladex.GetEntity("Camera")
   cam.SetMaxCamera("TumbaReyCamera01.cam",0,230)
   cam.AddCameraEvent(-1,camaraDos)
   cam.AddCameraEvent(200,LapidaSalta)
   cam.AddCameraEvent(205,EsqueletoAnima)

   #cam.AddCameraEvent(30,SndDemonio4)
   #cam.AddCameraEvent(60,SndDemonio3)
   #cam.AddCameraEvent(80,SndDemonio5)
   #cam.AddCameraEvent(119,SndDemonio1)
   #cam.AddCameraEvent(162,SndDemonio2)

   Bladex.AddScheduledFunc(Bladex.GetTime() + KING_ESFUERZO1,PlaySound,(sonido_esfuerzo1,))
   Bladex.AddScheduledFunc(Bladex.GetTime() + KING_ESFUERZO2,PlaySound,(sonido_esfuerzo2,))


   #esq             = Bladex.GetEntity("TheKing")
   #if esq!=None:
   #  esq.SubscribeToList("Pin")

   Bladex.ExeMusicEvent( Bladex.GetMusicEvent("inicio23") )



def LaunchLapida(xg = 0,yg = -300000,zg = 100000, px = 0,py = 0,pz = 0):
   LapidK.Solid = 0
   LapidK.Position = 109092.427000,1310.936000,607.453000
   LapidK.Orientation=0.498355,0.498555,-0.501735,0.501345
   LapidK.ImpulseC(px,py,pz,xg,yg,zg)

def LapidaSalta(Camera,frame):
   SndHostia(Camera,frame)
   LapidK.Solid = 0
   LapidK.Position = 109092.427000,1310.936000,607.453000
   LapidK.Orientation=0.498355,0.498555,-0.501735,0.501345
   #LapidK.ImpulseC( 0,0, 0, 0,-300000,100000 )
   LapidK.ImpulseC( 0,0, 0, 0,-300000,200000 )
   TumbaEnLlamas()

def EsqueletoAnima(Camera,frame):
   #esq = CreaElEsqueleto(109207,1841,482)
   esq = Bladex.GetEntity("TheKing")
   esq.UnFreeze()
   esq.Position = 109207,2000,482
   esq.Angle = 3.1415
   esq.SetTmpAnmFlags(1,1,1,0,5,1)
   esq.Wuea = Reference.WUEA_ENDED
   esq.LaunchAnmType("tumba_rey_aguila")
   OnOff.TurnOffLight("luzrey1")
   OnOff.TurnOffLight("luzrey2")
   OnOff.TurnOffLight("luzrey3")
   OnOff.TurnOffLight("luzrey4")
   EnciendeElEsqueletoEnLlamas()
   SndFireBall(Camera,frame)

def camaraDos(Camera,frame):
   cam = Bladex.GetEntity("Camera")
   cam.SetMaxCamera("TumbaReyCamera02.cam",230,350)

   cam.AddCameraEvent(-1,camaraTres)

   #cam.AddCameraEvent(250-230,SndDemonio4)
   #cam.AddCameraEvent(300-230,SndDemonio5)
   #cam.AddCameraEvent(340-230,SndDemonio1)


   puertadoble2.CloseDoor()
   puertadoble1.CloseDoor()



def camaraTres(Camera,frame):
   cam = Bladex.GetEntity("Camera")
   cam.SetMaxCamera("TumbaReyCamera01.cam",350,565)

   cam.AddCameraEvent(442-350,SndGritoKeletum)

   cam.AddCameraEvent(-1,StopCamera)

   #cam.AddCameraEvent(380-350,SndDemonio1)
   #cam.AddCameraEvent(420-350,SndDemonio2)
   #cam.AddCameraEvent(440-350,SndDemonio3)
   #cam.AddCameraEvent(490-350,SndDemonio4)
   #cam.AddCameraEvent(520-350,SndDemonio5)
   #cam.AddCameraEvent(560-350,SndDemonio5)
   cam.AddCameraEvent(485-350,EnGuardiaCanejo)


def EnGuardiaCanejo(Camera,frame):
	Actions.StdToggleWeapons("Player1")



def StopCamera(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	LapidK.Solid = 1

	esq             = Bladex.GetEntity("TheKing")
	esq.Blind       = 0
	esq.Deaf        = 0
	esq.Angle = 3.1415/2
	esq.SetOnFloor()

def EnciendeElEsqueletoEnLlamas():
    esq                = Bladex.GetEntity("TheKing")
    Bladex.GetEntity("EspadaDeFuego").CastShadows = 0
    Bladex.GetEntity("EscudoDeFuego").CastShadows = 0  
    
    luz             = Bladex.CreateEntity("LuzDelRey","Entity Spot",0,0,0)
    luz.Color       = 200,100,0
    luz.Intensity   = 15
    luz.Precission  = 0.1
    luz.CastShadows = 1
    luz.Visible     = 1
    luz.SizeFactor  = 0
    esq.Link(luz)
    esq.CastShadows = 0
    esq.CatchOnFire(0,0,0)
    esq.ImDeadFunc = TheKingIsDeath
    return esq

def CreaElEsqueleto(x, y, z):
    hacha=Bladex.CreateEntity("EspadaDeFuego", "KingSword", 0, 0, 0,"Weapon")
    
    escudo=Bladex.CreateEntity("EscudoDeFuego", "KingShield", 0, 0, 0,"Weapon")
    Sparks.MakeShield("EscudoDeFuego")
    Reference.EntitiesObjectData[escudo.Name]= copy.copy(Reference.DefaultObjectData['KingShield'])
    Reference.EntitiesObjectData[escudo.Name][7]=0
    
    esq=Bladex.CreateEntity("TheKing", "Skeleton", x,y,z,"Person")
    esq.Angle=0.0
    esq.Level=14
    esq.Blind=1
    esq.Deaf=1
    esq.ActionAreaMin=1<<31
    esq.ActionAreaMax=1<<31

    Actions.TakeObject(esq.Name, hacha.Name)
    Actions.TakeObject(esq.Name, escudo.Name)
    EnemyTypes.EnemyDefaultFuncs(esq)
    esq.Freeze()
    darfuncs.HideBadGuy("TheKing")


def TheKingIsDeath(entity_name):
   Bladex.AddScheduledFunc(Bladex.GetTime()+4.5,Bladex.TriggerEvent,(28,))
   Bladex.AddScheduledFunc(Bladex.GetTime()+10, DespuesMuerte,())
   Bladex.AddScheduledFunc(Bladex.GetTime()+4.5,seEsfumaElCoso,() )
   Bladex.AddScheduledFunc(Bladex.GetTime()+5, SubitaBoom,())
   Bladex.AddScheduledFunc(Bladex.GetTime()+5.5, DesapareceEsqueleto,())
   AbrePuertaCE1()
   AbrePuertaLlave2()
   rey = Bladex.GetEntity(entity_name)
   wl  = Bladex.GetEntity(rey.InvLeft)
   wr  = Bladex.GetEntity(rey.InvRight)

   rey.Data.StdImDead(entity_name)
   Breakings.SetBreakable(wr.Name)
   Breakings.ExplodeSpecialObject (wr.Name, 1000.0)
   Bladex.AddScheduledFunc(Bladex.GetTime()+0.05, rey.GetInventory().LinkLeftHand, ("EscudoDeFuego",))


def seEsfumaElCoso():
   sScenePrepare()
   PhantonFX.Delta = 0.05
   PhantonFX.DisappearsChar("TheKing")

def DesapareceEsqueleto():
   #esq                     = Bladex.GetEntity("TheKing")
   #esq.SubscribeToList("Pin")

   OnOff.TurnOnLight("luzrey1")
   OnOff.TurnOnLight("luzrey2")
   OnOff.TurnOnLight("luzrey3")
   OnOff.TurnOnLight("luzrey4")
   puertadoble2.OpenDoor()
   puertadoble1.OpenDoor()
   Bladex.DeactivateInput()
   Scorer.SetVisible(0)

def DespuesMuerte():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("TumboRey") )
        escalon1a.OnEndOpenFunc = SaleFetiche
        escalon1a.OpenDoor()

        AuxFuncs.MoveCamFromTo(108000, -586, -1252,     112000, -586, -1252,       110219, 1535, 642,     110219, 1535, 642,           8,FinaleCamera)

def Fetichazo():
	global ActivaLosEsqueletos
	ActivaLosEsqueletos = 1

def SubeFeticheX():
     global Continuafet
     global ffY
     global blY


     X        = ff.Position[0]
     Z        = ff.Position[2]
     sld_area = Bladex.GetEntity(escalon3a.Name)
     Y        = ffY - sld_area.Displacement
     ff.Position = X,Y,Z

     X      = bl.Position[0]
     Z      = bl.Position[2]
     Y      = blY - sld_area.Displacement
     bl.Position = X,Y,Z

     if Continuafet:
       Bladex.AddScheduledFunc(Bladex.GetTime()+0.025, SubeFeticheX, ())

def SaleFetiche():
        escalon3a.OnEndCloseFunc = TerminaHistoriaFetiche
        escalon3a.CloseDoor()
        SubeFeticheX()

def TerminaHistoriaFetiche():
        global Continuafet
        Continuafet = 0
        #Bladex.ActivateInput()

def FinaleCamera():
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	cam.Cut()

# crea un efecto de llamas en la tumba
def TumbaEnLlamas():
        FireBall=Bladex.CreateEntity("Llamas1", "Entity Particle System D3", 107375,2100,1375)
        FireBall.D1 = 0,0,-1200
        FireBall.D2 = 3700,0,-1200
        FireBall.ParticleType="LargeFire"
        FireBall.YGravity=0
        FireBall.Friction=0
        FireBall.PPS=256
        FireBall.Velocity= 0,-1000, 0
        FireBall.Time2Live=30
        FireBall.RandomVelocity=9
        FireBall.DeathTime=Bladex.GetTime()+12

        FireBall=Bladex.CreateEntity("Llamas2", "Entity Particle System D3", 107375,2100,1375)
        FireBall.D1 = 3700,0,0
        FireBall.D2 = 3700,0,-1200
        FireBall.ParticleType="LargeFire"
        FireBall.YGravity=0
        FireBall.Friction=0
        FireBall.PPS=256
        FireBall.Velocity= 0,-1000, 0
        FireBall.Time2Live=30
        FireBall.RandomVelocity=9
        FireBall.DeathTime=Bladex.GetTime()+12




def SubitaBoom():
	esq                     = Bladex.GetEntity("TheKing")
	FireBall                = Bladex.CreateEntity("Llamas2", "Entity Particle System D1", esq.Position[0],esq.Position[1]-100,esq.Position[2])
	FireBall.ParticleType   = "LargeFire"
	FireBall.YGravity       = -1000
	FireBall.Friction       = 0
	FireBall.PPS            = 1024
	FireBall.Velocity       = 0,800, 0
	FireBall.Time2Live      = 30
	FireBall.RandomVelocity = 35
	FireBall.DeathTime=Bladex.GetTime()+1
	_SndFireBall.Play(esq.Position[0], esq.Position[1], esq.Position[2], 0)
	ActivativaGeneradoresFeticho()
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,AuxFuncs.FadeFrom,(0.15,0.0,255,192,64))


#####################################################################################
####################################  Suelo.py   ####################################
#####################################################################################


def LineaPolvoSuelo(Name,pos,Disp,pps = 300):
	polvo=Bladex.CreateEntity(Name, "Entity Particle System D2", pos[0],pos[1],pos[2])
	polvo.D = Disp
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.ParticleType="DustDoor"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=pps
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0


def PushButtonTrampus():
	global suelo_state
	suelo1.CloseDoor()
	suelo2.CloseDoor()
	suelo_state = 0

	if (button1.state == 0):
		Button.Turn("SButton1")

	if (button2.state == 0):
		Button.Turn("SButton2")



def SueloCerrado():
	LineaPolvoSuelo("PolvoSuelo",(11000,5250,11250),(14000,0,0),700)


def SueloAbierto():
	if (button1.state == 1):
		c_button1.Reset(1)

	if (button2.state == 1):
		c_button2.Reset(1)

def ActivateSuelo(sld,entity):
	global suelo_state

	if (entity == "Player1"):
		if (suelo_state == 0):
			suelo_state = 1

			suelo1.OpenDoor()
			suelo2.OpenDoor()

##########################################################################
##                             GENAGUA.py
##########################################################################
def CreateParticle(r= 30,g = 40,b = 50,al = 180.0,part = "WaterParticle"):
	Bladex.AddParticleGType("Espumita",part,2,24)

	for i in range(24):
		if i < 12:
			aux=1.0 - ((12.0-i)/12.0)

		else:
			aux=(12.0-(i-12))/12.0

		size=30+aux*30.0
		Bladex.SetParticleGVal("Espumita",i,r,g,b,al,size)

def CalculatePositionWave(espuma,cam,posi,deathtime):
	time = Bladex.GetTime()

	if time < deathtime:
		campos = cam.Position
		v=campos[0]-posi[0], 0.0, campos[2]-posi[2]
		v=AuxFuncs.Normalize(v)

		pos = posi[0] + v[0] * 1000,posi[1],posi[2] + v[2] * 1000
		desp = v[2] * -500,v[0] * 500

		espuma.Position = pos[0] + desp[0],8300,pos[2] + desp[1]
		espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2

		#Bladex.AddScheduledFunc(time + 0.05,CalculatePositionWave,(espuma,posi,deathtime))

def SaltaAguaGen(enmgen):
	espuma=Bladex.CreateEntity("Espuma"+`Esp`, "Entity Particle System D1", 0,0,0)
	espuma.Position= enmgen.Position[0],6900,enmgen.Position[2]
	espuma.ParticleType="Espumita"
	espuma.PPS=512
	espuma.YGravity=500
	espuma.Friction=0.00
	espuma.Velocity=0.0, 0.0, 0.0
	espuma.RandomVelocity=10.0
	espuma.Time2Live=24
	espuma.DeathTime = Bladex.GetTime() + 3.0

	#Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,CalculatePositionWave,(espuma,cam,pos,espuma.DeathTime))


def SaltaAguaGenActivate(enmgen):
	enmgen.ActionAreaMin=1<<31
	enmgen.ActionAreaMax=1<<31
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,SaltaAguaGen,(enmgen,))

def ActivateGen1Agua(sector,entity):
	if (entity == "Player1"):
		Gen1SecAgua.OnEnter = ""
		generadorT1Agua.GenerateEnemy()

def ActivateGen2Agua(sector,entity):
	if (entity == "Player1"):
		Gen2SecAgua.OnEnter = ""
		generadorT2Agua.GenerateEnemy()


##########################################################################
##########################################################################
##########################################################################
