##///
##||| ORLOK_M10/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Ice golem now collapses like all other golems
##\\\ 


import ScriptSkip
import GotoMapVars
import AuxFuncs
import Scorer



#################################################################################################
## Positions.py


def IrPosicion1():
	char=Bladex.GetEntity("Player1")
	char.Position=-61000.0, -32500.0, -8000.0	# valle interior 1

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-26000, -35000, 41500		# entrada laberinto

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=-24000, -34500, 74000		# dentro del laberinto

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=7122, -33664, 69075		# dentro de la fortificacion (cerca entr. secr.)

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=44500, -42250, 64000		# dentro de la fortificacion (junto al orbe)

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=14000, -33000, 69000		# dentro de la fortificacion (junto al pedestal del orbe)

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=25000, -33164.0, 66000.0	# dentro de la fortificacion (junto a la llave)

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=8000.0, 825.0, 12450.0	# final

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=32400, -3350, -33360		# fuentes

posicion1=IrPosicion1
posicion2=IrPosicion2
posicion3=IrPosicion3
posicion4=IrPosicion4
posicion5=IrPosicion5
posicion6=IrPosicion6
posicion7=IrPosicion7
posicion8=IrPosicion8
posicion9=IrPosicion9




#################################################################################################
## Sonidos.py


def SuenaViento1(sectorindex,entityname):
    if entityname=='Player1':
	viento1.Play(-35000,-31000,-24000,0)
        z1.OnEnter=""




#################################################################################################
## Inicio.py


###########################
##	Funcionamiento
###########################


def Alud3():
	piedra1.RemoveFromWorld()
	piedra2.RemoveFromWorld()
	piedra3.RemoveFromWorld()
	sd1alud.DoBreak((0.0, 0.0, 4.0), (-62500.0, -29000.0, -75500.0), (0.0, 0.0, 0.0))
	sd2alud.DoBreak((0.0, 0.0, 4.0), (-60500.0, -29000.0, -75000.0), (0.0, 0.0, 0.0))
	sd3alud.DoBreak((0.0, 0.0, 4.0), (-59000.0, -29000.0, -73500.0), (0.0, 0.0, 0.0))
	nieve=Bladex.CreateEntity("Nieve2Alud", "Entity Particle System D2", -63000.0, -29000.0, -76250.0)
	nieve.D=5500.0, 0.0, 2000.0
	nieve.ParticleType="Nieve"
	nieve.YGravity=4900.0
	nieve.Friction=0.05
	nieve.PPS=200
	nieve.Velocity=-300.0, -1200.0, 1000.0
	nieve.RandomVelocity=80.0
	nieve.Time2Live=120
	nieve.DeathTime=Bladex.GetTime()+2.25

def Alud2():
	su2alud.DoBreak((0.0, 0.0, 1.0), (-59000.0, -40000.0, -78000.0), (0.0, 0.0, 0.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, Alud3, ())

def Alud():
	su1alud.DoBreak((0.0, 0.0, 1.0), (-59000.0, -35000.0, -78000.0), (0.0, 0.0, 0.0))
	nieve=Bladex.CreateEntity("Nieve1Alud", "Entity Particle System D2", -62500.0, -36000.0, -77750.0)
	nieve.D=5500.0, 0.0, 2000.0
	nieve.ParticleType="Nieve"
	nieve.YGravity=4900.0
	nieve.Friction=0.05
	nieve.PPS=200
	nieve.Velocity=-300.0, 400.0, 1000.0
	nieve.RandomVelocity=80.0
	nieve.Time2Live=120
	nieve.DeathTime=Bladex.GetTime()+2.0
	polvo=Bladex.CreateEntity("PolvoAlud", "Entity Particle System D2", -62500.0, -32000.0, -77750.0)
	polvo.D=5500.0, 0.0, 2000.0
	polvo.ParticleType="Polvo"
	polvo.YGravity=0.0
	polvo.Friction=0.05
	polvo.PPS=50
	polvo.Velocity=-500.0, 1000.0, 2000.0
	polvo.RandomVelocity=80.0
	polvo.Time2Live=120
	polvo.DeathTime=Bladex.GetTime()+3.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, Alud2, ())

def ReiniciaCamaraInicio(camera, frame):
	cam=Bladex.GetEntity("Camera")
	Bladex.SetListenerPosition(1)
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaexterior"))
	roca1.PutToWorld()
	roca2.PutToWorld()
	roca3.PutToWorld()
	roca4.PutToWorld()

def Camara2(camera, frame):
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("inicio_desfil_cam2.cam",324,439)
	cam.AddCameraEvent(-1, ReiniciaCamaraInicio)
	sonidoalud.Play(-60000, -32000, -76000, 0)

def ReposicionaPlayerInicio(person):
	char=Bladex.GetEntity("Player1")
	char.LaunchAnmType("Rlx")
	char.Position=-45800.0, -31120.0, -73500.0
	char.Angle=3.14159/2.0
	char.SetOnFloor()

def SuenaPiedra(piedran, sound):
	x, y, z = piedran.Position
	sound.Play(x, y, z, 0)

def SueltaPiedra1():
	piedra1.PutToWorld()
	piedra1.Impulse(0.0, 0.0, 200.0) # 3000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, SuenaPiedra, (piedra1, golpepiedranieve1))

def SueltaPiedras23():
	piedra2.PutToWorld()
	piedra2.Impulse(-20.0, 0.0, 60.0) # -1000.0, 0.0, 3000.0)
	piedra3.PutToWorld()
	piedra3.Impulse(-30.0, 0.0, 100.0) # -1000.0, 0.0, 3000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, SuenaPiedra, (piedra2, golpepiedranieve2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.1, SuenaPiedra, (piedra3, golpepiedranieve1))

def RegueroNieve1():
	SueltaPiedra1()
	rnieve1=Bladex.CreateEntity("RegueroNieve1", "Entity Particle System D1", -58706.0, -34000.0, -75520.0)
	rnieve1.ParticleType="PolvilloNieve"
	rnieve1.YGravity=4000.0
	rnieve1.Friction=0.15
	rnieve1.PPS=100
	rnieve1.Velocity=0.0, 0.0, 0.0
	rnieve1.RandomVelocity=4.0
	rnieve1.Time2Live=80
	rnieve1.DeathTime=Bladex.GetTime()+4.0
	cortinanieve.Play(-60000, -32000, -76000, 0)

def RegueroNieve2():
	SueltaPiedras23()
	rnieve2=Bladex.CreateEntity("RegueroNieve2", "Entity Particle System D2", -59720.0, -33000.0, -75945.0)
	rnieve2.D=-1333.0, -1800.0, -610.0
	rnieve2.ParticleType="PolvilloNieve"
	rnieve2.YGravity=3400.0
	rnieve2.Friction=0.15
	rnieve2.PPS=300
	rnieve2.Velocity=0.0, 0.0, 0.0
	rnieve2.RandomVelocity=4.0
	rnieve2.Time2Live=80
	rnieve2.DeathTime=Bladex.GetTime()+2.0

def Comienza():
	AuxFuncs.FadeFrom(1.0, 0.0)
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("inicio_desfil_cam1.cam",0,323)
	cam.AddCameraEvent(-1, Camara2)
	char=Bladex.GetEntity("Player1")
	pasosinicorlok=[63, 73, 83, 93, 103, 113, 123, 133, 143, 153, 163, 173, 183, 193, 203, 213, 223, 233, 243, 253, 263, 347, 352, 359, 365, 371, 377, 383, 389]
	for n in pasosinicorlok:
		np=whrandom.randint(1, 3)
		if np==1:
			sndpaso=orlokpasonie1
		elif np==2:
			sndpaso=orlokpasonie2
		else:
			sndpaso=orlokpasonie3
		NetSounds.AddAnimSound(char, char.CharTypeExt[:3]+'_inicio_desfil', sndpaso, n/390.0)
	#char.SetTmpAnmFlags(1,1,1,0,3,1)	valores por defecto
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("inicio_desfil")
	char.Position=-79077.0, -31061.0, -75518.0
	char.Angle=3.14159
	char.SetOnFloor()
	char.AnmEndedFunc=ReposicionaPlayerInicio
	Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, RegueroNieve1, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+13.0, RegueroNieve2, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+16.5, Alud, ())

def ComienzoPrevio3():
	AuxFuncs.FadeFrom(1.0, 0.0)
	AuxFuncs.MoveCamFromTo(16900.0, -25100.0, 90300.0, 31800.0, -33800.0, 95600.0, 22100.0, -27400.0, 82000.0, 27900.0, -36400.0, 86800.0, 11.0, Comienza)
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, AuxFuncs.FadeTo, (1.0, 0.0))

def ComienzoPrevio2():
	AuxFuncs.FadeFrom(1.0, 0.0)
	AuxFuncs.MoveCamFromTo(37200.0, -41300.0, 151400.0, 31400.0, -33400.0, 154200.0, 32700.0, -36600.0, 159000.0, 34500.0, -35800.0, 163400.0, 13.0, ComienzoPrevio3)
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, AuxFuncs.FadeTo, (1.0, 0.0))

def ComienzoPrevio():
	Scorer.SetVisible(0)
	AuxFuncs.FadeFrom(2.0, 0.0)
	ScriptSkip.SkipScriptStart("EscenaInicio")
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(-23500.0, -54500.0, -37800.0, -21500.0, -48100.0, -22800.0, -23000.0, -45200.0, -34000.0, -18000.0, -46400.0, -13500.0, 13.0, ComienzoPrevio2)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_inicio"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, GameText.WriteText, ("M10T1",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, AuxFuncs.FadeTo, (1.0, 0.0))




#################################################################################################
## Puente.py


############################
##	Funcionamiento
############################


def DespiertaOrcoPuente(person):
	ene=Bladex.GetEntity(person)
	ene.Blind=0
	ene.Deaf=0

def ColocacionOrcosPuente():
	orcopuente1.GoToJogging=1
	orcopuente2.GoToJogging=1
	orcopuente1.GoTo(-48250, -31500, -62500)
	orcopuente2.GoTo(-45750, -31500, -62000)
	DespiertaOrcoPuente(orcopuente1.Name)
	DespiertaOrcoPuente(orcopuente2.Name)
#	orcopuente1.RouteEndedFunc=DespiertaOrcoPuente
#	orcopuente2.RouteEndedFunc=DespiertaOrcoPuente

def AparecenOrcosPuente(sec_index, ent_name):
	if ent_name=="Player1":
		puente.OnEnter=""
		puertapuente.OpenDoor()
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, ColocacionOrcosPuente, ())
		# Esto es para que la palanganita de los cojones no produzca una sombra defectuosa de la columna sobre la que se apoya.
		Bladex.GetEntity("PutaPalangana").Move(0,0,0)




#################################################################################################
## Generadores.py


###################################################
#     Funciones complementarias del generador     #
###################################################

def RemueveNieveGen(gen_pos, v1, v2, v3):
	nieve=Bladex.CreateEntity("NieveRemoviendose", "Entity Particle System D3", gen_pos[0]+v1[0], gen_pos[1]-1250.0, gen_pos[2]+v1[2]) # -900.0, gen_pos[2]+v1[2])
	nieve.D1=v2[0]-v1[0], 0.0, v2[2]-v1[2]
	nieve.D2=v3[0]-v1[0], 0.0, v3[2]-v1[2]
	nieve.ParticleType="PolvoNieve"
	nieve.PPS=64
	nieve.YGravity=200.0
	nieve.Friction=0.1
	nieve.Velocity=0.0, -400.0, 0.0
	nieve.RandomVelocity=15.0
	nieve.Time2Live=64
	nieve.DeathTime=Bladex.GetTime()+2.0

def SaltaNieveGen(gen_pos, susto):
	if susto:
		Bladex.KillMusic()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicavalles"))
	char=Bladex.GetEntity("Player1")
	v=char.Position[0]-gen_pos[0], 0.0, char.Position[2]-gen_pos[2]
	v=AuxFuncs.Normalize(v)
	v1=v[0]*500.0, 0.0, v[2]*500.0
	v2=v1[0]*math.cos(1.7453)-v1[2]*math.sin(1.7453), 0.0, v1[0]*math.sin(1.7453)+v1[2]*math.cos(1.7453)
	v3=v2[0]*math.cos(2.7925)-v2[2]*math.sin(2.7925), 0.0, v2[0]*math.sin(2.7925)+v2[2]*math.cos(2.7925)
	saltanie=Bladex.CreateEntity("NieveSaltando", "Entity Particle System D1", gen_pos[0], gen_pos[1]-1250.0, gen_pos[2]) # -900.0, gen_pos[2])
	saltanie.ParticleType="Nievecilla"
	saltanie.PPS=1024
	saltanie.YGravity=4900.0
	saltanie.Friction=0.05
	saltanie.Velocity=0.0, -600.0, 0.0
	saltanie.RandomVelocity=50.0
	saltanie.Time2Live=60
	saltanie.DeathTime=Bladex.GetTime()+10.0/60.0
	saltani2=Bladex.CreateEntity("NieveSaltando2", "Entity Particle System D1", gen_pos[0], gen_pos[1]-1250.0, gen_pos[2]) # -900.0, gen_pos[2])
	saltani2.ParticleType="PolvoNieve"
	saltani2.PPS=128
	saltani2.YGravity=200.0
	saltani2.Friction=0.1
	saltani2.Velocity=0.0, -300.0, 0.0
	saltani2.RandomVelocity=15.0
	saltani2.Time2Live=32
	saltani2.DeathTime=Bladex.GetTime()+10.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, RemueveNieveGen, (gen_pos, v1, v2, v3))


###############################################
#     Generadores explanada fortificacion     #
###############################################

def ZombieListo(person):
	Bladex.GetEntity(person + "quad").SubscribeToList("Pin")
	char=Bladex.GetEntity("Player1")
	enm=Bladex.GetEntity(person)
	enm.InitPos=enm.Position
	alfa=AuxFuncs.Pos2PosXZAngle(enm.Position, char.Position)
	enm.Face(alfa)
	enm.Blind=0
	enm.Deaf=0
	Bladex.AddScheduledFunc(Bladex.GetTime(), enm.SetOnFloor, ())

def LevantaZombieExplanada(person, gen_pos):
	enm=Bladex.GetEntity(person)
	char=Bladex.GetEntity("Player1")
	enm.UnFreeze()
	enm.SetTmpAnmFlags(1,1,1,0,5,1,0)
	enm.LaunchAnmType("appears1")
	enm.Position=gen_pos
	alfa=AuxFuncs.Pos2PosXZAngle(enm.Position, char.Position)
	enm.Angle=alfa
	enm.AnmEndedFunc=ZombieListo
	darfuncs.CreateFalseCube(gen_pos,-1.0,enm.Name)
	SaltaNieveGen(gen_pos, 0)

def ZombiesExplanada(tr_sector, ent_name):
	Bladex.RemoveTriggerSectorFunc(tr_sector, "OnEnter")
	Bladex.KillMusic()
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaexterior"))
	gen1_pos=19000, -30850, 57500
	gen2_pos=26000, -30850, 53500
	gen3_pos=31000, -30850, 59500
	LevantaZombieExplanada("OrlokZombieExpl1", gen1_pos)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, LevantaZombieExplanada, ("OrlokZombieExpl2", gen2_pos))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LevantaZombieExplanada, ("OrlokZombieExpl3", gen3_pos))


#############################
#     Restos de batalla     #
#############################

#def MuertosExplanada():
#	muertoexpl1.SeverLimb(1)
#	muertoexpl2.SeverLimb(6)
#	muertoexpl1.Life=0
#	muertoexpl2.Life=0




#################################################################################################
## Collaps.py


####################################
#     Derrumbamiento del valle     #
####################################

def ContDerValle():
	dervalle.DoBreak((0.0, 0.0, 0.0), (-65750.0, -34000.0, 3500.0), (0.0, 0.0, 0.0))

def DerValle(sector_index, entity_name):
	derrumbesuelopiedra.Play(-65750.0, -34000.0, 3500.0, 0)
	secdervalle1.OnWalkOn=""
	secdervalle2.OnWalkOn=""
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ContDerValle, ())


########################
#     Muros falsos     #
########################

def RompeMuroFalsoLab(sector_index, entity_name, px, py, pz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	sonidoroturamurofalso.Play(-38625.0, -37000.0, 85220.0, 0)
	secmurofalsolab.DoBreak((1.2, 0.0, 1.2), (px, py, pz), (0.0, 0.0, 0.0))
	secrompemurofalsolab.OnHit=""
	luzantsecr.Intensity=4.0


##############################################
#     Derrumbamiento en la fortificacion     #
##############################################

def ContDerFort():
	derfort.DoBreak((0.0, -0.5, 0.0), (41250.0, -41125.0, 73750.0), (0.0, 0.0, 0.0))

def DerFort(sector_index, entity_name):
	derrumbesuelopiedra.Play(41250.0, -41125.0, 73750.0, 0)
	secderfort.OnWalkOn=""
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, ContDerFort, ())




#################################################################################################
## Pinchos.py


########################################
#     Pincho de la entrada secreta     #
########################################

def Solidifica(pincho):
	pincho.Solid=1

def LanzaPinchoLab():
	global pincholabactivado
	if pincholabactivado:
		pincholab.Solid=0
		pincholab.MessageEvent(MESSAGE_START_WEAPON,0,0)
		Objects.DisplaceObject(pincholabdin, 2800.0, (0.0, -1.0, 0.0), 20000.0, 20000.0, pinchodeslizando, "", pinchogolpeando, "", (), Solidifica, (pincholab,))
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, RecogePinchoLab, ())

def RecogePinchoLab():
	Objects.DisplaceObject(pincholabdin, 2800.0, (0.0, 1.0, 0.0), 20000.0, 20000.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, LanzaPinchoLab, ())

def ActivaPinchoLab():
	global pincholabactivado
	pincholabactivado=1
	LanzaPinchoLab()

def DesactivaPinchoLab():
	global pincholabactivado
	pincholabactivado=0



######################################
#     Pinchos del derrumbamiento     #
######################################

def ReposicionaPlayer(x, y, z):
	char=Bladex.GetEntity("Player1")
	char.Position=x, y, z
	Bladex.SetTriggerSectorFunc("TrampaPinchos", "OnEnter", MuertePinchos)

def MuertePinchos(trsector_name, entity_name):
	pers=Bladex.GetEntity(entity_name)
	if pers and pers.Person:
		pers.Life=0
		if entity_name=="Player1":
			Bladex.RemoveTriggerSectorFunc("TrampaPinchos", "OnEnter")
			AuxFuncs.FadeTo(1.5, 3.5, 80, 0, 0)
			Bladex.AddScheduledFunc(Bladex.GetTime()+4.8, ReposicionaPlayer, (-68841, -35624, 2896))





#################################################################################################
## Guarida.py


###########################
##	Funcionamiento
###########################

def rep():
	trolllab.Position=-23500.0, -34500.0, 90000.0
	murotroll.Active=0
	murotrolli1.Active=0
	murotrolli2.Active=0
	murotrolld.Active=0
	slanzatroll.OnEnter=LanzaTroll

def DespiertaTroll(person):
	cubotroll.SubscribeToList("Pin")
	trolllab.Blind=0
	trolllab.Deaf=0

def LanzaTroll(sec_idx, ent_name):
	if ent_name=="Player1":
		slanzatroll.OnEnter=""
		Bladex.KillMusic()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicacuevas"))
		sonidoroturamurotroll.Play(-23875.0, -34500.0, 87000.0, 0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, rugidoroturamurotroll.Play, (-23875.0, -34500.0, 87000.0, 0))
		murotroll.DoBreak((0.0, -0.5, -2.5), (-23875.0, -34500.0, 87000.0), (0.0, 0.0, 0.0))
		murotrolli1.DoBreak((0.0, -0.5, -1.5), (-25000.0, -34000.0, 87000.0), (0.0, 0.0, 0.0))
		murotrolli2.DoBreak((0.0, -0.5, -1.5), (-25000.0, -36000.0, 87000.0), (0.0, 0.0, 0.0))
		murotrolld.DoBreak((0.0, -0.5, -1.5), (-22750.0, -34500.0, 87000.0), (0.0, 0.0, 0.0))
		polvo=Bladex.CreateEntity("PolvoMuro", "Entity Particle System D2", -23875.0, -34000.0, 87000.0)
		polvo.D=0.0, -2000.0, 0.0
		polvo.ParticleType="PolvoRoca"
		polvo.YGravity=0.0
		polvo.Friction=0.05
		polvo.PPS=200
		polvo.Velocity=0.0, 0.0, -1000.0
		polvo.RandomVelocity=40.0
		polvo.Time2Live=100
		polvo.DeathTime=Bladex.GetTime()+0.1
		trolllab.SetTmpAnmFlags(1,1,1,0,5,1,0)
		trolllab.LaunchAnmType("orlok_brk_wll")
		trolllab.SetOnFloor()
		trolllab.AnmEndedFunc=DespiertaTroll




#################################################################################################
## Orbe.py


#######################################
###     Funcionamiento previo orbe
#######################################

def ReseteaCamaraOrbe():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ExeMusicEvent(-1)

def MueveChispasOrbe(psys):
	psys.Position=orbe.Position

def FlotaOrbe():
	global orbeflotando
	if orbeflotando:
		despl=(50.0, 50.0, 50.0, 50.0)
		vect=(ejeyn, ejeyn, ejey, ejey)
		vel_inic=(0.0, 200.0, 0.0, 200.0)
		vel_fin=(200.0, 0.0, 200.0, 0.0)
		Objects.NDisplaceObject(orbedin, despl, vect, vel_inic, vel_fin, (), (), (), MueveChispasOrbe, (chorbe,), FlotaOrbe, ())

def ParaFlotacionOrbe(tr_sector, ent_name):
	global orbeflotando
	if ent_name=="Player1":
		orbeflotando=0

def LanzaFlotacionOrbe(tr_sector, ent_name):
	global orbeflotando
	if ent_name=="Player1":
		orbeflotando=1
		FlotaOrbe()


#########################################
###     Funcionamiento pedestal orbe
#########################################

def ApagaRayos():
	global chelec
	global chelec1
	global chelec2
	global chelec3
	rayoob.Active=0
	rayog1.Active=0
	rayog2.Active=0
	luzob1.Intensity=0.0
	luzob2.Intensity=0.0
	luzg1.Intensity=0.0
	luzg2.Intensity=0.0
	chelec.DeathTime=Bladex.GetTime()+2.0
	chelec1.DeathTime=Bladex.GetTime()+2.0
	chelec2.DeathTime=Bladex.GetTime()+2.0
	chelec3.DeathTime=Bladex.GetTime()+2.0

def ParaCamaraPuertas(camera, frame):
	ApagaRayos()
	ReseteaCamaraOrbe()
	ene=Bladex.GetEntity("OrlokOrcoTejadoNorte")
	if ene and ene.Life>0:
		ene.Blind=0
		ene.Deaf=0

def AbrePuertas():
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("apertura_puertas.cam",0,240)
	cam.AddCameraEvent(-1, ParaCamaraPuertas)
	puerta1.OpenDoor()
	puerta2.OpenDoor()
	puerta3.OpenDoor()
	puerta4.OpenDoor()
	sndrayo1.Stop()
	sndrayo2.Stop()
	sndrayo3.Stop()

def RayosObeliscoGargolas():
	global chelec1
	global chelec2
	global chelec3
	chelec1=Bladex.CreateEntity("ChispasElectricidadOb2", "Entity Particle System D1", 18710.0, -37600.0, 68980.0)
	chelec1.ParticleType="ChispaElectrica"
	chelec1.YGravity=800.0
	chelec1.Friction=0.06
	chelec1.PPS=80
	chelec1.Velocity=0.0, -500.0, 0.0
	chelec1.RandomVelocity=20.0
	chelec1.Time2Live=40
	chelec2=Bladex.CreateEntity("ChispasElectricidadG1", "Entity Particle System D1", 16800.0, -38400.0, 66070.0)
	chelec2.ParticleType="ChispaElectrica"
	chelec2.YGravity=800.0
	chelec2.Friction=0.06
	chelec2.PPS=80
	chelec2.Velocity=0.0, 0.0, 0.0
	chelec2.RandomVelocity=15.0
	chelec2.Time2Live=40
	chelec3=Bladex.CreateEntity("ChispasElectricidadG2", "Entity Particle System D1", 16840.0, -38400.0, 71930.0)
	chelec3.ParticleType="ChispaElectrica"
	chelec3.YGravity=800.0
	chelec3.Friction=0.06
	chelec3.PPS=80
	chelec3.Velocity=0.0, 0.0, 0.0
	chelec3.RandomVelocity=15.0
	chelec3.Time2Live=40
	rayog1.Active=1
	rayog2.Active=1
	sndrayo2.Play(16800.0, -38400.0, 67000.0, -1)
	sndrayo3.Play(16800.0, -38400.0, 71000.0, -1)
	luzob2.Intensity=0.2
	luzg1.Intensity=0.2
	luzg2.Intensity=0.2

def ElevaEspiralObelisco(ent_name, time):
	global chob
	global initespobdir
	global espob_step
	espob_step=espob_step+1
	v_ang=espob_step*ESPOB_ANGLE_VARIATION
	v_alt=espob_step*ESPOB_HEIGHT_VARIATION
	v_vel=espob_step*ESPOB_VEL_VARIATION
	v_rvel=espob_step*ESPOB_RVEL_VARIATION
	curr_dir=initespobdir[0]*math.cos(v_ang), 0.0, initespobdir[0]*math.sin(v_ang)
	chob.Position=18710.0, -33500.0-v_alt, 68980.0
	chob.Velocity=curr_dir[0]*(ESPOB_INIT_VEL-v_vel), 0.0, curr_dir[2]*(ESPOB_INIT_VEL-v_vel)
	chob.RandomVelocity=ESPOB_INIT_RVEL-v_rvel
	if espob_step==TOTAL_ESPOB_STEPS:
		chob.RemoveFromList("Timer60")
		chob.TimerFunc=""
		chob.DeathTime=Bladex.GetTime()+1.0/60.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, RayosObeliscoGargolas, ())

def EspiralObelisco():
	global chob
	AuxFuncs.MoveCamFromTo(15525.0, -39225.0, 65100.0, 11235.0, -35260.0, 66650.0, 19775.0, -32200.0, 70800.0, 20025.0, -39130.0, 69450.0, 9.0, AbrePuertas)
	orbe.Static=1
	orbe.Alpha=0.2
	lorbe=AuxFuncs.GetSpot(orbe)
	lorbe.Intensity=0.5
	lorbe.Color=255,180,96
	lorbe.SizeFactor=1.0
	orbe.Move(0,0,0)
	chob=Bladex.CreateEntity("EspiralChispasOb", "Entity Particle System D1", 18710.0, -33500.0, 68980.0) # sube hasta 18710.0, -37600.0, 68980.0)
	chob.ParticleType="ChispaObelisco"
	chob.YGravity=800.0
	chob.Friction=0.1
	chob.PPS=200
	chob.Velocity=-1.0*ESPOB_INIT_VEL, 0.0, 0.0
	chob.RandomVelocity=ESPOB_INIT_RVEL
	chob.Time2Live=60
	chob.TimerFunc=ElevaEspiralObelisco
	chob.SubscribeToList("Timer60")

def LanzaRayoObelisco():
	global chelec
	rayoob.Active=1
	sndrayo1.Play(18325.0, -32825.0, 69000.0, -1)
	chelec=Bladex.CreateEntity("ChispasElectricidadOb1", "Entity Particle System D1", 18325.0, -32825.0, 69000.0)
	chelec.ParticleType="ChispaElectrica"
	chelec.YGravity=800.0
	chelec.Friction=0.06
	chelec.PPS=80
	chelec.Velocity=-600.0, 0.0, 0.0
	chelec.RandomVelocity=10.0
	chelec.Time2Live=40
	luzob1.Intensity=0.2

def MueveOrbePedestal():
	global chorbe
	chorbe.RandomVelocity=-4.0
	if char.Kind=="Dwarf_N":
		v_despl=1010.0, 185.0, 0.0 #de (15800.0, -32800.0, 69000.0) a (16810.0, -32615.0, 69000.0)
	else:
		v_despl=1010.0, 485.0, 0.0 #de (15800.0, -33100.0, 69000.0) a (16810.0, -32615.0, 69000.0)
	v_mod=AuxFuncs.Module(v_despl)
	despl=(2.0*v_mod/3.0, v_mod/3.0)
	vect=(v_despl, v_despl)
	vel_inic=(0.0, 400.0)
	vel_fin=(400.0, 0.0)
	Objects.NDisplaceObject(orbedin, despl, vect, vel_inic, vel_fin, (), (), (), MueveChispasOrbe, (chorbe,), LanzaRayoObelisco, ())

def ReapareceOrbeGradual(ent_name, time):
	orbe.Alpha=orbe.Alpha+TRVAR
	orbe.Scale=orbe.Scale+SCLVAR
	lorbe.Intensity=lorbe.Intensity+INTVAR
	lorbe.SizeFactor=lorbe.SizeFactor+SIZEVAR
	if orbe.Alpha>=0.2:
		orbe.RemoveFromList("Timer60")
		orbe.TimerFunc=""
		orbe.Alpha=0.2
		orbe.Scale=1.0
		lorbe.Intensity=0.5
		lorbe.SizeFactor=1.0
		MueveOrbePedestal()

def ReapareceOrbe():
	orbe.TimerFunc=ReapareceOrbeGradual
	orbe.SubscribeToList("Timer60")

def ConcentraEnergiaOrbe():
	global chorbe
	inv=char.GetInventory()
	inv.RemoveObject("Orbe")
	if char.Kind=="Dwarf_N":
		orbe.Position=15800.0, -32800.0, 69000.0
	else:
		orbe.Position=15800.0, -33100.0, 69000.0
	chorbe=Bladex.CreateEntity("ChispasOrbe", "Entity Particle System D1", 0.0, 0.0, 0.0)
	chorbe.Position=orbe.Position
	chorbe.ParticleType="ChispaOrbe"
	chorbe.YGravity=0.0
	chorbe.Friction=0.0
	chorbe.PPS=50
	chorbe.Velocity=0.0, 0.0, 0.0
	chorbe.RandomVelocity=-6.0
	chorbe.Time2Live=60
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ReapareceOrbe, ())

def UsaPedestal():
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("use_magic_key")
	char.Position=15250.0, -33000.0, 69000.0
	char.Angle=-3.14159/2.0
	char.SetOnFloor()
	Bladex.SetListenerPosition(2)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("usaorbe"))
	AuxFuncs.MoveCamFromTo(19775.0, -36600.0, 72900.0, 15750.0, -32250.0, 71500.0, char.Position[0], char.Position[1], char.Position[2], soporbe.Position[0]+1000.0, soporbe.Position[1]-1000.0, soporbe.Position[2], 12.0, EspiralObelisco)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ConcentraEnergiaOrbe, ())

def GuardaArmas(person):
	alfa=AuxFuncs.Pos2PosXZAngle(char.Position, soporbe.Position)
	char.QuickFace(alfa)
	Actions.FreeBothHands("Player1")
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, UsaPedestal, ())

def SituaPersonajePedestal(obj_name, use_from):
	inv=char.GetInventory()
	for n in range (inv.nObjects):
		item_name=inv.GetObject(n)
		if item_name=="Orbe":
			Scorer.SetVisible(0)
			ScriptSkip.SkipScriptStart("EscenaDejaOrbe")
			#Bladex.DeactivateInput()
			char.GoTo(15250.0, -32500.0, 69000.0)
			char.RouteEndedFunc=GuardaArmas
			ene=Bladex.GetEntity("OrlokOrcoTejadoNorte")
			if ene and ene.Life>0:
				ene.Blind=1
				ene.Deaf=1
			break




################################
###     Funcionamiento orbe
################################

def DesapareceOrbeGradual(ent_name, time):
	orbe.Alpha=orbe.Alpha-TRVAR
	orbe.Scale=max(0.01, orbe.Scale-SCLVAR)
	lorbe.Intensity=lorbe.Intensity-INTVAR
	lorbe.SizeFactor=lorbe.SizeFactor-SIZEVAR
	if orbe.Alpha<=0:
		orbe.RemoveFromList("Timer60")
		orbe.TimerFunc=""
		orbe.Alpha=0.0
		orbe.Scale=0.01
		lorbe.Intensity=0.0
		lorbe.SizeFactor=0.0

def LanzaEstelaChispas(ent_name, time):
	global estela
	global init_est_time
	global vdespl
	curr_est_time=time-init_est_time
	frac_var=curr_est_time/ESTTIME
	estela.Position=orbe.Position[0]+vdespl[0]*frac_var, orbe.Position[1]+vdespl[1]*frac_var, orbe.Position[2]+vdespl[2]*frac_var
	if curr_est_time>=ESTTIME:
		estela.RemoveFromList("Timer60")
		estela.TimerFunc=""
		estela.PPS=200
		estela.RandomVelocity=40
		estela.DeathTime=Bladex.GetTime()+0.5
		Actions.TakeObject("Player1", "Orbe")

def DesapareceOrbe():
	global estela
	global init_est_time
	global vdespl
	chorbe.DeathTime=Bladex.GetTime()+0.25
	estela=Bladex.CreateEntity("EstelaChispas", "Entity Particle System D1", 0.0, 0.0, 0.0)
	estela.Position=orbe.Position
	estela.ParticleType="ChispaOrbe"
	estela.YGravity=200
	estela.Friction=0.2
	estela.PPS=100
	estela.Velocity=0.0, 0.0, 0.0
	estela.RandomVelocity=10
	estela.Time2Live=60
	init_est_time=Bladex.GetTime()
	vdespl=char.Position[0]-orbe.Position[0], char.Position[1]-orbe.Position[1], char.Position[2]+150.0-orbe.Position[2]
	estela.TimerFunc=LanzaEstelaChispas
	estela.SubscribeToList("Timer60")
	orbe.TimerFunc=DesapareceOrbeGradual
	orbe.SubscribeToList("Timer60")

def ElevaOrbe():
	if char.Kind=="Dwarf_N":
		despl=(300.0, 500.0, 300.0, 320.0, 320.0)
		vect=((0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, 5.0, 1.0), (0.0, 5.0, 1.0))
		vel_inic=(0.0, 550.0, 550.0, 0.0, 350.0)
		vel_fin=(550.0, 550.0, 0.0, 350.0, 0.0)
	elif char.Kind=="Barbarian_N":
		despl=(300.0, 500.0, 300.0, 110.0, 110.0)
		vect=((0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, 1.5, 1.0), (0.0, 1.5, 1.0))
		vel_inic=(0.0, 600.0, 600.0, 0.0, 110.0)
		vel_fin=(600.0, 600.0, 0.0, 110.0, 0.0)
	else:
		despl=(300.0, 500.0, 300.0, 200.0, 200.0)
		vect=((0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, -4.0, 1.0), (0.0, 3.0, 1.0), (0.0, 3.0, 1.0))
		vel_inic=(0.0, 600.0, 600.0, 0.0, 200.0)
		vel_fin=(600.0, 600.0, 0.0, 200.0, 0.0)
	Objects.NDisplaceObject(orbedin, despl, vect, vel_inic, vel_fin, (), (), (), MueveChispasOrbe, (chorbe,), Bladex.AddScheduledFunc, (Bladex.GetTime()+0.1, DesapareceOrbe, ()))

def CogeOrbe():
	Scorer.SetVisible(0)
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("tke_orb")
	char.Position=43500, -41900, 62900
	char.Angle=3.14159
	char.SetOnFloor()
	Bladex.SetListenerPosition(2)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("cogeorbe"))
	AuxFuncs.MoveCamFromTo(40250.0, -41400.0, 64300.0, 40200.0, -43350.0, 61050.0, 48150.0, -42500.0, 58250.0, 49000.0, -39600.0, 64050.0, 13.0, ReseteaCamaraOrbe)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, ElevaOrbe, ())

def SituaPersonajeOrbe():
	global orbeflotando
	orbeflotando=0
	Bladex.RemoveTriggerSectorFunc("ZonaOrbe", "OnEnter")
	Bladex.RemoveTriggerSectorFunc("ZonaOrbe", "OnLeave")
	ScriptSkip.SkipScriptStart("EscenaCogeOrbe")
	#Bladex.DeactivateInput()
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, CogeOrbe, ())




#################################################################################################
## SpKey.py


#################################
###     Funcionamiento llave
#################################

def ReseteaCamaraLlave():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)

def MueveChispasLlave():
	luzllave.Position=chllave.Position=llaveazul.Position

def AbrePuertaFort():
	despl=(140.0, 650.0)
	vect=(ejey, ejey)
	vel_inic=(0.0, 131.3)
	vel_fin=(131.3, 131.3)
	Objects.NDisplaceObject(coldin, despl, vect, vel_inic, vel_fin)
	agujero.OpenDoor()
	hoja1.OpenDoor()
	hoja2.OpenDoor()
	puerta1.CloseDoor()
	puerta2.CloseDoor()
	puerta3.CloseDoor()
	puerta4.CloseDoor()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, AuxFuncs.MoveCamFromTo, (27000.0, -34700.0, 65900.0, 27000.0, -34700.0, 65900.0, 25000.0, -32500.0, 68975.0, 23000.0, -32500.0, 76500.0, 5.25))
	Bladex.AddScheduledFunc(Bladex.GetTime()+9.0, ReseteaCamaraLlave, ())

def DesapareceLlaveGradual(ent_name, time):
	llaveazul.Alpha=llaveazul.Alpha-KEYTRVAR
	luzllave.Intensity=luzllave.Intensity-KEYINTVAR
	luzllave.SizeFactor=luzllave.SizeFactor-KEYSIZEVAR
	if llaveazul.Alpha<=0:
		llaveazul.RemoveFromList("Timer60")
		llaveazul.TimerFunc=""
		llaveazul.Alpha=0.0
		luzllave.Intensity=0.0
		luzllave.SizeFactor=0.0

def LanzaEstelaChispasLlave(ent_name, time):
	global estela
	global init_est_time
	global vdespl
	curr_est_time=time-init_est_time
	frac_var=curr_est_time/KEYESTTIME
	estela.Position=llaveazul.Position[0]+vdespl[0]*frac_var, llaveazul.Position[1]+vdespl[1]*frac_var, llaveazul.Position[2]+vdespl[2]*frac_var
	if curr_est_time>=KEYESTTIME:
		estela.RemoveFromList("Timer60")
		estela.TimerFunc=""
		estela.PPS=200
		estela.RandomVelocity=40
		estela.DeathTime=Bladex.GetTime()+0.5
		llaveazul.RemoveFromWorld()
		luzllave.RemoveFromWorld()
		Actions.TakeObject("Player1", "SHELL")

def DesapareceLlave():
	global estela
	global init_est_time
	global vdespl
	chllave.DeathTime=Bladex.GetTime()+0.25
	estela=Bladex.CreateEntity("EstelaChispasLlave", "Entity Particle System D1", 0.0, 0.0, 0.0)
	estela.Position=llaveazul.Position
	estela.ParticleType="ChispaLlave"
	estela.YGravity=200
	estela.Friction=0.2
	estela.PPS=100
	estela.Velocity=0.0, 0.0, 0.0
	estela.RandomVelocity=10
	estela.Time2Live=60
	init_est_time=Bladex.GetTime()
	vdespl=char.Position[0]-llaveazul.Position[0], char.Position[1]-llaveazul.Position[1], char.Position[2]-llaveazul.Position[2]
	estela.TimerFunc=LanzaEstelaChispasLlave
	estela.SubscribeToList("Timer60")
	llaveazul.TimerFunc=DesapareceLlaveGradual
	llaveazul.SubscribeToList("Timer60")

def ElevaLlave():
	if char.Kind=="Dwarf_N":
		despl=(150.0, 300.0, 200.0)
		vel_inic=(0.0, 150.0, 150.0)
		vel_fin=(150.0, 150.0, 0.0)
	elif char.Kind=="Barbarian_N":
		despl=(150.0, 840.0, 250.0)
		vel_inic=(0.0, 250.0, 250.0)
		vel_fin=(250.0, 250.0, 0.0)
	else:
		despl=(150.0, 400.0, 250.0)
		vel_inic=(0.0, 200.0, 200.0)
		vel_fin=(200.0, 200.0, 0.0)
	vect=(ejeyn, ejeyn, ejeyn)
	Objects.NDisplaceObject(llaveazuldin, despl, vect, vel_inic, vel_fin, (), (), (), MueveChispasLlave, (), Bladex.AddScheduledFunc, (Bladex.GetTime()+6.5, DesapareceLlave, ()))

def CogeLlave():
	Scorer.SetVisible(0)
	v=char.Position[0]-col.Position[0], 0.0, char.Position[2]-col.Position[2]
	v1=AuxFuncs.Normalize(v)
	v2=v1[0]*math.cos(1.5)-v1[2]*math.sin(1.5), 0.0, v1[0]*math.sin(1.5)+v1[2]*math.cos(1.5)
	objpos1=col.Position[0]-v1[0]*2500.0, -34500.0, col.Position[2]-v1[2]*2500.0
	objpos2=col.Position[0]-v2[0]*2500.0, -32250.0, col.Position[2]-v2[2]*2500.0
	trgpos=col.Position[0]+v1[0]*300.0, -33200.0, col.Position[2]+v1[2]*300.0
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("tke_key_orlok")
	char.Position=col.Position[0]+v1[0]*1200.0, -33164.0, col.Position[2]+v1[2]*1200.0
	char.SetOnFloor()
	Bladex.SetListenerPosition(2)
	AuxFuncs.MoveCamFromTo(objpos1[0], objpos1[1], objpos1[2], objpos2[0], objpos2[1], objpos2[2], trgpos[0], trgpos[1], trgpos[2], trgpos[0], trgpos[1], trgpos[2], 15.0, AbrePuertaFort) # 13.0, AbrePuertaFort)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ElevaLlave, ())
	GameText.WriteText("M10T2")

def SituaPersonajeLlave():
	if char.Position[1]>-33600.0:
		Bladex.RemoveScheduledFunc("ApagaMusicaEncuentraLlave")
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musica_llave"))
		ScriptSkip.SkipScriptStart("EscenaCogeLlave")
		#Bladex.DeactivateInput()
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CogeLlave, ())

def repite():
	global chllave
	llaveazul.Position=25000.0, -32950.0, 69000.0
	luzllave.Position=llaveazul.Position
	chllave=Bladex.CreateEntity("ChispasLlave", "Entity Particle System D1", 0.0, 0.0, 0.0)
	chllave.Position=llaveazul.Position
	chllave.ParticleType="ChispaLlave"
	chllave.YGravity=0.0
	chllave.Friction=0.0
	chllave.PPS=50
	chllave.Velocity=0.0, 0.0, 0.0
	chllave.RandomVelocity=-4.0
	chllave.Time2Live=60
	llaveazul.Alpha=1.0
	luzllave.Intensity=0.4
	luzllave.SizeFactor=1.0
	hoja1.CloseDoor()
	hoja2.CloseDoor()
	agujero.CloseDoor()
	col.Move(0,-790,0)




#################################################################################################
## Final.py


def FinYCargaSiguienteMapa():
	ScriptSkip.SkipScriptEnd()
	GotoMapVars.EndOfLevel()

def ContinuaFinal():
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicafinal"))
	AuxFuncs.MoveCamFromTo(39100.0, -46425.0, 174050.0, 32150.0, -32480.0, 157080.0, 35450.0, -40400.0, 167950.0, 33200.0, -34125.0, 162675.0, 8.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+6.0, AuxFuncs.FadeTo, (2.0, 4.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, char.GoTo, (33250.0, -33000.0, 179000.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+10.0, Bladex.ExeMusicEvent, (-1,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+11.0, FinYCargaSiguienteMapa, ())

def LimpiaManos():
	Actions.FreeBothHands("Player1")
	Actions.FreeBothHands("Player1")
	# Lo hago dos veces por si acaso esta encarado

def LanzaFinal(tr_sector, ent_name):
	ScriptSkip.SkipScriptStart("EscenaFinal")
	#Bladex.DeactivateInput()
	Bladex.RemoveTriggerSectorFunc("Final", "OnEnter")
	lookat=33250.0, -33000.0, 165250.0
	alfa=AuxFuncs.Pos2PosXZAngle(char.Position, lookat)
	char.QuickFace(alfa)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, LimpiaManos, ())
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ContinuaFinal, ())

def repfin():
	Bladex.SetTriggerSectorFunc("Final", "OnEnter", LanzaFinal)
	Bladex.ActivateInput()
	char.Position=33250, -33250, 156250
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)




#################################################################################################
## Golem.py


### Funcionamiento

def CierraPorton(sec_index, ent_name):
	if ent_name=="Player1":
		sectorcierraporton.OnEnter=""
		hoja1.CloseDoor()
		hoja2.CloseDoor()

def NieveTroncos():
	nieve1=Bladex.CreateEntity("NieveTronco1", "Entity Particle System D1", 42800.0,-32050.0,92200.0)
	nieve1.ParticleType="PolvoNieve"
	nieve1.PPS=32
	nieve1.YGravity=200.0
	nieve1.Friction=0.1
	nieve1.RandomVelocity=15.0
	nieve1.Time2Live=64
	nieve1.DeathTime=Bladex.GetTime()+4.5
	nieve2=Bladex.CreateEntity("NieveTronco1", "Entity Particle System D1", 43575.0,-32050.0,91732.0)
	nieve2.ParticleType="PolvoNieve"
	nieve2.PPS=32
	nieve2.YGravity=200.0
	nieve2.Friction=0.1
	nieve2.RandomVelocity=15.0
	nieve2.Time2Live=64
	nieve2.DeathTime=Bladex.GetTime()+4.5
	nieve3=Bladex.CreateEntity("NieveTronco1", "Entity Particle System D1", 44245.0,-32050.0,91109.0)
	nieve3.ParticleType="PolvoNieve"
	nieve3.PPS=32
	nieve3.YGravity=200.0
	nieve3.Friction=0.1
	nieve3.RandomVelocity=15.0
	nieve3.Time2Live=64
	nieve3.DeathTime=Bladex.GetTime()+4.5
	nieve4=Bladex.CreateEntity("NieveTronco1", "Entity Particle System D1", 44997.0,-32050.0,90563.0)
	nieve4.ParticleType="PolvoNieve"
	nieve4.PPS=32
	nieve4.YGravity=200.0
	nieve4.Friction=0.1
	nieve4.RandomVelocity=15.0
	nieve4.Time2Live=64
	nieve4.DeathTime=Bladex.GetTime()+4.5

def BajaTroncos(person):
	Bladex.ExeMusicEvent(-1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaexterior"))
	despl=(250.0, 3000.0)
	vect=(ejey, ejey)
	vel_inic=(0.0, 600.0)
	vel_fin=(600.0, 600.0)
	Objects.NDisplaceObject(ptronco1din, despl, vect, vel_inic, vel_fin, (), (desliztronco1, desliztronco1))
	Objects.NDisplaceObject(ptronco2din, despl, vect, vel_inic, vel_fin, ()) # , (desliztronco2, desliztronco2))
	Objects.NDisplaceObject(ptronco3din, despl, vect, vel_inic, vel_fin, ()) # , (desliztronco3, desliztronco3))
	Objects.NDisplaceObject(ptronco4din, despl, vect, vel_inic, vel_fin, (), (desliztronco4, desliztronco4))
	enm=Bladex.GetEntity(person)
	enm.Data.OldDeadFunc(person)
	NieveTroncos()
	Bladex.SetTriggerSectorFunc("DesfiladeroPost",   "OnEnter", EnciendeMusicaDesfiladero)
	Bladex.SetTriggerSectorFunc("Fortificacion2",    "OnEnter", EnciendeMusicaFortificacion)


def SaltaNieve3GenGolem(ps):
	x, y, z = ps.Position
	ps.Position=x, y, z+600.0
	ps.D1=2400.0, 0.0, 0.0
	ps.D2=1200.0, 0.0, 2400.0
	ps.PPS=100

def SaltaNieve2GenGolem(ps):
	ps.D2=750.0, 0.0, 1500.0
	ps.PPS=800

def SaltaNieveGenGolem(gen_pos):
	saltanie=Bladex.CreateEntity("NieveSaltando", "Entity Particle System D3", gen_pos[0]-600.0, gen_pos[1]-900.0, gen_pos[2]-300.0)
	saltanie.D1=1500.0, 0.0, 0.0
	saltanie.D2=750.0, 0.0, -1500.0
	saltanie.ParticleType="Nievecilla"
	saltanie.PPS=600
	saltanie.YGravity=500.0
	saltanie.Friction=0.05
	saltanie.Velocity=0.0, -10.0, 0.0
	saltanie.RandomVelocity=10.0
	saltanie.RandomVelocity_V=10.0
	saltanie.Time2Live=60
	saltanie.DeathTime=Bladex.GetTime()+3.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, SaltaNieve2GenGolem, (saltanie,))
	saltani2=Bladex.CreateEntity("NieveSaltando2", "Entity Particle System D3", gen_pos[0]-1200.0, gen_pos[1]-900.0, gen_pos[2]-1200.0)
	saltani2.D1=2400.0, 0.0, 0.0
	saltani2.D2=1200.0, 0.0, 2400.0
	saltani2.ParticleType="PolvoNieve"
	saltani2.PPS=200
	saltani2.YGravity=200.0
	saltani2.Friction=0.1
	saltani2.Velocity=0.0, -20.0, 0.0
	saltani2.RandomVelocity=10.0
	saltani2.Time2Live=32
	saltani2.DeathTime=Bladex.GetTime()+5.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, SaltaNieve3GenGolem, (saltani2,))





def ParaCamaraGolem(camera, frame):
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.ExeMusicEvent(-1)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("combategolem"))

def GolemListo(person):
	golem.Blind=0
	golem.Deaf=0

def LevantaGolem():
	golem.UnFreeze()
	golem.SetTmpAnmFlags(1,1,1,0,5,1,0)
	golem.LaunchAnmType("raise_snow")
	golem.Position=25000.0, -31300.0, 85500.0
	golem.Angle=3.14159
	golem.AnmEndedFunc=GolemListo
	SaltaNieveGenGolem(golem.Position)	# en el Generadores.py
	GeneradorGlm.Play(golem.Position[0], golem.Position[1], golem.Position[2], 0)

def AparicionGolem(tr_sector, ent_name):
	Bladex.RemoveTriggerSectorFunc(tr_sector, "OnEnter")
	Scorer.SetVisible(0)
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaapgolem"))
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("aparicion_golem.cam",0,180)
	cam.AddCameraEvent(-1, ParaCamaraGolem)
	ScriptSkip.SkipScriptStart("EscenaGolem")
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, LevantaGolem, ())

def repgolem():
	Bladex.SetTriggerSectorFunc("SalidaFort", "OnEnter", AparicionGolem)

def RG1():
	golem.UnFreeze()
	golem.SetTmpAnmFlags(1,1,1,0,5,1,0)
	golem.LaunchAnmType("raise_snow")
	golem.Position=25000.0, -31300.0, 85500.0
	golem.Angle=3.14159
	golem.AnmEndedFunc=GolemListo
	SaltaNieveGenGolem(golem.Position)	# en el Generadores.py

def RG2():
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera("aparicion_golem.cam",0,180)
	cam.AddCameraEvent(-1, ParaCamaraGolem)
	Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, RG1, ())




#################################################################################################
## Enemigos.py


def CambiaArqueroSurFortaleza(sec_index, ent_name):
	if ent_name=="Player1":
		entradasecreta.OnEnter=""
		arquero=Bladex.GetEntity("OrlokOrcoTejadoSur")
		if arquero and arquero.Life>0:
			arquero.Position=18807, -45673, 63656
			arquero.Angle=0.0
			arquero.SetOnFloor()

def CambiaArqueroNorteFortaleza(sec_index, ent_name):
	if ent_name=="Player1":
		salidafortaleza.OnEnter=""
		arquero=Bladex.GetEntity("OrlokOrcoTejadoNorte")
		if arquero and arquero.Life>0:
			arquero.Position=31129, -45889, 76986
			arquero.Angle=0.0
			arquero.SetOnFloor()






#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************							**************************
#*******************************	Definiciones para Musica.py		**************************
#*******************************							**************************
#*************************************************************************************************
#*************************************************************************************************


def ApagaMusicaAlEntrar(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("emptyloquesea"))

def EnciendeMusicaValles(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicavalles"))

def EnciendeMusicaDesfiladero(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicaexterior"))

def EnciendeMusicaCuevas(trsector_name, entity_name):
	global cuevasvisitadas
	if entity_name=="Player1":
		if not cuevasvisitadas:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("accesocuevas"))
			cuevasvisitadas=1
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicacuevas"))

def EnciendeMusicaFortificacion(trsector_name, entity_name):
	global fortificacionvisitada
	if entity_name=="Player1":
		if not fortificacionvisitada:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("accesofortific"))
			fortificacionvisitada=1
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicafortific"))

def EnciendeMusicaEncuentraLLave(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("encuentrallave"))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, Bladex.ExeMusicEvent, (-1,), "ApagaMusicaEncuentraLlave")
		Bladex.RemoveTriggerSectorFunc("EncuentraLlave", "OnEnter")

def EnciendeMusicaEncuentraOrbe(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("encuentraorbe"))
		Bladex.RemoveTriggerSectorFunc("EncuentraOrbe", "OnEnter")

def EnciendeMusicaSustoDKN(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.KillMusic()
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("musicafortific"))
		Bladex.RemoveTriggerSectorFunc("SustoDKN", "OnEnter")
		Bladex.RemoveTriggerSectorFunc("DesactivaSusto", "OnEnter")
		pers=Bladex.GetEntity("OrlokDknPiso")
		if pers and pers.Life>0:
			pers.Blind=0
			pers.Deaf=0

def DesactivaEncendidoMusicaSustoDKN(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.RemoveTriggerSectorFunc("Susto", "OnEnter")
		Bladex.RemoveTriggerSectorFunc("DesactivaSustoDKN", "OnEnter")
		pers=Bladex.GetEntity("OrlokDknPiso")
		if pers and pers.Life>0:
			pers.Blind=0
			pers.Deaf=0
