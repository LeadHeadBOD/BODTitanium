from math import pow
import Bladex
import GameText
import Torchs
import Scorer
import EnemyTypes
import Raster
import pocimac
import Scorer
import AuxFuncs

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


##caballero traidor 2 en mazmorras 

Espadaromana=Bladex.CreateEntity("RagnarEspadaromana2","Gladius",0,0,0)
Espadaromana.Weapon=1
Breakings.SetBreakableWS("RagnarEspadaromana2")
escudo=Bladex.CreateEntity("RagnarEsc2kgt","Escudo5",0,0,0)
Sparks.MakeShield("RagnarEsc2kgt")
Breakings.SetBreakableWS("RagnarEsc2kgt")
potion=Bladex.CreateEntity("Kngtant2Potion","PocimaTodo",0,0,0)
potion.Static=0
potion.Solid=1
potion.Scale=1.220190
pocimac.CreatePotion("Kngtant2Potion")

o=Bladex.CreateEntity("Kngtant2","Antorcha",0,0,0,"Weapon")
o.FiresIntensity=[ 5 ]
o.Lights=[ (15.000000,0.031250,(255,196,128)) ]	
Torchs.SetUsable("Kngtant2",3,3,20)


pers=Bladex.CreateEntity("2kngt","Knight_Traitor",-98100, 1000, 70200,"Person")
pers.Angle=3.7
pers.Level=0
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
EnemyTypes.EnemyDefaultFuncs(pers)
Actions.TakeObject(pers.Name,"Kngtant2")
Actions.TakeObject(pers.Name,"Kngtant2Potion")
pers.Blind=1
pers.Deaf=1

#AniSound.AsignarSonidosCaballeroTraidor('2kngt')

#pers.AddBayPoint=-98100, 1000, 70200
#pers.AddBayPoint=-93051.8141374, 932.947014954, 71237.154
#pers.AddBayPoint=-85890.8616155, 932.604150047, 71641.050
#pers.AddBayPoint=-77306.4370715, 930.238760653, 71144.891
#pers.AddBayPoint=-76392.7903621, 931.640361443, 69432.1411
#pers.AddBayPoint=-77226.7815714, 932.134043412, 67912.4388
#pers.AddBayPoint=-80903.432048, 930.154812849, 67043.845
#pers.AddBayPoint=-87931.4914835, 931.914836803, 66960.075
#pers.AddBayPoint=-96978.6259705, 929.289814233, 67383.396
#pers.AddBayPoint=-98334.241998, 931.336597073, 69086.004

sec2kngt=Bladex.GetSector(-70000, -5000, 85000)

sec2kngt.OnEnter=Despierta2kngt

	
	

Bladex.AddScheduledFunc(Bladex.GetTime(),RagnarInicio,())

############################################


ApagalaSec4 = Bladex.GetSector(-65082.6396779, -319.785933817, 77606.801)
ApagalaSec4.OnEnter = Apagala4



########################
### Tejados que resbalan
########################

Bladex.GetSector(-122026, -13441, 25155).TooSteep=1
Bladex.GetSector(-120580, -2000, 58000).TooSteep=1
Bladex.GetSector(-120580, -2000, 52200).TooSteep=1
Bladex.GetSector(-110000, 0, -103750).TooSteep=1
Bladex.GetSector(-110000, 0, -104750).TooSteep=1
