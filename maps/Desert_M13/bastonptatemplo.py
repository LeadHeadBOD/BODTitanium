##///
##||| Desert_M13/objs.PY TITANIUM
##||| Change list:
##||| * Removed duplicate imports
##||| * Removed duplicate ontake assignment
##||| * Staff now categorized as a weapon, making it actually have a hitbox
##\\\ 

import AuxFuncs
import Sounds
import Doors
import Bladex
import Ontake
##########################################
#####-------PUERTA DOBLE--TEMPLO---#######
##########################################

spuertaTemplo1D=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
spuertaTemplo1D.MaxDistance=20000
spuertaTemplo1D.MinDistance=10000
spuertaTemplo1D.Volume=1.0


spuertaTemplo1G=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
spuertaTemplo1G.MaxDistance=20000
spuertaTemplo1G.MinDistance=10000
spuertaTemplo1G.Volume=1.0


puertadobleTemplo1=Doors.CreateDoor("puertadobleTemplo2", (-24000,-3000,23400), (-1,0,0), 0, 2125, Doors.CLOSED)

puertadobleTemplo1.opentype=Doors.UNIF
puertadobleTemplo1.o_med_vel=-400
puertadobleTemplo1.o_med_displ=2125

puertadobleTemplo1.closetype=Doors.UNIF
puertadobleTemplo1.c_med_displ=2125
puertadobleTemplo1.c_med_vel=400


puertadobleTemplo1.SetWhileOpenSound(spuertaTemplo1D)
puertadobleTemplo1.SetEndOpenSound(spuertaTemplo1G)

puertadobleTemplo1.SetWhileCloseSound(spuertaTemplo1D)
puertadobleTemplo1.SetEndCloseSound(spuertaTemplo1G)

#####

puertadobleTemplo2=Doors.CreateDoor("puertadobleTemplo1", (-24800,-3000,23400), (1,0,0), 0, 2125, Doors.CLOSED)


puertadobleTemplo2.opentype=Doors.UNIF
puertadobleTemplo2.o_med_vel=-400
puertadobleTemplo2.o_med_displ=2125

puertadobleTemplo2.closetype=Doors.UNIF
puertadobleTemplo2.c_med_displ=2125
puertadobleTemplo2.c_med_vel=400

##### Accionar puertas


#############################################################################################################
#############################################################################################################
#############################################################################################################

RayoBaston=Bladex.CreateEntity("Rayo Baston", "Entity ElectricBolt",0,0,0)
RayoBaston.MaxAmplitude    = 20
RayoBaston.MinSectorLength = 1000000
RayoBaston.Active          = 0
RayoBaston.Damage          = 0
RayoBaston.CoreGlowColor   = 255,000,000
RayoBaston.InnerGlowColor  = 128,000,000


Bladex.AddParticleGType("LaserHit","GenericParticle",B_PARTICLE_GTYPE_ADD,16)

for i in range(16):
	r=255.0
	g=127-i*8
	b=0
	size=30
	a = i*16


	Bladex.SetParticleGVal("LaserHit",i,r,g,b,a,size)

Bladex.AddParticleGType("LaserConcentrator","GenericParticle",B_PARTICLE_GTYPE_ADD,32)

for i in range(32):
	r=255.0
	g=127-i*4
	b=0
	size=i*1.5
	a = 255-i*8
	Bladex.SetParticleGVal("LaserConcentrator",i,r,g,b,a,size)


Rayo_Counter = 0


##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

import Reference
import Change



spuerta1D=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta1D.MaxDistance=20000
spuerta1D.MinDistance=10000
spuerta1D.Volume=1.0

spuerta1G=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta1G.MaxDistance=20000
spuerta1G.MinDistance=10000
spuerta1G.Volume=1.0

spuerta3D=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuerta3D.MaxDistance=20000
spuerta3D.MinDistance=10000
spuerta3D.Volume=1.0

spuerta3G=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuerta3G.MaxDistance=20000
spuerta3G.MinDistance=10000
spuerta3G.Volume=1.0


puerta1=Doors.CreateDoor("PuertarAgua", (-8625,-9000,42600), (0,1,0), 0, 7900, Doors.CLOSED)
puerta3=Doors.CreateDoor("PuertarFuego", (-42375,-9000,41600), (0,1,0), 0, 7900, Doors.CLOSED)

puerta1.opentype=Doors.UNIF
puerta1.o_med_vel=-1800
puerta1.o_med_displ=7900
puerta1.closetype=Doors.UNIF
puerta1.c_med_displ=7900
puerta1.c_med_vel=1800

puerta1.SetWhileOpenSound(spuerta1D)
puerta1.SetEndOpenSound(spuerta1G)
puerta1.SetWhileCloseSound(spuerta1D)
puerta1.SetEndCloseSound(spuerta1G)

puerta3.opentype=Doors.UNIF
puerta3.o_med_vel=-1800
puerta3.o_med_displ=7900
puerta3.closetype=Doors.UNIF
puerta3.c_med_displ=7900
puerta3.c_med_vel=1800
puerta3.SetWhileOpenSound(spuerta3D)
puerta3.SetEndOpenSound(spuerta3G)
puerta3.SetWhileCloseSound(spuerta3D)
puerta3.SetEndCloseSound(spuerta3G)





###baston para usar

#en la cripta
BM=Bladex.CreateEntity("BastonMagico","Baston3",-63670.749000,19100.737000,-42132.709000, "Weapon")		# Now weapon -LeadHead
BM.Static=0
BM.Scale=1.000000
BM.Orientation=0.583292,-0.441550,0.276471,-0.623192
BM.FiresIntensity=[ 45 ]
BM.Lights=[ (1.00000,0.050000,(255,69,43)) ]

Ontake.AddOnTakeEvent("BastonMagico", BastonCheck)



""" Commented this one out, since it's a dupe -LeadHead
# Ontake.AddOnTakeEvent("BastonMagico", BastonCheck)	
"""

AuxFuncs.GetSpot(BM).CastShadows = 0


import BladeTi
BladeTi.GiveShadowMask(BM)


o=Bladex.CreateEntity("PBaston","Lanzapivotes",-24457.677211,-751.352680,16489.950091)
o.Static=1
o.Scale=2.704814
o.Orientation=0.999848,-0.017452,0.000000,0.000000