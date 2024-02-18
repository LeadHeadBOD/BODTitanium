##///
##||| ORC_M9/DefFuncs.PY TITANIUM
##||| Change list:
##||| * DukeFix applied
##||| * Scorer at the end is hidden only if the player is actually on the elevator
##||| * Dungeon lock can no longer be used indefinitely until you run it outside the level boundaries and cause floating point errors
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 

import GotoMapVars
import AbreCam
import ScriptSkip
import MusicTool
import darfuncs
import Reference
import Enm_Def
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para puertorc.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************
def AbrerastRASTORRE2():

	desplazamientos=(1550.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(RASTORRE2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def AbrerastRASTORRE1():

	desplazamientos=(1550.0, 1500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(RASTORRE1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


def CierrarastRASTORRE2():

	desplazamientos=(1550.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(RASTORRE2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def CierrarastRASTORRE1():

	desplazamientos=(1550.0, 1500.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto rast6
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(RASTORRE1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)


##### Abrir el rastrillo al accionar una palanca
def AbreLosDosRatrillosTorre():
	AbrerastRASTORRE1()
	AbrerastRASTORRE2()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmosfera18"))


def Abrerastmaz2():

	desplazamientos=(1750.0, 1000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastmaz2
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	
def Cierrarastmaz2():

	desplazamientos=(1000.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastmaz2
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz2din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def Abrerastmaz3():

	desplazamientos=(1000.0, 1750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)

	#sonidos asociados a la puerta-objeto rastmaz3
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	
	
def Cierrarastmaz3():

	desplazamientos=(1000.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

	#sonidos asociados a la puerta-objeto rastmaz3
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)



def AbrePuertaLlave3():

	desplazamientos=(1000.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 3000)
	vel_finales=(3000.0, 500)


	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera1"))




def CierraPuertaLlave3():

	desplazamientos=(1000.0, 2000.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 3000, 6000.0, 0.0, 4000.0, 0.0)
	vel_finales=(3000.0, 6000, 0.0, 4000.0, 0.0, 3000.0)

	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(puerta3din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

darfuncs.EnterSecEvent(25150,50600,19350,CierraPuertaLlave3)


def AbrePuertaLlave333():
	
	desplazamientos=(700.0, 2000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 3000)
	vel_finales=(3000.0, 500)


	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta333din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera21"))
	cerradurp333.OnUnLockFunc= None # Added -LeadHead



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

def AbrePuertaLlave444():
	puerta444.OpenDoor()

def MuereMinorxMalo():
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, AhoraCheckeaSiSeAbrePuertaJEFE,())

def AhoraCheckeaSiSeAbrePuertaJEFE():
	sec = Bladex.GetSector(8523.27448476, 19251.6084798, 55528.2258367)
	if sec.Index == apply(Bladex.GetSector,char.Position).Index:	
		AbrePuertaJEFE(sec.Index,"Player1")
	else:
		sec.OnEnter = AbrePuertaJEFE

def AbrePuertaJEFE(sectorindex,entityname):
	if entityname == "Player1":
		puertaJEFE.OpenDoor()
		gorkboss = Bladex.GetEntity("JJorc1")
		gorkboss.Position = 5009, 20431, 33968
		gorkboss.Angle = 0
		darfuncs.UnhideBadGuy(gorkboss.Name)
		gorkboss.Position = 5009, 20431, 33968
		gorkboss.Angle = 0
		gorkboss.SetOnFloor()
		gorkboss.GoToJogging = 1
		gorkboss.GoTo(7411, 18933, 44752)
		

		sec = Bladex.GetSector(8523.27448476, 19251.6084798, 55528.2258367)
		sec.OnEnter = None

		AbreCam.PTS = [((8304.59047605, 17246.677863, 53124.7841136), (8565.28291392, 18359.8355736, 48773.1067968), 1), ((10225.6479214, 17542.064821, 54607.0907124), (7815.11898535, 18655.1278872, 50975.1250381), 2)]
		AbreCam.LastTime = 1.0
		AbreCam.AbreCam()
		
		
def CierraPuertaELE():

	global enmarcha
	if enmarcha:
		return

	desplazamientos=(500.0, 5900.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	columnaelevador.CloseDoor()
	enmarcha=1


def AbrePuertaELE():

	desplazamientos=(500.0, 5900.0, 500.0)
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
#####################################3	
def AbrePuertaLlaver3():
	puertar3.OpenDoor()
	
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

def AbrePuerta8():
	puerta8.OpenDoor()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combatelight"))
	darfuncs.UnhideBadGuy("orc244")
	darfuncs.UnhideBadGuy("orc255")


def Lalala():

	darfuncs.UnhideBadGuy("orc256")


def ApareceCapullo():
	sectx8=Bladex.GetSector(-4741.55759415, 47898.2427502, 40735.2145228)
	sectx8.OnEnter=x9
	sectx9=Bladex.GetSector(-14655.4227185, 48202.9520959, 40554.4905691)
	sectx9.OnEnter=x9

def x9(sectorindex,entityname):
	if entityname=='Player1':
		Lalala()
		sectx8=Bladex.GetSector(-4741.55759415, 47898.2427502, 40735.2145228)
		sectx8.OnEnter=""
		sectx9=Bladex.GetSector(-14655.4227185, 48202.9520959, 40554.4905691)
		sectx9.OnEnter=""


def AbrePuertaLlave88():
	puerta88.OpenDoor()
	darfuncs.UnhideBadGuy("orc345")
	darfuncs.UnhideBadGuy("orc355")
	
	
	
def Abrepuerta0():

	desplazamientos=(1750.0, 1750.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto puerta0
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(puerta0din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	

def Cierrapuerta0():
	
	desplazamientos=(1750.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto puerta0
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(puerta0din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
	

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para pris.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def MuereElPobreLordKerman (VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	import Blood
	global CanaMaster
    
	en            = Bladex.GetEntity(VictimName)
	wpn           = Bladex.GetEntity(WeaponName)
	Blood.BleedingImpact(en, en.Position[0], en.Position[1], en.Position[2], 0,10000,0,  wpn,   0,0,0,   0,0,0  )
	en.Life       = 0
	en.DamageFunc = None
	CanaMaster    = 0
	#darfuncs.UnhideBadGuy(OrcoCabreado.Name)
	#OrcoCabreado.Position = 18455.0322547, 50387.9289109, 24534.7211011         # This looks like was made as a failsafe in case the Duke somehow died in his cell. That or cut content.
	#OrcoCabreado.Angle = 3.1415*3/2                                             # Dont need any of this anymore since I removed his DamageFunc until the cell is unlocked.
	#OrcoCabreado.SetOnFloor()                                                   # If the Duke still somehow dies, the orc simply never spawns and the key is added to your inventory anyway.
	#OrcoCabreado.GoToJogging = 1                                                # -LeadHead
	#OrcoCabreado.GoTo(26351.1959878, 50388.8367659, 34333.0602338)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate6"))


def PrisioneroX():
	global pris
	
	pris=Bladex.CreateEntity("PPris","Knight_Traitor", 32497.973,50797.926,38294.32,"Person","Duque")
	#pris=Bladex.CreateEntity("PPris","Knight_Traitor", 32861.268, 50855.313-250, 37521.836,"Person","Duque")
	pris.Angle= 3.1415*6.738/180+3.1415/2       ## PLAGUE: Wtf is this angle?
	#EnemyTypes.EnemyDefaultFuncs(pris)         # Not a good idea. Too much extra data ends up being loaded and several Funcs have to override.
	pris.Blind = 0
	pris.Deaf = 0
	pris.SetTmpAnmFlags(1,1,0,0,1,1,0)
	pris.LaunchAnimation("Tkn_prisionero_rlx")
	pris.Life = 1
	pris.SetOnFloor()
	pris.DamageFunc = None




def OrcoDisfrutaMatando(x,y):
	OrcoCabreado.SetActiveEnemy(pris.Name)
	OrcoCabreado.Alpha                              = 1.0
	Bladex.GetEntity(OrcoCabreado.InvLeft).Alpha    = 1.0
	Bladex.GetEntity(OrcoCabreado.InvRight).Alpha   = 1.0	
	OrcoCabreado.LaunchAnmType("g_15")
	OrcoCabreado.Blind = 0
	OrcoCabreado.Deaf = 0
	
def CortaCabezaPrisionero(x,y):
	pris.Life = 0
	pris.SeverLimb(1)
	#pris.DamageFunc = None
	_MuereLordKerman.Play(en.Position[0], en.Position[1], en.Position[2], 0)
	ScriptSkip.SkipScriptEnd()

def SeCongelaALordKerman(x=0,y=0):
	pris.Freeze()



def BajarLaAntorcha():
	Comienza =  47500
	Finale   =  50092
	
	a   = Bladex.GetEntity("antapagada")
	pos =  a.Position[1]
	pos = pos + (Finale-Comienza)/200.0
	a.Position = a.Position[0], pos,a.Position[2]
	
	if pos <= Finale:		
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0/20.0, BajarLaAntorcha,())
		


def EncaraAlTipoConElOrco(x,y):
	char.SetActiveEnemy(OrcoCabreado.Name)
	Bladex.ActivateInput()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate6"))

def pSceneStartR():
	global OrcoCabreado
	char.Position = 27122.309,50427.418,37185.398
	char.Angle = -3.1415/2	
	char.SetOnFloor()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)

	char.LaunchAnmType("prisionero")	

	pris.Position = 32497.973,50797.926,38294.32
	pris.Angle= 3.1415*1.738/180+3.1415/2
	pris.SetTmpAnmFlags(1,1,1,0,5,1,0)
	pris.Wuea=Reference.WUEA_ENDED
	pris.LaunchAnimation("prisionero_camina")
	pris.AnmEndedFunc=SeCongelaALordKerman
	
	pris.SetOnFloor()
	cam = Bladex.GetEntity("Camera")
	OnOff.SetLightSpeed(0.0125)
	OnOff.SetLightInens(80.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, OnOff.TurnOnLight,("antapagada",))
	
	a   = Bladex.GetEntity("antapagada")
	a.Position = a.Position[0], 47500,a.Position[2]
	
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.5, BajarLaAntorcha,())
	darfuncs.LaunchMaxCamera("Orcos_Camera_prision.cam",0,357)
	cam.AddCameraEvent(332,OrcoDisfrutaMatando)
	cam.AddCameraEvent(350,CortaCabezaPrisionero)

	cam.AddCameraEvent(356,EncaraAlTipoConElOrco)
	
	GameText.WriteText("M9T3")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("prisorc"))
	
	inv.LinkLeftHand("None")
	inv.LinkRightHand("None")
	inv.LinkBack("None")
	darfuncs.UnhideBadGuy(OrcoCabreado.Name)
	OrcoCabreado.Blind = 1
	OrcoCabreado.Deaf = 1
	OrcoCabreado.Angle    = 3.44363006166
	OrcoCabreado.Position = 26592.5306627, 50385.5322966, 40787.5494261
	OrcoCabreado.Alpha    = 0.0
	Bladex.GetEntity(OrcoCabreado.InvLeft).Alpha    = 0.0
	Bladex.GetEntity(OrcoCabreado.InvRight).Alpha    = 0.0
	OrcoCabreado.SetOnFloor()
	pass

def pSceneStart():
	global CanaMaster
	#OnOff.TurnOffLight( "antapagada")
	
	if CanaMaster:
		CanaMaster = 0
		AniSound.AsignarSonidosCaballeroTraidor(pris.Name) #There has to be a better way to assign hit-sounds but I can't be bothered anymore. -LeadHead
		pris.DamageFunc = MuereElPobreLordKerman
		#pris.UnFreeze()
		#OrcoCabreado.PutToWorld()
		pris.Position = 32497.973,50797.926,38294.32
		pris.SetOnFloor()
		Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, pSceneStartR,())
		ScriptSkip.SkipScriptStart("mortimer")

def Abrerastmaz1():

	desplazamientos=(1750.0, 1000.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 4000)
	vel_finales=(4000.0, 500)
	
	#sonidos asociados a la puerta-objeto rastmaz1
	son_iniciales=("", "")
	son_durante=(sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano)
	Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

	pSceneStart()
	

	
def Cierrarastmaz1():

	desplazamientos=(1000.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
	vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
	vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
	vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)
	
	#sonidos asociados a la puerta-objeto rastmaz1
	son_iniciales=("", "", "", "", "", "")
	son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
	son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
	Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)

def SeAcabaFin():
	darfuncs.UnhideBadGuy("orcFin1")
	darfuncs.UnhideBadGuy("orcFin2")	

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
	char.Position=-37000, 36000, 9000
	Doors.Restore()
	
def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=10000, 30000, 54000
	Doors.Restore()
	
def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=9250, 12000, 37500	
	Doors.Restore()

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=19451, 36379, 25672
	Doors.Restore()




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para orchuye.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def Orchuyematadle(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.SubscribeToList("Pin")



def OrcHuye(sectorindex,entityname):
	pers=Bladex.GetEntity("3ORCAchalay")
	pers.Angle = 5
	pers.SetOnFloor()
	pers.GoToJogging  = 1
	pers.GoTo(28178, 48922, -4839)
	pers.RouteEndedFunc=Orchuyematadle
 	s1=Bladex.GetSector(-2905.63954523, 48158.708226, -1234.27245392)
	s1.OnEnter=""


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para obscene.py         **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************
def obBreakTabA() :
	tabA.DoBreak((-2.5, 3.0, 100.0), (6000,19000,37000), (0.0, 0.0, 0.0))

def obBreakTabB() :
	tabB.DoBreak((-2.5, 3.0, 100.0), (8500,19000,40750), (0.0, 0.0, 0.0))

def obSceneTrapDustTri(name,a,b,c):
	doorDust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2])
 	doorDust.D1= b[0]-a[0], b[1]-a[1], b[2]-a[2]
 	doorDust.D2= c[0]-a[0], c[1]-a[1], c[2]-a[2]
	doorDust.ParticleType="obarenadust"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=1112
	doorDust.Velocity=0.0, -210.0, 0.0
	doorDust.RandomVelocity=20.0
	doorDust.Time2Live=30
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0

def obBreakTabs() :
	a = 8500,18000,41000
	b = 5750,18000,41000
	c = 8500,19750,41000
	d = 5750,20000,41000
	obBreakTabA()
	obBreakTabB()
	obSceneTrapDustTri("oba1",a,b,c)
	obSceneTrapDustTri("oba2",b,c,d)
	roturamadera.Play(8500,18000,41000)
	rugido.Play(8500,18000,41000)
	#darfuncs.LaunchMaxCamera("Orcos_Camera_puerta_minotauro.cam",0,60)

## PLAGUE: wtf is this?
def obSceneFreeMin() :
	#Min = Bladex.GetEntity("OBMin")
	#JMinA.TurnOff()
	pass

def atakaDes():
	Minorx.Deaf  = 0
	Minorx.Blind = 0
	Minorx.Angle = 0
	Minorx.SetTmpAnmFlags(1,1,1,0,5,1,0)
	Minorx.LaunchAnimation("Min_sp")
	Minorx.Position = 25900,18000,37700
	Minorx.SetOnFloor()
	minogroup = darfuncs.E_Grup()
	minogroup.AddGuy(Minorx.Name)
	minogroup.OnDeath = MuereMinorxMalo
	
def obSceneAnimMin() :
	obSceneOrcBossRetire()
	obBreakTabs()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Combate3"))
	#Min = Bladex.GetEntity("OBMin")
	#JMinA.Actor = 1
	#JMinA.Animation="Min_sp"
	#JMinA.FPS=20.0
	#JMinA.SendSectorMsgs=0
	#JMinA.TurnOn()
	EnemyTypes.EnemyDefaultFuncs(Minorx)
	
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, atakaDes,())
	#Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, obBreakTabs, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, obSceneFreeMin, ())
	print "Se va en 45 segundos..."

def obSceneGetOrksN() :
	nOrcs = 0
	orc = Bladex.GetEntity("OEorc1")
	if (orc) : 
		if (orc.Life>0) :
			nOrcs=nOrcs+1	
	orc = Bladex.GetEntity("OEorc2")
	if (orc) : 
		if (orc.Life>0) :
			nOrcs=nOrcs+1
	return nOrcs



def obSceneOrcBossAnimA() :	
	gorkboss = Bladex.GetEntity("JJorc1")
	if (gorkboss) : 
		gorkboss.Angle = 0.0		
		gorkboss.SetTmpAnmFlags(1,1,1,0,5,1,0)		
		gorkboss.LaunchAnimation("Gok_order_orks")
		gorkboss.Position = 9002, 11844, 49064
		gorkboss.SetOnFloor()
		gorkboss.AnmEndedFunc = obSceneOrcBossRetire
		
		
def obSceneOrcBossAnimB() :	
	gorkboss = Bladex.GetEntity("JJorc1")
	if (gorkboss) : 		
		gorkboss.Angle = 0.0
		gorkboss.SetTmpAnmFlags(1,1,1,0,5,1,0)
		gorkboss.LaunchAnimation("Gok_order_minotaur")
		gorkboss.Position = 9002, 11844, 49064
		gorkboss.SetOnFloor()


def obSceneOrcBossLookArena() :
	gorkboss.Face(0.0)

def obSceneOrcBossRetire(x=0,y=0,z=0) :
	#gorkboss = Bladex.GetEntity("JJorc1")
	print "se veimosen!"
	gorkboss.Position = 5009, 20431, 33968
	gorkboss.Angle = 0
	


def obSceneOrcWakeUp(ent) :
	#print(ent)
	ork = Bladex.GetEntity(ent)
	ork.Blind = 0
	ork.Deaf = 0

def obSceneOrcsAttack() :
	gorkinA.GoToJogging=1
	gorkinA.GoTo(23232.4159367, 18835.2, 49660.9009099)
	gorkinA.RouteEndedFunc = obSceneOrcWakeUp
	gorkinB.GoToJogging=1
	gorkinB.GoTo(7634.23561013, 18835.2, 49019.415306)
	gorkinB.RouteEndedFunc = obSceneOrcWakeUp

###################################################### CAMERAS ###############################################

def obSceneCamRestore(camera,frame) :
	#print(">obSceneCamRestore()")
	cam=Bladex.GetEntity("Camera")
	cam.Cut()
	cam.SetPersonView("Player1")
	Scorer.SetVisible(1)
	obSceneOrcBossLookArena()
	char.SetOnFloor()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def obSceneCamB() :
	#print(">obSceneCamB()")
	cam = Bladex.GetEntity("Camera")
	#cam.SetPersonView("Player1")
	cam.SetMaxCamera("orcos_camera_manda2.cam",0,295)

	cam.AddCameraEvent( 27,  GritoOrco3)
	cam.AddCameraEvent( 37,  GritoOrco5)
	cam.AddCameraEvent( 47,  GritoOrco7)
	cam.AddCameraEvent( 57,  GritoOrco4)
	cam.AddCameraEvent( 76,  GritoOrco6)
	cam.AddCameraEvent(140,  GritoOrco2)
	cam.AddCameraEvent(173,  GritoOrco1)
	cam.AddCameraEvent(206,  GritoOrco2)
	cam.AddCameraEvent(260,  GritoOrcoResp)
	cam.AddCameraEvent(270,  GritoOrcoResp)
	
	cam.AddCameraEvent(-1,obSceneCamRestore)
	obSceneOrcBossAnimB()
	char.Position = (8962.9900587, 19261.0086368, 54325.1853926)
	char.Angle = 3.14159
	AbreCam.PTS = [((26284.2627712, 17251.6562616, 48928.3826454), (26205.5780946, 18364.8409745, 44569.5081603), 1.0), ((24596.7384243, 17265.0949795, 50043.961052), (26439.2958937, 18376.3260069, 46101.334262), 3)]
	AbreCam.LastTime = 1.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+15.0, AbreCam.AbreCam, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+16.0, obSceneAnimMin, ())
	ScriptSkip.SkipScriptStart("orcsObb")
	Scorer.SetVisible(0)
	#Bladex.DeactivateInput()

def GritoOrco1(a,b):
	_GritoOrco1.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco2(a,b):
	_GritoOrco2.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco3(a,b):
	_GritoOrco3.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco4(a,b):
	_GritoOrco4.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco5(a,b):
	_GritoOrco5.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco6(a,b):
	_GritoOrco6.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrco7(a,b):
	_GritoOrco7.Play(8630.652, 12043.932, 49068.852, 0)

def GritoOrcoResp(a,b):
	_GritoOrcoResp.Play(8630.652, 12043.932, 49068.852, 0)

def obSceneCamA(x=0,y=0,z=0,w=0) :
	#print(">obSceneCamA()")
	cam = Bladex.GetEntity("Camera")
	#cam.SetPersonView("Player1")
	cam.SetMaxCamera("orcos_camera_manda1.cam",0,200)
	cam.AddCameraEvent(44,  GritoOrco1)
	cam.AddCameraEvent(73,  GritoOrco5)
	cam.AddCameraEvent(95,  GritoOrco4)
	cam.AddCameraEvent(120, GritoOrco6)
	cam.AddCameraEvent(149, GritoOrco3)
	cam.AddCameraEvent(189, GritoOrcoResp)
	cam.AddCameraEvent(-1,obSceneCamRestore)
	obSceneOrcBossAnimA()	


###################################################### PROTA ###############################################

def obSceneStopTargetA(entity_name, camera_element, node):
	cam=Bladex.GetEntity("Camera")
	cam.CameraClearPath(1)	
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, obSceneCamA, ("x","x"))

def obSceneFaceA(ent) :
	char = Bladex.GetEntity("Player1")
	char.Face(3.96576026987)

	#char.StartLooking(-114670.0, -24000.0, -95000.0)
	cam=Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
	v=tpos[0]-opos[0], tpos[1]-opos[1], tpos[2]-opos[2]
	vnorm=B3DLib.Normalize(v)
	cam.ESource="Player1"
	cam.SType=2
	cam.AddCameraNode(1, 2.0, tpos[0]+vnorm[0]*2000, tpos[1]+vnorm[1]*2000, tpos[2]+vnorm[2]*2000)
	cam.AddCameraNode(1, 2.0, 8630.652, 12043.932-200+1000, 49068.852)
	cam.AddCameraNode(1, 2.0, 8630.652+30, 12043.932-200+1000+30, 49068.852+30)
	cam.TType=1
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=obSceneStopTargetA
	
def obScenePositionA() :
	Scorer.SetVisible(0)
	char = Bladex.GetEntity("Player1")
	"""
	char.GoTo(3154.8985901, 19135.2, 54581.2641379) 
	char.RouteEndedFunc = obSceneFaceA
	"""
	#obSceneFaceA("Player1")
	obSceneCamA()

def obSceneStopTargetB(entity_name, camera_element, node):
	cam=Bladex.GetEntity("Camera")
	cam.CameraClearPath(1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, obSceneCamB, ())

def obSceneFaceB(ent) :
	char = Bladex.GetEntity("Player1")
	char.Face(3.33071127334)

	#char.StartLooking(-114670.0, -24000.0, -95000.0)
	cam=Bladex.GetEntity("Camera")
	opos=cam.Position
	tpos=cam.TPos
	v=tpos[0]-opos[0], tpos[1]-opos[1], tpos[2]-opos[2]
	vnorm=B3DLib.Normalize(v)
	cam.ESource="Player1"
	cam.SType=2
	cam.AddCameraNode(1, 2.0, tpos[0]+vnorm[0]*2000, tpos[1]+vnorm[1]*2000, tpos[2]+vnorm[2]*2000)
	cam.AddCameraNode(1, 2.0, 8630.652, 12043.932-200+1000, 49068.852)
	cam.AddCameraNode(1, 2.0, 8630.652+30, 12043.932-200+1000+30, 49068.852+30)
	cam.TType=1
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=obSceneStopTargetB
	
def obScenePositionB() :
	Scorer.SetVisible(0)
	char = Bladex.GetEntity("Player1")
	"""
	char.GoTo(10712.2595744, 19135.2, 56572.8213365)
	char.RouteEndedFunc = obSceneFaceB
	"""
	#obSceneFaceB("Player1")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, obSceneCamB,())
	#Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, obSceneCamB,())

def obSceneStart(camera,frame):
	global obScenePlayed

	if (obScenePlayed) : return
	obScenePlayed =1
	
	#print(">>obSceneStart()")
	obScenePositionA()
	Bladex.AddScheduledFunc(Bladex.GetTime()+9.0, obSceneOrcsAttack, ())
	#Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, obSceneOrcsAttack, ())


def obSceneOrcChecker(ent, time) :
	global obScenePartPlayed

	#print("Checking orks")
	if (obSceneTimerRunning==0) :
		#print("autoremove")	
		gorkboss.RemoveFromList("orcCheckTimer")
		gorkboss.TimerFunc=""		

	if (obScenePartPlayed) : 
		#print("already played")	
		return 
	else:
		#print("trying to play")	
		orcs=obSceneGetOrksN()	
		#print(orcs)
		if (orcs==0) :
			#print("Minotauro fuera!")
			obScenePositionB()
			obScenePartPlayed = 1
		else:
			pass
			#print("aun hay orcos")	

def obScenePlazaIn(index,ent) :
	global obSceneTimerRunning
	if (ent<>"Player1") : return
	#print("obScenePlazaIn")

	if (obSceneTimerRunning==0) :
		#print("assign timer")
		gorkboss.TimerFunc=obSceneOrcChecker;
		gorkboss.SubscribeToList("orcCheckTimer")
		obSceneTimerRunning=1
	
def obScenePlazaOut(index,ent) :
	global obSceneTimerRunning
	if (ent<>"Player1") : return
	#print("obScenePlazaOut")
	obSceneTimerRunning=0

#  T_DKGT
def obSceneStartX():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,MusicTool.LaunchMusicEvent,("inicio6",))
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Orcos_Camara_orcomira.cam",0,110)
	cam.AddCameraEvent(-1,obSceneStart)
	gorkboss.Angle = 0.0
	gorkboss.SetTmpAnmFlags(1,1,1,0,5,1,0)
	gorkboss.LaunchAnimation("Gok_mira")
	gorkboss.Position = 8630.652, 12043.932, 49068.852
	gorkboss.SetOnFloor()
	char.Position = -1628.556,19282.621,56800.977
	char.Angle = 66.856*3.1415/180+3.1415
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	
	char.LaunchAnmType("anda_hacia_orco")
	Scorer.SetVisible(0)	
	
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, obScenePrecierra, ())
	
def obScenePrecierra():
	CierrarastRASTORRE2()
	CierrarastRASTORRE1()


def obSceneStartXX(index,ent):
	if (ent!="Player1"): return
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, obSceneStartX, ())
	ScriptSkip.SkipScriptStart("orcsOba")
	#Bladex.DeactivateInput()
	sec = Bladex.GetSector(-5750,18000,58000)
	sec.OnEnter = ""

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para iscene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def iSceneTrapDustLine(name,a,b):
	doorDust=Bladex.CreateEntity(name, "Entity Particle System D2", a[0],a[1],a[2])
 	doorDust.D= b[0]-a[0], b[1]-a[1], b[2]-a[2]
	doorDust.ParticleType="itrapdust"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=1024
	doorDust.Velocity=0.0, -750.0, 0.0
	doorDust.RandomVelocity=20.0
	doorDust.Time2Live=30
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0

def iSceneTrapDust():
	a = -17500,49500-30,11000
	b = -21000,49500-30,11000
	c = -21000,49500-30,8000
	d = -17500,49500-30,8000

	iSceneTrapDustLine("itrapdusta",a,b)
	iSceneTrapDustLine("itrapdusta",b,c)
	iSceneTrapDustLine("itrapdusta",c,d)
	
	soundhit.Position = a
	soundhit.PlaySound(0)
	

################################################# ANIMACION ###########################################
def iSceneTrapAnim():
	itrap.Actor=1
	itrap.Animation="Trampilla_orcos"
	# itrap.FPS=20.0                  ## PLAGUE: Why 20fps? Commented out.
	itrap.SendSectorMsgs=0
	itrap.TurnOn()

def iSceneRemoveTorch() :
	torch = Bladex.GetEntity("torcha")
	torch.SubscribeToList("Pin")
	torch.RemoveFromWorld()

def iSceneTrapStop():
	itrap.TurnOff()
	itrap.Actor=0
	AuxFuncs.FadeFrom(0.01,0.2,0,0,0)

def iSceneAnim() :
	Bladex.CreateEntity("torcha","Antorcha",-128110.203, -5178-520, -34928.453,"Physic")

	char = Bladex.GetEntity("Player1")
	inv = char.GetInventory()
	inv.LinkRightHand("torcha")
	if char.Kind[0] == 'K':
		char.Position = -26380.555, 51615.934, 9475.27 #Kgt
	elif char.Kind[0] == 'B':
		char.Position = -26862.555, 51529.273, 9575.003 #Bar
	elif char.Kind[0] == 'A':
		char.Position = -26857.791, 51701.934, 9578.27 #Kgt
	elif char.Kind[0] == 'D':
		char.Position = -26380.555, 51615.934, 9475.27 #Kgt
	char.Angle = 3.14159265
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("start_orks")
	char.SetOnFloor()

def iSceneDropTorch(camera, frame) :
	char = Bladex.GetEntity("Player1")
	coso = Bladex.GetEntity(char.InvRight)
	pos = coso.Position
	inv = char.GetInventory()
	inv.LinkRightHand("None")
	coso.Position = pos
	coso.Impulse(0.0, 0.0, 0.0) 

################################################# CAMARA ##############################################

def iSceneCamRestore(camera,frame) :
	#print(">iSceneCamRestore()")
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	Scorer.SetVisible(1)
	cam.Cut()
	iSceneTrapStop()
	ScriptSkip.SkipScriptEnd()
	iSceneRemoveTorch()

def iSceneCamB(camera,frame) :
	#print(">iSceneCamB()")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("orcos_camera02.cam",350,-1)
	cam.AddCameraEvent(-1,iSceneCamRestore)
	

def iSceneCamA() :
	#print(">iSceneCamA()")
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("orcos_camera01.cam",0,350)
	cam.AddCameraEvent(251,iSceneDropTorch)
	cam.AddCameraEvent(-1,iSceneCamB)

def PlaySound(sound,entity,ciclar = 0):
	ent = Bladex.GetEntity(entity)
	sound.Position = ent.Position
	sound.PlaySound(ciclar)

def iSceneStart():	
	#print(">>iSceneStart()")
	GameText.WriteText("M9T1")
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("inicioorc"))
	iSceneCamA()
	iSceneAnim()
	iSceneTrapAnim()
	ScriptSkip.SkipScriptStart("orcsal")
	
	time = Bladex.GetTime()
	
	PlaySound(soundagua,"Player1",-1)

	Bladex.AddScheduledFunc(time + 10.0, soundagua.StopSound,())
	
	Bladex.AddScheduledFunc(time + 15.0, PlaySound,(soundrechinar[0],"Player1",-1))
	Bladex.AddScheduledFunc(time + 15.0, PlaySound,(soundesfuerzo[0],"Player1"))
	Bladex.AddScheduledFunc(time + 17.0, PlaySound,(soundesfuerzo[1],"Player1"))
	Bladex.AddScheduledFunc(time + 17.0, soundrechinar[0].StopSound,())
	Bladex.AddScheduledFunc(time + 18.0, PlaySound,(soundrechinar[0],"Player1",-1))
	Bladex.AddScheduledFunc(time + 22.0, soundrechinar[0].StopSound,())
	Bladex.AddScheduledFunc(time + 22.0, PlaySound,(soundesfuerzo[2],"Player1"))
	Bladex.AddScheduledFunc(time + 24.5, PlaySound,(soundrechinar[1],"Player1"))
	
	Bladex.AddScheduledFunc(time + 25.0, iSceneTrapDust, ())

def Lanzador():	
	
	AuxFuncs.FadeFrom(4.5, 0.0)	


	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, iSceneStart, ())
	Scorer.SetVisible(0)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para escene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def eSceneCamRestore(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	GotoMapVars.MapText(-1,"ORCMURAL")
	Scorer.SetVisible(1)

def eSceneCam() :
	ScriptSkip.SkipScriptStart("OrcMural1")
	#Bladex.DeactivateInput()
	Scorer.SetVisible(0)
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Orcos_Camera_miraMural.cam",0,-1)
	cam.AddCameraEvent(-1,eSceneCamRestore)


def eSceneAnim() :
	char.Position = -19125, 36625, 21974
	char.Angle = esceneOrientation
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("mural_orcos")

def eSceneStart() :
	print("PLAY >")
	eSceneCam()
	eSceneAnim()

def eSceneFace(ent):
	o = Bladex.GetEntity("Player1")
	o.Face(esceneOrientation)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, eSceneStart, ())


def MusicayTexto():
	
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("finalorc"))
	GameText.WriteText("M9T2")
	eSceneCam()
	eScenePlayed=1

def useInGhostMural(gpointer,usefrom):
	global muralleido
	if (muralleido) : return
	muralleido=1

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,MusicayTexto,())



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para enemigos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def ambiente1():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera7"))


def ambiente2():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera7"))
	MusicTool.Music2Sector("ambiente3",None)
	MusicTool.Music2Sector("ambiente6",None)


def ambiente3():

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(31,))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))


def ambiente4():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera22"))
	MusicTool.Music2Sector("ambiente5",None)


def Ambientefinal():

	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atm2MP3"))


def TerminanLasMuertes():
	sectx2=Bladex.GetSector(-13600.0042598, 36850.585256, 4911.28433641)
	sectx2.OnEnter=x2

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def MueveOrco():
	for enemigo in listabichos:
		GoToMul(enemigo.Name)

def x1(sectorindex,entityname):

	if entityname=='Player1':
		MueveOrco()
		sectx1.OnEnter=""

def Patachof():
	Actions.QuickTurnToFaceEntity("orc5", "Player1")

def KreaOrkos():
	darfuncs.UnhideBadGuy("orc8")
	darfuncs.UnhideBadGuy("orc9")

def x2(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos()
		sectx2=Bladex.GetSector(-13600.0042598, 36850.585256, 4911.28433641)
		sectx2.OnEnter=""

def TerminanLasMuertes2():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("atmosfera5"))
	MusicTool.Music2Sector("ambiente4",None)
	sectx3=Bladex.GetSector(-1906.44160664, 25535.1400765, 31419.913098)
	sectx3.OnEnter=x3

def KreaOrkos2():
	darfuncs.UnhideBadGuy("orc14")
	darfuncs.UnhideBadGuy("orc15")

def x3(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos2()
		sectx3=Bladex.GetSector(-1906.44160664, 25535.1400765, 31419.913098)
		sectx3.OnEnter=""



def TerminanLasMuertes3():
	sectx4=Bladex.GetSector(-5991.02001623, 18898.1994426, 57734.1072279)
	sectx4.OnEnter=x4
	sectx4=Bladex.GetSector(25795.6764711, 18890.6650677, 57949.8133918)
	sectx4.OnEnter=x4

def TerminanLasMuertes4():
	sectx5=Bladex.GetSector(11194.0237768, 33128.7408032, 30429.3783516)
	sectx5.OnEnter=x5

def KreaOrkos3():
	darfuncs.UnhideBadGuy("orc16")
	darfuncs.UnhideBadGuy("orc17")

def x4(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos3()
		sectx4=Bladex.GetSector(9733.18751391, 12885.5629657, 39307.0908492)
		sectx4.OnEnter=""
		sectx4=Bladex.GetSector(25795.6764711, 18890.6650677, 57949.8133918)
		sectx4.OnEnter=""

def TerminanLasMuertes5():
	sectx6=Bladex.GetSector(10221.0512325, 39624.5441027, 31720.6817268)
	sectx6.OnEnter=x6

def KreaOrkos4():
	darfuncs.UnhideBadGuy("orc18")
	darfuncs.UnhideBadGuy("orc19")

def x5(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos4()
		sectx5=Bladex.GetSector(11194.0237768, 33128.7408032, 30429.3783516)
		sectx5.OnEnter=""

def KreaOrkos5():
	darfuncs.UnhideBadGuy("orc20")
	darfuncs.UnhideBadGuy("orc21")

def x6(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos5()
		sectx6=Bladex.GetSector(10221.0512325, 39624.5441027, 31720.6817268)
		sectx6.OnEnter=""

def TerminanLasMuertes6():
	sectx7=Bladex.GetSector(26316.6222637, 46131.7015377, 66661.4786887)
	sectx7.OnEnter=x7

def KreaOrkos6():
	darfuncs.UnhideBadGuy("orc24")
	darfuncs.UnhideBadGuy("orc25")



def x7(sectorindex,entityname):
	if entityname=='Player1':
		KreaOrkos6()
		sectx7=Bladex.GetSector(26316.6222637, 46131.7015377, 66661.4786887)
		sectx7.OnEnter=""

def DesapEnenTroll():
	darfuncs.CleanArea(-16579.5773054, 48219.3656388, 37466.944,25000)
	print "Enemigos Borrados 1"

def ActivaSacaMierda():
	darfuncs.EnterSecEvent(496.963312851, 44889.0594819, 18533.7006,DesapEnenTroll)
	darfuncs.EnterSecEvent(202.625654894, 46170.119366, 65838.818427,DesapEnenTroll)



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para .py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def charElevatorIn(tr_sector,entity):
	global charInElevator
	print("charElevatorIn")
	charInElevator=1

def charElevatorOut(tr_sector,entity):
	global charInElevator
	print("charElevatorOut")
	charInElevator=0

def SetScorer():
	#Scorer.SetVisible(1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.0,GotoMapVars.EndOfLevel,())

def elevadorFundido():
	AuxFuncs.FadeTo(3.5, 2.0)
	Scorer.SetVisible(0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0,GotoMapVars.EndOfLevel,())
	Bladex.DeactivateInput()
	


def SubeElevador2():

	desplazamientos=(500.0, 4250.0, 500.0)
	vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
	vel_iniciales=(0.0, 2000.0, 2000.0)
	vel_finales=(2000.0, 2000.0, 0.0)
	son_iniciales=(golpeelevador, "", golpeelevador)
	son_durante=(loopelevador, loopelevador, loopelevador)
	Objects.NDisplaceObject(plataformaelevador2movil, desplazamientos, vectores, vel_iniciales, vel_finales, son_iniciales, son_durante)
	columnaelevador2.CloseDoor()

	if (charInElevator) :		
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, elevadorFundido, ())	
		Scorer.SetVisible(0)    # Moved here -LeadHead

def BajaElevador2():

	global enmarcha
	if enmarcha:
		return
	desplazamientos=(500.0, 4250.0, 500.0)
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
#*******************************   Definiciones para bola.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


def dropStoneA(secIndex,ent):
	global stoneADropped
	if (ent=="Player1" and stoneADropped==0) :
		bolon = Bladex.GetEntity("IJBolon1")
		stone.drop( "IJBolon1", 40000000,-40000,-4000000 )
		stoneADropped=1
		Patachof()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("sorpresa-1"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.2,MusicTool.LaunchMusicEvent,("Atmosfera5",))
		MusicTool.Music2Sector("ambiente2",None)


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
	global puertaReventadaA
	if (puertaReventadaA) : return

	print ("hit")

	char=Bladex.GetEntity("Player1")
	weapon=Bladex.GetEntity(entity_name)
	print weapon.Weapon
	if (not weapon.Weapon)	: return	
	
	bgateA1.DoBreak((2.5, 0.0, 1.0), (px, py, pz), (0.0, 0.0, 0.0))
	bgateA2.DoBreak((2.5, 0.0, -1.0), (px, py, pz), (0.0, 0.0, 0.0))
		
	p0 = -29250, 34000, 22250
	p1 = -29250, 34000, 21125
	p2 = -29250, 36000, 22250
	p3 = -29250, 36000, 21125

	dustTriangle("rppolvo1",p0,p1,p2)
	dustTriangle("rppolvo2",p3,p1,p2)
	derrumbebgate1.Play(-29250, 34000, 22250)
	puertaReventadaA = 1
	


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para PROPIEDADES.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

	
def BorraLuz():
	pass

