##///
##||| ORC_M9/puertorc.PY TITANIUM
##||| Change list:
##||| * Lock to bottom floor cells now can actually be closed preventing players from keeping it open after descending.
##\\\ 

import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import darfuncs
import Stars

###### Definici�n de los sonidos de todas las puertas -incluyendo las objeto-


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


##### Mazmorras #####

puerta333=Bladex.CreateEntity("Puerta333","Rastrillo10",10229.207651,32097.587466,28438.715294,"Physic")
puerta333.Scale=0.914340
puerta333.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Puerta333")

puerta333din=Objects.CreateDinamicObject("Puerta333")


##definici�n rastrillos: 3 puertas con cerraduras propias que se abren con la misma llave##




rastmaz2=Bladex.CreateEntity("RastMaz2","Rastrillo2",28905.960065,49697.688972,31279.021333)
rastmaz2.Static=0
rastmaz2.Scale=0.685153
rastmaz2.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("RastMaz2")

rastmaz2din=Objects.CreateDinamicObject("RastMaz2")


rastmaz3=Bladex.CreateEntity("RastMaz3","Rastrillo2",28875,49697.688972,25500)
rastmaz3.Static=0
rastmaz3.Scale=0.685153
rastmaz3.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("RastMaz3")

rastmaz3din=Objects.CreateDinamicObject("RastMaz3")

##funciones abrir-cerrar##





###cerraduras rastrillos###




##cerradura 2##

cerradura2=Locks.PlaceLock("cerradura2","Cerraduracutre",(27742.021758,50432.984338,29090.599816),(0.000000,0.000000,0.707107,-0.707107),2.5)
cerradura2.key="llave88"
darfuncs.SetHint(cerradura2.obj,"Cells Lock")


cerradura2.OnUnLockFunc=Abrerastmaz2
cerradura2.OnUnLockArgs=()


cerradura2.OnLockFunc=Cierrarastmaz2
cerradura2.OnLockArgs=()



##cerradura 3##

cerradura3=Locks.PlaceLock("cerradura3","Cerraduracutre",(27742.021758,50432.984338,23090.599816),(0.000000,0.000000,0.707107,-0.707107),2.5)
cerradura3.key="llave88"
darfuncs.SetHint(cerradura3.obj,"Cells Lock")


cerradura3.OnUnLockFunc=Abrerastmaz3
cerradura3.OnUnLockArgs=()

cerradura3.OnLockFunc=Cierrarastmaz3
cerradura3.OnLockArgs=()





####################
####################
###puerta de madera puerta2
###############
##########################


puerta3=Bladex.CreateEntity("Puerta3","Rastrillo2",29086.460455,44237.719855,20015.324578)
puerta3.Static=0
puerta3.Scale=1.000000
puerta3.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Puerta3")

puerta3din=Objects.CreateDinamicObject("Puerta3")





###llave3


cerradurp3=Locks.PlaceLock("cerradurp3","Cerraduracutre",(28200,45000,18250),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradurp3.key="llave88"
darfuncs.SetHint(cerradurp3.obj,"Cells Lock")


cerradurp3.OnUnLockFunc=AbrePuertaLlave3
cerradurp3.OnUnLockArgs=()

## PLAGUE: Why was this originally commented out?
cerradurp3.OnLockFunc=CierraPuertaLlave3
cerradurp3.OnLockArgs=()


##Llave mazmorras##

o=Bladex.CreateEntity("llave333","Llavecutre",21250,45800,17000)
o.Static=0
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.Data=1
darfuncs.SetHint(o,"Dungeon Key")




##################

####################
####################
### reja del mural con el pulsador
###############
##########################






rastmur=Bladex.CreateEntity("RastMur","Rastrillo",-5779.614537,17418.840852,46366.164197)
rastmur.Static=0
rastmur.Scale=0.960980
rastmur.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("RastMur")






##################

####################
####################
### MAZMORRAS. La llave la tiene el Jefe Orco.
###############
##########################



###llave333 abrepuerta

cerradurp333=Locks.PlaceLock("cerradurp333","Cerraduracutre",(12881.027697,32709.955953,29394.895916),(0.500000,0.500000,-0.500000,0.500000),4.0)
cerradurp333.key="llave333"


cerradurp333.OnUnLockFunc=AbrePuertaLlave333
cerradurp333.OnUnLockArgs=()

## PLAGUE: Func below doesn't exist. It could be abused for fights, as such, override OnUnLockFunc after it has already been used in DefFuncs.
#cerradurp333.OnLockFunc=CierraPuertaLlave333
#cerradurp333.OnLockArgs=()
darfuncs.SetHint(cerradurp333.obj,"Dungeon Lock")

#############torre de la derecha


##Rastrillo.  con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast6=Bladex.CreateEntity("Rast6","Rastrillo",26265.875878,28748.060306,58005.657171)
rast6.Static=1
rast6.Scale=0.932718
rast6.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Rast6")

rast6din=Objects.CreateDinamicObject("Rast6")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca


palanc6=Levers.PlaceLever("Palanc6",Levers.LeverType3,(28381.619396,30090.115561,61861.475966),(0.500000,0.500000,0.500000,-0.500000),1.0)
palanc6.mode=3


palanc6.OnTurnOnFunc=Abrerast6
palanc6.OnTurnOnArgs=()

palanc6.OnTurnOffFunc=Cierrarast6
palanc6.OnTurnOffArgs=()
















#############ULTIMA

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta444=Doors.CreateDoor("Puerta444", (10250,53000,46125), (0,1,0), 0, 5000, Doors.CLOSED)


puerta444.opentype=Doors.UNIF
puerta444.o_med_vel=-500
puerta444.o_med_displ=5000

puerta444.SetWhileOpenSound(maderadesliz)
puerta444.SetEndOpenSound(maderagolpe)



cerradurp444=Locks.PlaceLock("cerradurp444","Cerraduracutre",(12184.952225,55660.740206,47534.104990),(0.183013,0.183013,-0.683013,0.683013),4.0)
cerradurp444.key="llave444"

cerradurp444.OnUnLockFunc=AbrePuertaLlave444
cerradurp444.OnUnLockArgs=()

o=Bladex.CreateEntity("llave444","Llavecutre",26250,50800,31000)
o.Static=0
o.Scale=1.0
o.Orientation=0.707107,0.707107,0.000000,0.000000


#######
#######RASTRILLOS DE LAS TORRES

##Rastrillo.  con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

RASTORRE1=Bladex.CreateEntity("RASTORRE1","Rastrillo2",-5777.327000,14756.295000,57906.515000)
RASTORRE1.Static=1
RASTORRE1.Scale=1
RASTORRE1.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("RASTORRE1")

RASTORRE1din=Objects.CreateDinamicObject("RASTORRE1")

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

RASTORRE2=Bladex.CreateEntity("RASTORRE2","Rastrillo2",26189.555000,14735.603000,57832.038000)
RASTORRE2.Static=1
RASTORRE2.Scale=1
RASTORRE2.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("RASTORRE2")

RASTORRE2din=Objects.CreateDinamicObject("RASTORRE2")

##funciones abrir-cerrar##


palancRASTORRE2=Levers.PlaceLever("PalancRASTORRE2",Levers.LeverType3,(8284.143703,20057.397295,32631.707157),(0.006171,0.006171,-0.707080,0.707080),1.0)
palancRASTORRE2.mode=2


palancRASTORRE2.OnTurnOnFunc=AbreLosDosRatrillosTorre
palancRASTORRE2.OnTurnOnArgs=()




#############
#############
##PUERTA DEL JEFE ORCO

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertaJEFE=Doors.CreateDoor("puertaJEFE", (6750,18000,40750), (0,1,0), 700, 4700, Doors.CLOSED)


puertaJEFE.opentype=Doors.UNIF
puertaJEFE.o_med_vel=-1000
puertaJEFE.o_med_displ=4000

puertaJEFE.SetWhileOpenSound(maderadesliz)
puertaJEFE.SetEndOpenSound(maderagolpe)




##########################

##ESTABLECEMOS LOS SONIDOS QUE TENDR� EL ELEVADOR

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")

##CREAMOS LA BARRA ELEVADORA -no tiene por que ser una sola, podr�an ser varias-

columnaelevador=Doors.CreateDoor("ColumnaElevador", (33000,45000,48000), (0, -1, 0), 0, 6900, Doors.OPENED)

##ESTABLECEMOS LOS TRAMOS DE MOVIMIENTO

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=5900
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=5900
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500



enmarcha=0



columnaelevador.OnEndCloseFunc=EsperaYBajaElevador
columnaelevador.OnEndOpenFunc=ElevadorArriba

##CREAMOS LA PALANCA
##### Accionar puertas al accionar una palanca
palanELE=Levers.PlaceLever("PalanELE",Levers.LeverType3,(31388.910082,40576.057382,44962.182391),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanELE2=Levers.PlaceLever("PalanELE2",Levers.LeverType3,(32857.529755,47686.662469,45935.121289),(0.000000,0.000000,0.707107,-0.707107),1.0)

palanELE.mode=1
palanELE2.mode=1

palanELE.OnTurnOnFunc=CierraPuertaELE
palanELE.OnTurnOnArgs=()

palanELE2.OnTurnOffFunc=CierraPuertaELE
palanELE2.OnTurnOffArgs=()



###########
#####puerta del principio

############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertar3=Doors.CreateDoor("Puertar3", (53000,48000,-2000), (0,1,0), 500, 4000, Doors.CLOSED)
puertar3.Squezze = 1

puertar3.opentype=Doors.UNIF
puertar3.o_med_vel=-800
puertar3.o_med_displ=3500




puertar3.SetWhileOpenSound(maderadesliz)
puertar3.SetEndOpenSound(maderagolpe)


###llaver3 abrepuertar3###


cerradurpr3=Locks.PlaceLock("cerradurpr3","Cerraduracutre",(51387.145629,48744.624189,-2515.455364),(0.491198,0.491198,0.508650,-0.508650),3.0)
cerradurpr3.key="llaver3"


cerradurpr3.OnUnLockFunc=AbrePuertaLlaver3
cerradurpr3.OnUnLockArgs=()


darfuncs.SetHint(cerradurpr3.obj,"Store Lock")


o=Bladex.CreateEntity("llaver3","Llavecutre",51231.681570,48510.273959,-3161.332565,"Physic")
o.Scale=1.0
o.Orientation=0.044459,0.987682,-0.008945,0.149756
darfuncs.SetHint(o,"Store Key")


#######################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


puerta1=Bladex.CreateEntity("Puerta1","Rastrillo2",-5736.086657,29226.631944,58029.125137,"Physic")
puerta1.Scale=1.0
puerta1.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Puerta1")

puerta1din=Objects.CreateDinamicObject("Puerta1")



###cerradura rastrillos###

##cerradura ##

cerradurabu=Locks.PlaceLock("cerradurabu","Cerraduracutre",(-8318.548596,30780.203024,57489.631933),(0.495618,0.495618,0.504344,-0.504344),3.0)
cerradurabu.key="llave1"


cerradurabu.OnUnLockFunc=Abrepuerta1
cerradurabu.OnUnLockArgs=()

cerradurabu.OnLockFunc=Cierrapuerta1
cerradurabu.OnLockArgs=()

darfuncs.SetHint(cerradurabu.obj,"Iron Lock")

##Llave 1##

o=Bladex.CreateEntity("llave1","Llavecutre",-6995.736326,30602.306670,55847.061683,"Physic")
o.Scale=1.0
o.Orientation=0.997457,-0.008145,-0.070589,-0.005438
darfuncs.SetHint(o,"Iron Key")

#################################################################################################3
########
########puerta de la entrada a las mazmorras palanca


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")

puerta8=Doors.CreateDoor("Puerta8", (-8000,45000,59000), (0,1,0), 1250, 7250, Doors.CLOSED)
puerta8.Squezze = 1

puerta8.opentype=Doors.UNIF
puerta8.o_med_vel=-500
puerta8.o_med_displ=6000



puerta8.SetWhileOpenSound(maderadesliz)
puerta8.SetEndOpenSound(maderagolpe)


##### Accionar puertas al accionar una palanca


palancap8=Levers.PlaceLever("PalancaP8",Levers.LeverType3,(-9619.865021,48031.192835,60570.281677),(0.500000,0.500000,-0.500000,0.500000),1.0)

palancap8.mode=1

palancap8.OnTurnOnFunc=AbrePuerta8
palancap8.OnTurnOnArgs=()

#################################################################################################3
########
########puerta de la salida de las mazmorras palanca

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puerta88=Doors.CreateDoor("Puerta88", (-5750,45000,21250), (0,1,0), 1000, 6250, Doors.CLOSED)
puerta88.Squezze = 1

puerta88.opentype=Doors.UNIF
puerta88.o_med_vel=-500
puerta88.o_med_displ=5250


puerta88.SetWhileOpenSound(maderadesliz)
puerta88.SetEndOpenSound(maderagolpe)


###llave88 abrepuerta del almacen despues de las mazmorras. Esta con el  T R O L L  ###


cerradurp88=Locks.PlaceLock("cerradurp88","Cerraduracutre",(-7739.244583,47443.709470,22689.731388),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradurp88.key="llave88"


cerradurp88.OnUnLockFunc=AbrePuertaLlave88
cerradurp88.OnUnLockArgs=()



darfuncs.SetHint(cerradurp88.obj,"Cells Lock")


o=Bladex.CreateEntity("llave88","Llavecutre",-4683.32169737, 47748.1857413, 22556.469)
o.Static=0
o.Scale=1.0
o.Orientation=0.998135,0.061049,0.000000,0.000000
o.Data=5
Stars.Twinkle("llave88")
darfuncs.SetHint(o,"Cells Key")

#######################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


puerta0=Bladex.CreateEntity("Puerta0","Rastrillo2",9909.999000,40406.442000,38020.654000,"Physic")
puerta0.Scale=1.149474
puerta0.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Puerta0")

puerta0din=Objects.CreateDinamicObject("Puerta0")

##funciones abrir-cerrar##





###cerradura rastrillos###

##cerradura ##

cerradura0=Locks.PlaceLock("cerradura0","Cerraduracutre",(8274.990690,41534.188640,36955.218098),(0.707107,0.707107,0.000000,0.000000),3.0)
cerradura0.key="llave88"


cerradura0.OnUnLockFunc=Abrepuerta0
cerradura0.OnUnLockArgs=()

cerradura0.OnLockFunc=Cierrapuerta0
cerradura0.OnLockArgs=()

darfuncs.SetHint(cerradura0.obj,"Cells Lock")