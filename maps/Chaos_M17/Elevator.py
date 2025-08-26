##///
##||| CHAOS_M17/Elevator.PY TITANIUM
##||| Change list:
##||| * Spark pass
##\\\ 

import Doors
import Bladex
import Room
import Sounds
import AbreCam
import whrandom
import dust

#################################### Sonidos #############################################

# ELEVADOR 1

SndStartElevador= Sounds.CreateEntitySound("../../Sounds/Stone-lever.wav",        "SonidoInicioElevador")
SndStartElevador.MaxDistance=500000
SndStartElevador.MinDistance=250000
SndStartElevador.Volume=1.0

SndInElevador= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "SonidoElevador")
SndInElevador.MaxDistance=500000
SndInElevador.MinDistance=250000
SndInElevador.Volume=1.0

SndEndElevador= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "SonidoFinElevador")
SndEndElevador.MaxDistance=500000
SndEndElevador.MinDistance=250000
SndEndElevador.Volume=1.0

# PLATAFORMA  1

SndStartPlatA= Sounds.CreateEntitySound("../../Sounds/Stone-lever.wav",        "SonidoInicioPlatA")
SndStartPlatA.MaxDistance=25000
SndStartPlatA.MinDistance=2000
SndStartPlatA.Volume=1.0

SndInPlatA= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "SonidoPlatA")
SndInPlatA.MaxDistance=25000
SndInPlatA.MinDistance=2000
SndInPlatA.Volume=1.0

SndEndPlatA= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "SonidoFinPlatA")
SndEndPlatA.MaxDistance=25000
SndEndPlatA.MinDistance=2000
SndEndPlatA.Volume=1.0

# PLATAFORMA 2

SndStartPlatB= Sounds.CreateEntitySound("../../Sounds/Stone-lever.wav",        "SonidoInicioPlatB")
SndStartPlatB.MaxDistance=25000
SndStartPlatB.MinDistance=2000
SndStartPlatB.Volume=1.0

SndInPlatB= Sounds.CreateEntitySound("../../Sounds/Huge-stone-door.wav",    "SonidoPlatB")
SndInPlatB.MaxDistance=25000
SndInPlatB.MinDistance=2000
SndInPlatB.Volume=1.0

SndEndPlatB= Sounds.CreateEntitySound("../../Sounds/mechanism8.wav",         "SonidoFinPlatB")
SndEndPlatB.MaxDistance=25000
SndEndPlatB.MinDistance=2000
SndEndPlatB.Volume=1.0

#################################### Puertas #############################################

o=Bladex.CreateEntity("Lamp0","Lamparaegipto",525273.253000,90297.186000,57240.434000,"Physic")
o.Scale=1.000000
o.Orientation=0.694658,0.719340,0.000000,0.000000
o.FiresIntensity=[ 0 ]
o.Lights=[ (75.000000,0.300000,(255,165,64)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp1","LamparaNegra",552385.711000,86494.961000,92217.614000)
o.Scale=1.000000
o.Orientation=0.006176,0.006171,0.707080,-0.707080
o.FiresIntensity=[ 0 ]
o.Lights=[ (70.000000,0.100000,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp2","LamparaNegra",504100.681000,87305.410000,92690.537000)
o.Scale=1.000000
o.Orientation=0.707080,0.707080,-0.006171,0.006171
o.FiresIntensity=[ 0 ]
o.Lights=[ (70.000000,0.100000,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp3","LamparaNegra",535463.665000,121283.480000,105156.777000)
o.Scale=1.000000
o.Orientation=0.043168,0.043168,-0.705788,0.705788
o.FiresIntensity=[ 0 ]
o.Lights=[ (100.000000,0.100000,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp4","LamparaNegra",521061.953000,159460.528000,79221.593000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp5","LamparaNegra",541229.802000,199792.018000,85003.659000)
o.Scale=1.000000
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Lamp6","LamparaNegra",514732.393000,240027.528000,84979.111000)
o.Scale=1.000000
o.Orientation=0.504344,0.504344,-0.495618,0.495618
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n

## ascensor abajo
o=Bladex.CreateEntity("Lamp7","LamparaNegra",520975.336000,290228.712000,105252.531000)
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 10 ]
o.Lights=[ (0,0,(255,165,64)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


#
##
###
####
#####
######
#######
########
#########
##########


o=Bladex.CreateEntity("Parita0","Lamparaegipto",534950.005000,297794.506000,147733.200000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,165,64)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Parita1","Lamparaegipto",521466.869000,297793.400000,147708.809000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,165,64)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n



o=Bladex.CreateEntity("Parita2","Lamparaegipto",525074.260000,299544.135000,183538.127000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n




o=Bladex.CreateEntity("Parita3","Lamparaegipto",578541.903, 302048.729125, 183221.196, "Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
o.Mass=15.0
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n



o=Bladex.CreateEntity("Parita4","Lamparaegipto",632557.988000,296300.044000,175151.828000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n



o=Bladex.CreateEntity("Parita5","Lamparaegipto",632452.298000,296306.940000,191225.445000,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,164,62)) ]
Sparks.SetMetalSparkling(o.Name)        # Add
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("Parita6","LamparaNegra",666417.026000,294789.557000,184543.734000)
o.Scale=1.000000
o.Orientation=0.000000,0.000000,0.707107,-0.707107
o.FiresIntensity=[ 20 ]
o.Lights=[ (0,0,(255,155,45)) ]
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n

##########
#########
########
#######
######
#####
####
###
##

import OnOff
import Doors
import Levers
import Locks
import Objects
import Sounds
import EnemyTypes
import PhantonFX

###ELEVADOR MALEFICO

elevador=Doors.CreateDoor("Elevador", (528000,72000,92000), (0,-1,0), 0, 204000, Doors.CLOSED)


elevador.SetInitOpenSound (SndStartElevador)
elevador.SetWhileOpenSound(SndInElevador)
elevador.SetEndOpenSound  (SndEndElevador)



elevador.opentype=Doors.UNIF
elevador.o_med_vel=-3000
elevador.o_med_displ=204000


elevador.closetype=Doors.UNIF
elevador.c_med_vel=3000
elevador.c_med_displ=204000


##funcion que sube y baja el elevador malefico

Bladex.CreateTimer("Elevador",0.5)

AsenderOne=Bladex.GetSector(528993, 94677, 92547)

EndOfTravel = 0  # indica si el asensor termino el trayecto hacia abajo


nChaos = 0

############################################
#   Rayo que crea al caballero del caos    #
############################################

ChaosCounter = 0.0

# Timer del caballero del caos que aparece

Bladex.CreateTimer("ChaosTimer",0.05)

AsenderOne.OnEnter = ActivaAsensor

###PLATAFORMA MALEFICA


plataforma=Doors.CreateDoor("Plataforma", (528000,301000,111000), (0,0,-1), 0, 25000, Doors.OPENED)

plataforma.SetInitOpenSound (SndStartPlatA)
plataforma.SetWhileOpenSound(SndInPlatA)
plataforma.SetEndOpenSound  (SndEndPlatA)


plataforma.SetInitCloseSound (SndStartPlatA)
plataforma.SetWhileCloseSound(SndInPlatA)
plataforma.SetEndCloseSound  (SndEndPlatA)



plataforma.opentype=Doors.UNIF
plataforma.o_med_vel=-2300
plataforma.o_med_displ=25000


plataforma.closetype=Doors.UNIF
plataforma.c_med_vel=2300
plataforma.c_med_displ=25000


AfterBrigeSector         = Bladex.GetSector(528525, 298177, 146410)
AfterBrigeSector.OnEnter = NoPasa


# Aqui se activa la primera arena
FirstArenaActivationSector         = Bladex.GetSector(538571.385831, 300177.1, 183611.632647)
FirstArenaActivationSector.OnEnter = LightArena1


############### Despues de la Arena ###############
platfin=Doors.CreateDoor("Platfin", (626000,302000,183000), (-1,0,0), 0, 16500, Doors.OPENED)

platfin.SetInitOpenSound (SndStartPlatB)
platfin.SetWhileOpenSound(SndInPlatB)
platfin.SetEndOpenSound  (SndEndPlatB)

platfin.SetInitCloseSound (SndStartPlatB)
platfin.SetWhileCloseSound(SndInPlatB)
platfin.SetEndCloseSound  (SndEndPlatB)


platfin.opentype=Doors.UNIF
platfin.o_med_vel=-2300
platfin.o_med_displ=16500


platfin.closetype=Doors.UNIF
platfin.c_med_vel=2300
platfin.c_med_displ=16500


###Puerta tras ultima plataforma malefica


puertafina=Doors.CreateDoor("Puertafina", (650000,300000,185000), (0,0,-1), 0, 6000, Doors.CLOSED)


puertafina.opentype=Doors.UNIF
puertafina.o_med_vel=-2000
puertafina.o_med_displ=6000


puertafina.closetype=Doors.UNIF
puertafina.c_med_vel=2000
puertafina.c_med_displ=6000



puertafinb=Doors.CreateDoor("Puertafinb", (650000,300000,180000), (0,0,1), 0, 6000, Doors.CLOSED)


puertafinb.opentype=Doors.UNIF
puertafinb.o_med_vel=-2000
puertafinb.o_med_displ=6000


puertafinb.closetype=Doors.UNIF
puertafinb.c_med_vel=2000
puertafinb.c_med_displ=6000

#funci�n que sube y baja los escalones de ambos tramos al unisono

StartPortalSector     = Bladex.GetSector(621743, 299927, 182691)


EndPortalSector         = Bladex.GetSector(657000, 299927, 182836)
EndPortalSector.OnEnter = CasiTerminaLaCosa

#char.Position = 528611, 90677, 57322


OnOff.LightSetInens  = 200.0
OnOff.LightSetRadius =   0.03

# char.Position = (529254.127966, 91729.8530637, 65831.5190256)

			     ###              #               ###
			    ###     #        ###        #      ###
			   ###     ###      #####      ###      ###
			  ##########################################
			 ####     ##  ##  ######    ###    ###    ###
			#####  #####  ##  #####  #  ##  ##  ##  ######
			#####  #####      ####  ##  ##  ##  ###   ####
			#####  #####  ##  ###       ##  ##  ####  ####
			 ####     ##  ##  ##  ####  ###    ###    ####
			  ###########################################
			   ###     ###      #####      ###      ###
			    ###     #        ###        #      ###
			     ###              #               ###

import Bladex
import EnemyTypes
import Damage
import math
import Sounds
import Reference
import Select
import Change
import Actions
import AuxFuncs
import OnInitTake
import GameText
import Scorer
import Sparks
import EnemyTypes
import Interpolator
import ConcenEf
import darfuncs
import Actions
import PhantonFX
import AbreCam





#######################
#     Preparacion     #
#######################


chaosk1=Bladex.CreateEntity("ChaosK1", "ChaosKnight", 325973.1,  -1291.66181046, 83.29,"Person")
chaosk1.Angle=0
chaosk1.Level=19
EnemyTypes.EnemyDefaultFuncs(chaosk1)

chaosk1.Data.DamageFactorNone=0.15
chaosk1.Data.DamageFactorLight=0.35
chaosk1.Data.DamageFactorHeavy=0.35
chaosk1.Data.PrepareWeapons("Espadon", "Escudon")
#chaosk1.Data.PrepareDisappearance()
darfuncs.HideBadGuy(chaosk1.Name)

##################
#     Muerte     #
##################

TOTAL_TIME=8.0
TOTAL_STEPS=TOTAL_TIME*60.0
ANGLE_VARIATION=2.0*3.14159/TOTAL_STEPS


chaosk1.ImDeadFunc=AbreteSesamus



##############################################################
##########   GRAN MUERTE DEL CABALLERO DEL CAOS !!  ##########
##############################################################

Bladex.ReadBitMap("../../Data/SmokePrtl3.bmp","SmokePart3")

Bladex.AddParticleGType("DeathCloud","SmokePart3",B_PARTICLE_GTYPE_MUL,64)


for i in range(64):
	aux=(64.0-i)/64
	r=255
	g=255
	b=255
	a=0
	if aux < 0.5:
		size = aux*512
	else:
		size = (1-aux)*512
	Bladex.SetParticleGVal("DeathCloud",i,r,g,b,a,size)

PartesRayuela = ("L_Hand","R_Hand","L_Foot","R_Foot","Head")

"""
elevador.o_med_vel=-30000
elevador.c_med_vel= 30000

# char.Position = (528120.232632, 90673.1254913, 56116.8250833)
# char.SetActiveEnemy("")

"""