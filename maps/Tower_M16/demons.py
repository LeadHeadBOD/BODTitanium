##///
##||| Tower_M16/demons.PY TITANIUM
##||| Change list:
##||| * Removed duplicate sound assignments to the demons and lava golem
##\\\ 

import Bladex
import EnemyTypes
import AniSound
import PhantonFX





RugidoDemonio=Sounds.CreateEntitySound("../../Sounds/M-rugido-demon.wav", "RugidoDemonio")
RugidoDemonio.Volume=1
RugidoDemonio.MinDistance=10000
RugidoDemonio.MaxDistance=90000

FireBallCool=Sounds.CreateEntitySound("../../Sounds/fireball-swing.wav","Fireball")
FireBallCool.Volume=1
FireBallCool.MinDistance=10000
FireBallCool.MaxDistance=90000


##se crean los demonios

#1
demoniox=Bladex.CreateEntity("demoniox","Little_Demon",-16417.7, -48549.6, 3497.0,"Person")
demoniox.Level=11
demoniox.Angle=4.5
EnemyTypes.EnemyDefaultFuncs(demoniox)
demoniox.Blind = 1
demoniox.Deaf  = 1
demoniox.SetOnFloor()

demoniox.Freeze()
demoniox.Alpha = 0.0
demoniox.RemoveFromWorld()

#2
demonioxx=Bladex.CreateEntity("demonioxx","Little_Demon",-16554.82, -48548.0, 14394.35,"Person")
demonioxx.Level=10
demonioxx.Angle=4.5
EnemyTypes.EnemyDefaultFuncs(demonioxx)
demonioxx.Blind = 1
demonioxx.Deaf  = 1
demonioxx.SetOnFloor()

demonioxx.Freeze()
demonioxx.Alpha = 0.0
demonioxx.RemoveFromWorld()

ELDEMOSEC=Bladex.GetSector(-5150.94087256, -47562.8163468, 9452.37270313)
ELDEMOSEC.OnEnter = ElDemonio

# CoolDemon("demoniox")
# demoniox.SubscribeToList("Pin")
# char.Position = (-5191.87789317, -47552.5969016, 9202.6848471)


#2
golemla=Bladex.CreateEntity("golemla","Golem_lava",-25182.466, -49065.2, 9699.99,"Person")
golemla.Level=10
golemla.Angle=4.5
EnemyTypes.EnemyDefaultFuncs(golemla)

darfuncs.HideBadGuy("golemla")

################################################################################################
###
###		GENERAROR DE DEMONIOS EN LA SALA DE LAS VIDRIERAS
###
################################################################################################

generadordemon = EnmGenRnd.CreateEnemiesGenerator(6, 2)
#generadordemon.Level = 7
generadordemon.CallBak = CBgeneradorD2



generadordemon.AddPoint((-6172.9, -54100, 2715.8),("daemon1", "Little_Demon", "", 0, "", 1), "",10)
generadordemon.AddPoint((-5000, -54100, 9000),("daemon5", "Little_Demon", "", 0, "", 1), "",10)
generadordemon.AddPoint((5000, -54600, 9000),("daemon6", "Little_Demon", "", 0, "", 1), "",10)
generadordemon.AddPoint((-7373.36, -54100, 16201.7),("daemon2", "Little_Demon", "", 0, "", 1), "",11)
generadordemon.AddPoint((3528.5, -54600, 15341.6),("daemon3", "Little_Demon", "", 0, "", 1), "",12)
generadordemon.AddPoint((4991.0, -54600, 5897.9),("daemon4", "Little_Demon", "", 0, "", 1), "",13)

generadordemon.InitGenFunc=AparicionDemonioGenerado
generadordemon.DifTime = 0.025
generadordemon.FinishGenFunc = finGeneradaemons
generadordemon.Activate()


darfuncs. EnterSecEvent(4991.0, -55477.1, 2500,Startgendaemon)