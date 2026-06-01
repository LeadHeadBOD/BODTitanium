##///
##||| INITPARTICLESYSTEMS.PY TITANIUM
##||| Change list:
##||| * Venom spit now more visible
##||| * GreenBlood fix - no longer blocky (credit: Sryml)
##\\\ 



def Init():

	import math
	import Bladex
	import Reference



	Bladex.ReadBitMap("../../Data/FirePrtl.bmp","FireParticle")
	Bladex.ReadBitMap("../../Data/Glow.bmp","Glow")
	Bladex.ReadBitMap("../../Data/SunFlare.bmp","SunFlare")
	Bladex.ReadBitMap("../../Data/BloodPrtl.bmp","BloodParticle")
	Bladex.ReadBitMap("../../Data/GreenBloodPrtl.bmp","GreenBloodParticle")
	Bladex.ReadAlphaBitMap("../../Data/BloodDropPrtl.bmp","BloodDropParticle")
	Bladex.ReadAlphaBitMap("../../Data/GenericPrtl.bmp","GenericParticle")
	Bladex.ReadAlphaBitMap("../../Data/GenericPrtl2.bmp","GenericParticle2")
	Bladex.ReadAlphaBitMap("../../Data/SmokePrtl.bmp","SmokeParticle")
	Bladex.ReadAlphaBitMap("../../Data/SmokePrtl2.bmp","SmokeParticle2")
	Bladex.ReadAlphaBitMap("../../Data/Flare magico 128.BMP","MagicFlare128")
	Bladex.ReadAlphaBitMap("../../Data/Water.bmp","WaterParticle")
	Bladex.ReadAlphaBitMap("../../Data/Water2.bmp","WaterParticle2")
	Bladex.ReadAlphaBitMap("../../Data/Estrellita2.bmp","StarParticle")
	Bladex.ReadBitMap("../../Data/SmokePrtl3.bmp","SmokePart3")
	Bladex.ReadBitMap("../../Data/Changre.bmp","ChangreParticle")
	Bladex.ReadAlphaBitMap("../../Data/Estrellita.bmp","Estrellita")


	##### Miguillas Particle definition ######
	Bladex.AddParticleGType("Miguillas","GenericParticle",Reference.B_PARTICLE_GTYPE_BLEND,32)

	for i in range(32):
		traux=(32.0-i)/32.0
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=90
		g=70
		b=60
		a=255*(1.0-traux)
		size=20.0*(1.0-aux)
		Bladex.SetParticleGVal("Miguillas",i,r,g,b,a,size)

	##### GreenFire Particle definition ######
	Bladex.AddParticleGType("GreenFire","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,31)

	for i in range(32):
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=10
		g=205
		b=150+105*aux
		a=255.0*(1.0-aux)
		size=150.0-(aux**2.0)*120.0
		Bladex.SetParticleGVal("GreenFire",i,r,g,b,a,size)


	##### VenomSmoke Particle definition ######
	Bladex.AddParticleGType("VenomSmoke","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,95)

	for i in range(96):
		aux=(96.0-i)/96.0
		r=64
		g=128
		b=64
		a=255.0*math.sqrt(1.0-aux)
		size=40.0+aux*200.0
		Bladex.SetParticleGVal("VenomSmoke",i,r,g,b,a,size)

	##### Fire Particle definition ######

	Bladex.AddParticleGType("Fire","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,31)

	for i in range(32):
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=255
		g=min(300.0*(1.0-aux*aux)+148,255.0)
		b=min(255.0*(1.0-aux)+80,255.0)
		a=min(255.0*(1.0-aux),255.0)
		size=80.0+math.sqrt(1.0-aux)*70.0
		Bladex.SetParticleGVal("Fire",i,r,g,b,a,size)


	##### Large Fire Particle definition ######

	Bladex.AddParticleGType("LargeFire","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,31)

	for i in range(32):
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=255
		g=min(300.0*(1.0-aux*aux)+35,255.0)
		b=min(255.0*(1.0-aux)+20,255.0)
		a=min(200.0*(1.0-aux),255.0)
		size=130.0+math.sqrt(1.0-aux)*110.0
		Bladex.SetParticleGVal("LargeFire",i,r,g,b,a,size)


	##### Big Fire Particle definition ######

	Bladex.AddParticleGType("BigFire","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,31)

	for i in range(32):
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=255
		g=min(300.0*(1.0-aux*aux)+35,255.0)
		b=min(255.0*(1.0-aux)+20,255.0)
		a=min(200.0*(1.0-aux),255.0)
		size=275.0+math.sqrt(1.0-aux)*110.0
		Bladex.SetParticleGVal("BigFire",i,r,g,b,a,size)


	##### Blood Particle definition ######

	Bladex.AddParticleGType("Blood","BloodParticle",Reference.B_PARTICLE_GTYPE_MUL,64)

	for i in range(64):
		if(i>64):
			aux=0.0
		else:
			aux=(64.0-i)/64.0
		r=255
		g=255
		b=255
		a=0
		size=20.0*(1.0-aux)+2.0
		Bladex.SetParticleGVal("Blood",i,r,g,b,a,size)

	##### GreenBlood Particle definition ######

	# Bladex.AddParticleGType("GreenBlood","GenericParticle",Reference.B_PARTICLE_GTYPE_COPY,128)

	# for i in range(128):
		# if(i>64):
			# aux=0.0
		# else:
			# aux=(64.0-i)/64.0
		# r=8
		# g=16
		# b=8
		# a=128
		# size=20.0*(1.0-aux)+2.0
		# Bladex.SetParticleGVal("GreenBlood",i,r,g,b,a,size)
		
	Bladex.AddParticleGType("GreenBlood","GreenBloodParticle",Reference.B_PARTICLE_GTYPE_MUL,64)

	for i in range(64):
		if(i>64):
			aux=0.0
		else:
			aux=(64.0-i)/64.0
		r=255
		g=255
		b=255
		a=0
		size=20.0*(1.0-aux)+2.0
		Bladex.SetParticleGVal("GreenBlood",i,r,g,b,a,size)

	##### GreyBlood Particle definition ######


	Bladex.AddParticleGType("GreyBlood","BloodParticle",Reference.B_PARTICLE_GTYPE_MUL,32)

	for i in range(32):
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=100
		g=100
		b=100
		a=0
		size=20.0*(1.0-aux)+2.0
		Bladex.SetParticleGVal("GreyBlood",i,r,g,b,a,size)


	##### Splinter Particle definition ######

	Bladex.AddParticleGType("Splinter","GenericParticle",Reference.B_PARTICLE_GTYPE_BLEND,16)

	for i in range(16):
		if(i>8):
			aux=0.0
		else:
			aux=(8.0-i)/8.0
		r=190
		g=150
		b=50
		a=255*(1.0-aux)
		size=10.0*(1.0-aux)
		Bladex.SetParticleGVal("Splinter",i,r,g,b,a,size)


	##### Smoke Particle definition ######

	Bladex.AddParticleGType("Smoke","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

	for i in range(64):
		aux=(64.0-i)/64.0
		r=255
		g=255
		b=255
		a=255.0*math.sqrt(1.0-aux)
		size=50.0+aux*300.0
		Bladex.SetParticleGVal("Smoke",i,r,g,b,a,size)

	##### Dark Smoke Particle definition ######
	duration=96
	Bladex.AddParticleGType("DarkSmoke","SmokeParticle2",Reference.B_PARTICLE_GTYPE_BLEND,duration)
	#import pdb
	#pdb.set_trace()
	for i in range(duration):
		if(i>duration/2):
			aux=0.0
		else:
			aux=(duration/2.0-i)/(duration/2.0)
		r=5
		g=3
		b=4
		a=255.0*math.sqrt(1.0-aux)
		size=300.0-(aux**2.0)*240.0
		Bladex.SetParticleGVal("DarkSmoke",i,r,g,b,a,size)

	##### Flame Particle definition #####

	Bladex.AddParticleGType("Flame","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,21)

	for i in range(21):
		if i>=14:
			aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
			caux=(21.0-i)/21.0 #va de 0 a 1/3
			saux=3.0*(21.0-i)/21.0 #va de 0 a 1
		elif i>7 and i<14:
			aux=1.0
			caux=1.0/3.0
			saux=1.0
		else:
			aux=1.0-((7.0-i)/7.0) #va de 1 a 0
			caux=1.0/3.0
			saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
		r=155.0*3.0*caux
		g=155.0*3.0*caux
		b=min(255*(1.0-2.0*caux), 255.0)
		a=100.0*aux
		size=300.0+200.0*saux
		Bladex.SetParticleGVal("Flame",i,r,g,b,a,size)

	##### LargeFlame Particle definition #####

	Bladex.AddParticleGType("LargeFlame","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,21)

	for i in range(21):
		if i>=14:
			aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
			caux=(21.0-i)/21.0 #va de 0 a 1/3
			saux=3.0*(21.0-i)/21.0 #va de 0 a 1
		elif i>7 and i<14:
			aux=1.0
			caux=1.0/3.0
			saux=1.0
		else:
			aux=1.0-((7.0-i)/7.0) #va de 1 a 0
			caux=1.0/3.0
			saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
		r=155.0*3.0*caux
		g=155.0*3.0*caux
		b=min(255*(1.0-2.0*caux), 255.0)
		a=100.0*aux
		size=900.0+600.0*saux
		Bladex.SetParticleGVal("LargeFlame",i,r,g,b,a,size)

	##### DemonShield Particle definition #####

	Bladex.AddParticleGType("DemonShield","MagicFlare128",Reference.B_PARTICLE_GTYPE_BLEND,128)

	for i in range(128):
		"""
		if i>=14:
			aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
			caux=(21.0-i)/21.0 #va de 0 a 1/3
			saux=3.0*(21.0-i)/21.0 #va de 0 a 1
			a=50.0*aux
			size=300.0+200.0*saux

		elif i>7 and i<14:
			aux=1.0
			caux=1.0/3.0
			saux=1.0
			a=50.0*aux
			size=300.0+200.0*saux
		"""
		if i <= 21.0:
			aux=1.0-((7.0-i)/7.0) #va de 1 a 0
			caux=1.0/3.0
			saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
			a=50.0*aux
			size=300.0+200.0*saux

		else:
			aux=(128.0-i)/128.0
			if i>64:
				traux=0.0
			else:
				traux=(64.0-i)/64.0

			a=100.0*(1.0-traux)**0.5
			size=3.0+aux*300.0

		r=max(0.0, min(255*(1.0-2.0*caux), 255.0))
		g=max(0.0, min(255*(1.0-2.0*caux), 255.0))
		b=max(0.0, min(155.0*3.0*caux, 255.0))
		Bladex.SetParticleGVal("DemonShield",i,r,g,b,a,size)


	##### Sand Particle definition #####

	Bladex.AddParticleGType("Sand","GenericParticle",Reference.B_PARTICLE_GTYPE_BLEND,32)

	for i in range(32):
		traux=(32.0-i)/32.0
		if(i>16):
			aux=0.0
		else:
			aux=(16.0-i)/16.0
		r=90
		g=70
		b=60
		a=255*(1.0-traux)
		size=10.0*(1.0-aux)
		Bladex.SetParticleGVal("Sand",i,r,g,b,a,size)


	##### Dust Particle definition #####

	Bladex.AddParticleGType("Dust","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

	for i in range(64):
		if i>32:
			traux=0.0
		else:
			traux=(32.0-i)/32.0
		aux=(64.0-i)/64.0
		r=255
		g=230
		b=210
		a=100.0*(1.0-traux)**0.5
		size=1.0+aux*350.0
		Bladex.SetParticleGVal("Dust",i,r,g,b,a,size)


	##### Large Dust Particle definition #####

	Bladex.AddParticleGType("LargeDust","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,128)

	for i in range(128):
		if i>64:
			traux=0.0
		else:
			traux=(64.0-i)/64.0
		aux=(128.0-i)/128.0
		r=255
		g=230
		b=210
		a=150.0*(1.0-traux)**0.5
		size=10.0+aux*1200.0
		Bladex.SetParticleGVal("LargeDust",i,r,g,b,a,size)


	##### Medium Dust Particle definition #####

	Bladex.AddParticleGType("MediumDust","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,128)

	for i in range(128):
		if i>64:
			traux=0.0
		else:
			traux=(64.0-i)/64.0
		aux=(128.0-i)/128.0
		r=255
		g=230
		b=210
		a=150.0*(1.0-traux)**0.5
		size=4.0+aux*400.0
		Bladex.SetParticleGVal("MediumDust",i,r,g,b,a,size)

	##### Venom Particle definition ######

	duration=32
	max_opacity=180.0
	Bladex.AddParticleGType("Venom","GenericParticle",Reference.B_PARTICLE_GTYPE_BLEND,duration)
	#import pdb
	#pdb.set_trace()
	for i in range(duration):
		if(i>duration/2):
			aux=0.0
		else:
			aux=(duration/2.0-i)/(duration/2.0)
		r=0
		#g=5
		g=65    # Previous was almost black/invisible -LeadHead
		b=0
		a=max_opacity-(max(0,i-duration/2.0)*max_opacity)
		#a= MAX(0, (16.0-i)/16.0)   MIN (1.0, i-16.0     )
		#a=180
		size=30.0*(1.0-aux)+2.0
		Bladex.SetParticleGVal("Venom",i,r,g,b,a,size)

	##### Vomit Particle definition ######

	duration=32
	max_opacity=180.0
	Bladex.AddParticleGType("Vomit","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,duration)
	#import pdb
	#pdb.set_trace()
	for i in range(duration):
		if(i>duration/2):
			aux=0.0
		else:
			aux=(duration/2.0-i)/(duration/2.0)
		r=180
		g=255
		b=180
		a=max_opacity-(max(0,i-duration/2.0)*max_opacity)
		#a= MAX(0, (16.0-i)/16.0)   MIN (1.0, i-16.0     )
		#a=180
		size=30.0*(1.0-aux)+2.0
		Bladex.SetParticleGVal("Vomit",i,r,g,b,a,size)

	Bladex.AddParticleGType("Energia2","GenericParticle",Reference.B_PARTICLE_GTYPE_ADD,120)

	for i in range(120):
		if i>90:
			traux=1-((i-90.0)/30.0) #va de 0 a 1
		elif i<20:
			traux=i/20.0 #va de 1 a 0
		else:
			traux=1.0
		r=100
		g=100
		b=255
		a=255.0*traux
		size=20.0
		Bladex.SetParticleGVal("Energia2",i,r,g,b,a,size)


	##### Demon energy Particle definition ######
	Bladex.AddParticleGType("Energia3","GenericParticle",Reference.B_PARTICLE_GTYPE_ADD,80)

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
		size=20.0
		Bladex.SetParticleGVal("Energia3",i,r,g,b,a,size)

	##### Fiery Invocation Particle definition ######
	Bladex.AddParticleGType("FuegoInvocacion","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,120)

	for i in range(120):
		if i<40:
			traux=i/40.0 #va de 1 a 0
		else:
			traux=1.0
		r=150
		g=100
		b=255
		a=255.0*traux
		size=400.0
		Bladex.SetParticleGVal("FuegoInvocacion",i,r,g,b,a,size)


	##### Energy concentration

	Bladex.AddParticleGType("EnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>10:
			traux=(60.0-i)/50.0 #va de 0 a 1
		else:
			traux=i/10.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=20.0+250.0*(1-i/60.0)**2.0
		Bladex.SetParticleGVal("EnergyConc",i,r,g,b,a,size)


	##### Energy dissipation

	Bladex.AddParticleGType("EnergyDissip","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>50:
			traux=(60.0-i)/10.0 #va de 0 a 1
		else:
			traux=i/50.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=20.0+250.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("EnergyDissip",i,r,g,b,a,size)


	##### Little Energy dissipation

	Bladex.AddParticleGType("LittleEnergyDissip","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/25.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=250.0*(1-(1-i/30.0)**0.5)
		Bladex.SetParticleGVal("LittleEnergyDissip",i,r,g,b,a,size)


	##### Blue Magic Missile

	Bladex.AddParticleGType("BlueMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/25.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=340.0*(1-(1-i/30.0)**0.5)
		Bladex.SetParticleGVal("BlueMagicMissile",i,r,g,b,a,size)


	##### Fast Blue Energy concentration

	Bladex.AddParticleGType("FastEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>5:
			traux=(30.0-i)/25.0 #va de 0 a 1
		else:
			traux=i/5.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=10.0+150.0*(1-i/30.0)**2.0
		Bladex.SetParticleGVal("FastEnergyConc",i,r,g,b,a,size)


	##### Red Magic Missile

	Bladex.AddParticleGType("RedMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/25.0 #va de 1 a 0
		r=255
		g=130
		b=100
		a=255.0*traux
		size=340.0*(1-(1-i/30.0)**0.5)
		Bladex.SetParticleGVal("RedMagicMissile",i,r,g,b,a,size)


	##### Fast Red Energy concentration

	Bladex.AddParticleGType("FastRedEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>5:
			traux=(30.0-i)/25.0 #va de 0 a 1
		else:
			traux=i/5.0 #va de 1 a 0
		r=255
		g=130
		b=100
		a=255.0*traux
		size=10.0+150.0*(1-i/30.0)**2.0
		Bladex.SetParticleGVal("FastRedEnergyConc",i,r,g,b,a,size)


	##### Deep Red Energy concentration

	Bladex.AddParticleGType("DeepRedEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>10:
			traux=(60.0-i)/50.0 #va de 0 a 1
		else:
			traux=i/10.0 #va de 1 a 0
		r=255
		g=50
		b=40
		a=255.0*traux
		size=320.0*(1-i/60.0)**2.0
		Bladex.SetParticleGVal("DeepRedEnergyConc",i,r,g,b,a,size)


	##### Deep Red Magic Missile

	Bladex.AddParticleGType("DeepRedMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=50
		b=40
		a=255.0*traux
		size=400.0*aux
		Bladex.SetParticleGVal("DeepRedMagicMissile",i,r,g,b,a,size)



	###### Snow dust

	Bladex.AddParticleGType("SnowDust","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)
	r=255.0
	g=255.0
	b=255.0
	for i in range(68):
		a    = 255*i/64.0
		size = 256*(64-i)/64.0+256
		if i>64: a =0;size = 0

		Bladex.SetParticleGVal("SnowDust",i,r,g,b,a,size)


	##### Little blue energy concentration

	Bladex.AddParticleGType("LittleBlueEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		r=100
		g=130
		b=255
		a=255.0
		size=60.0*(1-i/30.0)**2.0
		Bladex.SetParticleGVal("LittleBlueEnergyConc",i,r,g,b,a,size)


	##### Blue spark

	Bladex.AddParticleGType("BlueSpark","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,6)

	for i in range(6):
		r=100
		g=130
		b=255
		a=255.0
		size=20.0+10.0*(i/6.0)**2.0
		Bladex.SetParticleGVal("BlueSpark",i,r,g,b,a,size)


	##### Little blue spark

	Bladex.AddParticleGType("LittleBlueSpark","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,6)

	for i in range(6):
		r=100
		g=130
		b=255
		a=255.0
		size=10.0+5.0*(i/6.0)**2.0
		Bladex.SetParticleGVal("LittleBlueSpark",i,r,g,b,a,size)


	##### Deep Green Energy concentration

	Bladex.AddParticleGType("DeepGreenEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,20)

	for i in range(20):
		if i>3:
			traux=1.0
			saux=((20.0-i)/17.0)**2.0 #va de 0 a 1
		else:
			saux=traux=i/3.0 #va de 1 a 0
		r=40
		g=255
		b=60
		a=255.0*traux
		size=100.0*saux
		Bladex.SetParticleGVal("DeepGreenEnergyConc",i,r,g,b,a,size)


	##### Deep Green Magic Missile

	Bladex.AddParticleGType("DeepGreenMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=40
		g=255
		b=60
		a=255.0*traux
		size=400.0*aux
		Bladex.SetParticleGVal("DeepGreenMagicMissile",i,r,g,b,a,size)


	##### Multicolour energy dissipation

	Bladex.AddParticleGType("MulticolourEnergyDissip","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=40
		g=255
		b=60
		a=255.0*traux
		size=300.0*aux
		Bladex.SetParticleGVal("MulticolourEnergyDissip",i,r,g,b,a,size)


	##### Deep Orange Energy concentration

	Bladex.AddParticleGType("DeepOrangeEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>5:
			traux=1.0
			saux=((30.0-i)/25.0)**2.0 #va de 0 a 1
		else:
			saux=traux=i/5.0 #va de 1 a 0
		r=255
		g=100.0*(1.0-i/30.0)
		b=20+80*(i/30.0)
		a=200.0*traux
		size=300.0*saux
		Bladex.SetParticleGVal("DeepOrangeEnergyConc",i,r,g,b,a,size)


	##### Deep Orange Magic Missile

	Bladex.AddParticleGType("DeepOrangeMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=100.0*(i/30.0)
		b=20+80*(1.0-i/30.0)
		a=200.0*traux
		size=400.0*aux
		Bladex.SetParticleGVal("DeepOrangeMagicMissile",i,r,g,b,a,size)


	##### Little Deep Orange Magic Missile

	Bladex.AddParticleGType("LittleDeepOrangeMagicMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,20)

	for i in range(20):
		if i>17:
			traux=(20.0-i)/3.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/17.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=100.0*(i/20.0)
		b=20+80*(1.0-i/20.0)
		a=200.0*traux
		size=250.0*aux
		Bladex.SetParticleGVal("LittleDeepOrangeMagicMissile",i,r,g,b,a,size)


	##### Multicolour Level Up Particles

	Bladex.AddParticleGType("LevelUpParticle","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=255
		b=255
		a=255.0*traux
		size=200.0*aux
		Bladex.SetParticleGVal("LevelUpParticle",i,r,g,b,a,size)


	###
	####################### DALGURAK
	###

	##### Multicolour DalGurak Level Up Particles

	Bladex.AddParticleGType("DGLevelUpParticle","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=255
		b=255
		a=255.0*traux
		size=200.0*aux
		Bladex.SetParticleGVal("DGLevelUpParticle",i,r,g,b,a,size)


	##### DalGurak LifeUp Energy concentration

	Bladex.AddParticleGType("DGLifeUpEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,50)

	for i in range(50):
		if i>5:
			traux=1.0
			saux=((50.0-i)/45.0)**2.0 #va de 0 a 1
		else:
			saux=traux=i/5.0 #va de 1 a 0
		r=255
		g=80
		b=20
		a=200.0*traux
		size=200.0*saux
		Bladex.SetParticleGVal("DGLifeUpEnergyConc",i,r,g,b,a,size)



	###
	####################### DARKLORD
	###

	##### Multicolour DarkLord Level Up Particles

	Bladex.AddParticleGType("DLLevelUpParticle","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=255
		b=255
		a=255.0*traux
		size=300.0*aux
		Bladex.SetParticleGVal("DLLevelUpParticle",i,r,g,b,a,size)


	##### DarkLord LifeUp Energy concentration

	Bladex.AddParticleGType("DLLifeUpEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,50)

	for i in range(50):
		if i>5:
			traux=1.0
			saux=((50.0-i)/45.0)**2.0 #va de 0 a 1
		else:
			saux=traux=i/5.0 #va de 1 a 0
		r=255
		g=40
		b=10
		a=200.0*traux
		size=300.0*saux
		Bladex.SetParticleGVal("DLLifeUpEnergyConc",i,r,g,b,a,size)



	###
	####################### GREATDEMON
	###

	##### Multicolour GreatDemon Level Up Particles

	Bladex.AddParticleGType("GDLevelUpParticle","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
			aux=traux**0.5
		else:
			traux=i/25.0 #va de 1 a 0
			aux=traux**2.0
		r=255
		g=255
		b=255
		a=255.0*traux
		size=400.0*aux
		Bladex.SetParticleGVal("GDLevelUpParticle",i,r,g,b,a,size)


	##### DarkLord LifeUp Energy concentration

	Bladex.AddParticleGType("GDLifeUpEnergyConc","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,50)

	for i in range(50):
		if i>5:
			traux=1.0
			saux=((50.0-i)/45.0)**2.0 #va de 0 a 1
		else:
			saux=traux=i/5.0 #va de 1 a 0
		r=255
		g=140
		b=40
		a=200.0*traux
		size=400.0*saux
		Bladex.SetParticleGVal("GDLifeUpEnergyConc",i,r,g,b,a,size)



	#####################################################
	#     Sistemas de particulas para algunas armas     #
	#####################################################

	##### Definicion de particulas de vapor de hielo seco ######

	Bladex.AddParticleGType("Vaho","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,60)

	for i in range(60):
		if i>40:
			aux=((60.0-i)/20.0)**0.3
		else:
			aux=(i/40.0)**0.5
		r=255
		g=255
		b=255
		a=140.0*aux
		size=50.0+200.0*aux
		Bladex.SetParticleGVal("Vaho",i,r,g,b,a,size)


	##### Definicion de particulas de gas venenoso ######

	Bladex.AddParticleGType("GasVenenoso","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,60)

	for i in range(60):
		if i>40:
			aux=((60.0-i)/20.0)**0.3
		else:
			aux=(i/40.0)**0.5
		r=85
		g=90
		b=0
		a=200.0*aux
		size=50.0+200.0*aux
		Bladex.SetParticleGVal("GasVenenoso",i,r,g,b,a,size)


	##### Definicion de particulas de gas venenoso2 ######

	Bladex.AddParticleGType("GasVenenoso2","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,60)

	for i in range(60):
		if i>40:
			aux=((60.0-i)/20.0)**0.3
		else:
			aux=(i/40.0)**0.5
		r=10
		g=180
		b=160
		a=255.0*aux
		size=400.0+800.0*aux
		Bladex.SetParticleGVal("GasVenenoso2",i,r,g,b,a,size)


	##### Definicion de particulas de gotas de sangre ######

	Bladex.AddParticleGType("GotasSangre","BloodDropParticle",Reference.B_PARTICLE_GTYPE_BLEND,24)

	for i in range(24):
		if i>20:
			aux=((24.0-i)/4.0)**0.5
		elif i<8:
			aux=(i/8.0)**0.5
		else:
			aux=1.0
		r=60
		g=0
		b=0
		a=220.0*aux+35.0
		size=16.0*aux+4.0
		Bladex.SetParticleGVal("GotasSangre",i,r,g,b,a,size)


	##### Definicion de llamitas ######

	Bladex.AddParticleGType("Llamita","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,21)

	for i in range(21):
		if i>=14:
			aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
			caux=(21.0-i)/21.0 #va de 0 a 1/3
			saux=3.0*(21.0-i)/21.0 #va de 0 a 1
		elif i>7 and i<14:
			aux=1.0
			caux=1.0/3.0
			saux=1.0
		else:
			aux=1.0-((7.0-i)/7.0) #va de 1 a 0
			caux=1.0/3.0
			saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
		r=155.0*3.0*caux
		g=155.0*3.0*caux
		b=min(255*(1.0-2.0*caux), 255.0)
		a=200.0*aux
		size=4.0+6.0*saux
		Bladex.SetParticleGVal("Llamita",i,r,g,b,a,size)


	##### Definicion de brillitos ######

	Bladex.AddParticleGType("BrillosBladeSword","StarParticle",Reference.B_PARTICLE_GTYPE_ADD,8)

	for i in range(8):
		if i>5:
			aux=(8.0-i)/3.0
		else:
			aux=i/5.0
		r=235.0
		g=245.0
		b=255.0
		a=255.0
		size=100.0*aux
		Bladex.SetParticleGVal("BrillosBladeSword",i,r,g,b,a,size)



	################################################################################
	#     Sistemas de particulas para el efecto de algunas armas en personajes     #
	################################################################################


	##### Definicion de llamitas2 ######

	Bladex.AddParticleGType("Llamita2","FireParticle",Reference.B_PARTICLE_GTYPE_ADD,21)

	for i in range(21):
		if i>=14:
			aux=1.0/3.0+2*(21.0-i)/21.0 #va de 1/3 a 1
			caux=(21.0-i)/21.0 #va de 0 a 1/3
			saux=3.0*(21.0-i)/21.0 #va de 0 a 1
		elif i>7 and i<14:
			aux=1.0
			caux=1.0/3.0
			saux=1.0
		else:
			aux=1.0-((7.0-i)/7.0) #va de 1 a 0
			caux=1.0/3.0
			saux=1.0-2*((7.0-i)/7.0) #va de 1 a -1
		r=155.0*3.0*caux
		g=155.0*3.0*caux
		b=min(255*(1.0-2.0*caux), 255.0)
		a=160.0*aux
		size=80.0*saux
		Bladex.SetParticleGVal("Llamita2",i,r,g,b,a,size)


	##### Estela roja

	Bladex.AddParticleGType("RedTrail","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>55:
			traux=(60.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/55.0 #va de 1 a 0
		r=255
		g=20
		b=10
		a=255.0*traux
		size=20+200.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("RedTrail",i,r,g,b,a,size)


	##### Estela verde

	Bladex.AddParticleGType("GreenTrail","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>55:
			traux=(60.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/55.0 #va de 1 a 0
		r=10
		g=255
		b=50
		a=255.0*traux
		size=20+200.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("GreenTrail",i,r,g,b,a,size)


	##### Estela azul

	Bladex.AddParticleGType("BlueTrail","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>55:
			traux=(60.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/55.0 #va de 1 a 0
		r=10
		g=50
		b=255
		a=255.0*traux
		size=20+200.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("BlueTrail",i,r,g,b,a,size)


	##### Estela blanca

	Bladex.AddParticleGType("WhiteTrail","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>55:
			traux=(60.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/55.0 #va de 1 a 0
		r=255
		g=255
		b=255
		a=255.0*traux
		size=20+200.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("WhiteTrail",i,r,g,b,a,size)


	##### Estela amarilla

	Bladex.AddParticleGType("YellowTrail","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,60)

	for i in range(60):
		if i>55:
			traux=(60.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/55.0 #va de 1 a 0
		r=255
		g=230
		b=10
		a=255.0*traux
		size=20+200.0*(1-(1-i/60.0)**0.5)
		Bladex.SetParticleGVal("YellowTrail",i,r,g,b,a,size)


	######################################################################
	#     Sistemas de particulas para el misil de la espada de Blade     #
	######################################################################

	Bladex.AddParticleGType("BladeSwordMissile","GenericParticle2",Reference.B_PARTICLE_GTYPE_ADD,30)

	for i in range(30):
		if i>25:
			traux=(30.0-i)/5.0 #va de 0 a 1
		else:
			traux=i/25.0 #va de 1 a 0
		r=100
		g=130
		b=255
		a=255.0*traux
		size=20.0+250.0*(1-(1-i/30.0)**0.5)
		Bladex.SetParticleGVal("BladeSwordMissile",i,r,g,b,a,size)


	################################################################################
	#     Sistemas de particulas para el golem de barro                            #
	################################################################################

	Bladex.AddParticleGType("ShitSmoke","SmokeParticle",Reference.B_PARTICLE_GTYPE_BLEND,64)

	for i in range(64):
		aux=(64.0-i)/64.0
		r=128
		g=80
		b=32
		a=255.0*math.sqrt(1.0-aux)
		size=40.0+aux*200.0
		Bladex.SetParticleGVal("ShitSmoke",i,r,g,b,a,size)

	Bladex.AddParticleGType("SacredFX","GenericParticle",Reference.B_PARTICLE_GTYPE_ADD,16)

	for i in range(16):
		aux = 1.0-i/16.0
		r=205
		g=150
		b=10
		a=(1-aux)*128.0
		size=aux*32
		Bladex.SetParticleGVal("SacredFX",i,r,g,b,a,size)

	Bladex.AddParticleGType("DeathCloud","SmokePart3",Reference.B_PARTICLE_GTYPE_MUL,64)


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

	Bladex.AddParticleGType("AnkBlood","ChangreParticle",Reference.B_PARTICLE_GTYPE_MUL,32)

	for i in range(32):
		aux=(32.0-i)/32.0
		r=255.0
		g=255.0
		b=255.0
		a=0
		size=100*(1.0-aux)**0.5
		Bladex.SetParticleGVal("AnkBlood",i,r,g,b,a,size)

	# LucesCools y duendes
	Bladex.AddParticleGType("LucesCools","Estrellita",1,16)
	for i in range(16):
		Tetha = 8-abs(i-8)
		r=255.0
		g=255.0
		b=255.0
		a   = (Tetha*255)/9
		size= Tetha*20
		Bladex.SetParticleGVal("LucesCools",i,r,g,b,a,size)
