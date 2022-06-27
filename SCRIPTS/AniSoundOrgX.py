import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

GolpeArmaEscudoOrk=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoOrk')
GolpeArmaEscudoOrk.SendNotify=0
GolpeArmaArmaOrk=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaOrk')
GolpeArmaArmaOrk.SendNotify=0
TajoEmpalanteOrk=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-33.wav', 'TajoEmpalanteOrk')
TajoEmpalanteOrk.SendNotify=0
TajoEmpalanteOrk.Volume=1
TajoCortanteOrk=Bladex.CreateSound('../../sounds/GOLPE-ARMADUR-44.wav', 'TajoCortanteOrk')
TajoCortanteOrk.SendNotify=0
TajoCortanteOrk.Volume=1
TajoMutilacionOrk=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionOrk')
TajoMutilacionOrk.SendNotify=0
GolpeContundenteOrk=Bladex.CreateSound('../../sounds/golpe-maza-arm.wav', 'GolpeContundenteOrk')
GolpeContundenteOrk.SendNotify=0

Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0
EsfuerzoCortoOrc=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-1.wav', 'EsfuerzoCortoOrc')
EsfuerzoCortoOrc.SendNotify=0
EsfuerzoCortoOrc.Volume=0.9
EsfuerzoCortoOrc.MinDistance=1000
EsfuerzoCortoOrc.MaxDistance=25000
EsfuerzoCorto1Orc=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-2.wav', 'EsfuerzoCorto1Orc')
EsfuerzoCorto1Orc.SendNotify=0
EsfuerzoCorto1Orc.Volume=0.9
EsfuerzoCorto1Orc.MinDistance=1000
EsfuerzoCorto1Orc.MaxDistance=25000
EsfuerzoCorto2Orc=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-5.wav', 'EsfuerzoCorto2Orc')
EsfuerzoCorto2Orc.SendNotify=0
EsfuerzoCorto2Orc.Volume=0.9
EsfuerzoCorto2Orc.MinDistance=1000
EsfuerzoCorto2Orc.MaxDistance=25000
EsfuerzoCorto3Orc=Bladex.CreateSound('../../sounds/esfuerzo-orco-corto-6.wav', 'EsfuerzoCorto3Orc')
EsfuerzoCorto3Orc.SendNotify=0
EsfuerzoCorto3Orc.Volume=0.9
EsfuerzoCorto3Orc.MinDistance=1000
EsfuerzoCorto3Orc.MaxDistance=25000

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

EsfuerzoGolpeFrontalOrc=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-frontal.wav', 'EsfuerzoGolpeFrontalOrc')
EsfuerzoGolpeFrontalOrc.SendNotify=1
EsfuerzoGolpeFrontalOrc.MinDistance=1000
EsfuerzoGolpeFrontalOrc.MaxDistance=25000
EsfuerzoGolpeLateralOrc=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-lateral.wav', 'EsfuerzoGolpeLateralOrc')
EsfuerzoGolpeLateralOrc.SendNotify=1
EsfuerzoGolpeLateralOrc.MinDistance=1000
EsfuerzoGolpeLateralOrc.MaxDistance=25000
EsfuerzoGolpeCabezaOrc=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'EsfuerzoGolpeCabezaOrc')
EsfuerzoGolpeCabezaOrc.SendNotify=1
EsfuerzoGolpeCabezaOrc.MinDistance=1000
EsfuerzoGolpeCabezaOrc.MaxDistance=25000
EsfuerzoGolpeArribaOrc=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-arriba.wav', 'EsfuerzoGolpeArribaOrc')
EsfuerzoGolpeArribaOrc.SendNotify=1
EsfuerzoGolpeArribaOrc.MinDistance=1000
EsfuerzoGolpeArribaOrc.MaxDistance=25000

Relax1=Bladex.CreateSound('../../sounds/Respiracion-orco-1.wav', 'Relax1')
Relax1.SendNotify=0
Relax1.Volume=1
Relax1.MinDistance=1000
Relax1.MaxDistance=14000

Relax2=Bladex.CreateSound('../../sounds/Respiracion-orco-2.wav', 'Relax2')
Relax2.SendNotify=0
Relax2.Volume=1
Relax2.MinDistance=1000
Relax2.MaxDistance=14000

MuerteOrc1=Bladex.CreateSound('../../sounds/muerte-orco-1.wav', 'MuerteOrc1')
MuerteOrc1.SendNotify=0
MuerteOrc1.MinDistance=1000
MuerteOrc1.MaxDistance=25000
MuerteOrc2=Bladex.CreateSound('../../sounds/muerte-orco-2.wav', 'MuerteOrc2')
MuerteOrc2.SendNotify=0
MuerteOrc2.MinDistance=1000
MuerteOrc2.MaxDistance=25000
MuerteOrc3=Bladex.CreateSound('../../sounds/muerte-orco-3.wav', 'MuerteOrc3')
MuerteOrc3.SendNotify=0
MuerteOrc3.MinDistance=1000
MuerteOrc3.MaxDistance=25000
MuerteOrc4=Bladex.CreateSound('../../sounds/muerte-orco-4.wav', 'MuerteOrc4')
MuerteOrc4.SendNotify=0
MuerteOrc4.MinDistance=1000
MuerteOrc4.MaxDistance=25000
HeridaOrc1=Bladex.CreateSound('../../sounds/herido-orco-1.wav', 'HeridaOrc1')
HeridaOrc1.SendNotify=0
HeridaOrc1.MinDistance=1000
HeridaOrc1.MaxDistance=25000
HeridaOrc2=Bladex.CreateSound('../../sounds/herido-orco-2.wav', 'HeridaOrc2')
HeridaOrc2.SendNotify=0
HeridaOrc2.MinDistance=1000
HeridaOrc2.MaxDistance=25000
HeridaOrc3=Bladex.CreateSound('../../sounds/herido-orco-3.wav', 'HeridaOrc3')
HeridaOrc3.SendNotify=0
HeridaOrc3.MinDistance=1000
HeridaOrc3.MaxDistance=25000

AndarOrc1=Bladex.CreateSound('../../sounds/mov-armadura-5.wav', 'AndarOrc1')
AndarOrc1.SendNotify=0
AndarOrc1.Volume=0.3
AndarOrc1.MinDistance=5000
AndarOrc1.MaxDistance=15000
AndarOrc2=Bladex.CreateSound('../../sounds/mov-armadura-6.wav', 'AndarOrc2')
AndarOrc2.SendNotify=0
AndarOrc2.Volume=0.3
AndarOrc2.MinDistance=5000
AndarOrc2.MaxDistance=15000


InsultoOrg=Bladex.CreateSound('../../sounds/esfuerzo-orco-golpe-cabeza.wav', 'InsultoOrg')
InsultoOrg.SendNotify=1
InsultoOrg.MinDistance=1000
InsultoOrg.MaxDistance=28000

DesangreOrc1=Bladex.CreateSound('../../sounds/desangre2.wav', 'DesangreOrc1')
DesangreOrc1.SendNotify=0
DesangreOrc1.Volume=0.8
DesangreOrc1.MinDistance=1000
DesangreOrc1.MaxDistance=25000
DesangreOrc2=Bladex.CreateSound('../../sounds/desangre4.wav', 'DesangreOrc2')
DesangreOrc2.SendNotify=0
DesangreOrc2.Volume=0.8
DesangreOrc2.MinDistance=1000
DesangreOrc2.MaxDistance=25000

CaidaOrc1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaOrc1')
CaidaOrc1.SendNotify=0
CaidaOrc1.Volume=0.4
CaidaOrc1.MinDistance=1000
CaidaOrc1.MaxDistance=25000

CaidaOrc2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaOrc2')
CaidaOrc2.SendNotify=0
CaidaOrc2.Volume=0.4
CaidaOrc2.MinDistance=1000
CaidaOrc2.MaxDistance=25000

GritoOrc1=Bladex.CreateSound('../../sounds/salto-inicio-orco.wav', 'GritoOrc1')
GritoOrc1.SendNotify=0
GritoOrc1.Volume=1
GritoOrc1.MinDistance=1000
GritoOrc1.MaxDistance=25000
GritoOrc2=Bladex.CreateSound('../../sounds/Prov_Orc1.wav', 'GritoOrc2')
GritoOrc2.SendNotify=0
GritoOrc2.Volume=1
GritoOrc2.MinDistance=1000
GritoOrc2.MaxDistance=25000

print "Sonidos para el orco creados..."
