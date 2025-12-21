##///
##||| Mine_M5/gemas.PY TITANIUM
##||| Change list:
##||| * Restored missing sound on inserting gem into socket?
##\\\ 

##################################################

# Poner las 5 gemas en su sitio (2 colocadas)
#
# (Yuio)
# Bugs corregidos por Dario.
# Me cago en Yuio y la madre que lo pario
##################################################


##       _||_
##       -||-
##    ____________
##   /            \
##  |  Aqui yace   |
##  | Yuio Capuio  |
##  |   El mejor   |
##  | Escritor de  |
##  |     Bugs     |
##  |Rest In Pieces|
##  |______________|
##  \***************\
##    \***************\
##      \***************\
##        \***************\



import Reference
import Select
import Doors
import Actions
import Change
import Ontake
import darfuncs
import Levers
import Scorer
import dust

# gemaazulson=Bladex.CreateSound("../../Sounds/burning-knight.wav", "GemaAzulSon")	### PLAGUE: Sound does not exist! And seriously, what is this file even
gemaazulson=Bladex.CreateSound("../../Sounds/coger-jarra.wav", "GemaAzulSon")
gemaazulson.Volume=1
gemaazulson.MinDistance=5000
gemaazulson.MaxDistance=40000

############# HORNACINAS #################

o=Bladex.CreateEntity("NoName4","Hornacina",24315.584000,-24824.778000,-40398.878000)
o.Static=1
o.Scale=0.887449
o.Orientation=0.116706,0.116706,0.697409,-0.697409
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n

o=Bladex.CreateEntity("NoName1","Hornacina",24266.626020,-24836.171670,-13608.260088)
o.Static=1
o.Scale=0.844377
o.Orientation=0.703233,0.703233,0.073913,-0.073913
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n


o=Bladex.CreateEntity("NoName2","Hornacina",33981.885614,-24879.802597,-27025.000482)
o.Static=1
o.Scale=1.000000
o.Orientation=0.500000,0.500000,0.500000,-0.500000
#o.NodesOrientation=?  En la siguiente versi�n
#o.Scripts=?  En la siguiente versi�n

##########################################

maderadesliz1=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz1")
maderagolpe1=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe1")

maderadesliz2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz2")
maderagolpe2=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe2")


######## particulas de polvo ocre
Bladex.AddParticleGType("DesertDust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(64):
	if i>32:
		traux=0.0
	else:
		traux=(32.0-i)/32.0
	aux=(64.0-i)/64.0
	r=90
	g=85
	b=80
	a=100.0*(1.0-traux)**0.5
	size=(1.0+aux*350.0)*2.0
	Bladex.SetParticleGVal("DesertDust",i,r,g,b,a,size)

######## puertas
gemRoomPlatform=Doors.CreateDoor("gRoomPlatform", (17250,-13700,-27000), (0,-1,0), 0, 10000, Doors.CLOSED)
gemRoomDoor=Doors.CreateDoor("gRoomDoor", (-7160,-14000,-27070), (0,1,0), 0, 4000, Doors.CLOSED)

######### numero de gemas bien colocadas
RGemOk=0
GGemOk=0
BGemOk=0

################## gema 3 verde ( Por colocar )
o=Bladex.CreateEntity("GemaG", "Gema",21124.831012,9972.935700,-208231.629233)
o.SelfIlum= -1
o.Static=0
o.Scale=1.115668
o.Orientation=0.011700,0.999333,-0.000007,-0.034591
o.Solid=0

luz = Bladex.CreateEntity("GemaGLight","Entity Spot",21124.831012,9972.935700-100,-208231.629233)
luz.Color = 34,84,44
luz.Intensity = 2
luz.CastShadows = 0
luz.Precission = 0.06
luz.Visible = 0
luz.Flick = 0

################## gema 5 roja ( Por colocar )
o=Bladex.CreateEntity("GemaR","Gemaroja",-122215.932547,-10553.301563,63282.984978)
o.Static=0
o.Scale=1.061520
o.Orientation=0.999366,0.013970,0.018620,0.026930
o.SelfIlum= -1
o.Solid=0
luz = Bladex.CreateEntity("GemaRLight","Entity Spot",-122215.932547,-10553.301563-100,63282.984978)
luz.Color = 120,1,4
luz.Intensity = 2
luz.CastShadows = 0
luz.Precission = 0.06
luz.Visible = 0
luz.Flick = 0
"""
#########gema 1 ( Ya colocada )

o=Bladex.CreateEntity("GemaStatica1","Gema",11760.679825,-24095.671605,-8212.024231)
o.Static=1
o.Scale=1.160969
o.Orientation=0.500000,0.500000,-0.500000,-0.500000
o.Solid=0

luz1=Bladex.CreateEntity("GemaLight1","Entity Spot",11860.679825,-24095.671605,-8612.024231)
luz1.Color=4,20,14
luz1.Intensity=6
luz1.CastShadows=0
luz1.Precission=0.06
luz1.Visible=0
luz1.Flick=0

############gema 2 ( Ya colocada )

o=Bladex.CreateEntity("GemaStatica2","Gemapurpura",25841.979274,-23961.812220,-9108.504916)
o.Static=1
o.Scale=1.388690
o.Orientation=0.521791,0.495161,-0.478171,-0.503887
o.Solid=0

luz2=Bladex.CreateEntity("GemaLight2","Entity Spot",25441.979274,-23961.812220,-9408.504916)
luz2.Color=9,4,16
luz2.Intensity=16
luz2.CastShadows=0
luz2.Precission=0.06
luz2.Visible=0
luz2.Flick=0
"""

############################ Timers de luces

lightTimerStartTime=0.0



##################gema azul ghostpointer
p=Bladex.CreateEntity("GemBGPointer","GhostPointer",24267.933167,-24811.917853,-13673.558495)
p.Static=0
p.Scale=0.100000
p.Orientation=0.553388,0.440184,-0.440184,-0.553388
p.UseFunc = useInGemGhostP
darfuncs.SetHint(p,"Blue Gem")
##################gema verde ghostpointer
p=Bladex.CreateEntity("GemGGPointer","GhostPointer",24287.778000,-24835.662000,-40362.065000)
p.Static=0
p.Scale=0.100000
p.Orientation=0.553388,0.440184,-0.440184,-0.553388
p.UseFunc = useInGemGhostP
darfuncs.SetHint(p,"Green Gem")
##################gema roja ghostpointer
p=Bladex.CreateEntity("GemRGPointer","GhostPointer",33929.460208,-24853.672511,-27032.143880)
p.Static=0
p.Scale=0.100000
p.Orientation=0.586218,0.415627,0.395409,0.572061
p.UseFunc = useInGemGhostP
darfuncs.SetHint(p,"Red Gem")

Ontake.AddOnTakeEvent("GemaG",takeGemG)
Ontake.AddOnTakeEvent("GemaR",takeGemR)

# Bladex.GetEntity("GemaR").Position = char.Position
# Bladex.GetEntity("GemaG").Position 0= char.Position
# dust.RemueveTierraGen(16873.044921, -23316.999269, -26828.8794677,2000,1500)