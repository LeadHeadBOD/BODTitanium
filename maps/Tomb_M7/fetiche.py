##///
##||| TOMB_M7/FETICHE.PY TITANIUM
##||| Change list:
##||| * Doors leading to tomb beneath temple now both make opening sound.
##|||   
##|||   
##\\\ 

import Bladex
import Doors
import Levers
import Actions
import Sounds
import GameText
import darfuncs

fetiche_located = 0
o_hand = ""
hand = 0


maderadesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderagolpe1=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "MaderaDesliz")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "MaderaGolpe")

piedradesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "PiedraDesliz")
piedragolpe1=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "PiedraGolpe")

piedradesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-metal .wav", "PiedraDesliz")
piedragolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-metal-pesado.wav", "PiedraGolpe")

puerta1  = Doors.CreateDoor("Puerta1",(28312,-11000, 12000), (0,1,0),  0, 5000,Doors.CLOSED)
puerta2  = Doors.CreateDoor("Puerta2",(28312,-11000,-15000), (0,1,0),  0, 5000,Doors.CLOSED)
puerta3  = Doors.CreateDoor("Puerta3",(38250, -4000, 13500), (0,1,0),  0, 4000,Doors.CLOSED)
puerta4  = Doors.CreateDoor("Puerta4",(38250, -4000,-16500), (0,1,0),  0, 4000,Doors.CLOSED)

puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-1000
puerta1.o_med_displ=4500
puerta1.closetype=Doors.AC
puerta1.c_init_displ=4500
puerta1.c_med_vel=8000
puerta1.SetWhileOpenSound(maderadesliz1)
puerta1.SetEndOpenSound(maderagolpe1)
puerta1.SetWhileCloseSound(maderadesliz1)
puerta1.SetEndCloseSound(maderagolpe1)

puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-1000
puerta2.o_med_displ=4500
puerta2.closetype=Doors.AC
puerta2.c_init_displ=4500
puerta2.c_med_vel=2000
#puerta2.SetWhileOpenSound(maderadesliz2)   # PLAGUE: Leave for now as it is, as the sounds on both sides
#puerta2.SetEndOpenSound(maderagolpe2)      #         don't make it clear what exactly has opened
#puerta2.SetWhileCloseSound(maderadesliz2)
#puerta2.SetEndCloseSound(maderagolpe2)

puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-500
puerta3.o_med_displ=3500
puerta3.closetype=Doors.AC
puerta3.c_init_displ=3500
puerta3.c_med_vel=2000
puerta3.SetWhileOpenSound(piedradesliz1)
puerta3.SetEndOpenSound(piedragolpe1)
puerta3.SetWhileCloseSound(piedradesliz1)
puerta3.SetEndCloseSound(piedragolpe1)

puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-500
puerta4.o_med_displ=3500
puerta4.closetype=Doors.AC
puerta4.c_init_displ=3500
puerta4.c_med_vel=2000
puerta4.SetWhileOpenSound(piedradesliz2)    # Was same as puerta 3
puerta4.SetEndOpenSound(piedragolpe2)       # Because the same sound entity cannot be played twice
puerta4.SetWhileCloseSound(piedradesliz2)   # it doesn't actually play it
puerta4.SetEndCloseSound(piedragolpe2)      #                                   -LeadHead



punterofetiche=Bladex.CreateEntity("PunteroFetiche","GhostPointer", 37326.822380,-2032.869097,-1484.375504)
punterofetiche.Static=1
punterofetiche.Scale=0.300000
punterofetiche.Orientation=0.504344,0.504344,-0.495618,0.495618
punterofetiche.UseFunc= SetupPutFetiche
darfuncs.SetHint(punterofetiche,"Fetish Recess")



palanca1=Levers.PlaceLever("Palanca1",Levers.LeverType3,(37935.862241,-8143.102607,-14670.203713),(0.5,0.5,0.5,-0.5),1.0)
palanca2=Levers.PlaceLever("Palanca1",Levers.LeverType3,(37909.417475,-8201.175389,11798.228900), (0.5,0.5,0.5,-0.5),1.0)

palanca1.OnTurnOnFunc=ActivateLever
palanca1.OnTurnOnArgs=(1,0)
palanca2.mode=1

palanca2.OnTurnOnFunc=ActivateLever
palanca2.OnTurnOnArgs=(2,0)
palanca2.mode=1

#palanca1.OnTurnOffFunc=CierraPuerta3
#palanca1.OnTurnOffArgs=()

#fetiche=Bladex.CreateEntity("Fetiche1","Fetiche",42568.632141,-1838.082663,-1599.205681)
#fetiche.Static=0
#fetiche.Scale=1.000000
#fetiche.Orientation=0.937728,-0.010984,-0.344836,-0.040418

levers_activates = 0
chapu_flag = 1



############### funcion que utiliza ghpointer ###################3

############## ghost pointer fetiche ########################3
p=Bladex.CreateEntity("GhpFetiche","GhostPointer",33750.0,-1500.0,-1500.0)
p.Static=0
p.Scale=0.100000
p.Orientation=0.681583,0.038276,-0.023801,-0.730351
p.UseFunc = useInGhostFetiche	# cambiar funcion

darfuncs.SetHint(p,"Tomb Oracle")
