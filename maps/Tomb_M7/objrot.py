##///
##||| TOMB_M7/OBJROT.PY TITANIUM
##||| Change list:
##||| * Torches in the underground lich area now should be usable.
##\\\ 


import Breakings
import Actions
BoxBurnTime = 6
BoxDestroyTime = 12
import Torchs
import pocimac


Torchs.SetUsable("antorcha1",3,8,50)
Torchs.SetUsable("antorcha2",3,8,60)

Torchs.SetUsable("LEDEntity_temp312",4,7,-1)    # Added
Torchs.SetUsable("LEDEntity_temp315",4,7,-1)    # Added
Torchs.SetUsable("LEDEntity_temp326",4,3,-1)    # Added
Torchs.SetUsable("LEDEntity_temp330",3,3,-1)    # Added
Torchs.SetUsable("LEDEntity_temp333",2,3,-1)    # Added
Torchs.SetUsable("antorchaen1",3,6,-1)
Torchs.SetUsable("palangana1",3,3,-1)


Breakings.SetBreakable("tmesa1",8,12)
Breakings.SetBreakable("tmesa2",8,12)
Breakings.SetBreakable("tmesa3",8,12)
Breakings.SetBreakable("tmesa4",8,12)

#Breakings.SetBreakable("mesita1",8,12)


Breakings.SetBreakable("armero1",8,12)
Breakings.SetBreakable("armero2",8,12)
Breakings.SetBreakable("armero3",8,12)
Breakings.SetBreakable("armero4",8,12)

Breakings.SetBreakable("cofre1",8,12)



Breakings.SetBreakable("cajon1",8,12)
Actions.SetBurnable("cajon1",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon2",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("cajon2",8,12)
#
Breakings.SetBreakable("cajon3",8,12)
Actions.SetBurnable("cajon3",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon4",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("cajon4",8,12)
#
Breakings.SetBreakable("cajon5",8,12)
Actions.SetBurnable("cajon5",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon6",8,12)
Actions.SetBurnable("cajon6",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon7",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("cajon7",8,12)
#
Breakings.SetBreakable("cajon8",8,12)
Actions.SetBurnable("cajon8",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon9",8,12)
Actions.SetBurnable("cajon9",BoxBurnTime,BoxDestroyTime)
#
queso=Breakings.CreateHiddenObject("queso1", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso1")
Breakings.SetBreakable("cajon10",10,20,"queso1")
Actions.SetBurnable("cajon10",BoxBurnTime,BoxDestroyTime)
#

queso=Breakings.CreateHiddenObject("queso2", "Hogaza",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso2")
Breakings.SetBreakable("cajon11",10,20,"queso2")
Actions.SetBurnable("cajon11",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon12",8,12)
Actions.SetBurnable("cajon12",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon13",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("cajon13",8,12)





queso=Breakings.CreateHiddenObject("queso3", "Queso",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso3")
Breakings.SetBreakable("cajon14",10,20,"queso3")
Actions.SetBurnable("cajon14",BoxBurnTime,BoxDestroyTime)
#
queso=Breakings.CreateHiddenObject("queso4", "Paletilla",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
queso.Solid=1
queso.Static=0
pocimac.CreateFood("queso4")
Breakings.SetBreakable("cajon15",8,12,"queso4")
Actions.SetBurnable("cajon15",BoxBurnTime,BoxDestroyTime)





Breakings.SetBreakable("cajon16",8,12)
Actions.SetBurnable("cajon16",BoxBurnTime,BoxDestroyTime)
#

Breakings.SetBreakable("cajon17",8,12)
Actions.SetBurnable("cajon17",BoxBurnTime,BoxDestroyTime)
#

#en el patio pequenyo
Breakings.SetBreakable("cajon18",8,12)
Actions.SetBurnable("cajon18",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon19",8,12)
Actions.SetBurnable("cajon19",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("cajon20",8,12)
Actions.SetBurnable("cajon20",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon21",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("cajon22",BoxBurnTime,BoxDestroyTime)
#


Breakings.SetBreakable("barril1",8,12)
Actions.SetBurnable("barril1",BoxBurnTime,BoxDestroyTime)
#
Actions.SetBurnable("barril2",BoxBurnTime,BoxDestroyTime)
Breakings.SetBreakable("barril2",8,12)
#
Breakings.SetBreakable("barril3",8,12)
Actions.SetBurnable("barril3",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril4",8,12)
Actions.SetBurnable("barril4",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril5",8,12)
Actions.SetBurnable("barril5",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril6",8,12)
Actions.SetBurnable("barril6",BoxBurnTime,BoxDestroyTime)
#
Breakings.SetBreakable("barril7",8,12)
Actions.SetBurnable("barril7",BoxBurnTime,BoxDestroyTime)
#

Breakings.SetBreakable("skeleto1",8,12)
Breakings.SetBreakable("skeleto2",8,12)
Breakings.SetBreakable("skeleto3",8,12)


#Bladex.AddCombustionDataFor("Caja_i_i", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("Cajon2", "LargeFire", 250, 400, 4, 1, 1, (BoxBurnTime+BoxDestroyTime)*2)
Bladex.AddCombustionDataFor("CajonPieza1", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza2", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza3", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza4", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza5", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza6", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza7", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza8", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza9", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza10", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza11", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza12", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza13", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza14", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza15", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza16", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza17", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("CajonPieza18", "LargeFire", 250, 400, 4, 1, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("Barril", "LargeFire", 250, 400, 4, 1.5, 1, (BoxBurnTime+BoxDestroyTime)*3)
Bladex.AddCombustionDataFor("BarrilPieza1", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza2", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza3", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza4", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza5", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)
Bladex.AddCombustionDataFor("BarrilPieza6", "Fire", 250, 400, 4, 0.5, 10, BoxDestroyTime*3)


#####################################	FUEGO QUE QUEMA
import darfuncs
import ReadGSFile
# leer los sectores fantasma

res=ReadGSFile.ReadGhostSectorFile("fuego.sf")
for igs in res:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

# asignarles el fuego
darfuncs.FireOnGS("fuego1")
