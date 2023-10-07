##///
##||| ANISOUNDDWFX.PY TITANIUM
##||| Change list:
##||| * Normalized "draw weapon" sound for all 4 characters.
##||| * Added fire sound for Fire Axe special attack.
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

RuidoLlaveCerradura=Bladex.CreateSound('../../sounds/unlock-door3.wav', 'RuidoLlaveCerradura')
RuidoLlaveCerradura.SendNotify=0

Ruidook=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'Ruidook')
Ruidook.SendNotify=0

SonidoPalanca=Bladex.CreateSound('../../sounds/lever2.wav', 'SonidoPalanca')
SonidoPalanca.SendNotify=0

SonidoVaciarBotella=Bladex.CreateSound('../../sounds/agua-fuente-sobre-agua.wav', 'SonidoVaciarBotella')
SonidoVaciarBotella.SendNotify=0

SaltoCortoDwf=Bladex.CreateSound('../../sounds/enano-esfuerzo2.wav', 'SaltoCortoDwf')
SaltoCortoDwf.SendNotify=1
SaltoCortoDwf.Volume=1
SaltoCortoDwf.MinDistance=3000
SaltoCortoDwf.MaxDistance=6000

CogerLlave=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerLlave')
CogerLlave.SendNotify=0

CogerEspada=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CogerEspada')
CogerEspada.SendNotify=0

CogerArma=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerArma')
CogerArma.SendNotify=0

CambiarEscudo=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CambiarEscudo')
CambiarEscudo.SendNotify=0

GolpeArmaEscudoDwf=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoDwf')
GolpeArmaEscudoDwf.SendNotify=1
GolpeArmaEscudoDwf.MinDistance=1000
GolpeArmaEscudoDwf.MaxDistance=25000

GolpeArmaArmaDwf=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaDwf')
GolpeArmaArmaDwf.SendNotify=1
GolpeArmaArmaDwf.MinDistance=1000
GolpeArmaArmaDwf.MaxDistance=25000

GolpeContundenteDwf=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteDwf')
GolpeContundenteDwf.SendNotify=1
GolpeContundenteDwf.MinDistance=1000
GolpeContundenteDwf.MaxDistance=25000

TajoEmpalanteDwf=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteDwf')
TajoEmpalanteDwf.SendNotify=0

TajoCortanteDwf=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteDwf')
TajoCortanteDwf.SendNotify=0

TajoMutilacionDwf=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionDwf')
TajoMutilacionDwf.SendNotify=0

Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')                # PLAGUE: wtf, all 4 characters use the same sound, but all of them have different parameters.
Enfundar.SendNotify=1                                                                       # Normalized across all characters, I guess
Enfundar.Volume=0.8                                                                         #
Enfundar.MinDistance=2000                                                                   #                   -LeadHead
Enfundar.MaxDistance=4000


EsfuerzoCortoDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf2.wav', 'EsfuerzoCortoDwf')
EsfuerzoCortoDwf.SendNotify=1
EsfuerzoCortoDwf.Volume=1
EsfuerzoCortoDwf.MinDistance=1000
EsfuerzoCortoDwf.MaxDistance=25000

EsfuerzoCorto1Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf1.wav', 'EsfuerzoCorto1Dwf')
EsfuerzoCorto1Dwf.SendNotify=1
EsfuerzoCorto1Dwf.Volume=1
EsfuerzoCorto1Dwf.MinDistance=1000
EsfuerzoCorto1Dwf.MaxDistance=25000

EsfuerzoCorto2Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf7.wav', 'EsfuerzoCorto2Dwf')
EsfuerzoCorto2Dwf.SendNotify=1
EsfuerzoCorto2Dwf.Volume=1
EsfuerzoCorto2Dwf.MinDistance=1000
EsfuerzoCorto2Dwf.MaxDistance=25000

EsfuerzoCorto3Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf9.wav', 'EsfuerzoCorto3Dwf')
EsfuerzoCorto3Dwf.SendNotify=1
EsfuerzoCorto3Dwf.Volume=1
EsfuerzoCorto3Dwf.MinDistance=1000
EsfuerzoCorto3Dwf.MaxDistance=25000

EsfuerzoCorto4Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf10.wav', 'EsfuerzoCorto4Dwf')
EsfuerzoCorto4Dwf.SendNotify=1
EsfuerzoCorto4Dwf.Volume=1
EsfuerzoCorto4Dwf.MinDistance=1000
EsfuerzoCorto4Dwf.MaxDistance=25000

EsfuerzoCorto5Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf8.wav', 'EsfuerzoCorto5Dwf')
EsfuerzoCorto5Dwf.SendNotify=1
EsfuerzoCorto5Dwf.Volume=1
EsfuerzoCorto5Dwf.MinDistance=1000
EsfuerzoCorto5Dwf.MaxDistance=25000

EsfuerzoCorto6Dwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf6.wav', 'EsfuerzoCorto6Dwf')
EsfuerzoCorto6Dwf.SendNotify=1
EsfuerzoCorto6Dwf.Volume=1
EsfuerzoCorto6Dwf.MinDistance=1000
EsfuerzoCorto6Dwf.MaxDistance=25000

SesgadoCorto=Bladex.CreateSound('../../sounds/sesgado-corto.wav', 'SesgadoCorto')
SesgadoCorto.SendNotify=0
SesgadoCorto.Volume=1
SesgadoLargo=Bladex.CreateSound('../../sounds/sesgado-largo.wav', 'SesgadoLargo')
SesgadoLargo.SendNotify=0
SesgadoLargo.Volume=1
SesgadoCortoGrave=Bladex.CreateSound('../../sounds/sesgado-corto-grave.wav', 'SesgadoCortoGrave')
SesgadoCortoGrave.SendNotify=0
SesgadoCortoGrave.Volume=1
SesgadoLargoGrave=Bladex.CreateSound('../../sounds/sesgado-largo-grave.wav', 'SesgadoLargoGrave')
SesgadoLargoGrave.SendNotify=0
SesgadoLargoGrave.Volume=1
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoAgudo.Volume=1
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoLargoAgudo.Volume=1

SesgadoLento=Bladex.CreateSound('../../sounds/sesgado-lento2.wav', 'SesgadoLento')
SesgadoLento.SendNotify=0
SesgadoLento.Volume=0.6

ConcBladeSword1=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword1')
ConcBladeSword1.SendNotify=0
ConcBladeSword1.Volume=1.0
ConcBladeSword1.Pitch=0.7
ConcBladeSword2=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword2')
ConcBladeSword2.SendNotify=0
ConcBladeSword2.Volume=1.0
ConcBladeSword2.Pitch=0.9

EsfuerzoGolpeFrontalDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf5.wav', 'EsfuerzoGolpeFrontalDwf')
EsfuerzoGolpeFrontalDwf.SendNotify=1
EsfuerzoGolpeFrontalDwf.Volume=1
EsfuerzoGolpeFrontalDwf.MinDistance=1000
EsfuerzoGolpeFrontalDwf.MaxDistance=25000

EsfuerzoGolpeLateralDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf4.wav', 'EsfuerzoGolpeLateralDwf')
EsfuerzoGolpeLateralDwf.SendNotify=1
EsfuerzoGolpeLateralDwf.Volume=1
EsfuerzoGolpeLateralDwf.MinDistance=1000
EsfuerzoGolpeLateralDwf.MaxDistance=25000

EsfuerzoGolpeCabezaDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf3.wav', 'EsfuerzoGolpeCabezaDwf')
EsfuerzoGolpeCabezaDwf.SendNotify=1
EsfuerzoGolpeCabezaDwf.Volume=1
EsfuerzoGolpeCabezaDwf.MinDistance=1000
EsfuerzoGolpeCabezaDwf.MaxDistance=25000

EsfuerzoGolpeAtrasDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf2.wav', 'EsfuerzoGolpeAtrasDwf')
EsfuerzoGolpeAtrasDwf.SendNotify=1
EsfuerzoGolpeAtrasDwf.Volume=1
EsfuerzoGolpeAtrasDwf.MinDistance=1000
EsfuerzoGolpeAtrasDwf.MaxDistance=25000

EsfuerzoDwfMediano=Bladex.CreateSound('../../sounds/esfuerzo-Dwf1.wav', 'EsfuerzoDwfMediano')
EsfuerzoDwfMediano.SendNotify=1
EsfuerzoDwfMediano.Volume=1
EsfuerzoDwfMediano.MinDistance=1000
EsfuerzoDwfMediano.MaxDistance=25000

EsfuerzoGolpeArribaDwf=Bladex.CreateSound('../../sounds/esfuerzo-Dwf10.wav', 'EsfuerzoGolpeArribaDwf')
EsfuerzoGolpeArribaDwf.SendNotify=1
EsfuerzoGolpeArribaDwf.Volume=1
EsfuerzoGolpeArribaDwf.MinDistance=1000
EsfuerzoGolpeArribaDwf.MaxDistance=25000

MuerteDwf1=Bladex.CreateSound('../../sounds/Muerte-Dwf1.wav', 'MuerteDwf1')
#MuerteDwf1.SendNotify=0
MuerteDwf2=Bladex.CreateSound('../../sounds/Muerte-Dwf2.wav', 'MuerteDwf2')
#MuerteDwf2.SendNotify=0
MuerteDwf3=Bladex.CreateSound('../../sounds/Muerte-Dwf3.wav', 'MuerteDwf3')
#MuerteDwf3.SendNotify=0
MuerteDwf4=Bladex.CreateSound('../../sounds/Muerte-Dwf1.wav', 'MuerteDwf4')
#MuerteDwf4.SendNotify=0
HeridaDwf1=Bladex.CreateSound('../../sounds/herida-Dwf1.wav', 'HeridaDwf1')
#HeridaDwf1.SendNotify=0
HeridaDwf2=Bladex.CreateSound('../../sounds/herida-Dwf2.wav', 'HeridaDwf2')
#HeridaDwf2.SendNotify=0
HeridaDwf3=Bladex.CreateSound('../../sounds/herida-Dwf3.wav', 'HeridaDwf3')
#HeridaDwf3.SendNotify=0


AndarDwf1=Bladex.CreateSound('../../sounds/Mov-enano1.wav', 'AndarDwf1')
AndarDwf1.SendNotify=0.1
AndarDwf1.Volume=0.5
AndarDwf2=Bladex.CreateSound('../../sounds/Mov-enano2.wav', 'AndarDwf2')
AndarDwf2.SendNotify=0.1
AndarDwf2.Volume=0.5


CaidaDwf1=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaDwf1')
CaidaDwf1.SendNotify=1
CaidaDwf1.Volume=1
CaidaDwf2=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDwf2')
CaidaDwf2.SendNotify=1
CaidaDwf2.Volume=1
CaidaDwf3=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaDwf3')
CaidaDwf3.SendNotify=1
CaidaDwf3.Volume=1
CaidaDwf4=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDwf4')
CaidaDwf4.SendNotify=1
CaidaDwf4.Volume=1

DesangreDwf1=Bladex.CreateSound('../../sounds/desangre2.wav', 'DesangreDwf1')
DesangreDwf1.SendNotify=1
DesangreDwf1.Volume=1
DesangreDwf1.MinDistance=1000
DesangreDwf1.MaxDistance=25000
DesangreDwf2=Bladex.CreateSound('../../sounds/desangre4.wav', 'DesangreDwf2')
DesangreDwf2.SendNotify=1
DesangreDwf2.Volume=1
DesangreDwf2.MinDistance=1000
DesangreDwf2.MaxDistance=25000

EsfuerzoSubirDwf1=Bladex.CreateSound('../../sounds/esfuerzo-subirDwf1.wav', 'EsfuerzoSubirDwf1')
EsfuerzoSubirDwf1.SendNotify=1
EsfuerzoSubirDwf1.Volume=0.8
EsfuerzoSubirDwf1.MinDistance=1000
EsfuerzoSubirDwf1.MaxDistance=25000
EsfuerzoSubirDwf2=Bladex.CreateSound('../../sounds/esfuerzo-subirDwf2.wav', 'EsfuerzoSubirDwf2')
EsfuerzoSubirDwf2.SendNotify=1
EsfuerzoSubirDwf2.Volume=0.8
EsfuerzoSubirDwf2.MinDistance=1000
EsfuerzoSubirDwf2.MaxDistance=25000
EsfuerzoSubirDwf2.MaxDistance=25000
EsfuerzoSubirDwf3=Bladex.CreateSound('../../sounds/esfuerzo-subirDwf3.wav', 'EsfuerzoSubirDwf3')
EsfuerzoSubirDwf3.SendNotify=1
EsfuerzoSubirDwf3.Volume=0.8
EsfuerzoSubirDwf3.MinDistance=1000
EsfuerzoSubirDwf3.MaxDistance=25000

EsfuerzoSubirFinalDwf1=Bladex.CreateSound('../../sounds/esfuerzo-subirfinalDwf2.wav', 'EsfuerzoSubirFinalDwf1')
EsfuerzoSubirFinalDwf1.SendNotify=1
EsfuerzoSubirFinalDwf1.Volume=0.8
EsfuerzoSubirFinalDwf1.MinDistance=1000
EsfuerzoSubirFinalDwf1.MaxDistance=25000
EsfuerzoSubirFinalDwf2=Bladex.CreateSound('../../sounds/esfuerzo-subirfinalDwf1.wav', 'EsfuerzoSubirFinalDwf2')
EsfuerzoSubirFinalDwf2.SendNotify=1
EsfuerzoSubirFinalDwf2.Volume=0.8
EsfuerzoSubirFinalDwf2.MinDistance=1000
EsfuerzoSubirFinalDwf2.MaxDistance=25000
EsfuerzoSubirFinalDwf3=Bladex.CreateSound('../../sounds/esfuerzo-subirfinalDwf3.wav', 'EsfuerzoSubirFinalDwf3')
EsfuerzoSubirFinalDwf3.SendNotify=1
EsfuerzoSubirFinalDwf3.Volume=0.8
EsfuerzoSubirFinalDwf3.MinDistance=1000
EsfuerzoSubirFinalDwf3.MaxDistance=25000
MuerteQuemandoDwf=Bladex.CreateSound('../../sounds/muerte-quemandoDwf.wav', 'MuerteQuemandoDwf')
MuerteQuemandoDwf.SendNotify=1
MuerteQuemandoDwf.Volume=0.8
MuerteQuemandoDwf.MinDistance=1000
MuerteQuemandoDwf.MaxDistance=25000
MuerteSaltoVacioDwf1=Bladex.CreateSound('../../sounds/salto-vacio-final-Dwf.wav', 'MuerteSaltoVacioDwf1')
MuerteSaltoVacioDwf1.SendNotify=1
MuerteSaltoVacioDwf1.Volume=0.8
MuerteSaltoVacioDwf1.MinDistance=1000
MuerteSaltoVacioDwf1.MaxDistance=25000
Grito_Salto_VacioDwf=Bladex.CreateSound('../../sounds/salto-vacioDwf.wav', 'Grito-Salto-VacioDwf')
Grito_Salto_VacioDwf.SendNotify=1
Grito_Salto_VacioDwf.Volume=0.8
Grito_Salto_VacioDwf.MinDistance=1000
Grito_Salto_VacioDwf.MaxDistance=25000
MuerteAplastamientoDwf1=Bladex.CreateSound('../../sounds/aplastamiento.wav', 'MuerteAplastamientoDwf1')
MuerteAplastamientoDwf1.SendNotify=1
MuerteAplastamientoDwf1.Volume=0.8
MuerteAplastamientoDwf1.MinDistance=1000
MuerteAplastamientoDwf1.MaxDistance=25000

SesgadoEspecialCorto1=Bladex.CreateSound('../../sounds/sesgado-especial-corto.wav', 'SesgadoEspecialCorto1')
SesgadoEspecialCorto1.SendNotify=1
SesgadoEspecialCorto1.Volume=1.0
SesgadoEspecialCorto1.MinDistance=1000
SesgadoEspecialCorto1.MaxDistance=25000
SesgadoEspecialCorto2=Bladex.CreateSound('../../sounds/sesgado-especial-corto2.wav', 'SesgadoEspecialCorto2')
SesgadoEspecialCorto2.SendNotify=1
SesgadoEspecialCorto2.Volume=1.0
SesgadoEspecialCorto2.MinDistance=1000
SesgadoEspecialCorto2.MaxDistance=25000
SesgadoEspecialLargo1=Bladex.CreateSound('../../sounds/sesgado-especial-largo.wav', 'SesgadoEspecialLargo1')
SesgadoEspecialLargo1.SendNotify=1
SesgadoEspecialLargo1.Volume=1.0
SesgadoEspecialLargo1.MinDistance=1000
SesgadoEspecialLargo1.MaxDistance=25000
SesgadoEspecialLargo2=Bladex.CreateSound('../../sounds/sesgado-especial-largo2.wav', 'SesgadoEspecialLargo2')
SesgadoEspecialLargo2.SendNotify=1
SesgadoEspecialLargo2.Volume=1.0
SesgadoEspecialLargo2.MinDistance=1000
SesgadoEspecialLargo2.MaxDistance=25000

### Below added for Fire Axe -LeadHead

AtaqueFuego4=Bladex.CreateSound('../../sounds/fuego-ascende.wav', 'AtaqueFuego4')
AtaqueFuego4.SendNotify=1
AtaqueFuego4.Volume=1.0
AtaqueFuego4.MinDistance=3000
AtaqueFuego4.MaxDistance=15000

print "Sonidos para el Enano creados..."
