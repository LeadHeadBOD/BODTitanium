##///
##||| Palace_M15/GEnems.PY TITANIUM
##||| Change list:
##||| * OrkController 
##\\\ 

import Reference
import pocimac
import Select
import Doors
import Change
import Actions
import EnemyTypes
#import AniSound
import Sparks
from math import pow
import Breakings
import persPath
import darfuncs

### Orc controller
import OrkController
darkOrk_thresh = 15
goldOrk_thresh = 18
Orkk = OrkController.MinorOrk(darkOrk_thresh,goldOrk_thresh)
#

######### orcs despues de la tercera llave


#1

pers=Bladex.CreateEntity("01ORC",Orkk,65358.9537731, 1637.94028879, 87911.212031,"Person")
pers.Level=17
pers.Angle=6.07235136458
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada01","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PotionO1","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo01","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo1")


#2

pers=Bladex.CreateEntity("02ORC",Orkk,90398.4797181, 1640.27841729, 85606.4832058,"Person")
pers.Level=17
pers.Angle=0.0407268200763
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada02","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PotionO2","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo02","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo1")


darfuncs.EnterSecEvent(79462.3411219, 887.75921151, 116589.773186,corredorcs)


## orcos pelotudos




Inicio0 = darfuncs.E_Grup()



#1


pers=Bladex.CreateEntity("1ORC",Orkk,83971.670379, 2399.46610513, 56888.8393195,"Person")
pers.Level=17
pers.Angle=1.47971122503
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada1","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo1","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo1")
Inicio0.AddGuy(pers.Name)



#2

pers=Bladex.CreateEntity("2ORC",Orkk,73426.2722423, 2377.96665149, 49820.9101288,"Person")
pers.Level=17
pers.Angle=4.73881549379
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada2","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo2","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO3","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo1")
Inicio0.AddGuy(pers.Name)



#3


pers=Bladex.CreateEntity("3ORC","Great_Ork",83650.9111551, 2402.23174569, 41823.4715237,"Person")
pers.Level=17
pers.Angle=1.42637607375
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada3","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo3","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PalacePotionO4","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo1")
Inicio0.AddGuy(pers.Name)




darfuncs.EnterSecEvent(78317.2873722, 2220.25296718, 76491.6439659,AparecenOrcosPelotudos)



## orcos pelotudos II contingentes con los anteriores


#1

pers=Bladex.CreateEntity("4ORC","Great_Ork",38117.9281597, 124.251368367, 47623.6158434,"Person")
pers.Level=17
pers.Angle=3.23871204389
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()


sword=Bladex.CreateEntity("PalaceEspada4","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo4","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PalacePotionO5","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo2")

Inicio0.AddGuy(pers.Name)


#2

pers=Bladex.CreateEntity("5ORC",Orkk,29256.2109424, 122.87092282, 39240.947992,"Person")
pers.Level=17
pers.Angle=5.57377969935
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada5","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo5","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO4b","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo2")

Inicio0.AddGuy(pers.Name)


#3

pers=Bladex.CreateEntity("6ORC",Orkk,28495.3632236, 136.751816646, 46137.3139325,"Person")
pers.Level=17
pers.Angle=3.93858624967
pers.ActionAreaMin=pow(2,2)
pers.ActionAreaMax=pow(2,3)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada6","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo6","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

potion=Bladex.CreateEntity("PotionO6","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
pers.Data.JoinGroup(pers.Name, "Grupo2")

Inicio0.AddGuy(pers.Name)


## arkeros 2,4  2,5

Inicio0.HideBadGuys()

#1

pers=Bladex.CreateEntity("PalaceArq1", "Ork",-11135.0051873, -5603.26287928, 63814.0641356,"Person")
pers.Angle=3.83631882826
pers.Level=11
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada1","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow1","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver1","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#2

pers=Bladex.CreateEntity("PalaceArq2", "Ork",-5480.58655159, -7100.94485625, 35165.1217001,"Person")
pers.Angle=6.14217443981
pers.Level=11
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada2","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow2","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver2","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)



darfuncs.EnterSecEvent(42206.9507877, 131.232950205, 42712.5442662,AparecenArkeros1)


## Orkos y minorx macarra

#1


pers=Bladex.CreateEntity("PalaceArq9", "Ork",-19272.8610896, 5870.26626052, 51648.2995991,"Person")
pers.Angle=1.45568327119
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada9","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow9","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

potion=Bladex.CreateEntity("PalacePotionO7","Pocima100",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

quiver=Bladex.CreateEntity("Palacequiver9","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#2

pers=Bladex.CreateEntity("PalaceArq10", "Ork",-30723.1208861, 5884.51642847, 51330.3385699,"Person")
pers.Angle=4.70007296291
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada10","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow10","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

potion=Bladex.CreateEntity("PotionO8","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

quiver=Bladex.CreateEntity("Palacequiver10","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#minorx macarra escondido


o=Bladex.CreateEntity("Hachacarnicero","Hachacarnicero",0,0,0,"Weapon") # EgyptSword

#pers=Bladex.CreateEntity("Minot1","Great_Ork",-24388.4871043, 9764.71493146, 74217.8620991,"Person") # Minotaur
pers=Bladex.CreateEntity("Minot1","Minotaur",-24250.0, 14500.0, 101250.0,"Person") # Minotaur
pers.Level=17
pers.Angle=3.19154910268
Actions.TakeObject(pers.Name,"Hachacarnicero")
#pers.ActionAreaMin=pow(2,0)
#pers.ActionAreaMax=pow(2,1)
#pers.ActionAreaMin=pow(2,10)
#pers.ActionAreaMax=pow(2,11)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy(pers.Name)



darfuncs.EnterSecEvent(-14426.3243151, 3851.87182146, 57451.3477049,ActivaSectorDosYMedioN)



## orcos a partir primera llave


Inicio1 = darfuncs.E_Grup()

#1


pers=Bladex.CreateEntity("9ORC",Orkk,-31470.1811694, -1109.56768659, 24771.6415751,"Person")
pers.Level=17
pers.Angle=0.479141870782
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada9","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PotionO9","Pocima50",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo9","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio1.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)


#2


pers=Bladex.CreateEntity("10ORC",Orkk,-37648.7694262, -624.284016313, 65786.9694478,"Person")
pers.Level=17
pers.Angle=4.60009944162
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada10","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo10","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio1.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)


darfuncs.EnterSecEvent(-14426.3243151, 3851.87182146, 57451.3477049,ActivaSectorVuelta1)


##arkero entre llaves 1 y 2 

#1

pers=Bladex.CreateEntity("PalaceArq3", "Ork",-36909.0701843, -6135.60147169, 79463.5263845,"Person")
pers.Angle=3.39785386203
pers.Level=15
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada3","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver3","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio1.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)



##orkos en templo


#1


pers=Bladex.CreateEntity("11ORC","Great_Ork",-16749.6036378, -2128.55788771, 96526.0188461,"Person")
pers.Level=17
pers.Angle=1.61362680326
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada11","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PalacePotion10","PocimaTodo",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo11","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio1.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)



#2


pers=Bladex.CreateEntity("12ORC","Great_Ork",-32088.4912233, -2131.87545292, 96235.9383387,"Person")
pers.Level=17
pers.Angle=4.64364271668

pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada12","EgyptSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PalacePotion11","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo12","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

Inicio1.AddGuy(pers.Name)

darfuncs.HideBadGuy(pers.Name)


#3


#pers=Bladex.CreateEntity("PalaceArq4", "Ork",-23696.8917123, -8121.5326812, 91584.1209037,"Person")
#pers.Angle=3.13309344388
#pers.Level=15
#pers.ActionAreaMin=pow(2,4)
#pers.ActionAreaMax=pow(2,5)
#pers.SetOnFloor()

#sword=Bladex.CreateEntity("PalaceArcEspada4","Cimitarra",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs(sword)
#Actions.TakeObject(pers.Name,sword.Name)

#bow=Bladex.CreateEntity("Palacebow4","Arco",0,0,0,"Weapon")
#ItemTypes.ItemDefaultFuncs(bow)
#Actions.TakeObject(pers.Name,bow.Name)

#quiver=Bladex.CreateEntity("Palacequiver4","Carcaj",0,0,0,"Physic")
#ItemTypes.ItemDefaultFuncs (quiver)
#quiver.Data.SetNumberOfArrows(10, pers.Name)
#Actions.TakeObject(pers.Name,quiver.Name)
#EnemyTypes.EnemyDefaultFuncs(pers)

#Inicio1.AddGuy(pers.Name)

#darfuncs.HideBadGuy(pers.Name)


###  bichos junto a entrada que se rompe en escena orcos correteando 

#arkeros 2,0  2,1

#1


pers=Bladex.CreateEntity("PalaceArq5", "Ork",-34545.4901221, -10113.8880705, 137513.344081,"Person")
pers.Angle=3.69953883762
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada5","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow5","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver5","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#2


pers=Bladex.CreateEntity("PalaceArq6", "Ork",-17802.2974424, -8116.84639304, 138263.043905,"Person")
pers.Angle=2.73460269575
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada6","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow6","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver6","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#3


pers=Bladex.CreateEntity("PalaceArq7", "Ork",-13187.8589701, -6101.6913748, 128244.612377,"Person")
pers.Angle=2.0008959854
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada7","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow7","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver7","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)


#4


pers=Bladex.CreateEntity("PalaceArq8", "Ork",-31063.4710135, -8104.29530241, 139127.116677,"Person")
pers.Angle=3.39901383263
pers.Level=19
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceArcEspada8","Cimitarra",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

bow=Bladex.CreateEntity("Palacebow8","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(bow)
Actions.TakeObject(pers.Name,bow.Name)

quiver=Bladex.CreateEntity("Palacequiver8","Carcaj",0,0,0,"Physic")
ItemTypes.ItemDefaultFuncs (quiver)
quiver.Data.SetNumberOfArrows(10, pers.Name)
Actions.TakeObject(pers.Name,quiver.Name)
EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.HideBadGuy(pers.Name)

#minorx hijoputa

#1


o=Bladex.CreateEntity("Hachacarnicero2","Hachacarnicero",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot2","Minotaur",-16884.4723141, -1500.0, 159891.351595,"Person")
pers.Level=17
pers.Angle=1.57032396497
Actions.TakeObject(pers.Name,"Hachacarnicero2")
pers.ActionAreaMin=pow(2,8)
pers.ActionAreaMax=pow(2,9)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy(pers.Name)


darfuncs.EnterSecEvent(-14426.3243151, 3851.87182146, 57451.3477049,ActivaSectorVuelta2)


## keletos antes de zona inundada 2,0  2,1


#1

pers=Bladex.CreateEntity("15Skeleton","Skeleton",13152.0792418, 1882.23328709, 193313.77709,"Person")
pers.Angle=4.68821369045
pers.Level=14
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada15","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo15","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2


pers=Bladex.CreateEntity("16Skeleton","Skeleton",22306.0932333, 1889.10869148, 193596.73472,"Person")
pers.Angle=1.61694226906
pers.Level=14
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada16","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo16","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#3


pers=Bladex.CreateEntity("17Skeleton","Skeleton",-13589.3993897, 371.051083995, 199218.4372,"Person")
pers.Angle=4.60267110681
pers.Level=14
pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada17","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo17","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)



## caballeros negros prefinales 2,4  2,5

#1

pers=Bladex.CreateEntity("13Kngt","Dark_Knight",-21333.1579842, 822.16489307, 216403.530981,"Person")
pers.Angle=4.76293940558
pers.Level=24
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada13","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PalacePotion12","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo13","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

#potion=Bladex.CreateEntity("Potion12","Pocima200",0,0,0,"Physic")
#potion.Scale=1.220190
#pocimac.CreatePotion(potion.Name)
#Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


darfuncs.EnterSecEvent(17708.568066, 2869.77253676, 216382.906016,Final1)


#2


pers=Bladex.CreateEntity("14Kngt","Dark_Knight",-46248.0815829, 3219.69112738, 220942.859399,"Person")
pers.Angle=4.08528617004
pers.Level=24
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
pers.SetOnFloor()

sword=Bladex.CreateEntity("PalaceEspada14","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

potion=Bladex.CreateEntity("PalacePotion13","Pocima200",0,0,0,"Physic")
potion.Scale=1.220190
pocimac.CreatePotion(potion.Name)
Actions.TakeObject(pers.Name,potion.Name)

shield=Bladex.CreateEntity("PalaceEscudo14","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

#potion=Bladex.CreateEntity("Potion12","Pocima200",0,0,0,"Physic")
#potion.Scale=1.220190
#pocimac.CreatePotion(potion.Name)
#Actions.TakeObject(pers.Name,potion.Name)

EnemyTypes.EnemyDefaultFuncs(pers)

darfuncs.EnterSecEvent(-21184.3661611, 855.693321027, 216499.399983,Final2)



#minorx colega de los anteriores  2,4  2,5


o=Bladex.CreateEntity("Hachacarnicero3","Hachacarnicero",0,0,0,"Weapon")

pers=Bladex.CreateEntity("Minot3","Minotaur",-46345.2601688, 845.962188239, 232089.947361,"Person")
pers.Level=24
pers.Angle=3.11968574806
Actions.TakeObject(pers.Name,"Hachacarnicero3")
pers.ActionAreaMin=pow(2,4)
pers.ActionAreaMax=pow(2,5)
EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.EnterSecEvent(-36593.3453035, 3872.85315559, 216455.533528,Final3)




## keletos antes del final


#1

pers=Bladex.CreateEntity("18Skeleton","Skeleton",-3004.60012983, -1115.60739846, 269380.323996,"Person")
pers.Angle=4.4222
pers.Level=14
pers.SetOnFloor()
pers.InitPos=17584.6752797, -1118.09352443, 273092.32722

sword=Bladex.CreateEntity("PalaceEspada18","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo18","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)


#2

pers=Bladex.CreateEntity("19Skeleton","Skeleton",11288.5820299, -1110.79809349, 268775.561897,"Person")
pers.Angle=2.0071
pers.Level=14
pers.SetOnFloor()
pers.InitPos=16093.0215904, -1104.43000221, 273083.36944

sword=Bladex.CreateEntity("PalaceEspada19","HookSword",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(sword)
Actions.TakeObject(pers.Name,sword.Name)

shield=Bladex.CreateEntity("PalaceEscudo19","Escudo4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(shield)
Actions.TakeObject(pers.Name,shield.Name)

EnemyTypes.EnemyDefaultFuncs(pers)
