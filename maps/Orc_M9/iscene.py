#########################################################
#														#
# FORTALEZA DE LOS ORCOS								#
#														#
# escena de inicio										#
#														#
# (Yuio)												#
#														#
#########################################################

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText
import Scorer

soundesfuerzo = [0,0,0]
soundrechinar = [0,0]

soundagua=Sounds.CreateEntitySound('../../Sounds/m-movenaguapormuslos1.wav', 'SoundAgua')
soundagua.Volume=1.0
soundagua.MinDistance=10000
soundagua.MaxDistance=20000

soundhit=Sounds.CreateEntitySound('../../Sounds/golpe-madera-pesada.wav', 'SoundHit')
soundhit.Volume=1.0
soundhit.MinDistance=10000
soundhit.MaxDistance=20000

char = Bladex.GetEntity("Player1")

### PLAGUE: to do-  Replace with char specific sounds
if char.Kind[0] == "A":
	soundesfuerzo[0]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-corto-amz.wav', 'zoundEsfuerzo1')
	soundesfuerzo[1]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-mediano-amz.wav', 'zoundEsfuerzo2')
	soundesfuerzo[2]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-largo-amz.wav', 'zoundEsfuerzo3')
else:
	soundesfuerzo[0]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-corto.wav', 'zoundEsfuerzo1')
	soundesfuerzo[1]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-mediano.wav', 'zoundEsfuerzo2')
	soundesfuerzo[2]=Sounds.CreateEntitySound('../../Sounds/esfuerzo-barb-largo.wav', 'zoundEsfuerzo3')



soundesfuerzo[0].Volume=0.75
soundesfuerzo[0].MinDistance=10000
soundesfuerzo[0].MaxDistance=20000

soundesfuerzo[1].Volume=0.75
soundesfuerzo[1].MinDistance=10000
soundesfuerzo[1].MaxDistance=20000

soundesfuerzo[2].Volume=0.75
soundesfuerzo[2].MinDistance=10000
soundesfuerzo[2].MaxDistance=20000

soundrechinar[0]=Sounds.CreateEntitySound('../../Sounds/M-subirmadera.wav', 'SoundCrujido1')
soundrechinar[0].Volume=1
soundrechinar[0].MinDistance=10000
soundrechinar[0].MaxDistance=20000

soundrechinar[1]=Sounds.CreateEntitySound('../../Sounds/wood-bridge-creak2.wav', 'SoundCrujido2')
soundrechinar[1].Volume=1
soundrechinar[1].MinDistance=10000
soundrechinar[1].MaxDistance=20000


itrap=Bladex.CreateEntity("itrap","Trampilla",-19517.320000+1600,49870.394000,9489.451000)
#itrap=Bladex.CreateEntity("itrap","Trampilla",-19517.320000,49870.394000,9489.451000)
itrap.Static=1
itrap.Scale=0.960981
itrap.Orientation=0.707107,0.707107,0.000000,0.000000


################################################# PARTICULAS ###########################################
Bladex.AddParticleGType("itrapdust","SmokeParticle",B_PARTICLE_GTYPE_BLEND,128)
for i in range(128):
	if i>64:
		traux=0.0
	else:
		traux=(64.0-i)/64.0
	aux=(128.0-i)/128.0
	r=200
	g=170
	b=140
	a=150.0*(1.0-traux)**0.5
	size=4.0+aux*300.0
	Bladex.SetParticleGVal("itrapdust",i,r,g,b,a,size)

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)


Bladex.AddScheduledFunc(Bladex.GetTime(), Lanzador, ())
