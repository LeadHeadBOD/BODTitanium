##///
##||| Palace_M15/generadores.PY TITANIUM
##||| Change list:
##||| * Removed duplicate sound assignment entries to clay golems
##\\\ 

import ReadGSFile
import math
import EnmGenRnd
import B3DLib
import darfuncs

golemla=Bladex.CreateEntity("golemla","Golem_clay",-25182.466, -165.2, 6699.99,"Person")
golemla.Level=8
golemla.Angle=3.5
EnemyTypes.EnemyDefaultFuncs(golemla)
golemla.SetOnFloor()

GOLBAR = darfuncs.E_Grup()
GOLBAR.OnDeath = TerminanLasMuertes

GOLBAR.AddGuy("golemla")

###########

golemla2=Bladex.CreateEntity("golemla2","Golem_clay",45182.466, -1065.2, 262699.99,"Person")
golemla2.Level=12
golemla2.Angle=6.2
EnemyTypes.EnemyDefaultFuncs(golemla2)
golemla2.SetOnFloor()

"""
#char.Position = -26315.4249668, -1223.90439316, -37016.8

Bladex.ReadAlphaBitMap("../../Data/Bubble.bmp","BubbleParticle")


CreateParticle(80,70,60)


Esp = 0



res=ReadGSFile.ReadGhostSectorFile("generador2.sf")

for igs in res:
	Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

char.SendTriggerSectorMsgs=1


generadorT1 = EnmGenRnd.CreateEnemiesGenerator(6, 2,'../../Sounds/generador-agua.wav')
generadorT1.AddPoint((-27990, 2100, -17200),("Gen1Lich_1", "Lich", "Hacha3", 0, "Escudo5", 1), "Skl_appears1",13)
generadorT1.AddPoint((-23100, 2100, -19200),("Gen1Lich_2", "Lich", "Martillo2", 0, "Escudo2", 1), "Skl_appears1",14)
generadorT1.AddPoint((-28900, 2100, -23100),("Gen1Lich_3", "Lich", "Martillo", 0, "Escudo5", 1), "Skl_appears1",13)
generadorT1.InitGenFunc=SaltaAguaGen
generadorT1.DifTime = 1.5
generadorT1.Activate()


Gen1Sec = Bladex.GetSector(-24000, -1000, -29000)
Gen1Sec.OnEnter = ActivateGen1

generadorT2 = EnmGenRnd.CreateEnemiesGenerator(6, 2,'../../Sounds/generador-agua.wav')
generadorT2.AddPoint((-16900, 2100, 5500),("Gen2Lich_1", "Lich", "Hacha3", 0, "Escudo5", 1), "Skl_appears1",12)
generadorT2.AddPoint((-22200, 2100, 5400),("Gen2Lich_2", "Lich", "Martillo", 0, "Escudo2", 1), "Skl_appears1",13)
generadorT2.AddPoint((-25700, 2100, 2200),("Gen2Lich_3", "Lich", "Martillo2", 0, "Escudo1", 1), "Skl_appears1",14)
generadorT2.InitGenFunc=SaltaAguaGen
generadorT2.DifTime = 1.5
generadorT2.Activate()
Bladex.SetTriggerSectorFunc("generador2", "OnEnter", ActivateGen2)


generadorT3 = EnmGenRnd.CreateEnemiesGenerator(6, 2,'../../Sounds/generador-agua.wav')
generadorT3.AddPoint(( 9820, 1000, 91400),("Gen3Lich_1", "Lich", "Martillo", 0, "Escudo5", 1), "Skl_appears1",14)
generadorT3.AddPoint((16600, 1000, 90000),("Gen3Lich_2", "Lich", "Martillo2", 0, "Escudo5", 1), "Skl_appears1",14)
generadorT3.AddPoint((14700, 1000, 96400),("Gen3Lich_3", "Lich", "Martillo2", 0, "Escudo2", 1), "Skl_appears1",15)
generadorT3.InitGenFunc=SaltaAguaGen
generadorT3.DifTime = 1.5
generadorT3.Activate()


Gen3Sec = Bladex.GetSector(5092, -1046, 87054)
Gen3Sec.OnEnter = ActivateGen3
"""