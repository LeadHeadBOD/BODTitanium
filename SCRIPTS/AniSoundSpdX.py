##///
##||| ANISOUNDSPDX.PY TITANIUM
##||| Change list:
##||| * Made movement sounds less obnoxious by limiting min/max distance.
##||| * Spider spit should actually be decently audible now.
##\\\ 

import Bladex

# *********************************
# *      Creacion de sonidos      *
# *********************************


GolpeArmaEscudoSpd=Bladex.CreateSound('../../sounds/golpe-arma-escudo.wav', 'GolpeArmaEscudoSpd')
GolpeArmaEscudoSpd.SendNotify=0
GolpeArmaArmaSpd=Bladex.CreateSound('../../sounds/golpe-arma-arma.wav', 'GolpeArmaArmaSpd')
GolpeArmaArmaSpd.SendNotify=0
TajoEmpalanteSpd=Bladex.CreateSound('../../sounds/tajo-empalante.wav', 'TajoEmpalanteSpd')
TajoEmpalanteSpd.SendNotify=0
TajoCortanteSpd=Bladex.CreateSound('../../sounds/tajo-cortante.wav', 'TajoCortanteSpd')
TajoCortanteSpd.SendNotify=0
TajoMutilacionSpd=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'TajoMutilacionSpd')
TajoMutilacionSpd.SendNotify=0
#GolpeContundenteSpd=Bladex.CreateSound('../../sounds/slice-splat1.wav', 'GolpeContundenteSpd')
#GolpeContundenteSpd.SendNotify=0


MuerteSpd=Bladex.CreateSound('../../sounds/MUERTE-ARANA.wav', 'MuerteSpd')
MuerteSpd.SendNotify=0

EscupeSpd=Bladex.CreateSound('../../sounds/ECUPIENDO-VENENO.wav', 'EscupeSpd')
EscupeSpd.SendNotify=0
EscupeSpd.Volume=1
EscupeSpd.MinDistance=5000
EscupeSpd.MaxDistance=25000
Derrite=Bladex.CreateSound('../../sounds/arana_derrite.wav', 'Derrite')
Derrite.SendNotify=0
Derrite.Volume=1
GritoSpd1=Bladex.CreateSound('../../sounds/GRITO_ARANA.wav', 'GritoSpd1')
GritoSpd1.SendNotify=0

Movimiento1=Bladex.CreateSound('../../sounds/mov-arana11.wav', 'Movimiento1')
Movimiento1.SendNotify=0
Movimiento1.MinDistance=1000
Movimiento1.MaxDistance=12000
Movimiento2=Bladex.CreateSound('../../sounds/mov-arana2.wav', 'Movimiento2')
Movimiento2.SendNotify=0
Movimiento2.MinDistance=1000
Movimiento2.MaxDistance=12000
Movimiento3=Bladex.CreateSound('../../sounds/mov-arana3.wav', 'Movimiento3')
Movimiento3.SendNotify=0
Movimiento3.MinDistance=1000
Movimiento3.MaxDistance=12000


print "Sonidos para la aranita creados..."
