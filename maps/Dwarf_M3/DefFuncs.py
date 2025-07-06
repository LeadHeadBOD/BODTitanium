##///
##||| DWARF_M3/DEFFUNCS.PY TITANIUM
##||| Change list:
##||| * Final book now twinkles to make it more obvious as to what you're supposed to do since all the books look the same.
##||| * Removed comments for ScriptSkip events to make cutscenes skippable.
##||| * Final cutscene is longer in English due to slower narration.
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
# import stone			### PLAGUE: not actually ever used???
import heavyObjects		### PLAGUE: Whhhyyyy???
import Room
import Button
import GotoMapVars
import ScriptSkip

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para cuchillas.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateChispaIf(name,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u):
	chispa = Bladex.GetEntity(name)	
	if chispa == None:
		chispa=Bladex.CreateSpark(name, a,b,c,d,e,f,g,h,i,j,k,l,m, n, o, p, q,r,s,t,u)
	return chispa

def Blade0TimerFunc(blade_name,time):
	global b0_time
	global WAIT_TIME
	global CounterXCU
	
	itime=time-b0_time
	blade = Bladex.GetEntity(blade_name)	
	chispa = CreateChispaIf("Chispas0", -233260, -23572 + 2250,90102,-0.7, -0.7,0,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)

	if(itime < 0.25):
		blade.SetPosition(-231922 + 16000 * itime,(-23572 + 2250) - 9000 * itime,90102,0)
		if itime>0.0:
			if CounterXCU == 0:
				Sonido_Cuchilla_Inicio.PlaySound(0)
				Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,Sonido_Cuchilla_Bucle.PlaySound,(12,))
				CounterXCU = 1
	elif (itime < 1.0):
		blade.SetPosition(-231922 + 16000 * itime,-23572,90102,0)
	elif (itime < 1.25):
		blade.SetPosition(-231922 + 16000 * itime,-23572 + 9000 * (itime - 1.0),90102,0)
	else:
		b0_time = time+WAIT_TIME		
		blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
		if CounterXCU == 1:
			Sonido_Cuchilla_Fin.PlaySound(0)
			Sonido_Cuchilla_Bucle.StopSound()
		CounterXCU = 0
		if (stop_blades):
			if(playerstate == 0):
				StopBlade(blade,chispa)

	if itime < 0.0:
		chispa.Position = 0,0,0
	else:
		chispa.Position = blade.Position[0] + 2250, -23672, 90102
		Sonido_Cuchilla_Inicio.Position = chispa.Position
		Sonido_Cuchilla_Bucle.Position  = chispa.Position
		Sonido_Cuchilla_Fin.Position    = chispa.Position
	
	blade.Rotate(0.0,1.0,0.0,0.3,1)

		

def Blade1TimerFunc(blade_name,time):
	global b1_time
	global WAIT_TIME
	global CounterXCU1
	
	itime=time-b1_time
	blade=Bladex.GetEntity(blade_name)
	chispa=CreateChispaIf("Chispas1", -233260,  -25151, 87000,-0.7,0, 0.7,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)	

	if(itime < 0.25):
		blade.SetPosition(-231922 + 12000 * itime,-25101,(86997 - 2250) + 9000 * itime,0)
		if itime>0.0:
			if CounterXCU1 == 0:
				Sonido_Cuchilla_Inicio1.PlaySound(0)
				Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,Sonido_Cuchilla_Bucle1.PlaySound,(12,))
				CounterXCU1 = 1
	elif (itime < 1.41):
		blade.SetPosition(-231922 + 12000 * itime,-25101,86997,0)
	elif (itime < 1.66):
		blade.SetPosition(-231922 + 12000 * itime,-25101,86997 - 9000 * (itime - 1.41),0)
	else:
		b1_time = time+WAIT_TIME
		blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
		if CounterXCU1 == 1:
			Sonido_Cuchilla_Fin1.PlaySound(0)
			Sonido_Cuchilla_Bucle1.StopSound()
		CounterXCU1 = 0		
		if (stop_blades):
			if(playerstate == 0):
				StopBlade(blade,chispa)
	
	if itime < 0.0:
		chispa.Position = 0,0,0
	else:
		chispa.Position = blade.Position[0] + 2250, -25151, 86997
		Sonido_Cuchilla_Inicio1.Position = chispa.Position
		Sonido_Cuchilla_Bucle1.Position  = chispa.Position
		Sonido_Cuchilla_Fin1.Position    = chispa.Position

	blade.Rotate(0.0,1.0,0.0,-0.3,1)

def Blade2TimerFunc(blade_name,time):
	global b2_time
	global WAIT_TIME
	global CounterXCU2
	itime=time-b2_time
		
	blade=Bladex.GetEntity(blade_name)	
	chispa=CreateChispaIf("Chispas2", -233260,  -25151, 92600,-0.7, 0.0,-0.7,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)

	if(itime < 0.25):
		blade.SetPosition(-231922 + 14000 * itime,-25101,(93154 + 2250) - 9000 * itime,0)
		if itime>0.0:
			if CounterXCU2 == 0:
				Sonido_Cuchilla_Inicio2.PlaySound(0)
				Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,Sonido_Cuchilla_Bucle2.PlaySound,(12,))
				CounterXCU2 = 1				
	elif (itime < 1.17):
		blade.SetPosition(-231922 + 14000 * itime,-25101,93154,0)
	elif (itime < 1.42):
		blade.SetPosition(-231922 + 14000 * itime,-25101,93154 + 9000 * (itime - 1.17),0)
	else:
		b2_time = time+WAIT_TIME		
		blade.MessageEvent(MESSAGE_START_WEAPON,0,0)		
		if CounterXCU2 == 1:
			Sonido_Cuchilla_Fin2.PlaySound(0)
			Sonido_Cuchilla_Bucle2.StopSound()
		CounterXCU2 = 0
		if (stop_blades):
			if(playerstate == 0):
				StopBlade(blade,chispa)

	if itime < 0.0:
		chispa.Position = 0,0,0
	else:
		chispa.Position = blade.Position[0] + 2250, -25151, 93154
		Sonido_Cuchilla_Inicio2.Position = chispa.Position
		Sonido_Cuchilla_Bucle2.Position  = chispa.Position
		Sonido_Cuchilla_Fin2.Position    = chispa.Position

	blade.Rotate(0.0,1.0,0.0,0.3,1)

b0_time=0.0

def LaunchBlade0():
	global b0_time	
	b0_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade0")

	chispas0=CreateChispaIf("Chispas0", -233260, -23572 + 2250,90102,-0.7, -0.7,0,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)
	
	blade.Solid=0
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	blade.TimerFunc=Blade0TimerFunc
	blade.SubscribeToList("Timer60")
	

def LaunchBlade1():
	global b1_time
	b1_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade1")	

	chispas1=CreateChispaIf("Chispas1", -233260,  -25151, 87000,-0.7,0, 0.7,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)

	blade.Solid=0
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)
	blade.TimerFunc=Blade1TimerFunc
	blade.SubscribeToList("Timer60")

b2_time=0.0

def LaunchBlade2():
	global b2_time
	b2_time=Bladex.GetTime()
	blade=Bladex.GetEntity("Blade2")	

	chispas2=CreateChispaIf("Chispas2", -233260,  -25151, 92600,-0.7, 0.0,-0.7,0.5,3000,2000,0,150, 200, 100, 0, 32, 32, 32,800,0.1,100,0)

	blade.Solid=0	
	blade.MessageEvent(MESSAGE_START_WEAPON,0,0)	
	blade.TimerFunc=Blade2TimerFunc
	blade.SubscribeToList("Timer60")	

def LaunchBlades():
	global blades_ready	
	LaunchBlade2()
	LaunchBlade1()
	LaunchBlade0()	
	blades_ready=0
	

def ActivateBlades(SectorIndex,EntityName):
	global playerstate
	global stop_blades
	if (EntityName == "Player1"):
		if (playerstate == 0):
			playerstate = 1
			stop_blades = 0

			if(blades_ready):
				#print ("Activada")
				Sonido_TrampaCuchilla_Activada.Play(-208922.078132,-25572.057567,90102.453506,0)
				LaunchBlades()

def DeactivateBlades(SectorIndex,EntityName):
	global playerstate
	global stop_blades
	if (EntityName == "Player1"):
		if (playerstate == 1):
			playerstate = 0
			stop_blades = 0			
			Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,StopBlades,())

def StopBlades():
	global stop_blades
	stop_blades = 1

def StopBlade(blade,chispa):
	global blades_ready
	blade.TimerFunc=None
	blade.RemoveFromList("Timer60")
	chispa.SubscribeToList("Pin")
	blades_ready = 1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para pulsadores.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AbrirPuerta():
	global camdelta
	#AbreCam.PTS = [((-44053.6946095, -9790.04993464, -70329.2970342), (-44345.0324903, -9651.22325015, -70743.8150209), 2), ((-55452.8562414, -10100.7981767, -75752.235663), (-55422.8271935, -9481.28263837, -78178.2692823), 3), ((-44461.8860287, -10089.3462153, -70990.3420748), (-42429.5741962, -9470.75470874, -72308.9407869), 4)]
	#AbreCam.AbreCam()
	darfuncs.LaunchMaxCamera("Enanos_Pulsadores.cam",0,-1)
	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0,Puerta1Pulsa.OpenDoor,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("coro6") )

def ResetCombinado():
	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0,CoButton.Reset,(1,))

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************				        **************************
#*******************************   Definiciones para chorritos.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

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

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para cascadapint.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CreateCascada2(Cascada,p,d,v,pc,Time = 16,Grav = 13000,PPS = 600):
	cascada=Bladex.CreateEntity(Cascada, "Entity Particle System D2",p[0],p[1],p[2])
	cascada.D=d[0],d[1],d[2]
	cascada.ParticleType="AguaCpi"
	cascada.Friction=0.07
	cascada.RandomVelocity=10.0
	cascada.Velocity=v[0],v[1],v[2]
	cascada.PPS=PPS
	cascada.YGravity=Grav
	cascada.Time2Live=Time

	espuma=Bladex.CreateEntity(Cascada+"Espumapi", "Entity Particle System D2",pc[0],pc[1],pc[2])
	espuma.D=d[0],d[1],d[2]
	espuma.ParticleType="Espumapi"
	espuma.PPS=50
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, -1000.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.RandomVelocity_V=30.0
	espuma.Time2Live=10


def BorrarCascada2(cascada):
	cascada = Bladex.GetEntity(cascada)
	cascada.SubscribeToList("Pin")
	
	espuma = Bladex.GetEntity(cascada+"Espumapi")
	espuma.SubscribeToList("Pin")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para biblio.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Descubre():
	AbreCam.PTS = [((-274556.8198+LIBROS_DELTA_X, -28598.1705645, 71978.8687873), (-270674.229433+LIBROS_DELTA_X, -27486.8043323, 73945.9542189), 2), ((-266831.590664+LIBROS_DELTA_X, -28576.9748604, 71737.8566917), (-269720.454833+LIBROS_DELTA_X, -27460.5213217, 75019.9637074), 2), ((-268913.463945+LIBROS_DELTA_X, -28434.4889486, 76751.1828779), (-269681.065822+LIBROS_DELTA_X, -27798.3886644, 76729.1473585), 2), ((-271166.038343+LIBROS_DELTA_X, -28276.4168647, 71250.7237261), (-271215.650118+LIBROS_DELTA_X, -27657.5856075, 73673.7554744), 2)]
	AbreCam.AbreCam();
	sb1.Active=1
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("coro6") )

	o=Bladex.CreateEntity("libroestante4","Libro",-269220.640000+LIBROS_DELTA_X,-26051.900000,75868.913000)
	o.Static=1
	o.Scale=1.745810
	o.Orientation=0.000000,0.942204,0.001940,0.335033
	Reference.EntitiesSelectionData['libroestante4']=         [0, 0,  " kk"]
	
	
	o=Bladex.CreateEntity("libroestante3","Libro2",-269161.796000+LIBROS_DELTA_X,-26019.991000,77217.515000)
	o.Static=1
	o.Scale=2.173037
	o.Orientation=0.000000,0.255856,0.003536,0.966709
	Reference.EntitiesSelectionData['libroestante3']=         [0, 0,  " kk"]
	
	
	o=Bladex.CreateEntity("libroestante1","Libro2",-269444.077000+LIBROS_DELTA_X,-26207.608000,76197.129000)
	o.Static=1
	o.Scale=1.474123
	o.Orientation=0.003349,-0.999901,-0.008476,-0.010755
	Reference.EntitiesSelectionData['libroestante1']=         [0, 0,  " kk"]
	
	
	o=Bladex.CreateEntity("libroestante2","Libro3",-268690.268000+LIBROS_DELTA_X,-26186.471000,76772.439000)
	o.Static=1
	o.Scale=1.816697
	o.Orientation=0.981649,-0.018665,-0.149920,0.116363
	Reference.EntitiesSelectionData['libroestante2']=         [0, 0,  " kk"]
	
	o=Bladex.CreateEntity("libroestante5","Libro2",-270649.528000+LIBROS_DELTA_X,-27409.675000,77121.237000)
	o.Static=1
	o.Scale=1.986894
	o.Orientation=0.030844,0.030844,0.706434,-0.706434
	Reference.EntitiesSelectionData['libroestante5']=         [0, 0,  " kk"]
	
	
	o=Bladex.CreateEntity("llave3","Llavecobox",-270013.422151+LIBROS_DELTA_X,-27031.501485,76605.819869)
	o.Static=0
	o.Scale=1.000000
	o.Orientation=0.012075,0.988262,0.001038,-0.152288
	Stars.Twinkle("llave3")
	darfuncs.SetHint(o,"Bronze Key")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para DERR.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def polvoTri(a,b,c,name):
	dust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2] )
	dust.D1= b[0]-a[0] ,b[1]-a[1] ,b[2]-a[2]
	dust.D2= c[0]-a[0] ,c[1]-a[1] ,c[2]-a[2]
	dust.ParticleType="MediumDust"
	dust.YGravity=30.0
	dust.Friction=0.2
	dust.PPS=812
	dust.Velocity=0.0, -410.0, 0.0
	dust.RandomVelocity=40.0
	dust.Time2Live=13
	dust.DeathTime=Bladex.GetTime()+40.0/60.0

def polvoDelDerrumbamiento():
	p0 = -110500,-8500,-63500
	p1 = -106000,-8500,-63500
	p2 = -107000,-8500,-54000
	p3 = -110500,-8500,-54000

	polvoTri(p0,p1,p2,"dustA")
	polvoTri(p1,p2,p3,"dustB")


def Cont2Derr():
	derr1.DoBreak((0, -2, 0), (-108500, -7000, -56400), (0.0, 0.0, 0.0))
	derr2.DoBreak((0, -4, 0), (-108500, -7000, -61400), (0.0, 0.0, 0.0))
	derr3.DoBreak((0, 1, 0), (-108500, -17000, -56400), (0, 0.0, 0.0))
	derr4.DoBreak((0, -5, 0), (-108500, -17000, -61400), (0, 0.0, 0.0))
	polvoDelDerrumbamiento()
	
def ContDerr():
	derrumbesuelopiedra.Play(-108500, -11000, -56400)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, Cont2Derr, ())

def Derrumba(sector_index, entity_name):
	if entity_name=="Player1":
		sectorderr.OnWalkOn=""
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerr, ())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para elevator.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def SubeElevador2():

	global enmarcha
	if enmarcha:
		return
	desplazamientos=(1000.0, 5000.0, 1000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.CloseDoor()
	enmarcha=1

def BajaElevador2():

	desplazamientos=(1000.0, 5000.0, 1000.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.OpenDoor()

##############
def Elevador2Arriba():

	global enmarcha
	enmarcha=0

## DEFINIMOS LA FUNCION QUE AUTOMATICAMENTE BAJARA EL ELEVADOR 3 SEGUNDOS DESPUES DE DETENERSE EN SU PUNTO MAS ALTO

def EsperaYBajaElevador2():

	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, BajaElevador2, ())

## ESTABLECEMOS QUE EL ELEVADOR ESTARÁ EN REPOSO CUANDO EL PARÁMETRO enmarcha SEA CERO


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para flechas_yo.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def BorraFlecha(Name):
	global InsideTrap
	en = Bladex.GetEntity(Name)
	if (en.Parent==None) | (en.Parent == ""):
		if(en.Kind == "Flecha"):
			en.SubscribeToList("Pin")
	if InsideTrap:
		DropArrow()



def Entrampa(sectorindex,entityname):  
	global InsideTrap
	
	if entityname == "Player1":
		InsideTrap = 1
		DropArrow()
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, DropArrow,())

def Saltrampa(sectorindex,entityname):  
	global InsideTrap
	if entityname == "Player1":
		InsideTrap = 0

def DropArrow():
	global __X__
	global __Y__
	
	SPEED = 30000
	
	o=Bladex.CreateEntity(Bladex.GenerateEntityName(), "Flecha", -70689.0+__X__, -9982.0, whrandom.randint(-76121.0+__Z__,-67121.0+__Z__))
	o.Orientation=0.50005787611, 0.50005787611, -0.499942094088, -0.499942094088
	flechazo.Position = o.Position
	flechazo.PlaySound(1)
	char = Bladex.GetEntity("Player1")
	
	o.Arrow=1
	o.Scale=0.7
	o.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
	o.MessageEvent(Reference.MESSAGE_START_TRAIL, 0,0)
	o.Gravity = 0,0,0
	
	vx = char.Position[0]-o.Position[0]
	vz = char.Position[2]-o.Position[2]
	dist = math.sqrt(vx*vx+vz*vz)/SPEED
	vx = vx/dist
	vz = vz/dist
	
	o.Fly(vx,0,vz)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, BorraFlecha,(o.Name,))
	return o

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para FinalScene.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def sReadBookEv(c,f):
	sReadBook.Position = char.Position
	sReadBook.PlaySound(0)
	
def escribirtexto(Camera,Frame):	
	GameText.WriteText("M3T3")	
	AuxFuncs.FadeTo(9,20)
	if Reference.DEMO_MODE==0:
		GotoMapVars.MapText(3,"D_M3_T2")

def ChangeBook(Camera,Frame):
	inv = char.GetInventory()
	inv.LinkRightHand("None")	

	libro2.Position = -276460.924000,-26975.092000,76582.933000
	libro2.Orientation = 0.707106,0.707106,-0.001126,0.001126

def StopCameraFinal(Camera,frame):
	#Bladex.ActivateInput()	
	ScriptSkip.SkipScriptEnd()
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	#Scorer.SetVisible(1)	
	import Language                                 # Added.
	language = Language.CheckFallback()             # 
	if language == "EnglishUS" or "English":        #
		time = 5.5                                  #
	else:                                           #   -LeadHead
		time = 3.5
	if Reference.DEMO_MODE==0:
		Bladex.AddScheduledFunc(Bladex.GetTime()+time,GotoMapVars.EndOfLevel,())
	else:
		AuxFuncs.setDemoBg(time)

def ChangeCameraFinal2(Camera,Frame):
	cam = Bladex.GetEntity("Camera")

	cam.SetMaxCamera("final_dwarfCamera03.cam",286,-1)
	
	cam.AddCameraEvent(-1,StopCameraFinal)


def ChangeCameraFinal(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	
	cam.SetMaxCamera("final_dwarfCamera02.cam",160,286)
	
	cam.AddCameraEvent(-1,ChangeCameraFinal2)
	cam.AddCameraEvent(280 - 160,ChangeBook)

	cam.AddCameraEvent(166 -160,ReverStepEv)
	cam.AddCameraEvent(177 -160,ReverStepEv)
	cam.AddCameraEvent(188 -160,ReverStepEv)
	cam.AddCameraEvent(199 -160,ReverStepEv)
	cam.AddCameraEvent(211 -160,ReverStepEv)
	cam.AddCameraEvent(222 -160,ReverStepEv)
	cam.AddCameraEvent(235 -160,ReverStepEv)
	cam.AddCameraEvent(247 -160,ReverStepEv)
	cam.AddCameraEvent(260 -160,sReadBookEv)

	cam.AddCameraEvent(246-160,escribirtexto)
	
	
	

def GetBook(Camera,Frame):
	inv = char.GetInventory()
	inv.LinkRightHand("LibroFin1")
	sTakeBook.Position = char.Position
	sTakeBook.PlaySound(0)
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("final") )

def LaunchAnimationFinal(entity):
	global player
	char = Bladex.GetEntity("Player1")
	
	char.Position = -276276.531,-27446,60054.25	
	char.Angle = 3.14
	
	Scorer.SetVisible(0)

	char.Wuea = Reference.WUEA_ENDED
	char.SetTmpAnmFlags(1,1,1,0,5,1)	
	char.LaunchAnimation("Dwf_final_dwarf")	
	char.SetOnFloor()

	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("final_dwarfCamera01.cam",0,160)	

	cam.AddCameraEvent(53 -0,ReverStepEv)
	cam.AddCameraEvent(73 -0,ReverStepEv)
	cam.AddCameraEvent(84 -0,ReverStepEv)
	cam.AddCameraEvent(95 -0,ReverStepEv)
	cam.AddCameraEvent(107-0,ReverStepEv)
	cam.AddCameraEvent(118-0,ReverStepEv)
	cam.AddCameraEvent(131-0,ReverStepEv)
	cam.AddCameraEvent(141-0,ReverStepEv)
	cam.AddCameraEvent(153-0,ReverStepEv)
	
	
	cam.AddCameraEvent(-1,ChangeCameraFinal)
	cam.AddCameraEvent(26,GetBook)

	# Bladex.DeactivateInput()                  # Re-enabled
	ScriptSkip.SkipScriptStart("FinalEnano")    #       -LeadHead
	
	
def UseMagicBook(entity = 0,usefrom = 0):
	Stars.DeTwinkle("LibroFin1")    # Added      -LeadHead
    
	char.Angle = 3.14
	
	if (char.InvLeft == "" and char.InvRight == ""):
		LaunchAnimationFinal(entity)
	else:		
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)	

		char.SetOnFloor()
		Actions.FreeBothHands("Player1")
		char.AnmEndedFunc = LaunchAnimationFinal


def TakeMagicBook():
	Bladex.AddScheduledFunc(Bladex.GetTime(),UseMagicBook,())

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para EscenaOrk.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DirigeOrcos1():
	enem1 = Bladex.GetEntity("OrkFight1")
	if enem1 and enem1.Life>0:
		#enem1.InterruptCombat()		
		enem1.Blind=1
		enem1.Deaf=1
		enem1.GoTo(-90000,-10000,-8000)	

	enem2 = Bladex.GetEntity("OrkFight2")
	if enem2 and enem2.Life>0:
		#enem2.InterruptCombat()
		enem2.Blind=1
		enem2.Deaf=1
		enem2.GoTo(-89000,-10000,-8000)

def DirigeOrcos2():
	enem1 = Bladex.GetEntity("OrkFight3")	
	if enem1 and enem1.Life>0:
		enem1.Blind=1
		enem1.Deaf=1
		enem1.GoTo(-60000,-10000,8000)

	enem2 = Bladex.GetEntity("OrkFight4")	
	if enem2 and enem2.Life>0:
		enem2.Blind=1
		enem2.Deaf=1
		enem2.GoTo(-60000,-10000,7000)

def BorraOrcos1():
	enem1 = Bladex.GetEntity("OrkFight1")

	if (enem1):
		enem1.Life = 0

	enem2 = Bladex.GetEntity("OrkFight2")

	if (enem2):
		enem2.Life = 0

def BorraOrcos2():
	enem1 = Bladex.GetEntity("OrkFight3")

	if (enem1):
		enem1.Life = 0

	enem2 = Bladex.GetEntity("OrkFight4")

	if (enem2):
		enem1.Life = 0

def BorraDwf1():
	enem1 = Bladex.GetEntity("DwfFight1")

	if (enem1):
		enem1.Life = 0

def BorraDwf2():
	enem1 = Bladex.GetEntity("DwfFight3")

	if (enem1):
		enem1.Life = 0

	enem2 = Bladex.GetEntity("DwfFight2")

	if (enem2):
		enem2.Life = 0		

def DwarfMuerto1(Dwarf):	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,DirigeOrcos1,())	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 27.0,BorraOrcos1,())		
	malo = Bladex.GetEntity("DwfFight1")
	arma = Bladex.GetEntity("WeaponDwf1")
	Actions.RemoveFromInventory (malo, arma,"DropRightEvent")
	arma.Impulse(0.0, 0.0, 0.0)
	Breakings.ExplodeSpecialObject("WeaponDwf1",50000)

def DwarfMuerto2(Dwarf):	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,DirigeOrcos2,())	
	Bladex.AddScheduledFunc(Bladex.GetTime() + 27.0,BorraOrcos2,())

	malo = Bladex.GetEntity("DwfFight2")
	arma = Bladex.GetEntity("WeaponDwf2")
	Actions.RemoveFromInventory (malo, arma,"DropRightEvent")
	arma.Impulse(0.0, 0.0, 0.0)
	Breakings.ExplodeSpecialObject("WeaponDwf2",50000)
	
	
def StopCameraFight(Camera,frame):
	#char.Angle = 0.0
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")		
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def StartAtack(SecIndex,Entity):
	global EscenaFight

	if (Entity == "Player1" and EscenaFight == 0):
		cam = Bladex.GetEntity("Camera")		
		cam.SetMaxCamera("pelea enanos orcosCamera03.cam",0,-1)
		cam.AddCameraEvent(-1,StopCameraFight)
		Bladex.ExeMusicEvent( Bladex.GetMusicEvent("sorpresa1b") )
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, Bladex.ExeMusicEvent,(Bladex.GetMusicEvent("escena_Orc"),))

		Scorer.SetVisible(0)

		Bladex.SetListenerPosition(2)
		ScriptSkip.SkipScriptStart("EscenaPeleaOrcos")
		#Bladex.DeactivateInput()

		EscenaFight = 1
		Ork1 = Bladex.GetEntity("OrkFight1")
		#Ork2 = Bladex.GetEntity("OrkFight2")
		Dwf1 = Bladex.GetEntity("DwfFight1")
	
		Ork3 = Bladex.GetEntity("OrkFight3")
		#Ork4 = Bladex.GetEntity("OrkFight4")
		Dwf2 = Bladex.GetEntity("DwfFight2")		

		Ork1.SetEnemy(Dwf1)
		#Ork2.SetEnemy(Dwf1)
		Dwf1.SetEnemy(Ork1)

		Ork3.SetEnemy(Dwf2)
		#Ork4.SetEnemy(Dwf2)
		Dwf2.SetEnemy(Ork3)		

def EraseFightOrk(sector,entity):
	if entity == "Player1":
		EraseSec1.OnEnter = ""
		EraseSec2.OnEnter = ""
		BorraOrcos1()
		BorraOrcos2()
		BorraDwf1()
		BorraDwf2()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Escalera.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Descubrelo():
	escalon1.CloseDoor()
	escalon2.CloseDoor()
	escalon3.CloseDoor()
	escalon4.CloseDoor()
	escalon5.CloseDoor()
	escalon6.CloseDoor()
	escalon7.CloseDoor()
	escalon8.CloseDoor()
	escalon9.CloseDoor()
	escalon10.CloseDoor()
	escalon11.CloseDoor()
	escalon12.CloseDoor()
	escalon13.CloseDoor()
	escalon14.CloseDoor()
	escalon15.CloseDoor()
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("biblio2") )

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AbreDespuesDeMorir(entity_name):
	#print "abre la puerta"
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(23,))
	Abrepuertasag()
	Bladex.GetEntity(entity_name).Data.StdImDead(entity_name)

def CreaOrcochulo():
	darfuncs.UnhideBadGuy("37ORC")
	GoToJogging=1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, CorreOrcochulo,())

def CorreOrcochulo():
	o = Bladex.GetEntity("37ORC")
	GoToJogging=1
	o.GoTo(-178761.371178, -12890.0515079, 12298.5019555)
	o.RouteEndedFunc = MueveOrcoListo

def MueveOrcochulo(Entity):
	o = Bladex.GetEntity("4ORC")
	o.GoTo(-172272.038284, -10890.5893725, 13436.3761261)

def x1(sectorindex,entityname):

  if entityname=='Player1':
    CreaOrcoListo()
    sectx1.OnEnter=""

def DwarfDefeatsOrc(person):
	Bladex.GetEntity(person).Data.ImDeadFuncX(person)
	Bladex.TriggerEvent(2)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Enanos.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def ReverStepEv(c,f):
	auxs = ReverStep[0]
	ReverStep.remove(auxs)
	ReverStep.append(auxs)
	
	ReverStep[0].Position = char.Position
	ReverStep[0].PlaySound(0)

def QueSueneElBasofio():	
	GameText.WriteText("M3T2")

############################
### Script de la masacre ###
############################
def CaMasacre1(sectorindex,entityname):  	
	if entityname == "Player1":
		cam = Bladex.GetEntity("Camera")
		cam.SetMaxCamera("Dwf_masacreCamera01.cam",0,60)
		cam.AddCameraEvent(-1,StopCameraMasacre1)
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("enano"))
		SEscenaMasacre.OnEnter = ""
		ScriptSkip.SkipScriptStart("EscenaMasacreEnanos")       # Re-enabled
		# Bladex.DeactivateInput()                              #       -LeadHead
		Scorer.SetVisible(0)		
		

def StopCameraMasacre1(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dwf_masacreCamera02.cam",61,120)
	cam.AddCameraEvent(50,EnanosAnimation)
	cam.AddCameraEvent(-1,StopCameraMasacre2)

def EnanosAnimation(camera,frame):
	char = Bladex.GetEntity("Player1")
	char.Position = 112257.82,6466.364,-27417.012
	char.Angle = 3.1415
	char.LaunchAnimation("Dwf_masacre")
	char.SetOnFloor()

def StopCameraMasacre2(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Dwf_masacreCamera03.cam",121,320)

	cam.AddCameraEvent(124-121,ReverStepEv)
	cam.AddCameraEvent(143-121,ReverStepEv)
	cam.AddCameraEvent(162-121,ReverStepEv)
	cam.AddCameraEvent(181-121,ReverStepEv)
	cam.AddCameraEvent(199-121,ReverStepEv)
	cam.AddCameraEvent(211-121,ReverStepEv)
	
	cam.AddCameraEvent(-1,StopCameraMasacre3)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, QueSueneElBasofio,())	
	

def StopCameraMasacre3(Camera,frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()
	# Bladex.ActivateInput()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para InicioScene.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def musicaytexto(Camera,Frame):
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicio"))
	GameText.WriteText("M3T1")
	if Reference.DEMO_MODE==0:
		GotoMapVars.MapText(3,"D_M3_T1")
"""
def DeleteComplements():
	
	weaponini.Position = weaponini2.Position
	weaponini.Orientation = weaponini2.Orientation
	weaponini.Alpha = 1.0	

	#shieldini.Position = 54344,7390,-121002
	#shieldini.Orientation = 0.3878,-0.466144,0.339895,-0.718859
	shieldini.Position = shieldini2.Position
	shieldini.Orientation = shieldini2.Orientation

	shieldini.Alpha = 1.0

	shieldini2.SubscribeToList("Pin")
	weaponini2.SubscribeToList("Pin")
"""

def Clean(Camera,Frame):	
	cam = Bladex.GetEntity("Camera")
	char = Bladex.GetEntity("Player1")
	soundclean.Position = cam.Position	

	if (Frame == 782):
		soundclean.PlaySound(0)		
		polvo=Bladex.CreateEntity("Polvo1015", "Entity Particle System D1", 58810,7112,-118000)
		polvo.Velocity=10.0, 0.0, 10.0
	else:		
		polvo=Bladex.CreateEntity("Polvo1135", "Entity Particle System D1", 59530,6336,-118130)
		polvo.Velocity=10.0, 0.0, -10.0

	polvo.ParticleType="Dust"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=60
	polvo.RandomVelocity=0.0
	polvo.DeathTime=Bladex.GetTime()+3.0/60.0
	

def StopCameraInicio(Camera,frame):
	#char.Angle = 0.0
	cam = Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	#cam.Cut()
	Bladex.SetListenerPosition(1)

	Scorer.SetVisible(1)
	ScriptSkip.SkipScriptEnd()      # Re-enabled -LeadHead
	# Bladex.ActivateInput()

	#DeleteComplements()
	shieldini.Mass        =  shieldini.Data.Massa
	weaponini.Mass        =  weaponini.Data.Massa

def SoundBurr(Camera,Frame):
	#char = Bladex.GetEntity("Player1")
	cam = Bladex.GetEntity("Camera")
	soundburr.Position = cam.Position	
	soundburr.PlaySound(0)	

def SoundLevantarse(Camera,Frame):
	#char = Bladex.GetEntity("Player1")
	cam = Bladex.GetEntity("Camera")
	soundlevantarse.Position = cam.Position	
	soundlevantarse.PlaySound(0)	

def ChangeCameraInicio(Camera,Frame):
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("entrada_enanoCamera02.cam",233,-1)	
	
	cam.AddCameraEvent(-1,StopCameraInicio)
	#cam.AddCameraEvent(1,Avalancha)
	cam.AddCameraEvent(290 - 233,Avalancha)
	cam.AddCameraEvent(440 - 233,SoundBurr)
	cam.AddCameraEvent(620 - 233,SoundBurr)
	cam.AddCameraEvent(750 - 233,SoundLevantarse)
	cam.AddCameraEvent(1015 - 233,Clean)
	cam.AddCameraEvent(1020-233,musicaytexto)
	cam.AddCameraEvent(1135 - 233,Clean)

def AnmComplements(camera,frame):	
	inv = char.GetInventory()

	inv.RemoveWeapon(char.InvRight)
	inv.RemoveShield(char.InvLeft)
	inv.LinkRightHand("None")
	inv.LinkLeftHand("None")

	weaponini.Alpha = 1.0
	shieldini.Alpha = 1.0
	
	#weaponini.Position = (54232, -3997, -105701)
	#weaponini.Orientation = (0.192901223898, -0.793508410454, -0.542288601398, 0.197627559304)
	weaponini.Data.Massa  = weaponini.Mass
	weaponini.Mass        = 3.5

	#shieldini.Position    = (54232, -4900, -105701)
	#shieldini.Orientation = (0.192901223898, -0.793508410454, -0.542288601398, 0.197627559304)
	shieldini.Data.Massa  = shieldini.Mass
	shieldini.Mass        = 3.5

	weaponini.Impulse(3000,7000,-22000)

	shieldini.Impulse(2000,7000,-22000)

def Hit(Camera,Frame):
	soundhitplayer.Position = char.Position	
	soundhit2player.Position = char.Position
	#soundhit3player.Position = char.Position

	pps = 300	
	
	if (Frame == 50):
		polvo=Bladex.CreateEntity("Polvo50", "Entity Particle System D1", 55000,-3500,-104568)
		polvo.Velocity=0.0, -200.0, 0.0
	else:
		soundhitplayer.StopSound()
		soundhit2player.StopSound()

		if (Frame == 69):
			polvo=Bladex.CreateEntity("Polvo69", "Entity Particle System D1", 55270,-2325,-106600)
			polvo.Velocity=0.0, -20.0, 0.0
		elif (Frame == 115):
			polvo=Bladex.CreateEntity("Polvo115", "Entity Particle System D2", 56500,1500,-111143)
			polvo.D = 0,0,-1000
			polvo.Velocity=400.0, -200.0, -400.0
		elif (Frame == 175):
			polvo=Bladex.CreateEntity("Polvo175", "Entity Particle System D2", 59200,7500,-117000)
			polvo.D = 0,0,-1000
			polvo.Velocity=400.0, -200.0, -400.0
			pps = 900

	polvo.ParticleType="MediumDust"
	polvo.YGravity=0.0
	polvo.Friction=0.2
	polvo.PPS=pps
	polvo.RandomVelocity=45.0	
	polvo.DeathTime=Bladex.GetTime()+3.0/60.0	
	soundhitplayer.PlaySound(0)	
	soundhit2player.PlaySound(0)

def Avalancha(Camara,Frame):
	if (Frame <> 1):
		soundavalanche.StopSound()
	
	soundavalanche.Position = 58675.3793567, 6565.4, -118361.612274
	soundavalanche.PlaySound(0)

def LaunchStones(Root,Start,End):
	global Launched
	i = Start	

	for i in range(End):
		stone = Bladex.GetEntity(Root+`i`)		
		stone.Static = 1
		stone.Solid = 0
		
		if (Launched):
			stone2 = Bladex.GetEntity("NewStone"+`i`)
		else:
			stone2 = Bladex.CreateEntity("NewStone"+`i`,stone.Kind,0,0,0)
			stone2.Static = 0
			stone.Alpha = 0.0	# was 1.0, left floating stones in the original cutscene	-LeadHead

		stone2.Orientation = stone.Orientation
		stone2.Position = stone.Position
		stone2.Impulse(0,0,0)
	Launched = 1



def LaunchAnimationStart():
	char.Position = 54982,-9000,-103329
	char.Angle = 3.14
	char.Wuea = Reference.WUEA_ENDED
	#char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0) # cicla, no colisiona y no hace transicion
	char.LaunchAnimation("Dwf_entrada")	
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("entrada_enanoCamera02.cam",0,232)	
	cam.AddCameraEvent(-1,ChangeCameraInicio)
	#cam.AddCameraEvent(-1,StopCameraInicio)
	cam.AddCameraEvent(50,Hit)
	cam.AddCameraEvent(69,Hit)	
	cam.AddCameraEvent(91,AnmComplements)
	cam.AddCameraEvent(115,Hit)
	cam.AddCameraEvent(175,Hit)
	Bladex.SetListenerPosition(1)
	LaunchStones("Stone",0,10)
	CAIDASPIEDRAS2.PlaySound(0)

def DwarfInicio():	
	AuxFuncs.FadeFrom(1.0,6.0)

	Scorer.SetVisible(0)
	char.Position = 54982,-9000,-103329
	char.Angle = 3.14
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, LaunchAnimationStart,())
	AbreCam.CallBack = None
	AbreCam.LastTime = 2.0

def RunAbreCam():
	ScriptSkip.SkipScriptStart("InicioEnano")       # Re-enabled -LeadHead
	#AbreCam.AbreCam()
	#AuxFuncs.FadeTo(10,2)
	#Bladex.AddScheduledFunc(Bladex.GetTime()+10.5, AuxFuncs.FadeTo,(1,10))
	#AbreCam.CallBack = DwarfInicio
	# Bladex.DeactivateInput()
	cam = Bladex.GetEntity("Camera")

	cam.TType    = 0
	cam.SType    = 0
	cam.Position = 54208, 5005,-118229
	cam.TPos     = 55597,-1926,-111155
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, DwarfInicio,())
  	
	
	# LaunchStones("Stone",0,10)
	if not char.InvRight:
		#inv.AddWeapon(weaponini.Name)
		inv.LinkRightHand(weaponini.Name)
	if not char.InvLeft:
		#inv.AddShield(shieldini.Name)
		inv.LinkLeftHand(shieldini.Name)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertdw.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abresub():
	ptatrampa3.OpenDoor()
	ptatrampa4.OpenDoor()

def AbrePuertaLlave1():
	puerta1.OpenDoor()

def CierraPuertaLlave1():
	puerta1.CloseDoor()

def AbrePuertaLlave2():
	puerta2.OpenDoor()

def CierraPuertaLlave2():
	puerta2.CloseDoor()
	
def AbrePuertaLlave4():
	puerta4.OpenDoor()

def CierraPuertaLlave4():
	puerta4.CloseDoor()

def AbrePuertar1():
	global ladoABIERTO
	if (ladoABIERTO==0) :
		puertar1.OpenDoor()
		ladoABIERTO=1


def CierraPuertar1():
	puertar1.CloseDoor()

def EntroEnTriggerSector(trsector_name, entity_name):
	#print("entidad:"+entity_name+", en sector"+trsector_name);
	if (entity_name<>"Player1") : return
	AbrePuertar1()

def Abrepta():
	ptatrampa1.OpenDoor()
	ptatrampa2.OpenDoor()

def Cierrapta():
	ptatrampa1.CloseDoor()
	ptatrampa2.CloseDoor()

def LineaPolvo():
	polvo=Bladex.CreateEntity("Polvo2", "Entity Particle System D2", -199500,-14200,27800)
	polvo.Velocity=0.0, 0.0, 0.0
	polvo.D = 0,0,5000
	polvo.ParticleType="DustDoor"
	polvo.YGravity=-700.0
	polvo.Friction=0.2
	polvo.PPS=300
	polvo.RandomVelocity=25.0
	polvo.Time2Live = 50
	polvo.DeathTime=Bladex.GetTime()+10.0/60.0

def Abrepuertasag():
	#puertasag1.OpenDoor()
	puertasag2.OpenDoor()

def CierraPuertasag(sectorindex,entityname):
	if entityname=="Player1":
		puertasag1.CloseDoor()
		puertasag2.CloseDoor()
		serr1.OnEnter=""
		serr2.OnEnter=""
		serr3.OnEnter=""

#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertatrampa1.py   **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Abrebarra1():

	desplazamientos=(1000.0, 500.0)
	vectores=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	
	#sonidos asociados a la puerta-objeto barra1din
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	barra1din=Objects.CreateDinamicObject("barra1")
	Objects.NDisplaceObject(barra1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def Abrebarra2():

	desplazamientos=(1000.0, 500.0)
	vectores=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra2din=Objects.CreateDinamicObject("barra2")
	Objects.NDisplaceObject(barra2din, desplazamientos, vectores, vel_iniciales, vel_finales)

def Abrebarra3():

	desplazamientos=(1000.0, 500.0)
	vectores=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra3din=Objects.CreateDinamicObject("barra3")
	Objects.NDisplaceObject(barra3din, desplazamientos, vectores, vel_iniciales, vel_finales)	

def Abrebarra4():

	desplazamientos=(1000.0, 500.0)
	vectores=((-1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra4din=Objects.CreateDinamicObject("barra4")
	Objects.NDisplaceObject(barra4din, desplazamientos, vectores, vel_iniciales, vel_finales)	

#####LOS OTROS

def Abrebarra5():

	desplazamientos=(1000.0, 500.0)
	vectores=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra5din=Objects.CreateDinamicObject("barra5")
	Objects.NDisplaceObject(barra5din, desplazamientos, vectores, vel_iniciales, vel_finales)	

def Abrebarra6():

	desplazamientos=(1000.0, 500.0)
	vectores=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra6din=Objects.CreateDinamicObject("barra6")
	Objects.NDisplaceObject(barra6din, desplazamientos, vectores, vel_iniciales, vel_finales)	

def Abrebarra7():

	desplazamientos=(1000.0, 500.0)
	vectores=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra7din=Objects.CreateDinamicObject("barra7")
	Objects.NDisplaceObject(barra7din, desplazamientos, vectores, vel_iniciales, vel_finales)	

def Abrebarra8():

	desplazamientos=(1000.0, 500.0)
	vectores=((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
	vel_iniciales=(0.0, 800)
	vel_finales=(800.0, 800)
	barra8din=Objects.CreateDinamicObject("barra8")
	Objects.NDisplaceObject(barra8din, desplazamientos, vectores, vel_iniciales, vel_finales)	

def Abrebarras():

	AbreCam.PTS = [((-150451.916552, -34.1271768169, -77426.8546025), (-151545.300698, -1439.66880706, -73713.185198)), ((-158817.594279, -2405.71104201, -75625.6615823), (-156863.557235, -1292.22329209, -71727.1918172))]
	AbreCam.AbreCam()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, AbrebarrasDeVerdad,())
	Bladex.ExeMusicEvent( Bladex.GetMusicEvent("coro6") )

def AbrebarrasDeVerdad():
	Abrebarra1()
	Abrebarra2()
	Abrebarra3()
	Abrebarra4()
	Abrebarra5()
	Abrebarra6()
	Abrebarra7()
	Abrebarra8()


#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	#char.Position= 78000,3000,-136000		# inicio
	char.Position=135504.33916, 8183.84014719, -57753.7976858		# inicio
	Doors.Restore()

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=29095.2361148, -1317.00351257, -41439.3640184		# sala octogonal
	Doors.Restore()

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-122088.738337, -8623.72263468, -76216.9346096		# ANTES DE LA SALA ROTA
	Doors.Restore()

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=-2056.42071202, -1567.23848306, -42127.2074218	# tras  la puerta de la sala octogonal
	Doors.Restore()

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=-191933.923815, -15317.6571648, 29323.9933468	# En la sala grande del final
	Doors.Restore()

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-61949.0292552, -9816.8118373, 9889.00972458		# en la sala rota
	Doors.Restore()

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=-244585.77, -26888.781, 75845.608			# Dentro de la biblioteca
	Doors.Restore()

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=-65069.8682812, -9884.28889129, -57604.507365	# antes del troll de la llave
	Doors.Restore()

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=-248125.45069, -19774.6701948, -8738.11164048		# Dentro del palacio final
	Doors.Restore()

def x1x():
	char.Position = (-66830.2757974, -10116.7641256, -61362.4738624)
		
	


#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para temblores.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def temblOff():
	cam = Bladex.GetEntity("Camera")
	cam.EarthQuakeFactor = 0
	cam.EarthQuake = 0

def temblOn():
	global Tiembla_
	
	if Tiembla_:
		cam = Bladex.GetEntity("Camera")
		cam.EarthQuakeFactor = 100
		cam.EarthQuake = 1
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, temblOff,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+whrandom.randint(40,80), temblOn,())
		char= Bladex.GetEntity("Player1")
		Temblon_s.Position = char.Position
		Temblon_s.PlaySound(1)
	

def Telmbluno_Off(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 0

# primer Temblor delante de la grieta con polvo
def Telmbluno_Com(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 1
		SActivaTembluno.OnEnter = ""
		dust.RemueveTierraGen(-32904, -6500, -21004,2500,2000)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, dust.DropDust,(-33076,-15002,-16374,100,-1000,-1000))
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, dust.DropDust,(-34834,-15555,-23438,100,-1000, 1000))
		char= Bladex.GetEntity("Player1")
		Piedruna.Position = char.Position
		Piedruna.PlaySound(1)
		temblOn()

# Segundo Temblor ENTRADA A LA CIUDAD
def XTelmbluno_Com(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 1
		XSActivaTembluno.OnEnter = ""
		XSActivaTemblunoA.OnEnter = ""
		"""
		dust.RemueveTierraGen(-84982, 3200, -72900,1500,1500)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1, dust.DropDust,(-91034,-1699,-68192,100,-1000, -7000))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2, dust.DropDust,(-79242,-6091,-74166,100,-1000,-1000))
		"""
		char= Bladex.GetEntity("Player1")
		Piedruna.Position = char.Position
		Piedruna.PlaySound(1)
		temblOn()

def XTelmbluno_Off(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 0


# Tercer Temblor TRAS LA SALA OCTOGONAL
def YTelmbluno_Com(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 1
		YSActivaTembluno.OnEnter = ""		
		"""
		dust.RemueveTierraGen(-84982, 3200, -72900,1500,1500)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1, dust.DropDust,(-91034,-1699,-68192,100,-1000, -7000))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2, dust.DropDust,(-79242,-6091,-74166,100,-1000,-1000))
		"""
		char= Bladex.GetEntity("Player1")
		Piedruna.Position = char.Position
		Piedruna.PlaySound(1)
		temblOn()

def YTelmbluno_Off(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 0

# CUARTO Temblor TRAS EL TROLL TONTO
def ZTelmbluno_Com(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 1
		ZSActivaTembluno.OnEnter = ""		
		"""
		dust.RemueveTierraGen(-84982, 3200, -72900,1500,1500)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1, dust.DropDust,(-91034,-1699,-68192,100,-1000, -7000))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2, dust.DropDust,(-79242,-6091,-74166,100,-1000,-1000))
		"""
		char= Bladex.GetEntity("Player1")
		Piedruna.Position = char.Position
		Piedruna.PlaySound(1)
		temblOn()

def ZTelmbluno_Off(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 0

# quinto Temblor EN PARTE BAJA GRUTAS
def ATelmbluno_Com(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 1
		ASActivaTembluno.OnEnter = ""		
		"""
		dust.RemueveTierraGen(-84982, 3200, -72900,1500,1500)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1, dust.DropDust,(-91034,-1699,-68192,100,-1000, -7000))
		Bladex.AddScheduledFunc(Bladex.GetTime()+2, dust.DropDust,(-79242,-6091,-74166,100,-1000,-1000))
		"""
		char= Bladex.GetEntity("Player1")
		Piedruna.Position = char.Position
		Piedruna.PlaySound(1)
		temblOn()

def ATelmbluno_Off(sectorindex,entityname):
	global Tiembla_
	
	if entityname == "Player1":
		Tiembla_ = 0


####APAGADO DE ANTORCHAS EN POCIONES.PY

############################################
def Apagala(sectorindex,entityname): 
	a = Bladex.GetEntity(entityname)	
	if a.Kind == "Antorcha":
		Torchs.ExtingueAntorcha(entityname)
		print"ExtingueAntorcha"