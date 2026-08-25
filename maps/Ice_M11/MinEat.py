##///
##||| Ice_M11/MinEat.PY TITANIUM
##||| Change list:
##||| * Disabled collision on meat so the scene actually works
##||| * Removed duplicate sound assignment to Mino
##\\\ 

import EnemyTypes
import Reference
import AniSound
import Actions
import Damage
import Sounds
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

MINO_FDESPEDAZA1 =  23.0/20.0
MINO_FDESPEDAZA2 =  67.0/20.0
MINO_FDESPEDAZA3 = 135.0/20.0
MINO_FDESPEDAZA4 = 195.0/20.0
MINO_FDESPEDAZA5 = 235.0/20.0

MINO_FMORDISCO1 =  28.0/20.0
MINO_FMORDISCO2 =  72.0/20.0
MINO_FMORDISCO3 = 140.0/20.0
MINO_FMORDISCO4 = 207.0/20.0
MINO_FMORDISCO5 = 242.0/20.0

CarneFadeDelta = 0.1
LifeMinoBlood = 0.3

SndBocado=Sounds.CreateEntitySound("../../Sounds/Masticar22.wav","Bocado")
SndBocado.MaxDistance=5000.0   ### was just 1k
SndBocado.Volume = 1.0

SndDespedaza=Sounds.CreateEntitySound("../../Sounds/rugido-demon2.wav","Despedaza")
SndDespedaza.MaxDistance=20000.0
SndDespedaza.Volume = 1.0


#ComidaMin = Bladex.CreateEntity("ComidaMinorauro","Knight_Traitor",77663, -885, 17076,"Person")
ComidaMin = Bladex.CreateEntity("ComidaMinorauro","Knight_Traitor",77463, -885, 17276,"Person")

ComidaMinCabeza = ComidaMin.SeverLimb(1)
ComidaMinCabeza.CastShadows = 0
ComidaMinLeftArm = ComidaMin.SeverLimb(2)
ComidaMinLeftArm.CastShadows = 0
ComidaMinRightArm = ComidaMin.SeverLimb(4)
ComidaMinRightArm.CastShadows = 0
#ComidaMinLeftLeg = ComidaMin.SeverLimb(6)
#ComidaMinLeftLeg.CastShadows = 0
ComidaMinRightLeg = ComidaMin.SeverLimb(8)
ComidaMinRightLeg.CastShadows = 0
ComidaMin.Angle = 0.75
ComidaMin.Life = 0
ComidaMin.CastShadows = 0

#Hachacarnicero
garropineat=Bladex.CreateEntity("MinGarropinEat","Hachacarnicero",0,0,0,"Weapon")

Mino=Bladex.CreateEntity("MinoEat","Minotaur",78400,-1200,18000,"Person")
Mino.Angle = 2.8
Mino.Level=lvl_control.GiveLevel(3,7)
EnemyTypes.EnemyDefaultFuncs(Mino)
Mino.DamageFunc = None
Mino.Deaf = 1
Mino.Blind = 1


MinoEatquad = Bladex.CreateEntity("MinoEatquad","Bloque",78400,-1200,18000)
MinoEatquad.Orientation = (0.707107245922, 0.0, 0.0, 0.707106292248)
MinoEatquad.Scale = 6
MinoEatquad.ExclusionMask=2|4|1337  ### Add
MinoEatquad.CastShadows = 0
MinoEatquad.Alpha       = 0.0
MinoEatquad.RasterMode  ="Read"



MinoCarneRight=Bladex.CreateEntity("CarneRight","Paletilla",0,0,0,"Physic")
MinoCarneRight.Scale = 1.5
inv = Mino.GetInventory()
inv.LinkRightHand("CarneRight")
MinoCarneRight.CastShadows = 0
MinoCarneRight.ExclusionMask = 1337 ### Add

MinoCarneLeft=Bladex.CreateEntity("CarneLeft","Paletilla",0,0,0,"Physic")
MinoCarneLeft.Scale = 1.3
inv.LinkLeftHand("CarneLeft")
#inv.LinkLeftHand(ComidaMinCabeza.Name)
MinoCarneLeft.CastShadows = 0
MinoCarneLeft.ExclusionMask = 1337 ### Add


arma = Bladex.GetEntity("MinGarropinEat")
arma.Position = 77576.8307735, 66.2779602609, 16874.917484
arma.Orientation = 0.0710847228765, -0.986545443535, 0.138073772192, -0.0510672628
#arma.Position = 78440.6180035, -1533.74537287, 18051.7721
#arma.Orientation = 0.837864220142, -0.338378101587, 0.220216616988, 0.367407977

SecMinEat = Bladex.GetSector(72900,-910,18300)
SecMinEat.OnEnter = ActivateMinoEat

SecMinEat2 = Bladex.GetSector(93700,-6200,27700)
SecMinEat2.OnEnter = ActivateMinoEat2

MinoEat = 1