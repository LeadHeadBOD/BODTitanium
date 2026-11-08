##///
##||| Mine_back/Puertmn.PY TITANIUM
##||| Change list:
##||| * Sounds for the door at the start of the acid flood
##||| * Sounds for the door as you exit the rune tablet room
##||| * Added different but more appropriate sounds for the platform leading out of the rune room
##\\\ 

import Doors
import Levers
import Locks
import Objects
import Sounds
import Button
import darfuncs
import Stars
import Sparks


#######################################################
########## PUERTA DE LA SALA DE LA TABLILLA ###########
#######################################################

#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz2")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe2")

###
# Reactivated these sounds, because otherwise the game might assign some incredibly weak sound effects to the 
# door in the tablet cut scene, which isn't very cool           -LeadHead
maderadeslizTab=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "maderadeslizTab")
maderadeslizTab.Volume=1
maderadeslizTab.MinDistance=1000
maderadeslizTab.MaxDistance=20000
maderagolpeTab=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe2.wav", "maderadeslizTab")
maderagolpeTab.Volume=1
maderagolpeTab.MinDistance=4000
maderagolpeTab.MaxDistance=50000


#escalon 1a
puerta1a=Doors.CreateDoor("Puerta1a", (93000,-20000,-164750), (0,1,0), 0, 4500, Doors.CLOSED)

puerta1a.opentype=Doors.UNIF
puerta1a.o_med_vel=-500
puerta1a.o_med_displ=4500
puerta1a.SetWhileOpenSound(maderadeslizTab)     # Added
puerta1a.SetEndOpenSound(maderagolpe)           #

puerta1a.closetype=Doors.UNIF
puerta1a.c_med_vel=3900
puerta1a.c_med_displ=4500
puerta1a.SetWhileCloseSound(maderadeslizTab)    # Added
puerta1a.SetEndCloseSound(maderagolpeTab)       #   -Leadhead


### Sounds for the platform that emerges        -LeadHead
PlatSlideFin=Sounds.CreateEntitySound("../../Sounds/Stone-lever.wav", "PlatSlideFin")
PlatSlideFin.Volume=1
PlatSlideFin.MinDistance=5000
PlatSlideFin.MaxDistance=40000
PlatSlide2=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando.wav", "PlatSlide2")
PlatSlide2.Volume=0.7
PlatSlide2.MinDistance=1000
PlatSlide2.MaxDistance=30000



o=Bladex.CreateEntity("bloque1","Bloque",94777.786102,-19044.803706,-162374.223081)
o.Static=0
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000

button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),400,0,0,1)



sc=Bladex.GetSector(86000,-20000,-164550)
sc.OnEnter=Cierrap1
