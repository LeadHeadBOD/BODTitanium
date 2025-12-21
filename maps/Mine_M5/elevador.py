##///
##||| Mine_M5/elevador.PY TITANIUM
##||| Change list:
##||| * Restored sound for one of the elevators that was missing it.
##\\\ 


import Doors
import Objects
import Sounds
import Levers

###CREAMOS LA PLATAFORMA-OBJETO


##ESTABLECEMOS LA PROPIEDAD "DINAMICA" PARA LA PLATAFORMA OBJETO



##ESTABLECEMOS LOS SONIDOS QUE TENDR� EL ELEVADOR

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")

##CREAMOS LA BARRA ELEVADORA -no tiene por que ser una sola, podr�an ser varias-

columnaelevador=Doors.CreateDoor("ColumnaElevador", (-31500, -22000, -101500), (0, -1, 0), 0, 6200, Doors.OPENED)

##ESTABLECEMOS LOS TRAMOS DE MOVIMIENTO

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=5200
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500
columnaelevador.SetWhileOpenSound(loopelevador)     # Add
columnaelevador.SetEndOpenSound(golpeelevador)      #

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=5200
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500
columnaelevador.SetWhileCloseSound(loopelevador)    # Add
columnaelevador.SetEndCloseSound(golpeelevador)     # 

enmarcha=0



columnaelevador.OnEndCloseFunc=EsperaYBajaElevador
columnaelevador.OnEndOpenFunc=ElevadorArriba

##CREAMOS LA PALANCA

palancaelevador=Levers.PlaceLever("PalancaElevador", Levers.LeverType3, (-33124.502292,-25928.344024,-97666.339698), (0.500000,0.500000,-0.500000,0.500000), 1.0)
palancaelevador.mode=1

palancaelevador.OnTurnOnFunc=SubeElevador
palancaelevador.OnTurnOnArgs=()



palanca2elevador=Levers.PlaceLever("Palanca2Elevador", Levers.LeverType3, (-31465.149680,-19113.628340,-98757.394174), (0.707107,0.707107,0.000000,0.000000), 1.0)
palanca2elevador.mode=1

palanca2elevador.OnTurnOnFunc=SubeElevador
palanca2elevador.OnTurnOnArgs=()

#########
#########
#########THE END