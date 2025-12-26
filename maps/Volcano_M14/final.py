##///
##||| VOLCANO_M14/Final.PY TITANIUM
##||| Change list:
##||| * Updated sound events.
##\\\ 

#########################################################
#														#
# VOLCANO												#
#														#
# demonios del final (golem)							#
#														#
# (Yuio)												#
#														#
#########################################################

import EnemyTypes
import Bezier
import ReadGSFile
import Doors
import Scorer
import dust
import AniSound
import EnemyTypes
import Sounds
kindGolem = "Golem_lava"


puertapiedrai= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Puertapiedrai")
puertapiedrai.MaxDistance=50000
puertapiedrai.MinDistance=15000
puertapiedrai.Volume=1.0

finpuertapiedrai= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finpuertapiedrai")
finpuertapiedrai.MaxDistance=50000
finpuertapiedrai.MinDistance=15000
finpuertapiedrai.Volume=1.0


puertapiedrad= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "Puertapiedrad")
puertapiedrad.MaxDistance=50000
puertapiedrad.MinDistance=15000
puertapiedrad.Volume=1.0

finpuertapiedrad= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "Finpuertapiedrad")
finpuertapiedrad.MaxDistance=50000
finpuertapiedrad.MinDistance=15000
finpuertapiedrad.Volume=1.0


SoundQuake=Sounds.CreateEntitySound('../../Sounds/derrumbe.wav', 'SoundQuake')
SoundQuake.Volume=1.0				# was 0.8
SoundQuake.MinDistance=1000000
SoundQuake.MaxDistance=5000000

SoundClank=Sounds.CreateEntitySound('../../Sounds/Stone-floor-collapse.wav', 'SoundClank')		# was fiuu3.wav
SoundClank.Volume=0.8
SoundClank.MinDistance=1000000
SoundClank.MaxDistance=5000000

SoundBrum=Sounds.CreateEntitySound('../../Sounds/caida-plataforma.wav', 'SoundBrum')
SoundBrum.Volume=0.8
SoundBrum.MinDistance=1000000
SoundBrum.MaxDistance=5000000

SoundRokus=Sounds.CreateEntitySound('../../Sounds/M-LLAMARADAMEDIANA.wav', 'SoundRokus')
SoundRokus.Volume=0.8
SoundRokus.MinDistance=1000000
SoundRokus.MaxDistance=5000000


SoundCrash=Sounds.CreateEntitySound('../../Sounds/caida-roca1.wav', 'SoundCrash')
SoundCrash.Volume=0.8
SoundCrash.MinDistance=1000000
SoundCrash.MaxDistance=5000000


res=ReadGSFile.ReadGhostSectorFile("final.sf") # modificar nombre
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char=Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs=1

res2=ReadGSFile.ReadGhostSectorFile("muere.sf") # modificar nombre
for igs in res2:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])


# char.Position = 5375.16593387, -2534.6, -159150.148907

###########################################################################################################################
####
###########################################                           #################################################
###############################################	      L A V A             #################################################
###############################################                           #################################################
###########################################################################################################################

#lava=Bladex.CreateEntity("mar","Entity Water",5000,13320,-140000)
#lava.Reflection=0
#lava.Color=110,0,0


###########################################################################################################################
###############################################                           #################################################
###############################################	      L U C E S           #################################################
###############################################                           #################################################
###########################################################################################################################
"""
LUZSG1=Bladex.CreateEntity("LUZSG1","Entity Spot",-5600,9000,-135800)
LUZSG2=Bladex.CreateEntity("LUZSG2","Entity Spot",17900,-1800,-154800)
LUZSG3=Bladex.CreateEntity("LUZSG3","Entity Spot",16400,9000,-126600)
LUZSG1.Color=255,50,0 ; LUZSG1.Intensity=99.0 ; LUZSG1.CastShadows=0 ; LUZSG1.Precission=0.03 ; LUZSG1.Visible=0 ; #LUZSG1.Flick=0
LUZSG2.Color=255,109,0 ; LUZSG2.Intensity=99.0 ; LUZSG2.CastShadows=0 ; LUZSG2.Precission=0.03 ; LUZSG2.Visible=0 ; #LUZSG2.Flick=0 ;
LUZSG3.Color=255,79,0 ; LUZSG3.Intensity=29.0 ; LUZSG3.CastShadows=0 ; LUZSG3.Precission=0.03 ; LUZSG3.Visible=0 ; #LUZSG3.Flick=0
"""


###########################################################################################################################
###############################################                           #################################################
###############################################	    G A R G O L A S       #################################################
###############################################                           #################################################
###########################################################################################################################


o=Bladex.CreateEntity("NoName3","Gargola",-9750,-12000,-140750)
o.Static=1 ; o.Scale=6.055760 ; o.Orientation=0.687569,0.687569,-0.7,0.7

o=Bladex.CreateEntity("NoName4","Gargola",21000,-12000,-140750)
o.Static=1 ; o.Scale=6.055760 ; o.Orientation=0.687569,0.687569,0.7,-0.7


###########################################################################################################################
###############################################                           #################################################
###############################################	 SECTORES QUE SE ROMPEN   #################################################
###############################################                           #################################################
###########################################################################################################################
"""

ftSectorA=Bladex.GetSector(-4000, 500,-121250) ; ftSectorA.Active=1
ftSectorB=Bladex.GetSector( 2250, 500,-126500) ; ftSectorB.Active=0
ftSectorC=Bladex.GetSector(-6000, 500,-136250) ; ftSectorC.Active=1
ftSectorD=Bladex.GetSector(-5500, 500,-156750) ; ftSectorD.Active=1
ftSectorE=Bladex.GetSector(17750, 500,-129750) ; ftSectorE.Active=1
ftSectorF=Bladex.GetSector(19250, 500,-143500) ; ftSectorF.Active=1
ftSectorG=Bladex.GetSector(18500, 500,-157250) ; ftSectorG.Active=1

ftSectorA.InitBreak((20,300,70),(4321,530,360),(432,143,3321),'piedra pesada')
ftSectorB.InitBreak((20,300,70),(3214,530,432),(321,433,4432),'piedra pesada')
ftSectorC.InitBreak((20,300,70),(3240,530,653),(555,143,4321),'piedra pesada')
ftSectorD.InitBreak((20,300,70),(4320,530,243),(532,143,3214),'piedra pesada')
ftSectorE.InitBreak((20,300,70),(1432,530,450),(643,143,4321),'piedra pesada')
ftSectorF.InitBreak((20,300,70),(4240,530,533),(545,143,4321),'piedra pesada')
ftSectorG.InitBreak((20,300,70),(1230,321,321),(325,143,2143),'piedra pesada')

def ftDust(name,p1,p2,p3):
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

def ftSectorABreak():
	ftSectorA.DoBreak((0,2,0),(-4000, 500,-121250),(134,100,34))
	#a=
	#b=
	#c=
	#d=
	#ftDust("ftdustA1",a,b,c)
	#ftDust("ftdustA2",c,b,d)

def ftSectorBBreak():
	ftSectorB.DoBreak((0,2,0),( 2250, 500,-126500),(32,100,12))

def ftSectorCBreak():
	ftSectorC.DoBreak((0,2,0),(-6000, 500,-136250),(324,100,34))

def ftSectorDBreak():
	ftSectorD.DoBreak((0,2,0),(-5500, 500,-156750),(0,100,-314))

def ftSectorEBreak():
	ftSectorE.DoBreak((0,2,0),(17750, 500,-129750),(213,100,-231))

def ftSectorFBreak():
	ftSectorF.DoBreak((0,2,0),(19250, 500,-143500),(212,00,45))

def ftSectorGBreak():
	ftSectorG.DoBreak((0,2,0),(18500, 500,-157250),(545,100,43))

def ftSectorsBreak():
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.5, ftSectorABreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.6, ftSectorBBreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.2, ftSectorCBreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+1.1, ftSectorDBreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.7, ftSectorEBreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.3, ftSectorFBreak, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+1.2, ftSectorGBreak, () )


"""

###########################################################################################################################
###########################################                                    ############################################
###########################################	 P U E R T A S D E E N T R A D A   ############################################
###########################################                                    ############################################
###########################################################################################################################




ftDoorA = Doors.CreateDoor("ftDoorA", (3920,-6000,-111500), ( 1, 0, 0), 0, 4250, Doors.CLOSED)
ftDoorB = Doors.CreateDoor("ftDoorB", (7290,-6000,-111500), (-1, 0, 0), 0, 4250, Doors.CLOSED)


eSecEntered =0

eSec = Bladex.GetSector(5052.55259457, -1484.28764986, -121947.0046)
eSec.OnEnter = eSecOnEnter





###########################################################################################################################
###########################################                                    ############################################
###########################################	 S E C T O R   D E   P I E D R A   ############################################
###########################################                                    ############################################
###########################################################################################################################
#stone =Bladex.CreateEntity("lavaStone","SectorVolcan",6411.0, 1974.0, -142172.0)
stone =Bladex.CreateEntity("lavaStone","SectorVolcan",6421.5, 2000.0, -142174.0)
stone.RotateRel(0,0,0,1,0,0,1.57)
stone.Static=1
stone.Scale=1
stone.ExclusionGroup = 1

stoneFalse =Bladex.CreateEntity("lavaStone","SectorVolcan",6421.5, 2000.0, -142174.0)
stoneFalse.RotateRel(0,0,0,1,0,0,1.57)
stoneFalse.Static=1
stoneFalse.Scale=1
stoneFalse.Alpha = 0.0

###########################################################################################################################
###########################################                                    ############################################
###########################################	            G O L E M              ############################################
###########################################                                    ############################################
###########################################################################################################################

fDestierro = 0.0, 0.0, 0.0

geodaTocha = Bladex.CreateEntity("fGeoda","Geoda", fDestierro[0], fDestierro[1], fDestierro[2])
geodaTocha.RotateRel(0,0,0,1,0,0,1.57); geodaTocha.Static=1; geodaTocha.RemoveFromWorld()
Bladex.AddCombustionDataFor( "Geoda" , "LargeFire", 500, 900, 4, 0.5, 10, 25)

LlaveNegra = Bladex.CreateEntity("SPIDER","LlaveNegra", fDestierro[0], fDestierro[1], fDestierro[2])

finalGolem = Bladex.CreateEntity("fGolem",kindGolem, 5255.22387399, -2612.87656427, -159107.311855)
finalGolem.Person = 1
finalGolem.Level=lvl_control.GiveLevel(5,10)
finalGolem.Deaf = 1
finalGolem.Blind = 1

luz             = Bladex.CreateEntity(finalGolem.Name+"Luz","Entity Spot",0,0,0)
luz.Color       = 200,100,0
luz.Intensity   = 7
luz.Precission  = 0.303456
luz.CastShadows = 0
luz.Visible     = 1
luz.SizeFactor  = 0
finalGolem.Link(luz)

#AniSound.AsignarSonidosGolem(finalGolem.Name)
EnemyTypes.EnemyDefaultFuncs(finalGolem)
finalGolem.SetOnFloor()
finalGolem.Freeze()
finalGolem.RemoveFromWorld()
finalGolem.ImDeadFunc = HellSpawDeath
finalGolem.SelfIlum = 1

Actions.TakeObject(finalGolem.Name, LlaveNegra.Name)

Bladex.AddCombustionDataFor( kindGolem , "LargeFire", 500, 900, 4, 0.5, 10, 144000)

geodaTrozoA = Bladex.CreateEntity("fGeodaPieza1","GeodaPieza1", fDestierro[0], fDestierro[1], fDestierro[2],"Physic")
geodaTrozoB = Bladex.CreateEntity("fGeodaPieza2","GeodaPieza2", fDestierro[0], fDestierro[1], fDestierro[2],"Physic")
geodaTrozoC = Bladex.CreateEntity("fGeodaPieza3","GeodaPieza3", fDestierro[0], fDestierro[1], fDestierro[2],"Physic")
geodaTrozoD = Bladex.CreateEntity("fGeodaPieza4","GeodaPieza4", fDestierro[0], fDestierro[1], fDestierro[2],"Physic")
geodaTrozoE = Bladex.CreateEntity("fGeodaPieza5","GeodaPieza5", fDestierro[0], fDestierro[1], fDestierro[2],"Physic")

geodaTrozoA.RotateRel(0,0,0,1,0,0,1.57) ;  geodaTrozoA.Solid=0 ; geodaTrozoA.RemoveFromWorld()
geodaTrozoB.RotateRel(0,0,0,1,0,0,1.57) ;  geodaTrozoB.Solid=0 ; geodaTrozoB.RemoveFromWorld()
geodaTrozoC.RotateRel(0,0,0,1,0,0,1.57) ;  geodaTrozoC.Solid=0 ; geodaTrozoC.RemoveFromWorld()
geodaTrozoD.RotateRel(0,0,0,1,0,0,1.57) ;  geodaTrozoD.Solid=0 ; geodaTrozoD.RemoveFromWorld()
geodaTrozoE.RotateRel(0,0,0,1,0,0,1.57) ;  geodaTrozoE.Solid=0 ; geodaTrozoE.RemoveFromWorld()

Bladex.AddCombustionDataFor( "GeodaPieza1" , "LargeFire", 500, 900, 4, 0.5, 10, 25)
Bladex.AddCombustionDataFor( "GeodaPieza2" , "LargeFire", 500, 900, 4, 0.5, 10, 25)
Bladex.AddCombustionDataFor( "GeodaPieza3" , "LargeFire", 500, 900, 4, 0.5, 10, 25)
Bladex.AddCombustionDataFor( "GeodaPieza4" , "LargeFire", 500, 900, 4, 0.5, 10, 25)
Bladex.AddCombustionDataFor( "GeodaPieza5" , "LargeFire", 500, 900, 4, 0.5, 10, 25)


Bladex.SetTriggerSectorFunc("SectorFantasma0", "OnEnter", eSceneStart )
Bladex.AddScheduledFunc(Bladex.GetTime(),MakeLavita,())
