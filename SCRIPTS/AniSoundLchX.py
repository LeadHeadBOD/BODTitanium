##///
##||| AniSoundLchX.PY TITANIUM
##||| Change list:
##||| * Commmented out sounds that do not exist
##||| * 
##||| * 
##||| * 
##||| * TODO: Re-enable "Respiracion2"
##||| * TODO: Re-enable randomized vomit sound
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************


GolpeArmaEscudoLch=Bladex.CreateSound('../../sounds/M-GOLPE-ESCUDO-METAL.wav', 'GolpeArmaEscudoLch')
GolpeArmaEscudoLch.SendNotify=0
GolpeArmaArmaLch=Bladex.CreateSound('../../sounds/M-METAL-METAL-1E.wav', 'GolpeArmaArmaLch')
GolpeArmaArmaLch.SendNotify=0
GolpeContundenteLch=Bladex.CreateSound('../../sounds/golpe-maza-lich.wav', 'GolpeContundenteLch')
GolpeContundenteLch.SendNotify=0
TajoEmpalanteLch=Bladex.CreateSound('../../sounds/corte_lich6.wav', 'TajoEmpalanteLch')
TajoEmpalanteLch.SendNotify=0
TajoCortanteLch=Bladex.CreateSound('../../sounds/corte_lich5.wav', 'TajoCortanteLch')
TajoCortanteLch.SendNotify=0
TajoMutilacionLch=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionLch')
TajoMutilacionLch.SendNotify=0

Enfundar=Bladex.CreateSound('../../sounds/M-DESENFUNDADING.wav', 'Enfundar')
Enfundar.SendNotify=0


EsfuerzoCortoLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch1.wav', 'EsfuerzoCortoLch')
EsfuerzoCortoLch.SendNotify=0
EsfuerzoCortoLch.Volume=0.8
EsfuerzoCorto1Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch2.wav', 'EsfuerzoCorto1Lch')
EsfuerzoCorto1Lch.SendNotify=0
EsfuerzoCorto1Lch.Volume=0.8
EsfuerzoCorto2Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch3.wav', 'EsfuerzoCorto2Lch')
EsfuerzoCorto2Lch.SendNotify=0
EsfuerzoCorto2Lch.Volume=0.8
EsfuerzoCorto3Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch4.wav', 'EsfuerzoCorto3Lch')
EsfuerzoCorto3Lch.SendNotify=0
EsfuerzoCorto3Lch.Volume=0.8
EsfuerzoCorto4Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch5.wav', 'EsfuerzoCorto4Lch')
EsfuerzoCorto4Lch.SendNotify=0
EsfuerzoCorto4Lch.Volume=0.8
EsfuerzoCorto5Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch6.wav', 'EsfuerzoCorto5Lch')
EsfuerzoCorto5Lch.SendNotify=0
EsfuerzoCorto5Lch.Volume=0.8
EsfuerzoCorto6Lch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch1.wav', 'EsfuerzoCorto6Lch')
EsfuerzoCorto6Lch.SendNotify=0
EsfuerzoCorto6Lch.Volume=0.8
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
EsfuerzoGolpeFrontalLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch1.wav', 'EsfuerzoGolpeFrontalLch')
EsfuerzoGolpeFrontalLch.SendNotify=0
EsfuerzoGolpeLateralLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch2.wav', 'EsfuerzoGolpeLateralLch')
EsfuerzoGolpeLateralLch.SendNotify=0
EsfuerzoGolpeCabezaLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch3.wav', 'EsfuerzoGolpeCabezaLch')
EsfuerzoGolpeCabezaLch.SendNotify=0
EsfuerzoGolpeAtrasLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch4.wav', 'EsfuerzoGolpeAtrasLch')
EsfuerzoGolpeAtrasLch.SendNotify=0
EsfuerzoLchMediano=Bladex.CreateSound('../../sounds/Esfuerzo-Lch5.wav', 'EsfuerzoLcharoMediano')
EsfuerzoLchMediano.SendNotify=0
EsfuerzoGolpeArribaLch=Bladex.CreateSound('../../sounds/Esfuerzo-Lch6.wav', 'EsfuerzoGolpeArribaLch')
EsfuerzoGolpeArribaLch.SendNotify=0
MuerteLch1=Bladex.CreateSound('../../sounds/muerteLch1.wav', 'MuerteLch1')
MuerteLch1.SendNotify=0
MuerteLch2=Bladex.CreateSound('../../sounds/muerte-Lch2.wav', 'MuerteLch2')
MuerteLch2.SendNotify=0
# MuerteLch3=Bladex.CreateSound('../../sounds/muerteLch1.wav', 'MuerteLch3')      # Commented out, 
# MuerteLch3.SendNotify=0                                                         # identical to Muerte1 and Muerte 2
# MuerteLch4=Bladex.CreateSound('../../sounds/muerte-Lch2.wav', 'MuerteLch4')     # 
# MuerteLch4.SendNotify=0                                                         #                   -LeadHead
HeridaLch1=Bladex.CreateSound('../../sounds/herida-Lch1.wav', 'HeridaLch1')
HeridaLch1.SendNotify=0
HeridaLch2=Bladex.CreateSound('../../sounds/herida-Lch2.wav', 'HeridaLch2')
HeridaLch2.SendNotify=0
# HeridaLch3=Bladex.CreateSound('../../sounds/herida-Lch2.wav', 'HeridaLch3')   #Commented out, unused.
# HeridaLch3.SendNotify=0                                                       #           -LeadHead

EscupeLch1=Bladex.CreateSound('../../sounds/lich-escupe-3.wav', 'EscupeLch1')   
EscupeLch1.SendNotify=0                                                        
EscupeLch1.Volume=1                                                            

# EscupeLch2=Bladex.CreateSound('../../sounds/lich-escupe-3.wav', 'EscupeLch2')       # Previously unused
# EscupeLch2.SendNotify=0                                                              # Was set to same sound file as Escupe1
# EscupeLch2.Volume=1                                                                  #           -LeadHead

# EscupeLch2.AddAltSound('EscupeLch1')                                            # TODO: rework this lich-escupe2 to better suit the anim


RespiracionLch1=Bladex.CreateSound('../../sounds/respiracion-lich1.wav', 'RespiracionLch1')
RespiracionLch1.SendNotify=0
RespiracionLch1.Volume=1
RespiracionLch1.MinDistance=1000
RespiracionLch1.MaxDistance=14000
RespiracionLch2=Bladex.CreateSound('../../sounds/respiracion-lich1.wav', 'RespiracionLch2') #
RespiracionLch2.SendNotify=0                                                                # Should comment out
RespiracionLch2.Volume=1                                                                    # Targets the same sound file as Respiracion1
RespiracionLch2.MinDistance=1000                                                            # Will re-enable once I can replace Dal Gurak's sounds, since they are identical to these.
RespiracionLch2.MaxDistance=14000                                                           #                     -LeadHead

GeneradorLch1=Bladex.CreateSound('../../sounds/M-GENERADOR-ENTIERRA3.wav', 'GeneradorLch1')
GeneradorLch1.Volume=1
GeneradorLch1.MinDistance=1000
GeneradorLch1.MaxDistance=25000

GeneradorLch2=Bladex.CreateSound('../../sounds/generador-agua.wav', 'GeneradorLch2')
GeneradorLch2.Volume=1
GeneradorLch2.MinDistance=1000
GeneradorLch2.MaxDistance=25000


AndarLch1=Bladex.CreateSound('../../sounds/mov.lich-1.wav', 'AndarLch1')
AndarLch1.Volume=0.2
AndarLch1.MinDistance=1000
AndarLch1.MaxDistance=25000

AndarLch2=Bladex.CreateSound('../../sounds/mov.lich-2.wav', 'AndarLch2')
AndarLch2.Volume=0.2
AndarLch2.MinDistance=1000
AndarLch2.MaxDistance=25000

CaidaLch1=Bladex.CreateSound('../../sounds/caida-mano.wav', 'CaidaLch1')
CaidaLch1.Volume=0.8
CaidaLch1.MinDistance=1000
CaidaLch1.MaxDistance=25000
CaidaLch2=Bladex.CreateSound('../../sounds/caida-pie.wav', 'CaidaLch2')
CaidaLch2.Volume=0.8
CaidaLch2.MinDistance=1000
CaidaLch2.MaxDistance=25000

DesangreLch1=Bladex.CreateSound('../../sounds/lich-desangre.wav', 'DesangreLch1')
DesangreLch1.Volume=1
DesangreLch1.MinDistance=1000
DesangreLch1.MaxDistance=25000




print "Sonidos para el lich creados..."
