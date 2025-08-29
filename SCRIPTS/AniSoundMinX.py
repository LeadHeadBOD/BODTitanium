##///
##||| AniSoundMinX.PY TITANIUM
##||| Change list:
##||| * Fixed the mistimed "whooshing"
##||| * Commented out non-existent animations
##||| * Movimento2 is now a unique sound not a dupe of Movimento1
##||| * Restored unused minotaur death sound (var name "MuerteMin3")
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

GolpeArmaEscudoMin=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoMin')
GolpeArmaEscudoMin.SendNotify=0
GolpeArmaArmaMin=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaMin')
GolpeArmaArmaMin.SendNotify=0
TajoEmpalanteMin=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteMin')
TajoEmpalanteMin.SendNotify=0
TajoCortanteMin=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteMin')
TajoCortanteMin.SendNotify=0
TajoMutilacionMin=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionMin')
TajoMutilacionMin.SendNotify=0
GolpeContundenteMin=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteMin')
GolpeContundenteMin.SendNotify=0



EsfuerzoCorto1Min=Bladex.CreateSound('../../sounds/ATAQUE-MINO1.wav', 'EsfuerzoCorto1Min')
EsfuerzoCorto1Min.SendNotify=0
EsfuerzoCorto1Min.Volume=0.8
EsfuerzoCorto1Min.MinDistance=1000
EsfuerzoCorto1Min.MaxDistance=25000
EsfuerzoCorto2Min=Bladex.CreateSound('../../sounds/ATAQUE-MINO8.wav', 'EsfuerzoCorto2Min')
EsfuerzoCorto2Min.SendNotify=0
EsfuerzoCorto2Min.Volume=0.8
EsfuerzoCorto2Min.MinDistance=1000
EsfuerzoCorto2Min.MaxDistance=25000
EsfuerzoCorto3Min=Bladex.CreateSound('../../sounds/ATAQUE-MINO3.wav', 'EsfuerzoCorto3Min')
EsfuerzoCorto3Min.SendNotify=0
EsfuerzoCorto3Min.Volume=0.8
EsfuerzoCorto3Min.MinDistance=1000
EsfuerzoCorto3Min.MaxDistance=25000
EsfuerzoCorto4Min=Bladex.CreateSound('../../sounds/ATAQUE-MINO5.wav', 'EsfuerzoCorto4Min')
EsfuerzoCorto4Min.SendNotify=0
EsfuerzoCorto4Min.Volume=0.8
EsfuerzoCorto4Min.MinDistance=1000
EsfuerzoCorto4Min.MaxDistance=25000
EsfuerzoCorto4Min.SendNotify=0
EsfuerzoCorto5Min=Bladex.CreateSound('../../sounds/ATAQUE-MINO6.wav', 'EsfuerzoCorto5Min')
EsfuerzoCorto5Min.SendNotify=0
EsfuerzoCorto5Min.Volume=0.8
EsfuerzoCorto5Min.MinDistance=1000
EsfuerzoCorto5Min.MaxDistance=25000


SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=0.8
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=0.8
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.8
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.8
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.8
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.8


EsfuerzoGolpeLateralMin=Bladex.CreateSound('../../sounds/ATAQUE-MINO7.wav', 'EsfuerzoGolpeLateralMin')
EsfuerzoGolpeLateralMin.SendNotify=0
EsfuerzoGolpeLateralMin.Volume=0.8
EsfuerzoGolpeLateralMin.MinDistance=1000
EsfuerzoGolpeLateralMin.MaxDistance=25000
EsfuerzoGolpeArribaMin=Bladex.CreateSound('../../sounds/ATAQUE-MINO4.wav', 'EsfuerzoGolpeArribaMin')
EsfuerzoGolpeArribaMin.SendNotify=0
EsfuerzoGolpeArribaMin.Volume=0.8
EsfuerzoGolpeArribaMin.MinDistance=1000
EsfuerzoGolpeArribaMin.MaxDistance=25000

###
# Added Min/Max distance param for all heridas and muertes 
# Previously was missing, making the sounds low range and quiet
#       -LeadHead

MuerteMin1=Bladex.CreateSound('../../sounds/MUERTE-MINO3.wav', 'MuerteMin1')
MuerteMin1.SendNotify=0
MuerteMin1.MinDistance=1000
MuerteMin1.MaxDistance=25000
MuerteMin2=Bladex.CreateSound('../../sounds/MUERTE-MINO2.wav', 'MuerteMin2')
MuerteMin2.SendNotify=0
MuerteMin2.MinDistance=1000
MuerteMin2.MaxDistance=25000

### Previously unused sound file    -LeadHead
MuerteMin3=Bladex.CreateSound('../../sounds/MUERTE-MINO1.wav', 'MuerteMin3')
MuerteMin3.SendNotify=0
MuerteMin3.MinDistance=1000
MuerteMin3.MaxDistance=25000

AgonizaMin2=Bladex.CreateSound('../../sounds/AGONIZANDO-MINO.wav', 'AgonizaMin2')
AgonizaMin2.SendNotify=0
AgonizaMin2.MinDistance=1000
AgonizaMin2.MaxDistance=16000

HeridaMin1=Bladex.CreateSound('../../sounds/MINOTAURO-GRUNIDO1.wav', 'HeridaMin1')
HeridaMin1.SendNotify=0
HeridaMin1.MinDistance=1000
HeridaMin1.MaxDistance=16000

HeridaMin2=Bladex.CreateSound('../../sounds/MINOTAURO-GRUNIDO2.wav', 'HeridaMin2')
HeridaMin2.SendNotify=0
HeridaMin2.MinDistance=1000
HeridaMin2.MaxDistance=16000

HeridaMin3=Bladex.CreateSound('../../sounds/MINOTAURO-GRUNIDO1.wav', 'HeridaMin3')      # PLAGUE: Dupe of HeridaMin1
HeridaMin3.SendNotify=0
HeridaMin3.MinDistance=1000
HeridaMin3.MaxDistance=16000

HeridaMin4=Bladex.CreateSound('../../sounds/MUERTE-MINO2.wav', 'HeridaMin4')
HeridaMin4.SendNotify=0
HeridaMin4.MinDistance=1000
HeridaMin4.MaxDistance=25000

RespiraMin1=Bladex.CreateSound('../../sounds/RESPIRACIONES-MINO.wav', 'RespiraMin1')
RespiraMin1.SendNotify=0
RespiraMin1.Volume=0.6
RespiraMin1.MinDistance=1000
RespiraMin1.MaxDistance=16000

RespiraMin2=Bladex.CreateSound('../../sounds/RESPIRACIONES-MINO2.wav', 'RespiraMin2')
RespiraMin2.SendNotify=0
RespiraMin2.Volume=0.6
RespiraMin2.MinDistance=1000
RespiraMin2.MaxDistance=16000


AndarMin1=Bladex.CreateSound('../../sounds/ANDANDO-MINO.wav', 'AndarMin1')
AndarMin1.SendNotify=0
AndarMin1.Volume=0.6
AndarMin1.MinDistance=1000
AndarMin1.MaxDistance=25000

AndarMin2=Bladex.CreateSound('../../sounds/ANDANDO-MINO2.wav', 'AndarMin2')
AndarMin2.SendNotify=0
AndarMin2.Volume=0.6
AndarMin2.MinDistance=1000
AndarMin2.MaxDistance=25000


MovimientoMin1=Bladex.CreateSound('../../sounds/mov-troll-1.wav', 'MovimientoMin1')
MovimientoMin1.SendNotify=0
MovimientoMin1.Volume=1
MovimientoMin1.MinDistance=1000
MovimientoMin1.MaxDistance=25000

MovimientoMin2=Bladex.CreateSound('../../sounds/mov-troll-2.wav', 'MovimientoMin2')     # Changed, was prev dupe of Min1
MovimientoMin2.SendNotify=0
MovimientoMin2.Volume=1
MovimientoMin2.MinDistance=1000
MovimientoMin2.MaxDistance=25000


CaidaMin1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaMin1')
CaidaMin1.SendNotify=0
CaidaMin1.Volume=0.3
CaidaMin1.MinDistance=1000
CaidaMin1.MaxDistance=25000





print "Sonidos para el Minotaur creados..."
