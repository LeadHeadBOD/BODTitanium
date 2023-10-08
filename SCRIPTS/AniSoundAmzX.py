##///
##||| ANISOUNDAMZX.PY TITANIUM
##||| Change list:
##||| * Normalized "draw weapon" sound for all 4 characters.
##||| * Added fire sound for Fire Axe special attack.
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

SonidoPalanca=Bladex.CreateSound('../../sounds/lever2.wav', 'SonidoPalanca')
SonidoPalanca.SendNotify=0

RuidoLlaveCerradura=Bladex.CreateSound('../../sounds/unlock-door3.wav', 'RuidoLlaveCerradura')
RuidoLlaveCerradura.SendNotify=0

RuidoLlave=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'RuidoLlave')
RuidoLlave.SendNotify=0

Ruidook=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'Ruidook')
Ruidook.SendNotify=0

SonidoVaciarBotella=Bladex.CreateSound('../../sounds/agua-fuente-sobre-agua.wav', 'SonidoVaciarBotella')
SonidoVaciarBotella.SendNotify=0

CogerLlave=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerLlave')
CogerLlave.SendNotify=0

CogerEspada=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CogerEspada')
CogerEspada.SendNotify=0

CogerArma=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerArma')
CogerArma.SendNotify=0

CambiarEscudo=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CambiarEscudo')
CambiarEscudo.SendNotify=0

#GritoHerida=Bladex.CreateSound('../../sounds/esfuerzo-barb-corto.wav', 'GritoHerida')      #PLAGUE: Why is this here AND commented out?
#GritoHerida.SendNotify=1
#GritoHerida.Volume=0.8

SaltoCortoAmz=Bladex.CreateSound('../../sounds/esfuerzo-salto-Amz.wav', 'SaltoCortoAmz')
SaltoCortoAmz.SendNotify=1
SaltoCortoAmz.MinDistance=1000
SaltoCortoAmz.MaxDistance=25000

GolpeArmaEscudoAmz=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoAmz')
GolpeArmaEscudoAmz.SendNotify=1
GolpeArmaEscudoAmz.MinDistance=1000
GolpeArmaEscudoAmz.MaxDistance=25000

GolpeArmaArmaAmz=Bladex.CreateSound('../../sounds/golpe-arma-arma.wav', 'GolpeArmaArmaAmz')
GolpeArmaArmaAmz.SendNotify=0

TajoEmpalanteAmz=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteAmz')
TajoEmpalanteAmz.SendNotify=1
TajoEmpalanteAmz.MinDistance=1000
TajoEmpalanteAmz.MaxDistance=25000

TajoCortanteAmz=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteAmz')
TajoCortanteAmz.SendNotify=1
TajoCortanteAmz.MinDistance=1000
TajoCortanteAmz.MaxDistance=25000

TajoMutilacionAmz=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionAmz')
TajoMutilacionAmz.SendNotify=1
TajoMutilacionAmz.MinDistance=1000
TajoMutilacionAmz.MaxDistance=25000

GolpeContundenteAmz=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteAmz')
GolpeContundenteAmz.SendNotify=1
GolpeContundenteAmz.MinDistance=1000
GolpeContundenteAmz.MaxDistance=25000

EnfundarAmz=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'EnfundarAmz')      # PLAGUE: wtf, all 4 characters use the same sound, but all of them have different parameters.
EnfundarAmz.SendNotify=1                                                                # Normalized across all characters, I guess
EnfundarAmz.Volume=0.8                                                                  #
EnfundarAmz.MinDistance=2000                                                            #                   -LeadHead
EnfundarAmz.MaxDistance=4000

EsfuerzoCortoAmz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz.wav', 'EsfuerzoCortoAmz')
EsfuerzoCortoAmz.SendNotify=1
EsfuerzoCortoAmz.Volume=1
EsfuerzoCortoAmz.MinDistance=1000
EsfuerzoCortoAmz.MaxDistance=25000

EsfuerzoCorto1Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz2.wav', 'EsfuerzoCorto1Amz')
EsfuerzoCorto1Amz.SendNotify=1
EsfuerzoCorto1Amz.Volume=1
EsfuerzoCorto1Amz.MinDistance=1000
EsfuerzoCorto1Amz.MaxDistance=25000

EsfuerzoCorto2Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz3.wav', 'EsfuerzoCorto2Amz')
EsfuerzoCorto2Amz.SendNotify=1
EsfuerzoCorto2Amz.Volume=1
EsfuerzoCorto3Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz4.wav', 'EsfuerzoCorto3Amz')
EsfuerzoCorto3Amz.SendNotify=1
EsfuerzoCorto3Amz.Volume=1
EsfuerzoCorto3Amz.MinDistance=1000
EsfuerzoCorto3Amz.MaxDistance=25000

EsfuerzoCorto4Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz5.wav', 'EsfuerzoCorto4Amz')
EsfuerzoCorto4Amz.SendNotify=1
EsfuerzoCorto4Amz.Volume=1
EsfuerzoCorto4Amz.MinDistance=1000
EsfuerzoCorto4Amz.MaxDistance=25000

EsfuerzoCorto5Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz6.wav', 'EsfuerzoCorto5Amz')
EsfuerzoCorto5Amz.SendNotify=1
EsfuerzoCorto5Amz.Volume=1
EsfuerzoCorto5Amz.MinDistance=1000
EsfuerzoCorto5Amz.MaxDistance=25000

EsfuerzoCorto6Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz3.wav', 'EsfuerzoCorto6Amz')   #PLAGUE: same as Corto2
EsfuerzoCorto6Amz.SendNotify=1
EsfuerzoCorto6Amz.Volume=1
EsfuerzoCorto6Amz.MinDistance=1000
EsfuerzoCorto6Amz.MaxDistance=25000


EsfuerzoGrandeAmz1=Bladex.CreateSound('../../sounds/esfuerzo-grande-Amz1.wav', 'EsfuerzoGrandeAmz1')
EsfuerzoGrandeAmz1.SendNotify=1
EsfuerzoGrandeAmz1.Volume=1
EsfuerzoGrandeAmz1.MinDistance=1000
EsfuerzoGrandeAmz1.MaxDistance=25000
EsfuerzoGrandeAmz2=Bladex.CreateSound('../../sounds/esfuerzo-grande-Amz2.wav', 'EsfuerzoGrandeAmz2')
EsfuerzoGrandeAmz2.SendNotify=1
EsfuerzoGrandeAmz2.Volume=1
EsfuerzoGrandeAmz2.MinDistance=1000
EsfuerzoGrandeAmz2.MaxDistance=25000

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
SesgadoLargoGrave.Volume=0.6

SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoAgudo.Volume=0.6

SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoLargoAgudo.Volume=0.6


SesgadoLento=Bladex.CreateSound('../../sounds/sesgado-lento.wav', 'SesgadoLento')
SesgadoLento.SendNotify=0
SesgadoLento.Volume=0.6

SesgadoLento2=Bladex.CreateSound('../../sounds/sesgado-lento2.wav', 'SesgadoLento2')
SesgadoLento2.SendNotify=0
SesgadoLento2.Volume=0.6

ConcBladeSword1=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword1')
ConcBladeSword1.SendNotify=0
ConcBladeSword1.Volume=1.0
ConcBladeSword1.Pitch=0.7
ConcBladeSword2=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword2')
ConcBladeSword2.SendNotify=0
ConcBladeSword2.Volume=1.0
ConcBladeSword2.Pitch=0.9

EsfuerzoGolpeFrontalAmz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz.wav', 'EsfuerzoGolpeFrontalAmz')
EsfuerzoGolpeFrontalAmz.SendNotify=1
EsfuerzoGolpeFrontalAmz.Volume=1
EsfuerzoGolpeFrontalAmz.MinDistance=1000
EsfuerzoGolpeFrontalAmz.MaxDistance=25000

EsfuerzoGolpeLateralAmz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz2.wav', 'EsfuerzoGolpeLateralAmz')
EsfuerzoGolpeLateralAmz.SendNotify=1
EsfuerzoGolpeLateralAmz.Volume=1
EsfuerzoGolpeLateralAmz.MinDistance=1000
EsfuerzoGolpeLateralAmz.MaxDistance=25000

EsfuerzoGolpeCabezaAmz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz3.wav', 'EsfuerzoGolpeCabezaAmz')
EsfuerzoGolpeCabezaAmz.SendNotify=1
EsfuerzoGolpeCabezaAmz.Volume=1
EsfuerzoGolpeCabezaAmz.MinDistance=1000
EsfuerzoGolpeCabezaAmz.MaxDistance=25000

EsfuerzoGolpeAtrasAmz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz4.wav', 'EsfuerzoGolpeAtrasAmz')
EsfuerzoGolpeAtrasAmz.SendNotify=1
EsfuerzoGolpeAtrasAmz.MinDistance=1000
EsfuerzoGolpeAtrasAmz.MaxDistance=25000

EsfuerzoAmzMediano=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz5.wav', 'EsfuerzoAmzMediano')
EsfuerzoAmzMediano.SendNotify=1
EsfuerzoAmzMediano.Volume=1
EsfuerzoAmzMediano.MinDistance=1000
EsfuerzoAmzMediano.MaxDistance=25000

EsfuerzoGolpeArribaAmz=Bladex.CreateSound('../../sounds/esfuerzo-largo-amz6.wav', 'EsfuerzoGolpeArribaAmz')
EsfuerzoGolpeArribaAmz.SendNotify=1
EsfuerzoGolpeArribaAmz.MinDistance=1000
EsfuerzoGolpeArribaAmz.MaxDistance=25000


EsfuerzoSubir1=Bladex.CreateSound('../../sounds/esfuerzo-subirAmz1.wav', 'EsfuerzoSubir1')
EsfuerzoSubir1.SendNotify=1
EsfuerzoSubir1.MinDistance=1000
EsfuerzoSubir1.MaxDistance=25000
EsfuerzoSubir2=Bladex.CreateSound('../../sounds/esfuerzo-subirAmz2.wav', 'EsfuerzoSubir2')
EsfuerzoSubir2.SendNotify=1
EsfuerzoSubir2.MinDistance=1000
EsfuerzoSubir2.MaxDistance=25000
EsfuerzoSubir3=Bladex.CreateSound('../../sounds/esfuerzo-subirAmz3.wav', 'EsfuerzoSubir3')
EsfuerzoSubir3.SendNotify=1
EsfuerzoSubir3.MinDistance=1000
EsfuerzoSubir3.MaxDistance=25000
EsfuerzoSubir4=Bladex.CreateSound('../../sounds/esfuerzo-subirAmz4.wav', 'EsfuerzoSubir4')
EsfuerzoSubir4.SendNotify=1
EsfuerzoSubir4.MinDistance=1000
EsfuerzoSubir4.MaxDistance=25000
EsfuerzoSubir5=Bladex.CreateSound('../../sounds/esfuerzo-subirAmz5.wav', 'EsfuerzoSubir5')
EsfuerzoSubir5.SendNotify=1
EsfuerzoSubir5.MinDistance=1000
EsfuerzoSubir5.MaxDistance=25000

EsfuerzoCaida1Amz=Bladex.CreateSound('../../sounds/esfuerzo-caida-amz.wav', 'EsfuerzoCaida1Amz')
EsfuerzoCaida1Amz.SendNotify=1
EsfuerzoCaida1Amz.MinDistance=1000
EsfuerzoCaida1Amz.MaxDistance=25000


MuerteQuemandoAmz1=Bladex.CreateSound('../../sounds/muerte-quemandoAmz1.wav', 'MuerteQuemandoAmz1')
MuerteQuemandoAmz1.SendNotify=0
MuerteAmz1=Bladex.CreateSound('../../sounds/muerte-amz1.wav', 'MuerteAmz1')
MuerteAmz1.SendNotify=0
MuerteAmz2=Bladex.CreateSound('../../sounds/Muerte-Amz2.wav', 'MuerteAmz2')
MuerteAmz2.SendNotify=0
MuerteAmz3=Bladex.CreateSound('../../sounds/Muerte-Amz3.wav', 'MuerteAmz3')
MuerteAmz3.SendNotify=0
MuerteAmz4=Bladex.CreateSound('../../sounds/muerte-amz1.wav', 'MuerteAmz4')
MuerteAmz4.SendNotify=0
MuerteAmz5=Bladex.CreateSound('../../sounds/Muerte-Amz2.wav', 'MuerteAmz5')
MuerteAmz5.SendNotify=0
MuerteAmz6=Bladex.CreateSound('../../sounds/Muerte-Amz3.wav', 'MuerteAmz6')
MuerteAmz6.SendNotify=0
MuerteAmz7=Bladex.CreateSound('../../sounds/muerte-amz1.wav', 'MuerteAmz7')
MuerteAmz7.SendNotify=0
HeridaAmz1=Bladex.CreateSound('../../sounds/herida-amz1.wav', 'HeridaAmz1')
HeridaAmz1.SendNotify=0
HeridaAmz2=Bladex.CreateSound('../../sounds/herida-amz2.wav', 'HeridaAmz2')
HeridaAmz2.SendNotify=0
HeridaAmz3=Bladex.CreateSound('../../sounds/herida-amz3.wav', 'HeridaAmz3')
HeridaAmz3.SendNotify=0
HeridaAmz4=Bladex.CreateSound('../../sounds/herida-amz4.wav', 'HeridaAmz4')
HeridaAmz4.SendNotify=0

DesangreAmz1=Bladex.CreateSound('../../sounds/desangre1.wav', 'DesangreAmz1')
DesangreAmz1.SendNotify=0
DesangreAmz1.Volume=0.8
DesangreAmz2=Bladex.CreateSound('../../sounds/desangre2.wav', 'DesangreAmz2')
DesangreAmz2.SendNotify=0
DesangreAmz2.Volume=0.8

AndarAmz1=Bladex.CreateSound('../../sounds/Mov-amazona-1.wav', 'AndarAmz1')
AndarAmz1.SendNotify=0
AndarAmz1.Volume=0.3
AndarAmz2=Bladex.CreateSound('../../sounds/Mov-Amazona-2.wav', 'AndarAmz2')
AndarAmz2.SendNotify=0
AndarAmz2.Volume=0.3


CaidaAmz1=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaAmz1')
CaidaAmz1.SendNotify=1
CaidaAmz1.Volume=1
CaidaAmz2=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaAmz2')
CaidaAmz2.SendNotify=1
CaidaAmz2.Volume=1
CaidaAmz3=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaAmz3')
CaidaAmz3.SendNotify=1
CaidaAmz3.Volume=0.5
CaidaAmz4=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaAmz4')
CaidaAmz4.SendNotify=1
CaidaAmz4.Volume=0.5

CaidaDerrapeAmz1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaDerrapeAmz1')
CaidaDerrapeAmz1.SendNotify=1
CaidaDerrapeAmz1.Volume=1

CansancioAmz=Bladex.CreateSound('../../sounds/cansancioAmz.wav', 'CansancioAmz')
CansancioAmz.SendNotify=1
CansancioAmz.Volume=1

MuerteSaltoVacioAmz1=Bladex.CreateSound('../../sounds/salto-vacio-final-Amz.wav', 'MuerteSaltoVacioAmz1')
MuerteSaltoVacioAmz1.SendNotify=1
MuerteSaltoVacioAmz1.Volume=1
MuerteSaltoVacioAmz1.MinDistance=1000
MuerteSaltoVacioAmz1.MaxDistance=25000
MuerteSaltoVacioAmz2=Bladex.CreateSound('../../sounds/salto-vacio-Amz.wav', 'MuerteSaltoVacioAmz2')
MuerteSaltoVacioAmz2.SendNotify=1
MuerteSaltoVacioAmz2.Volume=1
MuerteSaltoVacioAmz2.MinDistance=1000
MuerteSaltoVacioAmz2.MaxDistance=25000

MuerteAplastamientoAmz1=Bladex.CreateSound('../../sounds/aplastamiento.wav', 'MuerteAplastamientoAmz1')
MuerteAplastamientoAmz1.SendNotify=1
MuerteAplastamientoAmz1.Volume=1
MuerteAplastamientoAmz1.MinDistance=1000
MuerteAplastamientoAmz1.MaxDistance=25000

EsfuerzoCorto7Amz=Bladex.CreateSound('../../sounds/esfuerzo-corto-amz7.wav', 'EsfuerzoCorto7Amz')
EsfuerzoCorto7Amz.SendNotify=1
EsfuerzoCorto7Amz.Volume=1
EsfuerzoCorto7Amz.MinDistance=1000
EsfuerzoCorto7Amz.MaxDistance=25000

AtaquesEspecialesAmz1=Bladex.CreateSound('../../sounds/sesgado-especial-largo.wav', 'AtaquesEspecialesAmz1')
AtaquesEspecialesAmz1.SendNotify=1
AtaquesEspecialesAmz1.Volume=1.0
AtaquesEspecialesAmz1.MinDistance=1000
AtaquesEspecialesAmz1.MaxDistance=15000
AtaquesEspecialesAmz2=Bladex.CreateSound('../../sounds/sesgado-especial-largo2.wav', 'AtaquesEspecialesAmz2')
AtaquesEspecialesAmz2.SendNotify=1
AtaquesEspecialesAmz2.Volume=1.0
AtaquesEspecialesAmz2.MinDistance=1000
AtaquesEspecialesAmz2.MaxDistance=15000
AtaquesEspecialesAmz3=Bladex.CreateSound('../../sounds/sesgado-especial-corto.wav', 'AtaquesEspecialesAmz3')
AtaquesEspecialesAmz3.SendNotify=1
AtaquesEspecialesAmz3.Volume=1.0
AtaquesEspecialesAmz3.MinDistance=1000
AtaquesEspecialesAmz3.MaxDistance=15000
AtaquesEspecialesAmz4=Bladex.CreateSound('../../sounds/sesgado-especial-corto2.wav', 'AtaquesEspecialesAmz4')
AtaquesEspecialesAmz4.SendNotify=1
AtaquesEspecialesAmz4.Volume=1.0
AtaquesEspecialesAmz4.MinDistance=1000
AtaquesEspecialesAmz4.MaxDistance=15000

### Below added for Fire Bo -LeadHead

AtaqueFuego4=Bladex.CreateSound('../../sounds/fuego-ascende.wav', 'AtaqueFuego4')
AtaqueFuego4.SendNotify=1
AtaqueFuego4.Volume=1.0
AtaqueFuego4.MinDistance=3000
AtaqueFuego4.MaxDistance=15000


print "Sonidos para la amazona creados..."
