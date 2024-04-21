##///
##||| RAGNAR_M2/PENDULOS.PY TITANIUM
##||| Change list:
##||| * Pendulum trap should now be at 60fps
##\\\ 

import def_class
import Bladex
import AuxFuncs
import Sounds



MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

Bladex.CreateTimer("Timer30",1.0/30.0)

MuerteBarb1=Bladex.CreateSound('../../sounds/muerte-barb-1.wav', 'MuerteBarbaro1')

Bladex.AddParticleGType("Flame","FireParticle",B_PARTICLE_GTYPE_ADD,20)

for i in range(20):
	if i>14:
		aux=1.0
		caux=1.0/3.0
		saux=1.0
	else:
		aux=1.0-((14.0-i)/14.0) #va de 1 a 0
		caux=1.0/3.0
		saux=1.0-2*((14.0-i)/14.0) #va de 1 a -1

	r=155.0*3.0*caux
	g=155.0*3.0*caux
	b=min(255*(1.0-2.0*caux), 255.0)
	a=150.0*aux
	size=600.0+200.0*saux
	Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)


Bladex.AddParticleGType("Explode","FireParticle",B_PARTICLE_GTYPE_ADD,20)

for i in range(20):
	if i>14:
		aux=1.0
		caux=1.0/3.0
		saux=1.0
	else:
		aux=1.0-((14.0-i)/14.0) #va de 1 a 0
		caux=1.0/3.0
		saux=1.0-2*((14.0-i)/14.0) #va de 1 a -1

	r=155.0*3.0*caux
	g=155.0*3.0*caux
	b=min(255*(1.0-2.0*caux), 255.0)
	a=150.0*aux
	size=300.0+300.0*saux
	Bladex.SetParticleGVal("Explode",i,r,g,b,a,size)



Trampa_Pendulos = 0
DesactivarPendulos = 0
ExHitFunc = 0



P1 = CreatePendulo("Pendulo1")
P1.Piv = [0,0,4900]
P1.Axi = [1,0,0]
P1.Angulo = 0
P1.Dir = 1
P1.Vel = 0.015 #0.03
P1.fAc = -0.0015 # -0.003

P2 = CreatePendulo("Pendulo2")
P2.Piv = [0,0,4900]
P2.Axi = [1,0,0]
P2.Angulo = 0
P2.Dir = -1
P2.Vel = 0.013 # 0.026
P2.fAc = -0.00225 # -0.0045

P1.Pendulo.RotateRel(P1.Piv[0],P1.Piv[1],P1.Piv[2],P1.Axi[0],P1.Axi[1],P1.Axi[2],0)
P2.Pendulo.RotateRel(P2.Piv[0],P2.Piv[1],P2.Piv[2],P2.Axi[0],P2.Axi[1],P2.Axi[2],0)



zoc1 = Bladex.GetEntity("zoc1")
zoc2 = Bladex.GetEntity("zoc2")
pen1 = Bladex.GetEntity("Pendulo1")
pen2 = Bladex.GetEntity("Pendulo2")

zoc1.ExcludeHitFor(pen1)
zoc1.ExcludeHitFor(pen2)
zoc2.ExcludeHitFor(pen1)
zoc2.ExcludeHitFor(pen2)

Pendulo_Sector1 = Bladex.GetSector(-96121.5769213, 6251.5, -87959.059290)
Pendulo_Sector1.OnEnter = Activar_Pendulos
Pendulo_Sector1.OnLeave = Desactivar_Pendulos
Pendulo_Sector2 =  Bladex.GetSector(-102168.828801, 7251.5, -94608.10031)
Pendulo_Sector2.OnEnter = ActivarDesactivadoPendulos
