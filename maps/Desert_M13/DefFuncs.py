##///
##||| Desert_M13/DEFFUNCS.PY TITANIUM
##||| Change list:
##||| * Amber key cutscene now plays at 60fps.
##||| * 
##||| * 
##||| * 
##\\\ 


import Auras
import Reference
import B3DLib
import ScriptSkip

###############################################################################
###                     antorchas.py
###############################################################################

def Apagala(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)
	print entityname
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingueAntorcha"


###############################################################################
###                     bgates.py
###############################################################################
import def_class

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

def revientaPuertaA(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global n_hit_sound
	global LifeGateA	
	
	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta
	
	
	LifeGateA = LifeGateA - 1
	
	if (LifeGateA <= 0):	
		bgateA1.DoBreak((5,0,0), (px, py, pz), (0.0, 0.0, 0.0))		#DIRECCION DE LA ROTURA
		bgateA2.DoBreak((5,0,0), (px, py, pz), (0.0, 0.0, 0.0))

		p0 = 15750,-3500,72500		#PUNTOS DE LAS PARTICULAS DE POLVO
		p1 = 15750,-7300,72500
		p2 = 15750,-3500,70250
		p3 = 15750,-7300,70250

		dustTriangle("rppolvo1",p0,p1,p2)
		dustTriangle("rppolvo2",p3,p1,p2)

		break_sound.Position = px,py,pz
		break_sound.PlaySound(0)
	else:		
		hit_sound[n_hit_sound].Position = px,py,pz		
		hit_sound[n_hit_sound].PlaySound(0)

		if n_hit_sound:
			n_hit_sound = 0
		else:
			n_hit_sound = 1		

def revientaPuertaB(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global n_hit_sound
	global LifeGateB

	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta
	

	LifeGateB = LifeGateB - 1
	
	if (LifeGateB <= 0):
		bgateB1.DoBreak((4, 0.0, 0), (px, py, pz), (0.0, 0.0, 0.0))
		bgateB2.DoBreak((4, 0.0, 0), (px, py, pz), (0.0, 0.0, 0.0))
		
		p0 = 15750,-3500,96750
		p1 = 15750,-7300,96750
		p2 = 15750,-3500,94250
		p3 = 15750,-7300,94250

		dustTriangle("rppolvo3",p0,p1,p2)
		dustTriangle("rppolvo4",p3,p1,p2)

		break_sound.Position = px,py,pz
		break_sound.PlaySound(0)
	else:
		hit_sound[n_hit_sound].Position = px,py,pz
		hit_sound[n_hit_sound].PlaySound(0)

		if n_hit_sound:
			n_hit_sound = 0
		else:
			n_hit_sound = 1		

def revientaPuertaC(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global n_hit_sound
	global LifeGateC

	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta
	bgateC1.DoBreak((-5,0,0), (px, py, pz), (0.0, 0.0, 0.0))
	bgateC2.DoBreak((-5,0,0), (px, py, pz), (0.0, 0.0, 0.0))

	p0 = -67250,-3500,85250
	p1 = -67250,-7300,85250
	p2 = -67250,-3500,83000
	p3 = -67250,-7300,83000

	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)

	break_sound.Position = px,py,pz
	break_sound.PlaySound(0)

def revientaPuertaD(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	global n_hit_sound
	global LifeGateD

	if (Bladex.GetEntity(entity_name).Parent!="Player1"):return		# el arma es la que colisiona con la puerta
	
	bgateD1.DoBreak((-5,0,0), (px, py, pz), (0.0, 0.0, 0.0))
	
	p0 = -37750,-3000,114500
	p1 = -37750,-8000,114500
	p2 = -37750,-3000,117400
	p3 = -37750,-8000,117400
	
	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)
	
	break_sound.Position = px,py,pz
	break_sound.PlaySound(0)
			
###############################################################################
###                     chorritos.py
###############################################################################

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
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")
	
	espuma = Bladex.GetEntity(cascada+"Espuma")
	espuma.SubscribeToList("Pin")



###############################################################################
###                     Crows.py
###############################################################################
def AnmEndF1(name):
	EspantarCuervo1()

def AnmEndF2(name):
	EspantarCuervo2()

def ActivarCuervos1(SectorIndex,EntityName):
	global CuervosStatus
	if (CuervosStatus==0):
		CuervosStatus=1
		corpse1.SubscribeToList("TimerCuervos")
		
def AsustarCuervos(time):
	global timer1
	global corpse1
	if (timer1==0.0):
		timer1=time
		cuervo1_sound.Play(-3180,6800,-125800,0)
		crow1.ClearPath();
		crow1.FPS=80.0
		crow1.Animation="Crw_jmp"
		crow1.OnAnimationEndFunc=AnmEndF1
	if (time>(timer1+0.4)):
		corpse1.RemoveFromList("TimerCuervos")
		cuervo2_sound.Play(-3180,6800,-125800,0)
		crow2.ClearPath();
		crow2.FPS=80.0
		crow2.Animation="Crw_jmp"
		crow2.OnAnimationEndFunc=AnmEndF2


def PathNodeC1E(name,node):
	if (node==2):
		crow1.ClearPath();
		crow1.Animation="Crw_fly"
		crow1.FPS=20.0
		crow1.AddPathNode(15.0,75000,-26000,-90000);
		crow1.AddPathNode(15.0,0,-26000,-20000);
		crow1.AddPathNode(15.0,-50000,-26000,-100000);
		crow1.SetNodeSpeed(0,4000.0)
		crow1.SetNodeSpeed(1,4000.0)
		crow1.SetNodeSpeed(2,4000.0)
		crow1.GoToPath(0,2);

def PathNodeC2E(name,node):
	if (node==5):
		cuervo2_sound.Play(crow2.Position[0],crow2.Position[1],crow2.Position[2],0)	

def EspantarCuervo1():
	crow1.OnPathNodeFunc=PathNodeC1E
	crow1.ClearPath();
	crow1.Animation="Crw_fly"
	crow1.FPS=20.0
	crow1.AddPathNode(3.0,8000,-8000,-120000);
	crow1.AddPathNode(3.0,21000,-14000,-124000);
	crow1.AddPathNode(3.0,43000,-20000,-106000);
	crow1.SetNodeSpeed(0,4000.0)
	crow1.SetNodeSpeed(1,4000.0)
	crow1.SetNodeSpeed(2,4000.0)
	crow1.GoToPath(0,1.5);

def EspantarCuervo2():
	crow2.OnPathNodeFunc=PathNodeC2E
	crow2.ClearPath();
	crow2.Animation="Crw_fly"
	crow2.FPS=20.0
	crow2.AddPathNode(6.0,4800,-4000,-134000);
	crow2.AddPathNode(6.0,21000,-7000,-114000);
	crow2.AddPathNode(6.0,3000,-9000,-88000);
	crow2.AddPathNode(7.5,-35000,-4000,-66000);
	crow2.AddPathNode(7.5,16000,-7000,-68000);
	crow2.AddPathNode(6.0,10000,2000,-95000);
	crow2.SetNodeSpeed(0,4000.0)
	crow2.SetNodeSpeed(1,4000.0)
	crow2.SetNodeSpeed(2,4000.0)
	crow2.SetNodeSpeed(3,4000.0)
	crow2.SetNodeSpeed(4,4000.0)
	crow2.SetNodeSpeed(5,4000.0)
	crow2.GoToPath(2,1.5);
###############################################################################
###                     Crows11.py
###############################################################################

def EspantarCuervo11():
	crow11.ClearPath();
	crow11.Animation="Crw_fly"
	crow11.FPS=20.0
	crow11.AddPathNode(6.0,66000,-28000,-61000);
	crow11.AddPathNode(6.0,82000,-28000,-90000);
	crow11.AddPathNode(6.0,73000,-28000,-109000);
	crow11.AddPathNode(7.5,53000,-28000,-112000);
	crow11.AddPathNode(7.5,28000,-26000,-98000);
	crow11.AddPathNode(6.0,0,-24000,-86000);
	crow11.AddPathNode(6.0,-31000,-22000,-73000);
	crow11.AddPathNode(6.0,-56000,-20000,-58000);
	crow11.AddPathNode(6.0,-62000,-22000,-25000);
	crow11.AddPathNode(6.0,-58000,-24000,10000);
	crow11.AddPathNode(6.0,-46000,-26000,35000);
	crow11.AddPathNode(6.0,-24000,-26000,37000);
	crow11.AddPathNode(6.0,-12000,-25000,25000);
	crow11.AddPathNode(6.0,-5000,-25000,-4000);
	crow11.GoToPath(0,2);
	
def EspantarCuervo12():
	crow12.ClearPath();
	crow12.Animation="Crw_fly"
	crow12.FPS=20.0
	crow12.AddPathNode(6.0,57000,3000,-10000);
	crow12.AddPathNode(6.0,45000,10000,-27000);
	crow12.AddPathNode(6.0,30000,12000,-57000);
	crow12.AddPathNode(6.5,23500,15000,-81000);
	crow12.AddPathNode(6.5,22000,15000,-93000);
	crow12.AddPathNode(6.5,9500,12000,-99000);
	crow12.AddPathNode(5.0,-8000,12000,-85000);
	crow12.AddPathNode(6.0,-4000,10000,-74000);
	crow12.AddPathNode(4.0,12000,10000,-59000);
	crow12.AddPathNode(6.0,25000,10000,-41000);
	crow12.AddPathNode(6.0,44000,8000,19000);
	crow12.AddPathNode(6.0,61000,8000,6000);
	crow12.AddPathNode(6.0,54000,6000,31000);
	crow12.AddPathNode(4.0,66000,4,40000);
	crow12.AddPathNode(6.0,83000,2,29000);

	crow12.GoToPath(0,2);

###############################################################################
###                     DespredimientoSuelo.py
###############################################################################
def InitFloor():
	i = 0
	for i in range(n_fragments):
		fragment_state[i] = 1
		fragment[i].Active = 0

def PisandoSuelo(Entity,Timer):
	global fragment_state
	global number
	global last_pilar
	if (char.OnFloor):
		i = 0

		for i in range(n_pilares):			
			dist_x = char.Position[0] - pilar[i][0]
			dist_z = char.Position[2] - pilar[i][2]

			dist = dist_x * dist_x + dist_z * dist_z

			if (dist < 3000000):
				return
		i = 0

		for i in range(n_fragments):			
			if (fragment_state[i]):
				dist_x = char.Position[0] - fragment_position[i][0]
				dist_z = char.Position[2] - fragment_position[i][2]

				#dist = dist_x * dist_x + dist_z * dist_z

				if (dist_x < 0):
					dist_x = dist_x * -1

				if (dist_z < 0):
					dist_z = dist_z * -1

				if (dist_x < fragment_radio[i][0]):
					if (dist_z < fragment_radio[i][1]):
						ThrowDesprendimiento(i,(char.Position[0],3800,char.Position[2]))
			
	
def ActivateDesprendimientoSuelo(SectorIndex,Entity):
	global number
	if (Entity == "Player1"):
		char = Bladex.GetEntity("Player1")
		number = 0
		char.SubscribeToList("Timer10")
		char.TimerFunc = PisandoSuelo

def DeactivateDesprendimientoSuelo(SectorIndex,Entity):
	if (Entity == "Player1"):
		char.RemoveFromList("Timer10")

def AddPilar(pos):
	global n_pilares

	pilar[n_pilares:n_pilares] = [pos]
	n_pilares = n_pilares + 1

def ThrowDesprendimiento(index,pos):
	global fragment_state
	frag = fragment[index]
	fragment_state[index] = 0
	frag.DoBreak((0.0, 1.0, 0), pos, (0.0, 0.0, 0.0))

	PPS = 0.00008 * fragment_radio[index][0] * fragment_radio[index][1]

	polvareda=Bladex.CreateEntity("PolvoDesprendimiento", "Entity Particle System D3", fragment_position[index][0] + fragment_radio[index][0],fragment_position[index][1], fragment_position[index][2] + fragment_radio[index][1])
	polvareda.D1= fragment_radio[index][0] * -2, 0.0, 0.0
	polvareda.D2= fragment_radio[index][0] * -2, 0.0, 0 - fragment_radio[index][1]
	polvareda.ParticleType="LargeDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=PPS
	polvareda.DeathTime=Bladex.GetTime()+2.0/60.0
	polvareda.Velocity=0.0, -1000.0, 0.0
	polvareda.RandomVelocity=80.0

	polvareda=Bladex.CreateEntity("PolvoDesprendimiento2", "Entity Particle System D3", fragment_position[index][0] + fragment_radio[index][0],fragment_position[index][1], fragment_position[index][2])	
	polvareda.D1= fragment_radio[index][0] * -2, 0.0, 0 - fragment_radio[index][1]
	polvareda.D2= 0.0, 0.0, fragment_radio[index][1]
	polvareda.ParticleType="LargeDust"
	polvareda.YGravity=0.0
	polvareda.Friction=0.2
	polvareda.PPS=PPS
	polvareda.DeathTime=Bladex.GetTime()+2.0/60.0
	polvareda.Velocity=0.0, -1000.0, 0.0
	polvareda.RandomVelocity=80.0
	desprendimiento.Position = pos[0],pos[1],pos[2]
	desprendimiento.PlaySound(0)	


def AddDesprendimiento(pos,radio_x,radio_z):
	global n_fragments
	global fragment_state
	frag = Bladex.GetSector(pos[0],pos[1],pos[2])
	frag.Active = 0
	frag.InitBreak((0.0, 500.0, 0.0), (2000.0, 0.0, 0.0), (0.0, 0.0, 2000.0))
	fragment[n_fragments:n_fragments] = [frag]
	fragment_position[n_fragments:n_fragments] = [pos]
	fragment_radio[n_fragments:n_fragments] = [(radio_x,radio_z)]
	fragment_state[n_fragments:n_fragments] = [1]
	n_fragments = n_fragments + 1




###############################################################################
###                     GenEnemy.py
###############################################################################
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
#def SaltaTierraGen():
	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position		
	#pos=generadorT1.Points[0].Position
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

def ActivateEnemyGenerator(TrSector,Entity):
	if Entity == "Player1":
		generadorT1.GenerateEnemy()
		RodEnemyGen1.OnEnter = ""
		RodEnemyGen2.OnEnter = ""

def CreaSkeletoDichoso(o):
	o.Level = 0
	o.ActionAreaMin=pow(2,14)
	o.ActionAreaMax=pow(2,15)


def ActivateSkeletonGenerator():
	RodEnemyGen1.OnEnter = ActivateEnemyGenerator
	RodEnemyGen2.OnEnter = ActivateEnemyGenerator


# generator################################

def ActivateTempleEnemyGenerator(TrSector,Entity):
	if Entity == "Player1":
		CierrapuertadobleTemplo()
		puerta1.CloseDoor()
		puerta3.CloseDoor()
		TempleEnemyGenerator.GenerateEnemy()
		InsideTempleZone.OnEnter = ""



###############################################################################
###                     LLaveMagica.py
###############################################################################
def AbrePuertaLlaveA1():
	puertalA1.OpenDoor()
	puertalA2.OpenDoor()
	darfuncs.LuzChapuzera(Bladex.GetEntity("torchkey"), Bladex.GetTime() + 7.0) # mueve "torchkey" durante 7 segundos

def Musicaytextollave():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("llave") )	
	GameText.WriteText("M13T7")

def MueveTimer(e_name, time):
### Function's keyframe amount increased for smooth 60fps anim. 
### Commented values are the original.                -LeadHead
  global Contador
  Contador = Contador+1

  # darfuncs.GiraCamara(0.02)
  darfuncs.GiraCamara(0.02/3)

  lg = Bladex.GetEntity("BEETLE")
  luzta = Bladex.GetEntity("LuzBEETLE")
  
  # if (Contador>=20) and (Contador<=66):
  if (Contador>=60) and (Contador<=198):
    # lg.Move(0,1700/(20-66),0)
    # lg.Rotate(0, 0, 1,0.06532)
    lg.Move(0,1700/(60-198),0)
    lg.Rotate(0, 0, 1,0.06532/3)
    
  # elif (Contador>=160) and (Contador<=185):
    # iTick = (1.0-(Contador-160.0)/(185.0-160.0))
  elif (Contador>=480) and (Contador<=555):
    iTick = (1.0-(Contador-480.0)/(555.0-480.0))
    lg.Alpha                 =  iTick
    luzta.Intensity          =  10.0*iTick
    luzta.SizeFactor         =   2.0*iTick
    
  # elif (Contador==186):
  elif (Contador==558):
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
  # elif (Contador==230):
  elif (Contador==690):
    StarFlare=Bladex.CreateEntity("aTablillaBrillos", "Entity Particle System D1", char.Position[0], char.Position[1], char.Position[2])
    StarFlare.ParticleType   = "Estrellitas"
    StarFlare.YGravity       = 1000
    StarFlare.Friction       = 0.3
    StarFlare.PPS            = 112
    StarFlare.Velocity       = 0, 0.0, 0.0
    StarFlare.Time2Live      = 64
    StarFlare.DeathTime      = Bladex.GetTime()+2.0
    StarFlare.RandomVelocity = 50   
  # elif (Contador>=254):    
  elif (Contador>=762):    
    # lg.RemoveFromList("LlaveTimer") 
    lg.RemoveFromList("Timer60")      
    lg.TimerFunc = ""    
    luzta.SubscribeToList("Pin")
    Actions.TakeObject("Player1",lg.Name)
    
    cam = Bladex.GetEntity("Camera")
    cam.SetPersonView("Player1")
    AbrePuertaLlaveA1()
    
def IniciaCoger():
  global Contador

  darfuncs.InitGiroCamera()
  
  char.Wuea = Reference.WUEA_ENDED
  char.SetTmpAnmFlags(1,1,1,0,5,1)
  char.LaunchAnmType("tke_key")
  Bladex.AddScheduledFunc(Bladex.GetTime()+(256.0/20.0),Bladex.ActivateInput,())
  Bladex.AddScheduledFunc(Bladex.GetTime()+(256.0/20.0),Scorer.SetVisible,(1,))
  Contador = 0
  lg = Bladex.GetEntity("BEETLE")
  lg.TimerFunc     = MueveTimer
  # lg.SubscribeToList("LlaveTimer")    # Now 60fps, see "def MuevueTimer"
  lg.SubscribeToList("Timer60")         #       -LeadHead
  Musicaytextollave()


def PickUpLaLlave():
  llave = Bladex.GetEntity("BEETLE")
  llave.Position = -24595.105589,16968.456436,34935.464395
  Bladex.DeactivateInput()
  Scorer.SetVisible(0)
  Actions.FreeBothHands("Player1")
  cam = Bladex.GetEntity("Camera")
  #cam.PViewType = 0
  Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,IniciaCoger,())



###############################################################################
###                     MuralScene.py
###############################################################################
def MusicaytextoMural():
	GameText.WriteText("M13T2")

def ApagaLuz():	
	fluz = def_class.FLuz()
	fluz.Fire = AuxFuncs.GetFire(antini)
	fluz.Luz = AuxFuncs.GetSpot(antini)	
	fluz.Luz.Visible = 0
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 25,fluz.Apaga,())


def CleanLeg():
	polvo=Bladex.CreateEntity("Polvo", "Entity Particle System D1", -41953,6500,-118800)
	#polvo.D = -1000,0,0
	polvo.ParticleType="Dust"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=50
	polvo.Velocity=-10.0, 0.0, -10.0
	polvo.RandomVelocity=25.0
	#polvo.Time2Live=15	
	polvo.DeathTime=Bladex.GetTime()+3.0/60.0

def HitPlayer():
	soundhitplayer.Position = -41835,7000,-118500
	soundhit2player.Position = -41835,7000,-118500
	soundhitplayer.PlaySound(0)
	soundhit2player.PlaySound(0)

	polvo=Bladex.CreateEntity("Polvo", "Entity Particle System D2", -41835,7000,-118500)
	polvo.D = -1000,0,0
	polvo.ParticleType="MediumDust"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.Velocity=0.0, -200.0, 0.0
	polvo.RandomVelocity=45.0
	#polvo.Time2Live=15	
	polvo.DeathTime=Bladex.GetTime()+3.0/60.0


def GetTorch():
	char = Bladex.GetEntity("Player1")
	#char.InvRight == "":
	inv = char.GetInventory()
	inv.LinkRightHand("AntorchaInicio")
	soundhit2player.Position = -41560.0605302, 7031.3666973, -118575.876983
	soundhit2player.PlaySound(0)


def StopMuralScene(camera):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	char = Bladex.GetEntity("Player1")
	char.Position = -38500,char.Position[1],char.Position[2]
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()	
	char.SetOnFloor()

def SoundStart():
	soundesfuerzoplayer.Position = -41198,-142,-118553
	soundesfuerzoplayer.PlaySound(0)

def LookMuralScene():
	global initial_time
	global alpha	
	ApagaLuz()
	#Torchs.ExtingueAntorcha("AntorchaInicio")

	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()	
	
	if char.InvRight <> "":
		inv.LinkBack(char.InvRight)
	if char.InvLeft <> "":
		inv.LinkBack(char.InvLeft)

	char.Angle = 4.6483		
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	#char.LaunchAnimation("Kgt_start_desierto")		
	char.LaunchAnmType("start_desierto")

	if   char.Kind[0]=="K":
		char.Position = -41166, -37,-118402
	elif char.Kind[0]=="B":
		char.Position = -41110, 51,-118404
	elif char.Kind[0]=="A":
		char.Position = -41200, -124,-118553
	elif char.Kind[0]=="D":
		char.Position = -41314, -83,-118362

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("startCamera01.cam",0,705)
	#cam.AddCameraEvent(-1,StopMuralScene)
	char.AnmEndedFunc = StopMuralScene

	time = Bladex.GetTime()

	Bladex.AddScheduledFunc(time + 70.0/20.0,HitPlayer,())
	Bladex.AddScheduledFunc(time + 124.0/20.0,CleanLeg,())
	Bladex.AddScheduledFunc(time + 157.0/20.0,GetTorch,())
	Bladex.AddScheduledFunc(time + 158.0/20.0,MusicaytextoMural,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("mural") )	


	soundhittorch.Position = -41560.0605302, 7031.3666973, -118575.876983
	soundhittorch.PlaySound(0)	

	Bladex.AddScheduledFunc(time ,SoundStart,())
	
	
def ParchePrecarga():
	ScriptSkip.SkipScriptStart("EscenaINICIODESIERTO")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	AuxFuncs.FadeFrom(1.5,7.0)

	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,LookMuralScene,())

	
###############################################################################
###                     Positions.py
###############################################################################
def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=-38462.6377026, 5931.15915197, -107179.468953	# inicio
	#char.Position= -77000,2000,139000		# TABLILLA

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=7750, -2000, -13000			# bath

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-25500,-6000,116000		# sala hipostila

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=41500,0,19000			# Antes de la cripta

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-25000, -6000, 42000		# dentro del templo

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	#char.Position=7750, -2000, -13000			# bath
	char.Position=-27582.42, 9391.03, -19921.58		# en la crypta

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=-1500, -8000, 42500		# water

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-66000, -8000, 42000		# fire
	
def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=-104200.80, 7885.30, -4902.40	#final



###############################################################################
###                     Puertas.py
###############################################################################





def Abrereja1():
	desplazamientos=(1500.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrareja1():
	desplazamientos=(1500.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto reja1din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def AbrePuertaLlave1():
	puertal1.OpenDoor()

def CierraPuertaLlave1():
	puertal1.CloseDoor()

def StopPtaspalCamera(frame = 0,camera = 0):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	Bladex.ActivateInput()

def AbrePtaspal():
	puertar1.OpenDoor()
	puertar2.OpenDoor()
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,Investigan,())
	darfuncs.HideBadGuy("DesertArq2b")
	darfuncs.HideBadGuy("DesertArq3")
	#cam = Bladex.GetEntity("Camera")
	#cam.SetMaxCamera("Piedra_verdeCamera01.cam",0,-1)
	#cam.AddCameraEvent(-1,StopPtaspalCamera)
	#Scorer.SetVisible(0)
	#Bladex.DeactivateInput()
	
	
	
def CierraPtaspal():
	puertar1.CloseDoor()
	puertar2.CloseDoor()


def AbrePuertaLlave4():
	puertal4.OpenDoor()
	cerradurp4.key=""

def CierraPuertaLlave4():
	puertal4.CloseDoor()
	
def AbrePuertadoble():
	puertadoble1.OpenDoor()
	puertadoble2.OpenDoor()

def CierraPuertadoble():
	puertadoble1.CloseDoor()
	puertadoble2.CloseDoor()

def AbrePuertar6():
	puertar6.OpenDoor()


def CierraPuertar6():
	puertar6.CloseDoor()


def AbrePuertar7():
	puertar7.OpenDoor()
def CierraPuertar7():
	puertar7.CloseDoor()

def Abrereja3():
	desplazamientos=(1800.0, 1800.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def Cierrareja3():
	desplazamientos=(1800.0, 1800.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto reja3din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(reja3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbrePuertadobleF():
	puertadobleF1.OpenDoor()
	puertadobleF2.OpenDoor()

def CierraPuertadobleF():
	puertadobleF1.CloseDoor()
	puertadobleF2.CloseDoor()


def AbrePuertatablilla():
	puertatablilla.OpenDoor()
	
def CierraPuertatablilla():
	puertatablilla.CloseDoor()
	

def AbrePuertatablilla2():
	puertatablilla2.OpenDoor()
	
def CierraPuertatablilla2():
	puertatablilla2.CloseDoor()


def AbrePuertatablilla3():
	puertatablilla3.OpenDoor()


def CierraPuertatablilla3():
	puertatablilla3.CloseDoor()


def AbrePuerta11():
	puertal11.OpenDoor()

def CierraPuerta11():
	puertal11.CloseDoor()

def AbrePuerta12():
	puertal12.OpenDoor()

def CierraPuerta12():
	puertal12.CloseDoor()


def AbrePuerta13():
	puertal13.Active = 1

def CierraPuerta13():
	puertal13.Active = 0
	

def Abrecompuertas():
	compuerta1.OpenDoor()
	compuerta2.OpenDoor()

def Cierracompuertas():
	compuerta1.CloseDoor()
	compuerta2.CloseDoor()
	

def AbreBarrotes():
	BARROTE1.OpenDoor()
	BARROTE2.OpenDoor()
	BARROTE3.OpenDoor()
	BARROTE4.OpenDoor()

def CierraBarrotes():
	BARROTE1.CloseDoor()
	BARROTE2.CloseDoor()
	BARROTE3.CloseDoor()
	BARROTE4.CloseDoor()


def AbrePTAMURALLA():
	PTAMURALLA.OpenDoor()


def CierraPTAMURALLA():
	PTAMURALLA.CloseDoor()


def Abrereja4():
	desplazamientos=(1600.0, 1600.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja4din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo4, sonidorastrillo4)
	son_finales=("", golperastrillo4)
	Objects.NDisplaceObject(reja4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja4():
	desplazamientos=(1600.0, 1600.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto reja4din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo4, sonidorastrillo4, sonidorastrillo4, sonidorastrillo4, sonidorastrillo4, sonidorastrillo4)
	son_finales=("", golperastrillo4,"",golperastrillo4,"",golperastrillo4)
	Objects.NDisplaceObject(reja4din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrereja5():
	desplazamientos=(1600.0, 1600.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto reja5din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo5, sonidorastrillo5)
	son_finales=("", golperastrillo5)
	Objects.NDisplaceObject(reja5din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Cierrareja5():
	desplazamientos=(1600.0, 1600.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto reja5din
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo5, sonidorastrillo5, sonidorastrillo5, sonidorastrillo5, sonidorastrillo5, sonidorastrillo5)
	son_finales=("", golperastrillo5,"",golperastrillo5,"",golperastrillo5)
	Objects.NDisplaceObject(reja5din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



###############################################################################
###                     skeleto.py
###############################################################################


def MuereChicoMalo(ent_name):
	Bladex.GetEntity("CaballeroLlave").Data.StdImDead("CaballeroLlave")
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, PhantonFX.DisappearsChar,("CaballeroLlave",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, ScriptCompleted,())

def ApareceElTipoDeLaLlave():
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, ApareceElTipoDeLaLlave2,())
	
def ApareceElTipoDeLaLlave2():
	darfuncs.UnhideBadGuy("CaballeroLlave")
	PhantonFX.AppearsChar("CaballeroLlave")
	Bladex.GetEntity("CaballeroLlave").ImDeadFunc=MuereChicoMalo



###############################################################################
###                     gema.py
###############################################################################

def leaveGem(ent,event) :
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	handItem = char.InvRight

	inv.LinkRightHand("None")	
	inv.RemoveObject(handItem)
	gem = Bladex.GetEntity("gemaX")
	gem.Position = Bladex.GetEntity("GemBGPointer").Position
	gem.Orientation = 0.491198,0.491198,0.508650,0.508650
	gem.Static      = 1
	
	###### Process Here ########
	AbrePuerta11()

def useInGemGhostP(gpointer,usefrom):
	global RGemOk
	global GGemOk
	global BGemOk
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	obj = inv.GetSelectedObject()
	
	if obj=="gemaX":
		Actions.TurnToFaceEntityNow("Player1",gpointer)
		inv.LinkRightHand("gemaX")
		char.LaunchAnmType("Fire2")
		char.AddAnmEventFunc("SetAlightEvent",leaveGem)


def ApareceElEskeletoDeLaOstia():
	Bladex.AddScheduledFunc(Bladex.GetTime()+10, ApareceElEskeletoDeLaOstia2,())

def ApareceElEskeletoDeLaOstia2():
	darfuncs.UnhideBadGuy("EskeletoOstia")
	PhantonFX.AppearsChar("EskeletoOstia")	
	
	
###############################################################################
###                     cripta.py
###############################################################################
def Descubre():
	
	escalon1a.OpenDoor()
	escalon2a.OpenDoor()
	escalon3a.OpenDoor()
	escalon4a.OpenDoor()
	escalon5a.OpenDoor()
	escalon6a.OpenDoor()
	escalon7a.OpenDoor()
	escalon8a.OpenDoor()
	escalon9a.OpenDoor()
	escalon10a.OpenDoor()
	escalon11a.OpenDoor()
	escalon12a.OpenDoor()
	escalon13a.OpenDoor()
	escalon14a.OpenDoor()
	
	escalon1b.OpenDoor()
	escalon2b.OpenDoor()
	escalon3b.OpenDoor()
	escalon4b.OpenDoor()
	escalon5b.OpenDoor()
	escalon6b.OpenDoor()
	escalon7b.OpenDoor()
	escalon8b.OpenDoor()
	escalon9b.OpenDoor()
	escalon10b.OpenDoor()
	escalon11b.OpenDoor()
	escalon12b.OpenDoor()
	escalon13b.OpenDoor()
	escalon14b.OpenDoor()
	

def Tapa():

	escalon1a.CloseDoor()
	escalon2a.CloseDoor()
	escalon3a.CloseDoor()
	escalon4a.CloseDoor()
	escalon5a.CloseDoor()
	escalon6a.CloseDoor()
	escalon7a.CloseDoor()
	escalon8a.CloseDoor()
	escalon9a.CloseDoor()
	escalon10a.CloseDoor()
	escalon11a.CloseDoor()
	escalon12a.CloseDoor()
	escalon13a.CloseDoor()
	escalon14a.CloseDoor()

def Abrelados():
	global ladosCerrados	
	ptatrampa.OpenDoor()
	cam.EarthQuake = 0
	ladosCerrados = 0
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0, lado1.OpenDoor,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0, lado2.OpenDoor,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

def CierraladosCR():
	global ladosCerrados
	if (ladosCerrados==0) :
		ptatrampa.CloseDoor()
		Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0, lado1.CloseDoor, ()) #Wall slidding
		Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0, lado2.CloseDoor, ()) #Wall slidding
		ladosCerrados=1
		cam.EarthQuakeFactor = 20
		cam.EarthQuake = 1
		darfuncs.LuzChapuzera(Bladex.GetEntity("LUZCHAPUTRAN"), Bladex.GetTime() + 60.0) 
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("comb2") )
		

def ClosedTrap():
	global TrapClack
	cam.EarthQuake = 0
	TrapClack.StopSound()

def EntroEnTriggerSector(trsector_name, entity_name):
	global TrapClack
	global bTrapUsed
	print("entidad:"+entity_name+", en sector"+trsector_name);
	if (entity_name == "Player1") :
		Bladex.SetTriggerSectorFunc("sectortr1", "OnEnter", "")
		# Activate trap
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0, CierraladosCR, ()) #Wall slidding
		# Finish trap effects
		Bladex.AddScheduledFunc(Bladex.GetTime() + 16.0, ClosedTrap, ())
		bTrapUsed = 1
		# Play Trap Sound
		TrapClack.Position = char.Position
		TrapClack.PlaySound(0)





###############################################################################
###                     TrikyTorch.py
###############################################################################

def QuadRado(x):
	return x*x

def CheckTrikyTorch():
	global TRIKY_TIME_CHECK
	global TRIKY_SQR_DIST
	Ontake.DelOnTakeEvent("TrikyTorch")
	
	Bladex.RemoveScheduledFunc("CheckTrikyTorch")
	Bladex.AddScheduledFunc(Bladex.GetTime()+TRIKY_TIME_CHECK,CheckTrikyTorch,(),"CheckTrikyTorch")
	o = Bladex.GetEntity("TrikyTorch")
	print "checking tricky torch..."
	if not o.Parent:
		print "tricky torch is free"
		char = Bladex.GetEntity("Player1")
		d    = (QuadRado(char.Position[0]-o.Position[0])+
			QuadRado(char.Position[0]-o.Position[0])+
			QuadRado(char.Position[0]-o.Position[0]))
		
		if TRIKY_SQR_DIST < d:
			o.SubscribeToList("Pin")
			Bladex.AddScheduledFunc(Bladex.GetTime()+TRIKY_TIME_CHECK,CreateTrikyTorch,())
			Bladex.RemoveScheduledFunc("CheckTrikyTorch")
			print "tricky torch is out"



def CreateTrikyTorch():
	o                = Bladex.CreateEntity("TrikyTorch","Antorcha",-63878.3203724, -4369.51101303, 79487.7317179,"Physic")
	o.Scale          = 1.000000
	o.Orientation    = (0.63704097271, -0.679524719715, -0.126430600882, -0.341216504574)
	o.Position       = (-65275.4012192, -3753.99655403, 71332.2750366)
	o.FiresIntensity = [ 45 ]
	o.Lights         = [ (0.000000,0.090000,(255,159,53)) ]
	Torchs.SetUsable("TrikyTorch",3,7,50)
	Ontake.AddOnTakeEvent("TrikyTorch", CheckTrikyTorch)
	print "you've got it"
	
	return o

###############################################################################
###                     Tablilla.py
###############################################################################

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
    #char.GoTo(TablStartPosition[0],TablStartPosition[1],TablStartPosition[2])
    #char.RouteEndedFunc = EscenaTablilla
    EscenaTablilla("Player1")
    TabillaSector.OnEnter = ""
  

def EscenaTablilla(Entity):
  ScriptSkip.SkipScriptStart("EscenaDesertTablillas")
  #Bladex.DeactivateInput()
  Scorer.SetVisible(0)
  Actions.FreeBothHands(Entity,IniciaEscenaTablilla,())


def Musicaytexto():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("tablilla") )
	GameText.WriteText("M13T3")

def IniciaEscenaTablilla():
  cam  = Bladex.GetEntity("Camera")
  char = Bladex.GetEntity("Player1")
  
  char.Position = TablStartPosition[0],TablStartPosition[1],TablStartPosition[2]
  char.Angle = AnglStartPosition
  char.SetTmpAnmFlags(1,1,1,0,5,1,0)
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

  ###################################################
  # Tablilla para Knight_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'K':
  	o             = Bladex.GetEntity('Tablilla6')
  	o.Position    =  (-62707.8010486, 1404.16970359, 124078.268343)
  	o.Orientation =  (0.641422569752, 0.378317922354, 0.601839780807, -0.288516014814)

  ###################################################
  # Tablilla para Amazon_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'A':
  	o             = Bladex.GetEntity('Tablilla6')
  	o.Position    =  (-62635.1326281, 1426.25735819, 124075.191873)
  	o.Orientation =  (0.596074998379, 0.375632166862, 0.614985585213, -0.354101628065)

  ###################################################
  # Tablilla para Barbarian_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'B':
  	o             = Bladex.GetEntity('Tablilla6')
  	o.Position    =  (-62568.8313537, 1246.62140585, 124082.589473)
  	o.Orientation =  (0.638403058052, 0.338941633701, 0.588434934616, -0.362359374762)
  
  ###################################################
  # Tablilla para Dwarf_N
  ###################################################
  if Bladex.GetEntity('Player1').Kind[0] == 'D':
  	o             = Bladex.GetEntity('Tablilla6')
  	o.Position    =  (-62497.0200065, 1733.41234049, 124021.910261)
  	o.Orientation =  (0.623763203621, 0.372531980276, 0.588422000408, -0.354822009802)
	  
  
  
def CreateEstrellitas():
        StarFlare=Bladex.CreateEntity("aTablillaBrillos", "Entity Particle System D1", tab.Position[0], tab.Position[1], tab.Position[2])
        StarFlare.ParticleType="Chispas"
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
  inv.RemoveObject("Tablilla6")
  
  char.RemoveFromInventLeft()  
  CreateEstrellitas()  
  PosX  = tab.Position[0]
  PosY  = tab.Position[1]
  PosZ  = tab.Position[2]
  Tick  = 0
  Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CoolStart, ())
  tab.Position = PosX,  PosY, PosZ
  AbrePuertatablilla2()
  
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
# Todavia me da cosa decir coger pero bueno
#------------------------------------------------------
def CogeLaTablilla(Camera,frame):
  char = Bladex.GetEntity("Player1")  
  inv  = char.GetInventory()
  inv.AddTablet("Tablilla6")
  inv.LinkLeftHand("Tablilla6")
  ImprimeDatosTablilla("Tablilla6")
  Musicaytexto()




###############################################################################
###                     bastonptatemplo.py
###############################################################################

def HideRayoBastonPower():
	print "HideRayoBastonPower()"
	bm = Bladex.GetEntity("BastonMagico")
	RayoBaston = Bladex.GetEntity("Rayo Baston")
	RayoBaston.Active          = 0
	RayoBaston.MaxAmplitude    = 20

def coolBastonFX(bm):
		spot = AuxFuncs.GetSpot(bm)
		RayoBaston = Bladex.GetEntity("Rayo Baston")		
		time = Bladex.GetTime()
		
		RayoBaston.Target          =( spot.Position[0]+(bm.Position[0]-spot.Position[0])*2
		                             ,spot.Position[1]+(bm.Position[1]-spot.Position[1])*2
		                             ,spot.Position[2]+(bm.Position[2]-spot.Position[2])*2
		                            )
		RayoBaston.Position        = spot.Position
		RayoBaston.Active          = 1
		RayoBaston.MaxAmplitude    = 20
		RayoBaston.Active          = 1		
		

		RayoHit                = Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D2", 0,0,0)
		RayoHit.Position       = RayoBaston.Position
		RayoHit.D1             =(RayoBaston.Target[0]-RayoBaston.Position[0]
		                        ,RayoBaston.Target[1]-RayoBaston.Position[1]
		                        ,RayoBaston.Target[2]-RayoBaston.Position[2])
		RayoHit.Time2Live      = 15
	 	RayoHit.ParticleType   = "LaserHit"
		RayoHit.YGravity       = 0.0
		RayoHit.Friction       = 0
		RayoHit.PPS            = 1024
		RayoHit.Velocity       = 0,0,0
		RayoHit.RandomVelocity = 3
		RayoHit.DeathTime      = time+1.5

		bm.Stop()
		bm.Position    = -63670.749000,19100.737000,-42132.709000
		bm.Orientation = 0.583292,-0.441550,0.276471,-0.623192
		bm.PutToWorld()

		Bladex.AddScheduledFunc(time +  1.0,HideRayoBastonPower,())

#
# cuando el baston regresa a su morada
#
def BastonChau():
	bm = Bladex.GetEntity("BastonMagico")
	print "BastonChau()"

	time = Bladex.GetTime()
	if not bm.Parent:
		coolBastonFX(bm)
		bm.RemoveFromWorld()
		Bladex.AddScheduledFunc(time +  2.0,coolBastonFX,(bm,))
	else:
		Bladex.RemoveScheduledFunc("BastonCheck")
		Bladex.AddScheduledFunc(time +  8.0,BastonCheck,(),"BastonCheck")
	

def BastonCheck():
	print "BastonCheck()"
	BASTON_RESTORE_LIFE          = 5
	BASTON_RESTORE_TIME          = 8
	BASTON_RESTORE_TIME_RELAX    = 3
	
	
	bm = Bladex.GetEntity("BastonMagico")
	time = Bladex.GetTime()
	if bm.Parent:
		Bladex.RemoveScheduledFunc("BastonCheck")
		char = Bladex.GetEntity("Player1")
		if char.AnimFullName == "Rlx":
			Bladex.AddScheduledFunc(time +  BASTON_RESTORE_TIME_RELAX,BastonCheck,(),"BastonCheck")
		else:
			Bladex.AddScheduledFunc(time +  BASTON_RESTORE_TIME,BastonCheck,(),"BastonCheck")

		if (char.Life>0):
			maxlife = CharStats.GetCharMaxLife(char.Kind, char.Level)
			if (maxlife > char.Life+BASTON_RESTORE_LIFE):
				char.Life = char.Life + BASTON_RESTORE_LIFE
				char.Data.UnVenom ()

				RayoHit=Bladex.CreateEntity("Player1Restore", "Entity Particle System Dperson", 0, 0, 0)
				RayoHit.PersonName="Player1"				
				RayoHit.Time2Live      = 20
			 	RayoHit.ParticleType   = "Llamita"
				RayoHit.YGravity       = 0.0
				RayoHit.Friction       = 0
				RayoHit.PPS            = 1024
				RayoHit.Velocity       = 0,0,0
				RayoHit.NormalVelocity = -5
				RayoHit.FollowFactor   = 1
				RayoHit.DeathTime      = time+0.5

				spot         = AuxFuncs.GetSpot(bm)
			else:
				char.Life = maxlife
	else:
		Bladex.AddScheduledFunc(time +  15.0,BastonChau,())
	
def AbrepuertadobleTemplo():
	puertadobleTemplo1.OpenDoor()
	puertadobleTemplo2.OpenDoor()

def CierrapuertadobleTemplo():
	puertadobleTemplo1.CloseDoor()
	puertadobleTemplo2.CloseDoor()

def HideRayoBaston():
	RayoHit=Bladex.GetEntity("RayoBastonHit")
	RayoConcent=Bladex.GetEntity("RayoBastonConcent")
	if RayoHit:
		RayoHit.DeathTime     = Bladex.GetTime()
	if RayoConcent:
		RayoConcent.DeathTime = Bladex.GetTime()
	RayoBaston.Active          = 0
	CierraPuertaLlave4()

def LanzaRayoBaston(p1):
	global RayoHit
	
	RayoBaston.Target          = p1
	RayoBaston.Position        = AuxFuncs.GetSpot(Bladex.GetEntity("BastonMagico")).Position
	RayoBaston.Active          = 1
	p2			   = RayoBaston.Position

	RayoHit=Bladex.GetEntity("RayoBastonHit")
	if not RayoHit:
		RayoHit=Bladex.CreateEntity("RayoBastonHit", "Entity Particle System D1", p1[0],p1[1],p1[2])
		RayoHit.Time2Live=15
	 	RayoHit.ParticleType="LaserHit"
		RayoHit.YGravity=0.0
		RayoHit.Friction=0
		RayoHit.PPS=112
		RayoHit.Velocity=0,0,0
		RayoHit.RandomVelocity=10
	else:
		RayoHit.Position = p1
	

	RayoConcent=Bladex.GetEntity("RayoBastonConcent")
	if not RayoConcent:
		RayoConcent=Bladex.CreateEntity("RayoBastonConcent", "Entity Particle System D1", p2[0],p2[1],p2[2])
		RayoConcent.Time2Live=32
	 	RayoConcent.ParticleType="LaserConcentrator"
		RayoConcent.YGravity=0.0
		RayoConcent.Friction=0
		RayoConcent.PPS=112
		RayoConcent.Velocity=0,0,0
		RayoConcent.RandomVelocity=-10
	else:
		RayoConcent.Position = p2
	

	return RayoBaston


def RayoTimer(e_name, time):
	global Rayo_Counter
	
	LanzaRayoBaston((-24500,Rayo_Counter,23000))
	Rayo_Counter = Rayo_Counter+50
	if Rayo_Counter > -1300:
		bm = Bladex.GetEntity("BastonMagico")
		bm.RemoveFromList("Timer30")
		HideRayoBaston()
		AbrepuertadobleTemplo()
		Bladex.AddScheduledFunc(Bladex.GetTime() +  2.5,Bladex.ActivateInput,())
	
      	
def Rayoto():
	global Rayo_Counter
	
	Rayo_Counter = -8000
	LanzaRayoBaston((-24500,Rayo_Counter,23000))
	RayoBaston.Active          = 0
	bm = Bladex.GetEntity("BastonMagico")
	Gems.SetGemColor(Gems.RED_GEM)
	Gems.GemParams   = (("Timer30",))
	Gems.GemCallBack = bm.SubscribeToList
	Gems.Concentrator(RayoBaston.Position,(0,0,0))	
		
	bm.TimerFunc=RayoTimer


def RestoreHand(ent):
	Change.RestoreHand(ent,1)

def PutBaston(ent,event):	
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	inv.RemoveObject(char.InvRight)		
	inv.LinkRightHand("None")

	baston = Bladex.GetEntity("BastonMagico")	
	baston.Position = -24438,-1510,16503
	baston.Orientation = 0.707107,0.707107,0.000000,0.000000
	baston.Static = 1
	baston.FiresIntensity=[ 45 ]
	baston.Lights=[ (0.200000,0.050000,(255,69,43)) ]	
		
	puerta1.OpenDoor()
	puerta3.OpenDoor()
	
	Rayoto()

	#luz=Bladex.CreateEntity("rlight","Entity Spot",-24438.547069,-3850.150844,16503.460813)
	#luz.Color = 236,35,0

def FinishChange(ent,object):
	char = Bladex.GetEntity(ent)
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("Fire2")
	char.AddAnmEventFunc("SetAlightEvent",PutBaston)
	#char.AnmEndedFunc = RestoreHand

def UsePunteroBaston(ent,use_from):
	#entpunt = Bladex.GetEntity(ent)
	#entpunt.SubscribeToList("Pin")
	char = Bladex.GetEntity("Player1")
	#inv = char.GetInventory()
	#obj = inv.GetSelectedObject()
	obj = char.InvRight
	
	if (obj == "BastonMagico"):
		Bladex.DeactivateInput()
		FinishChange("Player1",0)
	
		#Change.ChangeObject("Player1","BastonMagico",FinishChange)




###############################################################################
###                     GolemSleep.py
###############################################################################
def EmptyWater(Entity,timer):
	global AlturaWater

	water = Bladex.GetEntity(Entity)		
	AlturaWater = AlturaWater + DespWater
	water.Position = -25000,AlturaWater,54000 
	
	wawa = Bladex.GetEntity("agua_monolitoto")
	if not wawa:
		if AlturaWater>11400:
			wawa=Bladex.CreateEntity("agua_monolitoto","Entity Water",-26000,11400,62500)
			wawa.Reflection=-1
			wawa.Color=5,15,25
	else:
		wawa.Position = -26000,11400,62500

def MoveRejas(Entity,Timer):	
	reja1 = Bladex.GetEntity("RejaGolem1")
	reja2 = Bladex.GetEntity("RejaGolem2")

	reja1.Position = -23539,12351,reja1.Position[2] - DespReja
	reja2.Position = -26092,12351,reja2.Position[2] - DespReja


def GolemWakeUp(Sector,Entity):
	if Entity == "Player1":
		generadorCueva.GenerateEnemy()
		GolemSector1.OnEnter = ""
		GolemSector2.OnEnter = ""
		

def StopEmptyWater():
	water = Bladex.GetEntity("WaterGolem")
	water.RemoveFromList("Timer60")
	water.TimerFunc = ""
	water.Position = -25000,19000,54000 
	
def StopMoveRejas():
	reja = Bladex.GetEntity("RejaGolem1")
	reja.RemoveFromList("Timer60")
	reja.TimerFunc = ""

	reja = Bladex.GetEntity("RejaGolem2")
	reja.RemoveFromList("Timer60")
	reja.TimerFunc = ""

def StopCameraGolem(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)


def ActivateWater():
	cam = Bladex.GetEntity("Camera")
	
	darfuncs.LaunchMaxCamera("desert_aguabajaCamera01.cam",0,-1)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("coro6") )

	Bladex.SetListenerPosition(2)

	water = Bladex.GetEntity("WaterGolem")
	water.TimerFunc = EmptyWater
	water.SubscribeToList("Timer60")
	
	AbrePuerta13()
	"""
	reja1 = Bladex.GetEntity("RejaGolem1")
	reja1.SubscribeToList("Timer60")
	reja1.TimerFunc = MoveRejas
	"""
	#charco que queda arriba


def GolemMuerto():
	time = Bladex.GetTime()

	Bladex.AddScheduledFunc(time +  4.5,ActivateWater,())
	Bladex.AddScheduledFunc(time + 20.5,StopEmptyWater,())
	#Bladex.AddScheduledFunc(time + 19.5,StopMoveRejas,())	

def SaltaTierraGen(enmgen):
	char=Bladex.GetEntity("Player1")
	pos=enmgen.Position		
	v=char.Position[0]-pos[0], 0.0, char.Position[2]-pos[2]
	v=AuxFuncs.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)

	saltatie=Bladex.CreateEntity("TierraSaltando", "Entity Particle System D1", pos[0], pos[1]-900.0, pos[2])
	saltatie.ParticleType="Fire"
	saltatie.PPS=1024
	saltatie.YGravity=4900.0
	saltatie.Friction=0.05
	saltatie.Velocity=0.0, -600.0, 0.0
	saltatie.RandomVelocity=50.0
	saltatie.Time2Live=32
	saltatie.DeathTime=Bladex.GetTime()+0.5

	
	enmgen.CatchOnFire(0,0,0)
	luz             = Bladex.CreateEntity(enmgen.Name+"Luz","Entity Spot",0,0,0)
	luz.Color       = 200,100,0
	luz.Intensity   = 15
	luz.Precission  = 0.1
	luz.CastShadows = 0
	luz.Visible     = 1
	luz.SizeFactor  = 0
	enmgen.Link(luz)	
	
	
def CreaSkeletoLlamarada(o):
	import CharStats 
	o.Level = 10
	o.Life = CharStats.GetCharMaxLife(o.Kind, o.Level)	
	o.ActionAreaMin=pow(2,6)
	o.ActionAreaMax=pow(2,7)



###############################################################################
###                     Puertasdeltemplo.py
###############################################################################
def ObjetoSigueSliding(entity,time):	
	obj = Bladex.GetEntity(entity)
	sld = obj.Data.sld
	X = obj.Position[0]
	Z = obj.Position[2]
	D = sld.Displacement	
	Y = obj.Data.y - D
	
	obj.Position = X,Y,Z

def LinkSld(entity,sld_name,y):
	obj = Bladex.GetEntity(entity)
	sld = Bladex.GetEntity(sld_name)
	
	Bladex.CreateTimer("Timer60",1.0/60.0)	
	
	obj.Static = 0
	obj.Data = def_class.Link(sld,y)

	obj.TimerFunc = ObjetoSigueSliding
	obj.SubscribeToList("Timer60")

def UnLinkSld(entity):
	obj = Bladex.GetEntity(entity)
	obj.RemoveFromList("Timer60")


def RestoreCam():
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	UnLinkSld("PBaston")
	

def ScriptCompleted():
	punterobaston=Bladex.CreateEntity("PunteroBaston","GhostPointer", -24438,-1010,16503)
	punterobaston.Static=1
	punterobaston.Scale=0.100000
	punterobaston.Orientation=0.504344,0.504344,-0.495618,0.495618
	punterobaston.UseFunc = UsePunteroBaston
	darfuncs.SetHint(punterobaston,"Round Hole")
	puerta5.CloseDoor()
	puerta4.OpenDoor()

	LinkSld("PBaston","PlataformaBaston",1000)
	darfuncs.LaunchMaxCamera("camara_mira_inscripcion.cam",0,-1)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb4") )

def UseFireAltar(ObjectName,use_from):	
	global fire_altar_completed
	global SacredTorchActive
	
	if fire_altar_completed:
		return
	
	if Bladex.GetEntity("Player1").InvRight != SacredTorchActive:
		return
		


	e1 = Bladex.GetEntity(ObjectName)
	e2 = Bladex.GetEntity("PunteroFire")
	
	Actions.StdSetFireToUseFunc("PunteroFire",use_from)
	e2.UseFunc = UseFireAltar

	e2.Data = e1.Data
	
	char = Bladex.GetEntity("Player1")
	
	char.DelAnmEventFunc("SetAlightEvent")
	char.AddAnmEventFunc("SetAlightEvent",AlightAltar)

def AlightAltar(entity,event):
	global fire_altar_completed

	fire_altar_completed = 1

	#Bladex.CreateEntity("fire_altar","Entity Fire",-60000,-3400,41500)
	llamarada=Bladex.CreateEntity("Llamarada", "Entity Particle System D1", -60150,-3200,41750)
	llamarada.ParticleType="Flame"
	llamarada.YGravity=-4000.0
	llamarada.Friction=0.12
	llamarada.PPS=300
	llamarada.Velocity=0.0, -2000.0, 0.0
	llamarada.RandomVelocity=45.0
	llamarada.Time2Live=15	
	encenf.Play(-60000, -4500, 41600,  0)	
	saltarf.Play(-60000, -4500, 41600,-1)
	darfuncs.FireOnGS("fuegosagrado")

	if (water_altar_completed):
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,AbrePtaspal,())

def Keep(ent,event):
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	inv.LinkRightHand("None")
	
def RestoreHand(entity):
	if BottelHand:
		char = Bladex.GetEntity(entity)
		char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
		char.LaunchAnmType("Chg_r")
	#pass
	#Change.RestoreHand(entity,0)

def TakeBottel(char):
	#Change.RestoreHand(char,0)
	char = Bladex.GetEntity(char)	
	char.LaunchAnmType("bag")	
	char.AddAnmEventFunc("ChangeREvent",Keep)
	char.AnmEndedFunc = RestoreHand

def FChange2(entity,object):
	char = Bladex.GetEntity(entity)
	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("fire0")
	char.AnmEndedFunc = TakeBottel

	soundllenarbotella.Position = char.Position
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.4,soundllenarbotella.PlaySound,(0,))


def UseBotellaVerde(en,fr):
	global BottelHand
	global BottelOHand

	if (bottel_state == EMPTY):
		char = Bladex.GetEntity("Player1")
		inv = char.GetInventory()
		obj = inv.GetSelectedObject()

		if (obj == "BotellaTemplo"):
			#Actions.FreeBothHands("Player1",ContiueUseBottle,(en,))

			if char.InvRight <> '':
				if Actions.IsRightHandStandardObject("Player1"):
					if Actions.TryDropRight("Player1"):	
						Actions.DropReleaseEventHandler("Player1", "DropRightEvent")
					if not char.InvRight:
						ContiueUseBottle()
				else:
					char.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
					char.LaunchAnmType("Chg_r")
					BottelHand = 1
					BottelOHand = char.InvRight
					char.AnmEndedFunc=ContiueUseBottle
			else:
				ContiueUseBottle()

			
def ContiueUseBottle(en = "Player1"):
	global bottel_state

	Change.ChangeObject("Player1","BotellaTemplo",FChange2)
	Actions.QuickTurnToFaceEntity ("Player1",en)
	bottel_state = FULL	
	darfuncs.SetHint(Bladex.GetEntity("BotellaTemplo"),"Full Bottle")

def WaterPrtlHit(prtl_name,hit_entity,x,y,z,vx,vy,vz,wcx,wcy,wcz,wdx,wdy,wdz):
	global n_pool_water
	if (n_pool_water < 6):
		p = Bladex.CreateEntity("WaterPool","Entity Pool",x,y,z)
		p.Color = (160,255,255)
		p.DeepColor = (120,215,215)
		n_pool_water = n_pool_water + 1

		time = Bladex.GetTime()
		water=Bladex.CreateEntity("w2","Entity Particle System D1",x,y,z)
		water.ParticleType="Water"
		water.YGravity=9800.0
		water.DeathTime=time + 0.4
		water.Friction=0.075
		water.PPS=500
		
		water.RandomVelocity=20.0
		water.Velocity=0,-1000,0


def WaterFunc(water_name,end_time,period):
	water=Bladex.GetEntity(water_name)
	if(water):
		prtl=water.GetParticleEntity()
		prtl.HitFunc=WaterPrtlHit		

		if(Bladex.GetTime()<end_time):
			Bladex.AddScheduledFunc(Bladex.GetTime()+period,WaterFunc,(water_name,end_time,period))

def BackPlayer(entity):
	char = Bladex.GetEntity(entity)
	char.Position = char.Data.Position
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")

	Change.RestoreHand("Player1",2)

	if (fire_altar_completed):
		Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,AbrePtaspal,())

def ThrowWater(entity,event):
	time = Bladex.GetTime()
	water=Bladex.CreateEntity("w","Entity Particle System D1",0,0,260)
	water.ParticleType="Water"
	water.YGravity=9800.0
	water.Friction=0.075
	water.PPS=2500
	water.DeathTime=time + 1.0
	water.RandomVelocity=2.0
	water.Velocity=0,500,0
	Bladex.GetEntity("BotellaTemplo").Link(water)
	WaterFunc("w",time + 4.0,0.03)

def FChange(entity,object):
	global water_altar_completed
	global bottel_state

	char = Bladex.GetEntity(entity)
	char.Data.Position = char.Position
	
	x = char.Position[0] - 3300
	z = char.Position[2] - 42500

	dx = x / long
	dz = z / long

	dist = long - 1000

	x = char.Position[0] - dx * dist
	z = char.Position[2] - dz * dist

	char.Position = (x,char.Position[1],z)		

	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("pour")
	char.AddAnmEventFunc("StartPouring",ThrowWater)
	char.AnmEndedFunc = BackPlayer
	cam = Bladex.GetEntity("Camera")
	cam.SetTravellingView(0,0)

	cam.TPos = 3300,-3200,42500
	x =  3300 - dx * 1000
	z = 42500 - dz * 1000

	cam.Position = x,-8000,z
	water_altar_completed = 1
	bottel_state = USED
	o = Bladex.GetEntity("BotellaTemplo")
	darfuncs.SetHint(o,"Broken Bottle")
	o.OnStopFunc = BreakTheSacredWater


	soundvaciarbotella.Position = char.Position
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.5,soundvaciarbotella.PlaySound,(0,))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.15,soundvaciarbotella.StopSound,())

def BreakTheSacredWater(obj_name):
	RayoHit                = Bladex.CreateEntity(obj_name+" Sarcred", "Entity Particle System D1", 0,0,0)
	RayoHit.ParticleType   = "SacredFX"
	RayoHit.Time2Live      = 16
	RayoHit.YGravity       = 1000
	RayoHit.Friction       = 0
	RayoHit.PPS            = 2048
	RayoHit.Velocity       = 0,0,0
	RayoHit.RandomVelocity = 10
	RayoHit.DeathTime      = Bladex.GetTime()+0.25

	o = Bladex.GetEntity(obj_name)	
	RayoHit.Position = o.Position
	o.SubscribeToList("Pin")
	

def	UseWaterAltar(en,fr):
	global n_pool_water
	global long

	if (bottel_state == FULL):
		char = Bladex.GetEntity("Player1")
		inv = char.GetInventory()
		obj = inv.GetSelectedObject()

		if (obj == "BotellaTemplo"):
			x = char.Position[0] - 3300
			z = char.Position[2] - 42500
			long = math.sqrt(x*x+z*z)

			if (long < 2000):
				Change.ChangeObject("Player1","BotellaTemplo",FChange)
				Actions.QuickTurnToFaceEntity ("Player1",en)
				n_pool_water = 0
				Bladex.DeactivateInput()				
				Bladex.AddScheduledFunc(Bladex.GetTime()+9.0, Bladex.ActivateInput,())


def MusicayTextoFuego():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("GhostFuego") )	
  	GameText.WriteText("M13T5")

def MusicayTextoAgua():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("GhostAgua") )	
  	GameText.WriteText("M13T4")

def MusicayTextoPuerta():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("GhostPuerta") )	
  	GameText.WriteText("M13T6")

############### funcion que utiliza ghpointer ###################3
def useInGhostAgua(gpointer,usefrom):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,MusicayTextoAgua,())

def useInGhostFuego(gpointer,usefrom):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,MusicayTextoFuego,())

def useInGhostPuerta(gpointer,usefrom):
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,MusicayTextoPuerta,())
	


def SacredFireFX(name):
	global SacredTorchActive
	
	RayoHit=Bladex.CreateEntity(name+" Sarcred", "Entity Particle System D1", 0,0,400)
	RayoHit.ParticleType="SacredFX"
	RayoHit.Time2Live=16
	RayoHit.YGravity=0.0
	RayoHit.Friction=0
	RayoHit.PPS=255
	RayoHit.Velocity=0,0,0
	RayoHit.RandomVelocity= -10
	RayoHit.DeathTime     = Bladex.GetTime()+2.0
	o = Bladex.GetEntity(name)
	o.Link(RayoHit)
	
	if o.Parent == "Player1":		
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, SacredFireFX, (name,))
		SacredTorchActive = name
	else:
		Torchs.ExtingueAntorcha(name)
		SacredTorchActive = None

def UseSacredFireTorch(FromName,ToName):
	print FromName, ToName
	if "SacredTorch"==FromName:
		o = Bladex.GetEntity(ToName)
		o.Data.torchobjdata.Life = -1
		o.Data.torchobjdata.LightIntensity = 0.2500000
		SacredFireFX(ToName)


###############################################################################
###                     Enemigos.py
###############################################################################

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


def x0(sectorindex,entityname):

	if entityname=='Player1':
		pers=Bladex.GetEntity("2ORC")
		pers.GoTo(-22381.1754831, 4882.78370597, -101397.744411)
		pers=Bladex.GetEntity("2ORCb")
		pers.GoTo(-16991.4180077, 4893.18464488, -100799.158058)
		sectx0.OnEnter=""

def x1(sectorindex,entityname):

	if entityname=='Player1':
		fastGoTo("3ORC",-24357.6595354, 132.27221048, -59065.2342199)
		fastGoTo("DesertArq1",-27003.5314919, 150.268582033, -56500.8131247)
		sectx1.OnEnter=""


def TerminanLasMuertes0():
	sectx2=Bladex.GetSector(-23831.0415337, -179.733425979, -43389.4982158)
	sectx2.OnEnter=x2


def x2(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("4ORC")
		darfuncs.UnhideBadGuy("5ORC")
		fastGoTo("4ORC",-13943.5613792, -777.958429501, -35716.3664553)
		fastGoTo("5ORC",-28522.9701984, 122.184140542, -37117.1674884)
		sectx2=Bladex.GetSector(-23831.0415337, -179.733425979, -43389.4982158)
		sectx2.OnEnter=""

def TerminanLasMuertes00():
	sectx2b=Bladex.GetSector(-11496.6820098, -2633.10867105, -14777.2905832)
	sectx2b.OnEnter=x2b
	sectx2bb=Bladex.GetSector(-36539.7993232, -1430.30659707, -14296.7965775)
	sectx2bb.OnEnter=x2b


def x2b(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("7ORC")
		darfuncs.UnhideBadGuy("8ORC")
		fastGoTo("7ORC",-5433.86129088, -1431.33782692, -6146.5905313)
		fastGoTo("8ORC",-44026.13755, -1416.10743333, -6507.83294863)
		sectx2b=Bladex.GetSector(-11496.6820098, -2633.10867105, -14777.2905832)
		sectx2b.OnEnter=""
		sectx2bb=Bladex.GetSector(-36539.7993232, -1430.30659707, -14296.7965775)
		sectx2bb.OnEnter=""




def TerminanLasMuertes1():
	sectx3=Bladex.GetSector(-2697.15121495, -1426.93159658, 19743.4899609)
	sectx3.OnEnter=x3
	sectx3b=Bladex.GetSector(-43056.2044568, -1361.65218263, 19182.2275748)
	sectx3b.OnEnter=x3
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
	MusicTool.Music2Sector("saleagua",None)
	MusicTool.Music2Sector("salefuego",None)
	MusicTool.Music2Sector("salealtarfuego",None)
	MusicTool.Music2Sector("salealtaragua",None)

def TerminanLasMuertestorres():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
	MusicTool.Music2Sector("entratorres1",None)
	MusicTool.Music2Sector("entratorres2",None)
	MusicTool.Music2Sector("salehipostila",None)
	
	
	
def TerminanLasMuertespalazzo():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
	MusicTool.Music2Sector("entrapalacio",None)
	
def TerminanLasMuertesmurallas():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )
	MusicTool.Music2Sector("entramurallas",None)


def KreaOrkos1():
	darfuncs.UnhideBadGuy("9ORC")
	darfuncs.UnhideBadGuy("10ORC")

def KreaLichosc():
	darfuncs.UnhideBadGuy("21Lich")
	darfuncs.UnhideBadGuy("22Lich")
	darfuncs.UnhideBadGuy("23Lich")
	darfuncs.UnhideBadGuy("24Lich")
	darfuncs.UnhideBadGuy("25Lich")


def x3(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos1()
		sectx3=Bladex.GetSector(-2697.15121495, -1426.93159658, 19743.4899609)
		sectx3.OnEnter=""
		sectx3=Bladex.GetSector(-43056.2044568, -1361.65218263, 19182.2275748)
		sectx3.OnEnter=""


def Investigan():

	darfuncs.UnhideBadGuy("13Kngt")
	darfuncs.UnhideBadGuy("14Kngt")
	darfuncs.UnhideBadGuy("14cKngt")
	pers=Bladex.GetEntity("13Kngt")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,pers.GoTo,(-729.914209919, -2902.33860238, 8767.37819679))
	GoToMul("14Kngt")


def TerminanLasMuertes2():
	sectx6=Bladex.GetSector(14902.3079305, -4149.85542094, 19122.1948543)
	sectx6.OnEnter=x6

def x6(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("14aKngt")
		darfuncs.UnhideBadGuy("14bKngt")
		pers=Bladex.GetEntity("14aKngt")
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,pers.GoTo,(17534.2865825, -4120.31012976, 29098.9938392))
		fastGoTo("14bKngt",20111.0953351, -4158.12077831, 18978.548482)
		sectx6.OnEnter=""


def x4(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("DesertArq10")
		darfuncs.UnhideBadGuy("DesertArq11")
		pers=Bladex.GetEntity("DesertArq10")
		pers.GoToJogging = 1
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(13049.0534034, -10758.03713, 906.667332085))
		sectx4.OnEnter=""


def x9(sectorindex,entityname):

	if entityname=='Player1':
		pers=Bladex.GetEntity("16bORC")
		pers.GoTo(-55383.0294171, -9415.81887717, -35979.2243482)
		sectx9.OnEnter=""


def x10(sectorindex,entityname):

	if entityname=='Player1':
		GoToMul("16bKngt")
		sectx10.OnEnter=""



def x5(sectorindex,entityname):

	if entityname=='Player1':
		darfuncs.UnhideBadGuy("DesertArq12")
		pers=Bladex.GetEntity("DesertArq12")
		pers.GoToJogging = 1
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(-7006.79848978, -1436.1283162, 6913.61209412))
		sectx5.OnEnter=""

def x7(sectorindex,entityname):

	if entityname=='Player1':
		pers=Bladex.GetEntity("18Lich")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(21471.3448783, 2622.53939436, 43706.9158589))
		sectx7.OnEnter=""


def x8(sectorindex,entityname):

	if entityname=='18Lich':
		pers=Bladex.GetEntity("19Lich")
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5,pers.GoTo,(16936.3249929, 2881.81269525, 25932.3317791))
		sectx8.OnEnter=""


def x11():
	darfuncs.UnhideBadGuy("26Kngt")
	darfuncs.UnhideBadGuy("27Kngt")
	darfuncs.UnhideBadGuy("28Kngt")
	darfuncs.UnhideBadGuy("29Kngt")
	fastGoTo("27Kngt",-19467.4903022, -3214.65427491, 39892.9458191)
	fastGoTo("28Kngt",-24693.4762481, -3215.84094571, 52992.5159962)



def DustlyAwake(PersonName = "Player1"):
	per = Bladex.GetEntity(PersonName)
	if per:
		wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=PersonName
		wps.ParticleType="Dust"
		wps.Time2Live=64
		wps.RandomVelocity=1.0
		wps.Velocity=0,-100,0
		wps.NormalVelocity=3
		wps.YGravity=100
		wps.PPS=512
		wps.DeathTime=Bladex.GetTime()+0.5
		
def CambiazoGolemFinal():
	Bladex.GetEntity("estatuaG").SubscribeToList("Pin")
	darfuncs.UnhideBadGuy("keyGLM")

def CambiazoGolem():
	DustlyAwake("keyGLM")
	CierraBarrotes()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,CambiazoGolemFinal,())
	#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("Acombhard") )
	

def ClearCentralGolem():
	Bladex.CleanArea(-24515, -1408, 16473,5000)
			
def MuereElGolemMaldito():
	AbreBarrotes()
	ClearCentralGolem()
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0,ScriptCompleted,())

def finGrupoDKGT():
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("empty") )

###############################################################################
###                     GemaRay.py
###############################################################################
def CreaRayo(g1,g2):
	LaserGem1=Bladex.CreateEntity(g1+g2, "Entity ElectricBolt",-23495.2904721, -3184.99228383, 42521.8183761)
	LaserGem1.Target          = Bladex.GetEntity(g1).Position
	LaserGem1.Position        = Bladex.GetEntity(g2).Position
	LaserGem1.Damage          = 0
	LaserGem1.Active          = 1
	LaserGem1.MaxAmplitude    = 20
	LaserGem1.MinSectorLength = 1000000
	LaserGem1.InnerGlowColor  = LASER_GEMCOLOR[0]*LASER_INERFAC,LASER_GEMCOLOR[1]*LASER_INERFAC,LASER_GEMCOLOR[2]*LASER_INERFAC
	LaserGem1.CoreGlowColor   = LASER_GEMCOLOR[0]*LASER_COREFAC,LASER_GEMCOLOR[1]*LASER_COREFAC,LASER_GEMCOLOR[2]*LASER_COREFAC
	LaserGem1.Active          = 0
	return LaserGem1

def LanzaRayoVerdoso1(rayname):
	
	#AuxFuncs.FadeFrom(0.15,0.0,128,255,128)
	r = Bladex.GetEntity(rayname)
	r.Active = 1


def ReiniciaEscenaGemas():
	LaserPuerta1[0].Active = 0
	LaserPuerta1[1].Active = 0
	LaserPuerta2[0].Active = 0
	LaserPuerta2[1].Active = 0
	Cierracompuertas()
	CierraPuerta12()
	Bladex.GetEntity("FaltaGema").DeathTime = Bladex.GetTime()
	

def SegundaCamaraGema(a,b):
	darfuncs.LaunchMaxCamera("Rayos_verdesCamera02.cam",438,560)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,   AbrePuerta12,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 4.0,   x11,())
	

def FirstGemaScene():
	darfuncs.LaunchMaxCamera("Rayos_verdesCamera01.cam",0,437,SegundaCamaraGema)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("incomb1") )
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("acomblh") )
	CierrapuertadobleTemplo()
	puerta1.CloseDoor()
	puerta3.CloseDoor()
	
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 75.0/20.0, Abrecompuertas,())
	Bladex.AddScheduledFunc(Bladex.GetTime() +180.0/20.0, ComienzaGema1a,())
	Bladex.AddScheduledFunc(Bladex.GetTime() +320.0/20.0, ComienzaGema2a,())
	
	
	
	
def ComienzaGema1a():
	pos = Bladex.GetEntity("gema1a").Position
	Gems.GemCallBack = LanzaRayoVerdoso1
	Gems.GemParams = (LaserPuerta1[0].Name,)
	Gems.SetGemColor(Gems.GREEN_GEM)
	Gems.Concentrator(pos,(0,300,300))



def ComienzaGema2a():
	pos = Bladex.GetEntity("gema2a").Position
	Gems.GemCallBack = LanzaRayoVerdoso1
	Gems.GemParams = (LaserPuerta1[1].Name,)
	Gems.SetGemColor(Gems.GREEN_GEM)
	Gems.Concentrator(pos,(0,120,-350))

	LaserPuerta2[0].Active = 1
	RayoHit=Bladex.CreateEntity("FaltaGema", "Entity Particle System D1", 0,0,0)
	RayoHit.Time2Live=32
	RayoHit.YGravity=500
	RayoHit.ParticleType="Particulate"
	RayoHit.Friction=0.1
	RayoHit.Velocity=0,-500,1000
	RayoHit.RandomVelocity=10
	RayoHit.PPS = 255
	
	RayoHit.Position = (-32142.875, -4335.11, 23029.048)
	
	#RayoHit.DeathTime     = Bladex.GetTime()+1.0

def ComienzaGema2b():
	pos = (-32142.875, -4335.11, 23029.048)
	Bladex.GetEntity("gema2b").Position = pos

	Gems.GemCallBack = LanzaRayoVerdoso1
	Gems.GemParams = (LaserPuerta2[1].Name,)
	Gems.SetGemColor(Gems.GREEN_GEM)
	Gems.Concentrator(pos,(0,120,-350))
	
	Bladex.GetEntity("FaltaGema").DeathTime = Bladex.GetTime()	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 8.0,   AbrePuerta11,())
	
############### PONER GEMA ###############


def leaveGem(ent,event) :
	char = Bladex.GetEntity(ent)
	inv = char.GetInventory()
	handItem = char.InvRight

	inv.RemoveObject(handItem)
	inv.LinkRightHand("None")	
	gem = Bladex.GetEntity("gema2b")
	gem.Position = Bladex.GetEntity("GemBGPointer").Position
	gem.Orientation = 0.500000,0.500000,0.500000,0.500000
	gem.Static      = 1
	
	###### Process Here ########
	ComienzaGema2b()

def useInGemGhostP(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	obj = inv.GetSelectedObject()

	if B3DLib.GetXZDistance('Player1', "GemBGPointer")< 1000:
	
		if obj=="gema2b":
			Bladex.DeactivateInput()
			Actions.FreeBothHands("Player1",ContiueUseGem)
			Bladex.GetEntity("gema2b").SelfIlum = 0

def ContiueUseGem():
	Bladex.ActivateInput()
	if not char.InvLeft:
		Actions.TurnToFaceEntityNow("Player1","GemBGPointer")
		inv = char.GetInventory()
		inv.LinkRightHand("gema2b")
		char.LaunchAnmType("Fire2")
		char.AddAnmEventFunc("SetAlightEvent",leaveGem)



###############################################################################
###                     FinalScene.py
###############################################################################


def DerrumbeGo():

	o=Bladex.CreateEntity("DER3","Roca1",-109985.680000,7149.424000,-3851.826000,"Physic")
	o.Scale=1.909366
	o.Orientation=0.008536,-0.978110,-0.207904,-0.001814


	o=Bladex.CreateEntity("DER2","Roca1",-112665.369000,5693.222000,-6579.507000,"Physic")
	o.Scale=2.238882
	o.Orientation=0.079484,-0.756240,0.067886,-0.645890


	o=Bladex.CreateEntity("DER1","Roca2",-113955.369000,9145.504000,-2542.603000,"Physic")
	o.Scale=1.082857
	o.Orientation=0.026177,-0.999657,0.000000,0.000000


def StopGolemsMuerto(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("camara_desert_final.cam",219,220)
	
	#cam.SetPersonView("Player1")
	#cam.Cut()
	#Scorer.SetVisible(1)
	#Bladex.ActivateInput()
	
def FadeOutDesertFinal(sector,entity):
	AuxFuncs.FadeTo(4,10)
	import GotoMapVars
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,GotoMapVars.EndOfLevel,())
		

def GranFinalDelNivel():
		#Bladex.AddScheduledFunc(Bladex.GetTime() + 10.0,AuxFuncs.FadeTo,(9,20))
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("camara_desert_final.cam",0,-1)
		cam.AddCameraEvent(200,FadeOutDesertFinal)		
		cam.AddCameraEvent(-1,StopGolemsMuerto)	
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa4") )

		char.Position = -138000,4000,11000
		char.Angle    =  1.68078026915
		char.SetOnFloor()
		char.GoToJogging = 0
		char.GoTo(-170000,-3500,10000)
		AbrePuertadobleF()		
		
		Scorer.SetVisible(0)
		Bladex.DeactivateInput()
		

def GolemFinalMuerto(golem):
	global GolemsMuertos

	if GolemsMuertos:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(34,))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0,GranFinalDelNivel,())		
	else:
		GolemsMuertos = 1


def StopFinalScene(camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	Bladex.ActivateInput()

def FinChenen():
	Scorer.SetVisible(1)
	Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ActivateInput()

def CambiazoGolemsFinales():
	darfuncs.UnhideBadGuy("GolemMalo1")
	darfuncs.UnhideBadGuy("GolemMalo2")
	Bladex.GetEntity("GolemTrucho1").SubscribeToList("Pin")
	Bladex.GetEntity("GolemTrucho2").SubscribeToList("Pin")
	DerrumbeGo()
	dust.RemueveTierraGen(-112398.444758, 7931.75790328, -2360.22741367,2000,2000)
	dust.DropDust(-112398, 3000, -2360,0,-15000,0)
	derrumbemuroagua.Play(-112398, 3000, -2360,0)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("acomblh") )

def ActivateFinalDesert(sector,entity):
	if entity == "Player1":
		FinDesert1.OnEnter = ""
		FinDesert2.OnEnter = ""
		FinDesert3.OnEnter = ""
		char.QuickFace(1.68078026915)
		darfuncs.Temblores(3,400)
		_SoundTemblorFatidico.Play(-112665.369000,5693.222000,-6579.507000,0)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 2.5,FinChenen,())
		
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0,CambiazoGolemsFinales,())
		
		DustlyAwake("GolemMalo1")
		DustlyAwake("GolemMalo2")

		Scorer.SetVisible(0)
		Bladex.DeactivateInput()
		
		
		
###############################################################################
###                     pocimas.py
###############################################################################

