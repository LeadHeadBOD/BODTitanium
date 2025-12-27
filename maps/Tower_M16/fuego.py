##///
##||| Tower_M16/fuego.PY TITANIUM
##||| Change list:
##||| * Brightened some lights to make less awkward pitch black corners
##||| * Skeleton spawner light moved up 1m to make the fire look more natural
##\\\ 


import Bladex
import math

###   EN LA SALA DEL ESQUELETO EN LLAMAS

#1
Lucex=Bladex.CreateEntity("hkgfoweua","Entity Spot",-14000, -36800, 7750)		# moved up 1m
Lucex.Color=255,149,32
Lucex.Intensity=3
Lucex.Precission=0.066
Lucex.CastShadows=1
Lucex.Visible=0
Lucex.Flick=1

towFire=Bladex.CreateEntity("cyioj", "Entity Particle System D1", -14000, -35800, 7750)
towFire.ParticleType="LargeFire"
towFire.YGravity=-2000.0
towFire.Friction=0.12
towFire.PPS=100
towFire.Velocity= 0.0, -500.0, 0.0
towFire.Time2Live=32
towFire.RandomVelocity=40


#2
Lucex2=Bladex.CreateEntity("weua","Entity Spot",-14000, -36800, 4000)			# moved up 1m
Lucex2.Color=255,149,32
Lucex2.Intensity=3
Lucex2.Precission=0.066
Lucex2.CastShadows=0
Lucex2.Visible=1
Lucex2.Flick=1

towFire2=Bladex.CreateEntity("cyioj2", "Entity Particle System D1", -14000, -35800, 4000)
towFire2.ParticleType="LargeFire"
towFire2.YGravity=-4000.0
towFire2.Friction=0.12
towFire2.PPS=100
towFire2.Velocity= 0.0, -500.0, 0.0
towFire2.Time2Live=32
towFire2.RandomVelocity=40


#############################################################################################
###	LUCES CON HUMO ROJO


####	SISTEMA DE PARTICULAS	###############

Bladex.AddParticleGType("HumoRojo","SmokeParticle",B_PARTICLE_GTYPE_BLEND,50)

for i in range(50):
	aux=(50.0-i)/50.0
	r=110
	g=30
	b=15
	a=250
	size=1000.0*math.sqrt(1.0-aux)
	Bladex.SetParticleGVal("HumoRojo",i,r,g,b,a,size)
	
##EN LA LAVA DE LOS SALAMANDERS	



####	EN LOS ESQUELETOS CON HUMO ROJO
#1
towFire3=Bladex.CreateEntity("cyioj3", "Entity Particle System D1", -14809.44,-43813,21000)
towFire3.ParticleType="HumoRojo"
towFire3.YGravity=-3000.0
towFire3.Friction=0.12
towFire3.PPS=25
towFire3.Velocity= 0.0, -100.0, 0.0
towFire3.Time2Live=50
towFire3.RandomVelocity=40
#luz
Lucex3=Bladex.CreateEntity("weua3","Entity Spot",-14809.44,-45000,21500)
Lucex3.Color=251,69,10
Lucex3.Intensity=10			# change from 12
Lucex3.Precission=0.099
Lucex3.CastShadows=1 		# change from 0 
Lucex3.Visible=0
Lucex3.Flick=1

#2	-6634.236000,-33433.124000,20792.343000
towFire3b=Bladex.CreateEntity("cyioj3b", "Entity Particle System D1", -6634,-43813,21000)
towFire3b.ParticleType="HumoRojo"
towFire3b.YGravity=-3000.0
towFire3b.Friction=0.12
towFire3b.PPS=25
towFire3b.Velocity= 0.0, -100.0, 0.0
towFire3b.Time2Live=50
towFire3b.RandomVelocity=40
#luz
Lucex3b=Bladex.CreateEntity("weua3b","Entity Spot",-6634,-45000,21500)
Lucex3b.Color=251,69,10
Lucex3b.Intensity=9			# Change from 4
Lucex3b.Precission=0.35		# from 0.7
Lucex3b.CastShadows=1
Lucex3b.Visible=0
Lucex3b.Flick=1

"""
#en sala lateral atm azul
# PLAGUE: This light is actually pretty cool, but might need some minor adjustments before re-enabling.
towFire4=Bladex.CreateEntity("cyioj3", "Entity Particle System D1", -10916.054000,-56476.882000,-5165.234000)
towFire4.ParticleType="HumoRojo"
towFire4.YGravity=-4000.0
towFire4.Friction=0.12
towFire4.PPS=30
towFire4.Velocity= 0.0, -100.0, 0.0
towFire4.Time2Live=50
towFire4.RandomVelocity=40
#luz
Lucex4=Bladex.CreateEntity("weua4","Entity Spot",-10916.054000,-58676.882000,-7165.234000)
Lucex4.Color=251,45,0
Lucex4.Intensity=7
Lucex4.Precission=0.06
Lucex4.CastShadows=1
Lucex4.Visible=0
Lucex4.Flick=1
"""



import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fuego.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("Fuego1")
darfuncs.FireOnGS("Fuego2")
darfuncs.FireOnGS("Fuego3")
