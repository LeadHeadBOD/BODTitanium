#########################################################
#														#
# FORTALEZA DE LOS ORCOS								#
#														#
# escena del jefe orco dando ordenes					#
#														#
# (Yuio)												#
#														#
#########################################################

## Revised by LeadHead for Titanium
## There are unnecessary calls here
## AniSound does not need to be called, all the sounds are already assigned when the entity is being created.


import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import B3DLib
import darfuncs
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 7
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

################################################# PARTICULAS ###########################################
Bladex.AddParticleGType("obarenadust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=200
	g=170
	b=140
	a=150.0*(1.0-traux)**0.5
	size=4.0+aux*300.0
	Bladex.SetParticleGVal("obarenadust",i,r,g,b,a,size)


################################# TABLAS ############################################
tabA=Bladex.GetSector(25250, 18000, 40750)
tabA.Active=0
tabA.InitBreak( (0.0, 0.0, 40.0), (0.0, 2000.0, 0.0), (1150.0, 0.0, 1400.0) ,'madera pesada')

tabB=Bladex.GetSector(27500, 18000, 40750)
tabB.Active=0
tabB.InitBreak( (0.0, 0.0, 30.0), (0.0, 2000.0, 0.0), (1150.0, 0.0, 400.0) ,'madera pesada')


################################################# MINOTAUR ##############################################


################################################# ENEMIES ##############################################

Orcomandon= darfuncs.E_Grup()
Orcomandon.OnDeath = ambiente3

Espadaromana=Bladex.CreateEntity("MuereOrcEspadaromana007","Garrote2",0,0,0,"Weapon")
Breakings.SetBreakableWS("MuereOrcEspadaromana007")
escudo=Bladex.CreateEntity("MuereOrcEscudo007","Escudo9",0,0,0)
Sparks.MakeShield("MuereOrcEscudo007")
Breakings.SetBreakableWS("MuereOrcEscudo007")


o=Bladex.CreateEntity("JJorc1Potion","Pocima50",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("JJorc1Potion")


gorkboss=Bladex.CreateEntity("JJorc1","Great_Ork", 13000,11000,39750)
gorkboss.SetOnFloor()
gorkboss.Person=1
gorkboss.Angle=1.5
gorkboss.Level=lvl_control.GiveLevel(8,12)
Actions.TakeObject(gorkboss.Name,"MuereOrcEspadaromana007")
Actions.TakeObject(gorkboss.Name,"MuereOrcEscudo007")
Actions.TakeObject("JJorc1","llave333")
Actions.TakeObject("JJorc1","JJorc1Potion")
#gorkboss.ActionAreaMin=pow(2,0)
#gorkboss.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(gorkboss)
gorkboss.Data.JoinGroup("JJorc1", "foso")
#AniSound.AsignarSonidosOrco(gorkboss.Name) ### YUIO, WE DONT NEED THIS, WHY ARE YOU ADDING THIS??? -LeadHead
gorkboss.Blind = 1
gorkboss.Deaf = 1

Orcomandon.AddGuy(gorkboss.Name)
Orcomandon.OnDeath = ambiente3

Espadaromana=Bladex.CreateEntity("MuereOrcEspadaromana1X","HookSword",0,0,0,"Weapon")
Breakings.SetBreakableWS("MuereOrcEspadaromana1X")
escudo=Bladex.CreateEntity("MuereOrcEscudo1X","Escudo1",0,0,0)
Sparks.MakeShield("MuereOrcEscudo1X")
Breakings.SetBreakableWS("MuereOrcEscudo1X")
gorkinA=Bladex.CreateEntity("OEorc1","Ork",26500,18000,44500)
gorkinA.Person=1
gorkinA.Angle=1.5
gorkinA.Level=lvl_control.GiveLevel(11,14)
Actions.TakeObject(gorkinA.Name,"MuereOrcEspadaromana1X")
Actions.TakeObject(gorkinA.Name,"MuereOrcEscudo1X")
#gorkinA.ActionAreaMin=pow(2,0)
#gorkinA.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(gorkinA)
gorkinA.Data.JoinGroup("OEorc1", "ENTRENA")
#AniSound.AsignarSonidosOrco(gorkinA.Name) ### YUIO, WE DONT NEED THIS, WHY ARE YOU ADDING THIS??? -LeadHead
gorkinA.Blind = 1
gorkinA.Deaf = 1

Espadaromana=Bladex.CreateEntity("MuereOrcEspadaromana2","Orksword",0,0,0,"Weapon")
Breakings.SetBreakableWS("MuereOrcEspadaromana2")
escudo=Bladex.CreateEntity("MuereOrcEscudo2","Escudo1",0,0,0)
Sparks.MakeShield("MuereOrcEscudo2")
Breakings.SetBreakableWS("MuereOrcEscudo2")
gorkinB=Bladex.CreateEntity("OEorc2","Ork",4000,18000,43250)
gorkinB.Person=1
gorkinB.Angle=3
gorkinB.Level=lvl_control.GiveLevel(10,13)
Actions.TakeObject(gorkinB.Name,"MuereOrcEspadaromana2")
Actions.TakeObject(gorkinB.Name,"MuereOrcEscudo2")
#gorkinB.ActionAreaMin=pow(2,0)
#gorkinB.ActionAreaMax=pow(2,0)
EnemyTypes.EnemyDefaultFuncs(gorkinB)
gorkinB.Data.JoinGroup("OEorc2", "ENTRENA")
#AniSound.AsignarSonidosOrco(gorkinB.Name) ### YUIO, WE DONT NEED THIS, WHY ARE YOU ADDING THIS??? -LeadHead
gorkinB.Blind = 1
gorkinB.Deaf = 1


######################################################  SEQUENCE #############################################

obSceneTimerRunning=0
obScenePlayed = 0

obScenePartPlayed=0

Bladex.CreateTimer("orcCheckTimer",0.8 )



#sec = Bladex.GetSector(7750 , 18000 , 37000)
#sec.OnEnter= obSceneOrcBossWakeUp

sec = Bladex.GetSector(-5750,18000,58000)
sec.OnEnter= obSceneStartXX

sec = Bladex.GetSector(9857.22907158, 19135.2, 53752.2533552)
sec.OnEnter= obScenePlazaIn
sec.OnLeave= obScenePlazaOut

#char.Position=23232.4159367, 18835.2, 49660.9009099



###############
######### TROLL en vez de MINORX.
########################
"""
o=Bladex.CreateEntity("OrcMinorxPotion","PowerPotion",0,0,0)
o.Static=0
o.Solid=1
o.Scale=1.220190
pocimac.CreatePotion("OrcMinorxPotion")
"""
garrote=Bladex.CreateEntity("MinGarropin1","Hachacarnicero",0,0,0,"Weapon")

Minorx=Bladex.CreateEntity("Minorx","Minotaur",6994.4, 19000.6, 38600,"Person")
Minorx.Angle = 0.7
Minorx.Level=lvl_control.GiveLevel(3,7)
Actions.TakeObject(Minorx.Name,"MinGarropin1")
#Actions.TakeObject(Minorx.Name,"OrcMinorxPotion")
#Minorx.ActionAreaMin=pow(2,8)
#Minorx.ActionAreaMax=pow(2,9)
Minorx.Deaf = 1
Minorx.Blind = 1
Minorx.Position = 25900,18000,37700
#AniSound.AsignarSonidosMinotaur("Minorx") ### YUIO, WE DONT NEED THIS, WHY ARE YOU ADDING THIS??? -LeadHead

_GritoOrco1=Bladex.CreateSound("../../Sounds/esfuerzo-gorco1.wav","GritoOrco1")
_GritoOrco1.MinDistance=100000.0
_GritoOrco1.MaxDistance=1000000.0

_GritoOrco2=Bladex.CreateSound("../../Sounds/esfuerzo-gorco2.wav","GritoOrco2")
_GritoOrco2.MinDistance=100000.0
_GritoOrco2.MaxDistance=1000000.0

_GritoOrco3=Bladex.CreateSound("../../Sounds/esfuerzo-gorco3.wav","GritoOrco3")
_GritoOrco3.MinDistance=100000.0
_GritoOrco3.MaxDistance=1000000.0

_GritoOrco4=Bladex.CreateSound("../../Sounds/esfuerzo-gorco4.wav","GritoOrco4")
_GritoOrco4.MinDistance=100000.0
_GritoOrco4.MaxDistance=1000000.0

_GritoOrco5=Bladex.CreateSound("../../Sounds/esfuerzo-gorco5.wav","GritoOrco5")
_GritoOrco5.MinDistance=100000.0
_GritoOrco5.MaxDistance=1000000.0

_GritoOrco6=Bladex.CreateSound("../../Sounds/esfuerzo-gorco6.wav","GritoOrco6")
_GritoOrco6.MinDistance=100000.0
_GritoOrco6.MaxDistance=1000000.0

_GritoOrco7=Bladex.CreateSound("../../Sounds/esfuerzo-gorco7.wav","GritoOrco7")
_GritoOrco7.MinDistance=100000.0
_GritoOrco7.MaxDistance=1000000.0

_GritoOrcoResp=Bladex.CreateSound("../../Sounds/respiracion-gorco1.wav","GritoOrcoResp")
_GritoOrcoResp.MinDistance=100000.0
_GritoOrcoResp.MaxDistance=1000000.0

roturamadera=Bladex.CreateSound("../../Sounds/rotura-madera.wav","RoturaMadera")
roturamadera.MinDistance=100000.0
roturamadera.MaxDistance=1000000.0

rugido=Bladex.CreateSound("../../Sounds/ATAQUE-MINO3.wav","Rugido")
rugido.MinDistance=100000.0
rugido.MaxDistance=1000000.0
