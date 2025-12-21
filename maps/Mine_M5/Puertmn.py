##///
##||| Mine_M5/Puertmn.PY TITANIUM
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
############################################################
##########-PUERTA-LLAVE-1. Orco jefe que patrulla por el principio.
############################################################
############################################################
############################################################
############################################################
#######################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


puerta1=Bladex.CreateEntity("Puerta1","Rastrillo",-55718.197526,-22925.400447,-7753.154644)
puerta1.Scale=1.0
puerta1.Orientation=0.706999,0.706999,0.012341,-0.012341
Sparks.SetMetalSparkling("Puerta1")

puerta1din=Objects.CreateDinamicObject("Puerta1")

##funciones abrir-cerrar##





###cerradura rastrillos###

##cerradura ##

cerradura1=Locks.PlaceLock("cerradura1","Cerraduracutre",(-53519.627577,-21129.492316,-11596.200138),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradura1.key="llave1"


cerradura1.OnUnLockFunc=Abrepuerta1
cerradura1.OnUnLockArgs=()

cerradura1.OnLockFunc=Cierrapuerta1
cerradura1.OnLockArgs=()

darfuncs.SetHint(cerradura1.obj,"Iron Lock")

##Llave 1##

o=Bladex.CreateEntity("llave1","Llavecutre",-54925.911099,-20021.640619,-12786.615240)
o.Static=0
o.Scale=1.0
o.Orientation=0.997457,-0.008145,-0.070589,-0.005438
darfuncs.SetHint(o,"Iron Key")






############################################################
############################################################
##########-PUERTA-LLAVEr3. oRCOS DEL TERCER RECORRIDO, AL FINAL, ANTES DEL ELEVADOR.
############################################################
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar3=Doors.CreateDoor("Puertar3", (-21450,-7500,-142800), (0,1,0), 750, 5500, Doors.CLOSED)
puertar3.Squezze = 1

puertar3.opentype=Doors.UNIF
puertar3.o_med_vel=-800
puertar3.o_med_displ=4750


puertar3.closetype=Doors.AC
puertar3.c_init_displ=4750
puertar3.c_med_vel=8000


puertar3.SetWhileOpenSound(maderadesliz)
puertar3.SetEndOpenSound(maderagolpe)

puertar3.SetWhileCloseSound(maderadesliz)
puertar3.SetEndCloseSound(maderagolpe)

###llaver3 abrepuertar3###


cerradurpr3=Locks.PlaceLock("cerradurpr3","Cerraduracutre",(-22760.034664,-5812.324894,-146558.957389),(0.686103,0.686103,0.171065,-0.171065),3.0)
cerradurpr3.key="llaver3"


cerradurpr3.OnUnLockFunc=AbrePuertaLlaver3
cerradurpr3.OnUnLockArgs=()

cerradurpr3.OnLockFunc=CierraPuertaLlaver3
cerradurpr3.OnLockArgs=()

darfuncs.SetHint(cerradurpr3.obj,"Iron Lock")


o=Bladex.CreateEntity("llaver3","Llavecutre",-19305.619387,-4527.289849,-147393.502511)
o.Static=0
o.Scale=1.0
o.Orientation=0.044459,0.987682,-0.008945,0.149756
darfuncs.SetHint(o,"Iron Key")


############################################################
################primer recorrido. Se abre desde dentro##########################
############################################################
############################################################
############################################################
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar1=Doors.CreateDoor("Puertar1", (-95250,-17000,-5500), (0,1,0), 750, 4500, Doors.CLOSED)
puertar1.Squezze = 1

puertar1.opentype=Doors.UNIF
puertar1.o_med_vel=-800
puertar1.o_med_displ=3750


puertar1.closetype=Doors.AC
puertar1.c_init_displ=3750
puertar1.c_med_vel=8000


puertar1.SetWhileOpenSound(maderadesliz)
puertar1.SetEndOpenSound(maderagolpe)

puertar1.SetWhileCloseSound(maderadesliz)
puertar1.SetEndCloseSound(maderagolpe)

##### Accionar puertas al accionar una palanca


palanr1=Levers.PlaceLever("Palanr1",Levers.LeverType3,(-92388.082801,-16666.685955,-4363.104393),(0.006171,0.006171,0.707080,-0.707080),1.0)

palanr1.mode=1

palanr1.OnTurnOnFunc=AbrePuertar1
palanr1.OnTurnOnArgs=()

palanr1.OnTurnOffFunc=CierraPuertar1
palanr1.OnTurnOffArgs=()



############################################################
############################################################
################segundo recorrido, al final. Se abre desde dentro##########################
############################################################
############################################################
############################################################
############################################################



maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar2=Doors.CreateDoor("Puertar2", (-41200,-31500,-30550), (0,1,0), 750, 5500, Doors.CLOSED)
puertar2.Squezze = 1

puertar2.opentype=Doors.UNIF
puertar2.o_med_vel=-800
puertar2.o_med_displ=4750


puertar2.closetype=Doors.AC
puertar2.c_init_displ=4750
puertar2.c_med_vel=8000


puertar2.SetWhileOpenSound(maderadesliz)
puertar2.SetEndOpenSound(maderagolpe)

puertar2.SetWhileCloseSound(maderadesliz)
puertar2.SetEndCloseSound(maderagolpe)

##### Abrir puertas al accionar una palanca


palanr2=Levers.PlaceLever("Palanr2",Levers.LeverType3,(-42883.866074,-29494.990897,-33197.394174),(0.188966,0.188966,0.681390,-0.681390),1.0)

palanr2.mode=1





palanr2.OnTurnOnFunc=AbrePuertar2
palanr2.OnTurnOnArgs=()

palanr2.OnTurnOffFunc=CierraPuertar2
palanr2.OnTurnOffArgs=()






#######################################################
########## PUERTA DE LA SALA DE LA TABLILLA ###########
#######################################################


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



###########PUERTA DE MADERA en el segundo recorrido


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertaen=Doors.CreateDoor("Puertaen", (-98250,-21000,-95450), (0,1,0), 500, 5250, Doors.CLOSED)
puertaen.Squezze = 1

puertaen.opentype=Doors.UNIF
puertaen.o_med_vel=-500
puertaen.o_med_displ=5250



puertaen.SetWhileOpenSound(maderadesliz)
puertaen.SetEndOpenSound(maderagolpe)




cerraduren=Locks.PlaceLock("cerraduren","Cerraduracutre",(-100424.707000,-20802.507000,-96195.054000),(0.495618,0.495618,0.504344,-0.504344),3.0)
cerraduren.key="llavemaz"



cerraduren.OnUnLockFunc=AbrePuertaLlaveen
cerraduren.OnUnLockArgs=()

darfuncs.SetHint(cerraduren.obj,"Iron Lock")

##Llave mazmorras##

o=Bladex.CreateEntity("llavemaz","Llavecutre",-98667.1385534, -20565.7775427, -97440.076)
o.Static=0
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Data = 4
darfuncs.SetHint(o,"Iron Key")
Stars.Twinkle("llavemaz")
