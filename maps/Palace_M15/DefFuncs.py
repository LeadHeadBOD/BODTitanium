##///
##||| PALACE_M15/DefFuncs.PY TITANIUM
##||| Change list:
##||| * Orcs in the invasion cutscene will now use weapons and meshes of real orcs
##||| * 
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 

import def_class
import Bladex
import ReadGSFile
import Enm_Gen
import B3DLib
import Traps_C
import GameText
import AuxFuncs
import Scorer
import Sounds
import EnmGenRnd
import ReadGSFile
import Actions
import Reference
import Sounds
import stone
import heavyObjects
import Room
import Button
import ScriptSkip
import GotoMapVars
import GenFX
import Sparks




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Positions.py       **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def IrPosicion1():
	AgregaTablilla()

def IrPosicion2():
	char=Bladex.GetEntity("Player1")
	char.Position=-28000, -500, -2700		# Graneros

def IrPosicion3():
	char=Bladex.GetEntity("Player1")
	char.Position=54000, -300, 129000	# Vidrieras

def IrPosicion4():
	char=Bladex.GetEntity("Player1")
	char.Position=4500, 3800, 169000		# Tablillas

def IrPosicion5():
	char=Bladex.GetEntity("Player1")
	char.Position=94500, -3800, 239000		# Tablillas

def IrPosicion6():
	char=Bladex.GetEntity("Player1")
	char.Position=-74644.0, 147.0, 70190.0		# Llave 1

def IrPosicion7():
	char=Bladex.GetEntity("Player1")
	char.Position=23897.0, -5873.0, 73176.0		# Llave 2

def IrPosicion8():
	char=Bladex.GetEntity("Player1")
	char.Position=77272.0, 387.0, 132607.0		# Llave 3

def IrPosicion9():
	char=Bladex.GetEntity("Player1")
	char.Position=-45212.0, -3114.0, 174977.0		# Llave 4

def IrPosicionFinal():
	char=Bladex.GetEntity("Player1")
	char.Position=94342.0, -3046.0, 196364.0		# Final
	char.Angle=3.14159

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para rrollonB.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def essSceneBDustTri(name,a,b,c):
	doorDust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2])
 	doorDust.D1= b[0]-a[0], b[1]-a[1], b[2]-a[2]
 	doorDust.D2= c[0]-a[0], c[1]-a[1], c[2]-a[2]
	doorDust.ParticleType="essSceneDust"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=2412
	doorDust.Velocity=0.0, 5000.0, -8000.0
	doorDust.RandomVelocity=10.0
	doorDust.Time2Live=20
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0

def essSceneBDustTriB(name,a,b,c):
	doorDust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2])
 	doorDust.D1= b[0]-a[0], b[1]-a[1], b[2]-a[2]
 	doorDust.D2= c[0]-a[0], c[1]-a[1], c[2]-a[2]
	doorDust.ParticleType="essSceneDust"
	doorDust.YGravity=0.0
	doorDust.Friction=0.2
	doorDust.PPS=1000
	doorDust.Velocity=0.0, -300.0, -800.0
	doorDust.RandomVelocity=40.0
	doorDust.Time2Live=30
	doorDust.DeathTime=Bladex.GetTime()+6.0/60.0

def essBreakDoorDustB() :
	a = -25637.5613209, -1001, 145961.115169
	b = -22970.9361089, -1001, 146048.37688
	c = -22713.562409 , -1001, 152298.68074
	d = -26033.562409 , -1001, 152298.68074
	essSceneBDustTriB ("essSceneDust3",a,b,d)
	essSceneBDustTriB ("essSceneDust4",b,d,c)

def essBreakDoorDust() :
	a = -26033.562409, -4434.6, 152298.68074
	b = -23373.562409, -4134.6, 152298.68074
	c = -22713.562409, -1234.6, 152298.68074
	d = -26033.562409, -1034.6, 152298.68074
	essSceneBDustTri ("essSceneDust1",a,b,d)
	essSceneBDustTri ("essSceneDust2",b,d,c)

def essBreakDoor() :
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.1, essBreakDoorDust, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+0.7, essBreakDoorDustB, () )
	essDoor.DoBreak((0, 0, -5.8), (-25033.562409, -2034.6, 152298.68074), (0.0, 0.0, 0.0))
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("estampidaorcos"))
	darfuncs.EnterSecEvent(-24358.3619395, -2105.52315802, 149607.745315,Atacaminorx)

def essSceneBCreateX():
	orkB_n = Bladex.GetEntity("01ORC")
	orkBA_K = orkB_n.Kind ; orkBA_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBA_L = Bladex.GetEntity(orkB_n.InvLeft).Kind
	
	orkB_n = Bladex.GetEntity("02ORC")
	orkBB_K = orkB_n.Kind ; orkBB_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBB_L = Bladex.GetEntity(orkB_n.InvLeft).Kind
	
	orkB_n = Bladex.GetEntity("PalaceArq1")
	orkBC_K = orkB_n.Kind ; orkBC_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBC_L = Bladex.GetEntity(orkB_n.InvLeft).Kind

	orkB_n = Bladex.GetEntity("3ORC")
	orkBD_K = orkB_n.Kind ; orkBD_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBD_L = Bladex.GetEntity(orkB_n.InvLeft).Kind
	
	orkB_n = Bladex.GetEntity("2ORC")
	orkBE_K = orkB_n.Kind ; orkBE_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBE_L = Bladex.GetEntity(orkB_n.InvLeft).Kind
	
	orkB_n = Bladex.GetEntity("5ORC")
	orkBF_K = orkB_n.Kind ; orkBF_R = Bladex.GetEntity(orkB_n.InvRight).Kind ; orkBF_L = Bladex.GetEntity(orkB_n.InvLeft).Kind
	
	essOrkB_A=Bladex.CreateEntity( "essOrk_B_A", orkBA_K		, -23392.016 ,  -1953.069, 153216.797  )
	essOrkB_B=Bladex.CreateEntity( "essOrk_B_B", orkBB_K	, -25309.123 ,  -1956.263, 154473.672  )
	essOrkB_C=Bladex.CreateEntity( "essOrk_B_C", orkBC_K	, -24701.467 ,  -1284.725, 155565.922  )
	essOrkB_D=Bladex.CreateEntity( "essOrk_B_D", orkBD_K		, -23356.531 ,  -1668.392, 155305.594  )
	essOrkB_E=Bladex.CreateEntity( "essOrk_B_E", orkBE_K	, -32007.924 , -2053.556, 107844.641  )
	essOrkB_F=Bladex.CreateEntity( "essOrk_B_F", orkBF_K	, -21189.088 , -2053.556, 107272.547  )
	essOrkB_A.Person=1; essOrkB_A.Angle=3.14
	essOrkB_B.Person=1; essOrkB_B.Angle=3.14
	essOrkB_C.Person=1; essOrkB_C.Angle=3.14
	essOrkB_D.Person=1; essOrkB_D.Angle=3.14
	essOrkB_E.Person=1; essOrkB_E.Angle=3.14
	essOrkB_F.Person=1; essOrkB_F.Angle=3.14
	essOrkB_Asw=Bladex.CreateEntity( "essOrk_B_Asw",orkBA_R, 0,0,0 ) ; essOrkB_Ash=Bladex.CreateEntity( "essOrk_B_Ash",orkBA_L, 0,0,0 ) ;
	essOrkB_Bsw=Bladex.CreateEntity( "essOrk_B_Bsw",orkBB_R, 0,0,0 ) ; essOrkB_Bsh=Bladex.CreateEntity( "essOrk_B_Bsh",orkBB_L, 0,0,0 ) ;
	essOrkB_Csw=Bladex.CreateEntity( "essOrk_B_Csw","Arco2",  0,0,0) ; essOrkB_Csh=Bladex.CreateEntity( "essOrk_B_Csh","Flecha", 0,0,0) ;
	essOrkB_Dsw=Bladex.CreateEntity( "essOrk_B_Dsw",orkBD_R, 0,0,0 ) ; essOrkB_Dsh=Bladex.CreateEntity( "essOrk_B_Dsh",orkBD_L, 0,0,0 ) ;
	essOrkB_Esw=Bladex.CreateEntity( "essOrk_B_Esw",orkBE_R, 0,0,0 ) ; essOrkB_Esh=Bladex.CreateEntity( "essOrk_B_Esh",orkBE_L, 0,0,0 ) ;
	essOrkB_Fsw=Bladex.CreateEntity( "essOrk_B_Fsw",orkBF_R, 0,0,0 ) ; essOrkB_Fsh=Bladex.CreateEntity( "essOrk_B_Fsh",orkBF_L, 0,0,0 ) ;
	Actions.TakeObject(essOrkB_A.Name,"essOrk_B_Ash") ; Actions.TakeObject(essOrkB_A.Name,"essOrk_B_Asw")
	Actions.TakeObject(essOrkB_B.Name,"essOrk_B_Bsh") ; Actions.TakeObject(essOrkB_B.Name,"essOrk_B_Bsw")
	essOrkB_C.GetInventory().LinkRightHand("essOrk_B_Csh") ;essOrkB_C.GetInventory().LinkLeftHand("essOrk_B_Csw")
	Actions.TakeObject(essOrkB_D.Name,"essOrk_B_Dsh") ; Actions.TakeObject(essOrkB_D.Name,"essOrk_B_Dsw")
	Actions.TakeObject(essOrkB_E.Name,"essOrk_B_Esh") ; Actions.TakeObject(essOrkB_E.Name,"essOrk_B_Esw")
	Actions.TakeObject(essOrkB_F.Name,"essOrk_B_Fsh") ; Actions.TakeObject(essOrkB_F.Name,"essOrk_B_Fsw")

	darfuncs.HideBadGuy( "essOrk_B_A")
	darfuncs.HideBadGuy( "essOrk_B_B")
	darfuncs.HideBadGuy( "essOrk_B_C")
	darfuncs.HideBadGuy( "essOrk_B_D")
	darfuncs.HideBadGuy( "essOrk_B_E")
	darfuncs.HideBadGuy( "essOrk_B_F")

def essSceneBCreate():
	darfuncs.UnhideBadGuy( "essOrk_B_A")
	darfuncs.UnhideBadGuy( "essOrk_B_B")
	darfuncs.UnhideBadGuy( "essOrk_B_C")
	darfuncs.UnhideBadGuy( "essOrk_B_D")
	darfuncs.UnhideBadGuy( "essOrk_B_E")
	darfuncs.UnhideBadGuy( "essOrk_B_F")

def essSceneBDestroy():
	essOrkB_A=Bladex.GetEntity( "essOrk_B_A")
	essOrkB_B=Bladex.GetEntity( "essOrk_B_B")
	essOrkB_C=Bladex.GetEntity( "essOrk_B_C")
	essOrkB_D=Bladex.GetEntity( "essOrk_B_D")
	essOrkB_E=Bladex.GetEntity( "essOrk_B_E")
	essOrkB_F=Bladex.GetEntity( "essOrk_B_F")
	essOrkB_A.SubscribeToList("Pin") ; essOrkB_A.RemoveFromWorld()
	essOrkB_B.SubscribeToList("Pin") ; essOrkB_B.RemoveFromWorld()
	essOrkB_C.SubscribeToList("Pin") ; essOrkB_C.RemoveFromWorld()
	essOrkB_D.SubscribeToList("Pin") ; essOrkB_D.RemoveFromWorld()
	essOrkB_E.SubscribeToList("Pin") ; essOrkB_E.RemoveFromWorld()
	essOrkB_F.SubscribeToList("Pin") ; essOrkB_F.RemoveFromWorld()

def essSceneBAnimParche() :
	essOrkB_E=Bladex.GetEntity( "essOrk_B_E")
	essOrkB_F=Bladex.GetEntity( "essOrk_B_F")
	essOrkB_E.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_E.LaunchAnimation("Ork_ejercito8")
	essOrkB_F.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_F.LaunchAnimation("Ork_ejercito8")

def essSceneBAnim() :
	essOrkB_A=Bladex.GetEntity( "essOrk_B_A")
	essOrkB_B=Bladex.GetEntity( "essOrk_B_B")
	essOrkB_C=Bladex.GetEntity( "essOrk_B_C")
	essOrkB_D=Bladex.GetEntity( "essOrk_B_D")
	# essOrkB_E=Bladex.GetEntity( "essOrk_B_E")
	# essOrkB_F=Bladex.GetEntity( "essOrk_B_F")
	essOrkB_A.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_A.LaunchAnimation("Ork_ejer1")
	essOrkB_B.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_B.LaunchAnimation("Ork_ejer2")
	essOrkB_C.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_C.LaunchAnimation("Ork_ejer_bow")
	essOrkB_D.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_D.LaunchAnimation("Gor_ejer3")
	#essOrkB_E.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_E.LaunchAnimation("Ork_ejer4")
	#essOrkB_F.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkB_F.LaunchAnimation("Ork_ejer5")
	Bladex.AddScheduledFunc( Bladex.GetTime()+17.3, essSceneBAnimParche, () )

def essSceneBCamReset(camera,frame) :
	essSceneBDestroy()
	essSceneALaunch()

def essSceneBFadeOut(ent,frame) :
	AuxFuncs.FadeTo(2.6, 0.0)

def essSceneBMiniFadeOut(ent,frame) :
	AuxFuncs.FadeTo(0.3, 0.0)

def essSceneBDMiniFadeOut(ent,frame) :
	AuxFuncs.FadeTo(2, 1.0)

def essSceneBCamD(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito2_Camera4.cam", 341 , 400 )
	cam.AddCameraEvent( 20 ,essSceneBDMiniFadeOut)
	cam.AddCameraEvent( -1,essSceneBCamReset)
	AuxFuncs.FadeFrom(0.4, 0.0)

def essSceneBCamC(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito2_Camera3.cam", 292 , 340 )
	cam.AddCameraEvent( 340 - (20.0*0.2),essSceneBMiniFadeOut)
	cam.AddCameraEvent( -1,essSceneBCamD)
	AuxFuncs.FadeFrom(0.4, 0.0)

def essSceneBCamB(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito2_Camera2.cam", 83 , 291 )
	cam.AddCameraEvent( 291 - (20.0*0.2),essSceneBMiniFadeOut)
	cam.AddCameraEvent( -1,essSceneBCamC)
	AuxFuncs.FadeFrom(0.4, 0.0)

def essSceneBCamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito2_Camera1.cam", 0 , 82+80 )
	cam.AddCameraEvent( 82+80 - (20.0*0.2),essSceneBMiniFadeOut)
	cam.AddCameraEvent( -1,essSceneBCamB)
	AuxFuncs.FadeFrom(0.4, 0.0)

def essSceneBLaunch(index, ent):
	if (ent<>"Player1") : return
	if (essSceneBLaunched) : return
	global essSceneBLaunched
	essSceneBLaunched=1

	essSceneBCreate()

	fadeTime = 0.0
	delay = 4.0

	Bladex.AddScheduledFunc( Bladex.GetTime()+fadeTime, essSceneBCamA, () )
	Bladex.AddScheduledFunc( Bladex.GetTime()+fadeTime+delay, essSceneBAnim, () )

	Bladex.AddScheduledFunc( Bladex.GetTime()+fadeTime+delay+0.2, essBreakDoor, () )


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para rrollonA.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def essSceneACreateX():
	
	orkA_n=Bladex.GetEntity("4ORC")
	orkAA_K = orkA_n.Kind ; orkAA_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAA_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("6ORC")
	orkAB_K = orkA_n.Kind ; orkAB_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAB_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("9ORC")
	orkAC_K = orkA_n.Kind ; orkAC_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAC_L = Bladex.GetEntity(orkA_n.InvLeft).Kind

	orkA_n=Bladex.GetEntity("10ORC")
	orkAD_K = orkA_n.Kind ; orkAD_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAD_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("PalaceArq10")	# PLAGUE: replace - spawns with bow
	orkAE_K = orkA_n.Kind ; orkAE_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAE_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("PalaceArq9")   # PLAGUE: replace - spawns with bow
	orkAF_K = orkA_n.Kind ; orkAF_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAF_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("PalaceArq2")
	orkAG_K = orkA_n.Kind ; orkAG_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAG_L = Bladex.GetEntity(orkA_n.InvLeft).Kind

	orkA_n=Bladex.GetEntity("11ORC")
	orkAH_K = orkA_n.Kind ; orkAH_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAH_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	orkA_n=Bladex.GetEntity("12ORC")
	orkAI_K = orkA_n.Kind ; orkAI_R = Bladex.GetEntity(orkA_n.InvRight).Kind ; orkAI_L = Bladex.GetEntity(orkA_n.InvLeft).Kind
	
	essOrkA_A=Bladex.CreateEntity( "essOrk__A_A",orkAA_K	,  79728.023 , 2407.449 , 37312.367 )
	essOrkA_B=Bladex.CreateEntity( "essOrk__A_B",orkAB_K		,  77420.219 , 2407.45  , 36685.434 )
	essOrkA_C=Bladex.CreateEntity( "essOrk__A_C",orkAC_K		,  77204.703 , 2411.432 , 36725.395 )
	essOrkA_D=Bladex.CreateEntity( "essOrk__A_D",orkAD_K		,  78226.961 , 2468.622 , 37222.082 )
	essOrkA_E=Bladex.CreateEntity( "essOrk__A_E",orkAE_K		,  77266.875 , 2392.445 , 39831.25  )
	essOrkA_F=Bladex.CreateEntity( "essOrk__A_F",orkAF_K		,  79941.445 , 2356.285 , 40694.676 )
	essOrkA_G=Bladex.CreateEntity( "essOrk__A_G",orkAG_K		,  78638.953 , 2392.445 , 42531.988 )
	essOrkA_H=Bladex.CreateEntity( "essOrk__A_H",orkAH_K	,  76806.891 , 2515.893 , 41689.875 )
	essOrkA_I=Bladex.CreateEntity( "essOrk__A_I",orkAI_K	,  69787.844 , 2356.285 , 42143.176 )
	essOrkA_A.Person=1; essOrkA_A.Angle=0
	essOrkA_B.Person=1; essOrkA_B.Angle=0
	essOrkA_C.Person=1; essOrkA_C.Angle=0
	essOrkA_D.Person=1; essOrkA_D.Angle=0
	essOrkA_E.Person=1; essOrkA_E.Angle=0
	essOrkA_F.Person=1; essOrkA_F.Angle=0
	essOrkA_G.Person=1; essOrkA_G.Angle=0
	essOrkA_H.Person=1; essOrkA_H.Angle=0
	essOrkA_I.Person=1; essOrkA_I.Angle = 3.14*1.5
	essOrkA_Asw=Bladex.CreateEntity( "essOrk__A_Asw",orkAA_R, 0,0,0 ) ; essOrkA_Ash=Bladex.CreateEntity( "essOrk__A_Ash",orkAA_L, 0,0,0 ) ;
	essOrkA_Bsw=Bladex.CreateEntity( "essOrk__A_Bsw",orkAB_R, 0,0,0 ) ; essOrkA_Bsh=Bladex.CreateEntity( "essOrk__A_Bsh",orkAB_L, 0,0,0 ) ;
	essOrkA_Csw=Bladex.CreateEntity( "essOrk__A_Csw",orkAC_R, 0,0,0 ) ; essOrkA_Csh=Bladex.CreateEntity( "essOrk__A_Csh",orkAC_L, 0,0,0 ) ;
	essOrkA_Dsw=Bladex.CreateEntity( "essOrk__A_Dsw",orkAD_R, 0,0,0 ) ; essOrkA_Dsh=Bladex.CreateEntity( "essOrk__A_Dsh",orkAD_L, 0,0,0 ) ;
	essOrkA_Esw=Bladex.CreateEntity( "essOrk__A_Esw",orkAE_R, 0,0,0 ) ; essOrkA_Esh=Bladex.CreateEntity( "essOrk__A_Esh",orkAE_L, 0,0,0 ) ;
	essOrkA_Fsw=Bladex.CreateEntity( "essOrk__A_Fsw",orkAF_R, 0,0,0 ) ; essOrkA_Fsh=Bladex.CreateEntity( "essOrk__A_Fsh",orkAF_L, 0,0,0 ) ;
	essOrkA_Gsw=Bladex.CreateEntity( "essOrk__A_Gsw",orkAG_R, 0,0,0 ) ; essOrkA_Gsh=Bladex.CreateEntity( "essOrk__A_Gsh",orkAG_L, 0,0,0 ) ;
	essOrkA_Hsw=Bladex.CreateEntity( "essOrk__A_Hsw",orkAH_R, 0,0,0 ) ; essOrkA_Hsh=Bladex.CreateEntity( "essOrk__A_Hsh",orkAH_L, 0,0,0 ) ;
	essOrkA_Isw=Bladex.CreateEntity( "essOrk__A_Isw",orkAI_R, 0,0,0 ) ; essOrkA_Ish=Bladex.CreateEntity( "essOrk__A_Ish",orkAI_L, 0,0,0 ) ;
	Actions.TakeObject(essOrkA_A.Name,"essOrk__A_Ash") ; Actions.TakeObject(essOrkA_A.Name,"essOrk__A_Asw")
	Actions.TakeObject(essOrkA_B.Name,"essOrk__A_Bsh") ; Actions.TakeObject(essOrkA_B.Name,"essOrk__A_Bsw")
	Actions.TakeObject(essOrkA_C.Name,"essOrk__A_Csh") ; Actions.TakeObject(essOrkA_C.Name,"essOrk__A_Csw")
	Actions.TakeObject(essOrkA_D.Name,"essOrk__A_Dsh") ; Actions.TakeObject(essOrkA_D.Name,"essOrk__A_Dsw")
	Actions.TakeObject(essOrkA_E.Name,"essOrk__A_Esh") ; Actions.TakeObject(essOrkA_E.Name,"essOrk__A_Esw")
	Actions.TakeObject(essOrkA_F.Name,"essOrk__A_Fsh") ; Actions.TakeObject(essOrkA_F.Name,"essOrk__A_Fsw")
	Actions.TakeObject(essOrkA_G.Name,"essOrk__A_Gsh") ; Actions.TakeObject(essOrkA_G.Name,"essOrk__A_Gsw")
	Actions.TakeObject(essOrkA_H.Name,"essOrk__A_Hsh") ; Actions.TakeObject(essOrkA_H.Name,"essOrk__A_Hsw")
	Actions.TakeObject(essOrkA_I.Name,"essOrk__A_Ish") ; Actions.TakeObject(essOrkA_I.Name,"essOrk__A_Isw")

	darfuncs.HideBadGuy( "essOrk__A_A")
	darfuncs.HideBadGuy( "essOrk__A_B")
	darfuncs.HideBadGuy( "essOrk__A_C")
	darfuncs.HideBadGuy( "essOrk__A_D")
	darfuncs.HideBadGuy( "essOrk__A_E")
	darfuncs.HideBadGuy( "essOrk__A_F")
	darfuncs.HideBadGuy( "essOrk__A_G")
	darfuncs.HideBadGuy( "essOrk__A_H")
	darfuncs.HideBadGuy( "essOrk__A_I")

def essSceneACreate():
	darfuncs.UnhideBadGuy( "essOrk__A_A")
	darfuncs.UnhideBadGuy( "essOrk__A_B")
	darfuncs.UnhideBadGuy( "essOrk__A_C")
	darfuncs.UnhideBadGuy( "essOrk__A_D")
	darfuncs.UnhideBadGuy( "essOrk__A_E")
	darfuncs.UnhideBadGuy( "essOrk__A_F")
	darfuncs.UnhideBadGuy( "essOrk__A_G")
	darfuncs.UnhideBadGuy( "essOrk__A_H")
	darfuncs.UnhideBadGuy( "essOrk__A_I")

def essSceneADestroy():
	essOrkA_A=Bladex.GetEntity( "essOrk__A_A")
	essOrkA_B=Bladex.GetEntity( "essOrk__A_B")
	essOrkA_C=Bladex.GetEntity( "essOrk__A_C")
	essOrkA_D=Bladex.GetEntity( "essOrk__A_D")
	essOrkA_E=Bladex.GetEntity( "essOrk__A_E")
	essOrkA_F=Bladex.GetEntity( "essOrk__A_F")
	essOrkA_G=Bladex.GetEntity( "essOrk__A_G")
	essOrkA_H=Bladex.GetEntity( "essOrk__A_H")
	essOrkA_I=Bladex.GetEntity( "essOrk__A_I")
	essOrkA_A.SubscribeToList("Pin") ; essOrkA_A.RemoveFromWorld()
	essOrkA_B.SubscribeToList("Pin") ; essOrkA_B.RemoveFromWorld()
	essOrkA_C.SubscribeToList("Pin") ; essOrkA_C.RemoveFromWorld()
	essOrkA_D.SubscribeToList("Pin") ; essOrkA_D.RemoveFromWorld()
	essOrkA_E.SubscribeToList("Pin") ; essOrkA_E.RemoveFromWorld()
	essOrkA_F.SubscribeToList("Pin") ; essOrkA_F.RemoveFromWorld()
	essOrkA_G.SubscribeToList("Pin") ; essOrkA_G.RemoveFromWorld()
	essOrkA_H.SubscribeToList("Pin") ; essOrkA_H.RemoveFromWorld()
	essOrkA_I.SubscribeToList("Pin") ; essOrkA_I.RemoveFromWorld()

def essSceneAAnim() :
	essOrkA_A=Bladex.GetEntity( "essOrk__A_A")
	essOrkA_B=Bladex.GetEntity( "essOrk__A_B")
	essOrkA_C=Bladex.GetEntity( "essOrk__A_C")
	essOrkA_D=Bladex.GetEntity( "essOrk__A_D")
	essOrkA_E=Bladex.GetEntity( "essOrk__A_E")
	essOrkA_F=Bladex.GetEntity( "essOrk__A_F")
	essOrkA_G=Bladex.GetEntity( "essOrk__A_G")
	essOrkA_H=Bladex.GetEntity( "essOrk__A_H")
	essOrkA_I=Bladex.GetEntity( "essOrk__A_I")
	essOrkA_A.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_A.LaunchAnimation("Ork_ejercito8")
	essOrkA_B.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_B.LaunchAnimation("Ork_ejercito7")
	essOrkA_C.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_C.LaunchAnimation("Gor_ejercito6")
	essOrkA_D.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_D.LaunchAnimation("Ork_ejercito4")
	essOrkA_E.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_E.LaunchAnimation("Ork_ejercito5")
	essOrkA_F.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_F.LaunchAnimation("Gor_ejercito6")
	essOrkA_G.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_G.LaunchAnimation("Ork_ejercito8")
	essOrkA_H.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_H.LaunchAnimation("Ork_ejercito7")
	essOrkA_I.SetTmpAnmFlags(1,1,1,0,5,1,0); essOrkA_I.LaunchAnimation("Gor_ejercito6")

def essSceneAMiniFadeOut(ent,frame) :
	AuxFuncs.FadeTo(2.0, 0.1)

def essSceneACamReset(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	essSceneADestroy()
	AuxFuncs.FadeFrom(4.0, 0.0)
	Bladex.AddScheduledFunc ( Bladex.GetTime()+4.0, BreakDoor, (0,"Player1"))
	palaceSecA.Active=1
	palaceSecB.Active=1
	Bladex.ExeMusicEvent(-1)


def essSceneACamC(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito_Camera03.cam",101,157)
	cam.AddCameraEvent( 117-101,essSceneAMiniFadeOut)
	cam.AddCameraEvent(-1,essSceneACamReset)

def essSceneACamB(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito_Camera02.cam",56,100)
	cam.AddCameraEvent(-1,essSceneACamC)

def essSceneACamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Ejercito_Camera01.cam",0,55)
	cam.AddCameraEvent(-1,essSceneACamB)
	AuxFuncs.FadeFrom(1.0, 0.0)

def essSceneALaunch():
	if (essSceneALaunched) : return
	global essSceneALaunched
	essSceneALaunched=1
	essSceneACreate()
	essSceneACamA()
	essSceneAAnim()



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_laser.py    **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def DerrumbeMeMuero():
	global EstadoPuertaGema

	if EstadoPuertaGema == Doors.OPENED:
		char.Life = 0.0
		char.Wuea = Reference.WUEA_ENDED
		char.SetTmpAnmFlags(1,1,1,0,5,1)
		char.LaunchAnmType("dth_rockfront")
		cam=Bladex.GetEntity("Camera")
		cam.TType = 0
		cam.SType = 0

	SexRock.Active = 1

	for v in vigacaida:
		v.PutToWorld()

	for v in vigas:
		v.RemoveFromWorld()

	for o in Rocas:
		o.Impulse(0,1000,1280)
	PisaBotonGema(0,"Player1")
	GemoSec.OnEnter = None
	GemoSec.OnLeave = None
	_SoundGolpeFatidico.Play(-63049.6863181, -5000, 171675.553902,1)
	_SndTunderRay.Play(-63049.6863181, -5000, 171675.553902,0)

	AuxFuncs.FadeFrom(0.15,0.0,128,128,128)
	darfuncs.Temblores(1.0,800)

def LanzaRayo(posi,d):
	rayo[0].Active  = d
	rayo[1].Active  = d
	rayo[2].Active  = d
	rayo[3].Active  = d

	rayoMalo.Target = posi
	rayoMalo.Active  = d
	_SndTunderRay.Play(posi[0],posi[1],posi[2],0)

def AbrepuertaGEMA():
	puertaGEMA.OpenDoor()

def CierrapuertaGEMA():
	puertaGEMA.CloseDoor()

def AbrepuertaCABEZA():
	puertaCABEZA.OpenDoor()
	AbreP.Position = (-62390.398, 1058.545, 178348.235)
	_SoundClank.Play(-62390.398, 1058.545, 178348.235,0)

def CierrapuertaCABEZA():
	puertaCABEZA.CloseDoor()

def PuertaCerrada():
	global EstadoPuertaGema
	if EstadoPuertaGema == Doors.OPENED:
		puertaGEMA.OpenDoor()

def PuertaAbierta():
	global EstadoPuertaGema
	if EstadoPuertaGema == Doors.CLOSED:
		puertaGEMA.CloseDoor()

def PisaBotonGema(sectorindex,entityname):
	global EstadoPuertaGema
	if entityname=='Player1':
		DerruP.Position = -62362.797, 1107.151, 171557.77
		_SoundClank.Play( -62362.797, 1107.151, 171557.77,0)
		EstadoPuertaGema = Doors.OPENED
		puertaGEMA.OpenDoor()

def SueltaBotonGema(sectorindex,entityname):
	global EstadoPuertaGema
	if entityname=='Player1':
		DerruP.Position = -62362.797000,907.151000,171557.77000
		_SoundClank.Play( -62362.797000,907.151000,171557.77000,0)
		EstadoPuertaGema = Doors.CLOSED
		puertaGEMA.CloseDoor()

def PartLimber(PersonName,idx):
	char = Bladex.GetEntity(PersonName)
	if char:
		if idx == 1:
		        o = char.SeverLimb(1)
		        if o: o.Impulse(0,-10000,0)
		if idx == 2:
		        o = char.SeverLimb(2)
		        if o: o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
		if idx == 4:
		        o = char.SeverLimb(4)
		        if o: o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))
		if idx == 6:
		        o = char.SeverLimb(6)
		        if o: o.Impulse(-10000*math.cos(char.Angle),-10000,-10000*math.sin(char.Angle))
		if idx == 8:
		        o = char.SeverLimb(8)
		        if o: o.Impulse(10000*math.cos(char.Angle),-10000,10000*math.sin(char.Angle))

def ElectricShock(PersonName = "Player1",i=0):
	per = Bladex.GetEntity(PersonName)
	x, y, z = per.Position
	rayo=Bladex.CreateEntity("Rayo1", "Entity ElectricBolt", 0, 0, 0)
	rayo.Target           = x, y, z
	rayo.MaxAmplitude     = 200
	rayo.MinSectorLength  = 100000
	rayo.Active           = 1
	rayo.Damage           = 0
	node = per.GetNodeIndex(PartesRayuela[i%len(PartesRayuela)])
	if node != -1:
		per.LinkToNode(rayo,node)
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.0, per.Unlink,(rayo,))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, rayo.SubscribeToList,("Pin",))

	return rayo

def FlickLight(luzname):
	o = Bladex.GetEntity(luzname)
	if o:
		o.Intensity   = whrandom.random()
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.05, FlickLight,(luzname,))

def Destrozator(persname="Player1"):
	pers=Bladex.GetEntity(persname)
	pers.Life = 0
	pers.Move(0,-100,0)
	pers.CastShadows = 0
	pers.Wuea = Reference.WUEA_ENDED
	pers.SetTmpAnmFlags(1,1,1,0,5,1)
	pers.LaunchAnmType("dth_n02")

	LanzaRayo(pers.Position,1)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1, LanzaRayo,(pers.Position,0))

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.05, ElectricShock,(persname,4))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.30, ElectricShock,(persname,0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.55, ElectricShock,(persname,1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.80, ElectricShock,(persname,2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.05, ElectricShock,(persname,3))

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, PartLimber, (persname,1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.50, PartLimber, (persname,2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.75, PartLimber, (persname,4))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.00, PartLimber, (persname,6))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.25, PartLimber, (persname,8))

	luzta             = Bladex.CreateEntity("Luz2","Entity Spot",0,0,0)
	luzta.Color       = 0,255,255
	luzta.Intensity   = 1
	luzta.Precission  = 0.09
	luzta.CastShadows = 0
	luzta.SizeFactor  = 0
	luzta.Flick       = 1
	pers.Link(luzta)

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.45, pers.Unlink,(luzta,))
	FlickLight(luzta.Name)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.50, luzta.SubscribeToList, ("Pin",))

def RayoMaloMataAlIdiota(sectorindex,entityname):
	global EstadoPuertaGema
	if entityname=='Player1':
		if EstadoPuertaGema == Doors.OPENED:
			AbreCam.PTS = [((-86328.0963008, -5696.69686388, 175821.686625), (-81975.4774546, -4584.14345227, 175623.857703), 2), ((-75380.3477814, -170.292168029, 176042.4683), (-77072.9417815, -2458.67321527, 175666.332108), 2)]
			AbreCam.AbreCam()
			AbreCam.LastTime = 2
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("conseguido"))
			Bladex.AddScheduledFunc(Bladex.GetTime()+2, LanzaRayo,(GemaUno.Position,1))
			Bladex.AddScheduledFunc(Bladex.GetTime()+4, LanzaRayo,(GemaUno.Position,0))
		else:
			Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
			Destrozator()
		RayoMaloSec.OnEnter = None

def GolpeAlPilar(stick,sticker,x,y,z,xc,yc,zc,wcx,wcy,wcz,wdx,wdy,wdz):
	global HitsLeft

	dust.DropDust(x,y,z,0,0,0,256,"Tierrax",64,0.125).YGravity=0
	_SoundMaderazo.Play(x,y,z,0)

	dust.DropDust(-63049.6863181, -5000, 171675.553902,0,0,0).YGravity=2500.0
	vigas[0].Rotate(1,0,0,-0.025)
	vigas[3].Rotate(1,0,0,0.025)
	_Soundbrum.Play(-63049.6863181, -5000, 171675.553902,0)

	HitsLeft = HitsLeft -1

	if HitsLeft <= 0:
		Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, DerrumbeMeMuero,())
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.00,dust.RemueveTierraGen,(-61670.3488544, -3000.0, 171566.507233,1500,1500))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.25,dust.RemueveTierraGen,(-61670.3488544, -2000.0, 171566.507233,1500,1500))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.50,dust.RemueveTierraGen,(-61670.3488544, -1000.0, 171566.507233,1500,1500))
		Bladex.AddScheduledFunc(Bladex.GetTime()+4.75,dust.RemueveTierraGen,(-61670.3488544,     0.0, 171566.507233,1500,1500))
		dust.DropDust(-63049.6863181, -5000, 171675.553902,0,0,0).YGravity=2500.0
		_SoundTemblorFatidico.Play(-63049.6863181, -5000, 171675.553902,0)
		vigas[0].HitFunc = None


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para agua.py            **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def cogeT1(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla1")
	inv.LinkLeftHand("Tablilla1")
	inv.RemoveObject("Tablilla1")

def cogeT2(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla2")
	inv.LinkLeftHand("Tablilla2")
	inv.RemoveObject("Tablilla2")

def cogeT3(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla3")
	inv.LinkLeftHand("Tablilla3")
	inv.RemoveObject("Tablilla3")

def cogeT4(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla4")
	inv.LinkLeftHand("Tablilla4")
	inv.RemoveObject("Tablilla4")

def cogeT5(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla5")
	inv.LinkLeftHand("Tablilla5")
	inv.RemoveObject("Tablilla5")

def cogeT6(gpointer,usefrom):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	inv.AddTablet("Tablilla6")
	inv.LinkLeftHand("Tablilla6")
	inv.RemoveObject("Tablilla6")


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para LlaveCabeza.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def musicayte1():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("palacellave1"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, GameText.WriteText, ("M15T2",))

def musicayte2():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("palacellave2"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, GameText.WriteText, ("M15T3",))

def musicayte3():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("palacellave3"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.5, GameText.WriteText, ("M15T4",))

def musicayte4():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("palacellave4"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.5, GameText.WriteText, ("M15T5",))

def StopCameraFire(Camera,Frame):
	global thiskey
	global KeyOpenDoor

	if (FireCamera == "Palacio_Camera_fuego1.cam"):
		essSceneBLaunch(0,"Player1")
		#print "Escena Yuio tu eres eres el culpable"
	elif (KeyOpenDoor == 2):
		KeyOpenDoor = 3
		cam=Bladex.GetEntity("Camera")
		cam.SetPersonView("Player1")
		cam.Cut()
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1,abrePuertaChota,(thiskey,))
	else:
		cam=Bladex.GetEntity("Camera")
		cam.SetPersonView("Player1")
		cam.Cut()
		ScriptSkip.SkipScriptEnd()
		Scorer.SetVisible(1)
		Bladex.SetListenerPosition(1)


def EnciendeAltar():
	llamarada=Bladex.CreateEntity(FireCamera, "Entity Particle System D1", PosFire[0],PosFire[1],PosFire[2])
	llamarada.ParticleType="Flame"+cab.Name
	llamarada.YGravity=-4000.0
	llamarada.Friction=0.12
	llamarada.PPS=300
	llamarada.Velocity=0.0, -2500.0, 0.0
	llamarada.RandomVelocity=45.0
	llamarada.Time2Live=14
	AuxFuncs.SetRadialFireDamageObject(llamarada.Name, 800.0)
	cam=Bladex.GetEntity("Camera")
	cam.SetMaxCamera(FireCamera,0,-1)
	cam.AddCameraEvent(-1,StopCameraFire)
	cam.RemoveFromList("Timer60")
	cam.TimerFunc=""

def CreateRingPS(ring_name, ps_color):
	headps=Bladex.CreateEntity(ring_name+"PS", "Entity Particle System Dobj", 0.0, 0.0, 0.0)
	headps.ObjectName=ring_name
	headps.ParticleType="EnergyRing"+ps_color
	headps.PPS=100
	headps.YGravity=-50.0
	headps.Friction=0.0
	headps.Velocity=0.0, 0.0, 0.0
	headps.RandomVelocity=1.0
	headps.NormalVelocity=0.0
	headps.Time2Live=60

def PuenteSacado():
	puente_llave1.OpenDoor()
	puente_llave2.CloseDoor()

def ResetButtons():
	ButLlave.Reset(1)

def EndConcentrationEffect():
	UnLinkSld(cab.Name)
	UnLinkSld(key.Name)

	headps=Bladex.GetEntity("Aro"+cab.Name+"PS")
	headps.PPS=200
	headps.YGravity=-150.0

	aro=Bladex.GetEntity("Aro"+cab.Name)
	cab.Unlink(aro)

	luzA = Bladex.GetEntity("LuzKeyA")
	luzB = Bladex.GetEntity("LuzKeyB")

	luzA.SubscribeToList("Pin")
	luzB.SubscribeToList("Pin")

	Bladex.GetEntity("Player1").GetInventory().RemoveSpecialKey(key.Name)

	Reference.EntitiesSelectionData[key.Name]=(0,0,"")

	soundenergy.StopSound()

	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, EnciendeAltar, ())

def ActivatePuente():
	puente_llave1.CloseDoor()
	puente_llave2.OpenDoor()

def BreakDoor(sector,entity):
	if (entity == "Player1"):
		sectorbreak.OnEnter = ""

		puerta_llave1.DoBreak((0.0, 0.0, 4.0), (80000,0,110000), (0.0, 0.0, 1000.0))
		puerta_llave2.DoBreak((0.0, 0.0, 4.0), (76000,0,110000), (0.0, 0.0, 1000.0))

		polvareda=Bladex.CreateEntity("PolvoPuerta1", "Entity Particle System D2", 78000,1000,111500)
		polvareda.D= 0,-3000,0
		polvareda.ParticleType="LargeDust"
		polvareda.YGravity=0.0
		polvareda.Friction=0.2
		polvareda.PPS=300
		polvareda.DeathTime=Bladex.GetTime()+3.0/60.0
		polvareda.Velocity=0.0, -1000.0, 1000.0
		polvareda.RandomVelocity=100.0

		polvareda=Bladex.CreateEntity("PolvoPuerta2", "Entity Particle System D2", 79500,1000,111500)
		polvareda.D= 0,-3000,0
		polvareda.ParticleType="LargeDust"
		polvareda.YGravity=0.0
		polvareda.Friction=0.2
		polvareda.PPS=300
		polvareda.DeathTime=Bladex.GetTime()+3.0/60.0
		polvareda.Velocity=0.0, -1000.0, 1000.0
		polvareda.RandomVelocity=100.0

		polvareda=Bladex.CreateEntity("PolvoPuerta3", "Entity Particle System D2", 76500,1000,111500)
		polvareda.D= 0,-3000,0
		polvareda.ParticleType="LargeDust"
		polvareda.YGravity=0.0
		polvareda.Friction=0.2
		polvareda.PPS=300
		polvareda.DeathTime=Bladex.GetTime()+3.0/60.0
		polvareda.Velocity=0.0, -1000.0, 1000.0
		polvareda.RandomVelocity=100.0

		#EnmGenRnd.ActivateEnemy(CabezaEnm1)
		#EnmGenRnd.ActivateEnemy(CabezaEnm2)

		desprendimiento.Position = 78000,0,111000
		desprendimiento.PlaySound(0)


def LinkSld(entity,sld_name):
	obj = Bladex.GetEntity(entity)
	sld = Bladex.GetEntity(sld_name)

	D = sld.Displacement
	Y = obj.Position[1] + D

	InitDataField.Initialise(obj)
	obj.Data = def_class.LinkObj(obj,sld,Y)
	if obj.Kind[:5]=="Llave":
		obj.Data.FollowTarget=1
	else:
		obj.Data.FollowTarget=0

	obj.TimerFunc = obj.Data.ObjetoSigueSliding
	obj.SubscribeToList("Timer60")


def UnLinkSld(entity):
	obj = Bladex.GetEntity(entity)
	obj.Data.FollowTarget=0
	obj.RemoveFromList("Timer60")

def StartConcentrationEffect():
	pos = key.Position
	color=key.Kind[5:]
	if color=="Blanca": # -> efectos verde-azulados
		r1, g1, b1 = 200, 255, 220
		r2, g2, b2 = 80, 255, 200
	elif color=="Amarilla": # -> efectos naranjas
		r1, g1, b1 = 255, 220, 200
		r2, g2, b2 = 255, 200, 80
	elif color=="Azul": # -> efectos azules
		r1, g1, b1 = 200, 220, 255
		r2, g2, b2 = 80, 100, 255
	else: # -> efectos rojos
		r1, g1, b1 = 255, 200, 220
		r2, g2, b2 = 255, 80, 100

	luzA=Bladex.CreateEntity("LuzKeyA","Entity Spot",pos[0],pos[1],pos[2])
	luzA.Color=r1, g1, b1
	luzA.Intensity=0.1
	luzA.Precission=0.1
	luzA.CastShadows=0
	luzA.GlowTexture="Flare Magico 256"
	luzA.GlowTestZ=0
	luzA.AngVel=1.59
	luzA.SizeFactor=0.005
	luzA.Data= 0.01

	luzB=Bladex.CreateEntity("LuzKeyB","Entity Spot",pos[0],pos[1],pos[2])
	luzB.Color=r2, g2, b2
	luzB.Intensity=0.1
	luzB.Precission=0.1
	luzB.CastShadows=0
	luzB.GlowTexture="Flare Magico 128"
	luzB.GlowTestZ=0
	luzB.AngVel=-3.14
	luzB.SizeFactor=0.01
	luzB.Data=0.01

	luzA.TimerFunc=GrowMe
	luzA.SubscribeToList("Timer60")
	luzB.TimerFunc=GrowMe
	luzB.SubscribeToList("Timer60")

	key.Link(luzA)
	key.Link(luzB)

	headps=Bladex.GetEntity("Aro"+cab.Name+"PS")
	headps.PPS=300
	headps.YGravity=-300.0

	sndflash.Position=pos[0],pos[1],pos[2]
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, sndflash.PlaySound, (0,))

def BajaPedestal():
	LinkSld(cab.Name,pedestal.sld_area().Name)
	LinkSld(key.Name,pedestal.sld_area().Name)

	pedestal.OpenDoor()

def GrowMe(ent_name, time):
	global Disminution
	global FadingOut
	global FadeColor
	luz=Bladex.GetEntity(ent_name)
	luz.SizeFactor = luz.SizeFactor + luz.Data

	if (Disminution < 2):
		if luz.SizeFactor > 50:
			Disminution = Disminution + 1
			luz.Data = -6.0
			if not FadingOut:
				FadingOut=1
				AuxFuncs.FadeFrom(1.0, 0.0, FadeColor[0], FadeColor[1], FadeColor[2])
				AuraKey(key.Name)
		elif luz.SizeFactor >= 3:
			luz.Data = 6.0
	elif (luz.SizeFactor <= 0.1):
		luz.SizeFactor = 0.1
		luz.Visible=0
		luz.RemoveFromList("Timer60")
		luz.TimerFunc=""

		if (Disminution == 3):
			Bladex.AddScheduledFunc(time + 2.0,BajaPedestal,())
			Disminution = 0
			FadingOut = 0
		else:
			Disminution = 3


def LlavePoseida(entity,time):
	framekey = time - start_time_key

	if (framekey < 8.0):
		posnode = Traps_C.GetSplinePos(splinellave,framekey)
		key.Position = posnode[0],posnode[1],posnode[2]

		if (framekey < 6.0):
			posnode = Traps_C.GetSplinePos(splinellave,framekey + 1.5)
	else:
		key.RemoveFromList("Timer60")
		StartConcentrationEffect()

def UnHideKey(entity,time):
	global start_time_key

	key.Scale = key.Scale + 0.002
	key.Alpha = min(1.0, key.Alpha + 0.0022)

	if (key.Scale > 1.0):
		key.Scale = 1.0
		key.Alpha = 1.0
		key.TimerFunc = LlavePoseida
		start_time_key = time

def StartConcentration():
	pos = key.Position
	key.Scale = 0.1
	key.SubscribeToList("Timer60")
	key.TimerFunc = UnHideKey

def ReseteaCamaraPuertaChota():
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	Bladex.ExeMusicEvent(-1)

def abrePuertaChota(id):
	AbreCam.PTS = [(( 19698.2961451, -4341.12099407, 72930.600740), (23661.7475197, -6438.68947761, 73114.56279), 2),
			   ((-1143.85078217, -2664.09722331, 68719.9894875), (-2261.56399012, -1720.24548149, 72082.2099828), 1.75),
			   ((-16325.9572188, -1294.87040183, 72919.5847106), (-20683.9946231, -181.996239274, 72865.8711614), 1.75),
			   ((-24284.1671183, -1568.14119981, 76135.626350), (-24323.947941, -454.300925584, 80497.59693), 2),
			   ((-26789.685117,  -3799.39692991, 84497.513482), (-25483.291788, -2684.06838226, 88665.55743), 2),
			   ((-26789.685117,  -3799.39692991, 84497.513482), (-25483.291788, -2684.06838226, 88665.55743), 2)]
			   #((-27290.685117,  -4245.39692991, 86169.513482), (-25715.291788, -3130.06838226, 90298.55743), 2)]
	AbreCam.CallBack = ReseteaCamaraPuertaChota
	AbreCam.LastTime = 0
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("conseguido"))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,puerta111.OpenDoor,())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0,puerta222.OpenDoor,())
	AbreCam.AbreCam()

def AuraPlayerVariation(ent_name, time):
	global aura_size
	global aura_var
	aura_size=aura_size+aura_var
	aplayer=Bladex.GetEntity(ent_name)
	if aura_size>5 and aura_size<200:
		aplayer.SetAuraParams(aura_size, 1, 1, 0, 1, 1)
	elif aura_size>=200:
		aura_var=-2
	else:
		aura_size=5
		aura_var=4
		aplayer.RemoveFromList("Timer30")
		aplayer.TimerFunc=""
		aplayer.SubscribeToList("Pin")

def CambiaPPSAuraPlayer(part, pps):
	part.PPS=pps

def AuraPlayer():
	global aura_size
	global AuraColor1
	global AuraColor2
	r1, g1, b1 = AuraColor1
	r2, g2, b2 = AuraColor2
	char=Bladex.GetEntity("Player1")
	aplayer=Bladex.CreateEntity("AuraJugador", "Entity Aura", 0, 0, 0)
	aplayer.SetAuraParams(aura_size, 1, 1, 0, 1, 1)
	aplayer.SetAuraGradient(2, r1, g1, b1, 1.0, 0.0, r1, g1, b1, 0.0, 0.3)
	aplayer.SetAuraGradient(1, r2, g2, b2, 0.2, 0.3, r2, g2, b2, 0.0, 1.0)
	char.Link(aplayer)
	aplayer.SetAuraActive(1)
	aplayer.TimerFunc=AuraPlayerVariation
	aplayer.SubscribeToList("Timer30")
	paplayer=Bladex.CreateEntity("PartsAuraJugador", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
	paplayer.PersonName="Player1"
	paplayer.FollowFactor=1.0
	paplayer.ParticleType="EnergyKey"+key.Kind[5:]
	paplayer.PPS=100
	paplayer.YGravity=0.0
	paplayer.Friction=0.0
	paplayer.Velocity=0.0, 0.0, 0.0
	paplayer.RandomVelocity=0.0
	paplayer.NormalVelocity=0.0
	paplayer.Time2Live=60
	paplayer.DeathTime=Bladex.GetTime()+3.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, CambiaPPSAuraPlayer, (paplayer, 150))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, CambiaPPSAuraPlayer, (paplayer, 200))
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, CambiaPPSAuraPlayer, (paplayer, 250))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, CambiaPPSAuraPlayer, (paplayer, 200))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, CambiaPPSAuraPlayer, (paplayer, 150))

def AuraKey(key_name):
	global AuraColor1
	global AuraColor2
	r1, g1, b1 = AuraColor1
	r2, g2, b2 = AuraColor2
	key=Bladex.GetEntity(key_name)
	akey=Bladex.CreateEntity("Aura"+key_name, "Entity Aura", 0, 0, 0)
	akey.SetAuraParams(35, 0.8, 1, 0, 0, 1)
	akey.SetAuraGradient(2, r1, g1, b1, 1.0, 0.0, r1, g1, b1, 0.0, 0.3)
	akey.SetAuraGradient(1, r2, g2, b2, 0.2, 0.3, r2, g2, b2, 0.0, 1.0)
	key.Link(akey)
	akey.SetAuraActive(1)
	pakey=Bladex.CreateEntity("PartsAura"+key_name, "Entity Particle System Dobj", 0.0, 0.0, 0.0)
	pakey.ObjectName=key_name
	pakey.FollowFactor=1.0
	pakey.ParticleType="EnergyRing"+key.Kind[5:]
	pakey.PPS=140
	pakey.YGravity=0.0
	pakey.Friction=0.0
	pakey.Velocity=0.0, 0.0, 0.0
	pakey.RandomVelocity=0.0
	pakey.NormalVelocity=0.0
	pakey.Time2Live=60

def StartCreateKey(sector,entity):
	global KeyOpenDoor
	global FireCamera
	global LlaveLocated
	global splinellave
	global PosFire
	global pedestal
	global luzAura
	global cab
	global key
	global thiskey
	global AuraColor1
	global AuraColor2
	global FadeColor

	if (entity == "Player1"):
		pos = char.Position

		if (sector == sectorllave1.Index and LlaveLocated[0] == 0): # Blanca -> Efectos verde-azulados
			ScriptSkip.SkipScriptStart("LlaveCab1")
			Bladex.GetSector(-14000,0,73250).Active = 0
			Bladex.GetSector(-16625,-2000,17750).Active = 0
			Bladex.GetSector(-42250,0,66300).Active = 0
			Bladex.GetSector(3250,-2000,129750).Active = 0
			pos = 78250, -620, 131100
			ang = 3.14159
			cab = Bladex.GetEntity("Cabezon")
			LlaveLocated[0] = 1
			pedestal = pedestal1
			pos3 = 78375,-1600,129125
			FireCamera = "Palacio_Camera_fuego1.cam"
			PosFire = 100000,-1600,209000
			key=key1
			AuraColor1=0.6, 1.0, 0.8
			AuraColor2=0.0, 1.0, 0.8
			FadeColor=185, 255, 210
			musicayte3()
		elif (sector == sectorllave2.Index and LlaveLocated[1] == 0): # Amarilla -> Efectos naranjas
			ScriptSkip.SkipScriptStart("LlaveCab2")
			seccer1.Active = 1

			pos = -77200, 150, 70300
			ang = 3.14159/2.0
			cab = Bladex.GetEntity("Cabezon1")
			LlaveLocated[1] = 1
			pedestal = pedestal2
			pos3 = -80958,-2054,70300
			FireCamera = "Palacio_Camera_fuego2.cam"
			PosFire = 89000,-1600,209000
			KeyOpenDoor = KeyOpenDoor + 1
			thiskey = 1
			#print thiskey
			key=key2
			AuraColor1=1.0, 0.8, 0.6
			AuraColor2=1.0, 0.6, 0.0
			FadeColor=255, 210, 185
			musicayte1()
		elif (sector == sectorllave3.Index and LlaveLocated[2] == 0): # Azul -> Efectos azules
			ScriptSkip.SkipScriptStart("LlaveCab3")
			pos = 26000, -5870, 73250
			ang = 3.0*3.14159/2.0
			cab = Bladex.GetEntity("Cabezon2")
			LlaveLocated[2] = 1
			pedestal = pedestal3
			pos3 = 29418,-7791,73250
			FireCamera = "Palacio_Camera_fuego3.cam"
			PosFire = 99750,-1600,203250
			KeyOpenDoor = KeyOpenDoor + 1
			thiskey = 2
			#print thiskey
			key=key3
			AuraColor1=0.7, 0.7, 1.0
			AuraColor2=0.2, 0.3, 1.0
			FadeColor=185, 210, 255
			musicayte2()
		elif (sector == sectorllave4.Index and LlaveLocated[3] == 0): # Negra -> Efectos rojos
			ScriptSkip.SkipScriptStart("LlaveCab4")
			pos = -87900, -5860, 175000
			ang = 3.14159/2.0
			cab = Bladex.GetEntity("Cabezon3")
			LlaveLocated[3] = 1
			pedestal = pedestal4
			pos3 =  -91314,-7545,175000
			FireCamera = "Palacio_Camera_fuego4.cam"
			PosFire = 89000,-1600,203250
			key=key4
			AbrepuertaNEGRA()
			AbrepuertaRANA()
			AuraColor1=1.0, 0.7, 0.7
			AuraColor2=1.0, 0.3, 0.2
			FadeColor=255, 185, 210
			musicayte4()
		else:
			return 1

		pedestal.CloseDoor()
		pos2 = pos[0] + ((pos3[0] - pos[0]) * 0.5), pos[1] + ((pos3[1] - pos[1]) * 0.5), pos[2] + ((pos3[2] - pos[2]) * 0.5)

		char.SetTmpAnmFlags(1,1,1,0,5,1,0)
		char.LaunchAnmType("drop_magic_key")
		char.Position=pos
		char.Angle=ang

		key.Position = pos[0] + ((pos3[0] - pos[0]) * 0.25), pos[1] - 200, pos[2] + ((pos3[2] - pos[2]) * 0.25)
		key.Scale=0.1
		posk = key.Position

		parts=Bladex.CreateEntity("Parts"+key.Name, "Entity Particle System Dobj", 0.0, 0.0, 0.0)
		parts.ObjectName=key.Name
		parts.FollowFactor=1.0
		parts.ParticleType="EnergyKey"+key.Kind[5:]
		parts.PPS=200
		parts.YGravity=0.0
		parts.Friction=0.0
		parts.Velocity=0.0, 0.0, 0.0
		parts.RandomVelocity=-4.0
		parts.NormalVelocity=-8.0
		parts.Time2Live=60
		parts.DeathTime=Bladex.GetTime()+19.0

		soundenergy.Position = pos[0],pos[1],pos[2]
		soundenergy.PlaySound(-1)

		AuraPlayer()
		StartConcentration()

		cam = Bladex.GetEntity("Camera")
		campos = pos3[0] + ((pos3[0] - posk[0]) * 0.5), pos3[1] + ((pos3[1] - posk[1]) * 0.5), pos3[2] + ((pos3[2] - posk[2]) * 0.5)
		def_class.RoundCamera(campos,pos3,2500)

		splinellave = Traps_C.CreateSpline()
		Traps_C.AddSplineNode(splinellave,posk[0],posk[1],posk[2],0,1,0,0,0,0,4)
		Traps_C.AddSplineNode(splinellave,pos2[0],pos2[1],pos2[2],0,1,0,0,0,0,4)
		Traps_C.AddSplineNode(splinellave,pos3[0],pos3[1],pos3[2],0,1,0,0,0,0,2.0)
		Traps_C.CloseSpline(splinellave)

		#Bladex.DeactivateInput()
		Scorer.SetVisible(0)
		Bladex.SetListenerPosition(2)

def SacaKK():
	seccer2.Active = 1
	seccer3.Active = 1
	seccer4.Active = 1


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para iscene.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def iLaunchPersAnim() :
	char = Bladex.GetEntity("Player1")
	char.Position = iCharPosition
	char.Angle = iCharAngle
	char.SetTmpAnmFlags(1,1,1,0,5,1)
	char.LaunchAnmType("diosa_start")

def iLaunchCamFadeOut(camera,frame) :
	AuxFuncs.FadeTo(2.5, 0.0)

def iLaunchCamReset(camera,frame) :
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	#cam.Cut()
	ScriptSkip.SkipScriptEnd()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)

def iLaunchCamB(ent,frame) :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Diosa_Camera2.cam",300,808)
	cam.AddCameraEvent(-1,iLaunchCamReset)
	AuxFuncs.FadeFrom(3.0, 0.0)

def iLaunchCamA() :
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera("Diosa_Camera1.cam",0,300)
	cam.AddCameraEvent(300 - (20.0*2.5),iLaunchCamFadeOut)
	cam.AddCameraEvent(-1,iLaunchCamB)

	iLaunchPersAnim()

def MusicayTexto():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("templodiosa-carga"))
	GameText.WriteText("M15T1")

def iLaunchB() :
	iLaunchCamA()

def iLaunch() :
	global iLaunched
	if (iLaunched) : return
	iLaunched=1

	iLaunchB()
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, MusicayTexto, ())


def ParchePrecarga():
	AuxFuncs.FadeFrom(5.0, 5.0)
	Scorer.SetVisible(0)
	Bladex.SetListenerPosition(2)
	ScriptSkip.SkipScriptStart("paldin")

	Bladex.AddScheduledFunc(Bladex.GetTime() + 5.0, iLaunch, ())


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para generadores.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def TerminanLasMuertes():
	AbrepuertaGOL()


def CreateParticle(r= 30,g = 40,b = 50,al = 230.0,part = "BubbleParticle"):
	Bladex.AddParticleGType("Espuma",part,2,8)

	for i in range(8):
		if i < 4:
			aux=1.0 - ((4.0-i)/4.0)

		else:
			aux=(4.0-(i-4))/4.0

		size=10+aux*30.0
		Bladex.SetParticleGVal("Espuma",i,r,g,b,al,size)

def EfectoAgua(espuma,cam,posi,deathtime):
	time = Bladex.GetTime()

	if time < deathtime:
		campos = cam.Position
		v=campos[0]-posi[0], 0.0, campos[2]-posi[2]
		v=B3DLib.Normalize(v)

		pos = posi[0] + v[0] * 1000,posi[1],posi[2] + v[2] * 1000
		desp = v[2] * -500,v[0] * 500

		espuma.Position = pos[0] + desp[0],posi[1] - 2000,pos[2] + desp[1]
		espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2

		Bladex.AddScheduledFunc(time + 0.05,EfectoAgua,(espuma,cam,posi,deathtime))

def SaltaAguaGen(enmgen):
#def SaltaAguaGen():
	global Esp
	Esp = Esp +1
	pos=enmgen.Position
	#pos = -28900, 1400, -23100
	#pos = char.Position
	cam = Bladex.GetEntity("Camera")
	charpos = cam.Position
	v=charpos[0]-pos[0], 0.0, charpos[2]-pos[2]
	v=B3DLib.Normalize(v)

	rpos = pos[0] + v[0] * 800,pos[1],pos[2] + v[2] * 800
	desp = v[2] * -400,v[0] * 400

	espuma=Bladex.CreateEntity("Espuma"+`Esp`, "Entity Particle System D2", rpos[0] + desp[0],pos[1] - 2000,rpos[2] + desp[1])
	espuma.D=-desp[0] * 2, 0.0, -desp[1] * 2
	espuma.ParticleType="Espuma"
	espuma.PPS=512
	espuma.YGravity=0.0
	espuma.Friction=0.07
	espuma.Velocity=0.0, 0.0, 0.0
	espuma.RandomVelocity=30.0
	espuma.Time2Live=8
	espuma.DeathTime = Bladex.GetTime() + 5.0

	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.05,EfectoAgua,(espuma,cam,pos,espuma.DeathTime))


def SaltaAguaGenActivate(enmgen):
	Bladex.AddScheduledFunc(Bladex.GetTime() + 2.0,SaltaAguaGen,(enmgen,))

def ActivateGen1(sector,entity):
	if (entity == "Player1"):
		Gen1Sec.OnEnter = ""
		generadorT1.GenerateEnemy()

def ActivateGen2(TrSector,entity):
	if (entity == "Player1"):
		Bladex.RemoveTriggerSectorFunc(TrSector, "OnEnter")
		generadorT2.GenerateEnemy()

def ActivateGen3(sector,entity):
	if (entity == "Player1"):
		Gen3Sec.OnEnter = ""
		generadorT3.GenerateEnemy()


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para GEnems.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def GoToMul(entity_name):
	ene=Bladex.GetEntity(entity_name)
	ene.GoTo(ene.Data.nodos[ene.Data.nodo_actual][0], ene.Data.nodos[ene.Data.nodo_actual][1], ene.Data.nodos[ene.Data.nodo_actual][2])
	if ene.Data.nodo_actual<len(ene.Data.nodos)-1:
		ene.Data.nodo_actual=ene.Data.nodo_actual+1
		ene.RouteEndedFunc=GoToMul

def fastGoTo(entName,x,y,z):
	p =Bladex.GetEntity(entName)
	if p.Life > 0:
		p.GoToJogging = 1
		p.GoTo(x,y,z)

def corredorcs():
	fastGoTo("01ORC",72149.8235976, 876.814420527, 104357.454678)
	fastGoTo("02ORC",85780.049567, 1133.95313335, 104009.978329)


def AparecenOrcosPelotudos2():
	Inicio0.UnhideBadGuys(3)
	fastGoTo("4ORC",53779.4372679, 2610.29803188, 42127.603895)
	fastGoTo("5ORC",51326.1481366, 2673.95419844, 44950.6336088)
	fastGoTo("6ORC",51219.7208315, 2624.41765174, 49970.6511026)
	darfuncs.EnterSecEvent(60785.9295331, 2623.02323699, 38911.5428819,AparecenOrcosPelotudos2)


def AparecenOrcosPelotudos():
	Inicio0.UnhideBadGuys(3)
	fastGoTo("1ORC",79617.7432849, 2393.7094478, 66971.3105817)
	fastGoTo("2ORC",76422.6178671, 2391.005053, 63175.3020381)
	fastGoTo("3ORC",78416.795429, 2391.67193099, 58561.1364323)
	darfuncs.EnterSecEvent(60785.9295331, 2623.02323699, 38911.5428819,AparecenOrcosPelotudos2)

def AparecenArkeros1():
	darfuncs.UnhideBadGuy("PalaceArq1")
	darfuncs.UnhideBadGuy("PalaceArq2")

def ActivaLosEnemigosDelSectorDosYMedioN():
	darfuncs.UnhideBadGuy("PalaceArq9")
	darfuncs.UnhideBadGuy("PalaceArq10")
	darfuncs.UnhideBadGuy("Minot1")
	fastGoTo("Minot1",-24599.5721085, 5838.23716678, 54829.1427896)
	AbreZonaSecreta()

def ActivaSectorDosYMedioN():
	darfuncs.EnterSecEvent(-16695.2263939, 1900.6821296, 56659.8988144,ActivaLosEnemigosDelSectorDosYMedioN)

def AparecenOrcosPelotudos3():
	Inicio1.UnhideBadGuys(3)
	fastGoTo("11ORC",-22175.4315868, -2130.08776007, 88897.8565016)
	fastGoTo("12ORC",-25400.2246163, -2131.90584059, 88782.4678619)
	darfuncs.EnterSecEvent(-24438.7726011, 116.532121721, 78546.0763347,AparecenOrcosPelotudos3)

def ActivaVuelta1():
	Inicio1.UnhideBadGuys(3)
	darfuncs.UnhideBadGuy("9ORC")
	darfuncs.UnhideBadGuy("10ORC")
	darfuncs.UnhideBadGuy("PalaceArq3")
	#darfuncs.UnhideBadGuy("PalaceArq4")
	fastGoTo("9ORC",-33675.3498216, -1124.12117698, 46659.0778065)
	fastGoTo("10ORC",-33778.3909658, -1108.9670296, 57417.3808738)
	darfuncs.EnterSecEvent(-24438.7726011, 116.532121721, 78546.0763347,AparecenOrcosPelotudos3)


def ActivaSectorVuelta1():
	darfuncs.EnterSecEvent(-32003.1840926, -1574.50717933, 48582.0973547,ActivaVuelta1)


def ActivaVuelta2():
	darfuncs.UnhideBadGuy("PalaceArq5")
	darfuncs.UnhideBadGuy("PalaceArq6")
	darfuncs.UnhideBadGuy("PalaceArq7")
	darfuncs.UnhideBadGuy("PalaceArq8")


def ActivaSectorVuelta2():
	darfuncs.EnterSecEvent(-32003.1840926, -1574.50717933, 48582.0973547,ActivaVuelta2)

def Atacaminorx():
	darfuncs.UnhideBadGuy("Minot2")
	fastGoTo("Minot2",-24089.537476, -2108.77862959, 149984.751972)

def Final1():
	fastGoTo("13Kngt",8592.30349013, 1871.03950333, 216627.487376)

def Final2():
	fastGoTo("14Kngt",-30606.6138761, 2619.94785406, 216662.378005)

def Final3():
	fastGoTo("Minot3",-34812.1659321, 3559.58817193, 216093.355375)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para flechas_yo.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def BorraFlecha(Name):
	global __FLECHA_KIND__

	global InsideTrapArrow
	ent = Bladex.GetEntity(Name)

	if (ent.Parent==None) | (ent.Parent == ""):
		if(ent.Kind == __FLECHA_KIND__):
			ent.SubscribeToList("Pin")

	if InsideTrapArrow:
		DropArrow()


def Entrampa(sectorindex,entityname):
	global InsideTrapArrow
	global CerradaTFPuerta

	if entityname == "Player1" and CerradaTFPuerta == 0:
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("susto"))
		InsideTrapArrow = 1
		DropArrow()
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, DropArrow,())

def Saltrampa(sectorindex,entityname):
	global InsideTrapArrow
	if entityname == "Player1":
		InsideTrapArrow = 0

def ActivateArrowTrap():
	SActivaTFlecha.OnEnter = Entrampa
	SActivaTFlecha.OnLeave = Saltrampa

def DeactivateArrowTrap():
	global InsideTrapArrow
	SActivaTFlecha.OnEnter = ""
	SActivaTFlecha.OnLeave = ""
	InsideTrapArrow=0

def DropArrow():
	global __POSI_FLECHA__
	global __DELTA_FLECHA__
	global __FLECHA_KIND__

	SPEED = 30000

	o=Bladex.CreateEntity(Bladex.GenerateEntityName(), __FLECHA_KIND__,whrandom.randint(__POSI_FLECHA__[0]-__DELTA_FLECHA__,__POSI_FLECHA__[0]+__DELTA_FLECHA__) ,__POSI_FLECHA__[1],__POSI_FLECHA__[2] , "Arrow")
	ItemTypes.ItemDefaultFuncs (o)
	o.Orientation=0.50005787611, 0.50005787611, -0.499942094088, -0.499942094088
	flechazo.Position = o.Position
	flechazo.PlaySound(1)
	char = Bladex.GetEntity("Player1")

	o.Scale=0.7
	o.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
	o.MessageEvent(Reference.MESSAGE_START_TRAIL, 0,0)
	o.Gravity = 0,9800,0

	vx = char.Position[0]-o.Position[0]
	vz = char.Position[2]-o.Position[2]
	dist = math.sqrt(vx*vx+vz*vz)/SPEED
	vx = vx/dist
	vz = vz/dist

	o.Fly(vx,1000,vz)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, BorraFlecha,(o.Name,))
	return o

def DeactivateSkull():
		DeactivateArrowTrap()
		luzAKalaVera.SubscribeToList("Pin")
		luzBKalaVera.SubscribeToList("Pin")
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("conseguido"))

		dust.DropPiedra(18223.0, -8350.0, 73256.0,-1000,-5000,1500,"Skull")
		dust.DropPiedra(18223.0, -8350.0, 72886.0,-1000,-6000,-1500,"Skull")

		SActivaCierraTF.OnEnter = ""
		SActivaAbreTF.OnEnter   = ""
		MagickSull.HitFunc      = ""
		MagickSull.Static = 1

def HitFuncSkull(stick,sticker,x,y,z,xc,yc,zc,wcx,wcy,wcz,wdx,wdy,wdz):
	global CerradaTFPuerta
	Bladex.GetEntity(sticker).RemoveFromWorld()

	if CerradaTFPuerta == 0:
		GolpeFuegoMaldito.Position = 18223.0, -8532.0, 73256.0
		GolpeFuegoMaldito.PlaySound(1)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, DeactivateSkull,())

def AbreTrampa(sectorindex,entityname):
	global CerradaTFPuerta
	if (entityname == "Player1") and (CerradaTFPuerta==1):
		desplazamientos=(1750.0, 1750.0)
		vectores=((0.0, -1.0, 0.0), (0.0, -1.0, 0.0))
		vel_iniciales=(0.0, 4000)
		vel_finales=(4000.0, 500)

		#sonidos asociados a la puerta-objeto rastmaz1
		son_iniciales=("", "")
		son_durante=(sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano)
		Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
		luzAKalaVera.Intensity=0.00001
		luzBKalaVera.Intensity=0.00001
		CerradaTFPuerta=0

def CierrTrampa(sectorindex,entityname):
	global CerradaTFPuerta
	if (entityname == "Player1") and (CerradaTFPuerta==0):
		desplazamientos=(1750.0, 1750.0, 700.0, 700.0, 250.0, 250.0)
		vectores=((0.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0))
		vel_iniciales=(0.0, 4000, 8000.0, 0.0, 6000.0, 0.0)
		vel_finales=(4000.0, 8000, 0.0, 6000.0, 0.0, 3000.0)

		#sonidos asociados a la puerta-objeto rastmaz1
		son_iniciales=("", "", "", "", "", "")
		son_durante=(sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo, sonidorastrillo)
		son_finales=("", golpemetalmediano,"",golpemetalmediano,"",golpemetalmediano)
		Objects.NDisplaceObject(rastmaz1din, desplazamientos, vectores, vel_iniciales, vel_finales, (), son_durante, son_finales)
		luzAKalaVera.Intensity=0
		luzBKalaVera.Intensity=0
		CerradaTFPuerta=1

def NumeroDeFlechasQueQuedan():
	result = 0
	inv = Bladex.GetEntity("Player1").GetInventory()
	for i in range(inv.nQuivers):
		result = result + Bladex.GetEntity(inv.GetQuiver(i)).Data.ArrowsLeft
	return result

def calcuadrado(x):
	return x*x

def CrearOtraFlechaMagicaSiEsNecesario():
	global SuperFlecha
	if NumeroDeFlechasQueQuedan() == 0:
		dis = calcuadrado(char.Position[0]-18681)+calcuadrado(char.Position[1]-165.363511084)+calcuadrado(char.Position[2]-68674.9442008)
		if dis > 10000*10000:
			CreaSuperFlecha()
		else:
			Bladex.AddScheduledFunc(Bladex.GetTime()+25.0, CrearOtraFlechaMagicaSiEsNecesario,())
	else:
		Bladex.AddScheduledFunc(Bladex.GetTime()+25.0, CrearOtraFlechaMagicaSiEsNecesario,())


def SeLlevaLaFlechaMagica():
	Bladex.AddScheduledFunc(Bladex.GetTime()+25.0, CrearOtraFlechaMagicaSiEsNecesario,())

def CreaSuperFlecha():
	global SuperFlecha
	SuperFlecha=Bladex.CreateEntity("FlechaMagica", "Flecha",18681.6347212, -165.363511084, 68674.9442008)
	SuperFlecha.Scale       = 1
	SuperFlecha.Orientation = (0.740026473999, 0.545812368393, -0.327434927225, -0.217321947217)
	SuperFlecha.Arrow       = 1
	Ontake.AddOnTakeEvent(SuperFlecha.Name,SeLlevaLaFlechaMagica)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para espada.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def AgregaTablilla():
	for i in range(6):
		name = "Tablilla"+`i+1`
		if not Bladex.GetEntity(name):
			o=Bladex.CreateEntity(name,name, 0, 0, 0)
			o.Static = 0
			Bladex.GetEntity("Player1").GetInventory().AddTablet(name)
			return


def musicaytespadacontodastablillas():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("espadacontodastablillas"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, GameText.WriteText, ("M15T7",))

def musicaytespadasinalgunatablilla():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("espadasinalgunatablilla"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, GameText.WriteText, ("M15T6",))

def musicaytespadasinningunatablilla():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("espadasinningunatablilla"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, GameText.WriteText, ("M15T6",))

def musicaytsolopoderconrestotablillas():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("solopoderconrestotablillas"))
	Bladex.AddScheduledFunc(Bladex.GetTime()+16.0, GameText.WriteText, ("M15T9",))

def musicasolotablillas():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("solotablillas"))



#############################
#     Funciones comunes     #
#############################


def FadeAndScaleAuraGrad(ent_name, time):
	aura=Bladex.GetEntity(ent_name)
	aura.Data.CurrentSize=aura.Data.CurrentSize+aura.Data.SizeVar
	aura.Data.CurrentAlpha=aura.Data.CurrentAlpha+aura.Data.AlphaVar
	if aura.Data.CurrentAlpha<0.0:
		aura.Data.CurrentAlpha=0.0
	elif aura.Data.CurrentAlpha>1.0:
		aura.Data.CurrentAlpha=1.0
	aura.SetAuraParams(aura.Data.CurrentSize, aura.Data.CurrentAlpha, 1, 0, 0, 1)
	if ((aura.Data.SizeVar>0 and aura.Data.CurrentSize>=aura.Data.EndSize) or (aura.Data.SizeVar<0 and aura.Data.CurrentSize<=aura.Data.EndSize)):
		aura.RemoveFromList("Timer30")
		aura.TimerFunc=""
		if aura.Data.DestroyOnEnd:
			aura.SubscribeToList("Pin")
		else:
			aura.SetAuraParams(aura.Data.EndSize, aura.Data.EndAlpha, 1, 0, 0, 1)

def FadeAndScaleAura(aura_name, init_size, end_size, init_alpha, end_alpha, time, destroy=0):
	aura=Bladex.GetEntity(aura_name)
	InitDataField.Initialise(aura)
	aura.Data.CurrentSize=init_size
	aura.Data.EndSize=end_size
	aura.Data.SizeVar=(end_size-init_size)/(time*30.0)
	aura.Data.CurrentAlpha=init_alpha
	aura.Data.EndAlpha=end_alpha
	aura.Data.AlphaVar=(end_alpha-init_alpha)/(time*30.0)
	aura.Data.DestroyOnEnd=destroy
	aura.TimerFunc=FadeAndScaleAuraGrad
	aura.SubscribeToList("Timer30")

def FadeAndScaleGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.InitTime
	obj.Alpha=obj.Data.InitAlpha+obj.Data.AlphaInitVel*curr_time+0.5*obj.Data.AlphaAcc*curr_time**2
	obj.Scale=obj.Data.InitScale+obj.Data.ScaleInitVel*curr_time+0.5*obj.Data.ScaleAcc*curr_time**2
	if obj.Data.AngleVar:
		ang=whrandom.uniform(-obj.Data.AngleVar, obj.Data.AngleVar)
		obj.RotateRel(0, 0, 0, 0, 0, 1, ang)
	if curr_time>=obj.Data.TotalTime:
		obj.Alpha=obj.Data.EndAlpha
		obj.Scale=obj.Data.EndScale
		obj.RemoveFromList("Timer30")
		obj.TimerFunc=""
		if obj.Data.DestroyOnEnd==1:
			obj.SubscribeToList("Pin")
		elif obj.Data.DestroyOnEnd==2:
			obj.RemoveFromWorld()

def FadeAndScale(obj_name, pos, init_alpha, end_alpha, alpha_acc, init_scl, end_scl, scl_acc, time, ang_var=0, destroy=0):
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=init_alpha
	obj.Scale=init_scl
	obj.Position=pos
	InitDataField.Initialise(obj)
	obj.Data.InitAlpha=init_alpha
	obj.Data.EndAlpha=end_alpha
	obj.Data.AlphaAcc=alpha_acc*2.0*(end_alpha-init_alpha)/time**2
	obj.Data.AlphaInitVel=(end_alpha-init_alpha-alpha_acc*(end_alpha-init_alpha))/time
	obj.Data.InitScale=init_scl
	obj.Data.EndScale=end_scl
	obj.Data.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.AngleVar=ang_var
	obj.Data.DestroyOnEnd=destroy
	obj.Data.InitTime=Bladex.GetTime()
	obj.Data.TotalTime=time
	obj.TimerFunc=FadeAndScaleGrad
	obj.SubscribeToList("Timer30")

def EnciendeLuzVerde():
	AuxFuncs.SpotIntensityVariation("LuzfIN", 0.0, 30.0, 2.0)

def ApagaLuzVerde():
	AuxFuncs.SpotIntensityVariation("LuzfIN", 30.0, 0.0, 2.0)



#####################################
#     Funciones comunes poderes     #
#####################################


def BorraLenguas(lps):
	lps.DeathTime=Bladex.GetTime()+0.1

def GiraLenguas(genleng):
	genleng.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(1.5*30.0))
	genleng.RotateRel(0, 0, 0, 0, 1, 0, 3.14159/(2.0*30.0))

def LanzaLenguas():
	BladeSword.Alpha=0.0
	BladeSword.RemoveFromWorld()
	cilab=Bladex.GetEntity("CilindroAbajo")
	nv=Bladex.GetEntity("NucleoVortice")
	x, y, z=cilab.Position[0], -17000, cilab.Position[2]
	nv.Position=x, y+1000.0, z
	cv=Bladex.CreateEntity("ConcentracionVortice","Entity Particle System Dobj", x, y, z)
	cv.ObjectName=nv.Name
	cv.ParticleType="BigBlueEnergyCon"
	cv.YGravity=0
	cv.RandomVelocity=5
	cv.NormalVelocity=-20
	cv.Velocity=0.0,-1000.0,0.0
	cv.Time2Live=60
	cv.PPS=400
	cv.DeathTime=Bladex.GetTime()+3.5
	genleng=Bladex.GetEntity("GeneradorLenguas")
	genleng.Orientation=0.707107,0.707107,0.000000,0.000000
	lps=Bladex.CreateEntity("LenguasPS","Entity Particle System Dobj", x, y, z)
	lps.ObjectName=genleng.Name
	lps.ParticleType="BlueEnergyDis3"
	lps.YGravity=-400
	lps.RandomVelocity=2
	lps.NormalVelocity=0
	lps.Velocity=0.0,0.0,0.0
	lps.Time2Live=60
	lps.PPS=400
	genlengdin=genleng.Data.dinobjdata
	Objects.DisplaceObjectFromTo(genlengdin, (x, y, z), (x, y+14500, z), 3000.0, 3000.0, "", "", "", GiraLenguas, (genleng,), BorraLenguas, (lps,))

def ApagaSegundoImpacto():
	cilgo.Alpha=max(0.0, cilgo.Alpha-1.0/(2.0*30.0))
	if cilgo.Alpha<=0.0:
		cilgodin.Stop()

def OcultaImpactosYTornado():
	cilab.RemoveFromWorld()
	cilar.RemoveFromWorld()
	cilgo.RemoveFromWorld()
	DesapareceTornado()

def ApagaPrimerImpacto():
	FadeAndScale("CilindroAbajo", (cilab.Position[0], cilab.Position[1], cilab.Position[2]), 0.95, 0.0, 1, 1.0, 0.1, 1, 1.0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, OcultaImpactosYTornado, ())

def ApagaPoder(EntityName, EventName):
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 80.0, 0.0, 2.5)
	FadeAndScaleAura("AuraCilindroAbajo", 200, 100, 1, 0, 2.0, 1)
	FadeAndScaleAura("AuraCilindroArriba", 200, 100, 1, 0, 2.0, 1)
	FadeAndScaleAura("AuraCilindroGordo", 1000, 100, 1, 0, 1.5, 1)
	FadeAndScaleAura("AuraPlayerPrimerImpacto", 80, 5, 1, 0, 2.0, 1)
	cilgodin.WhileRotFunc=ApagaSegundoImpacto
	pspi=Bladex.GetEntity("PSPrimerImpactoJugador")
	pspi.RandomVelocity=2
	pspi.NormalVelocity=2
	pspi.PPS=600
	pspi.DeathTime=Bladex.GetTime()+1.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, ApagaPrimerImpacto, ())

def ContSegundoImpacto():
	global acilgo
	nv=Bladex.GetEntity("NucleoVortice")
	nv.RemoveFromWorld()
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 20.0, 80.0, 2.0)
	r1, g1, b1 = 0.4, 0.6, 1.0
	r2, g2, b2 = 0.1, 0.2, 1.0
	acilgo=Bladex.CreateEntity("AuraCilindroGordo", "Entity Aura", 0, 0, 0)
	acilgo.SetAuraParams(10, 1, 1, 0, 0, 1)
	acilgo.SetAuraGradient(1, r1, g1, b1, 0.5, 0.0, r2, g2, b2, 0.0, 0.8)
	cilgo.Link(acilgo)
	acilgo.SetAuraActive(1)
	FadeAndScaleAura(acilgo.Name, 10, 1000, 1, 1, 1.5)
	pspi=Bladex.GetEntity("PSPrimerImpactoJugador")
	pspi.RandomVelocity=5
	pspi.NormalVelocity=5
	pspi.PPS=1400
	FadeAndScale("OndaExp", (cilgo.Position[0], -2500.0, cilgo.Position[2]), 0.96, 0.0, -1, 0.1, 6.0, -1, 2.5, 1.0, 2)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, FadeAndScale, ("OndaExp1", (cilgo.Position[0], -2500.0, cilgo.Position[2]), 0.96, 0.0, -1, 0.1, 6.0, -1, 2.5, 1.0, 2))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, FadeAndScale, ("OndaExp", (cilgo.Position[0], -2500.0, cilgo.Position[2]), 0.96, 0.0, -1, 0.1, 6.0, -1, 2.5, 1.0, 2))

def ContGiroSegundoImpacto():
	Objects.RotateObject(cilgodin, 3.14159*40.0, 50.0, 50.0, (0, 0, 0), (0, 0, 1), Objects.REL, "", "", "", cilgodin.WhileRotFunc, (), ContGiroSegundoImpacto, ())

def EnciendeSegundoImpacto():
	cilgo.Alpha=min(0.95, cilgo.Alpha+1.0/(1.5*30.0))
	if cilgo.Alpha>=0.95:
		cilgodin.WhileRotFunc=""

def SegundoImpacto():
	AuxFuncs.FadeTo(1.15, 0.0, 180, 210, 255)
	cilgo.Position=cilar.Position[0], -11000, cilar.Position[2]
	Objects.RotateObject(cilgodin, 3.14159*40.0, 30.0, 30.0, (0, 0, 0), (0, 0, 1), Objects.REL, "", "", "", EnciendeSegundoImpacto, (), ContGiroSegundoImpacto, ())

def ImpactaPersonajeYSuelo():
	global acilar
	global acilab
	global aplpi
	char=Bladex.GetEntity("Player1")
	pspi=Bladex.CreateEntity("PSPrimerImpactoJugador","Entity Particle System Dperson",0,0,0)
	pspi.PersonName="Player1"
	pspi.ParticleType="BlueEnergyDis2"
	pspi.FollowFactor=0.0
	pspi.YGravity=0
	pspi.RandomVelocity=2.0
	pspi.NormalVelocity=2.0
	pspi.Velocity=0.0,0.0,0.0
	pspi.Time2Live=30
	pspi.PPS=600
	r1, g1, b1 = 0.4, 0.6, 1.0
	r2, g2, b2 = 0.1, 0.2, 1.0
	acilar=Bladex.CreateEntity("AuraCilindroArriba", "Entity Aura", 0, 0, 0)
	acilar.SetAuraParams(10, 1, 1, 0, 0, 1)
	acilar.SetAuraGradient(1, r1, g1, b1, 0.5, 0.0, r2, g2, b2, 0.0, 0.8)
	cilar.Link(acilar)
	acilar.SetAuraActive(1)
	acilab=Bladex.CreateEntity("AuraCilindroAbajo", "Entity Aura", 0, 0, 0)
	acilab.SetAuraParams(10, 1, 1, 0, 0, 1)
	acilab.SetAuraGradient(1, r1, g1, b1, 0.5, 0.0, r2, g2, b2, 0.0, 0.8)
	cilab.Link(acilab)
	acilab.SetAuraActive(1)
	aplpi=Bladex.CreateEntity("AuraPlayerPrimerImpacto", "Entity Aura", 0, 0, 0)
	aplpi.SetAuraParams(10, 1, 1, 0, 0, 1)
	aplpi.SetAuraGradient(1, r1, g1, b1, 0.5, 0.0, r2, g2, b2, 0.0, 0.8)
	char.Link(aplpi)
	aplpi.SetAuraActive(1)
	FadeAndScaleAura(acilar.Name, 10, 200, 1, 1, 2.0)
	FadeAndScaleAura(acilab.Name, 10, 200, 1, 1, 2.0)
	FadeAndScaleAura(aplpi.Name, 10, 80, 1, 1, 2.0)

def EnciendePrimerImpacto():
	cilar.Alpha=cilab.Alpha=min(0.95, cilar.Alpha+1.0/30.0)
	if cilar.Alpha>=0.95:
		cilardin.WhileDisplFunc=cilabdin.WhileDisplFunc=""

def PrimerImpacto(EntityName, EventName):
	char=Bladex.GetEntity("Player1")
	x, y, z = char.Position
	cilar.Position=cilab.Position=x, -19000, z-150
	Objects.DisplaceObject(cilardin, 4250, (0, 1, 0), 20000, 20000)
	Objects.DisplaceObject(cilabdin, 4250+8500, (0, 1, 0), 20000, 20000, "", "", "", EnciendePrimerImpacto, (), ImpactaPersonajeYSuelo, ())
	luzimp=Bladex.GetEntity("LuzImpacto")
	luzimp.Position=x, -6000, z-150
	AuxFuncs.SpotIntensityVariation("LuzImpacto", 0.0, 20.0, 1.5)

#####################################
#     Funciones comunes tornado     #
#####################################


def ApagaRayo():
	rayot=Bladex.GetEntity("RayoTornado")
	luzrayot=Bladex.GetEntity("LuzRayoTornado")
	rayot.Active = 0
	luzrayot.Intensity=0.0

def DisparaRayo():
	#global nr
	global sonidosrayotornado
	global sndnumber
	rayot=Bladex.GetEntity("RayoTornado")
	luzrayot=Bladex.GetEntity("LuzRayoTornado")
	soundrayot=Bladex.GetEntity("SonidoRayoTornado")
	rayot.Active   = 1
	rayot.Position = 94605+GenR.randint(-8000,8000), -16733+GenR.randint(-3000,3000), 172887+GenR.randint(-8000,8000)
	rayot.Target   = 94605+GenR.randint(-5000,5000), -16733+GenR.randint(-2000,2000), 172887+GenR.randint(-5000,5000)
	xl, yl, zl = (rayot.Position[0]+rayot.Target[0])/2.0, (rayot.Position[1]+rayot.Target[1])/2.0, (rayot.Position[2]+rayot.Target[2])/2.0
	luzrayot.Position=xl, yl, zl
	luzrayot.Intensity=80.0
	sonidosrayotornado[sndnumber].Position=xl, yl, zl
	sonidosrayotornado[sndnumber].StopSound()
	sonidosrayotornado[sndnumber].PlaySound(0)
	sndnumber=sndnumber+1
	if (sndnumber>len(sonidosrayotornado)-1):
		sndnumber=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.06, ApagaRayo, ())
	#nr=nr+1
	#print nr

def RepiteRayo():
	rayot=Bladex.GetEntity("RayoTornado")
	DisparaRayo()
	if rayot.Data.Active:
		variation=whrandom.uniform(-rayot.Data.FrecuencyVariation, rayot.Data.FrecuencyVariation)
		Bladex.AddScheduledFunc(Bladex.GetTime()+rayot.Data.Frecuency+variation, RepiteRayo, ())

def CambiaProbRayos(frec, frecvar):
	rayot=Bladex.GetEntity("RayoTornado")
	rayot.Data.Frecuency=frec
	rayot.Data.FrecuencyVariation=frecvar

def PlayRayoPeriodico():
	rayot=Bladex.GetEntity("RayoTornado")
	rayot.Data.Active=1
	RepiteRayo()

def AumentaFrecuenciaRayos():
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.0, CambiaProbRayos, (0.5, 0.45))

def GiraTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(3.0*30.0))
	corona.RotateRel(0, 0, 0, 0, 0, 1, 3.14159/(6.0*30.0))

def DesapareceTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.Alpha=corona.Alpha=max(0.0, corona.Alpha-1.0/(3.0*30.0))
	if vortice.Alpha<=0.0:
		vortice.RemoveFromList("Timer30")
		vortice.TimerFunc=""
		vortice.Scale=0.4
		corona.Scale=0.45
		Bladex.GetEntity("RayoTornado").Data.Active=0
	else:
		GiraTornadoGrad("Vortice", 0)

def DesapareceTornado():
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	rayot=Bladex.GetEntity("RayoTornado")
	rayot.Data.Frecuency=1.5
	rayot.Data.FrecuencyVariation=1.45
	Bladex.GetEntity("PVortice").DeathTime=Bladex.GetTime()+1.0/60.0
	Bladex.GetEntity("PCorona").DeathTime=Bladex.GetTime()+1.0/60.0
	vortice.TimerFunc=DesapareceTornadoGrad

def ApareceTornadoGrad(ent_name, time):
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	vortice.Alpha=corona.Alpha=min(0.99, corona.Alpha+1.0/(6.0*30.0))
	if vortice.Alpha>=0.99:
		vortice.TimerFunc=GiraTornadoGrad
	else:
		GiraTornadoGrad("Vortice", 0)

def ApareceTornado():
	global vortice
	global corona
	global pvor
	global pcor
	vortice=Bladex.GetEntity("Vortice")
	corona=Bladex.GetEntity("Corona")
	pvor=Bladex.CreateEntity("PVortice", "Entity Particle System Dobj", 0, 0, 0)
	pvor.ObjectName="Vortice"
	pvor.ParticleType="Tornado1"
	pvor.YGravity=0
	pvor.Velocity=0, 0, 0
	pvor.NormalVelocity=0
	pvor.RandomVelocity=2
	pvor.FollowFactor=1.0
	pvor.PPS=50
	pvor.Time2Live=90
	pcor=Bladex.CreateEntity("PCorona", "Entity Particle System Dobj", 0, 0, 0)
	pcor.ObjectName="Corona"
	pcor.ParticleType="Tornado2"
	pcor.YGravity=0
	pcor.Velocity=0, 0, 0
	pcor.NormalVelocity=0
	pcor.RandomVelocity=2
	pcor.FollowFactor=0.9
	pcor.PPS=110
	pcor.Time2Live=90
	vortice.TimerFunc=ApareceTornadoGrad
	vortice.SubscribeToList("Timer30")
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, PlayRayoPeriodico, ())



####################################
#     Funciones comunes espada     #
####################################


def Imprimelo():
	bladesword.Position = 94605.0898438, -20733.0249825, 172887.026402
	BladeSword.Position = 94605.0898438, -20733.0249825, 172887.026402
	bladesword.Orientation = 0.707107,0.707107,0.000000,0.000000
	BladeSword.Orientation = 0.707107,0.707107,0.000000,0.000000
	bladesword.PutToWorld()
	BladeSword.PutToWorld()
	bladeswordA.SubscribeToList("Pin")
	BladeSword.Alpha=0.0

def ParticulasFadingCool():
	br=Bladex.CreateEntity("FadingCoolPS","Entity Particle System Dobj",0,0,0)
	br.ObjectName="BladeSword"
	br.ParticleType="BlueEnergyDis"
	br.YGravity=0
	br.RandomVelocity=1
	br.NormalVelocity=1
	br.Velocity=0.0,0.0,0.0
	br.Time2Live=30
	br.PPS=500
	br.DeathTime=Bladex.GetTime()+1.5

def MorphingEspada(ent_name, time):
	bladesword.Alpha=max(0.0, bladesword.Alpha-1.0/(2.0*30.0))
	BladeSword.Alpha=1.0-bladesword.Alpha
	if bladesword.Alpha<=0.0:
		BladeSword.Alpha=1.0
		bladesword.Alpha=0.0
		bladesword.RemoveFromList("Timer30")
		bladesword.SubscribeToList("Pin")

def EnciendeEspadaParaMorphing(ent_name, time):
	bladesword.SelfIlum=bladesword.SelfIlum+0.2/(2.0*30.0)
	if bladesword.SelfIlum>=0.2:
		bladesword.SelfIlum=0.2
		bladesword.TimerFunc=MorphingEspada

def FadingCoolDeUnaAOtra():
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ParticulasFadingCool, ())
	bladesword.SelfIlum=0.0
	x, y, z = bladesword.Position
	ld=Bladex.CreateEntity("LuzDiosa", "Entity Spot", x, y-260.0, z+150.0)
	ld.Color=90, 190, 255
	ld.Intensity=0.0
	ld.Precission=0.01
	ld.Visible=0
	ld.CastShadows=0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.SpotIntensityVariation, ("LuzDiosa", 0.0, 4.0, 1.0))
	Bladex.AddScheduledFunc(Bladex.GetTime()+2.5, AuxFuncs.SpotIntensityVariation, ("LuzDiosa", 4.0, 0.0, 2.5))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.1, Bladex.GetEntity("LuzDiosa").SubscribeToList, ("Pin",))
	bladesword.TimerFunc=EnciendeEspadaParaMorphing
	bladesword.SubscribeToList("Timer30")

def ApagaLuzReaparicionEspada():
	AuxFuncs.SpotIntensityVariation("LuzReaparicionBladeSword", 4.0, 0.0, 1.75)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.8, Bladex.GetEntity("LuzReaparicionBladeSword").SubscribeToList, ("Pin",))

def ApareceEspadaMagica(EntityName, EventName):
	sndreapesp.Position=BladeSword.Position
	sndreapesp.PlaySound(0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+12.0, EnciendeLuzVerde, ())
	BladeSword.Alpha = 0.0
	bladeswordadd.Position=0,0,0
	bladeswordadd.Orientation = BladeSword.Orientation
	BladeSword.Link(bladeswordadd)
	inv = Bladex.GetEntity("Player1").GetInventory()
	# Here increase the number of weapons carryable by 1
	inv.maxWeapons= 5
	Actions.TakeObject("Player1", BladeSword.Name)

	inv.LinkRightHand(BladeSword.Name)
	#inv.LinkBack("None")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.FadeObject, (bladeswordadd.Name, 0.0, 0.98, 3.9))
	Bladex.AddScheduledFunc(Bladex.GetTime()+4.9, AuxFuncs.FadeObject, (bladeswordadd.Name, 0.98, 0.0, 1.0, 1))
	Bladex.AddScheduledFunc(Bladex.GetTime()+5.0, AuxFuncs.FadeObject, (BladeSword.Name, 0.0, 1.0, 1.0))
	lbs=Bladex.CreateEntity("LuzReaparicionBladeSword", "Entity Spot", 0, 0, 0)
	lbs.Color=90, 190, 255
	lbs.Intensity=0
	lbs.Precission=0.01
	lbs.Visible=0
	lbs.Flick=0
	lbs.CastShadows=0
	BladeSword.Link(lbs)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.SpotIntensityVariation, ("LuzReaparicionBladeSword", 0.0, 4.0, 2.5))
	Bladex.AddScheduledFunc(Bladex.GetTime()+3.5, ApagaLuzReaparicionEspada, ())
	wps=Bladex.CreateEntity("WPS", "Entity Particle System Dobj", 0, 0, 0)
	wps.ObjectName=bladeswordadd.Name
	wps.ParticleType="MediumBlueEnergyCon"
	wps.FollowFactor=1.0
	wps.PPS=600
	wps.YGravity=0.0
	wps.Friction=0.0
	wps.Velocity=0.0, 0.0, 0.0
	wps.RandomVelocity=-2.0
	wps.NormalVelocity=-2.0
	wps.Time2Live=60
	wps.DeathTime=Bladex.GetTime()+3.0

def ApagaEspada(ent_name, time):
	a=Bladex.GetEntity(ent_name)
	a.Data.alpha=max(0.0, a.Data.alpha+a.Data.alphavar)
	a.SetAuraParams(10, a.Data.alpha, 1, 0, 0, 1)
	if ent_name=="AuraBladeSword":
		intens=a.Data.alpha*2.0
		bladesword.SelfIlum=a.Data.alpha/4.0
	else:
		intens=a.Data.alpha*8.0
	a.Data.luz.Intensity=intens
	if a.Data.alpha==0.0:
		a.RemoveFromList("Timer30")
		a.TimerFunc=""
		a.Data.luz.SubscribeToList("Pin")
		a.SubscribeToList("Pin")

def EnciendeEspada(ent_name, time):
	a=Bladex.GetEntity(ent_name)
	a.Data.alpha=min(1.0, a.Data.alpha+a.Data.alphavar)
	a.SetAuraParams(10, a.Data.alpha, 1, 0, 0, 1)
	if ent_name=="AuraBladeSword":
		intens=a.Data.alpha*2.0
		bladesword.SelfIlum=a.Data.alpha/4.0
	else:
		intens=a.Data.alpha*8.0
	a.Data.luz.Intensity=intens
	if a.Data.alpha==1.0:
		a.RemoveFromList("Timer30")
		a.TimerFunc=""

def CambiaChispas(ch, a):
	ch.Time2Live=30
	ch.ParticleType="BlueEnergyDis"
	ch.PPS=300
	ch.YGravity=200
	a.Data.alphavar=-1.0/(3.0*30.0)
	a.TimerFunc=ApagaEspada
	a.SubscribeToList("Timer30")
	sndsacaespada.PlaySound(0)
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, FadeAndScale, ("OndaExp", (94355.2677885, -3008.18632875, 172034.430763), 0.9, 0.0, -1, 0.1, 0.9, -1, 0.6, 1.0, 2))

def ChispasTakeSwordBlade(chngtime, dthtime):
	ch=Bladex.CreateEntity("Ch","Entity Particle System Dobj",0,0,0)
	ch.ObjectName=chbladesword.Name
	ch.ParticleType="BlueEnergyCon"
	ch.YGravity=100
	ch.RandomVelocity=1
	ch.Velocity=0.0,0.0,0.0
	ch.PPS=1000
	ch.Time2Live=40
	ch.DeathTime=Bladex.GetTime()+dthtime

	r, g, b = 0.2, 0.4, 1.0
	a=Bladex.CreateEntity("AuraBladeSword", "Entity Aura", 0, 0, 0)
	a.SetAuraParams(10, 0, 1, 0, 0, 1)
	a.SetAuraGradient(2, r, g, b, 0.8, 0.0, r, g, b, 0.0, 0.8)
	bladesword.Link(a)
	a.SetAuraActive(1)

	la=Bladex.CreateEntity("LuzAuraBladeSword", "Entity Spot", 0, 0, 0)
	la.Color=50, 160, 255
	la.Intensity=0
	la.Precission=0.03125
	la.Visible=0
	la.Flick=0
	la.CastShadows=0
	bladesword.Link(la)

	InitDataField.Initialise(a)
	a.Data.luz=la
	a.Data.alpha=0.05
	a.Data.alphavar=1.0/(1.0*30.0)
	a.TimerFunc=EnciendeEspada
	a.SubscribeToList("Timer30")

	Bladex.AddScheduledFunc(Bladex.GetTime()+chngtime, CambiaChispas, (ch, a))

def PickUpSwordBladeTrue(EntityName, EventName):
	# Here increase the number of weapons carryable by 1
	inv = Bladex.GetEntity("Player1").GetInventory()
	inv.maxWeapons= 5
	Actions.TakeObject("Player1", bladesword.Name)
	inv.LinkRightHand(bladesword.Name)
	#inv.LinkBack("None")
	ChispasTakeSwordBlade(10.25, 11.05)
	#print bladesword.Position
	#print bladesword.Orientation

def ApagaExplosionEspada(a):
	a.Data.alphavar=-1.0/(10.0*30.0)
	a.TimerFunc=ApagaEspada
	a.SubscribeToList("Timer30")

def OndaExpansivaEspadaVar(ent_name, time):
	oe=Bladex.GetEntity(ent_name)
	oe.Data.alpha=max(0.0, oe.Data.alpha-oe.Data.alphavar)
	oe.Data.size=oe.Data.size+oe.Data.alpha*12.0
	oe.SetAuraParams(oe.Data.size, oe.Data.alpha, 1, 0, 0, 1)
	if oe.Data.alpha==0.0:
		oe.RemoveFromList("Timer30")
		oe.TimerFunc=""
		oe.SubscribeToList("Pin")

def OndaExpansivaEspada():
	r, g, b = 0.3, 0.5, 1.0
	oe=Bladex.CreateEntity("AuraOndaExpBladeSwordA", "Entity Aura", 0, 0, 0)
	oe.SetAuraParams(0, 1, 1, 0, 0, 1)
	oe.SetAuraGradient(2, r, g, b, 1.0, 0.0, r, g, b, 0.0, 0.4)
	oe.SetAuraGradient(1, r, g, b, 0.0, 0.4, r, g, b, 0.0, 1.0)
	bladeswordA.Link(oe)
	oe.SetAuraActive(1)

	InitDataField.Initialise(oe)
	oe.Data.alpha=1.0
	oe.Data.alphavar=1.0/(1.5*30.0)
	oe.Data.size=0.0
	oe.TimerFunc=OndaExpansivaEspadaVar
	oe.SubscribeToList("Timer30")

def ExplosionEspada():
	sndflash.Position=bladeswordA.Position
	sndflash.PlaySound(0)
	r, g, b = 0.3, 0.5, 1.0
	a=Bladex.CreateEntity("AuraBladeSwordA", "Entity Aura", 0, 0, 0)
	a.SetAuraParams(10, 0, 1, 0, 0, 1)
	a.SetAuraGradient(2, r, g, b, 0.8, 0.0, r, g, b, 0.0, 0.8)
	bladeswordA.Link(a)
	a.SetAuraActive(1)

	la=Bladex.CreateEntity("LuzAuraBladeSwordA", "Entity Spot", 0, 0, 0)
	la.Color=60, 170, 255
	la.Intensity=0
	la.Precission=0.03125
	la.Visible=0
	la.Flick=0
	la.CastShadows=0
	bladeswordA.Link(la)

	InitDataField.Initialise(a)
	a.Data.luz=la
	a.Data.alpha=0.05
	a.Data.alphavar=1.0/(0.25*30.0)
	a.TimerFunc=EnciendeEspada
	a.SubscribeToList("Timer30")

	x1, y1, z1=bladeswordA.Rel2AbsPoint(0.0, 0.0, 782.0)
	x2, y2, z2=bladeswordA.Rel2AbsPoint(0.0, 0.0, -782.0)
	ray1=Bladex.CreateEntity("Ray1", "Entity ElectricBolt", x1, y1, z1)
	ray1.Position=x1, y1, z1
	ray1.Target=x2, y2, z2
	ray1.MaxAmplitude=300
	ray1.MinSectorLength=10000
	ray1.Damage=0
	ray1.Active=1
	ray2=Bladex.CreateEntity("Ray2", "Entity ElectricBolt", x1, y1, z1)
	ray2.Position=x1, y1, z1
	ray2.Target=x2, y2, z2
	ray2.MaxAmplitude=200
	ray2.MinSectorLength=10000
	ray2.Damage=0
	ray2.Active=1
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.25, ray1.SubscribeToList, ("Pin",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ray2.SubscribeToList, ("Pin",))

	OndaExpansivaEspada()

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, ApagaExplosionEspada, (a,))

def CambiazoPorActorTrue(EntityName, EventName):
	#pdb.set_trace()
	char = Bladex.GetEntity("Player1")
	bls  = Bladex.GetEntity("BladeSword")
	inv  = char.GetInventory()
	if EventName=="ReleaseBladeSword":
		inv.LinkRightHand("None")
		#inv.LinkBack("None")
		Actions.RemoveFromInventory(char, bls, "")
	bladeswordA.Alpha=1.0
	bls.RemoveFromWorld()
	ExplosionEspada()



#######################################
#     Funciones comunes tablillas     #
#######################################


def AuraTablillaSizeVariation(ent_name, time):
	atabl=Bladex.GetEntity(ent_name)
	atabl.Data.size=atabl.Data.size+atabl.Data.sizevar
	atabl.Data.alpha=atabl.Data.alpha+atabl.Data.alphavar
	if atabl.Data.size>10 and atabl.Data.size<500:
		atabl.SetAuraParams(atabl.Data.size, atabl.Data.alpha, 1, 0, 0, 1)
	elif atabl.Data.size>=500:
		atabl.Data.sizevar=-500.0/(1.25*30.0)
		atabl.Data.alphavar=-0.5/(1.25*30.0)
	else:
		atabl.RemoveFromList("Timer30")
		atabl.TimerFunc=""
		atabl.SubscribeToList("Pin")

def MueveTablilla(e_name, time):
	global Tablist

	timex = Bladex.GetTime()-Tablist[e_name][0]
	part = Bladex.GetEntity(e_name)
	atabl=Bladex.GetEntity("Aura"+e_name)

	if( Tablist[e_name][2] <= timex ):
		if( Tablist[e_name][2]+2.0 <= timex ):
			part.TimerFunc=""
			part.RemoveFromList("Timer30")
			fx=Bladex.GetEntity(e_name+"PS")
			fx.RandomVelocity=8
			fx.PPS=600
			fx.DeathTime=Bladex.GetTime()+0.5
			SegundoIncrementoIntensidadHalo(part.Name)
			InitDataField.Initialise(atabl)
			atabl.Data.size=100
			atabl.Data.sizevar=400.0/(0.5*30.0)
			atabl.Data.alpha=1.0
			atabl.Data.alphavar=0.0
			atabl.TimerFunc=AuraTablillaSizeVariation
			atabl.SubscribeToList("Timer30")
		else:
			part.Move(0,Tablist[e_name][4]/(2.0*30.0),0)
			part.Alpha=1.0
			part.RotateRel(0,0,0,1,0,0,0.16/(2.0*30.0))
	else:
		part.Position=Traps_C.GetMaxPathPosition(Tablist[e_name][1],timex)
		alfa=timex/Tablist[e_name][2]
		part.Alpha=alfa
		atabl.SetAuraParams(100, alfa, 1, 0, 0, 1)
		part.RotateRel(0,0,0,0,1,0,Tablist[e_name][3]/(Tablist[e_name][2]*30.0))
		if part.Scale<1.0:
			part.Scale=part.Scale+1.0/60.0


def DecrementoIntensidadHalo(tablix_name):
	AuxFuncs.FadeObject("ConoHalo"+tablix_name, 0.7, 0.0, 1.0, 1)


def SegundoIncrementoIntensidadHalo(tablix_name):
	sndluztabl.PlaySound(0)
	AuxFuncs.FadeObject("ConoHalo"+tablix_name, 0.2, 0.7, 0.25)
	Bladex.GetEntity("BaseConoHalo"+tablix_name).SubscribeToList("Pin")
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.3, DecrementoIntensidadHalo, (tablix_name,))


def PrimerIncrementoIntensidadHalo(tablix_name):
	AuxFuncs.FadeObject("ConoHalo"+tablix_name, 0.0, 0.2, 6.0)
	AuxFuncs.FadeObject("BaseConoHalo"+tablix_name, 0.0, 0.5, 6.0)


def CambiaPPS(ps_name, newPPS):
	ps=Bladex.GetEntity(ps_name)
	ps.PPS=newPPS


def AuraTablilla(tabl_name):
	r, g, b = 0.2, 0.4, 1.0
	tabl=Bladex.GetEntity(tabl_name)
	atabl=Bladex.CreateEntity("Aura"+tabl_name, "Entity Aura", 0, 0, 0)
	atabl.SetAuraParams(100, 0, 1, 0, 0, 1)
	atabl.SetAuraGradient(2, r, g, b, 1.0, 0.0, r, g, b, 0.0, 0.4)
	tabl.Link(atabl)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, atabl.SetAuraActive, (1,))

def LanzaTablilla(CameraName,nFrames,TabliObj,ang,desp):
	global Tablist
	global lista_tablillas_cambia_zbuffer

	inv = Bladex.GetEntity("Player1").GetInventory()
	inv.RemoveTablet(TabliObj)
	tablix = Bladex.GetEntity(TabliObj+"X")
	tablix.Position = char.Position
	tablix.Orientation=1.0, 0.0, 0.0, 0.0
	tablix.RasterMode="Read"
	tablix.Scale = 0.1
	tablix.Alpha = 0.01

	lista_tablillas_cambia_zbuffer.append(tablix.Name)

	AuraTablilla(tablix.Name)

	parts=Bladex.CreateEntity(TabliObj+"XPS","Entity Particle System Dobj",0,0,0)
	parts.ObjectName=tablix.Name
	parts.ParticleType="BlueEnergyDis"
	parts.YGravity=0
	parts.RandomVelocity=4
	parts.Velocity=0.0,0.0,0.0
	parts.Time2Live=30
	parts.PPS=300

	Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, CambiaPPS, (parts.Name, 100))

	Tablist[tablix.Name] = [Bladex.GetTime(),Traps_C.LoadMaxPath(CameraName,0,nFrames),nFrames/20.0,ang,desp]
	tablix.SubscribeToList("Timer30")
	tablix.TimerFunc = MueveTablilla

	Bladex.AddScheduledFunc(Bladex.GetTime()+4.0, PrimerIncrementoIntensidadHalo, (TabliObj+"X",))

def FullZBufferTablillas():
	global lista_tablillas_cambia_zbuffer
	for tabl_name in lista_tablillas_cambia_zbuffer:
		tabl=Bladex.GetEntity(tabl_name)
		tabl.RasterMode="Full"
	lista_tablillas_cambia_zbuffer=[]

def GetTabletInfo(n):
	global TabliState

	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()

	if not GotoMapVars.PlacedTablets[n]:
		if inv.GetTablet("Tablilla"+`n+1`):
			TabliState[n] = 1
		else:
			TabliState[n] = 0
	else:
		Bladex.GetEntity("Tablilla"+`n+1`+"X").PutToWorld()
		TabliState[n] = 2



def GetTabliStates():
	GetTabletInfo(0)
	GetTabletInfo(1)
	GetTabletInfo(2)
	GetTabletInfo(3)
	GetTabletInfo(4)
	GetTabletInfo(5)

def AuraJugadorDejaTablillaVariation(ent_name, time):
	global aura_size_jugdejatabl
	global aura_var_jugdejatabl
	aura_size_jugdejatabl=aura_size_jugdejatabl+aura_var_jugdejatabl
	aplayer=Bladex.GetEntity(ent_name)
	if aura_size_jugdejatabl>2 and aura_size_jugdejatabl<90:
		aplayer.SetAuraParams(60, min(1.0, aura_size_jugdejatabl/60.0), 1, 0, 0, 1)
	elif aura_size_jugdejatabl>=90:
		aura_var_jugdejatabl=-1.5
	else:
		aura_size_jugdejatabl=2
		aura_var_jugdejatabl=2
		aplayer.RemoveFromList("Timer30")
		aplayer.TimerFunc=""
		aplayer.SubscribeToList("Pin")

def AuraJugadorDejaTablilla():
	char=Bladex.GetEntity("Player1")
	r1, g1, b1 = 0.4, 0.6, 1.0
	r2, g2, b2 = 0.1, 0.2, 1.0
	aplayer=Bladex.CreateEntity("AuraJugadorDejaTablilla", "Entity Aura", 0, 0, 0)
	aplayer.SetAuraParams(60, 1, 1, 0, 0, 1)
	aplayer.SetAuraGradient(1, r1, g1, b1, 0.5, 0.0, r2, g2, b2, 0.0, 0.8)
	char.Link(aplayer)
	aplayer.SetAuraActive(1)
	aplayer.TimerFunc=AuraJugadorDejaTablillaVariation
	aplayer.SubscribeToList("Timer30")
	psaplayer=Bladex.CreateEntity("PSAuraJugadorDejaTablilla","Entity Particle System Dperson",0,0,0)
	psaplayer.PersonName="Player1"
	psaplayer.ParticleType="BlueEnergyDis2"
	psaplayer.FollowFactor=0.0
	psaplayer.YGravity=0
	psaplayer.RandomVelocity=2.0
	psaplayer.NormalVelocity=2.0
	psaplayer.Velocity=0.0,0.0,0.0
	psaplayer.Time2Live=30
	psaplayer.PPS=600
	psaplayer.DeathTime=Bladex.GetTime()+2.25

	snddejatabl.Position=char.Position
	snddejatabl.PlaySound(0)

def CalculaPosicionTablillas():
	global TabliState

	s = "posi = ["
	for i in range(6):
		t = Bladex.GetEntity("Tablilla"+`i+1`+"X")
		s = s + "("+`t.Position`+","+`t.Orientation`+"),"
	print s+"]"



def LanzaTodasLasTablillas():
	global TabliState

	if(TabliState[0] == 1):
		LanzaTablilla("Palacio_Camera01.cam",200,"Tablilla1",2.06,695.0)
		TabliState[0] = 2

	if(TabliState[1] == 1):
		LanzaTablilla("Palacio_Camera02.cam",200,"Tablilla2",1.06,715.0)
		TabliState[1] = 2

	if(TabliState[2] == 1):
		LanzaTablilla("Palacio_Camera03.cam",200,"Tablilla3",0.0,693.0)
		TabliState[2] = 2

	if(TabliState[3] == 1):
		LanzaTablilla("Palacio_Camera04.cam",200,"Tablilla4",-1.06,732.0)
		TabliState[3] = 2

	if(TabliState[4] == 1):
		LanzaTablilla("Palacio_Camera05.cam",200,"Tablilla5",-2.06,717.0)
		TabliState[4] = 2

	if(TabliState[5] == 1):
		LanzaTablilla("Palacio_Camera06.cam",200,"Tablilla6",3.14,787.0)
		TabliState[5] = 2

#######################################
#     Funciones comunes de camara     #
#######################################

def CameraFinaleX(Camera,frame):
	global TabliState
	ScriptSkip.SkipScriptEnd()
	for i in range(len(TabliState)):
		if TabliState[i]==2:
			GotoMapVars.PlacedTablets[i] = 1
	#cam=Bladex.GetEntity("Camera") # Esto
	#cam.SetPersonView("Player1") # Esto
	#Bladex.SetListenerPosition(1) # Esto
	#Scorer.SetVisible(1) # Esto
	#SectorInicial.OnEnter = ComienzaLaHistoria # Esto
	#return # Esto
	GotoMapVars.EndOfLevel()

def TieneLaSagradaBlade(PerName = "Player1"):
	inv = Bladex.GetEntity(PerName).GetInventory()
	for i in range(inv.nWeapons):
		if Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2":
			return 1
	return 0

def FinalFadeOut(Camera,frame):
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, AuxFuncs.FadeTo,(1.0, 20.0))
	#return # Esto
	GenFX.PersonMagicallyDisappearing()

def XQTeCamera(Camera,frame):
	global CameraSecuence
	global iCameraSecuence

	cam = Bladex.GetEntity("Camera")
	#print CameraSecuence[iCameraSecuence][0]
	cam.SetMaxCamera( CameraSecuence[iCameraSecuence][0], CameraSecuence[iCameraSecuence][1], CameraSecuence[iCameraSecuence][2] )
	if(CameraSecuence[iCameraSecuence][3] != ""):
		CameraSecuence[iCameraSecuence][3]()
	iCameraSecuence = iCameraSecuence + 1
	if(len(CameraSecuence)>iCameraSecuence):
		cam.AddCameraEvent(-1,XQTeCamera)
	else:
		cam.AddCameraEvent(CameraSecuence[iCameraSecuence-1][2]-CameraSecuence[iCameraSecuence-1][1]-40,FinalFadeOut)
		cam.AddCameraEvent(-1,CameraFinaleX)


def RunCameraSecuence(l):
	global CameraSecuence
	global iCameraSecuence

	CameraSecuence = l
	iCameraSecuence = 0
	XQTeCamera(0,0)



####################################################################################################
#                            ESCENA 1 : LLEGA CON TODAS LAS TABLILLAS                              #
####################################################################################################



def EscenaSuper():
	ScriptSkip.SkipScriptStart("EscenaSuperEsp")
	char.GoTo(94461,-3101,176364)
	char.RouteEndedFunc = LanzaEscenaX
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)

def LanzaEscenaX(Entity):
	Actions.FreeBothHands(Entity)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, IniciaGranEscena,())


def IniciaGranEscena():
	global TabliState
	global BladeReady
	musicaytespadacontodastablillas()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("coger_blade")
	if   char.Kind[0]=="K": ####  CABALLERO  ####
		char.Position = 94462,-3101,176364
	elif char.Kind[0]=="D": ####    ENANO    ####
		char.Position = 94461, -2867 ,176364
	elif char.Kind[0]=="A": ####   AMAZONA   ####
		char.Position = 94461, -3100, 176218
	elif char.Kind[0]=="B": ####   BARBARO   ####
		char.Position = 94461, -3277, 176474

	char.Angle    = 3.14159
	char.AddAnmEventFunc("TakeBladeSword", PickUpSwordBladeTrue)
	char.AddAnmEventFunc("ReleaseBladeSword", CambiazoPorActorTrue)
	char.AddAnmEventFunc("PrevFirstImpact", PrimerImpacto)
	char.AddAnmEventFunc("EndImpact", ApagaPoder)
	char.AddAnmEventFunc("AppearBladeSword", ApareceEspadaMagica)
	bladesword.Position = 94355.2677885, -3148.18632875, 172034.430763
	bladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
	Bladex.SetListenerPosition(2)
	AuraJugadorDejaTablilla()
	RunCameraSecuence(CamaraTodasLasTablillas)
	bladeswordA.Actor=1
	bladeswordA.Animation="Bld_vuela"
	bladeswordA.SendSectorMsgs=0
	bladeswordA.TurnOn()
	bladeswordA.Alpha=0.0
	LanzaTodasLasTablillas()
	BladeReady = 1
	### AQUI
	if char.InvLeftBack:
		Bladex.GetEntity(char.InvLeftBack).RemoveFromWorld()
	if char.InvRightBack:
		Bladex.GetEntity(char.InvRightBack).RemoveFromWorld()
	Bladex.GetEntity("Player1").GetInventory().LinkBack("None")


####################################################################################################
#                            ESCENA 2 : LLEGA CON NINGUNA  TABLILLA                                #
####################################################################################################


def EscenaHorrible():
	ScriptSkip.SkipScriptStart("EscenaHorribleEsp")
	char.GoTo(94461,-3101,176364)
	char.RouteEndedFunc = LanzaEscenaH
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)

def LanzaEscenaH(Entity):
	Actions.FreeBothHands(Entity)
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, IniciaPorqueriaDeEscena,())

def IniciaPorqueriaDeEscena():
	global BladeReady
	BladeReady = 1
	musicaytespadasinningunatablilla()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("blade_tablillas_no")
	if   char.Kind[0]=="K": ####  CABALLERO  ####
		char.Position = 94440, -3080 ,176305
	elif char.Kind[0]=="D": ####    ENANO    ####
		char.Position = 94435, -2857, 176474
	elif char.Kind[0]=="A": ####   AMAZONA   ####
		char.Position = 94456, -3078, 176173
	elif char.Kind[0]=="B": ####   BARBARO   ####
		char.Position = 94436, -3277, 176384

	char.Angle    = 3.14159
	char.AddAnmEventFunc("TakeBladeSwordNT", PickUpLaEspadaFea)
	cam = Bladex.GetEntity("Camera")
	cam.SetMaxCamera( "Palacio_Camara_blade.cam", 0, 741 )
	bladesword.Position = 94360.1039325, -3141.79042721, 172028.909751
	bladesword.Orientation = 0.0109584331512, 0.00787348393351, 0.707041442394, -0.707378804684
	Bladex.SetListenerPosition(2)
	cam.AddCameraEvent(700,FinalFadeOut)
	cam.AddCameraEvent(-1, CameraFinaleX)
	### AQUI
	if char.InvLeftBack:
		Bladex.GetEntity(char.InvLeftBack).RemoveFromWorld()
	if char.InvRightBack:
		Bladex.GetEntity(char.InvRightBack).RemoveFromWorld()
	Bladex.GetEntity("Player1").GetInventory().LinkBack("None")


def PickUpLaEspadaFea(EntityName, EventName):
	inv = Bladex.GetEntity("Player1").GetInventory()
	inv.maxWeapons= 5
	Actions.TakeObject("Player1", bladesword.Name)
	inv.LinkRightHand(bladesword.Name)
	#inv.LinkBack("None")

	if EventName=="TakeBladeSwordNT":
		chngtime=3.9
		dthtime=4.45
	else:
		chngtime=4.15
		dthtime=4.9
	ChispasTakeSwordBlade(chngtime, dthtime)
	#print bladesword.Position
	#print bladesword.Orientation

####################################################################################################
#                            ESCENA 3 : SOLO DEJA LAS TABLILLAS                                    #
####################################################################################################

def DejaTablillas():
	ScriptSkip.SkipScriptStart("EscenaSoloTablillasEsp")
	char.GoTo(94461,-3101,176364)
	char.RouteEndedFunc = LanzaEscenaT
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)

def LanzaEscenaT(Entity):
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, IniciaEscenaTablillas,())

def IniciaEscenaTablillas():
	global BladeReady
	BladeReady = 1
	musicasolotablillas()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("blade_solotablas")

	if   char.Kind[0]=="K": ####  CABALLERO  ####
		char.Position = 94420,-3101,176300
	elif char.Kind[0]=="D": ####    ENANO    ####
		char.Position = 94420,-3101,176300
	elif char.Kind[0]=="A": ####   AMAZONA   ####
		char.Position = 94420,-3101,176300
	elif char.Kind[0]=="B": ####   BARBARO   ####
		char.Position = 94420,-3101,176300

	char.SetOnFloor()

	char.Angle    = 3.14159
	Bladex.SetListenerPosition(2)
	AuraJugadorDejaTablilla()
	RunCameraSecuence(CamaraSoloTablillas)
	LanzaTodasLasTablillas()

###############################################################################################
#                            ESCENA 4 : ESPADA Y DEJA LAS TABLILLAS                           #
###############################################################################################

def EspadaDejaTablillas():
	ScriptSkip.SkipScriptStart("EscenaEspadaYTablillasEsp")
	char.GoTo(94461,-3101,176364)
	char.RouteEndedFunc = ELanzaEscenaT
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)

def ELanzaEscenaT(Entity):
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, EIniciaEscenaTablillas,())
	Actions.FreeBothHands(Entity)

def EIniciaEscenaTablillas():
	global BladeReady
	BladeReady = 1
	musicaytespadasinalgunatablilla()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("blade_faltantablillas")
	if   char.Kind[0]=="K": ####  CABALLERO  ####
		char.Position = 94462,-3102,176364
	elif char.Kind[0]=="D": ####    ENANO    ####
		char.Position = 94461,-2876,176448
	elif char.Kind[0]=="A": ####   AMAZONA   ####
		char.Position = 94461,-3093,176259
	elif char.Kind[0]=="B": ####   BARBARO   ####
		char.Position = 94461,-3256,176364

	char.Angle    = 3.14159
	char.AddAnmEventFunc("TakeBladeSwordFT", PickUpLaEspadaFea)
	bladesword.Position = 94360.1039325, -3141.79042721, 172028.909751
	bladesword.Orientation = 0.0109584331512, 0.00787348393351, 0.707041442394, -0.707378804684
	Bladex.SetListenerPosition(2)
	AuraJugadorDejaTablilla()
	RunCameraSecuence(EspadaCamaraSoloTablillas)
	LanzaTodasLasTablillas()
	### AQUI
	if char.InvLeftBack:
		Bladex.GetEntity(char.InvLeftBack).RemoveFromWorld()
	if char.InvRightBack:
		Bladex.GetEntity(char.InvRightBack).RemoveFromWorld()
	Bladex.GetEntity("Player1").GetInventory().LinkBack("None")



########################################################################################
#		   ESCENA 5 : RECIBE EL PODER DESPUES DE DAR VUELTAS POR EL MUNDO		   #
########################################################################################


def ApagaLuzVerdeYApareceTornado():
	ApagaLuzVerde()
	ApareceTornado()

def PowerMaker():
	ScriptSkip.SkipScriptStart("EscenaPowerEsp")
	char.GoTo(94461,-3101,176364)
	char.RouteEndedFunc = PowerBladeStart
	#Bladex.DeactivateInput()
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)
	#bladesword.Position = 94375,-3203,172000

def PowerBladeStart(Entity):
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, StartPowerAct,())
	Actions.FreeBothHands(Entity)

def StartPowerAct():
	global BladeReady
	musicaytsolopoderconrestotablillas()
	char.SetTmpAnmFlags(1,1,1,0,5,1,0)
	char.LaunchAnmType("powerblade")
	if   char.Kind[0]=="K": ####  CABALLERO  ####
		char.Position = 94462, -3101, 176364
	elif char.Kind[0]=="D": ####    ENANO    ####
		char.Position = 94461, -2876, 176493
	elif char.Kind[0]=="A": ####   AMAZONA   ####
		char.Position = 94345, -3101, 176364
	elif char.Kind[0]=="B": ####   BARBARO   ####
		char.Position = 94461, -3189, 176488

	char.Angle    = 3.14159
	char.AddAnmEventFunc("ReallocateBladeSword", RecolocaBladeSword)
	char.AddAnmEventFunc("ReleaseBladeSwordLater", CambiazoPorActorTrue)
	char.AddAnmEventFunc("PrevFirstImpact", PrimerImpacto)
	char.AddAnmEventFunc("EndImpact", ApagaPoder)
	char.AddAnmEventFunc("AppearBladeSword", ApareceEspadaMagica)
	Bladex.SetListenerPosition(2)
	AuraJugadorDejaTablilla()
	RunCameraSecuence(CamaraSuperPoder)
	bladeswordA.Actor=1
	bladeswordA.Animation="Bld_vuela4"
	bladeswordA.SendSectorMsgs=0
	bladeswordA.TurnOn()
	bladeswordA.Alpha=0.0
	LanzaTodasLasTablillas()
	### AQUI
	if char.InvLeftBack:
		Bladex.GetEntity(char.InvLeftBack).RemoveFromWorld()
	if char.InvRightBack:
		Bladex.GetEntity(char.InvRightBack).RemoveFromWorld()
	Bladex.GetEntity("Player1").GetInventory().LinkBack("None")


def SacaDeEspaldaEInventario():
	char = Bladex.GetEntity("Player1")
	bls  = Bladex.GetEntity("BladeSword")
	inv  = char.GetInventory()
	if char.InvLeftBack:
		Bladex.GetEntity(char.InvLeftBack).Alpha=1.0
	#inv.LinkBack("None")
	Actions.RemoveFromInventory(char, bls, "")

def SacaDeInventario():
	char = Bladex.GetEntity("Player1")
	bls  = Bladex.GetEntity("BladeSword")
	Actions.RemoveFromInventory(char, bls, "")

def ContinuaRecolocacion(psbs):
	psbs.DeathTime=Bladex.GetTime()+1.0/60.0
	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, AuxFuncs.FadeObject, ("BladeSword", 0.0, 1.0, 1.0))
	Bladex.GetEntity("BladeSword").Unlink(bladeswordadd)

def SacaDeCuerpo():
	char = Bladex.GetEntity("Player1")
	bls  = Bladex.GetEntity("BladeSword")
	bls.Alpha = 0.0
	x, y, z = bls.Position = char.Position
	bladeswordadd.Position=0,0,0
	bladeswordadd.Orientation = bls.Orientation = 0.510729670525, -0.585062086582, -0.252546846867, 0.577128827572
	bls.Link(bladeswordadd)
	psbs=Bladex.CreateEntity("PSBladeSword","Entity Particle System Dobj", 0, 0, 0)
	psbs.ObjectName="BladeSwordAdd"
	psbs.ParticleType="BlueEnergyDis2"
	psbs.YGravity=0
	psbs.RandomVelocity=2
	psbs.NormalVelocity=2
	psbs.Velocity=0.0,0.0,0.0
	psbs.Time2Live=30
	psbs.PPS=600
	blsdin=Objects.CreateDinamicObject("BladeSword")
	blsdin.Timer="Timer30"
	Objects.DisplaceObjectFromTo(blsdin, (x, y, z), (94052.251008, -4033.91838564, 172999.071657), 1000, 800, "", "", "", "", (), ContinuaRecolocacion, (psbs,))

def RecolocaBladeSword(EntityName, EventName):
	char = Bladex.GetEntity("Player1")
	if (char.InvRightBack and char.InvRightBack=="BladeSword"):
		ps1bs=Bladex.CreateEntity("PS1BladeSword","Entity Particle System Dobj", 0, 0, 0)
		ps1bs.ObjectName="BladeSword"
		ps1bs.ParticleType="BlueEnergyDis"
		ps1bs.YGravity=0
		ps1bs.RandomVelocity=2
		ps1bs.NormalVelocity=2
		ps1bs.Velocity=0.0,0.0,0.0
		ps1bs.Time2Live=30
		ps1bs.PPS=200
		ps1bs.DeathTime=Bladex.GetTime()+1.0
		AuxFuncs.FadeObject(char.InvRightBack, 1.0, 0.0, 1.5)
		if char.InvLeftBack:
			AuxFuncs.FadeObject(char.InvLeftBack, 1.0, 0.0, 1.5)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.6, SacaDeEspaldaEInventario, ())
	else:
		SacaDeInventario()
	Bladex.AddScheduledFunc(Bladex.GetTime()+1.7, SacaDeCuerpo, ())



####################################################################################################
#                                    Selector de Escenas                                           #
####################################################################################################


def ComienzaLaHistoria(sectorindex,entityname):
	global TabliState
	global BladeReady

	if entityname == "Player1":
		GetTabliStates()
		Carried = 0
		Ready   = 0

		for i in range(6):
			if(TabliState[i]==1):
				Carried = Carried + 1
			elif(TabliState[i]==2):
				Ready = Ready + 1

		if(Carried+Ready == 0) & (BladeReady==0):
			EscenaHorrible() # Solo Espaducha
		elif(Carried == 6) & (BladeReady==0):
			EscenaSuper()            # Espada y todas las tablillas
		elif(Carried+Ready < 6) & (Carried > 0) & (BladeReady==1):
			DejaTablillas()          # deja algunas tablillas
		elif(Carried+Ready < 6) & (Carried > 0) & (BladeReady==0):
			EspadaDejaTablillas()    # deja algunas tablillas
		elif(Carried+Ready >= 6) & (Carried > 0) & (BladeReady==1):
			PowerMaker()            # deja algunas tablillas
		else:
			return

		SectorInicial.OnEnter = ""

###########################################################
#     Creacion de objetos, carga de animaciones, etc.     #
###########################################################

def CreaEspadas():
	global bladesword
	global bladeswordA
	global BladeSword
	global bladeswordadd

	bladesword = Bladex.GetEntity("BladeSword")
	if not bladesword:
		if char.Kind[0] == "B":
			bladesword = Bladex.CreateEntity("BladeSword","BladeSwordBarbarian",94355.2677885, -3148.18632875, 172034.430763)
		else:
			bladesword = Bladex.CreateEntity("BladeSword","BladeSword",94355.2677885, -3148.18632875, 172034.430763)

		bladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
		bladesword.Static=1
		bladesword.Weapon=1
		#ItemTypes.ItemDefaultFuncs (bladesword)
		Reference.EntitiesSelectionData[bladesword.Name]=(0,0,"")

	bladeswordA = Bladex.CreateEntity("BladeSword1","BladeSword",94052.251008, -4033.91838564, 172999.071657)
	bladeswordA.Orientation = 0.707107,0.707107,0.000000,0.000000
	bladeswordA.Static=1
	bladeswordA.Alpha=0.0
	Reference.EntitiesSelectionData[bladeswordA.Name]=(0,0,"")
	if char.Kind[0] == "B":
		BladeSword = Bladex.CreateEntity("BladeSword2","BladeSword2Barbarian",94605.0898438, -20733.0249825, 172887.026402)
	else:
		BladeSword = Bladex.CreateEntity("BladeSword2","BladeSword2",94605.0898438, -20733.0249825, 172887.026402)

	BladeSword.Orientation = 0.707107,0.707107,0.000000,0.000000
	BladeSword.Static=1
	BladeSword.Weapon=1
	BladeSword.Alpha=0.0
	#ItemTypes.ItemDefaultFuncs (BladeSword)
	Reference.EntitiesSelectionData[BladeSword.Name]=(0,0,"")

	bladeswordadd = Bladex.CreateEntity("BladeSwordAdd","BladeSword2Poly", 0, 0, 0)
	bladeswordadd.Orientation = 0.707107,0.707107,0.000000,0.000000
	bladeswordadd.Static=1
	bladeswordadd.Alpha=0.0
	bladeswordadd.RasterMode="AdditiveAlpha"
	bladeswordadd.RasterMode="Read"
	bladeswordadd.SelfIlum=1.0
	Reference.EntitiesSelectionData[bladeswordadd.Name]=(0,0,"")

def CreaObjetosEnergeticos():
	global chbladesword
	global ondaexp
	global ondaexp1
	global ondaexp2
	global cilar
	global cilab
	global cilgo
	global cilardin
	global cilabdin
	global cilgodin
	global luzimp
	chbladesword = Bladex.CreateEntity("ChBladeSword","ChispasBladeSword",0,0,0)
	chbladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
	chbladesword.Static=1
	chbladesword.Scale=1.1
	chbladesword.CastShadows=0
	chbladesword.Alpha=0.0
	bladesword.Link(chbladesword)
	ondaexp=Bladex.CreateEntity("OndaExp", "OndaExpansiva", 94355.2677885, -3008.18632875, 172034.430763)
	ondaexp1=Bladex.CreateEntity("OndaExp1", "OndaExpansiva", 94355.2677885, -3008.18632875, 172034.430763)
	ondaexp2=Bladex.CreateEntity("OndaExp2", "OndaExpansiva", 94355.2677885, -3008.18632875, 172034.430763)
	cilar=Bladex.CreateEntity("CilindroArriba", "LuzDivinaFina", 94375, -19500, 172000)
	cilab=Bladex.CreateEntity("CilindroAbajo", "LuzDivinaFina", 94375, -19500, 172000)
	cilgo=Bladex.CreateEntity("CilindroGordo", "LuzDivinaGorda", 94375, -11000, 172000)
	ondaexp.Orientation=ondaexp1.Orientation=ondaexp2.Orientation=cilar.Orientation=cilab.Orientation=cilgo.Orientation=0.707107,0.707107,0.000000,0.000000
	ondaexp.CastShadows=ondaexp1.CastShadows=ondaexp2.CastShadows=cilar.CastShadows=cilab.CastShadows=cilgo.CastShadows=0
	ondaexp.SelfIlum=ondaexp1.SelfIlum=ondaexp2.SelfIlum=cilar.SelfIlum=cilab.SelfIlum=cilgo.SelfIlum=1
	ondaexp.RasterMode=ondaexp1.RasterMode=ondaexp2.RasterMode=cilar.RasterMode=cilab.RasterMode=cilgo.RasterMode="AdditiveAlpha"
	ondaexp.RasterMode=ondaexp1.RasterMode=ondaexp2.RasterMode=cilar.RasterMode=cilab.RasterMode=cilgo.RasterMode="Read"
	ondaexp.Alpha=ondaexp1.Alpha=ondaexp2.Alpha=cilar.Alpha=cilab.Alpha=cilgo.Alpha=0.0
	cilardin=Objects.CreateDinamicObject(cilar.Name)
	cilabdin=Objects.CreateDinamicObject(cilab.Name)
	cilgodin=Objects.CreateDinamicObject(cilgo.Name)
	cilardin.Timer=cilabdin.Timer=cilgodin.Timer="Timer30"
	luzimp=Bladex.CreateEntity("LuzImpacto", "Entity Spot", 0, 0, 0)
	luzimp.Color=60, 170, 255
	luzimp.Intensity=0.0
	luzimp.Precission=0.06
	luzimp.Visible=0
	luzimp.CastShadows=0
	genleng=Bladex.CreateEntity("GeneradorLenguas", "Helice", 0, 0, 0)
	genleng.Scale=2.0
	genleng.Orientation=0.707107,0.707107,0.000000,0.000000
	genleng.CastShadows=0
	genleng.Alpha=0.0
	genlengdin=Objects.CreateDinamicObject(genleng.Name)
	genlengdin.Timer="Timer30"
	nv=Bladex.CreateEntity("NucleoVortice", "SemiBolaRayos", 0, 0, 0)
	nv.Scale=1.0
	nv.Orientation=-0.707107,0.707107,0.000000,0.000000
	nv.Alpha=0.0
	nv.CastShadows=0

def CreaTablillasX():
	global TabliState

	posi = [((92650.03125, -2377.51391602, 173149.53125),(0.51610326767, 0.041376568377, 0.852790176868, -0.06836912781)),((92596.0390625, -2389.875, 171159.5),(0.860936462879, 0.069022230804, 0.502396285534, -0.0402776673436)),((94472.7578125, -2370.47631836, 169868.5625),(0.996801733971, 0.0799146965146, 0.0, 0.0)),((96278.1484375, -2372.875, 171162.46875),(0.860047578812, 0.0689509660006, -0.503916501999, 0.040399543941)),((96224.15625, -2355.51391602, 173152.5),(0.51610326767, 0.041376568377, -0.852790176868, 0.06836912781)),((94440.71875, -2396.15820312, 173982.265625),(0.00601033912972, 0.000481855531689, 0.996783614159, -0.0799132436514)),]

	for n in range(6):
		tablix             = Bladex.CreateEntity("Tablilla"+`n+1`+"X","Tablilla"+`n+1`,0,0,0)
		tablix.Position    = posi[n][0]
		tablix.Orientation = posi[n][1]
		tablix.CastShadows = 0
		tablix.RasterMode  = "Read"
		tablix.RemoveFromWorld()



def CreaHalosTablillasX():
	datos_halo=[((92650.03125, -2377.51391602, 173149.53125),(0.519028127193, 0.0416110567749, 0.851013183594, -0.0682266652584)),
			((92596.0390625, -2389.875, 171159.5),(0.860936462879, 0.069022230804, 0.502396285534, -0.0402776673436)),
			((94472.7578125, -2370.47631836, 169868.5625),(0.996801733971, 0.0799146965146, 0.0, 0.0)),
			((96278.1484375, -2372.875, 171162.46875),(0.860936462879, 0.069022230804, -0.502396285534, 0.0402776673436)),
			((96224.15625, -2355.51391602, 173152.5),(0.51610326767, 0.041376568377, -0.852790176868, 0.06836912781)),
			((94440.6953125, -2395.56518555, 173982.203125),(0.00601033912972, 0.000481855531689, 0.996783614159, -0.0799132436514))]
	for n in range(6):
		conohalotablix=Bladex.CreateEntity("ConoHaloTablilla"+`n+1`+"X", "Cono1", datos_halo[n][0][0], datos_halo[n][0][1], datos_halo[n][0][2])
		conohalotablix.Orientation=datos_halo[n][1][0], datos_halo[n][1][1], datos_halo[n][1][2], datos_halo[n][1][3]
		baseconohalotablix=Bladex.CreateEntity("BaseConoHaloTablilla"+`n+1`+"X", "BaseCono", 0, 0, 0)
		baseconohalotablix.Position=conohalotablix.Position
		baseconohalotablix.Orientation=conohalotablix.Orientation
		conohalotablix.CastShadows=baseconohalotablix.CastShadows=0
		conohalotablix.SelfIlum=baseconohalotablix.SelfIlum=1.0
		conohalotablix.Alpha=baseconohalotablix.Alpha=0.0
		conohalotablix.RasterMode=baseconohalotablix.RasterMode="AdditiveAlpha"
		conohalotablix.RasterMode=baseconohalotablix.RasterMode="Read"

def CreaTornado():
	global sonidosrayotornado
	vortice=Bladex.CreateEntity("Vortice", "Vortice1", 94375, -17000, 172000)
	corona=Bladex.CreateEntity("Corona", "Vortice2", 94375, -16500, 172000)
	vortice.Orientation=corona.Orientation=0.707107,0.707107,0.000000,0.000000
	vortice.Scale=0.4
	corona.Scale=0.45
	vortice.CastShadows=corona.CastShadows=0
	vortice.Alpha=corona.Alpha=0.0
	vortice.SelfIlum=corona.SelfIlum=1.0
	vortice.SendSectorMsgs=corona.SendSectorMsgs=0
	vortice.SendTriggerSectorMsgs=corona.SendTriggerSectorMsgs=0
	vortice.RasterMode=corona.RasterMode="AdditiveAlpha"
	vortice.RasterMode=corona.RasterMode="Read"
	rayot=Bladex.CreateEntity("RayoTornado", "Entity ElectricBolt",345700.0, 3081.0, -5062.0)
	rayot.Target=326229, 3678, 14665
	rayot.MaxAmplitude=400.0
	rayot.MinSectorLength=1000000.0
	rayot.Active=0
	rayot.Damage=0
	InitDataField.Initialise(rayot)
	rayot.Data.Active=0
	rayot.Data.Frecuency=1.5
	rayot.Data.FrecuencyVariation=1.45
	xl, yl, zl = (rayot.Position[0]+rayot.Target[0])/2.0, (rayot.Position[1]+rayot.Target[1])/2.0, (rayot.Position[2]+rayot.Target[2])/2.0
	luzrayot=Bladex.CreateEntity("LuzRayoTornado", "Entity Spot", xl, yl, zl)
	luzrayot.Color=60, 170, 255
	luzrayot.Intensity=0.0
	luzrayot.Precission=0.06
	luzrayot.Visible=0
	luzrayot.CastShadows=0
	soundrayot1=Bladex.CreateEntity("SonidoRayoTornado1", "Entity Sound", xl, yl, zl)
	soundrayot1.SetSound("../../Sounds/M-IMPACTO-FUEGO2.wav")
	soundrayot1.Volume=1.0
	soundrayot1.MinDistance=15000
	soundrayot1.MaxDistance=30000
	soundrayot2=Bladex.CreateEntity("SonidoRayoTornado2", "Entity Sound", xl, yl, zl)
	soundrayot2.SetSound("../../Sounds/M-IMPACTO-FUEGO.wav")
	soundrayot2.Volume=1.0
	soundrayot2.MinDistance=15000
	soundrayot2.MaxDistance=30000
	soundrayot3=Bladex.CreateEntity("SonidoRayoTornado3", "Entity Sound", xl, yl, zl)
	soundrayot3.SetSound("../../Sounds/M-IMPACTO-FUEGO2.wav")
	soundrayot3.Volume=1.0
	soundrayot3.MinDistance=15000
	soundrayot3.MaxDistance=30000
	soundrayot4=Bladex.CreateEntity("SonidoRayoTornado4", "Entity Sound", xl, yl, zl)
	soundrayot4.SetSound("../../Sounds/M-IMPACTO-FUEGO.wav")
	soundrayot4.Volume=1.0
	soundrayot4.MinDistance=15000
	soundrayot4.MaxDistance=30000
	soundrayot5=Bladex.CreateEntity("SonidoRayoTornado5", "Entity Sound", xl, yl, zl)
	soundrayot5.SetSound("../../Sounds/M-IMPACTO-FUEGO2.wav")
	soundrayot5.Volume=1.0
	soundrayot5.MinDistance=15000
	soundrayot5.MaxDistance=30000
	soundrayot6=Bladex.CreateEntity("SonidoRayoTornado6", "Entity Sound", xl, yl, zl)
	soundrayot6.SetSound("../../Sounds/M-IMPACTO-FUEGO.wav")
	soundrayot6.Volume=1.0
	soundrayot6.MinDistance=15000
	soundrayot6.MaxDistance=30000
	sonidosrayotornado=[soundrayot1, soundrayot2, soundrayot3, soundrayot4, soundrayot5, soundrayot6]

def CreaLuzFinal():
	global luzfIN
	luzfIN=Bladex.CreateEntity("LuzfIN","Entity Spot",94400,-7000,171900)
	luzfIN.Color=101,176,94
	luzfIN.Intensity=30.0
	luzfIN.CastShadows=0
	luzfIN.Precission=0.1
	luzfIN.Visible=0
	luzfIN.Flick=0

def CT(numero1,numero2):
	char = Bladex.GetEntity("Player1")
	inv  = char.GetInventory()
	for n in range(numero1,numero2):
		inv.AddTablet("Tablilla"+`n+1`)

def CTT():
	CT(0,6)

def C2T():
	CT(0,2)

def C4T():
	CT(2,6)

def repite():
	global TabliState
	global BladeReady
	global BladeSword
	global bladesword
	global bladeswordadd
	global chbladesword
	global bladeswordA
	global luzimp
	TabliState = [0,0,0,0,0,0]
	BladeReady = 0
	BladeSword.Alpha = 0.0
	Actions.RemoveFromInventory(char, BladeSword, "Hola")
	if char.Kind[0] == "B":
		bladesword = Bladex.CreateEntity("BladeSword","BladeSwordBarbarian",94355.2677885, -3148.18632875, 172034.430763)
	else:
		bladesword = Bladex.CreateEntity("BladeSword","BladeSword",94355.2677885, -3148.18632875, 172034.430763)

	bladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
	bladesword.Static=1
	bladesword.Weapon=1

	#ItemTypes.ItemDefaultFuncs (bladesword)

	chbladesword = Bladex.CreateEntity("ChBladeSword","ChispasBladeSword",0,0,0)
	chbladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
	chbladesword.Static=1
	chbladesword.Scale=1.1
	chbladesword.CastShadows=0
	chbladesword.Alpha=0.0
	bladesword.Link(chbladesword)
	bladeswordA = Bladex.CreateEntity("BladeSword1","BladeSword",94052.251008, -4033.91838564, 172999.071657)
	bladeswordA.Orientation = 0.707107,0.707107,0.000000,0.000000
	bladeswordA.Static=1
	bladeswordA.Alpha=0.0
	bladeswordadd = Bladex.CreateEntity("BladeSwordAdd","BladeSword2Poly", 0, 0, 0)
	bladeswordadd.Orientation = 0.707107,0.707107,0.000000,0.000000
	bladeswordadd.Static=1
	bladeswordadd.Alpha=0.0
	bladeswordadd.RasterMode="AdditiveAlpha"
	bladeswordadd.RasterMode="Read"
	bladeswordadd.SelfIlum=1.0
	CreaHalosTablillasX()
	cilar.Scale=1.0
	cilab.Scale=1.0
	cilgo.Scale=1.0
	cilar.Alpha=0.0
	cilab.Alpha=0.0
	cilgo.Alpha=0.0
	luzimp.Intensity=0.0

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para ChaosKnight.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def kSceneOpenDoors():
	global kSceneOpenDoorsStartTime
	kSceneOpenDoorsStartTime=Bladex.GetTime()
	kaosdoor1.TimerFunc=kSceneOpenDoorTimer
	kaosdoor1.SubscribeToList("kaosdoortimer")

def kSceneOpenDoorTimer(ent, time):
	time = Bladex.GetTime()
	time = time - kSceneOpenDoorsStartTime
	delta = (3.14159/2.0)/(kSceneOpenDoorsTime/kSceneOpenDoorsPrec)
	kaosdoor1.RotateRel(0,0,0,0,0,1,-delta)
	kaosdoor2.RotateRel(0,0,0,0,0,1, delta)
	if (time>kSceneOpenDoorsTime):
		kaosdoor1.RemoveFromList("kaosdoortimer")
		kaosdoor1.TimerFunc=""


###############
#   Eventos   #
###############


def ChaosDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	chaos = Bladex.GetEntity(VictimName)
	Damage.CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
	if chaos.Life < 800:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, Bladex.TriggerEvent, (36,))
		Bladex.GetEntity("Player1").SetActiveEnemy("")
		chaos.ImDeadFunc(VictimName)
		chaos.DamageFunc = ""


#####################
#     Aparicion     #
#####################

def DetenCamaraApChk(Camera,frame):
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	Scorer.SetVisible(1)
	Bladex.SetListenerPosition(1)
	ScriptSkip.SkipScriptEnd()
	Bladex.ExeMusicEvent(-1)
	#Bladex.ActivateInput()

def MueveCamaraChk(sector_index, entity_name):
	global prevtpos
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("aparicionchaos"))
		darfuncs.UnhideBadGuy(chaosk1.Name)
		chaosk1.Data.Appear()
		darfuncs.LaunchMaxCamera("Palacio_Camera_chaos.cam",0,-1,DetenCamaraApChk)
		sectorcamarachk.OnEnter =""
		Scorer.SetVisible(0)
		Bladex.SetListenerPosition(2)
		ScriptSkip.SkipScriptStart("EscenaApChk")


##################
#     Muerte     #
##################


def ReiniciaCamaraChaosK1():
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	cam.Cut()
	ScriptSkip.SkipScriptEnd()
	#Bladex.ActivateInput()
	Bladex.SetListenerPosition(1)
	Scorer.SetVisible(1)

def GiraCamara(obj_name, time):
	global paso_n
	global chaospos
	global init_tpos
	cam=Bladex.GetEntity("Camera")
	vtpos=init_tpos[0]-chaospos[0], 0.0, init_tpos[2]-chaospos[2]
	vtposnorm=B3DLib.Normalize(vtpos)
	paso_n=paso_n+1
	newvtposnorm=vtposnorm[0]*math.cos(paso_n*ANGLE_VARIATION)-vtposnorm[2]*math.sin(paso_n*ANGLE_VARIATION), 0.0, vtposnorm[0]*math.sin(paso_n*ANGLE_VARIATION)+vtposnorm[2]*math.cos(paso_n*ANGLE_VARIATION)
	newvtpos=newvtposnorm[0]*2000, 0.0, newvtposnorm[2]*2000
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	if paso_n==TOTAL_STEPS:
		cam.RemoveFromList("Timer60")
		cam.TimerFunc=""
		ReiniciaCamaraChaosK1()

def MuereChaosK1(entity_name):
	global paso_n
	global chaospos
	global init_tpos
	Bladex.SetListenerPosition(2)
	Scorer.SetVisible(0)
	ScriptSkip.SkipScriptStart("EscenaDesapChk")
	#Bladex.DeactivateInput()
	chaosk1.Data.Disappear(entity_name)
	cam=Bladex.GetEntity("Camera")
	char=Bladex.GetEntity("Player1")
	charpos=char.Position
	chaospos=chaosk1.Position
	vtpos=chaospos[0]-charpos[0], 0.0, chaospos[2]-charpos[2]
	vtposnorm=B3DLib.Normalize(vtpos)
	newvtposnorm=vtposnorm[0]*math.cos(3.14159/2.0)-vtposnorm[2]*math.sin(3.14159/2.0), 0.0, vtposnorm[0]*math.sin(3.14159/2.0)+vtposnorm[2]*math.cos(3.14159/2.0)
	newvtpos=newvtposnorm[0]*2000.0, 0.0, newvtposnorm[2]*2000.0
	cam.ESource="ChaosK1"
	cam.TPos=chaospos[0]+newvtpos[0], -250.0, chaospos[2]+newvtpos[2]
	cam.SType=2
	cam.TType=0
	init_tpos=cam.TPos
	paso_n=0
	cam.TimerFunc=GiraCamara
	cam.SubscribeToList("Timer60")

	seccer2.Active = 1
	seccer3.Active = 1
	seccer4.Active = 1
	kSceneOpenDoors()

def XMcretelas(posi):
	Cimitarra116=Bladex.CreateEntity("Gladius116","Cimitarra",0,0,0)
	Cimitarra116.Weapon=1
	escudo=Bladex.CreateEntity("Escudo116","Escudo1",0,0,0)
	Sparks.MakeShield("Escudo116")
	Breakings.SetBreakableWS("Escudo116")

	pers=Bladex.CreateEntity("116ORC","Lich",posi[0],posi[1],posi[2])
	pers.Person=1
	pers.Angle=4.4
	pers.Level=5
	Actions.TakeObject(pers.Name,"Gladius116")
	Actions.TakeObject(pers.Name,"Escudo116")
	pers.ActionAreaMin=pow(2,0)
	pers.ActionAreaMax=pow(2,1)
	EnemyTypes.EnemyDefaultFuncs(pers)
	return pers
	#AniSound.AsignarSonidosOrco('16ORC')


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para cripta.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CortaCamara():
	ScriptSkip.SkipScriptEnd()
	Bladex.ExeMusicEvent(-1)

def Descubre():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("conseguido"))
	ScriptSkip.SkipScriptStart("EscenaCripta")
	if char.Position[1]<0:
		c=-34250, -3200, 42800
		t=2
	elif char.Position[2]>47100:
		c=-24100, 100, 49250
		t=3
	else:
		c=-24100, 100, 44000
		t=4
	AbreCam.LastTime = 0
	AbreCam.PTS = [ (c                    , char.Position         , 2                    ),
			   ((-34750, -5000, 56200), (-33400, -1650, 65700), t, puertacer.OpenDoor),
			   ((-34750, -5300, 56200), (-33400, -1500, 65700), 3,                   ),
			   ((-21749, 3162, 49829) , (-23250, 5300, 55000) , 3, skalon            ),
			   ((-23451, 6591, 50223) , (-23548, 5300, 45919) , 6                    )]
	AbreCam.CallBack = CortaCamara
	AbreCam.AbreCam()

def skalon():
	escalon1a.OpenDoor()
	escalon2a.OpenDoor()
	escalon3a.OpenDoor()
	escalon4a.OpenDoor()
	escalon5a.OpenDoor()
	escalon6a.OpenDoor()
	escalon7a.OpenDoor()
	escalon8a.OpenDoor()
	escalon9a.OpenDoor()
	escalon10a.OpenDoor()
	escalon11a.OpenDoor()
	escalon12a.OpenDoor()
	escalon13a.OpenDoor()

def RompeMuroFalso(sector_index, entity_name, px, py, pz, ximpulse, yimpulse, zimpulse, x_norm, y_norm, z_norm,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
	sonidoroturamurofalso.Play(-24250, -1750, 33250, 0)
	sectormurofalso.DoBreak((0.0, -0.5, 2.5), (px, py, pz), (0.0, 0.0, 0.0))
	sectorrompemurofalso.OnHit=""

def AbreZonaSecreta():
	vigaseccen.Move(0,3250,0)
	vigasecder.Move(0,-2750,0)
	vigasecizq.Move(0,-2750,0)

def Tapa():
	escalon1a.CloseDoor()
	puertacer.CloseDoor()
	escalon2a.CloseDoor()
	escalon3a.CloseDoor()
	escalon4a.CloseDoor()
	escalon5a.CloseDoor()
	escalon6a.CloseDoor()
	escalon7a.CloseDoor()
	escalon8a.CloseDoor()
	escalon9a.CloseDoor()
	escalon10a.CloseDoor()
	escalon11a.CloseDoor()
	escalon12a.CloseDoor()
	escalon13a.CloseDoor()

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para paguas.py          **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

def CierraPuertaNegra():
	if puertaNEGRA.status==Doors.OPENED:
		puertaNEGRA.CloseDoor()
		puertaNEGRA2.CloseDoor()

def AbrepuertaNEGRA():
	puertaNEGRA.OpenDoor()
	puertaNEGRA2.OpenDoor()

def Abrep1():
	puerta1a.OpenDoor()
	puerta2a.OpenDoor()

def Abresub():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("conseguido"))
	ScriptSkip.SkipScriptStart("EscenaPuertasSub")
	AbreCam.LastTime = 0
	AbreCam.PTS = [((3338.25771341, 10225.9186139, 216535.188351), (3864.6298929, 9947.17891221, 216565.74585), 3),
			   ((3317.39728976, 11259.1956045, 216310.278291), (4414.4957069, 10058.0702485, 216368.857725), 3),
			   ((3317.39728976, 11259.1956045, 216310.278291), (4414.4957069, 10058.0702485, 216368.857725), 3)]
	AbreCam.CallBack = CortaCamara
	AbreCam.AbreCam()
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3, puertasub1.OpenDoor, ())
	Bladex.AddScheduledFunc(Bladex.GetTime() + 3, puertasub2.OpenDoor, ())

def Abrepuerta4():
	puerta4.OpenDoor()

def AbrepuertaRANA():
	puertaRANA.OpenDoor()
	puertaRANA1.OpenDoor()

def AbrepuertaGOL():
	puertaGOL.OpenDoor()


#*************************************************************************************************
#*******************************     Definiciones para Fires.py         **************************
#*************************************************************************************************


def EnciendeAltarFires(FireName,PosFire,cabezon_name):
	llamarada=Bladex.CreateEntity(FireName, "Entity Particle System D1", PosFire[0],PosFire[1],PosFire[2])
	llamarada.ParticleType="Flame"+cabezon_name
	llamarada.YGravity=-4000.0
	llamarada.Friction=0.12
	llamarada.PPS=300
	llamarada.Velocity=0.0, -2500.0, 0.0
	llamarada.RandomVelocity=45.0
	llamarada.Time2Live=14
	AuxFuncs.SetRadialFireDamageObject(llamarada.Name, 800.0)


def CreateFires():
	EnciendeAltarFires("Palacio_Camera_fuego1.cam",(100000,-1600,209000),"Cabezon")
	EnciendeAltarFires("Palacio_Camera_fuego2.cam",(89000,-1600,209000),"Cabezon1")
	EnciendeAltarFires("Palacio_Camera_fuego3.cam",(99750,-1600,203250),"Cabezon2")
	EnciendeAltarFires("Palacio_Camera_fuego4.cam",(89000,-1600,203250),"Cabezon3")






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

def EnciendeMusicaGenericaAntes(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("genericaantes"))

def EnciendeMusicaGenericaDespues(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("genericadespues"))

def EnciendeMusicaSuspense(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("suspense"))

def EnciendeMusicaMiserere(trsector_name, entity_name):
	if entity_name=="Player1":
		Bladex.ExeMusicEvent(Bladex.GetMusicEvent("miserere"))

###
#######  Aparicion del personaje
###

def EnciendeMusicaInicio():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("miserere"))
