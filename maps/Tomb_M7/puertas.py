##///
##||| TOMB_M7/PUERTAS.PY TITANIUM
##||| Change list:
##||| * Doors leading to tomb beneath temple now both make opening sound.
##||| * Restored unused gates (visual only, functionality not re-added to retain final gameplay)
##|||   
##\\\ 


import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import ReadGSFile
import Button
import Bladex
import AuxFuncs
import darfuncs
import Stars


############################################################
#####--RASTRILLO---CEMENTERIO--SALIDA---------##############
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

reja1=Bladex.CreateEntity("Reja1","Rastrillo",47092.596500,-2339.457184,8579.180533)
reja1.Scale=1.232392
reja1.Orientation=0.707107,0.707107,0.000000,0.000000
Sparks.SetSparkling("Reja1")

reja1din=Objects.CreateDinamicObject("Reja1")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar una palanca

palance1=Levers.PlaceLever("Palance1",Levers.LeverType3,(44246.871592,-268.947068,6970.200829),(0.707107,0.707107,0.000000,0.000000),1.0)

palance1.mode=3


palance1.OnTurnOnFunc=Abrereja1
palance1.OnTurnOnArgs=()

palance1.OnTurnOffFunc=Cierrareja1
palance1.OnTurnOffArgs=()

############################################################
#####------------------ANTES-RASTRILLO---TORRE-----AHORA-PUERTA-BRONCE-------------########
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0

maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0



ptatorre1=Doors.CreateDoor("ptatorre1", (71000,-4000,-28000), (-1,0,0), 250, 2750, Doors.CLOSED)


ptatorre1.opentype=Doors.UNIF
ptatorre1.o_med_vel=-700
ptatorre1.o_med_displ=2500


ptatorre1.closetype=Doors.AC
ptatorre1.c_init_displ=2500
ptatorre1.c_med_vel=8000


ptatorre1.SetWhileOpenSound(maderadesliz)
ptatorre1.SetEndOpenSound(maderagolpe)

ptatorre1.SetWhileCloseSound(maderadesliz)
ptatorre1.SetEndCloseSound(maderagolpe)

##### Abrir la puerta al accionar una palanca


palanptatorre1=Levers.PlaceLever("Palanptatorre1",Levers.LeverType1,(73965.741760,-3158.834923,-27213.188812),(0.0,0.0,-0.707080,0.707080),1.0)

palanptatorre1.mode=3


palanptatorre1.OnTurnOnFunc=Abreptatorre1
palanptatorre1.OnTurnOnArgs=()

palanptatorre1.OnTurnOffFunc=Cierraptatorre1
palanptatorre1.OnTurnOffArgs=()


###########################################
###-------------llave-segundo--recinto--abre--puerta1--------------------###
###########################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0

maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
maderadesliz.MaxDistance=20000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0



Lorenzo1=Doors.CreateDoor("Lorenzo", (2687,-1500,30000), (0,1,0), 1000, 5000, Doors.CLOSED)


Lorenzo1.opentype=Doors.UNIF
Lorenzo1.o_med_vel=-700
Lorenzo1.o_med_displ=4000


Lorenzo1.closetype=Doors.AC
Lorenzo1.c_init_displ=4000
Lorenzo1.c_med_vel=8000


Lorenzo1.SetWhileOpenSound(maderadesliz)
Lorenzo1.SetEndOpenSound(maderagolpe)

Lorenzo1.SetWhileCloseSound(maderadesliz)
Lorenzo1.SetEndCloseSound(maderagolpe)


###########################################


cerradurp1=Locks.PlaceLock("cerradurp1","Cerraduracutre",(1528.580957,-179.875893,34186.648470),(0.000000,0.000000,0.707107,-0.707107),2.5)
cerradurp1.key="llave1"

cerradurp1.OnUnLockFunc=AbrePuertaLlave1
cerradurp1.OnUnLockArgs=()

cerradurp1.OnLockFunc=CierraPuertaLlave1
cerradurp1.OnLockArgs=()

darfuncs.SetHint(cerradurp1.obj,"Iron Lock")

#en la puerta
#o=Bladex.CreateEntity("llave1","Llavecutre",-155.479212,978.895795,27418.445363)
#o.Static=0
#o.Scale=1.0
#o.Orientation=0.003416,0.981379,0.002321,0.192038

#en la torre
#o=Bladex.CreateEntity("llave1","Llavecutre",68681.759000,-3067.986000,-13844.493000)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.998924,0.016785,-0.043168,-0.002390
#Stars.Twinkle("llave1")

######################################################
###-------------PUERTA DEL TEMPLO---se cierra al entrar con el fetiche--------------------###
######################################################


maderadeslizT=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpeT=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertatemplo=Doors.CreateDoor("puertatemplo", (6000,-3500,15500), (0,1,0), 500, 3700, Doors.OPENED)


puertatemplo.opentype=Doors.UNIF
puertatemplo.o_med_vel=-700
puertatemplo.o_med_displ=3200
#LineaPolvoSuelo("PolvoSuelo",(-66750,-8300,-80000),(0,0,-8500),1000)

puertatemplo.closetype=Doors.AC
puertatemplo.c_init_displ=3200
puertatemplo.c_med_vel=8000


puertatemplo.SetWhileOpenSound(maderadeslizT)      # Was commented out
puertatemplo.SetEndOpenSound(maderagolpeT)         # Barely audible, but it's a nice touch if you turn around.
                                                   #
puertatemplo.SetWhileCloseSound(maderadeslizT)     #
puertatemplo.SetEndCloseSound(maderagolpeT)        #            -LeadHead

###########################################
###----------------------------llave-cementerio--------------------------------###
###########################################


maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertaZ2=Doors.CreateDoor("PuertaZ2", (61000,3000,14875), (-1,0,0), 2000, 8000, Doors.CLOSED)


puertaZ2.opentype=Doors.UNIF
puertaZ2.o_med_vel=-2000
puertaZ2.o_med_displ=6000
puertaZ2.Squezze = 1


puertaZ2.closetype=Doors.UNIF
puertaZ2.c_med_displ=6000
puertaZ2.c_med_vel=2200


puertaZ2.SetWhileOpenSound(maderadesliz)
puertaZ2.SetEndOpenSound(maderagolpe)

puertaZ2.SetWhileCloseSound(maderadesliz)
puertaZ2.SetEndCloseSound(maderagolpe)


###########################################


cerradurp2=Locks.PlaceLock("cerradurp2","Cerraduracutre",(64597.682604,4854.976510,16147.181337),(0.50,0.50,-0.5,0.5),2.5)
cerradurp2.key="llave2"


cerradurp2.OnUnLockFunc=AbrePuertaLlave2
cerradurp2.OnUnLockArgs=()

cerradurp2.OnLockFunc=CierraPuertaLlave2
cerradurp2.OnLockArgs=()

darfuncs.SetHint(cerradurp2.obj,"Graveyard Lock")

#o=Bladex.CreateEntity("llave2","Llavecutre",62559.253198,5971.211078,15938.285220)
#o.Static=0
#o.Scale=1.0
#o.Orientation=0.015024,-0.982610,-0.014468,-0.184509

o=Bladex.CreateEntity("llave2","Llavecutre",125262.313000,-3021.260000,29077.211000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.998810,0.003867,-0.048612,-0.000139
darfuncs.SetHint(o,"Graveyard Key")
Stars.Twinkle("llave2")

############################################################
############################################################
####----------------.......................,,,,,,,,,,,--#####
####----PUERTA-ACCESO AL PISO SUPERIOR DEL TEMPLO-------#####
############################################################
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertaZ3=Doors.CreateDoor("PuertaZ3", (2750,-3000,15500), (0,1,0), 0, 3700, Doors.CLOSED)


puertaZ3.opentype=Doors.UNIF
puertaZ3.o_med_vel=-800
puertaZ3.o_med_displ=3700


puertaZ3.closetype=Doors.AC
puertaZ3.c_init_displ=3700
puertaZ3.c_med_vel=8000


puertaZ3.SetWhileOpenSound(maderadesliz)      # Was commented out
puertaZ3.SetEndOpenSound(maderagolpe)         #
                                              #
puertaZ3.SetWhileCloseSound(maderadesliz)     #
puertaZ3.SetEndCloseSound(maderagolpe)        #     -LeadHead
                                              #








############################################################
############################################################
####----------------------------------------------------------------------------------------------------------------#####
####---------------------------PUERTA--SALA--TABLILLA---------------------------------------#####
############################################################
############################################################

maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


puertaz4=Doors.CreateDoor("Puertaz4", (154875,2000,625), (0,1,0), 1000, 7000, Doors.CLOSED)


puertaz4.opentype=Doors.UNIF
puertaz4.o_med_vel=-800
puertaz4.o_med_displ=6000


puertaz4.closetype=Doors.AC
puertaz4.c_init_displ=6000
puertaz4.c_med_vel=8000


puertaz4.SetWhileOpenSound(maderadesliz)
puertaz4.SetEndOpenSound(maderagolpe)

puertaz4.SetWhileCloseSound(maderadesliz)
puertaz4.SetEndCloseSound(maderagolpe)

##### Accionar puerta al pasar por un sector


serT=Bladex.GetSector(151000,0,1000)

serT.OnEnter=AbrePuertaz4

############################################################
#####------------------------------RASTRILLO---ENTRADA-AL RECINTO----------------------#########
############################################################

"""
res=ReadGSFile.ReadGhostSectorFile("inicio.sf")
for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1
esp=Bladex.GetEntity("WeaponInvPrb1")
esp.SendTriggerSectorMsgs=1


sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")
"""
### Unused gates at the start.
### It seems like they were supposed to close as you approach
### forcing you to climb in the "secret" tower above and open the gate
### It adds some nice visual flair though, so re-added them, albeit without any functionality
###         -LeadHead


rejasi=Bladex.CreateEntity("Rejasi1","Rastrillo",-32537.545000,316.166000,-19216.433000)
rejasi.Static=1
rejasi.Scale=0.923483
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000


rejasi=Bladex.CreateEntity("Rejasi2","Rastrillo",-36153.913000,316.166,-19216.4)
rejasi.Static=1
rejasi.Scale=0.923483
rejasi.Orientation=0.707107,0.707107,0.000000,0.000000

"""
Sparks.SetSparkling("Rejasi1")

rejasi1din=Objects.CreateDinamicObject("Rejasi1")

Sparks.SetSparkling("Rejasi2")

rejasi2din=Objects.CreateDinamicObject("Rejasi2")

##funciones abrir-cerrar##



ladosCerrados=0

##### Abrir el rastrillo al accionar una palanca


#palanrsi1=Levers.PlaceLever("PalanRsi1",Levers.LeverType2,(-33953.785783,-5421.522946,-17232.384152),(0.50,0.50,-0.50,0.50),1.0)
palanrsi1=Levers.PlaceLever("PalanRsi1",Levers.LeverType2,(-33953.785783,-5421.522946,-17232.384152),(0.707187,0.005838,-0.706972,0.006484),1.0)
palanrsi1.mode=3


palanrsi1.OnTurnOnFunc=Abrerejas
palanrsi1.OnTurnOnArgs=()



palanr1.OnTurnOffFunc=Cierrarejas
palanr1.OnTurnOffArgs=()


#print("poniendo el trigger sector")
Bladex.SetTriggerSectorFunc("inicio", "OnEnter", EntroEnTriggerSector)

"""
###########################################
###      puerta sala tablillas          ###
###########################################


sptaDesliz1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "sptaDesliz1")
sptaDesliz1.MaxDistance=20000
sptaDesliz1.MinDistance=2000
sptaDesliz1.Volume=1.0

sptaGolpe1=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "sptaGolpe1")
sptaGolpe1.MaxDistance=20000
sptaGolpe1.MinDistance=2000
sptaGolpe1.Volume=1.0

sptaDesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-deslizando-2.wav", "sptaDesliz2")
sptaDesliz2.MaxDistance=20000
sptaDesliz2.MinDistance=2000
sptaDesliz2.Volume=1.0

sptaGolpe2=Sounds.CreateEntitySound("../../Sounds/M-CIERRE-GATE.wav", "sptaGolpe2")
sptaGolpe2.MaxDistance=20000
sptaGolpe2.MinDistance=2000
sptaGolpe2.Volume=1.0

#1
puertata1=Doors.CreateDoor("puertata1", (114600,-1500,625), (-1,0,0), 0, 600, Doors.CLOSED)

puertata1.opentype=Doors.UNIF
puertata1.o_med_vel=-800
puertata1.o_med_displ=600

puertata1.closetype=Doors.AC
puertata1.c_init_displ=600
puertata1.c_med_vel=800

#2
puertata2=Doors.CreateDoor("puertata2", (115200,0,625), (0,-1,0), 0, 3800, Doors.CLOSED)

puertata2.opentype=Doors.UNIF
puertata2.o_med_vel=-800
puertata2.o_med_displ=3800

puertata2.closetype=Doors.AC
puertata2.c_init_displ=3800
puertata2.c_med_vel=800


puertata1.SetWhileOpenSound(sptaDesliz1)
puertata1.SetEndOpenSound(sptaGolpe1)

puertata1.SetWhileCloseSound(sptaDesliz1)
puertata1.SetEndCloseSound(sptaGolpe1)

puertata2.SetWhileOpenSound(sptaDesliz2)
puertata2.SetEndOpenSound(sptaGolpe1)

puertata2.SetWhileCloseSound(sptaDesliz2)
puertata2.SetEndCloseSound(sptaGolpe2)


o=Bladex.CreateEntity("bloqueta","AdoquinRuna",114850.331751,-2147.724669,569.486034)
o.Static=0
o.Scale=1.661078
o.Orientation=0.000000,0.000000,0.707107,-0.707107


###de adorno
o=Bladex.CreateEntity("sss","AdoquinRuna",173458.487969,6241.802718,554.232000)
o.Static=0
o.Scale=1.853212
o.Orientation=0.006171,0.006171,-0.707080,0.707080



buttonta=Button.CreateButtonCombination(0,AbrePuertata,"")
xx = buttonta.AddButton("bloqueta",3,(1,0,0),20,0,0,1)
xx.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound pta')
xx.sound.Volume=0.4
xx.sound.MinDistance=1000
xx.sound.MaxDistance=10000

############################################################
#####--RASTRILLO---CRIPTA---FINAL-------------##############
############################################################

sonidorastrillo=Sounds.CreateEntitySound("../../Sounds/rastrillo.wav", "SonidoRastrillo")
golpemetalmediano=Sounds.CreateEntitySound("../../Sounds/golpe-metal-mediano.wav", "GolpeMetalMediano")

rejaF1=Bladex.CreateEntity("RejaF1","Rastrillo",8752.431535,4332.692667,-17606.712653)
rejaF1.Static=1
rejaF1.Scale=0.905
rejaF1.Orientation=0.5,0.5,-0.500000,0.500000
Sparks.SetSparkling("RejaF1")

rejaF1din=Objects.CreateDinamicObject("RejaF1")

##funciones abrir-cerrar##


##### Abrir el rastrillo al accionar un pulsador


o=Bladex.CreateEntity("bloquetF","Bloque",18439.167784,5281.848464,-19239.511874)
o.Static=0
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
darfuncs.SetHint(o,"Trigger")


buttonta=Button.CreateButtonCombination(0,AbrerejaF1,"")
ortiba=buttonta.AddButton("bloquetF",3,(1,0,0),300,0,0,1)
ortiba.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound libro')
ortiba.sound.Volume=0.5
ortiba.sound.MinDistance=1000
ortiba.sound.MaxDistance=10000

###################################
#####-------PUERTA DOBLE-DEL TEMPLO----#######
###################################



Bladex.AddParticleGType("DustDoor","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)

for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(64.0-i)/64.0
	r=90
	g=70
	b=75
	a=255.0*(1.0-traux)**0.5
	size=10.0+aux*1700.0
	Bladex.SetParticleGVal("DustDoor",i,r,g,b,a,size)



maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderadesliz.MaxDistance=25000
maderadesliz.MinDistance=2000
maderadesliz.Volume=1.0
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")
maderagolpe.MaxDistance=25000
maderagolpe.MinDistance=2000
maderagolpe.Volume=1.0


puertadobleT1=Doors.CreateDoor("PuertaDobleT1", (28312,-4000,-1250), (0,0,-1), 0, 1500, Doors.OPENED)


puertadobleT1.opentype=Doors.UNIF
puertadobleT1.o_med_vel=-400
puertadobleT1.o_med_displ=1500

puertadobleT1.closetype=Doors.UNIF
puertadobleT1.c_med_displ=1500
puertadobleT1.c_med_vel=800


puertadobleT1.SetWhileOpenSound(maderadesliz)
puertadobleT1.SetEndOpenSound(maderagolpe)

puertadobleT1.SetWhileCloseSound(maderadesliz)
puertadobleT1.SetEndCloseSound(maderagolpe)

#####
puertadobleT2=Doors.CreateDoor("PuertaDobleT2", (28312,-4000,-2000), (0,0,1), 0, 1500, Doors.OPENED)

puertadobleT2.opentype=Doors.UNIF
puertadobleT2.o_med_vel=-400
puertadobleT2.o_med_displ=1500

puertadobleT2.closetype=Doors.UNIF
puertadobleT2.c_med_displ=1500
puertadobleT2.c_med_vel=800
puertadobleT2.OnEndCloseFunc=LineaPolvo


#puertadoble2.SetWhileOpenSound(maderadesliz)
#puertadoble2.SetEndOpenSound(maderagolpe)

#puertadoble2.SetWhileCloseSound(maderadesliz)
#puertadoble2.SetEndCloseSound(maderagolpe)


########################################################################3
####	puerta de LAS COSITAS


spuertac1d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuertac1d.MaxDistance=20000
spuertac1d.MinDistance=1000
spuertac1d.Volume=1.0


spuertac1g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuertac1g.MaxDistance=20000
spuertac1g.MinDistance=2000
spuertac1g.Volume=1.0

puertac1=Doors.CreateDoor("Puertac1", (-12800,3000,-33800), (0,0,-1), 500, 3500, Doors.CLOSED)


puertac1.opentype=Doors.UNIF
puertac1.o_med_vel=-800
puertac1.o_med_displ=3000


puertac1.closetype=Doors.AC
puertac1.c_init_displ=3000
puertac1.c_med_vel=8000


puertac1.SetWhileOpenSound(spuertac1d)
puertac1.SetEndOpenSound(spuertac1g)

puertac1.SetWhileCloseSound(spuertac1d)
puertac1.SetEndCloseSound(spuertac1g)

##### Accionar puertas al accionar una palanca


palanc1=Levers.PlaceLever("PALAPc1",Levers.LeverType3,(-11791.546333,4539.973544,-31062.855792),(0.500000,0.500000,-0.500000,0.500000),1.0)

palanc1.mode=1


#def AbrePuertac1():
#	puertac1.OpenDoor()

#def CierraPuertarc():
#	puertac1.CloseDoor()




palanc1.OnTurnOnFunc=AbrePuertac1
palanc1.OnTurnOnArgs=()

palanc1.OnTurnOffFunc=CierraPuertac1
palanc1.OnTurnOffArgs=()


########################################################################3
####	puerta DEL CUERPO DE GUARDIA


spuertag2d=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
spuertag2d.MaxDistance=20000
spuertag2d.MinDistance=1000
spuertag2d.Volume=1.0


spuertag2g=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")
spuertag2g.MaxDistance=20000
spuertag2g.MinDistance=2000
spuertag2g.Volume=1.0

puertag2=Doors.CreateDoor("Puertag2", (-27500,-7000,-2375), (1,0,0), 0, 2000, Doors.CLOSED)


puertag2.opentype=Doors.UNIF
puertag2.o_med_vel=-800
puertag2.o_med_displ=2000


puertag2.closetype=Doors.AC
puertag2.c_init_displ=2000
puertag2.c_med_vel=8000


puertag2.SetWhileOpenSound(spuertag2d)
puertag2.SetEndOpenSound(spuertag2g)

puertag2.SetWhileCloseSound(spuertag2d)
puertag2.SetEndCloseSound(spuertag2g)

##### Accionar puertas al accionar una palanca


palang2=Levers.PlaceLever("PALAPg2",Levers.LeverType3,(-29504.066889,-5593.354723,-3388.334217),(0.707107,0.707107,0.000000,0.000000),1.0)

palang2.mode=1


#def AbrePuertag2():
#	puertag2.OpenDoor()

#def CierraPuertag2():
#	puertag2.CloseDoor()




palang2.OnTurnOnFunc=AbrePuertag2
palang2.OnTurnOnArgs=()

palang2.OnTurnOffFunc=CierraPuertag2
palang2.OnTurnOffArgs=()


#####################	SARCOFAGO


sarcofago1=Doors.CreateDoor("sarcofago1", (19000,2000,-250), (0,-1,0), 0, 4000, Doors.CLOSED)

sarcofago1.opentype=Doors.UNIF
sarcofago1.o_med_vel=-800
sarcofago1.o_med_displ=4000

sarcofago1.closetype=Doors.AC
sarcofago1.c_init_displ=4000
sarcofago1.c_med_vel=8000

sarcofago1.SetWhileOpenSound(spuertag2d)
sarcofago1.SetEndOpenSound(spuertag2g)

sarcofago1.SetWhileCloseSound(spuertag2d)
sarcofago1.SetEndCloseSound(spuertag2g)

#2
sarcofago2=Doors.CreateDoor("sarcofago2", (21250,2000,-1500), (0,-1,0), 0, 4000, Doors.CLOSED)

sarcofago2.opentype=Doors.UNIF
sarcofago2.o_med_vel=-800
sarcofago2.o_med_displ=4000

sarcofago2.closetype=Doors.AC
sarcofago2.c_init_displ=4000
sarcofago2.c_med_vel=8000

#3
sarcofago3=Doors.CreateDoor("sarcofago3", (16750,2000,-1500), (0,-1,0), 0, 4000, Doors.CLOSED)

sarcofago3.opentype=Doors.UNIF
sarcofago3.o_med_vel=-800
sarcofago3.o_med_displ=4000

sarcofago3.closetype=Doors.AC
sarcofago3.c_init_displ=4000
sarcofago3.c_med_vel=8000

#4
sarcofago4=Doors.CreateDoor("sarcofago4", (19000,2000,-2750), (0,-1,0), 0, 4000, Doors.CLOSED)

sarcofago4.opentype=Doors.UNIF
sarcofago4.o_med_vel=-800
sarcofago4.o_med_displ=4000

sarcofago4.closetype=Doors.AC
sarcofago4.c_init_displ=4000
sarcofago4.c_med_vel=8000

ChapuzaFunctionFlag = 1


##################################################################################
#####	PUERTA QUE SE ABRE DE SALIDA DEL CEMENTERIO


#1
puertaCE1=Doors.CreateDoor("puertaCE1", (50250,4000,-7000), (0,1,0), 0, 3750, Doors.CLOSED)

puertaCE1.opentype=Doors.UNIF
puertaCE1.o_med_vel=-8000
puertaCE1.o_med_displ=3750

puertaCE1.closetype=Doors.AC
puertaCE1.c_init_displ=3750
puertaCE1.c_med_vel=8000