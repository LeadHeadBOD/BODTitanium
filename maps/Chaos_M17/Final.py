##///
##||| CHAOS_M17/Final.PY TITANIUM
##||| Change list:
##||| * Increased light radius in the corridor leading to old guy
##||| * Spark pass
##\\\ 


import Bladex
import OnOff
import ReadGSFile
import math
import ItemTypes
import B3DLib
import darfuncs

import NetSounds
import whrandom


###############
# PARTE FINAL #
###############

o=Bladex.CreateEntity("Lucero0","LamparaNegra",667279.222034,310713.171522,181006.346340)
o.Static=1
o.Scale=1.000000
o.Orientation=0.589646,0.589646,0.390278,-0.390278
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n




o=Bladex.CreateEntity("Lucero1","Lamparaegipto",690270.430000,322797.196000,176064.219000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
o.Data = 0
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n



o=Bladex.CreateEntity("Lucero2","Lamparaegipto",735975.900000,332763.469000,161432.534000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
o.Data = 0
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


########################################################
# THE BIG FINALE is Supercalifragilisticexpialidocious #
########################################################


o=Bladex.CreateEntity("Lucero3","Lamparaegipto",812297.009000,334794.295000,156548.813000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707080,0.707080,-0.006171,0.006171
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero3",60.000000,0.400000)
Sparks.SetMetalSparkling(o.Name)        # Add

o=Bladex.CreateEntity("Lucero4","Lamparaegipto",812317.160000,334795.139000,184153.103000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707080,0.707080,-0.006171,0.006171
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero4",60.000000,0.400000)
Sparks.SetMetalSparkling(o.Name)        # Add

o=Bladex.CreateEntity("Lucero5","Lamparaegipto",822570.506000,334798.220000,170180.512000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero5",35.000000,0.250000)    # Changed
Sparks.SetMetalSparkling(o.Name)        # Add

o=Bladex.CreateEntity("Lucero6","LamparaNegra",817815.339000,330625.335000,138558.978000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.508650,0.508650,-0.491198,0.491198
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero6", 35.000000, 0.100000)

o=Bladex.CreateEntity("Lucero7","LamparaNegra",817018.970000,329782.296000,201953.303000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero7",35.000000,0.100000)



o=Bladex.CreateEntity("Lucero8","LamparaNegra",848738.355000,329843.762000,189102.957000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.006164,0.006171,-0.707080,0.707080
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero8",30.000000,0.250000)

o=Bladex.CreateEntity("Lucero9","LamparaNegra",848728.004000,329882.792000,151418.563000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero9",30.000000,0.250000)

o=Bladex.CreateEntity("Lucero10","LamparaNegra",876461.326000,323047.094000,163799.092000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.495618,0.495618,-0.504344,0.504344
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero10",80.000000,0.250000)   # Changed

o=Bladex.CreateEntity("Lucero11","LamparaNegra",892987.584000,323812.575000,176618.534000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.517145,0.517145,0.482246,-0.482246
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero11",70.000000,0.125000)   # Changed

o=Bladex.CreateEntity("Lucero12","Lamparaegipto",920859.661000,342046.119000,150183.986000)
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero12",150.000000,0.100000)
Sparks.SetMetalSparkling(o.Name)        # Add

o=Bladex.CreateEntity("Lucero13","Lamparaegipto",921078.109000,342068.374000,190790.010000)
o.Static=1
o.Scale=0.990099
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(221,116,0)) ]
o.Data = 0
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n
OnOff.AddLightData("Lucero13",200.000000,0.100000)
Sparks.SetMetalSparkling(o.Name)        # Add


Stair1 = Bladex.GetSector(679730,308927,172595)
Stair1.OnEnter = Stair1Proc


Stair2 = Bladex.GetSector(666873, 318927, 161774)
Stair2.OnEnter = Stair2Proc

Stair3 = Bladex.GetSector(716841, 329517, 170206)
Stair3.OnEnter = Stair3Proc

Stair4 = Bladex.GetSector(758021, 333677, 168051)
Stair4.OnEnter = Stair4Proc



Room1 = Bladex.GetSector(808033, 335177, 158327)
Room1.OnEnter = Room1Proc

Room2 = Bladex.GetSector(803879, 335177, 181172)
Room2.OnEnter = Room1Proc

OldMan1 = Bladex.GetSector(870944, 337791, 170399)
OldMan1.OnEnter = OldMan1Proc

OldManStart = Bladex.GetSector(907978, 342528, 169847)
OldManStart.OnEnter = OldManStartProc

# Create the combined DarkLordDemon creature
AnAhkard=Bladex.CreateEntity("AnAhkard","DarkLord",936728.023485, 341276.066626, 170747.882814,"Person")
AnAhkard.Angle= math.pi*0.5
EnemyTypes.EnemyDefaultFuncs(AnAhkard)
AnAhkard.Blind= 1
AnAhkard.Deaf= 1


AnAhkard.Data.HidePos= (586400.75, 302647.75, 183222.469)

#AnAhkard.Data.positionlist.append(947942.0, 341046.0, 168636.0)
AnAhkard.Data.positionlist.append(936728.0, 341046.0, 170747.0)
AnAhkard.Data.positionlist.append(888887.0, 339467.0, 170374.0)
AnAhkard.Data.positionlist.append(857875.0, 336528.0, 169193.0)
AnAhkard.Data.positionlist.append(834775.0, 334800.0, 142409.0)
AnAhkard.Data.positionlist.append(830959.0, 334800.0, 197516.0)
AnAhkard.Data.positionlist.append(857602.0, 336500,0, 177598.0)
AnAhkard.Data.positionlist.append(854733.0, 335800.0, 160623.0)
AnAhkard.Data.positionlist.append(808223.0, 334800.0, 170505.0)
AnAhkard.Data.positionlist.append(824755.0, 334800.0, 181129.0)
AnAhkard.Data.positionlist.append(824687.0, 334800.0, 159004.0)
AnAhkard.Data.positionlist.append(790904.0, 333800.0, 170697.0)
AnAhkard.Data.positionlist.append(925000.0, 341635.0, 185000.0)
AnAhkard.Data.positionlist.append(925000.0, 341635.0, 155000.0)
AnAhkard.Data.positionlist.append(917804.0, 342300.0, 169627.0)
AnAhkard.Data.positionlist.append(816720.0, 334580.0, 198665.0)
AnAhkard.Data.positionlist.append(817128.0, 334580.0, 142612.0)
AnAhkard.Data.positionlist.append(808507.0, 334580.0, 180282.0)
AnAhkard.Data.positionlist.append(808179.0, 334580.0, 159567.0)
AnAhkard.Data.positionlist.append(791333.0, 334000.0, 158327.0)
AnAhkard.Data.positionlist.append(791049.0, 334000.0, 181503.0)

AnAhkard.Data.meteoritestartlist.append(918808, 311939, 170541)
AnAhkard.Data.meteoritestartlist.append(941884, 311939, 189170)
AnAhkard.Data.meteoritestartlist.append(942619, 312711, 15342)
AnAhkard.Data.meteoritestartlist.append(891605, 32000,  170348)
AnAhkard.Data.meteoritestartlist.append(862757, 311939, 170272)
AnAhkard.Data.meteoritestartlist.append(826864, 312833, 171076)
AnAhkard.Data.meteoritestartlist.append(808869, 312833, 171076)
AnAhkard.Data.meteoritestartlist.append(809675, 312833, 198035)
AnAhkard.Data.meteoritestartlist.append(808575, 312833, 141394)
AnAhkard.Data.meteoritestartlist.append(791985, 320918, 170745)
AnAhkard.Data.meteoritestartlist.append(925712, 311939, 186480)
AnAhkard.Data.meteoritestartlist.append(924000, 311939, 153966)
AnAhkard.Data.meteoritestartlist.append(902436, 323320, 170122)
AnAhkard.Data.meteoritestartlist.append(878578, 322825, 170391)
AnAhkard.Data.meteoritestartlist.append(853434, 320101, 178777)
AnAhkard.Data.meteoritestartlist.append(850538, 319372, 160015)
AnAhkard.Data.meteoritestartlist.append(827848, 318931, 159696)
AnAhkard.Data.meteoritestartlist.append(823467, 318587, 180050)
AnAhkard.Data.meteoritestartlist.append(839972, 322147, 198455)
AnAhkard.Data.meteoritestartlist.append(842386, 321194, 141280)



Rres = ReadGSFile.ReadGhostSectorFile("granfinal.sf")

for igs in Rres:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1

darfuncs.HideBadGuy(AnAhkard.Name)
# char.Position = (777026.612389, 333924.53425, 171282.712562)


### SONIDOS PASOS CARRERA FINAL PERSONAJE

chaospasopie= [0,0,0]
chaospasopie[0]=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'Chaospasopie1')
chaospasopie[0].MinDistance=30000
chaospasopie[0].MaxDistance=15000

chaospasopie[1]=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'Chaospasopie2')
chaospasopie[1].MinDistance=30000
chaospasopie[1].MaxDistance=15000

chaospasopie[2]=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'Chaospasopie3')
chaospasopie[2].MinDistance=30000
chaospasopie[2].MaxDistance=15000
