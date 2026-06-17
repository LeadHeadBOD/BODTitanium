##///
##||| Ragnar_M2/puertas.PY TITANIUM
##||| Change list:
##||| * Adjust item positions to make sure they don't float/stuck-in-geo
##\\\ 

import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import AuxFuncs
import darfuncs
import Stars
import Bladex


###### Definici�n de los sonidos de todas las puertas -incluyendo las objeto-

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


##### Mazmorras #####

##definici�n rastrillos: 3 puertas con cerraduras propias que se abren con la misma llave##

rastmaz1=Bladex.CreateEntity("RastMaz1","Rastrillo10",-88758.822862,5491.538943,75705.631400,"Physic") # esteeeeeeeeeeeeeeeeeeeeeeeeeeeeee
rastmaz1.Scale=1.2
rastmaz1.Orientation=0.707107,0.707107,0.000000,0.000000
rastmaz1=Sparks.SetMetalSparkling("RastMaz1")
rastmaz1.Frozen=1

rastmaz1din=Objects.CreateDinamicObject("RastMaz1")


rastmaz2=Bladex.CreateEntity("RastMaz2","Rastrillo10",-101774.938931,5491.538943,75744.824997,"Physic") # -101774 esteeeeeeeeeeeeeeeeeeeeeeeeeeeeee
rastmaz2.Scale=1.2
rastmaz2.Orientation=0.707107,0.707107,0.000000,0.000000
rastmaz2=Sparks.SetMetalSparkling("RastMaz2")
rastmaz2.Frozen=1

rastmaz2din=Objects.CreateDinamicObject("RastMaz2")


rastmaz3=Bladex.CreateEntity("RastMaz3","Rastrillo10",-111756.722871,5238.099278,75723.752896,"Physic") # esteeeeeeeeeeeeeeeeeeeeeeeeeeeeee
rastmaz3.Scale=1.3
rastmaz3.Orientation=0.707107,0.707107,0.000000,0.000000
rastmaz3=Sparks.SetMetalSparkling("RastMaz3")
rastmaz3.Frozen=1

rastmaz3din=Objects.CreateDinamicObject("RastMaz3")



#la,la,la...


###cerraduras rastrillos###

##cerradura 1##

cerradura1=Locks.PlaceLock("cerradura1","Cerraduracutre",(-85810.175, 7737.455251, 74478.046911),(0.504344,0.504344,0.495618,-0.495618),2.5)
cerradura1.key="llavemaz"


cerradura1.OnUnLockFunc=Abrerastmaz1
cerradura1.OnUnLockArgs=()

cerradura1.OnLockFunc=Cierrarastmaz1
cerradura1.OnLockArgs=()

darfuncs.SetHint(cerradura1.obj,"Dungeon Lock")


##cerradura 2##

cerradura2=Locks.PlaceLock("cerradura2","Cerraduracutre",(-99030.357156, 7737.455251, 74468.046911),(0.495618,0.495618,0.504344,-0.504344),2.5)
cerradura2.key="llavemaz"


cerradura2.OnUnLockFunc=Abrerastmaz2
cerradura2.OnUnLockArgs=()

cerradura2.OnLockFunc=Cierrarastmaz2
cerradura2.OnLockArgs=()

darfuncs.SetHint(cerradura2.obj,"Dungeon Lock")


##cerradura 3##

cerradura3=Locks.PlaceLock("cerradura3","Cerraduracutre",(-108745.911000,7698.883000,74488.046911),(0.504344,0.504344,0.495618,-0.495618),2.5)
cerradura3.key="llavemaz"


cerradura3.OnUnLockFunc=Abrerastmaz3
cerradura3.OnUnLockArgs=()

cerradura3.OnLockFunc=Cierrarastmaz3
cerradura3.OnLockArgs=()

darfuncs.SetHint(cerradura3.obj,"Dungeon Lock")



###########PUERTA DE MADERA QUE SE CIERRA SOLA


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puertaen=Doors.CreateDoor("Puertaen", (-95250,6000,69250), (0,1,0), 1000, 4500, Doors.CLOSED)
puertaen.Squezze = 1

puertaen.opentype=Doors.UNIF
puertaen.o_med_vel=-500
puertaen.o_med_displ=3500


puertaen.closetype=Doors.AC
puertaen.c_init_displ=3500
puertaen.c_med_vel=8000


puertaen.SetWhileOpenSound(maderadesliz)
puertaen.SetEndOpenSound(maderagolpe)




cerraduren=Locks.PlaceLock("cerraduren","Cerraduracutre",(-96518.142662,8014.579554,66352.351684),(0.012341,0.012341,0.706999,-0.706999),3.0)
cerraduren.key="llavemaz"

cerraduren.OnUnLockFunc=AbrePuertaLlaveen
cerraduren.OnUnLockArgs=()

darfuncs.SetHint(cerraduren.obj,"Dungeon Lock")

puertaen.SetWhileCloseSound(maderadesliz)
puertaen.SetEndCloseSound(maderagolpe2)


sen=Bladex.GetSector(-86750,6000,69550)
sen.OnEnter=CierraPuertaLlaveen

##Llave mazmorras##

o=Bladex.CreateEntity("llavemaz","Llavecutre",-113243.050546, 7949.07025002, 68889.022358,"Physic")
o.Scale=1.25
o.Orientation=0.0730228796601, -0.990972220898, 0.0152629939839, 0.111394353211
o.Data = 4
darfuncs.SetHint(o,"Dungeon Key")
Stars.Twinkle("llavemaz")



##### Puerta antes del puente levadizo #####


puerta1=Doors.CreateDoor("Puerta1", (-88500,-11000,-10750), (0,1,0), 1250, 6550, Doors.CLOSED)
puerta1.Squezze = 1

puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-500
puerta1.o_med_displ=5300


puerta1.closetype=Doors.AC
puerta1.c_init_displ=5300
puerta1.c_med_vel=16000


puerta1.SetWhileOpenSound(maderadesliz)
puerta1.SetEndOpenSound(maderagolpe)

puerta1.SetWhileCloseSound(maderadesliz)
puerta1.SetEndCloseSound(maderagolpe2)

##### Accionar puertas al accionar una palanca


palancap1=Levers.PlaceLever("PalancaP1",Levers.LeverType3,(-91444.539027,-8758.090546,-9613.706792),(0.000000,0.000000,0.707107,-0.707107),1.0)

palancap1.mode=1


palancap1.OnTurnOnFunc=AbrePuerta1
palancap1.OnTurnOnArgs=()

palancap1.OnTurnOffFunc=CierraPuerta1
palancap1.OnTurnOffArgs=()

p1yaabierta=0






########################################

##### Puerta de la sala del muerto #####


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta2=Doors.CreateDoor("Puerta2", (-94750,-2000,8750), (0,1,0), 1250, 7250, Doors.CLOSED)
puerta2.Squezze = 1

puerta2.opentype=Doors.UNIF
puerta2.o_med_vel=-500
puerta2.o_med_displ=6000




puerta2.SetWhileOpenSound(maderadesliz)
puerta2.SetEndOpenSound(maderagolpe)



###llave2 abrepuerta de la capilla###


cerradurp2=Locks.PlaceLock("cerradurp2","Cerraduracutre",(-92987.928000,-1034.547000,12841.838000),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradurp2.key="Llavep2"

cerradurp2.OnUnLockFunc=AbrePuertaLlave2
cerradurp2.OnUnLockArgs=()


darfuncs.SetHint(cerradurp2.obj,"Chapel Lock")


llavep2=Bladex.CreateEntity("Llavep2","Llavecutre",-90000,-100,12000)
llavep2.Static=0
llavep2.Scale=1.0
llavep2.Orientation=0.998135,0.061049,0.000000,0.000000
darfuncs.SetHint(llavep2,"Chapel Key")





########################################

##### Puerta de la salida de las mazmorras. Llave con los bichitos. #####




darfuncs.MuertoyTroceado(-153061.854683, 12865.8698322, 45745.3463,"Knight_Traitor","",(1,5))



maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta3=Doors.CreateDoor("Puerta3", (-130500,2000,39750), (0,1,0), 1750, 5750, Doors.CLOSED)
puerta3.Squezze = 1

puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-500
puerta3.o_med_displ=4000


puerta3.closetype=Doors.AC
puerta3.c_init_displ=4000
puerta3.c_med_vel=16000


puerta3.SetWhileOpenSound(maderadesliz)
puerta3.SetEndOpenSound(maderagolpe)


puerta3.SetWhileCloseSound(maderadesliz)
puerta3.SetEndCloseSound(maderagolpe2)


###llave3 abrepuerta del almacen despues de las mazmorras. Esta con el muerto de los bichitos###


cerradurp3=Locks.PlaceLock("cerradurp3","Cerraduracutre",(-127863.176852,3568.350091,38718.646319),(0.500000,0.500000,0.500000,-0.500000),3.0)
cerradurp3.key="llave3"


cerradurp3.OnUnLockFunc=AbrePuertaLlave3
cerradurp3.OnUnLockArgs=()

cerradurp3.OnLockFunc=CierraPuertaLlave3
cerradurp3.OnLockArgs=()

darfuncs.SetHint(cerradurp3.obj,"Store Lock")


o=Bladex.CreateEntity("llave3","Llavecutre",-154151.508147, 14223.9556277, 46118.353)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000
Stars.Twinkle("llave3")
darfuncs.SetHint(o,"Store Key")

sspl33=Bladex.GetSector(-79754.3550954, -7868.72272905, 66913.56)
sspl33.OnEnter=CierraPuertaLlave33



########################################
##### Puertas 4 y 5.  Salida al patio 1. Reentrada a las mazmorras   #####

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta4=Doors.CreateDoor("Puerta4", (-83750,-8750,72000), (0,1,0), 0, 4000, Doors.CLOSED)
puerta4.Squezze = 1

puerta4.opentype=Doors.UNIF
puerta4.o_med_vel=-500
puerta4.o_med_displ=4000


puerta4.closetype=Doors.AC
puerta4.c_init_displ=4000
puerta4.c_med_vel=16000


puerta4.SetWhileOpenSound(maderadesliz)
puerta4.SetEndOpenSound(maderagolpe)

puerta4.SetWhileCloseSound(maderadesliz)
puerta4.SetEndCloseSound(maderagolpe2)



maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")

puerta5=Doors.CreateDoor("Puerta5", (-72250,-8000,74250), (0,1,0), 0, 4500, Doors.CLOSED)
puerta5.Squezze = 1

puerta5.opentype=Doors.UNIF
puerta5.o_med_vel=-500
puerta5.o_med_displ=4500


puerta5.closetype=Doors.AC
puerta5.c_init_displ=4500
puerta5.c_med_vel=16000


puerta5.SetWhileOpenSound(maderadesliz)
puerta5.SetEndOpenSound(maderagolpe)

puerta5.SetWhileCloseSound(maderadesliz)
puerta5.SetEndCloseSound(maderagolpe2)

###llave45 abre las puertas 4 y 5. La tiene un guardia###


cerradurp4=Locks.PlaceLock("cerradurp4","Cerraduracutre",(-82957.465438,-7961.074879,74742.192663),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradurp4.key="llave45"


cerradurp4.OnUnLockFunc=AbrePuertaLlave4
cerradurp4.OnUnLockArgs=()

cerradurp4.OnLockFunc=CierraPuertaLlave4
cerradurp4.OnLockArgs=()

darfuncs.SetHint(cerradurp4.obj,"Iron Lock")

###

cerradurp5=Locks.PlaceLock("cerradurp5","Cerraduracutre",(-73401.325930,-8079.158707,71283.088834),(0.006171,0.006171,0.707080,-0.707080),3.0)
cerradurp5.key="llave45"


cerradurp5.OnUnLockFunc=AbrePuertaLlave5
cerradurp5.OnUnLockArgs=()

cerradurp5.OnLockFunc=CierraPuertaLlave5
cerradurp5.OnLockArgs=()

darfuncs.SetHint(cerradurp5.obj,"Iron Lock")



o=Bladex.CreateEntity("llave45","Llavecutre",-84250,-6327.856076,40500)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000
o.Data = 2
darfuncs.SetHint(o,"Iron Key")


########################################################################
##########puerta 6. Almacen del patio de la torre de Ragnar#############
########################################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta6=Doors.CreateDoor("Puerta6", (-91000,6000,-99500), (0,1,0), 0, 4000, Doors.CLOSED)
puerta6.Squezze = 1

puerta6.opentype=Doors.UNIF
puerta6.o_med_vel=-500
puerta6.o_med_displ=4000


puerta6.closetype=Doors.AC
puerta6.c_init_displ=4000
puerta6.c_med_vel=5000

puerta6.SetWhileOpenSound(maderadesliz)
puerta6.SetEndOpenSound(maderagolpe)

puerta6.SetWhileCloseSound(maderadesliz)
puerta6.SetEndCloseSound(maderagolpe2)

### Ademas en esta habitacion hay una armadura como recompensa, asi que...

armaduraencontrada=0



########################################################################
##########puerta 9. planta1 de la torre de Ragnar. Se cierra sola#############
########################################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta9=Doors.CreateDoor("Puerta9", (-137250,-7000,-90500), (0,1,0), 1000, 4250, Doors.CLOSED)
puerta9.Squezze = 1

puerta9.opentype=Doors.UNIF
puerta9.o_med_vel=-1000
puerta9.o_med_displ=3250


puerta9.closetype=Doors.AC
puerta9.c_init_displ=3250
puerta9.c_med_vel=5000

puerta9.SetWhileOpenSound(maderadesliz)
puerta9.SetEndOpenSound(maderagolpe)

puerta9.SetWhileCloseSound(maderadesliz)
puerta9.SetEndCloseSound(maderagolpe2)

###llave69 abre la puerta 6 y la puerta 9. La tiene alguien dentro de la torre###
##################################################################

cerradurp6=Locks.PlaceLock("cerradurp6","Cerraduracutre",(-91514.778462,6076.404939,-97287.666247),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradurp6.key="llave69"


cerradurp6.OnUnLockFunc=AbrePuertaLlave6
cerradurp6.OnUnLockArgs=()

cerradurp6.OnLockFunc=CierraPuertaLlave6
cerradurp6.OnLockArgs=()

darfuncs.SetHint(cerradurp6.obj,"Tower Lock")

##################################################################

cerradurp9=Locks.PlaceLock("cerradurp9","Cerraduracutre",(-135387.315561,-6096.250250,-88527.786406),(0.500000,0.500000,0.500000,-0.500000),3.0)
cerradurp9.key="llave69"


cerradurp9.OnUnLockFunc=AbrePuertaLlave9
cerradurp9.OnUnLockArgs=()

cerradurp9.OnLockFunc=CierraPuertaLlave9
cerradurp9.OnLockArgs=()

darfuncs.SetHint(cerradurp9.obj,"Tower Lock")



o=Bladex.CreateEntity("llave69","Llavecutre",-127040.098559,1617.641023,-105496.828495)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000
o.Data = 2
darfuncs.SetHint(o,"Tower Key")

########################################################################
##########puerta 7. Sala de los arcos con bandas#############
########################################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta7=Doors.CreateDoor("Puerta7", (-87000,500,-31250), (0,1,0), 1500, 5750, Doors.CLOSED)
puerta7.Squezze = 1

puerta7.opentype=Doors.UNIF
puerta7.o_med_vel=-500
puerta7.o_med_displ=4250

"""
puerta7.closetype=Doors.AC
puerta7.c_init_displ=4250
puerta7.c_med_vel=7000
"""

puerta7.SetWhileOpenSound(maderadesliz)
puerta7.SetEndOpenSound(maderagolpe)
"""
puerta7.SetWhileCloseSound(maderadesliz)
puerta7.SetEndCloseSound(maderagolpe2)
"""
###llave7 abre la puerta 7. La tiene alguien dentro de la sala octogonal###
###########################################################################

cerradurp7=Locks.PlaceLock("cerradurp7","Cerraduracutre",(-83764.215626,1777.484320,-33524.661116),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradurp7.key="llave7"

cerradurp7.OnUnLockFunc=AbrePuertaLlave7
cerradurp7.OnUnLockArgs=()
"""
cerradurp7.OnLockFunc=CierraPuertaLlave7
cerradurp7.OnLockArgs=()
"""
darfuncs.SetHint(cerradurp7.obj,"Armoury Lock")



o=Bladex.CreateEntity("llave7","Llavecutre",-86918.280796,2976.630982,-34863.485703)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000

darfuncs.SetHint(o,"Armoury Key")

########################################################################
##########puerta 8. Sala del almacen del segundo patio. Palanca#############
########################################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta8=Doors.CreateDoor("Puerta8", (-129750,-8000,38750), (0,1,0), 1500, 5500, Doors.CLOSED)
puerta8.Squezze = 1

puerta8.opentype=Doors.UNIF
puerta8.o_med_vel=-500
puerta8.o_med_displ=4000


puerta8.closetype=Doors.AC
puerta8.c_init_displ=4000
puerta8.c_med_vel=7000


puerta8.SetWhileOpenSound(maderadesliz)
puerta8.SetEndOpenSound(maderagolpe)

puerta8.SetWhileCloseSound(maderadesliz)
puerta8.SetEndCloseSound(maderagolpe2)

##### Accionar puertas al accionar una palanca


palancap8=Levers.PlaceLever("PalancaP8",Levers.LeverType3,(-126260.966300,-6113.997534,36626.459578),(0.707107,0.707107,0.000000,0.000000),1.0)

palancap8.mode=1


palancap8.OnTurnOnFunc=AbrePuerta8
palancap8.OnTurnOnArgs=()

palancap8.OnTurnOffFunc=CierraPuerta8
palancap8.OnTurnOffArgs=()


########################################################################
##########puerta 10. Sala de la torre. Piso 3�#############
########################################################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puerta10=Doors.CreateDoor("Puerta10", (-128000,-14000,-111750), (0,1,0), 1500, 5000, Doors.CLOSED)
puerta10.Squezze = 1

puerta10.opentype=Doors.UNIF
puerta10.o_med_vel=-500
puerta10.o_med_displ=3500

"""
puerta10.closetype=Doors.AC
puerta10.c_init_displ=3500
puerta10.c_med_vel=7000
"""

puerta10.SetWhileOpenSound(maderadesliz)
puerta10.SetEndOpenSound(maderagolpe)
"""
puerta10.SetWhileCloseSound(maderadesliz)
puerta10.SetEndCloseSound(maderagolpe2)
"""
###llave10 abre la puerta 10. La tiene alguien dentro de la torrre###
###########################################################################

cerradurp10=Locks.PlaceLock("cerradurp10","Cerraduracutre",(-128756.914800,-12660.046839,-114511.077255),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradurp10.key="llave10"

cerradurp10.OnUnLockFunc=AbrePuertaLlave10
cerradurp10.OnUnLockArgs=()
"""
cerradurp10.OnLockFunc=CierraPuertaLlave10
cerradurp10.OnLockArgs=()
"""
darfuncs.SetHint(cerradurp10.obj,"Second Tower Lock")



o=Bladex.CreateEntity("llave10","Llavecutre",-133161.732031,-11525.213021,-113645.872297)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000
darfuncs.SetHint(o,"Second Tower Key")



###################################
##### Paso de los patios 1, 2 #####
###################################
##Rastrillo. Paso de los patios con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rastpat=Bladex.CreateEntity("RastPat","Rastrillo2",-93506.868269,-5795.806818,33073.282030,"Physic")
rastpat.Scale=1.347849
rastpat.Orientation=0.707107,0.707107,0.000000,0.000000
rastpat=Sparks.SetMetalSparkling("RastPat")
rastpat.Frozen=1

rastpatdin=Objects.CreateDinamicObject("RastPat")


##### Abrir el rastrillo al accionar una palanca


palancpat=Levers.PlaceLever("PalancPat",Levers.LeverType3,(-99110.657607,-13171.500743,36757.886050),(0.504344,0.504344,0.495618,-0.495618),1.0)

palancpat.mode=3


palancpat.OnTurnOnFunc=Abrerastpat
palancpat.OnTurnOnArgs=()

palancpat.OnTurnOffFunc=Cierrarastpat
palancpat.OnTurnOffArgs=()



##Rastrillo. Al final del puente levadizo##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rastfin=Bladex.CreateEntity("RastFin","Rastrillo2",-104495.077333,-5947.048300,-73074.970156,"Physic")
rastfin.Scale=1.798710
rastfin.Orientation=0.707107,0.707107,0.000000,0.000000
rastfin=Sparks.SetMetalSparkling("RastFin")
rastfin.Frozen=1

rastfindin=Objects.CreateDinamicObject("RastFin")

sr1=Bladex.GetSector(-99500,0,-84250)
sr1.OnEnter=Cierrarastfin


#######
#######puerta del Caballero del Caos######
##################



maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puertacaos=Doors.CreateDoor("PuertaCaos", (-119000,0,-99500), (0,1,0), 1500, 5000, Doors.CLOSED)
puertacaos.Squezze = 1

puertacaos.opentype=Doors.UNIF
puertacaos.o_med_vel=-500
puertacaos.o_med_displ=3500
"""
puertacaos.closetype=Doors.AC
puertacaos.c_init_displ=3500
puertacaos.c_med_vel=7000
"""
puertacaos.SetWhileOpenSound(maderadesliz)
puertacaos.SetEndOpenSound(maderagolpe)
"""
puertacaos.SetWhileCloseSound(maderadesliz)
puertacaos.SetEndCloseSound(maderagolpe2)


sc=Bladex.GetSector(-138750,-7000,-90550)
sc.OnEnter=CierraPuertaCaos
"""



#######################
#######################
######## PUERTA FINAL##
###SALA DE RAGNAR######


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puertaragnar=Doors.CreateDoor("PuertaRagnar", (-142250,-32000,-95250), (0,1,0), 1000, 5000, Doors.OPENED)

puertaragnar.closetype=Doors.AC
puertaragnar.c_init_displ=4000
puertaragnar.c_med_vel=7000

puertaragnar.SetWhileCloseSound(maderadesliz)
puertaragnar.SetEndCloseSound(maderagolpe2)


#######RASTRILLO SECRETO RAGNAR


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rastrag=Bladex.CreateEntity("RastRag","Rastrillo",-133896.547000,-32188.615000,-90728.480000,"Physic")
rastrag.Scale=0.658419
rastrag.Orientation=0.500000,0.500000,0.500000,-0.500000
rastrag=Sparks.SetMetalSparkling("RastRag")
rastrag.Frozen=1

rastragdin=Objects.CreateDinamicObject("RastRag")



###llave que abre el rastrillo ragnar


cerradurfin=Locks.PlaceLock("cerradurfin","Cerraduracobox",(-132993.165255,-31606.005571,-89309.311947),(0.707107,0.707107,0.000000,0.000000),1.5)
cerradurfin.key="llaverag"


cerradurfin.OnUnLockFunc=Abrerastrag
cerradurfin.OnUnLockArgs=()
cerradurfin.OnLockFunc=Cierrarastrag
cerradurfin.OnLockArgs=()

darfuncs.SetHint(cerradurfin.obj,"Ragnar Lock")



o=Bladex.CreateEntity("llaverag","Llavecobox",-130634.811458,-30524.391957,-90038.124563)
o.Static=0
o.Scale=1.0
o.Orientation=0.999453,-0.016495,-0.028670,0.000210

darfuncs.SetHint(o,"Ragnar Key")


####################
####################
###########PUERTA EN EL PATIO DE LOS TRES CABALLEROS

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/golpe-madera-pesada.wav", "MaderaGolpe2")


puertatres=Doors.CreateDoor("PuertaTres", (-121000,-7000,48000), (0,0,1), 0, 3500, Doors.CLOSED)

puertatres.opentype=Doors.UNIF
puertatres.o_med_vel=-500
puertatres.o_med_displ=3500

puertatres.SetWhileOpenSound(maderadesliz)
puertatres.SetEndOpenSound(maderagolpe)
