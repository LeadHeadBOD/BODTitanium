##///
##||| Dwarf_M3/DERR.PY TITANIUM
##||| Change list:
##||| * Added material to breaking sector
##\\\ 

import Bladex



###################
#     Sonidos     #
###################

derrumbesuelopiedra=Bladex.CreateSound("../../Sounds/Stone-floor-collapse.wav", "DerrumbeSueloPiedra")
derrumbesuelopiedra.Volume=1
derrumbesuelopiedra.MinDistance=5000
derrumbesuelopiedra.MaxDistance=40000

derrumbesueloagua=Bladex.CreateSound("../../Sounds/impact-watersplash.wav", "DerrumbeSueloAgua")
derrumbesueloagua.Volume=1
derrumbesueloagua.MinDistance=5000
derrumbesueloagua.MaxDistance=40000


#############################################
#     Derrumbamiento SUELO TUNEL            #
#############################################

derr1=Bladex.GetSector(-108500, -7000, -56400)
derr1.Active=0
derr2=Bladex.GetSector(-108500, -7000, -61400)
derr2.Active=0
derr3=Bladex.GetSector(-108500, -17000, -56400)
derr3.Active=0
derr4=Bladex.GetSector(-108500, -17000, -61400)
derr4.Active=0


derr1.InitBreak((0, 1800, 0), (2500, 0, 130), (310, 0.0, 2050),'piedra pesada') # added material
derr2.InitBreak((0, 1800, 0), (2500, 0, 130), (510, 0.0, 2050),'piedra pesada')
derr3.InitBreak((0, 1800, 0), (2500, 0, 130), (310, 0.0, 2050),'piedra pesada')
derr4.InitBreak((0, 1800, 0), (2500, 0, 130), (310, 0.0, 2050),'piedra pesada')


###sector que activa la rotura
#sectorderr=Bladex.GetSector(-108500, -11000, -56400)
sectorderr=Bladex.GetSector(-101000, -11000, -58000)



sectorderr.OnWalkOn=Derrumba
