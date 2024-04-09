##///
##||| ISLAND_M8/DefFuncs.PY TITANIUM
##||| Change list:
##||| * sectx1 has been moved outside of any function to ensure the script cannot be called multiple times causing unneeded errors
##||| * Opening sequence drawbridge animation now plays at 60fps
##||| * Fixed ear-rape at skeleton surprise
##||| * Re-stored prisoners begging for their demise
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
import Room
import Button
import GotoMapVars
import AbreCam
import ItemTypes
import ScriptSkip
import Doors

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para historia.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def MusicaytextoB():	
	GameText.WriteText("M8T5")	
	
def CuentaCuentos(sectorindex,entityname): 
	if entityname =="Player1":
		HistoriaSec.OnEnter = ""
		char = Bladex.GetEntity("Player1")
		char.GoTo(-38193.48, 16889.342, 21222.578)
		char.RouteEndedFunc = Camara0
		Bladex.DeactivateInput()
	
def Camara0(Entity):
	global playerB	
	char = Bladex.GetEntity("Player1")	
	char.Angle       = 179.622*3.14159/180+3.14159
	Bladex.ActivateInput()
	ScriptSkip.SkipScriptStart("EscenaHistoriaTablillas")
	Scorer.SetVisible(0)
	GotoMapVars.MapText(-1,"SALATABLILLAS")
	
	char.LaunchAnmType("sala_tablillas")
	
	char.Position = -38193.48, 16889.342, 21222.578
	char.SetOnFloor()
	
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Camera_primera.cam",0,300)
	cam.AddCameraEvent( -1,Camara1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("isla-tablilla"))
	
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, OnOff.TurnOnLight,("lampegip2",))
	Torchs.EnciendeAntorcha("antorchaen1")
	Torchs.EnciendeAntorcha("antorchaen2")
	Torchs.EnciendeAntorcha("antorchaen3")
	Torchs.EnciendeAntorcha("antorchaen4")

	#Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, MusicaytextoB,())


def Camara1(Camera,frame):
	MusicaytextoB()
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Camera_segunda.cam",301,1150)
	cam.AddCameraEvent( -1,Camara2)


def Camara2(Camera,frame):
	
	cam = Bladex.GetEntity("Camera")
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()	
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)

def Apagalahist(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para generadores.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

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
		
		espuma.Position = pos[0] + desp[0],8300,pos[2] + desp[1]
		espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2

		Bladex.AddScheduledFunc(time + 0.05,CalculatePositionWave,(espuma,cam,posi,deathtime))

def SaltaAguaGen(enmgen):
#def SaltaAguaGen():
	global Esp
	Esp = Esp + 1
	pos=enmgen.Position
	#pos = -35000, 10000, -47000
	#pos = char.Position
	cam = Bladex.GetEntity("Camera")
	charpos = cam.Position
	v=charpos[0]-pos[0], 0.0, charpos[2]-pos[2]
	v=AuxFuncs.Normalize(v)
	
	rpos = pos[0] + v[0] * 800,pos[1],pos[2] + v[2] * 800
	desp = v[2] * -400,v[0] * 400
	
	espuma=Bladex.CreateEntity("Espuma"+`Esp`, "Entity Particle System D2", rpos[0] + desp[0],8300,rpos[2] + desp[1])
	espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2
	espuma.ParticleType="Espuma2"
	espuma.PPS=512
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, 0.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.Time2Live=8
	espuma.DeathTime = Bladex.GetTime() + 4.0

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,CalculatePositionWave,(espuma,cam,pos,espuma.DeathTime))
	

def SaltaAguaGenActivate(enmgen):
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,SaltaAguaGen,(enmgen,))
	print "sale", enmgen.Name

def terminaGeneradorT1(coso=0,otrocoso=0):
	AbrePuerta33()
	Abrereja34()
	print "Deberia abrirse"
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def ActivateGen1(sector,entity):	
	if (entity == "Player1"):
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("deposito") )
		Gen1Sec.OnEnter = ""
		generadorT1.GenerateEnemy()
		CierraPuerta33()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##################################################################################################
## funcion atomico-punki que despierta esqueletos cuando el jugador ha limpiado todo el exterior
##################################################################################################

def FinMuertesPLantabaja():
	AbrePuertasTrono()
	darfuncs.UnhideBadGuy("Skeleton95")
	darfuncs.UnhideBadGuy("Skeleton96")

sectx1=Bladex.GetSector(-38905.5707736, -4919.43312196, -7919.79524383)         # Moved here so x1() doesn't get called multiple times. -LeadHead

def TerminanLasMuertes():
    #sectx1=Bladex.GetSector(-38905.5707736, -4919.43312196, -7919.79524383)
    sectx1.OnEnter=x1

def KreaKeletos():
	darfuncs.UnhideBadGuy("Skeleton4")
	darfuncs.UnhideBadGuy("Skeleton5")
	darfuncs.UnhideBadGuy("Skeleton6")
	darfuncs.UnhideBadGuy("Islandarq5")
	darfuncs.UnhideBadGuy("Islandarq6")
	darfuncs.UnhideBadGuy("Islandarq7")
	darfuncs.UnhideBadGuy("Skeleton7")
	darfuncs.UnhideBadGuy("Skeleton8")
	darfuncs.UnhideBadGuy("Skeleton9")
	darfuncs.UnhideBadGuy("Islandarq8")
	darfuncs.UnhideBadGuy("Islandarq9")
	
	
def x1(sectorindex,entityname):

	if entityname=='Player1':
		KreaKeletos()
		sectx1.OnEnter=""

def CreaZombisTontos():
	darfuncs.UnhideBadGuy("Zombi2")
	darfuncs.UnhideBadGuy("Zombi3")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, AndadZombisTontos,())

def AndadZombisTontos():
	o = Bladex.GetEntity("Zombi2")
	o.GoTo(-54086.1509942, -5453.74268474, 48402.8722755)
	o = Bladex.GetEntity("Zombi3")
	o.GoTo(-22449.3372781, -5453.94724659, 44229.779784)

def x2(sectorindex,entityname):             # PLAGUE: This isn't working correctly. This function is still trying to be called even AFTER it has already been called.

  if entityname=='Player1':
    CreaZombisTontos()
    sectx2.OnEnter=""

def CreaZombiMazmorra():
	darfuncs.UnhideBadGuy("Zombi15")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, AndaZombiMazmorra,())

def AndaZombiMazmorra():
	o.GoTo(-18284.7441063, 388.330020182, 21219.0221544)

def x3(sectorindex,entityname):

  if entityname=='Player1':
    CreaZombiMazmorra()
    sectx3.OnEnter=""

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def MueveTodos():
	for enemigo in listazombis:
		GoToMul(enemigo.Name)


def KreaZombis():
	darfuncs.UnhideBadGuy("Zombi16")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, MueveTodos,())

def x4(sectorindex,entityname):

  if entityname=='Player1':
    KreaZombis()
    sectx4.OnEnter=""

def KreaKds():
	darfuncs.UnhideBadGuy("7kd")
	darfuncs.UnhideBadGuy("8kd")
	#darfuncs.UnhideBadGuy("9kd")

def x5(sectorindex,entityname):

  if entityname=='Player1':
    KreaKds()
    sectx5.OnEnter=""

def MuerteMinorx():
	Abrerast23()
	darfuncs.UnhideBadGuy("5kd")
	darfuncs.UnhideBadGuy("6kd")

def GoToMin(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMin


def MueveMin():
	for enemigo in listabichos:
		GoToMin(enemigo.Name)


def KreaMin():
	darfuncs.UnhideBadGuy("minot1")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, MueveMin,())


def x6(triggername,entityname):
  if entityname=='Player1':
    KreaMin()
    Bladex.SetTriggerSectorFunc("minorx", "OnEnter", "" )
 
def FinMuertesVigasinclinadas():
	puerta17.OpenDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
	MusicTool.Music2Sector("entrazonaskl1",None)
	MusicTool.Music2Sector("entrazonaskl2",None)
	
def AndaSkelarquero():
	o = Bladex.GetEntity("Islandarq11")
	o.GoTo(-33884.6028602, -37136.0328281, 30345.9248186)			

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevator2.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador2():

	desplazamientos=(1000.0, 2650.0, 1000.0)
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
	desplazamientos=(1000.0, 2650.0, 1000.0)
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
#*******************************   Definiciones para demonio.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

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
		
def AparicionDemonio(name):
	demonio=Bladex.GetEntity(name)
	demonio.Position = -37500,-51000,30500
	demonio.Angle=3	            # PLAGUE: This doesn't work
	demonio.Wuea=Reference.WUEA_ENDED
	demonio.SetTmpAnmFlags(1,1,1,0,5,1,0)
	demonio.LaunchAnimation("Ldm_appears")
	demonio.AnmEndedFunc=DespiertaDemonio
	demonio.Alpha = 0.0
	demonio.Blind = 1
	demonio.Deaf  = 1
	demonio.SetOnFloor()
	PhantonFX.Delta = 0.005
	PhantonFX.AppearsChar(demonio.Name)
	LanzaMegaSurtidor(demonio.Position[0],demonio.Position[1],demonio.Position[2])
	RugidoDemonio.Position = (demonio.Position[0],demonio.Position[1],demonio.Position[2])
	FireBallCool.Position = (demonio.Position[0],demonio.Position[1],demonio.Position[2])
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, RugidoDemonio.PlaySound,(0,))
	FireBallCool.PlaySound(0)
	print "Aparece "+name

def CoolDemon(name):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, AparicionDemonio, (name,))
	demonio=Bladex.GetEntity(name)
	demonio.UnFreeze()
	demonio.PutToWorld()
	
	
def DespiertaDemonio(ent_name):
	demonio = Bladex.GetEntity(ent_name)
	EnemyTypes.EnemyDefaultFuncs(demonio)
	demonio.Blind = 0
	demonio.Deaf  = 0
	demonio.ImDeadFunc=MuerteDemonio
	print "despierta el "+ent_name

def MuerteDemonio(ent_name):
	demonio=Bladex.GetEntity(ent_name)
	demonio.Data.ImDeadFunc (ent_name)
	AbrePuerta20()
	darfuncs.LuzChapuzera(Bladex.GetEntity("demonpuch"),Bladex.GetTime() + 5.5)

def ElDemonio(sectorindex,entityname):
	if(entityname == "Player1"):
		ELDEMOSEC.OnEnter = ""		
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.9, CoolDemon,("demoniox",))
		CierraPuerta19()
		AbreCam.PTS = [((-37683.0018824, -48213.5031308, 18969.6273073), (-38105.7655164, -49502.7470434, 23269.8444944), 3), ((-35090.6301058, -48222.3047871, 24010.9110696), (-38190.4232553, -49489.547406, 27012.4792809), 3), ((-41208.3660101, -50589.6426227, 22696.1949561), (-39524.139583, -49475.4554887, 26721.5650656), 3)]
		AbreCam.LastTime = 0.01
		AbreCam.AbreCam()
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa4") )

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para chorritos.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def PlaySound(sound,entity,ciclar = 0):
	print "Sonido"
	ent = Bladex.GetEntity(entity)
	sound.Position = ent.Position
	sound.PlaySound(ciclar)	
	

def PlaySoundP(sound,position,ciclar = 0):	
	sound.Position = position
	sound.PlaySound(ciclar)

def CreateCascada(Cascada,p,d,v,pc,Time = 18,Grav = 8000,PPS = 400):
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
	espuma.PPS=40
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10

def CreateEspuma(Espuma,pc,d,PPS = 40):
	espuma=Bladex.CreateEntity(Espuma, "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espuma"
	espuma.PPS=PPS
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada(cascada):
	cascada2 = Bladex.GetEntity(cascada)
	cascada2.SubscribeToList("Pin")
	
	espuma = Bladex.GetEntity(cascada+"Espuma")
	espuma.SubscribeToList("Pin")
	
def ApagaCascadas():
	soundchorro.StopSound()
	BorrarCascada("chorro1")
	BorrarCascada("chorro2")
	BorrarCascada("chorro3")		


def UsePalancaChorritos():
	global GenActivated
	if GenActivated == 1:
		water = Bladex.GetEntity("gen")
		water.TimerFunc = VaciarEstanque2
		water.SubscribeToList("Timer60")
		time = Bladex.GetTime()
		Bladex.AddScheduledFunc(time + 20.0,StopEmptyWater,(0,))

		PlaySoundP(soundvaciado,(-6346,2188,-20235),10)
		GenActivated = 0
		Bladex.GetEntity("Luzg1").SubscribeToList("Pin")
		Bladex.GetEntity("Luzg2").SubscribeToList("Pin")
	elif GenActivated == 2:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,ApagaCascadas,())
		GenActivated = 1		

def CreateParticle(r= 30,g = 40,b = 50,al = 230.0,part = "BubbleParticle"):
	Bladex.AddParticleGType("Espuma2",part,2,8)

	for i in range(8):
		if i < 4:
			aux=1.0 - ((4.0-i)/4.0)
			
		else:
			aux=(4.0-(i-4))/4.0

		size=10+aux*30.0
		Bladex.SetParticleGVal("Espuma2",i,r,g,b,al,size)

def EfectoAgua(espuma,cam,posi,deathtime):
	time = Bladex.GetTime()		

	if time < deathtime:		
		campos = cam.Position
		v=campos[0]-posi[0], 0.0, campos[2]-posi[2]				
		v=B3DLib.Normalize(v)		

		pos = posi[0] + v[0] * 1000,posi[1],posi[2] + v[2] * 1000
		desp = v[2] * -500,v[0] * 500		

		espuma.Position = pos[0] + desp[0],posi[1] - 1400,pos[2] + desp[1]
		espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2

		Bladex.AddScheduledFunc(time + 0.05,EfectoAgua,(espuma,cam,posi,deathtime))

def SaltaAguaGenCho(enmgen):
#def SaltaAguaGenCho():	
	global Esp
	Esp = Esp +1
	
	pos=enmgen.Position	
	#pos = -28900, 1400, -23100
	#pos = char.Position
	cam = Bladex.GetEntity("Camera")
	charpos = cam.Position
	
	v=charpos[0]-pos[0], 0.0, charpos[2]-pos[2]				
	v=B3DLib.Normalize(v)
	
	rpos = pos[0] + v[0] * 800,pos[1],pos[2] + v[2] * 800
	desp = v[2] * -400,v[0] * 400

	espuma=Bladex.CreateEntity("Espuma"+`Esp`, "Entity Particle System D2", rpos[0] + desp[0],pos[1] - 1400,rpos[2] + desp[1])
	espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2
	espuma.ParticleType="Espuma2"
	espuma.PPS=512
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, 0.0, 0.0	
	espuma.RandomVelocity=30.0
	espuma.Time2Live=8
	espuma.DeathTime = Bladex.GetTime() + 5.0	
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,EfectoAgua,(espuma,cam,pos,espuma.DeathTime))

def VaciarEstanque2(Entity,Timer):
	global AlturaWater	
	genwater = Bladex.GetEntity("gen")
	AlturaWater = AlturaWater + DespWater
	#genwater.Position = -4000,AlturaWater,-10500 
	genwater.Position = -2400,AlturaWater,-9900 	

def VaciarEstanque(Entity,Timer):
	global AlturaWater	
	genwater = Bladex.GetEntity("gen")
	AlturaWater = AlturaWater + DespWater2	
	genwater.Position = -4000,AlturaWater,-6000 	

def StopEmptyWater(v):	
	water = Bladex.GetEntity("gen")
	
	if v:
		water.TimerFunc = ""
		water.RemoveFromList("Timer60")	
		soundvaciado.StopSound()
		water.SubscribeToList("Pin")
		print "Vaciado"		
	else:
		water.TimerFunc = VaciarEstanque
		Bladex.AddScheduledFunc(Bladex.GetTime() + 20.0,StopEmptyWater,(1,))		

def ActivateSkeletonCho(entity):
	gen_a_lich = Bladex.GetEntity(entity)
	#EnmGenRnd.ActivateEnemy(gen_a_lich)		
	gen_a_lich.Blind = 0
	gen_a_lich.Deaf = 0

def SkeletonGoTo(entity):
	gen_a_lich = Bladex.GetEntity(entity)
	
	if Point_Gen == 1:
		gen_a_lich.GoTo(-500,3000,-17000)
	else:
		gen_a_lich.GoTo(-500,3000,-20500)

	gen_a_lich.RouteEndedFunc = ActivateSkeletonCho

def GenSklMuerto2(ent_name):
	global N_Lich_Gen
	global Point_Gen	

	
	if (Point_Gen == 2):
		Point_Gen = 0

	pos = PosLichGen[Point_Gen]			
	
	gen_a_lich = EnmGenRnd.CreateEnemy((pos),"Gen1Skl_"+ `N_Lich_Gen`, "Skeleton", "Hacha3", 1, "Escudo4", 1)
	gen_a_lich.Data.ImDeadFuncX = gen_a_lich.ImDeadFunc
	gen_a_lich.ImDeadFunc = GenSklMuerto
	gen_a_lich.Angle = 3
	gen_a_lich.UnFreeze()
		
	SaltaAguaGenCho(gen_a_lich)		
		
	gen_a_lich.LaunchAnimation("Skl_appears1")
	gen_a_lich.AnmEndedFunc = SkeletonGoTo	

	N_Lich_Gen = N_Lich_Gen + 1
	Point_Gen = Point_Gen + 1

def GenSklMuerto(ent_name):
	Bladex.GetEntity(ent_name).Data.ImDeadFuncX(ent_name)

	if (GenActivated == 2):
		Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,GenSklMuerto2,(ent_name,))		

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Chau_Bolu.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def MusicaytextoVampireCobarde():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,GameText.WriteText,("M8T3",))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("playerVampireCobarde"))

def ScreamWyv(camera,frame):
	soundwyvscream.Position = wyv.Position[0],wyv.Position[1],wyv.Position[2]
	soundwyvscream.PlaySound(0)

def OpenCupula(entity,time):
	ent = Bladex.GetEntity(entity)
	ent.RotateRel(11000,0,-11000,0,1,0,0.015)
	ptime = time - ent.Data

	if (ptime >= 133.0 / 40):
		ent.RemoveFromList("TimerCupula")

def ActivateCupula(ent):
	ent.TimerFunc = OpenCupula
	ent.SubscribeToList("TimerCupula")
	ent.Data = Bladex.GetTime()	

def StopWyvScene1(camera,frame):	
	#Scorer.SetVisible(1)
	#Bladex.ActivateInput()
	ScriptSkip.SkipScriptEnd()
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	wyv.TurnOff()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,GotoMapVars.EndOfLevel,())

def FadeLasPelotas(Camera,Frame):
	AuxFuncs.FadeTo(0.5,20)
	
	
def ChangeCameraWyvScene1_6(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("vamp+wyvernCamera06.cam",246,425)

	cam.AddCameraEvent(279 - 246,MontaVamp)
	cam.AddCameraEvent(314 - 246,JumpGroundwvr)
	cam.AddCameraEvent(388 - 246,ScreamWyv)
	cam.AddCameraEvent(415 - 246,FadeLasPelotas)

	cam.AddCameraEvent(349 - 246,PolvusFlap)
	cam.AddCameraEvent(377 - 246,JustFlap)	
	cam.AddCameraEvent(398 - 246,JustFlap)	
	
	cam.AddCameraEvent(-1,StopWyvScene1)


def ChangeCameraWyvScene1_5(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("vamp+wyvernCamera05.cam",191,245)
	cam.AddCameraEvent(207-191,PolvusFlap)
	cam.AddCameraEvent(227-191,HitGroundwvr)
	cam.AddCameraEvent(237-191,HitGroundwvr)
	cam.AddCameraEvent(243-191,SaltaVamp)
	
	
	cam.AddCameraEvent(-1,ChangeCameraWyvScene1_6)


def WyvScene1():	
	global Wyv1Activate

	Scorer.SetVisible(0)
	#Wyv1Activate = 1
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("vamp+wyvernCamera04.cam",0,190)		
	cam.AddCameraEvent(66,JustFlap)
	cam.AddCameraEvent(89,JustFlap)
	cam.AddCameraEvent(107,JustFlap)
	cam.AddCameraEvent(129,JustFlap)
	cam.AddCameraEvent(147,JustFlap)
	cam.AddCameraEvent(166,JustFlap)
	cam.AddCameraEvent(188,JustFlap)

	cam.AddCameraEvent(106,ScreamWyv)
	cam.AddCameraEvent(-1,ChangeCameraWyvScene1_5)

	wyv.Position = -41595.875 ,-64726.145, 53651.363
	wyv.Actor = 1
	wyv.Animation="Wyv_escena01"		
	wyv.SendSectorMsgs=0	
	wyv.TurnOn()		

	darfuncs.HideBadGuy(Drakula.Name)
	Kula = Bladex.CreateEntity("DrkActor","Vamp", -38124.813,-56042.043,19539.436)
	Kula.Position = -38124.813,-56042.043,19539.436
	Kula.Orientation = (0.707388281822, 0.706825196743, 0.0, 0.0)
	Kula.Actor = 1
	Kula.Animation="Vmp_escena01"		
	Kula.SendSectorMsgs=0	
	Kula.TurnOn()		

	OpenDome()

def OpenDome():
	ActivateCupula(c1)
	ActivateCupula(c2)
	ActivateCupula(c3)
	ActivateCupula(c4)
	ActivateCupula(c5)
	ActivateCupula(c6)
	ActivateCupula(c7)
	ActivateCupula(c8)
	soundCupOpen.Position = -42000, -60000, 25064
	soundCupOpen.PlaySound(0)
	soundCupWind.Position = -42000, -60000, 25064
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.9,soundCupWind.PlaySound,(10,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,soundCupOpen.StopSound,())
	

def WyvSceneX(x,y):
	global Drakula
	
	Drakula.Position = -38265,-55600,19000		
	Drakula.Angle = -3.1415
	Drakula.SetOnFloor()
	Drakula.Wuea = Reference.WUEA_ENDED
	Drakula.SetTmpAnmFlags(1,1,1,0,5,1,0)	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,WyvScene1,())
	
def WyvScene():
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("vampiro_cansado.cam",0,-1)
	
	Drakula.Position = -38104.559,-56012.266,19537.438
	Drakula.Angle = -3.1415
	Drakula.SetOnFloor()
	Drakula.Wuea = Reference.WUEA_ENDED
	Drakula.SetTmpAnmFlags(1,1,1,0,5,1,0)		
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.0,Drakula.LaunchAnimation,("Vmp_cansado",))

	cam.AddCameraEvent(-1,WyvSceneX)
	MusicaytextoVampireCobarde()
	
def Chau_BoluDos():
	Bladex.SetListenerPosition(2)
	print "Huye el cabron."
	Bladex.GetEntity("Player1").Position = -150168, 3421, 19938
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(30,))
	darfuncs.HideBadGuy("Player1")
	ScriptSkip.SkipScriptStart("EscenaFinalIsla")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.4,WyvScene,())
	
	AuxFuncs.FadeFrom(0.5,0.5)

	Drakula=Bladex.GetEntity("Drakula")
	DesapareceDrakula()
	Drakula=Bladex.GetEntity("DrakulaX")
	ApareceDrakula()
	

def Chau_Bolu():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.6,Chau_BoluDos,())
	AuxFuncs.FadeTo(0.5,0.2)


def PolvusFlap(x,y):
	dust.RemueveTierraGen(-42000, -55000, 25064,2500,2500,1024,"FastDust",16,0.1)	
	soundwyvflap.Position = wyv.Position[0],wyv.Position[1],wyv.Position[2]
	soundwyvflap.PlaySound(0)

def JustFlap(x,y):
	soundwyvflap.Position = wyv.Position[0],wyv.Position[1],wyv.Position[2]
	soundwyvflap.PlaySound(0)

def HitGroundwvr(x,y):
	soundwyvHit.Position = wyv.Position[0],wyv.Position[1],wyv.Position[2]
	soundwyvHit.PlaySound(0)

def JumpGroundwvr(x,y):
	soundwyvJump.Position = wyv.Position[0],wyv.Position[1],wyv.Position[2]
	soundwyvJump.PlaySound(0)
	
def SaltaVamp(x,y):
	soundVmpSalta.Position = Drakula.Position[0],Drakula.Position[1],Drakula.Position[2]
	soundVmpSalta.PlaySound(0)
		
def MontaVamp(x,y):
	soundVmpMonta.Position = Drakula.Position[0],Drakula.Position[1],Drakula.Position[2]
	soundVmpMonta.PlaySound(0)

def CreaNubes(x,y,z   ,sx,sz,pps):

	tierra1=Bladex.CreateEntity("TierraRemoviendose1", "Entity Particle System D3", x +sx, y, z + sz)
	tierra1.D1= -2*sx, 0, 0
	tierra1.D2= -2*sx, - 2*sz, 0
	tierra1.ParticleType="Coulds"
	tierra1.PPS=pps
	tierra1.YGravity=0.0
	tierra1.Friction=0.0
	tierra1.Velocity=0.0, 0.0, -10000.0
	tierra1.RandomVelocity=0.0
	tierra1.Time2Live=300
	


	tierra2=Bladex.CreateEntity("TierraRemoviendose2", "Entity Particle System D3", x + sx, y, z + sz)
	tierra2.D1= -2*sx, - 2*sz, 0
	tierra2.D2=     0, - 2*sz, 0
	tierra2.ParticleType="Coulds"
	tierra2.PPS=pps
	tierra2.YGravity=0.0
	tierra2.Friction=0.0
	tierra2.Velocity=0.0, 0.0, -10000.0
	tierra2.RandomVelocity=0.0
	tierra2.Time2Live=300
	
	return (tierra1,tierra2)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para celdas.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrerejasi1():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejasi2():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abrerejasi3():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrerejasi4():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto reja4din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def Cierrarejasi1():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 8000)
	
	#sonidos asociados a la puerta-objeto rejasi1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejasi2():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 8000)

	#sonidos asociados a la puerta-objeto rejasi2din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrarejasi3():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 8000)

	#sonidos asociados a la puerta-objeto rejasi3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrarejasi4():

	desplazamientos=(1200.0, 1010.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(4000.0, 8000)

	#sonidos asociados a la puerta-objeto rejasi4din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rejasi4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Abreladosr1():
	Abrerejasi1()
	Abrerejasi3()

	
def Abreladosr2():
	Abrerejasi2()
	Abrerejasi4()	
	
def Cierraladosr1():
	Cierrarejasi1()
	Cierrarejasi3()
	
def Cierraladosr2():
	Cierrarejasi2()
	Cierrarejasi4()	


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para bgates.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def dustTriangle (name,p1,p2,p3):
	print(p1)
	print(p2)
	print(p3)
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
	

	bgateA1.DoBreak((0,0,2.0), (-10000,10500,-42312), (0.0, 0.0, 0.0))
	bgateA2.DoBreak((0,0,4.0), (-8750,10500,-42312), (0.0, 0.0, 0.0))

	p0 = -11000,12400,42560
	p1 = -11000,9000,42560
	p2 = -8250,12400,42560
	p3 = -8250,9000,42560

	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)
		
	bgateA.OnHit = ""
		
	break_sound.Position = px,py,pz
	break_sound.PlaySound(0)
	
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para antorchas.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

############################################
def Apagala(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)	
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingueAntorcha"


def Apagala2(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)	
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingueAntorcha"

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para InicioScene.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def StopCameraInicio(Camera,Frame):
	global crowinicio2
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	#crowinicio2.SubscribeToList("Pin")
	#crowinicio2 = None
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

	#global ladosCerrados	
	#ladosCerrados=0
	char.SetOnFloor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("atm32") )

	
def Cierrareja3Puta(Camera,Frame):
	Cierrareja3()

def Musicaytexto():	
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("isla-carga"))	
	GameText.WriteText("M8T1")	

def SegundaCamaraInicio(a,b):	
	print "Lanza Segunda Camara Inicio"	
	cam = Bladex.GetEntity("Camera")	
	cam.SetMaxCamera("isla_Camera_volar_isla02.cam",101,800)		
	cam.AddCameraEvent(757-101,Cierrareja3Puta)	
	cam.AddCameraEvent(-1,StopCameraInicio)		
	











def StartInicio():					
	char.Position = -156551,3419,8985
	char.Angle = 3.1415
	char.Wuea = Reference.WUEA_ENDED	
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)

	char.LaunchAnmType("start_isla")
	char.Position = -156551,3419,8985	
	char.SetOnFloor()	

	crowinicio2.RemoveFromWorld()	                ### PLAGUE: I like crows. why remove them?
	#crowinicio2.Actor=1
	#crowinicio2.Animation="Crw_start_pic"
	#crowinicio2.FPS=20.0	
	#crowinicio2.SendSectorMsgs=0
	#crowinicio2.TurnOn()
	
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_Camera_volar_isla01.cam",0,100)	
	cam.AddCameraEvent(-1,SegundaCamaraInicio)	            ### PLAGUE: makes no sense, there's a nice shot of the entire Island which gets immediately cut away from.
	#print "Lanza Camara Inicio"	
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, Musicaytexto,())

	Bladex.SetListenerPosition(2)

def ParchePrecarga():
	ScriptSkip.SkipScriptStart("EscenaInicioIsla")	
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	# Bladex.SetListenerPosition(2) 
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_Camera_volar_isla01.cam",0,1)
	AuxFuncs.FadeFrom(10,10)
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, StartInicio,())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para WyvCiclica.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ScreamWyv2(camera,frame):
	wyv2 = Bladex.GetEntity("Wyv2")
	if wyv2:
		soundwyvscream2.Position = wyv2.Position[0],wyv2.Position[1],wyv2.Position[2]
		soundwyvscream2.PlaySound(0)	

def SetUpScreamEvents():
	time = Bladex.GetTime()
	if(Bladex.GetEntity("Wyv2")):
		Bladex.AddScheduledFunc(time +   20.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time +  221.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time +  364.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time +  506.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time +  621.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time +  750.0/20.0,ScreamWyv2,(0,0))
		Bladex.AddScheduledFunc(time + 1148.0/20.0,ScreamWyv2,(0,0))
	
		Bladex.AddScheduledFunc(time + 1200.0/20.0,SetUpScreamEvents,())


def WyvScene3b():
	wyv2.Actor = 0
	wyv2.Orientation = 0.7,0.7,0,0
	#wyv2.Position = -102789,-8680,21818	
	#wyv2.Position = -102789,-7680,21818	
	wyv2.Position = -42454,-30143,95026
	wyv2.Actor = 1
	wyv2.Animation="Wyv_escena03b_island"	
	#wyv2.Frame = 156.0
	wyv2.SendSectorMsgs=0
	wyv2.TurnOn()
	SetUpScreamEvents()

def WyvScene3a():	
	wyv2.Actor = 0
	wyv2.Orientation = 0.7,0.7,0,0
	#wyv2.Position = -81509.660207, -21665.0977195, 17168.56574	
	wyv2.Position = -81509.660207, -20665.0977195, 17168.56574	
	wyv2.Actor = 1
	wyv2.Animation="Wyv_escena03a_island"
	wyv2.SendSectorMsgs=0	
	wyv2.TurnOn()
	
	#wyv2.RotateRel(0,0,0,1,0,0,0.0001)

	Bladex.AddScheduledFunc(Bladex.GetTime() + 304.0/20.0,WyvScene3b,())
	
	
def WyvScene2():		
	wyv2.Position = -6012.023,-14213.682,-69911.445
	wyv2.Actor = 1
	wyv2.Animation="Wyv_escena02a"
	wyv2.SendSectorMsgs=0
	wyv2.TurnOn()

	time = Bladex.GetTime()		

	Bladex.AddScheduledFunc(time + 101.0/30.0,ScreamWyv2,(0,0))
	Bladex.AddScheduledFunc(time + 397.0/30.0,ScreamWyv2,(0,0))
	Bladex.AddScheduledFunc(time + 676.0/30.0,ScreamWyv2,(0,0))
	Bladex.AddScheduledFunc(time + 1075.0/30.0,WyvScene3a,())

def WyvCiclica(sector,entity):
	if entity == "Player1":
		SecWyvCiclica.OnEnter = ""
		WyvScene2()

def WyvSeVaATPC(sector,entity):
	if entity == "Player1":
		SecWyvSeVaATPC.OnEnter = ""
		Bladex.GetEntity("Wyv2").SubscribeToList("Pin")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para vamp_cool.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def MusicaytextoVampirazo():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("isla-vampiroc"))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 10.0,GameText.WriteText,("M8T2",))

def HideVampiro(Camera,Frame):
	Drakula.Alpha = 0.0
	Bladex.GetEntity(Drakula.InvRight).Alpha = 0
	Bladex.GetEntity(Drakula.InvLeft ).Alpha = 0

def UnhideVampiro(Camera,Frame):	
	Drakula.Alpha = 1.0
	Bladex.GetEntity(Drakula.InvRight).Alpha = 1.0
	Bladex.GetEntity(Drakula.InvLeft ).Alpha = 1.0


def StopVampiro(Camera,Frame):	
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()		
	Scorer.SetVisible(1)

	EnemyTypes.EnemyDefaultFuncs(Drakula)
	Drakula.DamageFunc    = VampDamage
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("1kd") )
	global OldShadow
	Bladex.SetDrawObjectShadows(OldShadow)
	
	
def VampCamera6(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera5.cam",321,-1)
	cam.AddCameraEvent(-1,StopVampiro)
	cam.AddCameraEvent(333 - 321,UnhideVampiro)
	Drakula.SetOnFloor()
	Drakula.Move(0,100,0)
	HideVampiro(0,0)	

def VampCamera5(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera4.cam",276,320)
	cam.AddCameraEvent(-1,VampCamera6)
	UnhideVampiro(0,0)

def VampCamera4(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera2.cam",236,275)
	cam.AddCameraEvent(-1,VampCamera5)


def VampCamera3(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera3.cam",195,235)
	cam.AddCameraEvent(-1,VampCamera4)
	
	HideVampiro(0,0)


def VampCamera2(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera2.cam",151,194)
	cam.AddCameraEvent(-1,VampCamera3)	
	
def DesapareceDrakula():
	Drakula.Freeze()
	Drakula.RemoveFromWorld()
	if Drakula.InvRight:
		Bladex.GetEntity(Drakula.InvRight).RemoveFromWorld()
	if Drakula.InvLeft:
		Bladex.GetEntity(Drakula.InvLeft ).RemoveFromWorld()

def ApareceDrakula():
	Drakula.UnFreeze()
	Drakula.PutToWorld()
	if Drakula.InvRight:
		Bladex.GetEntity(Drakula.InvRight).PutToWorld()
	if Drakula.InvLeft:
		Bladex.GetEntity(Drakula.InvLeft ).PutToWorld()	

def AparicionVampiro(Sector,Entity):	
	global tLaunched
	if ((Entity == "Player1") and (tLaunched==1)):
		ApareceDrakula()
		HideVampiro(0,0)
		ScriptSkip.SkipScriptStart("EscenaApareceVamp")
		#Bladex.DeactivateInput()		
		Scorer.SetVisible(0)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.01,DrakulasCoolAppears,())
		VampSector.OnEnter = ""
		global OldShadow
		OldShadow = Bladex.GetDrawObjectShadows()
		Bladex.SetDrawObjectShadows(1)
		

def DrakulasCoolAppears():
	Drakula.Position = -48172,-56188,39556
	Drakula.Angle = 3.1415
	Drakula.SetOnFloor()
	Drakula.Wuea = Reference.WUEA_ENDED
	Drakula.SetTmpAnmFlags(1,1,1,0,5,1,0)
	Drakula.LaunchAnimation("Vmp_aparicion_vampiro")
	
	char.Angle = 1.38
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("aparicion_vampiro")
	char.Position = -42298,-56105,24866
	char.SetOnFloor()
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("isla_vampiro_Camera1.cam",0,150)
	cam.AddCameraEvent(-1,VampCamera2)
	UnhideVampiro(0,0)	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.0,MusicaytextoVampirazo,())

def CreateDrakula(aditive=""):
	global Drakula
	hacha   = Bladex.CreateEntity("VampWeapon"+aditive, "VampWeapon", 0, 0, 0,"Weapon")
	escudo = Bladex.CreateEntity("VampShield"+aditive, "VampShield", 0, 0, 0,"Weapon")
	Drakula = Bladex.CreateEntity("Drakula"+aditive, "Vamp", -38265,-55600,19000,"Person")
	Drakula.Blind         = 0
	Drakula.Deaf          = 0
	Drakula.Angle         = -3.14159
	Drakula.Alpha         = 1.0
	Drakula.Level         = 2
	ItemTypes.ItemDefaultFuncs(hacha)
	ItemTypes.ItemDefaultFuncs(escudo)
	Actions.TakeObject(Drakula.Name, hacha.Name)
	Actions.TakeObject(Drakula.Name, escudo.Name)
	#EnemyTypes.EnemyDefaultFuncs(Drakula)
	AniSound.AsignarSonidosVampiro(Drakula.Name)
	Drakula.SetOnFloor()
	DesapareceDrakula()

def VampDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	global LifeLimit
	
	#pdb.set_trace()
	x = Damage.CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
	#Damage.CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
	Drakula.Life= max(1,Drakula.Life)
	print "vamp:",Drakula.Life
	if Drakula.Life < LifeLimit:
		Drakula.Blind=1
		Drakula.Deaf=1
		Drakula.InterruptCombat()
		Drakula.Alpha=1.0
		Drakula.AttackList= []
		Chau_Bolu()
		Drakula.DamageFunc = Damage.CalculateDamage                     ### PLAGUE: This causes multi-hit combos to dismember the vamp in cutscenes. Needs fix?
	return 0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ShadowVamp.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def StopVampShadow(Camera,Frame):	
	global OldShadow
	Bladex.SetDrawObjectShadows(OldShadow)
	
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()	
	vamp_sha.SubscribeToList("Pin")
	Scorer.SetVisible(1)
	Bladex.ActivateInput()
	ApagaLucesVampirescas()
	CierraPuertaLlave8()
	AndaSkelarquero()

def VampiroShadow(Sector,Entity):

	if (Entity == "Player1"):
		VSha.OnEnter = ""
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa10") )
		#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb4") )
		#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("atm9") )	

		char.Position = -21470,-23579,30613
		char.Angle = 3.141592/2
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)

		char.LaunchAnmType("sombra_vampiro")
		char.SetOnFloor()

		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("isla_Camera_vuelo.cam",0,-1)
		vamp_sha.Position = -42905,-34704,25328
		vamp_sha.Angle = Ang2 #28,143 grados.	
		vamp_sha.Wuea = Reference.WUEA_ENDED
		vamp_sha.SetTmpAnmFlags(1,1,1,0,5,1)
		vamp_sha.LaunchAnimation("Vmp_sombra")
		vamp_sha.SetOnFloor()
		
		cam.AddCameraEvent(-1,StopVampShadow)
		Bladex.DeactivateInput()

		Scorer.SetVisible(0)

		global OldShadow
		OldShadow = Bladex.GetDrawObjectShadows()
		Bladex.SetDrawObjectShadows(1)

		
		
def ApagaLucesVampirescas():
	OnOff.TurnOffLight("ltorre1")
	OnOff.TurnOffLight("ltorre2")
	OnOff.TurnOffLight("ltorre3")
	OnOff.TurnOffLight("ltorre4")
	OnOff.TurnOffLight("ltorre5")
	OnOff.TurnOffLight("ltorre6")
	OnOff.TurnOffLight("ltorre7")
	OnOff.TurnOffLight("ltorre8")
	OnOff.TurnOffLight("ltorre9")
	OnOff.TurnOffLight("ltorre10")
	OnOff.TurnOffLight("ltorre11")
	OnOff.TurnOffLight("ltorre12")
	OnOff.TurnOffLight("ltorre13")
	OnOff.TurnOffLight("ltorre14")
	OnOff.TurnOffLight("ltorre15")
	OnOff.TurnOffLight("ltorre16")
	OnOff.TurnOffLight("ltorre17")
	OnOff.TurnOffLight("ltorre18")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para rastrillo.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrereja3():

	desplazamientos=(2000.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja3():


	desplazamientos=(2000.0, 2000.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierralados(index,entity):
	global ladosCerrados
	if (ladosCerrados==0) :
		Cierrareja3()
		ladosCerrados=1


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrerast91():

	desplazamientos=(1150.0, 1150.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rast91
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast91din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	
def Cierrarast91():

	desplazamientos=(1150.0, 1150.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto rast91
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rast91din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def AbrePuertaLlave1():
	puerta1.OpenDoor()

def CierraPuertaLlave1():
	puerta1.CloseDoor()
	
def AbrePuerta2():
	puerta2.OpenDoor()

def CierraPuerta2():
	puerta2.CloseDoor()
	
def AbrePuertaLlave3():
	puerta3.OpenDoor()
	Abrerast91()
	darfuncs.UnhideBadGuy("Zombi17")

def CierraPuertaLlave3():
	puerta3.CloseDoor()

def ParaArenillaPuerta4():
	global arenillapuerta4
	arenillapuerta4.DeathTime=Bladex.GetTime()+1.0/60.0

def AbrePuerta4():
	global arenillapuerta4
	arenillapuerta4=Bladex.CreateEntity("ArenillaPuerta4", "Entity Particle System D2", -14300.0, -13990.0, 29600.0)
	arenillapuerta4.D=0.0, 0.0, 2450.0
	arenillapuerta4.ParticleType="Sand"
	arenillapuerta4.YGravity=4900.0
	arenillapuerta4.Friction=0.2
	arenillapuerta4.RandomVelocity=10.0
	arenillapuerta4.PPS=512
	arenillapuerta4.Time2Live=32
	puerta4.OpenDoor()

def CierraPuerta4_2():
	ParaArenillaPuerta4()
	polvareda=Bladex.CreateEntity("PolvoPuerta4", "Entity Particle System D2", -14300.0, -10600.0, 29600.0)
	polvareda.D=0.0, 0.0, 2450.0
	polvareda.ParticleType="MediumDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=512
	polvareda.Velocity=0.0, -1000.0, -1000.0
	polvareda.RandomVelocity=30.0
	polvareda.Time2Live=30
	polvareda.DeathTime=Bladex.GetTime()+3.0/60.0

def CierraPuerta4():
	global arenillapuerta4
	arenillapuerta4=Bladex.CreateEntity("Arenilla4", "Entity Particle System D2",  -14300.0, -13990.0, 29600.0)
	arenillapuerta4.D=0.0, 0.0, 2450.0
	arenillapuerta4.ParticleType="Sand"
	arenillapuerta4.YGravity=4900.0
	arenillapuerta4.Friction=0.2
	arenillapuerta4.RandomVelocity=10.0
	arenillapuerta4.PPS=512
	arenillapuerta4.Time2Live=32
	puerta4.CloseDoor()

def AbrePuerta5():
	puerta5.OpenDoor()


def CierraPuerta5():
	puerta5.CloseDoor()


def AbrePuerta7():
	puerta7.OpenDoor()


def CierraPuerta7():
	puerta7.CloseDoor()

def AbrePuertaLlave8():
	puerta8.OpenDoor()

def CierraPuertaLlave8():
	puerta8.CloseDoor()

def AbrePuerta12(sectorindex,entityname):
	if entityname=='Player1':
		puerta12.OpenDoor()

def AbrePuerta13():
	global ladoABIERTO
	if (ladoABIERTO==0) :
		puerta13.OpenDoor()
		puerta14.OpenDoor()
		ladoABIERTO=1

		
def EntroEnTriggerSector(trsector_name, entity_name):
	print("entidad:"+entity_name+", en sector"+trsector_name);
	if (entity_name<>"Player1") : return
	AbrePuerta13()

def AbrePuerta15(sectorindex,entityname):
	if entityname=='Player1':
		puerta15.OpenDoor()

def CierraPuerta16(sectorindex,entityname):
	if entityname=='Player1':
		puerta16.CloseDoor()

def CierraPuerta17(sectorindex,entityname):
	if entityname=='Player1':
		puerta17.CloseDoor()

def CierraPuerta18(sectorindex,entityname):
	if entityname=='Player1':
		puerta18.CloseDoor()

def CierraPuerta19():
	puerta19.CloseDoor()

def AbrePuerta20():
	puerta20.OpenDoor()
	puertai20.OpenDoor()

def CierraPuerta20():
	puerta20.CloseDoor()
	puertai20.CloseDoor()


def AbrePuerta21():
	puerta21.OpenDoor()


def CierraPuerta21():
	puerta21.CloseDoor()

def AbrePuertaLlave22():
	puerta22.OpenDoor()

def CierraPuertaLlave22():
	puerta22.CloseDoor()

def Abrerast23():

	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rast23
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast23din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	
def Cierrarast23():

	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto rast1
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rast23din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def AbrePuertaCHI():
	puerta24.OpenDoor()
	puerta25.OpenDoor()

def CierraPuertaCHI():
	puerta24.CloseDoor()
	puerta25.CloseDoor()
	
	
def AbrePuertasTrono():
	puerta26.OpenDoor()
	puerta27.OpenDoor()
	puerta28.OpenDoor()
	puerta29.OpenDoor()
	puerta30.OpenDoor()
	puerta31.OpenDoor()
	
	
def AbrePuertaTRO():
	puerta32.OpenDoor()

def CierraPuertaTRO():
	puerta32.CloseDoor()

def AbrePuerta33():
	puerta33.OpenDoor()

def CierraPuerta33():
	puerta33.CloseDoor()
	
def Abrereja34():
	desplazamientos=(2000.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rast34din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rast34din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puente.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

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


def AperturaStep(e_name, time):
  global p_num_frames
  global p_counter
  
  if(p_counter==10):
     looppuentelevadizo.StopSound()
     if(p_num_frames>0):
        dust.RemueveTierraGen(-89389-500, -500, 30746,100,1800,32)
        golpepuentelevadizo.PlaySound(0)
     else:
     	atranquepuentelevadizo.PlaySound(0)
  if(p_counter>0):    
        pte.RotateRel(0,7100,0,1,0,0,(3.14159/2-0.115)/p_num_frames)
  elif(p_counter>-5):
        pte.RotateRel(0,7100,0,1,0,0,-(3.14159/4-0.115)/p_num_frames)        
  elif(p_counter>-18):
        pte.RotateRel(0,7100,0,1,0,0,(3.14159/4-0.115)/p_num_frames)
        p_counter=p_counter-1
  else:
        pte.TimerFunc = ""
        pte.RemoveFromList("Timer60")           # Now done at 60fps for smoothness. -LeadHead
        pte2=Bladex.GetEntity("PuenteFalso")
        if pte2:
        	pte2.SubscribeToList("Pin")

        
  p_counter=p_counter-1
 
def AbrePuente(sectorindex,entityname):
        global p_num_frames
        global p_counter
        
        if entityname=='Player1':
                pte.TimerFunc = AperturaStep
                p_num_frames = 256              # Now done at 60fps for smoothness.
                p_counter = 260                 #
                pte.SubscribeToList("Timer60")  #       -LeadHead
                looppuentelevadizo.PlaySound(10)
                sopen.OnEnter=""

def CierraPuente(sectorindex,entityname):
        global p_num_frames
        global p_counter
        
        if entityname=='Player1':
                looppuentelevadizo.PlaySound(10)
                pte.TimerFunc = AperturaStep
                p_num_frames = -256             # Now done at 60fps for smoothness.
                p_counter = 260                 #
                pte.SubscribeToList("Timer60")  #       -LeadHead
                sclose.OnEnter=""

                pte2              = Bladex.CreateEntity("PuenteFalso","PuenteFernando",-80728.454000,-4556.012000,30535.204000)
                pte2.Static       = 1
                pte2.Scale        = 0.645445
                pte2.Orientation  = 0.706434,0.030844,0.706434,-0.030844
                pte2.Alpha        = 0.0
                pte2.RasterMode   = "AdditiveAlpha"
                pte2.RasterMode   = "Read"
                pte2.CastShadows  = 0
                


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ptatabl.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AbrePuertadoble():
	puertadoble1.OpenDoor()
	puertadoble2.OpenDoor()

def CierraPuertadoble():
	puertadoble1.CloseDoor()
	puertadoble2.CloseDoor()

def ExisteObjeto(obj):
	si = 0
	for x in obj:
		if Bladex.GetEntity(x)!=None:
			si = 1
	return si
		
def PonerBotonTablilla():
	o=Bladex.CreateEntity("bloqueta","AdoquinRuna",-3748.921547,7385.940768,-394.205872,"Physic")
	o.Scale=1.000000
	o.Orientation=0.495618,0.495618,-0.504344,0.504344
	
	buttonta=Button.CreateButtonCombination(0,AbrePuertadoble,"")
	buttonta.AddButton("bloqueta",3,(0,0,1),400,0,0,1)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para prisioneros.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

### PLAGUE: Prisoners.py contains agony sound 3. Need to un-comment it and create a script that selects the sound by random.


def PrsHerido(entity_name):
  person=Bladex.GetEntity(entity_name)
  person.Data.Agoniza(entity_name)

def PrsMatado(entity_name):
  person=Bladex.GetEntity(entity_name)
  person.Data.Muere(entity_name)

def QuejaPeriodica(prisionero):
  if prisionero.Data.Muerto:
    return
  prisionero.Data.Agoniza(prisionero.Name)
  variation=whrandom.uniform(-2.0, 15.0)        # Was -5.0 , 5.0 -LeadHead
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
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=-150177.953, 3383.60595, 17967.7180	# inicio
	#char.Position=24867.5430817, 13452.7112861, -26086.136191
	Doors.Restore()

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-75641.178, -7721.5689, 30799.030	# sobre la muralla
	Doors.Restore()

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-37750,-5516.19,27000			# sala trono
	Doors.Restore()

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=-38259.4561, 1900.07361, 2728.1524	# subterraneos
	Doors.Restore()

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-11000,-12000,30750			# pasarela 2ª planta
	Doors.Restore()

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-19648.1960, -23620.5353, 30660.9485	# pasarela 3ª planta
	Doors.Restore()

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=-48707.711, -37614.317, 31052.851	# elevador
	Doors.Restore()

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-27500, -58000, 29000			# final
	Doors.Restore()




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para MScene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def MusicaytextoA():	
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("isla-mural"))
	GameText.WriteText("M8T4")

def tLaunchPersAnim() :
	global tCharAngle
	global player
	char = Bladex.GetEntity("Player1")
	char.Position = -27602.893,-57360.297,40259.102
	char.Angle = tCharAngle
	char.SetTmpAnmFlags(1,1,1,0,5,1)

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("isla-mural"))

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, MusicaytextoA,())
	char.LaunchAnmType("isla_mira_mural")
	char.SetOnFloor()

def tLaunchCamReset(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	puerta35.CloseDoor()
	GotoMapVars.MapText(-1,"ISLANDMURAL")


def tLaunchCamH(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Detalle mural5.cam",833,1000)
	cam.AddCameraEvent(-1,tLaunchCamReset)
	
def tLaunchCamG(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Detalle mural4.cam",697,832)
	cam.AddCameraEvent(-1,tLaunchCamH)
	
def tLaunchCamF(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Camera2.cam",489,696)
	cam.AddCameraEvent(-1,tLaunchCamG)
	
def tLaunchCamE(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Detalle mural3.cam",408,488)
	cam.AddCameraEvent(-1,tLaunchCamF)

def tLaunchCamD(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Detalle mural2.cam",321,407)
	cam.AddCameraEvent(-1,tLaunchCamE)

def tLaunchCamC(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Detalle mural1.cam",235,320)
	cam.AddCameraEvent(-1,tLaunchCamD)

def tLaunchCamB(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Camera2.cam",81,234)
	cam.AddCameraEvent(-1,tLaunchCamC)

def tLaunchCamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Isla_Camera1.cam",0,80)
	cam.AddCameraEvent(-1,tLaunchCamB)
	
	ScriptSkip.SkipScriptStart("EscenaMuralHero")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)

def tLaunchB() :
	Bladex.ActivateInput()
	tLaunchCamA()
	tLaunchPersAnim()

def tLaunch(index, ent) :
	global tLaunched
	if (ent<>"Player1") : return
	if (tLaunched) : return
	tLaunched=1
	Bladex.DeactivateInput()
	char = Bladex.GetEntity("Player1")
	Actions.FreeBothHands("Player1")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, tLaunchB, ())


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************				        **************************
#*******************************   Definiciones para fuentes.py         **************************
#*******************************				        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateFuente(FuenteN,p,d,v,pc,Time = 18,Grav = 8000,PPS = 400):
	Fuente=Bladex.CreateEntity(FuenteN, "Entity Particle System D2",p[0],p[1],p[2])
	Fuente.D=d[0],d[1],d[2]
	Fuente.ParticleType="GUATERCL"
	Fuente.Friction=0.07
	Fuente.RandomVelocity=10.0
	Fuente.Velocity=v[0],v[1],v[2]
	Fuente.PPS=PPS
	Fuente.YGravity=Grav
	Fuente.Time2Live=Time

	EspumaCL=Bladex.CreateEntity(FuenteN+"EspumaCL", "Entity Particle System D2",pc[0],pc[1],pc[2])
	EspumaCL.D=d[0],d[1],d[2]
	EspumaCL.ParticleType="EspumaCL"
	EspumaCL.PPS=40
	EspumaCL.YGravity=0.0
	EspumaCL.Friction=0.07
	EspumaCL.Velocity=0.0, -1000.0, 0.0
	EspumaCL.RandomVelocity=30.0
	EspumaCL.RandomVelocity_V=30.0
	EspumaCL.Time2Live=10

def CreateEspumaCL(EspumaCL,pc,d,PPS = 40):
	EspumaCL=Bladex.CreateEntity(EspumaCL, "Entity Particle System D2",pc[0],pc[1],pc[2])
	EspumaCL.D=d[0],d[1],d[2]
	EspumaCL.ParticleType="EspumaCL"
	EspumaCL.PPS=PPS
	EspumaCL.YGravity=0.0
	EspumaCL.Friction=0.07
	EspumaCL.Velocity=0.0, -1000.0, 0.0
	EspumaCL.RandomVelocity=30.0
	EspumaCL.RandomVelocity_V=30.0
	EspumaCL.Time2Live=10


def BorrarFuente(Fuente):
	Fuente = Bladex.GetEntity(Fuente)
	Fuente.SubscribeToList("Pin")
	
	EspumaCL = Bladex.GetEntity(Fuente+"EspumaCL")
	EspumaCL.SubscribeToList("Pin")
	
	
	
	
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Pocimas.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************					**************************
#*******************************   Definiciones para BreakDoors.py      **************************
#*******************************					**************************
#*************************************************************************************************
#*************************************************************************************************
"""

def SklBreakDoor():
	if Entity == "Player1":
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")
		
		
"""




def SaleEsqueletoMaloso():
	cgateA1.DoBreak((-55,0,0), (-15750,1100,6500), (0.0, 0.0, 0.0))
	Bladex.KillMusic()    # Added -LeadHead
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb6") )
	darfuncs.UnhideBadGuy("Skeleton94")
	pers = Bladex.GetEntity("Skeleton94")
	pers.Angle = 1.6
	pers.LaunchAnmType("g_22")
	pers.SetActiveEnemy("Player1")
	
	darfuncs.UnhideBadGuy("Skeleton90")
	#pers = Bladex.GetEntity("Skeleton90")
	#pers.Angle=1.71
	#pers.LaunchAnmType("g_22")
	
	darfuncs.UnhideBadGuy("Skeleton91")
	#pers = Bladex.GetEntity("Skeleton91")
	#pers.Angle=0.65
	#pers.LaunchAnmType("g_22")




def ActivaSectorEsqueletoMaloso():
	darfuncs.EnterSecEvent(-20500,0,-7000,SaleEsqueletoMaloso)

