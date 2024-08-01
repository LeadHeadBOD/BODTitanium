##///
##||| ANISOUNDBARX.PY TITANIUM
##||| Change list:
##||| * Normalized "draw weapon" sound for all 4 characters.
##||| * 
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************

CogerLlave=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerLlave')
CogerLlave.SendNotify=0

RuidoLlaveCerradura=Bladex.CreateSound('../../sounds/unlock-door3.wav', 'RuidoLlaveCerradura')
RuidoLlaveCerradura.SendNotify=0

Ruidook=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'Ruidook')
Ruidook.SendNotify=0

SonidoPalanca=Bladex.CreateSound('../../sounds/lever2.wav', 'SonidoPalanca')
SonidoPalanca.SendNotify=0

SonidoVaciarBotella=Bladex.CreateSound('../../sounds/agua-fuente-sobre-agua.wav', 'SonidoVaciarBotella')
SonidoVaciarBotella.SendNotify=0

GolpeArmaEscudoBarb=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoBarb')
GolpeArmaEscudoBarb.SendNotify=1
GolpeArmaEscudoBarb.MinDistance=3000
GolpeArmaEscudoBarb.MaxDistance=6000

GolpeArmaArmaBarb=Bladex.CreateSound('../../sounds/golpe-arma-arma.wav', 'GolpeArmaArmaBarb')
GolpeArmaArmaBarb.SendNotify=1
GolpeArmaArmaBarb.MinDistance=3000
GolpeArmaArmaBarb.MaxDistance=6000

TajoEmpalanteBarb=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalanteBarb')
TajoEmpalanteBarb.SendNotify=0

TajoCortanteBarb=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortanteBarb')
TajoCortanteBarb.SendNotify=0

TajoMutilacionBarb=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionBarb')
TajoMutilacionBarb.SendNotify=0

GolpeContundenteBarb=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundenteBarb')
GolpeContundenteBarb.SendNotify=0


Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')                     # PLAGUE: wtf, all 4 characters use the same sound, but all of them have different parameters.
Enfundar.SendNotify=1                                                                            # Normalized across all characters, I guess
Enfundar.MinDistance=2000                                                                        #
Enfundar.MaxDistance=4000                                                                        #                   -LeadHead
Enfundar.Volume=0.8


CogerArma=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerArma')
CogerArma.SendNotify=0

CambiarEscudo=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CambiarEscudo')
CambiarEscudo.SendNotify=0

CogerEspada=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CogerEspada')
CogerEspada.SendNotify=0

GolpeMaza=Bladex.CreateSound('../../sounds/golpe-breast.wav', 'GolpeMaza')
GolpeMaza.SendNotify=1
GolpeMaza.Volume=0.6
GolpeMaza.MinDistance=3000
GolpeMaza.MaxDistance=6000

DesangreBarb1=Bladex.CreateSound('../../sounds/desangre1.wav', 'DesangreBarb1')
DesangreBarb1.SendNotify=0
DesangreBarb1.Volume=0.6
DesangreBarb2=Bladex.CreateSound('../../sounds/desangre3.wav', 'DesangreBarb2')
DesangreBarb2.SendNotify=0
DesangreBarb2.Volume=0.6


EsfuerzoCortoBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_7.wav', 'EsfuerzoCortoBarb')
EsfuerzoCortoBarb.SendNotify=1
EsfuerzoCortoBarb.Volume=1
EsfuerzoCortoBarb.MinDistance=3000
EsfuerzoCortoBarb.MaxDistance=6000

EsfuerzoCorto1Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_1.wav', 'EsfuerzoCorto1Barb')
EsfuerzoCorto1Barb.SendNotify=1
EsfuerzoCorto1Barb.Volume=1
EsfuerzoCorto1Barb.MinDistance=3000
EsfuerzoCorto1Barb.MaxDistance=6000

EsfuerzoCorto2Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_2.wav', 'EsfuerzoCorto2Barb')
EsfuerzoCorto2Barb.SendNotify=1
EsfuerzoCorto2Barb.Volume=1
EsfuerzoCorto2Barb.MinDistance=3000
EsfuerzoCorto2Barb.MaxDistance=6000

EsfuerzoCorto3Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_3.wav', 'EsfuerzoCorto3Barb')
EsfuerzoCorto3Barb.SendNotify=1
EsfuerzoCorto3Barb.Volume=1
EsfuerzoCorto3Barb.MinDistance=3000
EsfuerzoCorto3Barb.MaxDistance=6000

EsfuerzoCorto4Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_4.wav', 'EsfuerzoCorto4Barb')
EsfuerzoCorto4Barb.SendNotify=1
EsfuerzoCorto4Barb.Volume=1
EsfuerzoCorto4Barb.MinDistance=3000
EsfuerzoCorto4Barb.MaxDistance=6000

EsfuerzoCorto5Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_5.wav', 'EsfuerzoCorto5Barb')
EsfuerzoCorto5Barb.SendNotify=1
EsfuerzoCorto5Barb.Volume=1
EsfuerzoCorto5Barb.MinDistance=3000
EsfuerzoCorto5Barb.MaxDistance=6000

EsfuerzoCorto6Barb=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_6.wav', 'EsfuerzoCorto6Barb')
EsfuerzoCorto6Barb.SendNotify=1
EsfuerzoCorto6Barb.Volume=1
EsfuerzoCorto6Barb.MinDistance=3000
EsfuerzoCorto6Barb.MaxDistance=6000

GritoHerida=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_7.wav', 'GritoHerida')
GritoHerida.SendNotify=1
GritoHerida.Volume=0.8
GritoHerida.MinDistance=3000
GritoHerida.MaxDistance=6000

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

SesgadoLentoBarb=Bladex.CreateSound('../../sounds/sesgado-lento2.wav', 'SesgadoLentoBarb')
SesgadoLentoBarb.SendNotify=0
SesgadoLentoBarb.Volume=0.6

EsfuerzoGolpeFrontalBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo1.wav', 'EsfuerzoGolpeFrontalBarb')
EsfuerzoGolpeFrontalBarb.SendNotify=1
EsfuerzoGolpeFrontalBarb.Volume=1
EsfuerzoGolpeFrontalBarb.MinDistance=3000
EsfuerzoGolpeFrontalBarb.MaxDistance=6000

EsfuerzoGolpeLateralBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo2.wav', 'EsfuerzoGolpeLateralBarb')
EsfuerzoGolpeLateralBarb.SendNotify=1
EsfuerzoGolpeLateralBarb.Volume=1
EsfuerzoGolpeLateralBarb.MinDistance=3000
EsfuerzoGolpeLateralBarb.MaxDistance=6000

EsfuerzoGolpeCabezaBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo3.wav', 'EsfuerzoGolpeCabezaBarb')
EsfuerzoGolpeCabezaBarb.SendNotify=1
EsfuerzoGolpeCabezaBarb.Volume=1
EsfuerzoGolpeCabezaBarb.MinDistance=3000
EsfuerzoGolpeCabezaBarb.MaxDistance=6000

EsfuerzoGolpeAtrasBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo4.wav', 'EsfuerzoGolpeAtrasBarb')
EsfuerzoGolpeAtrasBarb.SendNotify=1
EsfuerzoGolpeAtrasBarb.Volume=1
EsfuerzoGolpeAtrasBarb.MinDistance=3000
EsfuerzoGolpeAtrasBarb.MaxDistance=6000

EsfuerzoBarbMediano=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo5.wav', 'EsfuerzoBarbMediano')
EsfuerzoBarbMediano.SendNotify=1
EsfuerzoBarbMediano.Volume=1
EsfuerzoBarbMediano.MinDistance=3000
EsfuerzoBarbMediano.MaxDistance=6000

EsfuerzoGolpeArribaBarb=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo6.wav', 'EsfuerzoGolpeArribaBarb')
EsfuerzoGolpeArribaBarb.SendNotify=1
EsfuerzoGolpeArribaBarb.Volume=1
EsfuerzoGolpeArribaBarb.MinDistance=3000
EsfuerzoGolpeArribaBarb.MaxDistance=6000

EsfuerzoSubir=Bladex.CreateSound('../../sounds/esfuerzo-subirBarb1.wav', 'EsfuerzoSubir')
EsfuerzoSubir.SendNotify=1
EsfuerzoSubir.Volume=1
EsfuerzoSubir.MinDistance=3000
EsfuerzoSubir.MaxDistance=6000
EsfuerzoSubir1=Bladex.CreateSound('../../sounds/esfuerzo-subirBarb2.wav', 'EsfuerzoSubir1')
EsfuerzoSubir1.SendNotify=1
EsfuerzoSubir1.Volume=1
EsfuerzoSubir1.MinDistance=3000
EsfuerzoSubir1.MaxDistance=6000
EsfuerzoSubir2=Bladex.CreateSound('../../sounds/esfuerzo-subirBarb3.wav', 'EsfuerzoSubir2')
EsfuerzoSubir2.SendNotify=1
EsfuerzoSubir2.Volume=1
EsfuerzoSubir2.MinDistance=3000
EsfuerzoSubir2.MaxDistance=6000
EsfuerzoSubir3=Bladex.CreateSound('../../sounds/esfuerzo-subirBarb4.wav', 'EsfuerzoSubir3')
EsfuerzoSubir3.SendNotify=1
EsfuerzoSubir3.Volume=1
EsfuerzoSubir3.MinDistance=3000
EsfuerzoSubir3.MaxDistance=6000

EsfuerzoTonto=Bladex.CreateSound('../../sounds/esfuerzotontoBarb.wav', 'EsfuerzoTonto')
EsfuerzoTonto.SendNotify=1
EsfuerzoTonto.Volume=1
EsfuerzoTonto.MinDistance=3000
EsfuerzoTonto.MaxDistance=6000


MuerteBarb1=Bladex.CreateSound('../../sounds/muerte-barb-1.wav', 'MuerteBarb1')
#MuerteBarb1.SendNotify=0
MuerteBarb1.Volume=0.5
MuerteBarb2=Bladex.CreateSound('../../sounds/muerte-barb-2.wav', 'MuerteBarb2')
#MuerteBarb2.SendNotify=0
MuerteBarb2.Volume=0.5
MuerteBarb3=Bladex.CreateSound('../../sounds/muerte-barb-3.wav', 'MuerteBarb3')
#MuerteBarb3.SendNotify=0
MuerteBarb3.Volume=0.5
MuerteBarb4=Bladex.CreateSound('../../sounds/muerte-barb-2.wav', 'MuerteBarb4')
#MuerteBarb4.SendNotify=0
HeridaBarb1=Bladex.CreateSound('../../sounds/herida_barb_1.wav', 'HeridaBarb1')
#HeridaBarb1.SendNotify=0
HeridaBarb1.Volume=0.5
HeridaBarb2=Bladex.CreateSound('../../sounds/herida_barb_2.wav', 'HeridaBarb2')
#HeridaBarb2.SendNotify=0
HeridaBarb2.Volume=0.5
HeridaBarb3=Bladex.CreateSound('../../sounds/herida_barb_3.wav', 'HeridaBarb3')
#HeridaBarb3.SendNotify=0
HeridaBarb3.Volume=0.5

Saltovacio=Bladex.CreateSound('../../sounds/salto-vacio-barb.wav', 'Saltovacio')
Saltovacio.SendNotify=0

Roce1=Bladex.CreateSound('../../sounds/mov.barbaro-1.wav', 'Roce1')
Roce1.SendNotify=0
Roce1.Volume=0.1
Roce2=Bladex.CreateSound('../../sounds/mov.barbaro-2.wav', 'Roce2')
Roce2.SendNotify=0
Roce2.Volume=0.1
Roce3=Bladex.CreateSound('../../sounds/mov.barbaro-3.wav', 'Roce3')
Roce3.SendNotify=0
Roce3.Volume=0.1
Roce4=Bladex.CreateSound('../../sounds/mov.barbaro-11.wav', 'Roce4')
Roce4.SendNotify=0
Roce4.Volume=0.1
Roce5=Bladex.CreateSound('../../sounds/mov.barbaro-22.wav', 'Roce5')
Roce5.SendNotify=0
Roce5.Volume=0.1
Roce6=Bladex.CreateSound('../../sounds/mov.barbaro-33.wav', 'Roce6')
Roce6.SendNotify=0
Roce6.Volume=0.1
Roce7=Bladex.CreateSound('../../sounds/mov.barbaro-rapido-1.wav', 'Roce7')
Roce7.SendNotify=0
Roce7.Volume=0.1
Roce8=Bladex.CreateSound('../../sounds/mov.barbaro-rapido-2.wav', 'Roce8')
Roce8.SendNotify=0
Roce8.Volume=0.1

Caida1=Bladex.CreateSound('../../sounds/caida-pie.wav', 'Caida1')
Caida1.SendNotify=1
Caida1.Volume=0.8
Caida1.MinDistance=3000
Caida1.MaxDistance=6000

Caida2=Bladex.CreateSound('../../sounds/caida-mano.wav', 'Caida2')
Caida2.SendNotify=1
Caida2.Volume=0.8
Caida2.MinDistance=3000
Caida2.MaxDistance=6000

Caida3=Bladex.CreateSound('../../sounds/caida-pie.wav', 'Caida3')   # PLAGUE: same as 1
Caida3.SendNotify=1
Caida3.Volume=0.8
Caida3.MinDistance=3000
Caida3.MaxDistance=6000

Caida4=Bladex.CreateSound('../../sounds/caida-mano.wav', 'Caida4')  # PLAGUE: same as 2
Caida4.SendNotify=1
Caida4.Volume=0.8
Caida4.MinDistance=3000
Caida4.MaxDistance=6000

CansancioBarb=Bladex.CreateSound('../../sounds/cansancioBarb.wav', 'CansancioBarb')
CansancioBarb.SendNotify=1
CansancioBarb.Volume=0.5
CansancioBarb.MinDistance=3000
CansancioBarb.MaxDistance=6000

MuerteSaltoVacioBar1=Bladex.CreateSound('../../sounds/salto-vacio-Barb.wav', 'MuerteSaltoVacioBar1')
MuerteSaltoVacioBar1.SendNotify=1
MuerteSaltoVacioBar1.Volume=0.5
MuerteSaltoVacioBar1.MinDistance=3000
MuerteSaltoVacioBar1.MaxDistance=6000


MuerteSaltoVacioBar2=Bladex.CreateSound('../../sounds/muerte-caida-final-barb.wav', 'MuerteSaltoVacioBar2')
MuerteSaltoVacioBar2.SendNotify=1
MuerteSaltoVacioBar2.Volume=0.5
MuerteSaltoVacioBar2.MinDistance=3000
MuerteSaltoVacioBar2.MaxDistance=6000


MuerteQuemandoBar1=Bladex.CreateSound('../../sounds/muerte-quemando-barb.wav', 'MuerteQuemandoBar1')
MuerteQuemandoBar1.SendNotify=1
MuerteQuemandoBar1.Volume=0.5
MuerteQuemandoBar1.MinDistance=3000
MuerteQuemandoBar1.MaxDistance=6000


MuerteAplastamientoBarb1=Bladex.CreateSound('../../sounds/aplastamiento.wav', 'MuerteAplastamientoBarb1')
MuerteAplastamientoBarb1.SendNotify=1
MuerteAplastamientoBarb1.Volume=1
MuerteAplastamientoBarb1.MinDistance=1000
MuerteAplastamientoBarb1.MaxDistance=25000


EsfuerzoEsquiva1=Bladex.CreateSound('../../sounds/Esfuerzo-esquiva-Barb1.wav', 'EsfuerzoEsquiva1')
EsfuerzoEsquiva1.SendNotify=1
EsfuerzoEsquiva1.Volume=0.5
EsfuerzoEsquiva1.MinDistance=3000
EsfuerzoEsquiva1.MaxDistance=6000
EsfuerzoEsquiva2=Bladex.CreateSound('../../sounds/Esfuerzo-esquiva-Barb2.wav', 'EsfuerzoEsquiva2')
EsfuerzoEsquiva2.SendNotify=1
EsfuerzoEsquiva2.Volume=0.5
EsfuerzoEsquiva2.MinDistance=3000
EsfuerzoEsquiva2.MaxDistance=6000

ConcBladeSword1=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword1')
ConcBladeSword1.SendNotify=0
ConcBladeSword1.Volume=1.0
ConcBladeSword1.Pitch=0.7
ConcBladeSword2=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword2')
ConcBladeSword2.SendNotify=0
ConcBladeSword2.Volume=1.0
ConcBladeSword2.Pitch=0.9

AtaquesEspeciales1=Bladex.CreateSound('../../sounds/sesgado-especial-largo.wav', 'AtaquesEspeciales1')
AtaquesEspeciales1.SendNotify=1
AtaquesEspeciales1.Volume=1.0
AtaquesEspeciales1.MinDistance=3000
AtaquesEspeciales1.MaxDistance=15000
AtaquesEspeciales2=Bladex.CreateSound('../../sounds/sesgado-especial-largo2.wav', 'AtaquesEspeciales2')
AtaquesEspeciales2.SendNotify=1
AtaquesEspeciales2.Volume=1.0
AtaquesEspeciales2.MinDistance=3000
AtaquesEspeciales2.MaxDistance=15000
AtaquesEspeciales3=Bladex.CreateSound('../../sounds/sesgado-especial-corto.wav', 'AtaquesEspeciales3')
AtaquesEspeciales3.SendNotify=1
AtaquesEspeciales3.Volume=1.0
AtaquesEspeciales3.MinDistance=3000
AtaquesEspeciales3.MaxDistance=15000
AtaquesEspeciales4=Bladex.CreateSound('../../sounds/sesgado-especial-corto2.wav', 'AtaquesEspeciales4')
AtaquesEspeciales4.SendNotify=1
AtaquesEspeciales4.Volume=1.0
AtaquesEspeciales4.MinDistance=3000
AtaquesEspeciales4.MaxDistance=15000

EsfuerzosEspeciales1=Bladex.CreateSound('../../sounds/esfuerzos_barb_largo3.wav', 'EsfuerzosEspeciales1')
EsfuerzosEspeciales1.SendNotify=1
EsfuerzosEspeciales1.Volume=1.0
EsfuerzosEspeciales1.MinDistance=3000
EsfuerzosEspeciales1.MaxDistance=15000
EsfuerzosEspeciales2=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_2.wav', 'EsfuerzosEspeciales2')
EsfuerzosEspeciales2.SendNotify=1
EsfuerzosEspeciales2.Volume=1.0
EsfuerzosEspeciales2.MinDistance=3000
EsfuerzosEspeciales2.MaxDistance=15000
EsfuerzosEspeciales3=Bladex.CreateSound('../../sounds/esfuerzos_barb_corto_4.wav', 'EsfuerzosEspeciales3')
EsfuerzosEspeciales3.SendNotify=1
EsfuerzosEspeciales3.Volume=1.0
EsfuerzosEspeciales3.MinDistance=3000
EsfuerzosEspeciales3.MaxDistance=15000

AtaqueFuego1=Bladex.CreateSound('../../sounds/Fireball-Fire.wav', 'AtaqueFuego1')
AtaqueFuego1.SendNotify=1
AtaqueFuego1.Volume=1.0
AtaqueFuego1.MinDistance=3000
AtaqueFuego1.MaxDistance=15000
AtaqueFuego2=Bladex.CreateSound('../../sounds/fireball-swing.wav', 'AtaqueFuego2')
AtaqueFuego2.SendNotify=1
AtaqueFuego2.Volume=1.0
AtaqueFuego2.MinDistance=3000
AtaqueFuego2.MaxDistance=15000
AtaqueFuego3=Bladex.CreateSound('../../sounds/fireball-impact.wav', 'AtaqueFuego3')
AtaqueFuego3.SendNotify=1
AtaqueFuego3.Volume=1.0
AtaqueFuego3.MinDistance=3000
AtaqueFuego3.MaxDistance=15000
AtaqueFuego4=Bladex.CreateSound('../../sounds/fuego-ascende.wav', 'AtaqueFuego4')
AtaqueFuego4.SendNotify=1
AtaqueFuego4.Volume=1.0
AtaqueFuego4.MinDistance=3000
AtaqueFuego4.MaxDistance=15000


print "Sonidos para el Barbaro creados..."
