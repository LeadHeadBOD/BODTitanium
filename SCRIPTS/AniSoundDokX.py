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
TajoCortanteDok=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteDok')
TajoCortanteDok.SendNotify=0
TajoMutilacionDok=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionDok')
TajoMutilacionDok.SendNotify=0
GolpeContundenteDok=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteDok')
GolpeContundenteDok.SendNotify=0

InsultoDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'InsultoDok')
InsultoDok.SendNotify=1
InsultoDok.MinDistance=1000
InsultoDok.MaxDistance=28000


Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0
EsfuerzoCortoDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-1.wav', 'EsfuerzoCortoDok')
EsfuerzoCortoDok.SendNotify=0
EsfuerzoCortoDok.Volume=0.8
EsfuerzoCorto1Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-2.wav', 'EsfuerzoCorto1Dok')
EsfuerzoCorto1Dok.SendNotify=0
EsfuerzoCorto1Dok.Volume=0.8
EsfuerzoCorto2Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-5.wav', 'EsfuerzoCorto2Dok')
EsfuerzoCorto2Dok.SendNotify=0
EsfuerzoCorto2Dok.Volume=0.8
EsfuerzoCorto3Dok=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-6.wav', 'EsfuerzoCorto3Dok')
EsfuerzoCorto3Dok.SendNotify=0
EsfuerzoCorto3Dok.Volume=0.8

SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=0.6
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=0.6
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.6
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoCortoGrave.Volume=0.6

EsfuerzoGolpeFrontalDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-frontal.wav', 'EsfuerzoGolpeFrontalDok')
EsfuerzoGolpeFrontalDok.SendNotify=0
EsfuerzoGolpeLateralDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-lateral.wav', 'EsfuerzoGolpeLateralDok')
EsfuerzoGolpeLateralDok.SendNotify=0
EsfuerzoGolpeCabezaDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'EsfuerzoGolpeCabezaDok')
EsfuerzoGolpeCabezaDok.SendNotify=0
EsfuerzoGolpeArribaDok=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-arriba.wav', 'EsfuerzoGolpeArribaDok')
EsfuerzoGolpeArribaDok.SendNotify=0

MuerteDok1=Bladex.CreateSound('../../sounds/muerte-orco-1.wav', 'MuerteDok1')
MuerteDok1.SendNotify=0
MuerteDok2=Bladex.CreateSound('../../sounds/muerte-orco-2.wav', 'MuerteDok2')
MuerteDok2.SendNotify=0
MuerteDok3=Bladex.CreateSound('../../sounds/muerte-orco-3.wav', 'MuerteDok3')
MuerteDok3.SendNotify=0
MuerteDok4=Bladex.CreateSound('../../sounds/muerte-orco-4.wav', 'MuerteDok4')
MuerteDok4.SendNotify=0
HeridaDok1=Bladex.CreateSound('../../sounds/herido-orco-1.wav', 'HeridaDok1')
HeridaDok1.SendNotify=0
HeridaDok2=Bladex.CreateSound('../../sounds/herido-orco-2.wav', 'HeridaDok2')
HeridaDok2.SendNotify=0
HeridaDok3=Bladex.CreateSound('../../sounds/herido-orco-3.wav', 'HeridaDok3')
HeridaDok3.SendNotify=0

GritoDok1=Bladex.CreateSound('../../sounds/salto-inicio-orco.wav', 'GritoDok1')
GritoDok1.SendNotify=0
GritoDok1.Volume=1
GritoDok1.MinDistance=1000
GritoDok1.MaxDistance=25000
GritoDok2=Bladex.CreateSound('../../sounds/Prov_Orc1.wav', 'GritoDok2')
GritoDok2.SendNotify=0
GritoDok2.Volume=1
GritoDok2.MinDistance=1000
GritoDok2.MaxDistance=25000

print "Sonidos para el Dorco creados..."
