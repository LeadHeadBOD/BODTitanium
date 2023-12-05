##///
##||| ANISOUNDKGTX.PY TITANIUM
##||| Change list:
##||| * Commented out duplicate entries.
##||| * Normalized "draw weapon" sound for all 4 characters.
##||| * PLAGUE: Lots of sound variable names are still named after Barbarian. This will innevitably cause problems.
##||| 
##\\\ 


import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************
CogerLlave=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerLlave')
CogerLlave.SendNotify=0

SonidoPalanca=Bladex.CreateSound('../../sounds/lever2.wav', 'SonidoPalanca')
SonidoPalanca.SendNotify=0

RuidoLlaveCerradura=Bladex.CreateSound('../../sounds/unlock-door3.wav', 'RuidoLlaveCerradura')
RuidoLlaveCerradura.SendNotify=1
RuidoLlaveCerradura.Volume=1
RuidoLlaveCerradura.MinDistance=1000
RuidoLlaveCerradura.MaxDistance=25000

RuidoLlave=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'RuidoLlave')
RuidoLlave.SendNotify=0

Ruidook=Bladex.CreateSound('../../sounds/Manipulado-llave2.wav', 'Ruidook')         # PLAGUE: It's identical to above????
Ruidook.SendNotify=0

SonidoVaciarBotella=Bladex.CreateSound('../../sounds/agua-fuente-sobre-agua.wav', 'SonidoVaciarBotella')
SonidoVaciarBotella.SendNotify=0

GolpeArmaEscudo=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudo')
GolpeArmaEscudo.SendNotify=1
GolpeArmaEscudo.MinDistance=6000
GolpeArmaEscudo.MaxDistance=10000

GolpeArmaArma=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArma')
GolpeArmaArma.SendNotify=1
GolpeArmaArma.MinDistance=6000
GolpeArmaArma.MaxDistance=10000

GolpeContundente=Bladex.CreateSound('../../sounds/golpe-maza-carne.wav', 'GolpeContundente')
GolpeContundente.SendNotify=1
GolpeContundente.MinDistance=6000
GolpeContundente.MaxDistance=10000

TajoEmpalante=Bladex.CreateSound('../../sounds/corte-carne.wav', 'TajoEmpalante')
TajoEmpalante.SendNotify=0
TajoCortante=Bladex.CreateSound('../../sounds/corte-carne-2.wav', 'TajoCortante')
#TajoCortante.SendNotify=0
TajoMutilacion=Bladex.CreateSound('../../sounds/mutilacion4-44.wav', 'TajoMutilacion')
#TajoMutilacion.SendNotify=0
CogerEspada=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CogerEspada')
CogerEspada.SendNotify=0
CogerArma=Bladex.CreateSound('../../sounds/M-guardar.wav', 'CogerArma')
CogerArma.SendNotify=0
CambiarEscudo=Bladex.CreateSound('../../sounds/M-ARMA-U-OBJETO.wav', 'CambiarEscudo')
CambiarEscudo.SendNotify=0

Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')                                      # PLAGUE: wtf, all 4 characters use the same sound, but all of them have different parameters.
Enfundar.SendNotify=1                                                                                             # Normalized across all characters, I guess
Enfundar.Volume=0.8                                                                                               #
Enfundar.MinDistance=2000                                                                                         #                   -LeadHead
Enfundar.MaxDistance=4000

EsfuerzoEspecialKgt2=Bladex.CreateSound('../../sounds/esfuerzo-caballero-especial1.wav', 'EsfuerzoEspecialKgt2') #PLAGUE: Duplicated later down
EsfuerzoEspecialKgt2.SendNotify=1
EsfuerzoEspecialKgt2.Volume=1
EsfuerzoEspecialKgt2.MinDistance=1000
EsfuerzoEspecialKgt2.MaxDistance=25000

EsfuerzoCortoBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero7.wav', 'EsfuerzoCortoBarbaro')
EsfuerzoCortoBarb.SendNotify=1
EsfuerzoCortoBarb.Volume=0.8
EsfuerzoCortoBarb.MinDistance=1000
EsfuerzoCortoBarb.MaxDistance=25000

EsfuerzoCorto1Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero1.wav', 'EsfuerzoCorto1Barbaro')
EsfuerzoCorto1Barb.SendNotify=1
EsfuerzoCorto1Barb.Volume=0.8
EsfuerzoCorto1Barb.MinDistance=1000
EsfuerzoCorto1Barb.MaxDistance=25000

EsfuerzoCorto2Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero2.wav', 'EsfuerzoCorto2Barbaro')
EsfuerzoCorto2Barb.SendNotify=1
EsfuerzoCorto2Barb.Volume=0.8
EsfuerzoCorto2Barb.MinDistance=1000
EsfuerzoCorto2Barb.MaxDistance=25000

EsfuerzoCorto3Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero3.wav', 'EsfuerzoCorto3Barbaro')
EsfuerzoCorto3Barb.SendNotify=1
EsfuerzoCorto3Barb.Volume=0.8
EsfuerzoCorto3Barb.MinDistance=1000
EsfuerzoCorto3Barb.MaxDistance=25000

EsfuerzoCorto4Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero4.wav', 'EsfuerzoCorto4Barbaro')
EsfuerzoCorto4Barb.SendNotify=1
EsfuerzoCorto4Barb.Volume=0.8
EsfuerzoCorto4Barb.MinDistance=1000
EsfuerzoCorto4Barb.MaxDistance=25000

EsfuerzoCorto5Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero5.wav', 'EsfuerzoCorto5Barbaro')
EsfuerzoCorto5Barb.SendNotify=1
EsfuerzoCorto5Barb.Volume=0.8
EsfuerzoCorto5Barb.MinDistance=1000
EsfuerzoCorto5Barb.MaxDistance=25000

EsfuerzoCorto6Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero6.wav', 'EsfuerzoCorto6Barbaro')
EsfuerzoCorto6Barb.SendNotify=1
EsfuerzoCorto6Barb.Volume=0.8
EsfuerzoCorto6Barb.MinDistance=1000
EsfuerzoCorto6Barb.MaxDistance=25000

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
SesgadoLargoGrave.Volume=0.4
SesgadoCortoAgudo=Bladex.CreateSound('../../sounds/sesgado-corto-agudo.wav', 'SesgadoCortoAgudo')
SesgadoCortoAgudo.SendNotify=0
SesgadoCortoAgudo.Volume=0.8
SesgadoLargoAgudo=Bladex.CreateSound('../../sounds/sesgado-largo-agudo.wav', 'SesgadoLargoAgudo')
SesgadoLargoAgudo.SendNotify=0
SesgadoLargoAgudo.Volume=0.6
SesgadoLento=Bladex.CreateSound('../../sounds/sesgado-lento2.wav', 'SesgadoLento')
SesgadoLento.SendNotify=0
SesgadoLento.Volume=0.6

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

SesgadoLava2=Bladex.CreateSound('../../sounds/Sesgado-lava2.wav', 'SesgadoLava2')
SesgadoLava2.SendNotify=0
SesgadoLava2.Volume=1.0

ConcBladeSword1=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword1')
ConcBladeSword1.SendNotify=0
ConcBladeSword1.Volume=1.0
ConcBladeSword1.Pitch=0.7
ConcBladeSword2=Bladex.CreateSound('../../sounds/aparicion-escudo.wav', 'ConcBladeSword2')
ConcBladeSword2.SendNotify=0
ConcBladeSword2.Volume=1.0
ConcBladeSword2.Pitch=0.9

EsfuerzoGolpeFrontalBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo.wav', 'EsfuerzoGolpeFrontalBarbaro')
EsfuerzoGolpeFrontalBarb.SendNotify=1
EsfuerzoGolpeFrontalBarb.Volume=0.7
EsfuerzoGolpeFrontalBarb.MinDistance=1000
EsfuerzoGolpeFrontalBarb.MaxDistance=25000

EsfuerzoGolpeLateralBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo.wav', 'EsfuerzoGolpeLateralBarbaro')
EsfuerzoGolpeLateralBarb.SendNotify=1
EsfuerzoGolpeLateralBarb.MinDistance=1000
EsfuerzoGolpeLateralBarb.MaxDistance=25000

EsfuerzoGolpeLateralDchBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo2.wav', 'EsfuerzoGolpeLateralDchBarbaro')
EsfuerzoGolpeLateralDchBarb.SendNotify=1
EsfuerzoGolpeLateralDchBarb.MinDistance=1000
EsfuerzoGolpeLateralDchBarb.MaxDistance=25000

EsfuerzoGolpeCabezaBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo3.wav', 'EsfuerzoGolpeCabezaBarbaro')
EsfuerzoGolpeCabezaBarb.SendNotify=1
EsfuerzoGolpeCabezaBarb.MinDistance=1000
EsfuerzoGolpeCabezaBarb.MaxDistance=25000

EsfuerzoGolpeAtrasBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo4.wav', 'EsfuerzoGolpeAtrasBarbaro')
EsfuerzoGolpeAtrasBarb.SendNotify=1
EsfuerzoGolpeAtrasBarb.MinDistance=1000
EsfuerzoGolpeAtrasBarb.MaxDistance=25000

# VOLUMEN EMPUJON
EsfuerzoGolpeAtras1Barb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo5.wav', 'EsfuerzoGolpeAtras1Barbaro')
EsfuerzoGolpeAtras1Barb.Volume=0.7
EsfuerzoGolpeAtras1Barb.MinDistance=1000
EsfuerzoGolpeAtras1Barb.MaxDistance=25000

EsfuerzoBarbMediano=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo6.wav', 'EsfuerzoBarbaroMediano')
EsfuerzoBarbMediano.SendNotify=1
EsfuerzoBarbMediano.MinDistance=1000
EsfuerzoBarbMediano.MaxDistance=25000

EsfuerzoBarbLargo=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo3.wav', 'EsfuerzoBarbaroLargo')
EsfuerzoBarbLargo.SendNotify=1
EsfuerzoBarbLargo.MinDistance=1000
EsfuerzoBarbLargo.MaxDistance=25000

EsfuerzoGolpeArribaBarb=Bladex.CreateSound('../../sounds/esfuerzo-caballero-largo2.wav', 'EsfuerzoGolpeArribaBarbaro')
EsfuerzoGolpeArribaBarb.SendNotify=1
EsfuerzoGolpeArribaBarb.MinDistance=1000
EsfuerzoGolpeArribaBarb.MaxDistance=25000

EsfuerzoPesadoKgt=Bladex.CreateSound('../../sounds/esfuerzo-pesadoKgt.wav', 'EsfuerzoPesadoKgt')
EsfuerzoPesadoKgt.SendNotify=1
EsfuerzoPesadoKgt.MinDistance=1000
EsfuerzoPesadoKgt.MaxDistance=25000
EsfuerzoPesadoKgt1=Bladex.CreateSound('../../sounds/esfuerzo-pesadoKgt1.wav', 'EsfuerzoPesadoKgt1')
EsfuerzoPesadoKgt1.SendNotify=1
EsfuerzoPesadoKgt1.MinDistance=1000
EsfuerzoPesadoKgt1.MaxDistance=25000
EsfuerzoPesadoKgt2=Bladex.CreateSound('../../sounds/esfuerzo-pesadoKgt2.wav', 'EsfuerzoPesadoKgt2')
EsfuerzoPesadoKgt2.SendNotify=1
EsfuerzoPesadoKgt2.MinDistance=1000
EsfuerzoPesadoKgt2.MaxDistance=25000

EsfuerzosubirKgt=Bladex.CreateSound('../../sounds/esfuerzo-subir-Kgt1.wav', 'EsfuerzosubirKgt')
EsfuerzosubirKgt.SendNotify=1
EsfuerzosubirKgt.MinDistance=1000
EsfuerzosubirKgt.MaxDistance=25000
EsfuerzosubirKgt1=Bladex.CreateSound('../../sounds/esfuerzo-subir-Kgt2.wav', 'EsfuerzosubirKgt1')
EsfuerzosubirKgt1.SendNotify=1
EsfuerzosubirKgt1.MinDistance=1000
EsfuerzosubirKgt1.MaxDistance=25000
EsfuerzosubirKgt2=Bladex.CreateSound('../../sounds/esfuerzo-subir-Kgt3.wav', 'EsfuerzosubirKgt2')
EsfuerzosubirKgt2.SendNotify=1
EsfuerzosubirKgt2.MinDistance=1000
EsfuerzosubirKgt2.MaxDistance=25000

EsfuerzofinalsubirKgt=Bladex.CreateSound('../../sounds/esfuerzofinal-subir-Kgt1.wav', 'EsfuerzofinalsubirKgt')
EsfuerzofinalsubirKgt.SendNotify=0.5
EsfuerzofinalsubirKgt.MinDistance=1000
EsfuerzofinalsubirKgt.MaxDistance=25000
EsfuerzofinalsubirKgt1=Bladex.CreateSound('../../sounds/esfuerzo-pesadoKgt1.wav', 'EsfuerzofinalsubirKgt1')
EsfuerzofinalsubirKgt1.SendNotify=1
EsfuerzofinalsubirKgt1.MinDistance=1000
EsfuerzofinalsubirKgt1.MaxDistance=25000

EsfuerzoEspecialKgt1=Bladex.CreateSound('../../sounds/esfuerzo-caballero-especial2.wav', 'EsfuerzoEspecialKgt1')
EsfuerzoEspecialKgt1.SendNotify=0.5
EsfuerzoEspecialKgt1.Volume=1
EsfuerzoEspecialKgt1.MinDistance=1000
EsfuerzoEspecialKgt1.MaxDistance=25000
EsfuerzoEspecialKgt2=Bladex.CreateSound('../../sounds/esfuerzo-caballero-especial1.wav', 'EsfuerzoEspecialKgt2')
EsfuerzoEspecialKgt2.SendNotify=1
EsfuerzoEspecialKgt2.Volume=1
EsfuerzoEspecialKgt2.MinDistance=1000
EsfuerzoEspecialKgt2.MaxDistance=25000





SaltoCortoBarbaro=Bladex.CreateSound('../../sounds/salto-caballero1.wav', 'SaltoCortoBarbaro')
SaltoCortoBarbaro.SendNotify=1
SaltoCortoBarbaro.Volume=1
SaltoCortoBarbaro.MinDistance=1000
SaltoCortoBarbaro.MaxDistance=25000
SaltoCortoBarbaro2=Bladex.CreateSound('../../sounds/salto-caballero2.wav', 'SaltoCortoBarbaro2')
SaltoCortoBarbaro2.SendNotify=1
SaltoCortoBarbaro2.Volume=1
SaltoCortoBarbaro2.MinDistance=1000
SaltoCortoBarbaro2.MaxDistance=25000
SaltoCortoBarbaro3=Bladex.CreateSound('../../sounds/salto-caballero3.wav', 'SaltoCortoBarbaro3')
SaltoCortoBarbaro3.SendNotify=1
SaltoCortoBarbaro3.Volume=1
SaltoCortoBarbaro3.MinDistance=1000
SaltoCortoBarbaro3.MaxDistance=25000
SaltoCortoBarbaro4=Bladex.CreateSound('../../sounds/salto-caballero4.wav', 'SaltoCortoBarbaro4')
SaltoCortoBarbaro4.SendNotify=1
SaltoCortoBarbaro4.Volume=1
SaltoCortoBarbaro4.MinDistance=1000
SaltoCortoBarbaro4.MaxDistance=25000
SaltoCortoBarbaro5=Bladex.CreateSound('../../sounds/salto-caballero5.wav', 'SaltoCortoBarbaro5')
SaltoCortoBarbaro5.SendNotify=1
SaltoCortoBarbaro5.Volume=1
SaltoCortoBarbaro5.MinDistance=1000
SaltoCortoBarbaro5.MaxDistance=25000
SaltoCortoBarbaro6=Bladex.CreateSound('../../sounds/salto-caballero6.wav', 'SaltoCortoBarbaro6')
SaltoCortoBarbaro6.SendNotify=1
SaltoCortoBarbaro6.Volume=1
SaltoCortoBarbaro6.MinDistance=1000
SaltoCortoBarbaro6.MaxDistance=25000

GritoHerida=Bladex.CreateSound('../../sounds/esfuerzo-barb-corto.wav', 'GritoHerida')
GritoHerida.SendNotify=0
GritoHerida.Volume=0.8
GritoHerida.MinDistance=5000
GritoHerida.MaxDistance=9000

ResbalaKgt1=Bladex.CreateSound('../../sounds/esfuerzo-resbala-Kgt1.wav', 'ResbalaKgt1')
ResbalaKgt1.SendNotify=0
ResbalaKgt1.Volume=0.8
ResbalaKgt1.MinDistance=5000
ResbalaKgt1.MaxDistance=9000


MuerteKgt1=Bladex.CreateSound('../../sounds/muerte-caballero1.wav', 'MuerteKgt1')
#MuerteBarb1.SendNotify=0
MuerteKgt2=Bladex.CreateSound('../../sounds/muerte-caballero2.wav', 'MuerteKgt2')
#MuerteBarb2.SendNotify=0
MuerteKgt3=Bladex.CreateSound('../../sounds/muerte-caballero3.wav', 'MuerteKgt3')
#MuerteBarb3.SendNotify=0
MuerteKgt4=Bladex.CreateSound('../../sounds/muerte-caballero4.wav', 'MuerteKgt4')
#MuerteBarb4.SendNotify=0

HeridaKgt1=Bladex.CreateSound('../../sounds/herida-caballero2.wav', 'HeridaKgt1')
#HeridaBarb1.SendNotify=0
HeridaKgt2=Bladex.CreateSound('../../sounds/herida-caballero1.wav', 'HeridaKgt2')
#HeridaBarb2.SendNotify=0
HeridaKgt3=Bladex.CreateSound('../../sounds/herida-caballero.wav', 'HeridaKgt3')
#HeridaBarb3.SendNotify=0

AndarKgt1=Bladex.CreateSound('../../sounds/correajes-55.wav', 'AndarKgt1') #PLAGUE: Same as 2
AndarKgt1.SendNotify=0
AndarKgt1.Volume=0.5
AndarKgt2=Bladex.CreateSound('../../sounds/correajes-55.wav', 'AndarKgt2')
AndarKgt2.SendNotify=0
AndarKgt2.Volume=0.5
AndarKgt3=Bladex.CreateSound('../../sounds/Correajes-66.wav', 'AndarKgt3') #PLAGUE: Same as 4
AndarKgt3.SendNotify=0
AndarKgt3.Volume=0.5
AndarKgt4=Bladex.CreateSound('../../sounds/Correajes-66.wav', 'AndarKgt4')
AndarKgt4.SendNotify=0
AndarKgt4.Volume=0.5
AndarKgt5=Bladex.CreateSound('../../sounds/Correajes-77.wav', 'AndarKgt5') #PLAGUE: Same as 6
AndarKgt5.SendNotify=0
AndarKgt5.Volume=0.5
AndarKgt6=Bladex.CreateSound('../../sounds/Correajes-77.wav', 'AndarKgt6')
AndarKgt6.SendNotify=0
AndarKgt6.Volume=0.5
AndarKgt7=Bladex.CreateSound('../../sounds/correajes-77a.wav', 'AndarKgt7')
AndarKgt7.SendNotify=0
AndarKgt7.Volume=0.3
AndarKgt8=Bladex.CreateSound('../../sounds/correajes-77b.wav', 'AndarKgt8')
AndarKgt8.SendNotify=0
AndarKgt8.Volume=0.3
AndarKgt9=Bladex.CreateSound('../../sounds/correajes-77c.wav', 'AndarKgt9')
AndarKgt9.SendNotify=0
AndarKgt9.Volume=0.3
AndarKgt10=Bladex.CreateSound('../../sounds/correajes-88.wav', 'AndarKgt10')
AndarKgt10.SendNotify=0
AndarKgt10.Volume=0.5
AndarKgt11=Bladex.CreateSound('../../sounds/correajes-88b.wav', 'AndarKgt11')
AndarKgt11.SendNotify=0
AndarKgt11.Volume=0.5

DesangreKgt1=Bladex.CreateSound('../../sounds/desangre2.wav', 'Desangre1Kgt')
DesangreKgt1.SendNotify=0
DesangreKgt1.Volume=0.6
DesangreKgt2=Bladex.CreateSound('../../sounds/desangre4.wav', 'Desangre2Kgt')
DesangreKgt2.SendNotify=0
DesangreKgt2.Volume=0.6

CaidaKgt1=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaKgt1')
CaidaKgt1.SendNotify=1
CaidaKgt1.Volume=1
CaidaKgt1.MinDistance=3000
CaidaKgt1.MaxDistance=12000

CaidaKgt2=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaKgt2')
CaidaKgt2.SendNotify=1
CaidaKgt2.Volume=1
CaidaKgt2.MinDistance=3000
CaidaKgt2.MaxDistance=12000

CaidaKgt3=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaKgt3')
CaidaKgt3.SendNotify=1
CaidaKgt3.Volume=1
CaidaKgt3.MinDistance=3000
CaidaKgt3.MaxDistance=12000

CaidaKgt4=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaKgt4')
CaidaKgt4.SendNotify=1
CaidaKgt4.Volume=1
CaidaKgt4.MinDistance=3000
CaidaKgt4.MaxDistance=12000

MuerteQuemado=Bladex.CreateSound('../../sounds/muerte-quemandoKgt.wav', 'MuerteQuemado')
MuerteQuemado.SendNotify=1
MuerteQuemado.Volume=1
MuerteQuemado.MinDistance=3000
MuerteQuemado.MaxDistance=12000

MuerteSaltoVacioKgt1=Bladex.CreateSound('../../sounds/salto-vacio-Kgt.wav', 'MuerteSaltoVacioKgt1')
MuerteSaltoVacioKgt1.SendNotify=1
MuerteSaltoVacioKgt1.Volume=1
MuerteSaltoVacioKgt1.MinDistance=3000
MuerteSaltoVacioKgt1.MaxDistance=12000

MuerteSaltoVacioKgt2=Bladex.CreateSound('../../sounds/salto-vacio-final-Kgt.wav', 'MuerteSaltoVacioKgt2')
MuerteSaltoVacioKgt2.SendNotify=1
MuerteSaltoVacioKgt2.Volume=1
MuerteSaltoVacioKgt2.MinDistance=3000
MuerteSaltoVacioKgt2.MaxDistance=12000

MuerteAplastamientoKgt1=Bladex.CreateSound('../../sounds/aplastamiento.wav', 'MuerteAplastamientoKgt1')
MuerteAplastamientoKgt1.SendNotify=1
MuerteAplastamientoKgt1.Volume=1
MuerteAplastamientoKgt1.MinDistance=3000
MuerteAplastamientoKgt1.MaxDistance=12000








# **********************************
#  pruebas ARMIN
#
# **********************************


#TensarArco=Bladex.CreateSound('../../sounds/bow_creak.wav', 'TensarArco')
TensarArco=Bladex.CreateSound('../../sounds/tensado_arco.wav', 'TensarArco')
#SoltarArco=Bladex.CreateSound('../../sounds/arrow_by.wav', 'SoltarArco')
SoltarArco=Bladex.CreateSound('../../sounds/disparo_arco.wav', 'SoltarArco')


print 'Sonidos para el caballero creados...'
