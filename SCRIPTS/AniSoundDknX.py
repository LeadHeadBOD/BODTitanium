##///
##||| AniSoundDknX.PY TITANIUM
##||| Change list:
##||| * Removed duplicate entry for alert sound
##||| * Changed alert sound variable name, to prevent the Tkn sound overriding Dkn sound
##||| * 
##||| * 
##||| *
##||| *
##\\\ 

import Bladex
import Language
# *********************************
# *      Creacion de sonidos      *
# *********************************

language = Language.CheckFallback()

GolpeArmaEscudoDkn=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoDkn')
GolpeArmaEscudoDkn.SendNotify=1
GolpeArmaArmaDkn=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaDkn')
GolpeArmaArmaDkn.SendNotify=1
TajoEmpalanteDkn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-33.wav', 'TajoEmpalanteDkn')
TajoEmpalanteDkn.SendNotify=1
TajoCortanteDkn=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteDkn')
TajoCortanteDkn.SendNotify=1
TajoMutilacionDkn=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionDkn')
TajoMutilacionDkn.SendNotify=1
GolpeContundenteDkn=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteDkn')
GolpeContundenteDkn.SendNotify=1


DKnightKeepStill=Bladex.CreateSound('../../sounds/'+language+'/InsultoDkn1.wav', 'DKnightKeepStill')    # Changed variable name not to conflict with Tkn -LeadHead
DKnightKeepStill.MinDistance=1000
DKnightKeepStill.MaxDistance=25000
# Dupe, commented out
# DKnightKeepStill=Bladex.CreateSound('../../sounds/'+language+'/InsultoDkn1.wav', 'DKnightKeepStill')    
# DKnightKeepStill.MinDistance=1000
# DKnightKeepStill.MaxDistance=25000



Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=1

EsfuerzoCortoDkn=Bladex.CreateSound('../../sounds/AtaqueDkn9.wav', 'EsfuerzoCortoTraidor')
EsfuerzoCortoDkn.SendNotify=1
EsfuerzoCortoDkn.Volume=0.8
EsfuerzoCorto1Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn1.wav', 'EsfuerzoCorto1Dkn')
EsfuerzoCorto1Dkn.SendNotify=1
EsfuerzoCorto1Dkn.Volume=0.8
EsfuerzoCorto2Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn10.wav', 'EsfuerzoCorto2Dkn')
EsfuerzoCorto2Dkn.SendNotify=1
EsfuerzoCorto2Dkn.Volume=0.8
EsfuerzoCorto3Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn13.wav', 'EsfuerzoCorto3Dkn')
EsfuerzoCorto3Dkn.SendNotify=1
EsfuerzoCorto3Dkn.Volume=0.8
EsfuerzoCorto4Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn2.wav', 'EsfuerzoCorto4Dkn')
EsfuerzoCorto4Dkn.SendNotify=1
EsfuerzoCorto4Dkn.Volume=0.8
EsfuerzoCorto5Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn3.wav', 'EsfuerzoCorto5Dkn')
EsfuerzoCorto5Dkn.SendNotify=1
EsfuerzoCorto5Dkn.Volume=0.8
EsfuerzoCorto6Dkn=Bladex.CreateSound('../../sounds/AtaqueDkn4.wav', 'EsfuerzoCorto6Dkn')
EsfuerzoCorto6Dkn.SendNotify=1
EsfuerzoCorto6Dkn.Volume=0.8
SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=1
SesgadoCorto.Volume=0.6
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=1
SesgadoLargo.Volume=0.6
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=1
SesgadoCortoGrave.Volume=0.6
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=1
SesgadoCortoGrave.Volume=0.6
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=1
SesgadoCortoGrave.Volume=0.6
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=1
SesgadoCortoGrave.Volume=0.6
EsfuerzoGolpeFrontalDkn=Bladex.CreateSound('../../sounds/AtaqueDkn11.wav', 'EsfuerzoGolpeFrontalDkn')
EsfuerzoGolpeFrontalDkn.SendNotify=1
EsfuerzoGolpeLateralDkn=Bladex.CreateSound('../../sounds/AtaqueDkn12.wav', 'EsfuerzoGolpeLateralDkn')
EsfuerzoGolpeLateralDkn.SendNotify=1
EsfuerzoGolpeCabezaDkn=Bladex.CreateSound('../../sounds/AtaqueDkn14.wav', 'EsfuerzoGolpeCabezaDkn')
EsfuerzoGolpeCabezaDkn.SendNotify=1
EsfuerzoGolpeAtrasDkn=Bladex.CreateSound('../../sounds/AtaqueDkn6.wav', 'EsfuerzoGolpeAtrasDkn')
EsfuerzoGolpeAtrasDkn.SendNotify=1

EsfuerzoDknMediano=Bladex.CreateSound('../../sounds/AtaqueDkn8.wav', 'EsfuerzoTraidorMediano')
EsfuerzoDknMediano.SendNotify=1
EsfuerzoDknLargo=Bladex.CreateSound('../../sounds/AtaqueDkn5.wav', 'EsfuerzoTraidorLargo')
EsfuerzoDknLargo.SendNotify=1

EsfuerzoGolpeArribaDkn=Bladex.CreateSound('../../sounds/AtaqueDkn7.wav', 'EsfuerzoGolpeArribaDkn')
EsfuerzoGolpeArribaDkn.SendNotify=1

MuerteDkn1=Bladex.CreateSound('../../sounds/MuerteDkn1.wav', 'MuerteDkn1')
MuerteDkn1.SendNotify=1
MuerteDkn2=Bladex.CreateSound('../../sounds/MuerteDkn2.wav', 'MuerteDkn2')
MuerteDkn2.SendNotify=1
MuerteDkn3=Bladex.CreateSound('../../sounds/MuerteDkn1.wav', 'MuerteDkn3')  # PLAGUE: These are effectively dupes
MuerteDkn3.SendNotify=1                                                     #         of Muerte1 and 2
MuerteDkn4=Bladex.CreateSound('../../sounds/MuerteDkn2.wav', 'MuerteDkn4')  #
MuerteDkn4.SendNotify=1                                                     #

HeridaDkn1=Bladex.CreateSound('../../sounds/HeridaDkn1.wav', 'HeridaTraidor1')
HeridaDkn1.SendNotify=1
HeridaDkn2=Bladex.CreateSound('../../sounds/HeridaDkn2.wav', 'HeridaTraidor2')
HeridaDkn2.SendNotify=1
HeridaDkn3=Bladex.CreateSound('../../sounds/HeridaDkn1.wav', 'HeridaTraidor3')
HeridaDkn3.SendNotify=1

RisaDkn=Bladex.CreateSound('../../sounds/RisaDkn.wav', 'RisaDkn')
#RisaDkn.SendNotify=1
RisaDkn.MinDistance=5000
RisaDkn.MaxDistance=30000
RisaDkn.Volume=0.7
RisaDkn2=Bladex.CreateSound('../../sounds/RisaDkn2.wav', 'RisaDkn2')
#RisaDkn2.SendNotify=1
RisaDkn2.MinDistance=5000
RisaDkn2.MaxDistance=30000
RisaDkn2.Volume=0.7


AltoDkn=Bladex.CreateSound('../../sounds/AlarmaDkn.wav', 'AltoDkn')
AltoDkn.MinDistance=5000
AltoDkn.MaxDistance=30000
AltoDkn.Volume=0.7
AltoDkn2=Bladex.CreateSound('../../sounds/AlarmaDkn1.wav', 'AltoDkn2')
AltoDkn2.MinDistance=5000
AltoDkn2.MaxDistance=30000
AltoDkn2.Volume=0.7

DesangreDkn1=Bladex.CreateSound('../../sounds/desangre1.wav', 'DesangreDkn1')
DesangreDkn1.SendNotify=0
DesangreDkn1.Volume=0.8
DesangreDkn2=Bladex.CreateSound('../../sounds/desangre3.wav', 'DesangreDkn2')
DesangreDkn2.SendNotify=0
DesangreDkn2.Volume=0.8

CaidaDkn1=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaDkn1')
CaidaDkn1.SendNotify=1
CaidaDkn1.Volume=0.8
CaidaDkn2=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDkn2')
CaidaDkn2.SendNotify=1
CaidaDkn2.Volume=0.8
CaidaDkn3=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaDkn3')
CaidaDkn3.SendNotify=1
CaidaDkn3.Volume=0.8
CaidaDkn4=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDkn4')
CaidaDkn4.SendNotify=1
CaidaDkn4.Volume=0.8


AndarDkn1=Bladex.CreateSound('../../sounds/mov-armadura-5.wav', 'AndarDkn1')
AndarDkn1.SendNotify=0
AndarDkn1.Volume=0.4
AndarDkn1.MinDistance=1000
AndarDkn1.MaxDistance=25000
AndarDkn2=Bladex.CreateSound('../../sounds/mov-armadura-6.wav', 'AndarDkn2')
AndarDkn2.SendNotify=0
AndarDkn2.Volume=0.4
AndarDkn2.MinDistance=1000
AndarDkn2.MaxDistance=25000

RespiraDkn1=Bladex.CreateSound('../../sounds/RespiracionDkn1.wav', 'RespiraDkn1')
RespiraDkn1.SendNotify=0
RespiraDkn1.Volume=0.4
RespiraDkn1.MinDistance=1000
RespiraDkn1.MaxDistance=15000
RespiraDkn2=Bladex.CreateSound('../../sounds/RespiracionDkn2.wav', 'RespiraDkn2')
RespiraDkn2.SendNotify=0
RespiraDkn2.Volume=0.4
RespiraDkn2.MinDistance=1000
RespiraDkn2.MaxDistance=15000


RespiraDkn3=Bladex.CreateSound('../../sounds/RespiracionDkn3.wav', 'RespiraDkn3')
RespiraDkn3.SendNotify=0
RespiraDkn3.Volume=0.4
RespiraDkn3.MinDistance=1000
RespiraDkn3.MaxDistance=15000
RespiraDkn4=Bladex.CreateSound('../../sounds/RespiracionDkn4.wav', 'RespiraDkn4')
RespiraDkn4.SendNotify=0
RespiraDkn4.Volume=0.4
RespiraDkn4.MinDistance=1000
RespiraDkn4.MaxDistance=15000




print "Sonidos para el caballero oscuro creados..."
