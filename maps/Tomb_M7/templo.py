import EnemyTypes
#-ESQUELETOS EN EL TEMPLO----

NumKeletumVitaEst = 4
		
	

#--PLANTA-BAJA-IZQUIERDA---
#1
o=Bladex.CreateEntity("TombEspada1t","Hacha5",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
o=Bladex.CreateEntity("TombEscudo1t","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("SKLt1","Skeleton",10500,-1300,11875,"Person")
pers.Level=5
pers.Angle=-3.1415/2
pers.Position = 10500,-1771,11875
Actions.TakeObject(pers.Name,"TombEspada1t")
Actions.TakeObject(pers.Name,"TombEscudo1t")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.RemoveFromWorld()
pers.ImDeadFunc = deKeletum

#2
Espada2t=Bladex.CreateEntity("TombEspada2t","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
escudo=Bladex.CreateEntity("TombEscudo2t","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("SKLt2","Skeleton",28000,-1300,11875,"Person")
pers.Level=5
pers.Angle=3.1415/2
pers.Position = 28000,-1771,11875
Actions.TakeObject(pers.Name,"TombEspada2t")
Actions.TakeObject(pers.Name,"TombEscudo2t")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.RemoveFromWorld()
pers.ImDeadFunc = deKeletum

#--PLANTA-BAJA-DERECHA---

#3
o=Bladex.CreateEntity("TombEspada3t","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
escudo=Bladex.CreateEntity("TombEscudo3t","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)


pers=Bladex.CreateEntity("SKLt3","Skeleton",10750,-1300,-15125,"Person")
pers.Level=5
pers.Angle=-3.1415/2
pers.Position = 10750,-1771,-15125
Actions.TakeObject(pers.Name,"TombEspada3t")
Actions.TakeObject(pers.Name,"TombEscudo3t")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
pers.RemoveFromWorld()
pers.ImDeadFunc = deKeletum

#4
Espada4t=Bladex.CreateEntity("TombEspada4t","Hacha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
escudo=Bladex.CreateEntity("TombEscudo4t","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)

pers=Bladex.CreateEntity("SKLt4","Skeleton",28000,-1300,-14975,"Person")
pers.Level=5
pers.Angle=3.1415/2
pers.Position = 28000,-1771,-14975
pers.RemoveFromWorld()
pers.ImDeadFunc = deKeletum
Actions.TakeObject(pers.Name,"TombEspada4t")
Actions.TakeObject(pers.Name,"TombEscudo4t")
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)



EsqueletSec1=Bladex.GetSector(11812, -2000, 12000)
EsqueletSec1.Active = 0
EsqueletSec1.InitBreak((150,0,0),(0,1000,0),(0, 200,700),'piedra pesada')


EsqueletSec2=Bladex.GetSector(26312, -2000, 12000)
EsqueletSec2.Active = 0
EsqueletSec2.InitBreak((150,0,0),(0,1000,0),(0, 200,700),'piedra pesada')

EsqueletSec3=Bladex.GetSector(12392, -2000, -15000)
EsqueletSec3.Active = 0
EsqueletSec3.InitBreak((150,0,0),(0,1000,0),(0, 200,700),'piedra pesada')

EsqueletSec4=Bladex.GetSector(26312, -2000, -15000)
EsqueletSec4.Active = 0
EsqueletSec4.InitBreak((150,0,0),(0,1000,0),(0, 200,700),'piedra pesada')

    
    
ActivaLosEsqueletos = 0
    
       

SectorEsqueletosAC=Bladex.GetSector(20000, -2000, 0)
SectorEsqueletosAC.OnEnter = Abretelas
