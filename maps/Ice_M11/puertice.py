##///
##||| Ice_M11/puertice.PY TITANIUM
##||| * Fixed Minorx not having default deadfunc being executed
##||| * Restored missing elevator sound
##\\\ 

import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import Button
import AniSound
import Reference
import EnemyTypes
import Breakings
import Stars
import darfuncs
import pocimac
import Ontake
import OnOff

#####################################
###      puerta del elevador      ###
#####################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta0=Doors.CreateDoor("Puerta0", (-29060,9000,57120), (0,1,0), 1500, 5200, Doors.CLOSED)


puerta0.opentype=Doors.UNIF
puerta0.o_med_vel=-500
puerta0.o_med_displ=3700


puerta0.closetype=Doors.AC
puerta0.c_init_displ=3700
puerta0.c_med_vel=8000


puerta0.SetWhileOpenSound(maderadesliz)
puerta0.SetEndOpenSound(maderagolpe)


puerta0.SetWhileCloseSound(maderadesliz)
puerta0.SetEndCloseSound(maderagolpe)


_SndRugido=Sounds.CreateEntitySound("../../Sounds/rugido-demon2.wav","RugidoPuertice")
_SndRugido.MaxDistance=1000000.0


###llave0. La tiene un guardia###


cerradurp0=Locks.PlaceLock("cerradurp0","Cerraduracutre",(-25851.826201,9949.879220,55082.827184),(0.500000,0.500000,0.500000,-0.500000),3.0)
cerradurp0.key="llave0"


cerradurp0.OnUnLockFunc=AbrePuertaLlave0
cerradurp0.OnUnLockArgs=()

cerradurp0.OnLockFunc=CierraPuertaLlave0
cerradurp0.OnLockArgs=()

darfuncs.SetHint(cerradurp0.obj,"Store Lock")

o=Bladex.CreateEntity("llave0","Llavecutre",-26476.267883,10975.332157,52426.171795,"Physic")
o.Scale=1.0
o.Orientation=0.998582,0.017206,-0.050348,-0.001426
darfuncs.SetHint(o,"Store Key")

####################11111111111111
####################11111111111111
###puerta de la entrada a lo que en su dia fue el cementerio
###############
##########################

"""
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puerta1=Doors.CreateDoor("Puerta1", (18900,-2000,63500), (0,1,0), 1750, 6750, Doors.CLOSED)


puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-500
puerta1.o_med_displ=5000


puerta1.closetype=Doors.AC
puerta1.c_init_displ=5000
puerta1.c_med_vel=9000


puerta1.SetWhileOpenSound(maderadesliz)
puerta1.SetEndOpenSound(maderagolpe)


puerta1.SetWhileCloseSound(maderadesliz)
puerta1.SetEndCloseSound(maderagolpe)
"""
###############
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puert11=Doors.CreateDoor("Puert11", (55100,-2000,91700), (0,1,0), 2500, 7000, Doors.CLOSED)


puert11.opentype=Doors.UNIF
puert11.o_med_vel=-500
puert11.o_med_displ=4500


puert11.SetWhileOpenSound(maderadesliz)
puert11.SetEndOpenSound(maderagolpe)



###llave1. La tiene un guardia###

"""
cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(14462.013000,-1573.245000,67298.070000),(0.582745,0.582745,-0.400510,0.400510),3.0)
cerradurp1.key="llave1"


cerradurp1.OnUnLockFunc=AbrePuertaLlave1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=CierraPuertaLlave1
cerradurp1.OnLockArgs=()
darfuncs.SetHint(cerradurp1.obj,"Courtyard Lock")
"""


############

cerradur11=Locks.PlaceLock("cerradur11","Cerraduracutre",(53631.611497,-1189.062591,88674.492274),(0.000000,0.000000,0.707107,-0.707107),3.0)
cerradur11.key="llave1"

cerradur11.OnUnLockFunc=AbrePuertaLlav11
cerradur11.OnUnLockArgs=()
darfuncs.SetHint(cerradur11.obj,"Courtyard Lock")


o=Bladex.CreateEntity("llave1","Llavecutre",7756.751021,-1140.881498,115471.564567,"Physic")
o.Scale=1.0
o.Orientation=0.869976,-0.011644,-0.492759,-0.013981
darfuncs.SetHint(o,"Courtyard Key")
Stars.Twinkle("llave1")

####################vid
####################vid
###puerta de la sala de las vidrieras###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertavid=Doors.CreateDoor("Puertavid", (-11625,-3000,21937), (0,1,0), 2000, 7800, Doors.CLOSED)


puertavid.opentype=Doors.UNIF
puertavid.o_med_vel=-500
puertavid.o_med_displ=5800


puertavid.closetype=Doors.AC
puertavid.c_init_displ=5800
puertavid.c_med_vel=8000


puertavid.SetWhileOpenSound(maderadesliz)
puertavid.SetEndOpenSound(maderagolpe)


puertavid.SetWhileCloseSound(maderadesliz)
puertavid.SetEndCloseSound(maderagolpe)


###llavevid. La tiene un guardia###


cerradurpvid=Locks.PlaceLock("cerradurpvid","Cerraduracutre",(-14191.233548,52.055610,24911.719622),(0.500000,0.500000,0.500000,-0.500000),3.0)
cerradurpvid.key="llavevid"


cerradurpvid.OnUnLockFunc=AbrePuertaLlavevid
cerradurpvid.OnUnLockArgs=()

cerradurpvid.OnLockFunc=CierraPuertaLlavevid
cerradurpvid.OnLockArgs=()
darfuncs.SetHint(cerradurpvid.obj,"Palace Lock")

o=Bladex.CreateEntity("llavevid","Llavecutre",-13870,0,21900,"Physic")
o.Scale=1.0
o.Orientation=0.998582,0.017206,-0.050348,-0.001426
darfuncs.SetHint(o,"Palace Key")

############################################################
##########-PUERTA-6. Rastrillo del patio del templete.
############################################################
############################################################
############################################################
############################################################


##Rastrillo.  con la palanca##

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rast6=Bladex.CreateEntity("Rast6","Rastrillo",87215.352992,-3908.604964,58571.628139)
rast6.Static=1
rast6.Scale=0.712973
rast6.Orientation=0.500000,0.500000,0.500000,-0.500000
Sparks.SetMetalSparkling("Rast6")

rast6din=Objects.CreateDinamicObject("Rast6")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca


palanc6=Levers.PlaceLever("Palanc6",Levers.LeverType3,(85918.583269,-2807.269153,55204.682936),(0.500000,0.500000,0.500000,-0.500000),1.0)
palanc6.mode=3


palanc6.OnTurnOnFunc=Abrerast6
palanc6.OnTurnOnArgs=()

palanc6.OnTurnOffFunc=Cierrarast6
palanc6.OnTurnOffArgs=()


####################toro2
####################toro2
###puerta del toro2###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertatoro2=Doors.CreateDoor("Puertatoro2", (70000,-2000,18250), (0,0,-1), 0, 3750, Doors.CLOSED)


puertatoro2.opentype=Doors.UNIF
puertatoro2.o_med_vel=-500
puertatoro2.o_med_displ=3750


puertatoro2.SetWhileOpenSound(maderadesliz)
puertatoro2.SetEndOpenSound(maderagolpe)


###palancas dos palancas abren la puerta###




palancatoro2=Levers.PlaceLever("Palancatoro2",Levers.LeverType3,(69129.107610,-956.603963,20687.019396),(0.500000,0.500000,0.500000,-0.500000),1.0)
palancatoro2.mode=1

palancatoro2.OnTurnOnFunc=AbrePuertaLlavetoro2
palancatoro2.OnTurnOnArgs=()

palanca1toro2=Levers.PlaceLever("Palanca1toro2",Levers.LeverType3,(70889.119179,-861.221068,15993.877340),(0.500000,0.500000,-0.500000,0.500000),1.0)
palanca1toro2.mode=1

palanca1toro2.OnTurnOnFunc=AbrePuertaLlavetoro2
palanca1toro2.OnTurnOnArgs=()



#######################################################
########## PUERTA DE LA SALA DE LA TABLILLA ###########
#######################################################

piedradesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "PiedraDesliz")
piedragolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "PiedraGolpe")


#escalon 1a
puerta1a=Doors.CreateDoor("Puerta1a", (44680,-3500,17400), (0,1,0), 2000, 7000, Doors.CLOSED)

puerta1a.opentype=Doors.UNIF
puerta1a.o_med_vel=-500
puerta1a.o_med_displ=7000

puerta1a.closetype=Doors.UNIF
puerta1a.c_med_vel=900
puerta1a.c_med_displ=7000


puerta1a.SetWhileOpenSound(piedradesliz)
puerta1a.SetEndOpenSound(piedragolpe)

o=Bladex.CreateEntity("bloque1","Bloque",44815.936676,-9504.976973,26984.732126,"Physic")
o.Scale=1.780901
o.Orientation=0.500000,0.500000,0.500000,-0.500000





button=Button.CreateButtonCombination(0,Abrep1,"")
button.AddButton("bloque1",3,(0,0,1),-400,0,0,1)


#o=Bladex.CreateEntity("bloquet","Adoquinpulsador",44815.936676,-9504.976973,26984.732126)
#o.Static=0
#o.Scale=1.780901
#o.Orientation=0.500000,0.500000,0.500000,-0.500000




####################gran
####################gran
###PUERTA DE LA CASETA DEL MINOTAURO QUE ROMPE LAS CAJAS###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertamino=Doors.CreateDoor("Puertamino", (69300,-2000,-1480), (0,1,0), 0, 3500, Doors.OPENED)


puertamino.opentype=Doors.UNIF
puertamino.o_med_vel=-500
puertamino.o_med_displ=3500


puertamino.closetype=Doors.AC
puertamino.c_init_displ=3500
puertamino.c_med_vel=8000


puertamino.SetWhileOpenSound(maderadesliz)
puertamino.SetEndOpenSound(maderagolpe)


puertamino.SetWhileCloseSound(maderadesliz)
puertamino.SetEndCloseSound(maderagolpe)


s22=Bladex.GetSector(75713.8612552, -1100.21951583, -631.188)
s22.OnEnter=CierraPuertaMino


####################gran
####################gran
###puerta despu�s de los graneros. Se abre sola###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertagran=Doors.CreateDoor("Puertagran", (42250,-3000,-12000), (0,1,0), 3000, 7500, Doors.CLOSED)

puertagran.opentype=Doors.UNIF
puertagran.o_med_vel=-1500
puertagran.o_med_displ=4500

puertagran.closetype=Doors.AC
puertagran.c_init_displ=4500
puertagran.c_med_vel=8000

puertagran.SetWhileOpenSound(maderadesliz)
puertagran.SetEndOpenSound(maderagolpe)

puertagran.SetWhileCloseSound(maderadesliz)
puertagran.SetEndCloseSound(maderagolpe)

cerradurpgran=Locks.PlaceLock("cerradurpvid","Cerraduracutre",(45300.941000,-1081.159000,-15874.495000),(0.599660,0.599660,-0.374710,0.374710),3.0)
cerradurpgran.key="llavetoro2"


cerradurpgran.OnUnLockFunc=AbrePuertaGran
cerradurpgran.OnUnLockArgs=()

sen=Bladex.GetSector(29000,200,-11550)
sen.OnEnter=CierraPuertaGran

darfuncs.SetHint(cerradurpgran.obj,"Copper Lock")


o=Bladex.CreateEntity("llavetoro2","Llavecutre",68119.613444,174.603304,20875.606938,"Physic")
o.Scale=1.0
o.Orientation=0.999679,-0.017201,-0.018596,0.000196
darfuncs.SetHint(o,"Copper Key")



ambiente2 = darfuncs.E_Grup()
ambiente2.OnDeath = Suenamusica2

garrote=Bladex.CreateEntity("IceMinGarropin1","Hachacarnicero",0,0,0,"Weapon")

Minorx=Bladex.CreateEntity("Minorx","Minotaur",86727, -874, 2561,"Person")
Minorx.Angle = 2.8
Minorx.Level = 12
AniSound.AsignarSonidosMinotaur("Minorx")

EnemyTypes.EnemyDefaultFuncs(Minorx)
Actions.TakeObject(Minorx.Name,"IceMinGarropin1")
Minorx.Data.OldDeadFunc = Minorx.ImDeadFunc         # Add
Minorx.ImDeadFunc = DieFukingMinorx
Minorx.Deaf = 1
Minorx.Blind = 1

ambiente2.AddGuy(Minorx.Name)
ambiente2.OnDeath = Suenamusica2

ktrai1 = CreaTraidor(67870.1968068, -872.18208274, -2346.05255751,4.65536125638,"jodedor1")
Actions.TakeObject(ktrai1.Name,"llavetoro2")

ambiente2.AddGuy(ktrai1.Name)
ambiente2.OnDeath = Suenamusica2

ktrai2 = CreaTraidor(67331.4347426, -874.853759665, 575.618283226,4.65536125638,"jodedor2")

ambiente2.AddGuy(ktrai2.Name)
ambiente2.OnDeath = Suenamusica2

# char.Position = 69300,-2000,-1480


Barrilazos = [0,0,0]

CreateBarril()


###### TROZO DE MURO QUE SE CIERRA ANTES DEL DEMONIO



puerta3=Doors.CreateDoor("Puerta3", (35750,-10000,-18500), (0,1,0), 0, 5800, Doors.OPENED)


### PLAGUE: 
puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-1600
puerta3.o_med_displ=5800
###   -LeadHead

puerta3.closetype=Doors.AC
puerta3.c_init_displ=5800
puerta3.c_med_vel=16000



puerta3.SetWhileCloseSound(piedradesliz)
puerta3.SetEndCloseSound(piedragolpe)


###llave3





sen=Bladex.GetSector(26250,-10000,-23500)
sen.OnEnter=CierraPuertaLlave3



#------------------------------------------------------------------#
#                        Pa' que aprenda!                          #
#------------------------------------------------------------------#
import dust
import Sounds

dust.intensidad = 140                           # pps
dust.SetPolvinColor(255,255,255)                # snow winds

WindSound = Sounds.CreateEntitySound("../../Sounds/M-rafaga-viento.wav", "CasualWind")

Efepolvo = dust.WindFX(8571, -872, 113448)      # sector as params
Efepolvo.SetSound(WindSound)                    # coolsound
Efepolvo.SetGenerationPoint(-2655, -200, 105963)
Efepolvo.SetWindVector(5000,-700)               # This way is the win
Efepolvo.Variance = 2                           # 3 of 1 time



Efepolvo2 = dust.WindFX(-61781.548988, 22890.9249997, 52172.491)      # sector as params
Efepolvo2.SetSound(WindSound)                    # coolsound
Efepolvo2.SetGenerationPoint(-61000, 23600, 51200)
Efepolvo2.SetWindVector(-5000,700)               # This way is the win
Efepolvo2.Variance = 1                           # 3 of 1 time




Efepolvo3 = dust.WindFX(33753.2642702, -1115.06004133, 93862.420)
Efepolvo3.SetSound(WindSound)
Efepolvo3.SetGenerationPoint(40300, -114, 87900)
Efepolvo3.SetWindVector(500,700)
Efepolvo3.Variance = 1


Efepolvo4 = dust.WindFX(55889.2642702, -2212.06004133, 74912.420)
Efepolvo4.SetSound(WindSound)
Efepolvo4.SetGenerationPoint(61300, -1224, 75900)
Efepolvo4.SetWindVector(500,700)
Efepolvo4.Variance = 1


Efepolvo5 = dust.WindFX(69489.2642702, -912.06004133, -13912.420)
Efepolvo5.SetSound(WindSound)
Efepolvo5.SetGenerationPoint(60500, -114, -9400)
Efepolvo5.SetWindVector(1000,-7000)
Efepolvo5.Variance = 0


Efepolvo6 = dust.WindFX(93489.2642702, -6302.06004133, 26412.420)
Efepolvo6.SetSound(WindSound)
Efepolvo6.SetGenerationPoint(94600, -5414, 21800)
Efepolvo6.SetWindVector(-8000,-100)
Efepolvo6.Variance = 0


Efepolvo7 = dust.WindFX(93989.2642702, -6302.06004133, 37712.420)
Efepolvo7.SetSound(WindSound)
Efepolvo7.SetGenerationPoint(95400, -6414, 35000)
Efepolvo7.SetWindVector(-8000,-100)
Efepolvo7.Variance = 0


Efepolvo8 = dust.WindFX(-18389.2642702, -622.06004133, -1912.420)
Efepolvo8.SetSound(WindSound)
Efepolvo8.SetGenerationPoint(-20900, -614, 3900)
Efepolvo8.SetWindVector(8000,-100)
Efepolvo8.Variance = 0


Efepolvo9 = dust.WindFX(18789.2642702, -9122.06004133, 47712.420)
Efepolvo9.SetSound(WindSound)
Efepolvo9.SetGenerationPoint(20900, -9114, 42770)
Efepolvo9.SetWindVector(-7000,-100)
Efepolvo9.Variance = 0


Efepolvo10 = dust.WindFX(18989.2642702, -9122.06004133, 37712.420)
Efepolvo10.SetSound(WindSound)
Efepolvo10.SetGenerationPoint(21300, -8614, 31870)
Efepolvo10.SetWindVector(-8000,-100)
Efepolvo10.Variance = 0


Efepolvo11 = dust.WindFX(18989.2642702, -9122.06004133, 14712.420)
Efepolvo11.SetSound(WindSound)
Efepolvo11.SetGenerationPoint(21300, -8614, 5170)
Efepolvo11.SetWindVector(-10000,-100)
Efepolvo11.Variance = 0

#------------------------------------------------------------------



###Cuchillas###############
##########################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertablade=Doors.CreateDoor("Puertablade", (26600,8000,40500), (0,0,-1), 0, 4000, Doors.OPENED)


puertablade.opentype=Doors.UNIF
puertablade.o_med_vel=-500
puertablade.o_med_displ=4000


puertablade.closetype=Doors.AC
puertablade.c_init_displ=4000
puertablade.c_med_vel=500


puertablade.SetWhileOpenSound(maderadesliz)
puertablade.SetEndOpenSound(maderagolpe)


puertablade.SetWhileCloseSound(maderadesliz)
puertablade.SetEndCloseSound(maderagolpe)


powp_PP=Bladex.CreateEntity("IcePowPot1","PowerPotion",-1659.763674,10385.372878,9677.275733,"Physic")
powp_PP.Scale=1.000000
powp_PP.Orientation=0.491198,0.491198,-0.508650,0.508650
powp_PP.Solid=1
powp_PP.Scale=1.321291
powp_PP.Orientation=0.707107,0.707107,0.000000,0.000000
pocimac.CreatePowerPotion("IcePowPot1")

luz2_PP=Bladex.CreateEntity("luz2_PP","Entity Spot",-133164.352712,11720.650997,-98637.402867)
luz2_PP.Color=61,233,61
luz2_PP.Intensity=0.2
powp_PP.Link(luz2_PP)


Ontake.AddOnTakeEvent("IcePowPot1",BorraLuz)


##########################

##ESTABLECEMOS LOS SONIDOS QUE TENDR� EL ELEVADOR

loopelevador=Sounds.CreateEntitySound("../../Sounds/drawbridge-loop.wav", "LoopElevador")
golpeelevador=Sounds.CreateEntitySound("../../Sounds/metal-lever3.wav", "GolpeElevador")

##CREAMOS LA BARRA ELEVADORA -no tiene por que ser una sola, podr�an ser varias-

columnaelevador=Doors.CreateDoor("ColumnaElevador", (22700,-2000,36900), (0, -1, 0), 0, 7500, Doors.OPENED)

##ESTABLECEMOS LOS TRAMOS DE MOVIMIENTO

columnaelevador.opentype=Doors.AC_UNIF_DEC
columnaelevador.o_init_vel=0
columnaelevador.o_init_displ=500
columnaelevador.o_med_vel=-2000
columnaelevador.o_med_displ=6500
columnaelevador.o_end_vel=0
columnaelevador.o_end_displ=500

columnaelevador.closetype=Doors.AC_UNIF_DEC
columnaelevador.c_init_vel=0
columnaelevador.c_init_displ=500
columnaelevador.c_med_vel=2000
columnaelevador.c_med_displ=6500
columnaelevador.c_end_vel=0
columnaelevador.c_end_displ=500

columnaelevador.SetWhileOpenSound(loopelevador)     # Added 
columnaelevador.SetEndOpenSound(golpeelevador)      # Restores missing elevator sound
columnaelevador.SetWhileCloseSound(loopelevador)    #
columnaelevador.SetEndCloseSound(golpeelevador)     #       -LeadHead

enmarcha=0



columnaelevador.OnEndCloseFunc=EsperaYBajaElevador
columnaelevador.OnEndOpenFunc=ElevadorArriba

##CREAMOS LA PALANCA
##### Accionar puertas al accionar una palanca
palanELE=Levers.PlaceLever("PalanELE",Levers.LeverType3,(22752.360976,-1117.856397,38607.336268),(0.707107,0.707107,0.000000,0.000000),1.0)
#palanELE2=Levers.PlaceLever("PalanELE2",Levers.LeverType3,(32857.529755,47686.662469,45935.121289),(0.000000,0.000000,0.707107,-0.707107),1.0)

palanELE.mode=1
#palanELE2.mode=1

palanELE.OnTurnOnFunc=CierraPuertaELE
palanELE.OnTurnOnArgs=()

#palanELE2.OnTurnOffFunc=CierraPuertaELE
#palanELE2.OnTurnOffArgs=()

#####################
#####################
######## PUERTA DE LOS ESTABLOS

#################################################################################################3
########
########puerta de la entrada a las mazmorras palanca


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")

puerta8=Doors.CreateDoor("Puerta8", (60750,-2000,8210), (1,0,0), 1250, 5250, Doors.CLOSED)
puerta8.Squezze = 1

puerta8.opentype=Doors.UNIF
puerta8.o_med_vel=-500
puerta8.o_med_displ=4000



puerta8.SetWhileOpenSound(maderadesliz)
puerta8.SetEndOpenSound(maderagolpe)


##### Accionar puertas al accionar una palanca


palancap8=Levers.PlaceLever("PalancaP8",Levers.LeverType3,(57906.862804,-981.314237,10913.185571),(0.500000,0.500000,-0.500000,0.500000),1.0)

palancap8.mode=2

palancap8.OnTurnOnFunc=AbrePuerta8
palancap8.OnTurnOnArgs=()



#######################################


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")


puerta11=Bladex.CreateEntity("Puerta11","Rastrillo",18857.076911,-2401.404770,-4456.967968,"Physic")
puerta11.Scale=0.887449
puerta11.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetMetalSparkling("Puerta11")

puerta11din=Objects.CreateDinamicObject("Puerta11")

##funciones abrir-cerrar##




###########PUERTA final que se abre con medallones


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/dist-dungeon-door2.wav", "MaderaGolpe")


puertaen=Doors.CreateDoor("Puertaen", (18750,-10000,-17250), (0,1,0), 2800, 6800, Doors.CLOSED)
puertaen.Squezze = 1

puertaen.opentype=Doors.UNIF
puertaen.o_med_vel=-500
puertaen.o_med_displ=4000


puertaen.closetype=Doors.AC
puertaen.c_init_displ=4000
puertaen.c_med_vel=8000


puertaen.SetWhileOpenSound(maderadesliz)
puertaen.SetEndOpenSound(maderagolpe)



puertaen.SetWhileCloseSound(maderadesliz)
puertaen.SetEndCloseSound(maderagolpe)


sen=Bladex.GetSector(18750,-10000,-25750)
sen.OnEnter=CierraPuertaLlaveen

###############
maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puert111=Doors.CreateDoor("Puert111", (10750,-2000,115500), (0,0,1), 500, 3250, Doors.CLOSED)


puert111.opentype=Doors.UNIF
puert111.o_med_vel=-500
puert111.o_med_displ=2750


puert111.SetWhileOpenSound(maderadesliz)
puert111.SetEndOpenSound(maderagolpe)

palancall11=Levers.PlaceLever("Palancall11",Levers.LeverType3,(10032.147845,-1143.243876,113269.023804),(0.500000,0.500000,0.500000,-0.500000),1.0)
palancall11.mode=1

palancall11.OnTurnOnFunc=AbrePuertaLlave11
palancall11.OnTurnOnArgs=()

ApagalaSec = Bladex.GetSector(-1139.0786669, 10197.8627111, 29380.897518)
ApagalaSec.OnEnter = Apagala
