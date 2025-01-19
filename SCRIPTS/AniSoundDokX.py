##///
##||| ANISOUNDDOKX.PY TITANIUM
##||| Change list:
##||| * Restored missing sounds
##||| * Dok voice pitch-shifted as an experiment
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

GolpeArmaEscudoDok=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoDok')
GolpeArmaEscudoDok.SendNotify=0
GolpeArmaArmaDok=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaDok')
GolpeArmaArmaDok.SendNotify=0
TajoEmpalanteDok=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-33.wav', 'TajoEmpalanteDok')
TajoEmpalanteDok.SendNotify=0
TajoEmpalanteDok.Volume=1
TajoCortanteDok=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteDok')
TajoCortanteDok.SendNotify=0
TajoCortanteDok.Volume=1
TajoMutilacionDok=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionDok')
TajoMutilacionDok.SendNotify=0
GolpeContundenteDok=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteDok')
GolpeContundenteDok.SendNotify=0

Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0
EsfuerzoCortoDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-1.wav', 'EsfuerzoCortoDok')
EsfuerzoCortoDok.SendNotify=0
EsfuerzoCortoDok.Volume=0.9
EsfuerzoCortoDok.MinDistance=1000
EsfuerzoCortoDok.MaxDistance=25000
EsfuerzoCortoDok.Pitch=0.8
EsfuerzoCorto1Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-2.wav', 'EsfuerzoCorto1Dok')
EsfuerzoCorto1Dok.SendNotify=0
EsfuerzoCorto1Dok.Volume=0.9
EsfuerzoCorto1Dok.MinDistance=1000
EsfuerzoCorto1Dok.MaxDistance=25000
EsfuerzoCorto1Dok.Pitch=0.8
EsfuerzoCorto2Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-5.wav', 'EsfuerzoCorto2Dok')
EsfuerzoCorto2Dok.SendNotify=0
EsfuerzoCorto2Dok.Volume=0.9
EsfuerzoCorto2Dok.MinDistance=1000
EsfuerzoCorto2Dok.MaxDistance=25000
EsfuerzoCorto2Dok.Pitch=0.8
EsfuerzoCorto3Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-6.wav', 'EsfuerzoCorto3Dok')
EsfuerzoCorto3Dok.SendNotify=0
EsfuerzoCorto3Dok.Volume=0.9
EsfuerzoCorto3Dok.MinDistance=1000
EsfuerzoCorto3Dok.MaxDistance=25000
EsfuerzoCorto3Dok.Pitch=0.8

SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=0.8
SesgadoCorto.MinDistance=1000
SesgadoCorto.MaxDistance=25000
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=0.8
SesgadoLargo.MinDistance=1000
SesgadoLargo.MaxDistance=25000
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.8
SesgadoCortoGrave.MinDistance=1000
SesgadoCortoGrave.MaxDistance=25000
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoLargoGrave.Volume=0.8
SesgadoLargoGrave.MinDistance=1000
SesgadoLargoGrave.MaxDistance=25000
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoAgudo.Volume=0.8
SesgadoCortoAgudo.MinDistance=1000
SesgadoCortoAgudo.MaxDistance=25000
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoLargoAgudo.Volume=0.8
SesgadoLargoAgudo.MinDistance=1000
SesgadoLargoAgudo.MaxDistance=25000

EsfuerzoGolpeFrontalDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-frontal.wav', 'EsfuerzoGolpeFrontalDok')
EsfuerzoGolpeFrontalDok.SendNotify=1
EsfuerzoGolpeFrontalDok.MinDistance=1000
EsfuerzoGolpeFrontalDok.MaxDistance=25000
EsfuerzoGolpeFrontalDok.Pitch=0.8
EsfuerzoGolpeLateralDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-lateral.wav', 'EsfuerzoGolpeLateralDok')
EsfuerzoGolpeLateralDok.SendNotify=1
EsfuerzoGolpeLateralDok.MinDistance=1000
EsfuerzoGolpeLateralDok.MaxDistance=25000
EsfuerzoGolpeLateralDok.Pitch=0.8
EsfuerzoGolpeCabezaDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'EsfuerzoGolpeCabezaDok')
EsfuerzoGolpeCabezaDok.SendNotify=1
EsfuerzoGolpeCabezaDok.MinDistance=1000
EsfuerzoGolpeCabezaDok.MaxDistance=25000
EsfuerzoGolpeCabezaDok.Pitch=0.8
EsfuerzoGolpeArribaDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-arriba.wav', 'EsfuerzoGolpeArribaDok')
EsfuerzoGolpeArribaDok.SendNotify=1
EsfuerzoGolpeArribaDok.MinDistance=1000
EsfuerzoGolpeArribaDok.MaxDistance=25000
EsfuerzoGolpeArribaDok.Pitch=0.8

Relax1Dok=Bladex.CreateSound('../../sounds/Respiracion-orco-1.wav', 'Relax1Dok')
Relax1Dok.SendNotify=0
Relax1Dok.Volume=1
Relax1Dok.MinDistance=1000
Relax1Dok.MaxDistance=14000
Relax1Dok.Pitch=0.8

Relax2Dok=Bladex.CreateSound('../../sounds/Respiracion-orco-2.wav', 'Relax2Dok')
Relax2Dok.SendNotify=0
Relax2Dok.Volume=1
Relax2Dok.MinDistance=1000
Relax2Dok.MaxDistance=14000
Relax2Dok.Pitch=0.8

MuerteDok1=Bladex.CreateSound('../../sounds/muerte-orco-1.wav', 'MuerteDok1')
MuerteDok1.SendNotify=0
MuerteDok1.MinDistance=1000
MuerteDok1.MaxDistance=25000
MuerteDok1.Pitch=0.8
MuerteDok2=Bladex.CreateSound('../../sounds/muerte-orco-2.wav', 'MuerteDok2')
MuerteDok2.SendNotify=0
MuerteDok2.MinDistance=1000
MuerteDok2.MaxDistance=25000
MuerteDok2.Pitch=0.8
MuerteDok3=Bladex.CreateSound('../../sounds/muerte-orco-3.wav', 'MuerteDok3')
MuerteDok3.SendNotify=0
MuerteDok3.MinDistance=1000
MuerteDok3.MaxDistance=25000
MuerteDok3.Pitch=0.8
MuerteDok4=Bladex.CreateSound('../../sounds/muerte-orco-4.wav', 'MuerteDok4')
MuerteDok4.SendNotify=0
MuerteDok4.MinDistance=1000
MuerteDok4.MaxDistance=25000
MuerteDok4.Pitch=0.8
HeridaDok1=Bladex.CreateSound('../../sounds/herido-orco-1.wav', 'HeridaDok1')
HeridaDok1.SendNotify=0
HeridaDok1.MinDistance=1000
HeridaDok1.MaxDistance=25000
HeridaDok1.Pitch=0.8
HeridaDok2=Bladex.CreateSound('../../sounds/herido-orco-2.wav', 'HeridaDok2')
HeridaDok2.SendNotify=0
HeridaDok2.MinDistance=1000
HeridaDok2.MaxDistance=25000
HeridaDok2.Pitch=0.8
HeridaDok3=Bladex.CreateSound('../../sounds/herido-orco-3.wav', 'HeridaDok3')
HeridaDok3.SendNotify=0
HeridaDok3.MinDistance=1000
HeridaDok3.MaxDistance=25000
HeridaDok3.Pitch=0.8

AndarDok1=Bladex.CreateSound('../../sounds/mov-armadura-5.wav', 'AndarDok1')
AndarDok1.SendNotify=0
AndarDok1.Volume=0.3
AndarDok1.MinDistance=5000
AndarDok1.MaxDistance=15000
AndarDok2=Bladex.CreateSound('../../sounds/mov-armadura-6.wav', 'AndarDok2')
AndarDok2.SendNotify=0
AndarDok2.Volume=0.3
AndarDok2.MinDistance=5000
AndarDok2.MaxDistance=15000


InsultoDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'InsultoDok')
InsultoDok.SendNotify=1
InsultoDok.MinDistance=1000
InsultoDok.MaxDistance=28000
InsultoDok.Pitch=0.8

DesangreDok1=Bladex.CreateSound('../../sounds/desangre2.wav', 'DesangreDok1')
DesangreDok1.SendNotify=0
DesangreDok1.Volume=0.8
DesangreDok1.MinDistance=1000
DesangreDok1.MaxDistance=25000
DesangreDok2=Bladex.CreateSound('../../sounds/desangre4.wav', 'DesangreDok2')
DesangreDok2.SendNotify=0
DesangreDok2.Volume=0.8
DesangreDok2.MinDistance=1000
DesangreDok2.MaxDistance=25000

CaidaDok1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDok1')
CaidaDok1.SendNotify=0
CaidaDok1.Volume=0.4
CaidaDok1.MinDistance=1000
CaidaDok1.MaxDistance=25000

CaidaDok2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaDok2')
CaidaDok2.SendNotify=0
CaidaDok2.Volume=0.4
CaidaDok2.MinDistance=1000
CaidaDok2.MaxDistance=25000

GritoDok1=Bladex.CreateSound('../../sounds/salto-inicio-orco.wav', 'GritoDok1')
GritoDok1.SendNotify=0
GritoDok1.Volume=1
GritoDok1.MinDistance=1000
GritoDok1.MaxDistance=25000
GritoDok1.Pitch=0.8
GritoDok2=Bladex.CreateSound('../../sounds/Prov_Orc1.wav', 'GritoDok2')
GritoDok2.SendNotify=0
GritoDok2.Volume=1
GritoDok2.MinDistance=1000
GritoDok2.MaxDistance=25000
GritoDok2.Pitch=0.8

print "Sonidos para el Dorco creados..."
