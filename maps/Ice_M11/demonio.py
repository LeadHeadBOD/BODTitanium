##///
##||| Ice_M11/demonio.PY TITANIUM
##||| Change list:
##||| * LlaveTimer made 60 ticks per second
##||| * 
##||| * 
##\\\ 


import whrandom
import PhantonFX
import OnInitTake
import Actions
import darfuncs
import AuxFuncs
import Scorer
import EnemyTypes
import AniSound
import LevelFuncs

# Set these values to the expected player's level (0-19) at the beginning of the map
expected_player_lvl_min= 12
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

#char.Position = 17286.3976448, -8964.80000236, -26884.1208017


_SndRugidoFuerte=Bladex.CreateSound("../../Sounds/M-rugido-demon.wav","RugiDon")
_SndRugidoFuerte.MinDistance =  200000
_SndRugidoFuerte.MaxDistance = 1000000

_SndRugidoSuave=Bladex.CreateSound("../../Sounds/rugido2.WAV","RugiDin")
_SndRugidoSuave.MinDistance =  200000
_SndRugidoSuave.MaxDistance = 1000000

_SndGolPolvo=Bladex.CreateSound("../../Sounds/golpe-madera-pesada.wav","GolPolvo")
_SndGolPolvo.MinDistance =  200000
_SndGolPolvo.MaxDistance = 1000000

_SndCristalonazo=Bladex.CreateSound("../../Sounds/Rotura-varia-cristal.wav","GolCristal")
_SndCristalonazo.MinDistance =  200000
_SndCristalonazo.MaxDistance = 1000000

_SndCristalero=Bladex.CreateSound("../../Sounds/M-cristales-caida.wav","LluCristal")
_SndCristalero.MinDistance =  200000
_SndCristalero.MaxDistance = 1000000


Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")

generator = whrandom.whrandom()

#
# Polvo de tierra
#----------------------------

Bladex.AddParticleGType("Tierrax","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=100
	g=100
	b=100
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierrax",i,r,g,b,a,size)


#
# Particulas de vidrio
#----------------------------

Bladex.AddParticleGType("Brillitos","Estrellita",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	r=255.0
	g=255.0
	b=255.0
	a   = generator.randint(0,255)
	size= generator.randint(0,100)

	Bladex.SetParticleGVal("Brillitos",i,r,g,b,a,size)

#
# Alo Magico de la muerte
#----------------------------

Bladex.AddParticleGType("Energia3","GenericParticle",B_PARTICLE_GTYPE_ADD,80)

for i in range(80):
	if i>60:
		traux=1-((i-60.0)/20.0) #va de 0 a 1
	elif i<20:
		traux=i/20.0 #va de 1 a 0
	else:
		traux=1.0
	r=255
	g=80
	b=100
	a=255.0*traux
	size=(80-i)*2.5
	Bladex.SetParticleGVal("Energia3",i,r,g,b,a,size)


se1=Bladex.GetSector(17680, -19000, -19480)
se2=Bladex.GetSector(19545,-19000,-19480)

se1.InitBreak((0,0,70),(0,1000,0),(700, 200,0),'GolpeCristal')
se2.InitBreak((0,0,70),(0, 900,0),(800,-300,0),'GolpeCristal')

# Bladex.CreateTimer("LlaveTimer",1.0/20.0)		# 60 fps for key anim
Bladex.CreateTimer("LlaveTimer",1.0/60.0)		#		-LeadHead

Contador = 0





lemntira=Bladex.CreateEntity("LlaveMentira","LlaveBlanca",0,0,0)
lemntira.Alpha = 0

demonio=Bladex.CreateEntity("Demonio de Ventana", "Little_Demon", 18712,-18252,-17020)
demonio.Person=1
demonio.Level=lvl_control.GiveLevel(14,16)
EnemyTypes.EnemyDefaultFuncs(demonio)
# AniSound.AsignarSonidosLittleDemon(demonio.Name)	# Not needed, commented out
demonio.Freeze()
demonio.RemoveFromWorld()
Actions.TakeObject(demonio.Name,"LlaveMentira")





DemonioSector = Bladex.GetSector(17286.3976448, -8964.80000236, -26884.1208017)
DemonioSector.OnEnter = CaminaHastaInicioD