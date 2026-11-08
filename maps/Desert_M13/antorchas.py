##///
##||| Desert_M13/antorchas.PY TITANIUM
##||| Change list:
##||| * Increased light strength in the crypt to better light the area and make it actually make sense.
##\\\ 

import Torchs
import Reference

####ANTORCHAS EN LA CRIPTA
#Reference.EntitiesSelectionData[gp.Name]=(Priority,Distance,Name)

###ANTORCHAS EN PATIO TRASERO Y CRIPTA

Torchs.SetUsable("dantorcha1",3,7,50)
Torchs.SetUsable("dantorcha2",3,7,60)
Torchs.SetUsable("dantorcha3",3,7,90)
Torchs.SetUsable("dantorcha4",4,7,80)
Torchs.SetUsable("dantorcha5",4,7,60)
Torchs.SetUsable("dantorcha6",4,7,90)
Torchs.SetUsable("dantorcha7",4,7,90)
Torchs.SetUsable("dantorcha8",4,7,90)
Torchs.SetUsable("dantorcha9",4,7,90)
Torchs.SetUsable("dantorcha10",4,7,90)
Torchs.SetUsable("dantorcha11",4,7,90)


Torchs.SetUsable("antorchaen1",3,6,-1)
Torchs.SetUsable("antorchaen2",3,6,-1)
Torchs.SetUsable("antorchaen3",3,6,-1)
Torchs.SetUsable("antorchaen4",5,6,-1)  #3
Torchs.SetUsable("antorchaen5",4,6,-1)  #3
Torchs.SetUsable("antorchaen6",4,6,-1)
Torchs.SetUsable("antorchaen7",2,6,-1)
Torchs.SetUsable("antorchaen8",3,6,-1)
Torchs.SetUsable("antorchaen9",4,6,-1)  # 3
Torchs.SetUsable("antorchaen10",3,6,-1)


import MenuText
Reference.EntitiesSelectionData["palangana1"]=(9,4000.0,MenuText.GetMenuText("Bowl"))
Reference.EntitiesSelectionData["palangana2"]=(9,4000.0,MenuText.GetMenuText("Bowl"))
Reference.EntitiesSelectionData["palangana3"]=(9,4000.0,MenuText.GetMenuText("Bowl"))
Reference.EntitiesSelectionData["palangana4"]=(9,4000.0,MenuText.GetMenuText("Bowl"))
Reference.EntitiesSelectionData["palangana5"]=(9,4000.0,MenuText.GetMenuText("Bowl"))


Torchs.SetUsable("palangana1",3,3,-1)
Torchs.SetUsable("palangana2",3,3,-1)
Torchs.SetUsable("palangana3",5,3,-1)
Torchs.SetUsable("palangana4",5,3,-1)
Torchs.SetUsable("palangana5",4,3,-1)


##apaga antorchas en la cripta

Apagala1Sec = Bladex.GetSector(-27026.5129399, 9195.3797359, -15258.4791667)
Apagala1Sec.OnEnter = Apagala

