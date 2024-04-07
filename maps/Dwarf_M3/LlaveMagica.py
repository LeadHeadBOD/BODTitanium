##///
##||| Desert_M13/LLAVEMAGICA.PY TITANIUM
##||| Change list:
##||| * Removed "LlaveTimer". No need for it.
##||| * 
##||| * 
##||| * 
##\\\ 

import OnInitTake
import Actions
import darfuncs
import whrandom
import Doors

generator = whrandom.whrandom()

#
# Particulas de estrella
#----------------------------

Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")
Bladex.AddParticleGType("Estrellitas","Estrellita",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	r=240.0
	g=170.0
	b=20.0
	a   = (i*255)/64
	size= (64-i)*2
	Bladex.SetParticleGVal("Estrellitas",i,r,g,b,a,size)


# Bladex.CreateTimer("LlaveTimer",1.0/20.0)     # Unused now, just uses regular Timer60 now -LeadHead

###############################
###---PUERTA DE LA LLAVE---####
###############################
#-PUERTA-LLAVEa


maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")


puertalA1=Doors.CreateDoor("PuertalA1", (-23000,13000,32250), (-1,0,0), 0, 2750, Doors.CLOSED)
puertalA2=Doors.CreateDoor("PuertalA2", (-26000,13000,32250), (1,0,0), 0, 2750, Doors.CLOSED)

#
puertalA1.opentype=Doors.UNIF
puertalA1.o_med_vel=-500
puertalA1.o_med_displ=2750

#puertalA1.closetype=Doors.AC
#puertalA1.c_init_displ=2750
#puertalA1.c_med_vel=8000
#
puertalA2.opentype=Doors.UNIF
puertalA2.o_med_vel=-500
puertalA2.o_med_displ=2750

#puertalA2.closetype=Doors.AC
#puertalA2.c_init_displ=2750
#puertalA2.c_med_vel=8000


puertalA1.SetWhileOpenSound(maderadesliz)
puertalA1.SetEndOpenSound(maderagolpe)

puertalA1.SetWhileCloseSound(maderadesliz)
puertalA1.SetEndCloseSound(maderagolpe)




o=Bladex.CreateEntity("BEETLE","LlaveAmarilla",-24595.105589,16968.456436,34935.464395)
o.Static=0
o.Scale=1.000000
o.Orientation=0.026277,-0.998672,0.044304,-0.000412

darfuncs.SetHint(o,"Amber Key")


#-------------------------LUZ DE-LA-LLAVE----------------------------------

luz2=Bladex.CreateEntity("LuzBEETLE","Entity Spot",-24595.105589,16968.456436,34935.464395)
luz2.Color=240,170,20
luz2.Intensity=10
luz2.Precission=0.1
luz2.CastShadows=0
luz2.Visible=1
luz2.Flick=0
luz2.SizeFactor = 2
luz2.AngVel=0.1
luz2.GlowTexture="SunFlare"
o.Link(luz2)


Contador = 0






OnInitTake.AddOnInitTakeEvent("BEETLE", PickUpLaLlave)
