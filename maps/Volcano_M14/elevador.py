##///
##||| Volcano_M14/elevador.PY TITANIUM
##||| Change list:
##||| * Restored missing elevator sounds
##\\\ 

import Doors
import Objects
import Sounds
import Levers



##################################################
##################################################
#######Elevador de la sala de la jaula############
##################################################



loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")


columnaelevador=Doors.CreateDoor("ColumnaElevador", (32125, 5000, 35125), (0, -1, 0), 0, 7500, Doors.OPENED)

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=6500
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500

columnaelevador.SetWhileOpenSound(loopelevador)     # Add
columnaelevador.SetEndOpenSound(golpeelevador)      #



columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=6500
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500

columnaelevador.SetWhileCloseSound(loopelevador)    # Add
columnaelevador.SetEndCloseSound(golpeelevador)     #

columnaelevador.OnEndCloseFunc=EsperaYBajaElevador
columnaelevador.OnEndOpenFunc=ElevadorArriba


palanca1elevador=Levers.PlaceLever("Palanca1Elevador", Levers.LeverType3, (33907.726998,8689.956646,36887.202347), (0.650895,0.650895,0.276289,-0.276289), 1.0)
palanca1elevador.mode=1

palanca1elevador.OnTurnOnFunc=SubeElevador
palanca1elevador.OnTurnOnArgs=()


palanca2elevador=Levers.PlaceLever("Palanca2Elevador", Levers.LeverType2, (32608.355827,558.770390,38335.832603), (0.061628,0.061628,-0.704416,0.704416), 1.0)
palanca2elevador.mode=1

palanca2elevador.OnTurnOnFunc=SubeElevador
palanca2elevador.OnTurnOnArgs=()
