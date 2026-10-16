import OnOff
import Actions
import AuxFuncs
import PhantonFX
import OnInitTake
import GameText
import Sparks
import Ontake
import copy
from math import pow
import Sounds

# Frames totales 565
# Pasos
# 4,27,47,102
# Esfuerzos
# 115, +160
# Rotura
# 200
# Apoya
# 551

sonido_esfuerzo1 = 0
sonido_esfuerzo2 = 0

KING_ESFUERZO1 = 115.0/20.0
KING_ESFUERZO2 = 160.0/20.0

#
TUMBA_PASO1 =   4.0/20.0
TUMBA_PASO2 =  27.0/20.0
TUMBA_PASO3 =  47.0/20.0
TUMBA_PASO4 = 102.0/20.0


SetSoundsEsfuerzo(char.Kind[0])


# sonidos Cool!

#_SndDemonio1=Bladex.CreateSound("../../Sounds/Demon-spirit1.wav","Demo1")
#_SndDemonio1.MaxDistance=1000000.0
#
#_SndDemonio2=Bladex.CreateSound("../../Sounds/Demon-spirit2.wav","Demo2")
#_SndDemonio2.MaxDistance=1000000.0
#
#_SndDemonio3=Bladex.CreateSound("../../Sounds/Demon-spirit3.wav","Demo3")
#_SndDemonio3.MaxDistance=1000000.0
#
#_SndDemonio4=Bladex.CreateSound("../../Sounds/Demon-spirit4.wav","Demo4")
#_SndDemonio4.MaxDistance=1000000.0
#
#_SndDemonio5=Bladex.CreateSound("../../Sounds/Demon-spirit5.wav","Demo4")
#_SndDemonio5.MaxDistance=1000000.0

_SndFireBall=Bladex.CreateSound("../../Sounds/fireball-swing.wav","Fireball")
_SndFireBall.MaxDistance=1000000.0

_SndFireWarp=Bladex.CreateSound("../../Sounds/Fire-curtains.wav","FireWarp")
_SndFireWarp.MaxDistance=1000000.0


_SndHostia=Bladex.CreateSound("../../Sounds/paso-golem-4.wav","SondoHostia")
_SndHostia.MaxDistance=1000000.0

_SndGritoKeletum=Bladex.CreateSound("../../Sounds/SNOWTROLL-ESFUERZO-3.wav","GritoKeletum")
_SndGritoKeletum.MaxDistance=1000000.0


OnOff.AddLightData("luzrey1",5.500000,0.070000)
OnOff.AddLightData("luzrey2",5.791800,0.180993)
OnOff.AddLightData("luzrey3",4.000000,0.070000)
OnOff.AddLightData("luzrey4",31.947647,0.100000)

# char.Position = 109092.427000,1310.936000-1500,607.453000


player = ""



KingStartSector=Bladex.GetSector(105360.716012, 1535.2, 169.181895237)
KingStartSector.OnEnter = CaminaHastaLapidaRey

Bladex.AddCombustionDataFor("Skeleton", "Fire", 250, 400, 4, 1, 3, 144000) # se extingira en 40 horas!


LapidK=Bladex.CreateEntity("lapidarey","Lapidarey",109092.427000,1310.936000,607.453000)
LapidK.Static=0
LapidK.Scale=1.257163
LapidK.Position = 109092.427000,1310.936000,607.453000
LapidK.Orientation=0.498355,0.498555,-0.501735,0.501345
LapidK.Solid = 0

# El rey ha muerto... Larga vida al rey!
#------------------------------------------------



ffY = ff.Position[1]
blY = bl.Position[1]
Continuafet = 1

# Activa las trampas del tempo

Ontake.AddOnTakeEvent(ff.Name,Fetichazo)

esq = CreaElEsqueleto(109207,2000,482)

#	"../../Sounds/fireball-swing.wav"	:	Enciende el fuego.
#	"../../Sounds/Fire-curtainsL.wav"    :	Loop de fuego (4 Secs).
#	"../../Sounds/Demon-spirit1.wav"     \
#	"../../Sounds/Demon-spirit2.wav"      |
#	"../../Sounds/Demon-spirit3.wav"       > Sonidos aleatorios en la escena
#	"../../Sounds/Demon-spirit4.wav"      |
#	"../../Sounds/Demon-spirit5.wav"     /
#	"../../Sounds/eagle-screech.wav"     :       Grito del esqueleto
#	"../../Sounds/Stone-door-shut.wav"	:	Golpe de lapida